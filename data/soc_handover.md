# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T10:38:17Z |
| **Shift Time** | 10:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **118** |
| Confirmed Threats | **93** |
| False Positives Filtered | **25** (21.2%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **22** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **165** |
| Unique Credential Pairs | **152** |
| Unique Usernames | **7** |
| Unique Passwords | **149** |
| Successful Auth Pairs | **160** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 144 |
| `support` | 9 |
| `unknown` | 5 |
| `blank` | 3 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwerty` | 6 |
| `support` | 4 |
| `unknown9` | 3 |
| `P@ssword` | 3 |
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 4 |
| `unknown` | `unknown9` | 3 |
| `support` | `qwerty` | 3 |
| `blank` | `qwerty` | 3 |
| `unknown` | `666` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `asd@qaz` | `10.0.0.73` | 2026-08-09T06:55:10 |
| `unknown` | `unknown9` | `10.0.0.73` | 2026-08-09T06:55:25 |
| `root` | `Admin...123` | `10.0.0.73` | 2026-08-09T06:55:59 |
| `root` | `123!@#123!@#` | `10.0.0.73` | 2026-08-09T06:56:40 |
| `root` | `Cli3ntServer!` | `10.0.0.73` | 2026-08-09T06:56:54 |
| `root` | `321ewq` | `10.0.0.73` | 2026-08-09T06:58:16 |
| `root` | `admin_login` | `10.0.0.73` | 2026-08-09T06:58:49 |
| `root` | `Qwe.ASD.123456` | `10.0.0.73` | 2026-08-09T07:00:02 |
| `root` | `Server@@` | `10.0.0.73` | 2026-08-09T07:00:10 |
| `root` | `Office123.` | `10.0.0.73` | 2026-08-09T07:00:43 |
| `support` | `support` | `10.0.0.73` | 2026-08-09T07:02:56 |
| `root` | `123zxc!@#` | `10.0.0.73` | 2026-08-09T07:03:17 |
| `root` | `p@ssword@2012` | `10.0.0.73` | 2026-08-09T07:03:35 |
| `root` | `De$kt0p123` | `10.0.0.73` | 2026-08-09T07:03:50 |
| `root` | `123456,.` | `10.0.0.73` | 2026-08-09T07:04:04 |
| `root` | `1q2w3e4r5t*` | `10.0.0.73` | 2026-08-09T07:04:06 |
| `root` | `!QAZ123` | `10.0.0.73` | 2026-08-09T07:05:07 |
| `root` | `win!2012` | `10.0.0.73` | 2026-08-09T07:05:13 |
| `root` | `@dm1n0` | `10.0.0.73` | 2026-08-09T07:05:22 |
| `root` | `!.Q` | `10.0.0.73` | 2026-08-09T07:05:56 |
| `root` | `Passowrd!` | `10.0.0.73` | 2026-08-09T07:06:08 |
| `root` | `Abbc123` | `10.0.0.73` | 2026-08-09T07:06:49 |
| `root` | `!23456@Admin` | `10.0.0.73` | 2026-08-09T07:07:05 |
| `root` | `p@55word!.` | `10.0.0.73` | 2026-08-09T07:08:15 |
| `root` | `!Admin$$` | `10.0.0.73` | 2026-08-09T07:08:40 |
| `root` | `123Asd456` | `10.0.0.73` | 2026-08-09T07:09:08 |
| `root` | `@dmin@i234` | `10.0.0.73` | 2026-08-09T07:10:31 |
| `root` | `root1` | `182.76.71.82` | 2026-08-09T07:11:24 |
| `root` | `321qaz321wsx` | `10.0.0.73` | 2026-08-09T07:12:33 |
| `unknown` | `unknown9` | `103.251.143.14` | 2026-08-09T07:12:58 |
| `unknown` | `unknown9` | `103.174.80.40` | 2026-08-09T07:13:10 |
| `root` | `zxc!@#$` | `10.0.0.73` | 2026-08-09T07:13:13 |
| `root` | `123123Aa` | `10.0.0.73` | 2026-08-09T07:16:51 |
| `root` | `adm!n!$tr@t0r` | `10.0.0.73` | 2026-08-09T07:17:08 |
| `root` | `111111` | `2.57.122.209` | 2026-08-09T07:17:46 |
| `root` | `passqwe12345` | `10.0.0.73` | 2026-08-09T07:17:47 |
| `root` | `user_ip` | `10.0.0.73` | 2026-08-09T07:18:01 |
| `root` | `Qwerty!QAZ` | `10.0.0.73` | 2026-08-09T07:18:37 |
| `root` | `P@ssw0rd)!@#` | `10.0.0.73` | 2026-08-09T07:18:57 |
| `root` | `R00tRoot!` | `10.0.0.73` | 2026-08-09T07:19:24 |
| `root` | `@server@` | `10.0.0.73` | 2026-08-09T07:20:11 |
| `root` | `#server#` | `10.0.0.73` | 2026-08-09T07:20:16 |
| `root` | `!server!` | `10.0.0.73` | 2026-08-09T07:20:30 |
| `support` | `qwerty` | `122.170.99.195` | 2026-08-09T07:20:40 |
| `root` | `123` | `2.57.122.209` | 2026-08-09T07:20:48 |
| `root` | `Changeme` | `10.0.0.73` | 2026-08-09T07:22:01 |
| `root` | `backupserver123` | `10.0.0.73` | 2026-08-09T07:22:47 |
| `root` | `backup123` | `10.0.0.73` | 2026-08-09T07:23:15 |
| `root` | `123123` | `2.57.122.209` | 2026-08-09T07:23:53 |
| `root` | `Zxc123456` | `10.0.0.73` | 2026-08-09T07:24:15 |
| `root` | `123qweAsd` | `10.0.0.73` | 2026-08-09T07:24:22 |
| `root` | `1Qaz2wsx` | `10.0.0.73` | 2026-08-09T07:25:29 |
| `root` | `11223344` | `10.0.0.73` | 2026-08-09T07:26:44 |
| `root` | `123321` | `2.57.122.209` | 2026-08-09T07:26:55 |
| `unknown` | `666` | `10.0.0.73` | 2026-08-09T07:27:00 |
| `root` | `ASDF@1234` | `10.0.0.73` | 2026-08-09T07:27:20 |
| `root` | `Abc123$$` | `10.0.0.73` | 2026-08-09T07:27:41 |
| `root` | `Qa123456` | `10.0.0.73` | 2026-08-09T07:29:49 |
| `root` | `1234` | `2.57.122.209` | 2026-08-09T07:29:51 |
| `root` | `data@123` | `10.0.0.73` | 2026-08-09T07:30:03 |
| `root` | `!QAZ2wsx#` | `10.0.0.73` | 2026-08-09T07:31:38 |
| `root` | `!qaz2ws` | `10.0.0.73` | 2026-08-09T07:32:04 |
| `root` | `12345` | `2.57.122.209` | 2026-08-09T07:32:47 |
| `root` | `102030405060` | `10.0.0.73` | 2026-08-09T07:33:38 |
| `root` | `Admin12!@` | `10.0.0.73` | 2026-08-09T07:34:40 |
| `root` | `!q2w3e4r` | `10.0.0.73` | 2026-08-09T07:34:46 |
| `root` | `P@$$wOrd` | `10.0.0.73` | 2026-08-09T07:36:08 |
| `support` | `qwerty` | `31.173.29.136` | 2026-08-09T07:37:07 |
| `support` | `qwerty` | `121.189.226.81` | 2026-08-09T07:37:15 |
| `root` | `Pass12` | `10.0.0.73` | 2026-08-09T07:37:56 |
| `root` | `A@12345` | `10.0.0.73` | 2026-08-09T07:38:07 |
| `root` | `1234567` | `2.57.122.209` | 2026-08-09T07:38:25 |
| `root` | `Password!!` | `10.0.0.73` | 2026-08-09T07:38:50 |
| `root` | `123-qwe` | `10.0.0.73` | 2026-08-09T07:39:24 |
| `root` | `Passw0rd123!` | `10.0.0.73` | 2026-08-09T07:40:55 |
| `root` | `12345678` | `2.57.122.209` | 2026-08-09T07:41:14 |
| `root` | `a123456+` | `10.0.0.73` | 2026-08-09T07:41:56 |
| `root` | `Hik12345` | `10.0.0.73` | 2026-08-09T07:42:17 |
| `root` | `123456789` | `2.57.122.209` | 2026-08-09T07:44:05 |
| `root` | `1234QWER` | `10.0.0.73` | 2026-08-09T07:44:11 |
| `root` | `!QAZ2was` | `10.0.0.73` | 2026-08-09T07:44:53 |
| `root` | `1q2w3e4` | `10.0.0.73` | 2026-08-09T07:45:33 |
| `unknown` | `666` | `222.99.52.202` | 2026-08-09T07:45:48 |
| `root` | `1234abcd` | `2.57.122.209` | 2026-08-09T07:46:45 |
| `root` | `Welcome1!` | `10.0.0.73` | 2026-08-09T07:46:58 |
| `root` | `abcd1234*` | `10.0.0.73` | 2026-08-09T07:47:53 |
| `root` | `Welkom1!` | `10.0.0.73` | 2026-08-09T07:48:00 |
| `root` | `Welkom@1234` | `10.0.0.73` | 2026-08-09T07:48:07 |
| `root` | `passwort` | `10.0.0.73` | 2026-08-09T07:48:13 |
| `root` | `qazWSX` | `10.0.0.73` | 2026-08-09T07:48:27 |
| `root` | `Passwort123` | `10.0.0.73` | 2026-08-09T07:49:07 |
| `root` | `123abc` | `2.57.122.209` | 2026-08-09T07:49:27 |
| `root` | `asdf.1234` | `10.0.0.73` | 2026-08-09T07:50:28 |
| `root` | `password012` | `10.0.0.73` | 2026-08-09T07:50:52 |
| `root` | `Password2014` | `10.0.0.73` | 2026-08-09T07:51:55 |
| `root` | `123qwe` | `2.57.122.209` | 2026-08-09T07:52:00 |
| `root` | `Admin06` | `10.0.0.73` | 2026-08-09T07:52:13 |
| `blank` | `qwerty` | `43.248.213.232` | 2026-08-09T07:52:56 |
| `root` | `London@123` | `10.0.0.73` | 2026-08-09T07:52:59 |
| `blank` | `qwerty` | `200.89.159.59` | 2026-08-09T07:53:04 |
| `root` | `Password007` | `10.0.0.73` | 2026-08-09T07:54:07 |
| `root` | `gianni` | `10.0.0.73` | 2026-08-09T07:54:28 |
| `root` | `1q2w3e` | `2.57.122.209` | 2026-08-09T07:54:36 |
| `support` | `P@ssword` | `115.241.228.34` | 2026-08-09T07:55:16 |
| `support` | `P@ssword` | `58.215.243.6` | 2026-08-09T07:55:33 |
| `root` | `!Password1` | `10.0.0.73` | 2026-08-09T07:55:33 |
| `root` | `1q2w3e4r` | `2.57.122.209` | 2026-08-09T07:57:09 |
| `root` | `!qazxsw2` | `10.0.0.73` | 2026-08-09T07:57:20 |
| `root` | `ab` | `10.0.0.73` | 2026-08-09T07:59:28 |
| `root` | `1qaz2wsx` | `2.57.122.209` | 2026-08-09T07:59:39 |
| `root` | `ABC` | `10.0.0.73` | 2026-08-09T07:59:59 |
| `root` | `abc@#123` | `10.0.0.73` | 2026-08-09T08:00:13 |
| `root` | `Ab12` | `10.0.0.73` | 2026-08-09T08:00:42 |
| `root` | `Ab12@` | `10.0.0.73` | 2026-08-09T08:00:51 |
| `root` | `abc@12345678` | `10.0.0.73` | 2026-08-09T08:01:45 |
| `root` | `321` | `2.57.122.209` | 2026-08-09T08:02:05 |
| `root` | `qwe123asd123` | `10.0.0.73` | 2026-08-09T08:03:46 |
| `root` | `123321A` | `10.0.0.73` | 2026-08-09T08:04:00 |
| `root` | `654321` | `2.57.122.209` | 2026-08-09T08:04:25 |
| `root` | `Pass1word` | `10.0.0.73` | 2026-08-09T08:04:39 |
| `blank` | `qwerty` | `10.0.0.73` | 2026-08-09T08:04:49 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-09T08:05:24 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-09T08:05:25 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-09T08:05:33 |
| `root` | `Server@2008` | `10.0.0.73` | 2026-08-09T08:05:34 |
| `root` | `123QWEasdzxc` | `10.0.0.73` | 2026-08-09T08:05:53 |
| `root` | `mmm123` | `10.0.0.73` | 2026-08-09T08:06:19 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-08-09T08:06:49 |
| `root` | `!Qazzaq1` | `10.0.0.73` | 2026-08-09T08:08:44 |
| `root` | `P@ssword` | `2.57.122.209` | 2026-08-09T08:09:10 |
| `root` | `Abc123@abc` | `10.0.0.73` | 2026-08-09T08:09:12 |
| `root` | `Abc123!` | `10.0.0.73` | 2026-08-09T08:09:29 |
| `root` | `Root123` | `2.57.122.209` | 2026-08-09T08:11:25 |
| `root` | `a@1234a` | `10.0.0.73` | 2026-08-09T08:11:38 |
| `root` | `asdfg12345#` | `10.0.0.73` | 2026-08-09T08:12:11 |
| `root` | `qwe12#` | `10.0.0.73` | 2026-08-09T08:12:39 |
| `root` | `password~1` | `10.0.0.73` | 2026-08-09T08:12:51 |
| `root` | `admin` | `2.57.122.209` | 2026-08-09T08:13:54 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T08:15:35 |
| `root` | `admin123` | `2.57.122.209` | 2026-08-09T08:16:00 |
| `user` | `123456654321` | `117.252.93.114` | 2026-08-09T08:20:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `45.79.181.223` | 2026-08-09T08:28:38 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-09T08:31:52 |
| `root` | `!@#qaz123` | `10.0.0.73` | 2026-08-09T08:34:15 |
| `root` | `PASSW0RD@12` | `10.0.0.73` | 2026-08-09T08:35:23 |
| `root` | `PASSW0RD_1234` | `10.0.0.73` | 2026-08-09T08:35:55 |
| `root` | `PASSW0RD_12345` | `10.0.0.73` | 2026-08-09T08:35:57 |
| `root` | `PASSWORD!@#$%` | `10.0.0.73` | 2026-08-09T08:36:06 |
| `root` | `PASSWORD..` | `10.0.0.73` | 2026-08-09T08:36:28 |
| `root` | `p@ssword.123` | `10.0.0.73` | 2026-08-09T08:37:22 |
| `root` | `aA1234` | `10.0.0.73` | 2026-08-09T08:38:23 |
| `root` | `123-ABC?` | `10.0.0.73` | 2026-08-09T08:38:48 |
| `root` | `1234asdf` | `10.0.0.73` | 2026-08-09T08:39:31 |
| `root` | `123abC` | `10.0.0.73` | 2026-08-09T08:39:53 |
| `root` | `asdf@@1234` | `10.0.0.73` | 2026-08-09T08:40:27 |
| `root` | `1234567ab` | `10.0.0.73` | 2026-08-09T08:40:41 |
| `root` | `root1234$` | `10.0.0.73` | 2026-08-09T08:41:30 |
| `root` | `inet!@#$` | `10.0.0.73` | 2026-08-09T08:41:43 |
| `root` | `12345Admin!@` | `10.0.0.73` | 2026-08-09T08:43:18 |
| `root` | `abc12@` | `10.0.0.73` | 2026-08-09T08:43:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **118** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 29 |
| OpenSSH | 16 |
| libssh | 7 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 23 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 16 | 15 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 23 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 16 | 15 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 22 | 1 | `T1082, T1592, T1078, T1083` |

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

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **48** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (41)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8efdf8e12546

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-09 07:11 |
| **Last Seen** | 2026-08-09 07:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:11:21` | `cowrie.session.connect` |
| `2026-08-09 07:11:22` | `cowrie.client.version` |
| `2026-08-09 07:11:22` | `cowrie.client.kex` |
| `2026-08-09 07:11:24` | `cowrie.login.success` |
| `2026-08-09 07:11:24` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891c851e017f

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-09 07:12 |
| **Last Seen** | 2026-08-09 07:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:12:55` | `cowrie.session.connect` |
| `2026-08-09 07:12:56` | `cowrie.client.version` |
| `2026-08-09 07:12:56` | `cowrie.client.kex` |
| `2026-08-09 07:12:58` | `cowrie.login.success` |
| `2026-08-09 07:12:58` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406618a73718

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-08-09 07:13 |
| **Last Seen** | 2026-08-09 07:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:13:08` | `cowrie.session.connect` |
| `2026-08-09 07:13:09` | `cowrie.client.version` |
| `2026-08-09 07:13:09` | `cowrie.client.kex` |
| `2026-08-09 07:13:10` | `cowrie.login.success` |
| `2026-08-09 07:13:11` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1fb96902038

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:17 |
| **Last Seen** | 2026-08-09 07:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:17:40` | `cowrie.session.connect` |
| `2026-08-09 07:17:41` | `cowrie.client.version` |
| `2026-08-09 07:17:41` | `cowrie.client.kex` |
| `2026-08-09 07:17:46` | `cowrie.login.success` |
| `2026-08-09 07:17:49` | `cowrie.session.params` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.success` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:49` | `cowrie.command.input` |
| `2026-08-09 07:17:50` | `cowrie.log.closed` |
| `2026-08-09 07:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc43baa0301f

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-09 07:20 |
| **Last Seen** | 2026-08-09 07:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:20:38` | `cowrie.session.connect` |
| `2026-08-09 07:20:38` | `cowrie.client.version` |
| `2026-08-09 07:20:38` | `cowrie.client.kex` |
| `2026-08-09 07:20:40` | `cowrie.login.success` |
| `2026-08-09 07:20:40` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8fdb564f4c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:20 |
| **Last Seen** | 2026-08-09 07:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:20:43` | `cowrie.session.connect` |
| `2026-08-09 07:20:44` | `cowrie.client.version` |
| `2026-08-09 07:20:44` | `cowrie.client.kex` |
| `2026-08-09 07:20:48` | `cowrie.login.success` |
| `2026-08-09 07:20:51` | `cowrie.session.params` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.success` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:51` | `cowrie.command.input` |
| `2026-08-09 07:20:53` | `cowrie.log.closed` |
| `2026-08-09 07:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f62476d134

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:23 |
| **Last Seen** | 2026-08-09 07:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:23:47` | `cowrie.session.connect` |
| `2026-08-09 07:23:48` | `cowrie.client.version` |
| `2026-08-09 07:23:48` | `cowrie.client.kex` |
| `2026-08-09 07:23:53` | `cowrie.login.success` |
| `2026-08-09 07:23:56` | `cowrie.session.params` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.success` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:56` | `cowrie.command.input` |
| `2026-08-09 07:23:57` | `cowrie.log.closed` |
| `2026-08-09 07:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c06077e43b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:26 |
| **Last Seen** | 2026-08-09 07:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:26:49` | `cowrie.session.connect` |
| `2026-08-09 07:26:50` | `cowrie.client.version` |
| `2026-08-09 07:26:50` | `cowrie.client.kex` |
| `2026-08-09 07:26:55` | `cowrie.login.success` |
| `2026-08-09 07:26:58` | `cowrie.session.params` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.success` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:58` | `cowrie.command.input` |
| `2026-08-09 07:26:59` | `cowrie.log.closed` |
| `2026-08-09 07:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab77bdad6fd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:29 |
| **Last Seen** | 2026-08-09 07:29 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:29:44` | `cowrie.session.connect` |
| `2026-08-09 07:29:45` | `cowrie.client.version` |
| `2026-08-09 07:29:45` | `cowrie.client.kex` |
| `2026-08-09 07:29:51` | `cowrie.login.success` |
| `2026-08-09 07:29:55` | `cowrie.session.params` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.success` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:55` | `cowrie.command.input` |
| `2026-08-09 07:29:56` | `cowrie.log.closed` |
| `2026-08-09 07:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736526b1285d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:32 |
| **Last Seen** | 2026-08-09 07:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:32:40` | `cowrie.session.connect` |
| `2026-08-09 07:32:42` | `cowrie.client.version` |
| `2026-08-09 07:32:42` | `cowrie.client.kex` |
| `2026-08-09 07:32:47` | `cowrie.login.success` |
| `2026-08-09 07:32:50` | `cowrie.session.params` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.success` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:50` | `cowrie.command.input` |
| `2026-08-09 07:32:52` | `cowrie.log.closed` |
| `2026-08-09 07:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe23a1bb848

| Field | Detail |
|---|---|
| **Source IP** | `31.173.29[.]136` |
| **First Seen** | 2026-08-09 07:37 |
| **Last Seen** | 2026-08-09 07:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:37:04` | `cowrie.session.connect` |
| `2026-08-09 07:37:05` | `cowrie.client.version` |
| `2026-08-09 07:37:05` | `cowrie.client.kex` |
| `2026-08-09 07:37:07` | `cowrie.login.success` |
| `2026-08-09 07:37:07` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.29[.]136` to AbuseIPDB if not already reported
- [ ] Block `31.173.29[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1693e8faa5

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-09 07:37 |
| **Last Seen** | 2026-08-09 07:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:37:12` | `cowrie.session.connect` |
| `2026-08-09 07:37:13` | `cowrie.client.version` |
| `2026-08-09 07:37:13` | `cowrie.client.kex` |
| `2026-08-09 07:37:15` | `cowrie.login.success` |
| `2026-08-09 07:37:15` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4721fc2972

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:38 |
| **Last Seen** | 2026-08-09 07:38 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:38:17` | `cowrie.session.connect` |
| `2026-08-09 07:38:19` | `cowrie.client.version` |
| `2026-08-09 07:38:19` | `cowrie.client.kex` |
| `2026-08-09 07:38:25` | `cowrie.login.success` |
| `2026-08-09 07:38:29` | `cowrie.session.params` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.success` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:29` | `cowrie.command.input` |
| `2026-08-09 07:38:31` | `cowrie.log.closed` |
| `2026-08-09 07:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db44a63bf943

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:41 |
| **Last Seen** | 2026-08-09 07:41 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:41:06` | `cowrie.session.connect` |
| `2026-08-09 07:41:08` | `cowrie.client.version` |
| `2026-08-09 07:41:08` | `cowrie.client.kex` |
| `2026-08-09 07:41:14` | `cowrie.login.success` |
| `2026-08-09 07:41:18` | `cowrie.session.params` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.success` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:18` | `cowrie.command.input` |
| `2026-08-09 07:41:20` | `cowrie.log.closed` |
| `2026-08-09 07:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60243c3d717

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:43 |
| **Last Seen** | 2026-08-09 07:44 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:43:52` | `cowrie.session.connect` |
| `2026-08-09 07:43:54` | `cowrie.client.version` |
| `2026-08-09 07:43:54` | `cowrie.client.kex` |
| `2026-08-09 07:44:05` | `cowrie.login.success` |
| `2026-08-09 07:44:10` | `cowrie.session.params` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.success` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:10` | `cowrie.command.input` |
| `2026-08-09 07:44:12` | `cowrie.log.closed` |
| `2026-08-09 07:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45b7cb0de4d

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-08-09 07:45 |
| **Last Seen** | 2026-08-09 07:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:45:45` | `cowrie.session.connect` |
| `2026-08-09 07:45:46` | `cowrie.client.version` |
| `2026-08-09 07:45:46` | `cowrie.client.kex` |
| `2026-08-09 07:45:48` | `cowrie.login.success` |
| `2026-08-09 07:45:49` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b3a77fd631

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:46 |
| **Last Seen** | 2026-08-09 07:46 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:46:34` | `cowrie.session.connect` |
| `2026-08-09 07:46:36` | `cowrie.client.version` |
| `2026-08-09 07:46:36` | `cowrie.client.kex` |
| `2026-08-09 07:46:45` | `cowrie.login.success` |
| `2026-08-09 07:46:50` | `cowrie.session.params` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.success` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:50` | `cowrie.command.input` |
| `2026-08-09 07:46:52` | `cowrie.log.closed` |
| `2026-08-09 07:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3d4743bcac

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:49 |
| **Last Seen** | 2026-08-09 07:49 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:49:13` | `cowrie.session.connect` |
| `2026-08-09 07:49:16` | `cowrie.client.version` |
| `2026-08-09 07:49:16` | `cowrie.client.kex` |
| `2026-08-09 07:49:27` | `cowrie.login.success` |
| `2026-08-09 07:49:32` | `cowrie.session.params` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.success` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:32` | `cowrie.command.input` |
| `2026-08-09 07:49:34` | `cowrie.log.closed` |
| `2026-08-09 07:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13eab840265d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:51 |
| **Last Seen** | 2026-08-09 07:52 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:51:50` | `cowrie.session.connect` |
| `2026-08-09 07:51:52` | `cowrie.client.version` |
| `2026-08-09 07:51:52` | `cowrie.client.kex` |
| `2026-08-09 07:52:00` | `cowrie.login.success` |
| `2026-08-09 07:52:06` | `cowrie.session.params` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.success` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:06` | `cowrie.command.input` |
| `2026-08-09 07:52:07` | `cowrie.log.closed` |
| `2026-08-09 07:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9b1e1cfecf

| Field | Detail |
|---|---|
| **Source IP** | `43.248.213[.]232` |
| **First Seen** | 2026-08-09 07:52 |
| **Last Seen** | 2026-08-09 07:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:52:54` | `cowrie.session.connect` |
| `2026-08-09 07:52:54` | `cowrie.client.version` |
| `2026-08-09 07:52:54` | `cowrie.client.kex` |
| `2026-08-09 07:52:56` | `cowrie.login.success` |
| `2026-08-09 07:52:57` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.213[.]232` to AbuseIPDB if not already reported
- [ ] Block `43.248.213[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8ee14c83b2

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-08-09 07:53 |
| **Last Seen** | 2026-08-09 07:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:53:02` | `cowrie.session.connect` |
| `2026-08-09 07:53:03` | `cowrie.client.version` |
| `2026-08-09 07:53:03` | `cowrie.client.kex` |
| `2026-08-09 07:53:04` | `cowrie.login.success` |
| `2026-08-09 07:53:04` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62cfe08b1d8a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:54 |
| **Last Seen** | 2026-08-09 07:54 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:54:26` | `cowrie.session.connect` |
| `2026-08-09 07:54:28` | `cowrie.client.version` |
| `2026-08-09 07:54:28` | `cowrie.client.kex` |
| `2026-08-09 07:54:36` | `cowrie.login.success` |
| `2026-08-09 07:54:41` | `cowrie.session.params` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.success` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:41` | `cowrie.command.input` |
| `2026-08-09 07:54:43` | `cowrie.log.closed` |
| `2026-08-09 07:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c4c888392b

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-08-09 07:55 |
| **Last Seen** | 2026-08-09 07:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:55:13` | `cowrie.session.connect` |
| `2026-08-09 07:55:14` | `cowrie.client.version` |
| `2026-08-09 07:55:14` | `cowrie.client.kex` |
| `2026-08-09 07:55:16` | `cowrie.login.success` |
| `2026-08-09 07:55:17` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf64257cd39

| Field | Detail |
|---|---|
| **Source IP** | `58.215.243[.]6` |
| **First Seen** | 2026-08-09 07:55 |
| **Last Seen** | 2026-08-09 07:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:55:27` | `cowrie.session.connect` |
| `2026-08-09 07:55:28` | `cowrie.client.version` |
| `2026-08-09 07:55:28` | `cowrie.client.kex` |
| `2026-08-09 07:55:33` | `cowrie.login.success` |
| `2026-08-09 07:55:34` | `cowrie.direct-tcpip.request` |
| `2026-08-09 07:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.215.243[.]6` to AbuseIPDB if not already reported
- [ ] Block `58.215.243[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e27035741a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:56 |
| **Last Seen** | 2026-08-09 07:57 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:56:59` | `cowrie.session.connect` |
| `2026-08-09 07:57:01` | `cowrie.client.version` |
| `2026-08-09 07:57:01` | `cowrie.client.kex` |
| `2026-08-09 07:57:09` | `cowrie.login.success` |
| `2026-08-09 07:57:14` | `cowrie.session.params` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.success` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:14` | `cowrie.command.input` |
| `2026-08-09 07:57:16` | `cowrie.log.closed` |
| `2026-08-09 07:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459b7de90619

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 07:59 |
| **Last Seen** | 2026-08-09 07:59 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 07:59:31` | `cowrie.session.connect` |
| `2026-08-09 07:59:32` | `cowrie.client.version` |
| `2026-08-09 07:59:32` | `cowrie.client.kex` |
| `2026-08-09 07:59:39` | `cowrie.login.success` |
| `2026-08-09 07:59:43` | `cowrie.session.params` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.success` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:43` | `cowrie.command.input` |
| `2026-08-09 07:59:45` | `cowrie.log.closed` |
| `2026-08-09 07:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419dae4fb759

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:01 |
| **Last Seen** | 2026-08-09 08:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:01:58` | `cowrie.session.connect` |
| `2026-08-09 08:01:59` | `cowrie.client.version` |
| `2026-08-09 08:01:59` | `cowrie.client.kex` |
| `2026-08-09 08:02:05` | `cowrie.login.success` |
| `2026-08-09 08:02:08` | `cowrie.session.params` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.success` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:08` | `cowrie.command.input` |
| `2026-08-09 08:02:09` | `cowrie.log.closed` |
| `2026-08-09 08:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-575fd913159c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:04 |
| **Last Seen** | 2026-08-09 08:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:04:19` | `cowrie.session.connect` |
| `2026-08-09 08:04:20` | `cowrie.client.version` |
| `2026-08-09 08:04:20` | `cowrie.client.kex` |
| `2026-08-09 08:04:25` | `cowrie.login.success` |
| `2026-08-09 08:04:29` | `cowrie.session.params` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.success` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:29` | `cowrie.command.input` |
| `2026-08-09 08:04:31` | `cowrie.log.closed` |
| `2026-08-09 08:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff10fcddfcb7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 08:05 |
| **Last Seen** | 2026-08-09 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:05:24` | `cowrie.session.connect` |
| `2026-08-09 08:05:24` | `cowrie.client.version` |
| `2026-08-09 08:05:24` | `cowrie.client.kex` |
| `2026-08-09 08:05:24` | `cowrie.login.success` |
| `2026-08-09 08:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f46ed2a277dc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 08:05 |
| **Last Seen** | 2026-08-09 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:05:25` | `cowrie.session.connect` |
| `2026-08-09 08:05:25` | `cowrie.client.version` |
| `2026-08-09 08:05:25` | `cowrie.client.kex` |
| `2026-08-09 08:05:25` | `cowrie.login.success` |
| `2026-08-09 08:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8033d5e3f0be

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 08:05 |
| **Last Seen** | 2026-08-09 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:05:33` | `cowrie.session.connect` |
| `2026-08-09 08:05:33` | `cowrie.client.version` |
| `2026-08-09 08:05:33` | `cowrie.client.kex` |
| `2026-08-09 08:05:33` | `cowrie.login.success` |
| `2026-08-09 08:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236db03fdf37

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-09 08:05 |
| **Last Seen** | 2026-08-09 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:05:33` | `cowrie.session.connect` |
| `2026-08-09 08:05:33` | `cowrie.client.version` |
| `2026-08-09 08:05:33` | `cowrie.client.kex` |
| `2026-08-09 08:05:33` | `cowrie.login.success` |
| `2026-08-09 08:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-767bf0106e38

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:06 |
| **Last Seen** | 2026-08-09 08:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:06:41` | `cowrie.session.connect` |
| `2026-08-09 08:06:43` | `cowrie.client.version` |
| `2026-08-09 08:06:43` | `cowrie.client.kex` |
| `2026-08-09 08:06:49` | `cowrie.login.success` |
| `2026-08-09 08:06:51` | `cowrie.session.params` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.success` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:51` | `cowrie.command.input` |
| `2026-08-09 08:06:52` | `cowrie.log.closed` |
| `2026-08-09 08:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a8856b5662

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:09 |
| **Last Seen** | 2026-08-09 08:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:09:03` | `cowrie.session.connect` |
| `2026-08-09 08:09:04` | `cowrie.client.version` |
| `2026-08-09 08:09:04` | `cowrie.client.kex` |
| `2026-08-09 08:09:10` | `cowrie.login.success` |
| `2026-08-09 08:09:14` | `cowrie.session.params` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.success` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:14` | `cowrie.command.input` |
| `2026-08-09 08:09:16` | `cowrie.log.closed` |
| `2026-08-09 08:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4438240bf146

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:11 |
| **Last Seen** | 2026-08-09 08:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:11:22` | `cowrie.session.connect` |
| `2026-08-09 08:11:22` | `cowrie.client.version` |
| `2026-08-09 08:11:22` | `cowrie.client.kex` |
| `2026-08-09 08:11:25` | `cowrie.login.success` |
| `2026-08-09 08:11:28` | `cowrie.session.params` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.success` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:28` | `cowrie.command.input` |
| `2026-08-09 08:11:29` | `cowrie.log.closed` |
| `2026-08-09 08:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae603a8fc85

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:13 |
| **Last Seen** | 2026-08-09 08:14 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:13:42` | `cowrie.session.connect` |
| `2026-08-09 08:13:44` | `cowrie.client.version` |
| `2026-08-09 08:13:44` | `cowrie.client.kex` |
| `2026-08-09 08:13:54` | `cowrie.login.success` |
| `2026-08-09 08:13:58` | `cowrie.session.params` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.success` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.command.input` |
| `2026-08-09 08:13:58` | `cowrie.log.closed` |
| `2026-08-09 08:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07dca157079a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 08:15 |
| **Last Seen** | 2026-08-09 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:15:35` | `cowrie.session.connect` |
| `2026-08-09 08:15:35` | `cowrie.client.version` |
| `2026-08-09 08:15:35` | `cowrie.client.kex` |
| `2026-08-09 08:15:35` | `cowrie.login.success` |
| `2026-08-09 08:15:35` | `cowrie.direct-tcpip.request` |
| `2026-08-09 08:15:35` | `cowrie.direct-tcpip.data` |
| `2026-08-09 08:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67544429013b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-09 08:15 |
| **Last Seen** | 2026-08-09 08:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:15:55` | `cowrie.session.connect` |
| `2026-08-09 08:15:56` | `cowrie.client.version` |
| `2026-08-09 08:15:56` | `cowrie.client.kex` |
| `2026-08-09 08:16:00` | `cowrie.login.success` |
| `2026-08-09 08:16:02` | `cowrie.session.params` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.success` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:02` | `cowrie.command.input` |
| `2026-08-09 08:16:03` | `cowrie.log.closed` |
| `2026-08-09 08:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60edb79fd7b

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-08-09 08:20 |
| **Last Seen** | 2026-08-09 08:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:20:46` | `cowrie.session.connect` |
| `2026-08-09 08:20:47` | `cowrie.client.version` |
| `2026-08-09 08:20:47` | `cowrie.client.kex` |
| `2026-08-09 08:20:48` | `cowrie.login.success` |
| `2026-08-09 08:20:49` | `cowrie.direct-tcpip.request` |
| `2026-08-09 08:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d006625e8be

| Field | Detail |
|---|---|
| **Source IP** | `45.79.181[.]223` |
| **First Seen** | 2026-08-09 08:28 |
| **Last Seen** | 2026-08-09 08:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:28:38` | `cowrie.session.connect` |
| `2026-08-09 08:28:38` | `cowrie.login.success` |
| `2026-08-09 08:28:38` | `cowrie.session.params` |
| `2026-08-09 08:28:38` | `cowrie.command.input` |
| `2026-08-09 08:28:38` | `cowrie.command.input` |
| `2026-08-09 08:28:38` | `cowrie.command.failed` |
| `2026-08-09 08:28:38` | `cowrie.command.input` |
| `2026-08-09 08:28:38` | `cowrie.command.failed` |
| `2026-08-09 08:28:38` | `cowrie.command.input` |
| `2026-08-09 08:28:38` | `cowrie.log.closed` |
| `2026-08-09 08:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.181[.]223` to AbuseIPDB if not already reported
- [ ] Block `45.79.181[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c65d0a9693a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 08:35 |
| **Last Seen** | 2026-08-09 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 08:35:34` | `cowrie.session.connect` |
| `2026-08-09 08:35:34` | `cowrie.client.version` |
| `2026-08-09 08:35:34` | `cowrie.client.kex` |
| `2026-08-09 08:35:35` | `cowrie.login.success` |
| `2026-08-09 08:35:35` | `cowrie.direct-tcpip.request` |
| `2026-08-09 08:35:35` | `cowrie.direct-tcpip.data` |
| `2026-08-09 08:35:35` | `cowrie.session.closed` |

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
| `139.199.80[.]137` | **4** | 2026-08-09 07:16 | 2026-08-09 08:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.64.39[.]43` | **3** | 2026-08-09 07:43 | 2026-08-09 08:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-09 08:01 | 2026-08-09 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-09 07:42 | 2026-08-09 07:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]191` | **3** | 2026-08-09 08:50 | 2026-08-09 08:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]170` | **3** | 2026-08-09 08:51 | 2026-08-09 08:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]103` | **3** | 2026-08-09 08:50 | 2026-08-09 08:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-09 07:45 | 2026-08-09 07:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `135.237.126[.]160` | **2** | 2026-08-09 07:20 | 2026-08-09 07:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-08-09 07:35 | 2026-08-09 08:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.161.50[.]108` | **2** | 2026-08-09 08:17 | 2026-08-09 08:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.174.80[.]40` | 1 | 2026-08-09 08:43 | 2026-08-09 08:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-09 07:35 | 2026-08-09 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.120.101[.]250` | 1 | 2026-08-09 08:36 | 2026-08-09 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-08-09 08:16 | 2026-08-09 08:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.36.100[.]125` | 1 | 2026-08-09 08:39 | 2026-08-09 08:39 | 11s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]136` | 1 | 2026-08-09 08:28 | 2026-08-09 08:28 | 1s | 0 | `T1592` | 🟢 LOW |
| `182.218.116[.]96` | 1 | 2026-08-09 07:34 | 2026-08-09 07:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `184.185.2[.]254` | 1 | 2026-08-09 07:08 | 2026-08-09 07:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.239.41[.]74` | 1 | 2026-08-09 08:55 | 2026-08-09 08:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.104.36[.]133` | 1 | 2026-08-09 07:21 | 2026-08-09 07:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | 1 | 2026-08-09 08:05 | 2026-08-09 08:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.202.91[.]147` | 1 | 2026-08-09 08:24 | 2026-08-09 08:24 | 20s | 0 | `T1592` | 🟢 LOW |
| `220.180.249[.]165` | 1 | 2026-08-09 07:11 | 2026-08-09 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-08-09 07:02 | 2026-08-09 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-09 07:36 | 2026-08-09 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.6.6[.]238` | 1 | 2026-08-09 08:03 | 2026-08-09 08:03 | 20s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | 1 | 2026-08-09 08:28 | 2026-08-09 08:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.174.35[.]18` | 1 | 2026-08-09 08:22 | 2026-08-09 08:22 | 5s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-09 08:36 | 2026-08-09 08:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-08-09 07:20 | 2026-08-09 07:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | 1 | 2026-08-09 07:01 | 2026-08-09 07:01 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
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
| `136.64.39[.]43` | US | Google LLC | **100** ⚠️ | 4 |
| `176.36.100[.]125` | UA | Lanet Network Ltd | **100** ⚠️ | 2 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `190.104.36[.]133` | AR | Jumpnet Soluciones de Internet S.R.L. | **100** ⚠️ | 0 |
| `220.180.249[.]165` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `172.104.210[.]105` | US | Linode | **100** ⚠️ | 50 |
| `58.215.243[.]6` | CN | CHINANET BACKBONE | **100** ⚠️ | 50 |
| `194.165.16[.]162` | PA | Flyservers S.A. | **100** ⚠️ | 50 |
| `117.252.93[.]114` | IN | CDMA Project, BSNL New Delhi | **100** ⚠️ | 50 |
| `176.32.193[.]16` | AM | Ucom CJSC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 57 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 22 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 22 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 118 cases |
| Tool 34  | Credential Extractor        | ✅ 165 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (21.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 41 priority case(s) shown individually · 32 recon entry/entries in table (11 group(s) consolidating 31 session(s)).

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
_Report time: 2026-08-09T10:38:17Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-27 |
| **Generated At** | 2026-06-27T21:09:17Z |
| **Shift Time** | 21:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **452** |
| Confirmed Threats | **442** |
| False Positives Filtered | **10** (2.2%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **11** |
| High Severity Cases | **165** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **287** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **170** |
| Unique Credential Pairs | **162** |
| Unique Usernames | **86** |
| Unique Passwords | **142** |
| Successful Auth Pairs | **166** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `ubuntu` | 8 |
| `admin` | 6 |
| `web` | 2 |
| `fengyingchao` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `admin` | 7 |
| `1234` | 6 |
| `111111` | 3 |
| `12345` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `root` | `LeitboGi0ro` | 2 |
| `root` | `123@@@` | 2 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | 2 |
| `kipt` | `kipt123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `kipt` | `kipt123` | `209.99.185.59` | 2026-06-27T18:55:32 |
| `root` | `12345` | `195.178.110.217` | 2026-06-27T18:55:40 |
| `root` | `Admin@333` | `209.99.185.59` | 2026-06-27T18:56:26 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-27T18:57:15 |
| `dsp_nmst` | `dsp_nmst` | `209.99.185.59` | 2026-06-27T18:57:21 |
| `xianghx` | `123456` | `209.99.185.59` | 2026-06-27T18:58:14 |
| `aaron` | `aaron` | `209.99.185.59` | 2026-06-27T18:59:06 |
| `xupeng` | `123456` | `209.99.185.59` | 2026-06-27T18:59:58 |
| `web` | `jesus1` | `45.205.1.42` | 2026-06-27T19:00:47 |
| `hpeadm` | `initial0` | `209.99.185.59` | 2026-06-27T19:00:52 |
| `root` | `Password001` | `209.99.185.59` | 2026-06-27T19:01:45 |
| `domicilios1` | `domicilios1` | `209.99.185.59` | 2026-06-27T19:02:40 |
| `hadoop` | `passpass` | `209.99.185.59` | 2026-06-27T19:03:34 |
| `operator` | `operator1` | `209.99.185.59` | 2026-06-27T19:04:37 |
| `root` | `Password123` | `209.99.185.59` | 2026-06-27T19:05:42 |
| `fengyingchao` | `111111` | `209.99.185.59` | 2026-06-27T19:06:36 |
| `root` | `P@ssw0rd!@#456` | `45.198.224.120` | 2026-06-27T19:07:01 |
| `backup` | `1qaz@WSX` | `209.99.185.59` | 2026-06-27T19:07:31 |
| `git` | `git123` | `209.99.185.59` | 2026-06-27T19:08:27 |
| `root` | `Passw0rd4H` | `209.99.185.59` | 2026-06-27T19:09:24 |
| `fengyingchao` | `fengyingchao1` | `209.99.185.59` | 2026-06-27T19:10:21 |
| `test` | `xsw21qaz` | `209.99.185.59` | 2026-06-27T19:11:19 |
| `xm` | `xm136` | `209.99.185.59` | 2026-06-27T19:12:18 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-27T19:12:54 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-27T19:12:54 |
| `inoue` | `inoue` | `209.99.185.59` | 2026-06-27T19:13:13 |
| `norna` | `norna2019` | `209.99.185.59` | 2026-06-27T19:14:16 |
| `debian` | `debian` | `45.205.1.42` | 2026-06-27T19:15:19 |
| `www` | `123abc` | `209.99.185.59` | 2026-06-27T19:15:25 |
| `bibi` | `1234` | `209.99.185.59` | 2026-06-27T19:16:23 |
| `root` | `P455WORD` | `209.99.185.59` | 2026-06-27T19:17:20 |
| `clamav` | `clamav` | `209.99.185.59` | 2026-06-27T19:18:17 |
| `root` | `senha123` | `45.198.224.120` | 2026-06-27T19:18:47 |
| `root` | `sshd` | `209.99.185.59` | 2026-06-27T19:19:13 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-27T19:19:37 |
| `root` | `euclid` | `209.99.185.59` | 2026-06-27T19:20:10 |
| `root` | `pa$$w0rd1` | `209.99.185.59` | 2026-06-27T19:21:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.61` | 2026-06-27T19:21:32 |
| `bitrix` | `bitrix!@#` | `209.99.185.59` | 2026-06-27T19:22:08 |
| `tomcat` | `1234567` | `209.99.185.59` | 2026-06-27T19:23:08 |
| `root` | `qaz1wsx2123` | `209.99.185.59` | 2026-06-27T19:24:06 |
| `root` | `admin123!@#` | `209.99.185.59` | 2026-06-27T19:25:04 |
| `web1` | `letmein` | `209.99.185.59` | 2026-06-27T19:26:01 |
| `root` | `Q1W2E3!@#` | `209.99.185.59` | 2026-06-27T19:27:00 |
| `root` | `As@998875` | `209.99.185.59` | 2026-06-27T19:28:00 |
| `root` | `12345678` | `195.178.110.217` | 2026-06-27T19:28:48 |
| `jamil` | `jamil` | `209.99.185.59` | 2026-06-27T19:29:00 |
| `db2inst1` | `db2password` | `209.99.185.59` | 2026-06-27T19:30:00 |
| `falcon` | `falcon` | `45.205.1.42` | 2026-06-27T19:30:03 |
| `oracle` | `baseball` | `45.198.224.120` | 2026-06-27T19:30:34 |
| `user02` | `123456` | `209.99.185.59` | 2026-06-27T19:30:59 |
| `zzx` | `zzx` | `209.99.185.59` | 2026-06-27T19:31:58 |
| `mcht` | `mcht` | `209.99.185.59` | 2026-06-27T19:33:00 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-27T19:33:24 |
| `root` | `cron` | `209.99.185.59` | 2026-06-27T19:34:01 |
| `zabbix` | `zabbix123` | `209.99.185.59` | 2026-06-27T19:35:02 |
| `cajas15` | `cajas15` | `209.99.185.59` | 2026-06-27T19:36:03 |
| `guest2` | `1234` | `209.99.185.59` | 2026-06-27T19:37:04 |
| `media` | `media` | `209.99.185.59` | 2026-06-27T19:38:05 |
| `debian` | `12345` | `209.99.185.59` | 2026-06-27T19:39:07 |
| `cassandra` | `cassandra` | `209.99.185.59` | 2026-06-27T19:40:09 |
| `kenny` | `kenny123` | `209.99.185.59` | 2026-06-27T19:41:14 |
| `root` | `1234` | `45.198.224.120` | 2026-06-27T19:42:08 |
| `gaoyx` | `199894Gyx` | `209.99.185.59` | 2026-06-27T19:42:18 |
| `wwwroot` | `123456` | `209.99.185.59` | 2026-06-27T19:43:22 |
| `root` | `a1a1a1` | `209.99.185.59` | 2026-06-27T19:44:25 |
| `root` | `qazwsx1234` | `45.205.1.42` | 2026-06-27T19:44:41 |
| `root` | `123456789` | `195.178.110.217` | 2026-06-27T19:44:54 |
| `subzero` | `Odin1434` | `209.99.185.59` | 2026-06-27T19:45:29 |
| `root` | `administrator` | `209.99.185.59` | 2026-06-27T19:46:36 |
| `root` | `@dm1n2019!bhq` | `209.99.185.59` | 2026-06-27T19:47:44 |
| `cykim` | `2252` | `209.99.185.59` | 2026-06-27T19:48:52 |
| `apache` | `password123` | `209.99.185.59` | 2026-06-27T19:49:57 |
| `ubuntu` | `git` | `209.99.185.59` | 2026-06-27T19:51:03 |
| `server` | `1234qwer` | `209.99.185.59` | 2026-06-27T19:52:09 |
| `root` | `qazwsxEDC!@#` | `209.99.185.59` | 2026-06-27T19:53:18 |
| `shutinggu3` | `shutinggu3` | `45.198.224.120` | 2026-06-27T19:53:26 |
| `root` | `debian2011` | `209.99.185.59` | 2026-06-27T19:54:28 |
| `quyx` | `quyx` | `209.99.185.59` | 2026-06-27T19:55:35 |
| `admin` | `admin` | `138.68.243.18` | 2026-06-27T19:56:15 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-27T19:56:15 |
| `root` | `QWEasd123...` | `209.99.185.59` | 2026-06-27T19:56:40 |
| `dev` | `Ucms9ZB4` | `209.99.185.59` | 2026-06-27T19:57:47 |
| `root` | `1q2w3e4r` | `195.178.110.217` | 2026-06-27T19:58:03 |
| `yuanwd` | `123321` | `209.99.185.59` | 2026-06-27T19:58:55 |
| `ubuntu` | `asd123` | `45.205.1.42` | 2026-06-27T19:59:27 |
| `root` | `password!12345` | `209.99.185.59` | 2026-06-27T20:00:06 |
| `root` | `6` | `209.99.185.59` | 2026-06-27T20:00:54 |
| `wangxm` | `123456` | `209.99.185.59` | 2026-06-27T20:01:39 |
| `root` | `Pass@word123` | `209.99.185.59` | 2026-06-27T20:02:23 |
| `root` | `6461258aA@` | `209.99.185.59` | 2026-06-27T20:03:07 |
| `test` | `123qwe` | `209.99.185.59` | 2026-06-27T20:03:51 |
| `root` | `f` | `209.99.185.59` | 2026-06-27T20:04:35 |
| `ftptest1` | `123456` | `209.99.185.59` | 2026-06-27T20:05:19 |
| `root` | `P@$$w0rD` | `45.198.224.120` | 2026-06-27T20:05:27 |
| `dell` | `111111` | `209.99.185.59` | 2026-06-27T20:06:04 |
| `Zhanghua` | `111111` | `209.99.185.59` | 2026-06-27T20:06:49 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-27T20:07:11 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-27T20:07:11 |
| `test2` | `1234567` | `209.99.185.59` | 2026-06-27T20:07:34 |
| `root` | `Pierro12*` | `209.99.185.59` | 2026-06-27T20:08:19 |
| `ubuntu` | `asdf` | `209.99.185.59` | 2026-06-27T20:09:02 |
| `devops` | `devops123` | `209.99.185.59` | 2026-06-27T20:09:46 |
| `root` | `654321` | `195.178.110.217` | 2026-06-27T20:10:06 |
| `root` | `Admin@1234` | `209.99.185.59` | 2026-06-27T20:10:31 |
| `root` | `yw123456` | `209.99.185.59` | 2026-06-27T20:11:16 |
| `root` | `QAZ@123cde` | `209.99.185.59` | 2026-06-27T20:12:03 |
| `oracle` | `123!@#` | `209.99.185.59` | 2026-06-27T20:12:50 |
| `chenqi` | `123456` | `209.99.185.59` | 2026-06-27T20:13:38 |
| `ubuntu` | `qwerty12345678` | `45.205.1.42` | 2026-06-27T20:14:07 |
| `www-data` | `1234` | `209.99.185.59` | 2026-06-27T20:14:26 |
| `heejin` | `heejin` | `209.99.185.59` | 2026-06-27T20:15:13 |
| `root` | `qwe12345^` | `209.99.185.59` | 2026-06-27T20:16:00 |
| `bbm` | `bbm` | `209.99.185.59` | 2026-06-27T20:16:46 |
| `ubuntu` | `qwe123!!` | `45.198.224.120` | 2026-06-27T20:17:22 |
| `ul` | `ul321` | `209.99.185.59` | 2026-06-27T20:17:34 |
| `root` | `Sxcdyy!23` | `209.99.185.59` | 2026-06-27T20:18:22 |
| `root` | `q1w2e3r4t5y6u7i8o9p0` | `209.99.185.59` | 2026-06-27T20:19:11 |
| `centos` | `centos!@#123` | `209.99.185.59` | 2026-06-27T20:19:59 |
| `zy` | `zy123` | `209.99.185.59` | 2026-06-27T20:20:47 |
| `root` | `Root1234` | `209.99.185.59` | 2026-06-27T20:21:34 |
| `datacenter` | `1234` | `209.99.185.59` | 2026-06-27T20:22:20 |
| `fanslau` | `fanslau` | `209.99.185.59` | 2026-06-27T20:23:06 |
| `amandabackup` | `amandabackup1234` | `209.99.185.59` | 2026-06-27T20:23:55 |
| `root` | `qwe123qWE` | `209.99.185.59` | 2026-06-27T20:24:44 |
| `weblogic` | `P@ssw0rd` | `209.99.185.59` | 2026-06-27T20:25:34 |
| `box` | `box` | `209.99.185.59` | 2026-06-27T20:26:23 |
| `caoll22` | `fDu043371,cll` | `209.99.185.59` | 2026-06-27T20:27:12 |
| `webmaster` | `123456` | `209.99.185.59` | 2026-06-27T20:28:00 |
| `guest` | `123456` | `209.99.185.59` | 2026-06-27T20:28:48 |
| `root` | `cookie` | `45.205.1.42` | 2026-06-27T20:28:50 |
| `ubuntu` | `abc` | `45.198.224.120` | 2026-06-27T20:29:24 |
| `root` | `LsUs4NfNHtsnUdqw@#12` | `209.99.185.59` | 2026-06-27T20:29:38 |
| `iso` | `iso` | `209.99.185.59` | 2026-06-27T20:30:28 |
| `ubuntu` | `test123` | `209.99.185.59` | 2026-06-27T20:31:19 |
| `szr` | `szr` | `209.99.185.59` | 2026-06-27T20:32:10 |
| `root` | `P@assw0rd` | `209.99.185.59` | 2026-06-27T20:33:02 |
| `uftp` | `321` | `209.99.185.59` | 2026-06-27T20:33:51 |
| `ypl16` | `t5wqs1c775` | `209.99.185.59` | 2026-06-27T20:34:40 |
| `root` | `Qwerty1` | `209.99.185.59` | 2026-06-27T20:35:28 |
| `root` | `passw0rd@123` | `209.99.185.59` | 2026-06-27T20:36:19 |
| `twinbell` | `twinbell` | `209.99.185.59` | 2026-06-27T20:37:11 |
| `freeneotree` | `1234` | `209.99.185.59` | 2026-06-27T20:38:04 |
| `ossuser` | `123456` | `209.99.185.59` | 2026-06-27T20:38:56 |
| `root` | `1z2x` | `209.99.185.59` | 2026-06-27T20:39:48 |
| `web` | `changeme` | `209.99.185.59` | 2026-06-27T20:40:39 |
| `root` | `admin` | `192.42.116.63` | 2026-06-27T20:41:22 |
| `root` | `Pass@word456` | `45.198.224.120` | 2026-06-27T20:41:25 |
| `root` | `P@ss123!@#` | `209.99.185.59` | 2026-06-27T20:41:30 |
| `root` | `root2004` | `209.99.185.59` | 2026-06-27T20:42:20 |
| `andres` | `andres` | `209.99.185.59` | 2026-06-27T20:43:13 |
| `root` | `qqtech` | `45.205.1.42` | 2026-06-27T20:43:31 |
| `yangliusha17` | `yangliusha17` | `209.99.185.59` | 2026-06-27T20:44:06 |
| `lihl` | `Asphodelus` | `209.99.185.59` | 2026-06-27T20:45:01 |
| `jenkins` | `jenkins1@` | `209.99.185.59` | 2026-06-27T20:45:56 |
| `root` | `Ef33rwrfsdsds` | `209.99.185.59` | 2026-06-27T20:46:50 |
| `root` | `Paic1234` | `209.99.185.59` | 2026-06-27T20:47:42 |
| `root` | `lol123` | `209.99.185.59` | 2026-06-27T20:48:36 |
| `design` | `design123` | `209.99.185.59` | 2026-06-27T20:49:30 |
| `autossh` | `autossh` | `209.99.185.59` | 2026-06-27T20:50:26 |
| `root` | `tszwanshankfwass` | `209.99.185.59` | 2026-06-27T20:51:23 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.235` | 2026-06-27T20:52:01 |
| `ubuntu` | `qwaszx` | `209.99.185.59` | 2026-06-27T20:52:19 |
| `root` | `torrent` | `45.198.224.120` | 2026-06-27T20:53:04 |
| `root` | `admin123!` | `209.99.185.59` | 2026-06-27T20:53:12 |
| `lenovo` | `123.com` | `209.99.185.59` | 2026-06-27T20:54:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **452** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 161 |
| libssh | 9 |
| Paramiko (Python) | 4 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 149 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 6 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 149 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `b893695067f9...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 5 | 1 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; dmidecode -s p
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null
```
Source IPs: `195.178.110.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **19** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS33363` | Charter Communications, Inc | 1 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (163)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0eedfe266bfd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 18:55 |
| **Last Seen** | 2026-06-27 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:55:31` | `cowrie.session.connect` |
| `2026-06-27 18:55:31` | `cowrie.client.version` |
| `2026-06-27 18:55:32` | `cowrie.client.kex` |
| `2026-06-27 18:55:32` | `cowrie.login.success` |
| `2026-06-27 18:55:33` | `cowrie.session.params` |
| `2026-06-27 18:55:33` | `cowrie.command.input` |
| `2026-06-27 18:55:33` | `cowrie.log.closed` |
| `2026-06-27 18:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e37f6f5dd38

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-27 18:55 |
| **Last Seen** | 2026-06-27 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; dmidecode -s p, uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:55:40` | `cowrie.session.connect` |
| `2026-06-27 18:55:40` | `cowrie.client.version` |
| `2026-06-27 18:55:40` | `cowrie.client.kex` |
| `2026-06-27 18:55:40` | `cowrie.login.success` |
| `2026-06-27 18:55:41` | `cowrie.session.params` |
| `2026-06-27 18:55:41` | `cowrie.command.input` |
| `2026-06-27 18:55:41` | `cowrie.command.input` |
| `2026-06-27 18:55:41` | `cowrie.command.input` |
| `2026-06-27 18:55:41` | `cowrie.command.input` |
| `2026-06-27 18:55:41` | `cowrie.log.closed` |
| `2026-06-27 18:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2820ec7a7518

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 18:56 |
| **Last Seen** | 2026-06-27 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:56:26` | `cowrie.session.connect` |
| `2026-06-27 18:56:26` | `cowrie.client.version` |
| `2026-06-27 18:56:26` | `cowrie.client.kex` |
| `2026-06-27 18:56:26` | `cowrie.login.success` |
| `2026-06-27 18:56:27` | `cowrie.session.params` |
| `2026-06-27 18:56:27` | `cowrie.command.input` |
| `2026-06-27 18:56:27` | `cowrie.log.closed` |
| `2026-06-27 18:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125687f9cf58

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-27 18:57 |
| **Last Seen** | 2026-06-27 18:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:57:14` | `cowrie.session.connect` |
| `2026-06-27 18:57:14` | `cowrie.client.version` |
| `2026-06-27 18:57:14` | `cowrie.client.kex` |
| `2026-06-27 18:57:15` | `cowrie.login.success` |
| `2026-06-27 18:57:15` | `cowrie.direct-tcpip.request` |
| `2026-06-27 18:57:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-27 18:57:15` | `cowrie.direct-tcpip.data` |
| `2026-06-27 18:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f039c65d4d5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-27 18:57 |
| **Last Seen** | 2026-06-27 18:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:57:15` | `cowrie.session.connect` |
| `2026-06-27 18:57:15` | `cowrie.client.version` |
| `2026-06-27 18:57:15` | `cowrie.client.kex` |
| `2026-06-27 18:57:15` | `cowrie.login.success` |
| `2026-06-27 18:57:16` | `cowrie.direct-tcpip.request` |
| `2026-06-27 18:57:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-27 18:57:16` | `cowrie.direct-tcpip.data` |
| `2026-06-27 18:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0859cd8b46f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 18:57 |
| **Last Seen** | 2026-06-27 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:57:20` | `cowrie.session.connect` |
| `2026-06-27 18:57:20` | `cowrie.client.version` |
| `2026-06-27 18:57:20` | `cowrie.client.kex` |
| `2026-06-27 18:57:21` | `cowrie.login.success` |
| `2026-06-27 18:57:22` | `cowrie.session.params` |
| `2026-06-27 18:57:22` | `cowrie.command.input` |
| `2026-06-27 18:57:22` | `cowrie.log.closed` |
| `2026-06-27 18:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f6224a8598

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 18:58 |
| **Last Seen** | 2026-06-27 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:58:14` | `cowrie.session.connect` |
| `2026-06-27 18:58:14` | `cowrie.client.version` |
| `2026-06-27 18:58:14` | `cowrie.client.kex` |
| `2026-06-27 18:58:14` | `cowrie.login.success` |
| `2026-06-27 18:58:15` | `cowrie.session.params` |
| `2026-06-27 18:58:15` | `cowrie.command.input` |
| `2026-06-27 18:58:15` | `cowrie.log.closed` |
| `2026-06-27 18:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d971edc52c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 18:59 |
| **Last Seen** | 2026-06-27 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:59:06` | `cowrie.session.connect` |
| `2026-06-27 18:59:06` | `cowrie.client.version` |
| `2026-06-27 18:59:06` | `cowrie.client.kex` |
| `2026-06-27 18:59:06` | `cowrie.login.success` |
| `2026-06-27 18:59:07` | `cowrie.session.params` |
| `2026-06-27 18:59:07` | `cowrie.command.input` |
| `2026-06-27 18:59:07` | `cowrie.log.closed` |
| `2026-06-27 18:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e2d5b6bf47f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 18:59 |
| **Last Seen** | 2026-06-27 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 18:59:58` | `cowrie.session.connect` |
| `2026-06-27 18:59:58` | `cowrie.client.version` |
| `2026-06-27 18:59:58` | `cowrie.client.kex` |
| `2026-06-27 18:59:58` | `cowrie.login.success` |
| `2026-06-27 18:59:59` | `cowrie.session.params` |
| `2026-06-27 18:59:59` | `cowrie.command.input` |
| `2026-06-27 18:59:59` | `cowrie.log.closed` |
| `2026-06-27 18:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d3fd634221

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 19:00 |
| **Last Seen** | 2026-06-27 19:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:00:44` | `cowrie.session.connect` |
| `2026-06-27 19:00:45` | `cowrie.client.version` |
| `2026-06-27 19:00:45` | `cowrie.client.kex` |
| `2026-06-27 19:00:47` | `cowrie.login.success` |
| `2026-06-27 19:00:49` | `cowrie.session.params` |
| `2026-06-27 19:00:49` | `cowrie.command.input` |
| `2026-06-27 19:00:49` | `cowrie.log.closed` |
| `2026-06-27 19:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc64e7d32bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:00 |
| **Last Seen** | 2026-06-27 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:00:51` | `cowrie.session.connect` |
| `2026-06-27 19:00:51` | `cowrie.client.version` |
| `2026-06-27 19:00:51` | `cowrie.client.kex` |
| `2026-06-27 19:00:52` | `cowrie.login.success` |
| `2026-06-27 19:00:52` | `cowrie.session.params` |
| `2026-06-27 19:00:52` | `cowrie.command.input` |
| `2026-06-27 19:00:52` | `cowrie.log.closed` |
| `2026-06-27 19:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0905bb3120

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:01 |
| **Last Seen** | 2026-06-27 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:01:45` | `cowrie.session.connect` |
| `2026-06-27 19:01:45` | `cowrie.client.version` |
| `2026-06-27 19:01:45` | `cowrie.client.kex` |
| `2026-06-27 19:01:45` | `cowrie.login.success` |
| `2026-06-27 19:01:46` | `cowrie.session.params` |
| `2026-06-27 19:01:46` | `cowrie.command.input` |
| `2026-06-27 19:01:46` | `cowrie.log.closed` |
| `2026-06-27 19:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93cd83b4ed0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:02 |
| **Last Seen** | 2026-06-27 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:02:39` | `cowrie.session.connect` |
| `2026-06-27 19:02:39` | `cowrie.client.version` |
| `2026-06-27 19:02:39` | `cowrie.client.kex` |
| `2026-06-27 19:02:40` | `cowrie.login.success` |
| `2026-06-27 19:02:40` | `cowrie.session.params` |
| `2026-06-27 19:02:40` | `cowrie.command.input` |
| `2026-06-27 19:02:40` | `cowrie.log.closed` |
| `2026-06-27 19:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae29d115754

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:03 |
| **Last Seen** | 2026-06-27 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:03:34` | `cowrie.session.connect` |
| `2026-06-27 19:03:34` | `cowrie.client.version` |
| `2026-06-27 19:03:34` | `cowrie.client.kex` |
| `2026-06-27 19:03:34` | `cowrie.login.success` |
| `2026-06-27 19:03:35` | `cowrie.session.params` |
| `2026-06-27 19:03:35` | `cowrie.command.input` |
| `2026-06-27 19:03:35` | `cowrie.log.closed` |
| `2026-06-27 19:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c79ce1a391

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:04 |
| **Last Seen** | 2026-06-27 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:04:36` | `cowrie.session.connect` |
| `2026-06-27 19:04:36` | `cowrie.client.version` |
| `2026-06-27 19:04:37` | `cowrie.client.kex` |
| `2026-06-27 19:04:37` | `cowrie.login.success` |
| `2026-06-27 19:04:38` | `cowrie.session.params` |
| `2026-06-27 19:04:38` | `cowrie.command.input` |
| `2026-06-27 19:04:38` | `cowrie.log.closed` |
| `2026-06-27 19:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79cc9aebf16e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:05 |
| **Last Seen** | 2026-06-27 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:05:42` | `cowrie.session.connect` |
| `2026-06-27 19:05:42` | `cowrie.client.version` |
| `2026-06-27 19:05:42` | `cowrie.client.kex` |
| `2026-06-27 19:05:42` | `cowrie.login.success` |
| `2026-06-27 19:05:43` | `cowrie.session.params` |
| `2026-06-27 19:05:43` | `cowrie.command.input` |
| `2026-06-27 19:05:43` | `cowrie.log.closed` |
| `2026-06-27 19:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269f8451c8fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:06 |
| **Last Seen** | 2026-06-27 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:06:35` | `cowrie.session.connect` |
| `2026-06-27 19:06:35` | `cowrie.client.version` |
| `2026-06-27 19:06:35` | `cowrie.client.kex` |
| `2026-06-27 19:06:36` | `cowrie.login.success` |
| `2026-06-27 19:06:36` | `cowrie.session.params` |
| `2026-06-27 19:06:36` | `cowrie.command.input` |
| `2026-06-27 19:06:37` | `cowrie.log.closed` |
| `2026-06-27 19:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-facdb1c8f386

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 19:06 |
| **Last Seen** | 2026-06-27 19:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:06:52` | `cowrie.session.connect` |
| `2026-06-27 19:06:54` | `cowrie.client.version` |
| `2026-06-27 19:06:54` | `cowrie.client.kex` |
| `2026-06-27 19:07:01` | `cowrie.login.success` |
| `2026-06-27 19:07:04` | `cowrie.session.params` |
| `2026-06-27 19:07:04` | `cowrie.command.input` |
| `2026-06-27 19:07:05` | `cowrie.log.closed` |
| `2026-06-27 19:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d76122be63

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:07 |
| **Last Seen** | 2026-06-27 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:07:30` | `cowrie.session.connect` |
| `2026-06-27 19:07:30` | `cowrie.client.version` |
| `2026-06-27 19:07:30` | `cowrie.client.kex` |
| `2026-06-27 19:07:31` | `cowrie.login.success` |
| `2026-06-27 19:07:31` | `cowrie.session.params` |
| `2026-06-27 19:07:31` | `cowrie.command.input` |
| `2026-06-27 19:07:32` | `cowrie.log.closed` |
| `2026-06-27 19:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2406c073b7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:08 |
| **Last Seen** | 2026-06-27 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:08:27` | `cowrie.session.connect` |
| `2026-06-27 19:08:27` | `cowrie.client.version` |
| `2026-06-27 19:08:27` | `cowrie.client.kex` |
| `2026-06-27 19:08:27` | `cowrie.login.success` |
| `2026-06-27 19:08:28` | `cowrie.session.params` |
| `2026-06-27 19:08:28` | `cowrie.command.input` |
| `2026-06-27 19:08:28` | `cowrie.log.closed` |
| `2026-06-27 19:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404f405b0974

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:09 |
| **Last Seen** | 2026-06-27 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:09:23` | `cowrie.session.connect` |
| `2026-06-27 19:09:23` | `cowrie.client.version` |
| `2026-06-27 19:09:23` | `cowrie.client.kex` |
| `2026-06-27 19:09:24` | `cowrie.login.success` |
| `2026-06-27 19:09:24` | `cowrie.session.params` |
| `2026-06-27 19:09:24` | `cowrie.command.input` |
| `2026-06-27 19:09:25` | `cowrie.log.closed` |
| `2026-06-27 19:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d0795b3e9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:10 |
| **Last Seen** | 2026-06-27 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:10:20` | `cowrie.session.connect` |
| `2026-06-27 19:10:20` | `cowrie.client.version` |
| `2026-06-27 19:10:20` | `cowrie.client.kex` |
| `2026-06-27 19:10:21` | `cowrie.login.success` |
| `2026-06-27 19:10:22` | `cowrie.session.params` |
| `2026-06-27 19:10:22` | `cowrie.command.input` |
| `2026-06-27 19:10:22` | `cowrie.log.closed` |
| `2026-06-27 19:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07488c6be01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:11 |
| **Last Seen** | 2026-06-27 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:11:19` | `cowrie.session.connect` |
| `2026-06-27 19:11:19` | `cowrie.client.version` |
| `2026-06-27 19:11:19` | `cowrie.client.kex` |
| `2026-06-27 19:11:19` | `cowrie.login.success` |
| `2026-06-27 19:11:20` | `cowrie.session.params` |
| `2026-06-27 19:11:20` | `cowrie.command.input` |
| `2026-06-27 19:11:20` | `cowrie.log.closed` |
| `2026-06-27 19:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708409549ab0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:12 |
| **Last Seen** | 2026-06-27 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:12:18` | `cowrie.session.connect` |
| `2026-06-27 19:12:18` | `cowrie.client.version` |
| `2026-06-27 19:12:18` | `cowrie.client.kex` |
| `2026-06-27 19:12:18` | `cowrie.login.success` |
| `2026-06-27 19:12:19` | `cowrie.session.params` |
| `2026-06-27 19:12:19` | `cowrie.command.input` |
| `2026-06-27 19:12:19` | `cowrie.log.closed` |
| `2026-06-27 19:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408d9ca3868d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 19:12 |
| **Last Seen** | 2026-06-27 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:12:53` | `cowrie.session.connect` |
| `2026-06-27 19:12:53` | `cowrie.client.version` |
| `2026-06-27 19:12:53` | `cowrie.client.kex` |
| `2026-06-27 19:12:54` | `cowrie.login.success` |
| `2026-06-27 19:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816d7d7c5c1a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 19:12 |
| **Last Seen** | 2026-06-27 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:12:53` | `cowrie.session.connect` |
| `2026-06-27 19:12:53` | `cowrie.client.version` |
| `2026-06-27 19:12:53` | `cowrie.client.kex` |
| `2026-06-27 19:12:54` | `cowrie.login.success` |
| `2026-06-27 19:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa3ee75e77f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:13 |
| **Last Seen** | 2026-06-27 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:13:13` | `cowrie.session.connect` |
| `2026-06-27 19:13:13` | `cowrie.client.version` |
| `2026-06-27 19:13:13` | `cowrie.client.kex` |
| `2026-06-27 19:13:13` | `cowrie.login.success` |
| `2026-06-27 19:13:14` | `cowrie.session.params` |
| `2026-06-27 19:13:14` | `cowrie.command.input` |
| `2026-06-27 19:13:14` | `cowrie.log.closed` |
| `2026-06-27 19:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ab380f4edb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:14 |
| **Last Seen** | 2026-06-27 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:14:16` | `cowrie.session.connect` |
| `2026-06-27 19:14:16` | `cowrie.client.version` |
| `2026-06-27 19:14:16` | `cowrie.client.kex` |
| `2026-06-27 19:14:16` | `cowrie.login.success` |
| `2026-06-27 19:14:17` | `cowrie.session.params` |
| `2026-06-27 19:14:17` | `cowrie.command.input` |
| `2026-06-27 19:14:17` | `cowrie.log.closed` |
| `2026-06-27 19:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a55809fd73

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 19:15 |
| **Last Seen** | 2026-06-27 19:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:15:17` | `cowrie.session.connect` |
| `2026-06-27 19:15:17` | `cowrie.client.version` |
| `2026-06-27 19:15:17` | `cowrie.client.kex` |
| `2026-06-27 19:15:19` | `cowrie.login.success` |
| `2026-06-27 19:15:20` | `cowrie.session.params` |
| `2026-06-27 19:15:20` | `cowrie.command.input` |
| `2026-06-27 19:15:20` | `cowrie.log.closed` |
| `2026-06-27 19:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d8efb5f7f10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:15 |
| **Last Seen** | 2026-06-27 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:15:24` | `cowrie.session.connect` |
| `2026-06-27 19:15:24` | `cowrie.client.version` |
| `2026-06-27 19:15:24` | `cowrie.client.kex` |
| `2026-06-27 19:15:25` | `cowrie.login.success` |
| `2026-06-27 19:15:25` | `cowrie.session.params` |
| `2026-06-27 19:15:25` | `cowrie.command.input` |
| `2026-06-27 19:15:26` | `cowrie.log.closed` |
| `2026-06-27 19:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed008ac4d6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:16 |
| **Last Seen** | 2026-06-27 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:16:23` | `cowrie.session.connect` |
| `2026-06-27 19:16:23` | `cowrie.client.version` |
| `2026-06-27 19:16:23` | `cowrie.client.kex` |
| `2026-06-27 19:16:23` | `cowrie.login.success` |
| `2026-06-27 19:16:24` | `cowrie.session.params` |
| `2026-06-27 19:16:24` | `cowrie.command.input` |
| `2026-06-27 19:16:24` | `cowrie.log.closed` |
| `2026-06-27 19:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3198ad5bd9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:17 |
| **Last Seen** | 2026-06-27 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:17:20` | `cowrie.session.connect` |
| `2026-06-27 19:17:20` | `cowrie.client.version` |
| `2026-06-27 19:17:20` | `cowrie.client.kex` |
| `2026-06-27 19:17:20` | `cowrie.login.success` |
| `2026-06-27 19:17:21` | `cowrie.session.params` |
| `2026-06-27 19:17:21` | `cowrie.command.input` |
| `2026-06-27 19:17:21` | `cowrie.log.closed` |
| `2026-06-27 19:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8a61a8acdcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:18 |
| **Last Seen** | 2026-06-27 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:18:16` | `cowrie.session.connect` |
| `2026-06-27 19:18:16` | `cowrie.client.version` |
| `2026-06-27 19:18:17` | `cowrie.client.kex` |
| `2026-06-27 19:18:17` | `cowrie.login.success` |
| `2026-06-27 19:18:18` | `cowrie.session.params` |
| `2026-06-27 19:18:18` | `cowrie.command.input` |
| `2026-06-27 19:18:18` | `cowrie.log.closed` |
| `2026-06-27 19:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afcb405ad5d7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 19:18 |
| **Last Seen** | 2026-06-27 19:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:18:39` | `cowrie.session.connect` |
| `2026-06-27 19:18:40` | `cowrie.client.version` |
| `2026-06-27 19:18:40` | `cowrie.client.kex` |
| `2026-06-27 19:18:47` | `cowrie.login.success` |
| `2026-06-27 19:18:50` | `cowrie.session.params` |
| `2026-06-27 19:18:50` | `cowrie.command.input` |
| `2026-06-27 19:18:52` | `cowrie.log.closed` |
| `2026-06-27 19:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a62236db4c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:19 |
| **Last Seen** | 2026-06-27 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:19:12` | `cowrie.session.connect` |
| `2026-06-27 19:19:12` | `cowrie.client.version` |
| `2026-06-27 19:19:13` | `cowrie.client.kex` |
| `2026-06-27 19:19:13` | `cowrie.login.success` |
| `2026-06-27 19:19:14` | `cowrie.session.params` |
| `2026-06-27 19:19:14` | `cowrie.command.input` |
| `2026-06-27 19:19:14` | `cowrie.log.closed` |
| `2026-06-27 19:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb097e14f719

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:20 |
| **Last Seen** | 2026-06-27 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:20:09` | `cowrie.session.connect` |
| `2026-06-27 19:20:09` | `cowrie.client.version` |
| `2026-06-27 19:20:10` | `cowrie.client.kex` |
| `2026-06-27 19:20:10` | `cowrie.login.success` |
| `2026-06-27 19:20:11` | `cowrie.session.params` |
| `2026-06-27 19:20:11` | `cowrie.command.input` |
| `2026-06-27 19:20:11` | `cowrie.log.closed` |
| `2026-06-27 19:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743a98fac80b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:21 |
| **Last Seen** | 2026-06-27 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:21:08` | `cowrie.session.connect` |
| `2026-06-27 19:21:08` | `cowrie.client.version` |
| `2026-06-27 19:21:08` | `cowrie.client.kex` |
| `2026-06-27 19:21:08` | `cowrie.login.success` |
| `2026-06-27 19:21:09` | `cowrie.session.params` |
| `2026-06-27 19:21:09` | `cowrie.command.input` |
| `2026-06-27 19:21:09` | `cowrie.log.closed` |
| `2026-06-27 19:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe89fa08de4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:22 |
| **Last Seen** | 2026-06-27 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:22:08` | `cowrie.session.connect` |
| `2026-06-27 19:22:08` | `cowrie.client.version` |
| `2026-06-27 19:22:08` | `cowrie.client.kex` |
| `2026-06-27 19:22:08` | `cowrie.login.success` |
| `2026-06-27 19:22:09` | `cowrie.session.params` |
| `2026-06-27 19:22:09` | `cowrie.command.input` |
| `2026-06-27 19:22:09` | `cowrie.log.closed` |
| `2026-06-27 19:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c43601841c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:23 |
| **Last Seen** | 2026-06-27 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:23:07` | `cowrie.session.connect` |
| `2026-06-27 19:23:07` | `cowrie.client.version` |
| `2026-06-27 19:23:07` | `cowrie.client.kex` |
| `2026-06-27 19:23:08` | `cowrie.login.success` |
| `2026-06-27 19:23:09` | `cowrie.session.params` |
| `2026-06-27 19:23:09` | `cowrie.command.input` |
| `2026-06-27 19:23:09` | `cowrie.log.closed` |
| `2026-06-27 19:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a938d3c638ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:24 |
| **Last Seen** | 2026-06-27 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:24:06` | `cowrie.session.connect` |
| `2026-06-27 19:24:06` | `cowrie.client.version` |
| `2026-06-27 19:24:06` | `cowrie.client.kex` |
| `2026-06-27 19:24:06` | `cowrie.login.success` |
| `2026-06-27 19:24:07` | `cowrie.session.params` |
| `2026-06-27 19:24:07` | `cowrie.command.input` |
| `2026-06-27 19:24:07` | `cowrie.log.closed` |
| `2026-06-27 19:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584aafcd9b54

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:25 |
| **Last Seen** | 2026-06-27 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:25:03` | `cowrie.session.connect` |
| `2026-06-27 19:25:03` | `cowrie.client.version` |
| `2026-06-27 19:25:03` | `cowrie.client.kex` |
| `2026-06-27 19:25:04` | `cowrie.login.success` |
| `2026-06-27 19:25:04` | `cowrie.session.params` |
| `2026-06-27 19:25:04` | `cowrie.command.input` |
| `2026-06-27 19:25:04` | `cowrie.log.closed` |
| `2026-06-27 19:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095e6b2582e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:26 |
| **Last Seen** | 2026-06-27 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:26:01` | `cowrie.session.connect` |
| `2026-06-27 19:26:01` | `cowrie.client.version` |
| `2026-06-27 19:26:01` | `cowrie.client.kex` |
| `2026-06-27 19:26:01` | `cowrie.login.success` |
| `2026-06-27 19:26:02` | `cowrie.session.params` |
| `2026-06-27 19:26:02` | `cowrie.command.input` |
| `2026-06-27 19:26:02` | `cowrie.log.closed` |
| `2026-06-27 19:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51be64f4e85a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:26 |
| **Last Seen** | 2026-06-27 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:26:59` | `cowrie.session.connect` |
| `2026-06-27 19:26:59` | `cowrie.client.version` |
| `2026-06-27 19:27:00` | `cowrie.client.kex` |
| `2026-06-27 19:27:00` | `cowrie.login.success` |
| `2026-06-27 19:27:01` | `cowrie.session.params` |
| `2026-06-27 19:27:01` | `cowrie.command.input` |
| `2026-06-27 19:27:01` | `cowrie.log.closed` |
| `2026-06-27 19:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33aaabe884f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:28 |
| **Last Seen** | 2026-06-27 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:28:00` | `cowrie.session.connect` |
| `2026-06-27 19:28:00` | `cowrie.client.version` |
| `2026-06-27 19:28:00` | `cowrie.client.kex` |
| `2026-06-27 19:28:00` | `cowrie.login.success` |
| `2026-06-27 19:28:01` | `cowrie.session.params` |
| `2026-06-27 19:28:01` | `cowrie.command.input` |
| `2026-06-27 19:28:01` | `cowrie.log.closed` |
| `2026-06-27 19:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e54754f9678

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-27 19:28 |
| **Last Seen** | 2026-06-27 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; dmidecode -s p, uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:28:48` | `cowrie.session.connect` |
| `2026-06-27 19:28:48` | `cowrie.client.version` |
| `2026-06-27 19:28:48` | `cowrie.client.kex` |
| `2026-06-27 19:28:48` | `cowrie.login.success` |
| `2026-06-27 19:28:49` | `cowrie.session.params` |
| `2026-06-27 19:28:49` | `cowrie.command.input` |
| `2026-06-27 19:28:49` | `cowrie.command.input` |
| `2026-06-27 19:28:49` | `cowrie.command.input` |
| `2026-06-27 19:28:49` | `cowrie.command.input` |
| `2026-06-27 19:28:49` | `cowrie.log.closed` |
| `2026-06-27 19:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42755b6b0ce9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:29 |
| **Last Seen** | 2026-06-27 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:29:00` | `cowrie.session.connect` |
| `2026-06-27 19:29:00` | `cowrie.client.version` |
| `2026-06-27 19:29:00` | `cowrie.client.kex` |
| `2026-06-27 19:29:00` | `cowrie.login.success` |
| `2026-06-27 19:29:01` | `cowrie.session.params` |
| `2026-06-27 19:29:01` | `cowrie.command.input` |
| `2026-06-27 19:29:01` | `cowrie.log.closed` |
| `2026-06-27 19:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201b49e91edc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 19:29 |
| **Last Seen** | 2026-06-27 19:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:29:59` | `cowrie.session.connect` |
| `2026-06-27 19:30:01` | `cowrie.client.version` |
| `2026-06-27 19:30:01` | `cowrie.client.kex` |
| `2026-06-27 19:30:03` | `cowrie.login.success` |
| `2026-06-27 19:30:05` | `cowrie.session.params` |
| `2026-06-27 19:30:05` | `cowrie.command.input` |
| `2026-06-27 19:30:05` | `cowrie.log.closed` |
| `2026-06-27 19:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed328f792c1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:30 |
| **Last Seen** | 2026-06-27 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:30:00` | `cowrie.session.connect` |
| `2026-06-27 19:30:00` | `cowrie.client.version` |
| `2026-06-27 19:30:00` | `cowrie.client.kex` |
| `2026-06-27 19:30:00` | `cowrie.login.success` |
| `2026-06-27 19:30:01` | `cowrie.session.params` |
| `2026-06-27 19:30:01` | `cowrie.command.input` |
| `2026-06-27 19:30:01` | `cowrie.log.closed` |
| `2026-06-27 19:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fcdd4de08a5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 19:30 |
| **Last Seen** | 2026-06-27 19:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:30:27` | `cowrie.session.connect` |
| `2026-06-27 19:30:28` | `cowrie.client.version` |
| `2026-06-27 19:30:28` | `cowrie.client.kex` |
| `2026-06-27 19:30:34` | `cowrie.login.success` |
| `2026-06-27 19:30:38` | `cowrie.session.params` |
| `2026-06-27 19:30:38` | `cowrie.command.input` |
| `2026-06-27 19:30:39` | `cowrie.log.closed` |
| `2026-06-27 19:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758fd45f8603

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:30 |
| **Last Seen** | 2026-06-27 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:30:58` | `cowrie.session.connect` |
| `2026-06-27 19:30:58` | `cowrie.client.version` |
| `2026-06-27 19:30:59` | `cowrie.client.kex` |
| `2026-06-27 19:30:59` | `cowrie.login.success` |
| `2026-06-27 19:31:00` | `cowrie.session.params` |
| `2026-06-27 19:31:00` | `cowrie.command.input` |
| `2026-06-27 19:31:00` | `cowrie.log.closed` |
| `2026-06-27 19:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ccb375c022

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:31 |
| **Last Seen** | 2026-06-27 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:31:58` | `cowrie.session.connect` |
| `2026-06-27 19:31:58` | `cowrie.client.version` |
| `2026-06-27 19:31:58` | `cowrie.client.kex` |
| `2026-06-27 19:31:58` | `cowrie.login.success` |
| `2026-06-27 19:31:59` | `cowrie.session.params` |
| `2026-06-27 19:31:59` | `cowrie.command.input` |
| `2026-06-27 19:31:59` | `cowrie.log.closed` |
| `2026-06-27 19:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0e7815879e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:32 |
| **Last Seen** | 2026-06-27 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:32:59` | `cowrie.session.connect` |
| `2026-06-27 19:32:59` | `cowrie.client.version` |
| `2026-06-27 19:32:59` | `cowrie.client.kex` |
| `2026-06-27 19:33:00` | `cowrie.login.success` |
| `2026-06-27 19:33:00` | `cowrie.session.params` |
| `2026-06-27 19:33:00` | `cowrie.command.input` |
| `2026-06-27 19:33:00` | `cowrie.log.closed` |
| `2026-06-27 19:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95537d8c9784

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:34 |
| **Last Seen** | 2026-06-27 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:34:01` | `cowrie.session.connect` |
| `2026-06-27 19:34:01` | `cowrie.client.version` |
| `2026-06-27 19:34:01` | `cowrie.client.kex` |
| `2026-06-27 19:34:01` | `cowrie.login.success` |
| `2026-06-27 19:34:02` | `cowrie.session.params` |
| `2026-06-27 19:34:02` | `cowrie.command.input` |
| `2026-06-27 19:34:02` | `cowrie.log.closed` |
| `2026-06-27 19:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c7c34c7aaad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:35 |
| **Last Seen** | 2026-06-27 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:35:02` | `cowrie.session.connect` |
| `2026-06-27 19:35:02` | `cowrie.client.version` |
| `2026-06-27 19:35:02` | `cowrie.client.kex` |
| `2026-06-27 19:35:02` | `cowrie.login.success` |
| `2026-06-27 19:35:03` | `cowrie.session.params` |
| `2026-06-27 19:35:03` | `cowrie.command.input` |
| `2026-06-27 19:35:03` | `cowrie.log.closed` |
| `2026-06-27 19:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1c0a0fe93e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:36 |
| **Last Seen** | 2026-06-27 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:36:03` | `cowrie.session.connect` |
| `2026-06-27 19:36:03` | `cowrie.client.version` |
| `2026-06-27 19:36:03` | `cowrie.client.kex` |
| `2026-06-27 19:36:03` | `cowrie.login.success` |
| `2026-06-27 19:36:04` | `cowrie.session.params` |
| `2026-06-27 19:36:04` | `cowrie.command.input` |
| `2026-06-27 19:36:04` | `cowrie.log.closed` |
| `2026-06-27 19:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f19aef48b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:37 |
| **Last Seen** | 2026-06-27 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:37:04` | `cowrie.session.connect` |
| `2026-06-27 19:37:04` | `cowrie.client.version` |
| `2026-06-27 19:37:04` | `cowrie.client.kex` |
| `2026-06-27 19:37:04` | `cowrie.login.success` |
| `2026-06-27 19:37:05` | `cowrie.session.params` |
| `2026-06-27 19:37:05` | `cowrie.command.input` |
| `2026-06-27 19:37:05` | `cowrie.log.closed` |
| `2026-06-27 19:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f835a73cb3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:38 |
| **Last Seen** | 2026-06-27 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:38:04` | `cowrie.session.connect` |
| `2026-06-27 19:38:04` | `cowrie.client.version` |
| `2026-06-27 19:38:05` | `cowrie.client.kex` |
| `2026-06-27 19:38:05` | `cowrie.login.success` |
| `2026-06-27 19:38:06` | `cowrie.session.params` |
| `2026-06-27 19:38:06` | `cowrie.command.input` |
| `2026-06-27 19:38:06` | `cowrie.log.closed` |
| `2026-06-27 19:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716fab3008cf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:39 |
| **Last Seen** | 2026-06-27 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:39:06` | `cowrie.session.connect` |
| `2026-06-27 19:39:06` | `cowrie.client.version` |
| `2026-06-27 19:39:06` | `cowrie.client.kex` |
| `2026-06-27 19:39:07` | `cowrie.login.success` |
| `2026-06-27 19:39:08` | `cowrie.session.params` |
| `2026-06-27 19:39:08` | `cowrie.command.input` |
| `2026-06-27 19:39:08` | `cowrie.log.closed` |
| `2026-06-27 19:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d7fc87708a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:40 |
| **Last Seen** | 2026-06-27 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:40:09` | `cowrie.session.connect` |
| `2026-06-27 19:40:09` | `cowrie.client.version` |
| `2026-06-27 19:40:09` | `cowrie.client.kex` |
| `2026-06-27 19:40:09` | `cowrie.login.success` |
| `2026-06-27 19:40:10` | `cowrie.session.params` |
| `2026-06-27 19:40:10` | `cowrie.command.input` |
| `2026-06-27 19:40:10` | `cowrie.log.closed` |
| `2026-06-27 19:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbaf53756ff3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:41 |
| **Last Seen** | 2026-06-27 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:41:13` | `cowrie.session.connect` |
| `2026-06-27 19:41:13` | `cowrie.client.version` |
| `2026-06-27 19:41:13` | `cowrie.client.kex` |
| `2026-06-27 19:41:14` | `cowrie.login.success` |
| `2026-06-27 19:41:15` | `cowrie.session.params` |
| `2026-06-27 19:41:15` | `cowrie.command.input` |
| `2026-06-27 19:41:15` | `cowrie.log.closed` |
| `2026-06-27 19:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28eb33c0b173

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 19:42 |
| **Last Seen** | 2026-06-27 19:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:42:01` | `cowrie.session.connect` |
| `2026-06-27 19:42:02` | `cowrie.client.version` |
| `2026-06-27 19:42:02` | `cowrie.client.kex` |
| `2026-06-27 19:42:08` | `cowrie.login.success` |
| `2026-06-27 19:42:11` | `cowrie.session.params` |
| `2026-06-27 19:42:11` | `cowrie.command.input` |
| `2026-06-27 19:42:12` | `cowrie.log.closed` |
| `2026-06-27 19:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04597663b14f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:42 |
| **Last Seen** | 2026-06-27 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:42:18` | `cowrie.session.connect` |
| `2026-06-27 19:42:18` | `cowrie.client.version` |
| `2026-06-27 19:42:18` | `cowrie.client.kex` |
| `2026-06-27 19:42:18` | `cowrie.login.success` |
| `2026-06-27 19:42:19` | `cowrie.session.params` |
| `2026-06-27 19:42:19` | `cowrie.command.input` |
| `2026-06-27 19:42:19` | `cowrie.log.closed` |
| `2026-06-27 19:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5023aa730bb5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:43 |
| **Last Seen** | 2026-06-27 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:43:22` | `cowrie.session.connect` |
| `2026-06-27 19:43:22` | `cowrie.client.version` |
| `2026-06-27 19:43:22` | `cowrie.client.kex` |
| `2026-06-27 19:43:22` | `cowrie.login.success` |
| `2026-06-27 19:43:23` | `cowrie.session.params` |
| `2026-06-27 19:43:23` | `cowrie.command.input` |
| `2026-06-27 19:43:23` | `cowrie.log.closed` |
| `2026-06-27 19:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac1b0a8da73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:44 |
| **Last Seen** | 2026-06-27 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:44:25` | `cowrie.session.connect` |
| `2026-06-27 19:44:25` | `cowrie.client.version` |
| `2026-06-27 19:44:25` | `cowrie.client.kex` |
| `2026-06-27 19:44:25` | `cowrie.login.success` |
| `2026-06-27 19:44:26` | `cowrie.session.params` |
| `2026-06-27 19:44:26` | `cowrie.command.input` |
| `2026-06-27 19:44:26` | `cowrie.log.closed` |
| `2026-06-27 19:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9867f88c0211

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 19:44 |
| **Last Seen** | 2026-06-27 19:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:44:39` | `cowrie.session.connect` |
| `2026-06-27 19:44:39` | `cowrie.client.version` |
| `2026-06-27 19:44:39` | `cowrie.client.kex` |
| `2026-06-27 19:44:41` | `cowrie.login.success` |
| `2026-06-27 19:44:42` | `cowrie.session.params` |
| `2026-06-27 19:44:42` | `cowrie.command.input` |
| `2026-06-27 19:44:42` | `cowrie.log.closed` |
| `2026-06-27 19:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af151e2de25a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-27 19:44 |
| **Last Seen** | 2026-06-27 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; dmidecode -s p, uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:44:54` | `cowrie.session.connect` |
| `2026-06-27 19:44:54` | `cowrie.client.version` |
| `2026-06-27 19:44:54` | `cowrie.client.kex` |
| `2026-06-27 19:44:54` | `cowrie.login.success` |
| `2026-06-27 19:44:55` | `cowrie.session.params` |
| `2026-06-27 19:44:55` | `cowrie.command.input` |
| `2026-06-27 19:44:55` | `cowrie.command.input` |
| `2026-06-27 19:44:55` | `cowrie.command.input` |
| `2026-06-27 19:44:55` | `cowrie.command.input` |
| `2026-06-27 19:44:55` | `cowrie.log.closed` |
| `2026-06-27 19:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23668d95869

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:45 |
| **Last Seen** | 2026-06-27 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:45:29` | `cowrie.session.connect` |
| `2026-06-27 19:45:29` | `cowrie.client.version` |
| `2026-06-27 19:45:29` | `cowrie.client.kex` |
| `2026-06-27 19:45:29` | `cowrie.login.success` |
| `2026-06-27 19:45:30` | `cowrie.session.params` |
| `2026-06-27 19:45:30` | `cowrie.command.input` |
| `2026-06-27 19:45:30` | `cowrie.log.closed` |
| `2026-06-27 19:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb3c5d96476

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:46 |
| **Last Seen** | 2026-06-27 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:46:35` | `cowrie.session.connect` |
| `2026-06-27 19:46:35` | `cowrie.client.version` |
| `2026-06-27 19:46:36` | `cowrie.client.kex` |
| `2026-06-27 19:46:36` | `cowrie.login.success` |
| `2026-06-27 19:46:37` | `cowrie.session.params` |
| `2026-06-27 19:46:37` | `cowrie.command.input` |
| `2026-06-27 19:46:37` | `cowrie.log.closed` |
| `2026-06-27 19:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4756e9817ccd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:47 |
| **Last Seen** | 2026-06-27 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:47:44` | `cowrie.session.connect` |
| `2026-06-27 19:47:44` | `cowrie.client.version` |
| `2026-06-27 19:47:44` | `cowrie.client.kex` |
| `2026-06-27 19:47:44` | `cowrie.login.success` |
| `2026-06-27 19:47:45` | `cowrie.session.params` |
| `2026-06-27 19:47:45` | `cowrie.command.input` |
| `2026-06-27 19:47:45` | `cowrie.log.closed` |
| `2026-06-27 19:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db489168e69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:48 |
| **Last Seen** | 2026-06-27 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:48:51` | `cowrie.session.connect` |
| `2026-06-27 19:48:51` | `cowrie.client.version` |
| `2026-06-27 19:48:51` | `cowrie.client.kex` |
| `2026-06-27 19:48:52` | `cowrie.login.success` |
| `2026-06-27 19:48:52` | `cowrie.session.params` |
| `2026-06-27 19:48:52` | `cowrie.command.input` |
| `2026-06-27 19:48:52` | `cowrie.log.closed` |
| `2026-06-27 19:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a64724eaa9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:49 |
| **Last Seen** | 2026-06-27 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:49:57` | `cowrie.session.connect` |
| `2026-06-27 19:49:57` | `cowrie.client.version` |
| `2026-06-27 19:49:57` | `cowrie.client.kex` |
| `2026-06-27 19:49:57` | `cowrie.login.success` |
| `2026-06-27 19:49:58` | `cowrie.session.params` |
| `2026-06-27 19:49:58` | `cowrie.command.input` |
| `2026-06-27 19:49:58` | `cowrie.log.closed` |
| `2026-06-27 19:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2a87298e8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:51 |
| **Last Seen** | 2026-06-27 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:51:03` | `cowrie.session.connect` |
| `2026-06-27 19:51:03` | `cowrie.client.version` |
| `2026-06-27 19:51:03` | `cowrie.client.kex` |
| `2026-06-27 19:51:03` | `cowrie.login.success` |
| `2026-06-27 19:51:04` | `cowrie.session.params` |
| `2026-06-27 19:51:04` | `cowrie.command.input` |
| `2026-06-27 19:51:04` | `cowrie.log.closed` |
| `2026-06-27 19:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dbd637e0637

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:52 |
| **Last Seen** | 2026-06-27 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:52:09` | `cowrie.session.connect` |
| `2026-06-27 19:52:09` | `cowrie.client.version` |
| `2026-06-27 19:52:09` | `cowrie.client.kex` |
| `2026-06-27 19:52:09` | `cowrie.login.success` |
| `2026-06-27 19:52:10` | `cowrie.session.params` |
| `2026-06-27 19:52:10` | `cowrie.command.input` |
| `2026-06-27 19:52:10` | `cowrie.log.closed` |
| `2026-06-27 19:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4be5e73a7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:53 |
| **Last Seen** | 2026-06-27 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:53:18` | `cowrie.session.connect` |
| `2026-06-27 19:53:18` | `cowrie.client.version` |
| `2026-06-27 19:53:18` | `cowrie.client.kex` |
| `2026-06-27 19:53:18` | `cowrie.login.success` |
| `2026-06-27 19:53:19` | `cowrie.session.params` |
| `2026-06-27 19:53:19` | `cowrie.command.input` |
| `2026-06-27 19:53:19` | `cowrie.log.closed` |
| `2026-06-27 19:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02dd9fc46363

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 19:53 |
| **Last Seen** | 2026-06-27 19:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:53:19` | `cowrie.session.connect` |
| `2026-06-27 19:53:20` | `cowrie.client.version` |
| `2026-06-27 19:53:20` | `cowrie.client.kex` |
| `2026-06-27 19:53:26` | `cowrie.login.success` |
| `2026-06-27 19:53:30` | `cowrie.session.params` |
| `2026-06-27 19:53:30` | `cowrie.command.input` |
| `2026-06-27 19:53:31` | `cowrie.log.closed` |
| `2026-06-27 19:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1011ab8158e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:54 |
| **Last Seen** | 2026-06-27 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:54:27` | `cowrie.session.connect` |
| `2026-06-27 19:54:27` | `cowrie.client.version` |
| `2026-06-27 19:54:27` | `cowrie.client.kex` |
| `2026-06-27 19:54:28` | `cowrie.login.success` |
| `2026-06-27 19:54:29` | `cowrie.session.params` |
| `2026-06-27 19:54:29` | `cowrie.command.input` |
| `2026-06-27 19:54:29` | `cowrie.log.closed` |
| `2026-06-27 19:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79beb610ebb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:55 |
| **Last Seen** | 2026-06-27 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:55:34` | `cowrie.session.connect` |
| `2026-06-27 19:55:34` | `cowrie.client.version` |
| `2026-06-27 19:55:34` | `cowrie.client.kex` |
| `2026-06-27 19:55:35` | `cowrie.login.success` |
| `2026-06-27 19:55:36` | `cowrie.session.params` |
| `2026-06-27 19:55:36` | `cowrie.command.input` |
| `2026-06-27 19:55:36` | `cowrie.log.closed` |
| `2026-06-27 19:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-845b46d575cf

| Field | Detail |
|---|---|
| **Source IP** | `138.68.243[.]18` |
| **First Seen** | 2026-06-27 19:56 |
| **Last Seen** | 2026-06-27 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:56:15` | `cowrie.session.connect` |
| `2026-06-27 19:56:15` | `cowrie.client.version` |
| `2026-06-27 19:56:15` | `cowrie.client.kex` |
| `2026-06-27 19:56:15` | `cowrie.login.success` |
| `2026-06-27 19:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `138.68.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aff64d3ef01

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-27 19:56 |
| **Last Seen** | 2026-06-27 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:56:15` | `cowrie.session.connect` |
| `2026-06-27 19:56:15` | `cowrie.client.version` |
| `2026-06-27 19:56:15` | `cowrie.client.kex` |
| `2026-06-27 19:56:15` | `cowrie.login.success` |
| `2026-06-27 19:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162633e0fcd4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:56 |
| **Last Seen** | 2026-06-27 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:56:40` | `cowrie.session.connect` |
| `2026-06-27 19:56:40` | `cowrie.client.version` |
| `2026-06-27 19:56:40` | `cowrie.client.kex` |
| `2026-06-27 19:56:40` | `cowrie.login.success` |
| `2026-06-27 19:56:41` | `cowrie.session.params` |
| `2026-06-27 19:56:41` | `cowrie.command.input` |
| `2026-06-27 19:56:41` | `cowrie.log.closed` |
| `2026-06-27 19:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d63dfec6b9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:57 |
| **Last Seen** | 2026-06-27 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:57:46` | `cowrie.session.connect` |
| `2026-06-27 19:57:46` | `cowrie.client.version` |
| `2026-06-27 19:57:46` | `cowrie.client.kex` |
| `2026-06-27 19:57:47` | `cowrie.login.success` |
| `2026-06-27 19:57:48` | `cowrie.session.params` |
| `2026-06-27 19:57:48` | `cowrie.command.input` |
| `2026-06-27 19:57:48` | `cowrie.log.closed` |
| `2026-06-27 19:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef4752a487b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-27 19:58 |
| **Last Seen** | 2026-06-27 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; dmidecode -s p, uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:58:02` | `cowrie.session.connect` |
| `2026-06-27 19:58:02` | `cowrie.client.version` |
| `2026-06-27 19:58:03` | `cowrie.client.kex` |
| `2026-06-27 19:58:03` | `cowrie.login.success` |
| `2026-06-27 19:58:04` | `cowrie.session.params` |
| `2026-06-27 19:58:04` | `cowrie.command.input` |
| `2026-06-27 19:58:04` | `cowrie.command.input` |
| `2026-06-27 19:58:04` | `cowrie.command.input` |
| `2026-06-27 19:58:04` | `cowrie.command.input` |
| `2026-06-27 19:58:04` | `cowrie.log.closed` |
| `2026-06-27 19:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9148229e8ea4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 19:58 |
| **Last Seen** | 2026-06-27 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:58:55` | `cowrie.session.connect` |
| `2026-06-27 19:58:55` | `cowrie.client.version` |
| `2026-06-27 19:58:55` | `cowrie.client.kex` |
| `2026-06-27 19:58:55` | `cowrie.login.success` |
| `2026-06-27 19:58:56` | `cowrie.session.params` |
| `2026-06-27 19:58:56` | `cowrie.command.input` |
| `2026-06-27 19:58:56` | `cowrie.log.closed` |
| `2026-06-27 19:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537fac267548

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 19:59 |
| **Last Seen** | 2026-06-27 19:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 19:59:24` | `cowrie.session.connect` |
| `2026-06-27 19:59:25` | `cowrie.client.version` |
| `2026-06-27 19:59:25` | `cowrie.client.kex` |
| `2026-06-27 19:59:27` | `cowrie.login.success` |
| `2026-06-27 19:59:28` | `cowrie.session.params` |
| `2026-06-27 19:59:28` | `cowrie.command.input` |
| `2026-06-27 19:59:28` | `cowrie.log.closed` |
| `2026-06-27 19:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd540b6dd47

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:00 |
| **Last Seen** | 2026-06-27 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:00:06` | `cowrie.session.connect` |
| `2026-06-27 20:00:06` | `cowrie.client.version` |
| `2026-06-27 20:00:06` | `cowrie.client.kex` |
| `2026-06-27 20:00:06` | `cowrie.login.success` |
| `2026-06-27 20:00:07` | `cowrie.session.params` |
| `2026-06-27 20:00:07` | `cowrie.command.input` |
| `2026-06-27 20:00:07` | `cowrie.log.closed` |
| `2026-06-27 20:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c71d3ddd8d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:00 |
| **Last Seen** | 2026-06-27 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:00:53` | `cowrie.session.connect` |
| `2026-06-27 20:00:53` | `cowrie.client.version` |
| `2026-06-27 20:00:54` | `cowrie.client.kex` |
| `2026-06-27 20:00:54` | `cowrie.login.success` |
| `2026-06-27 20:00:55` | `cowrie.session.params` |
| `2026-06-27 20:00:55` | `cowrie.command.input` |
| `2026-06-27 20:00:55` | `cowrie.log.closed` |
| `2026-06-27 20:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ff6b4fd228

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:01 |
| **Last Seen** | 2026-06-27 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:01:39` | `cowrie.session.connect` |
| `2026-06-27 20:01:39` | `cowrie.client.version` |
| `2026-06-27 20:01:39` | `cowrie.client.kex` |
| `2026-06-27 20:01:39` | `cowrie.login.success` |
| `2026-06-27 20:01:40` | `cowrie.session.params` |
| `2026-06-27 20:01:40` | `cowrie.command.input` |
| `2026-06-27 20:01:40` | `cowrie.log.closed` |
| `2026-06-27 20:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4435a29bcdbb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:02 |
| **Last Seen** | 2026-06-27 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:02:23` | `cowrie.session.connect` |
| `2026-06-27 20:02:23` | `cowrie.client.version` |
| `2026-06-27 20:02:23` | `cowrie.client.kex` |
| `2026-06-27 20:02:23` | `cowrie.login.success` |
| `2026-06-27 20:02:24` | `cowrie.session.params` |
| `2026-06-27 20:02:24` | `cowrie.command.input` |
| `2026-06-27 20:02:24` | `cowrie.log.closed` |
| `2026-06-27 20:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663e3efd1bc2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:03 |
| **Last Seen** | 2026-06-27 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:03:06` | `cowrie.session.connect` |
| `2026-06-27 20:03:06` | `cowrie.client.version` |
| `2026-06-27 20:03:07` | `cowrie.client.kex` |
| `2026-06-27 20:03:07` | `cowrie.login.success` |
| `2026-06-27 20:03:08` | `cowrie.session.params` |
| `2026-06-27 20:03:08` | `cowrie.command.input` |
| `2026-06-27 20:03:08` | `cowrie.log.closed` |
| `2026-06-27 20:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3013b2c85b81

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:03 |
| **Last Seen** | 2026-06-27 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:03:50` | `cowrie.session.connect` |
| `2026-06-27 20:03:50` | `cowrie.client.version` |
| `2026-06-27 20:03:51` | `cowrie.client.kex` |
| `2026-06-27 20:03:51` | `cowrie.login.success` |
| `2026-06-27 20:03:52` | `cowrie.session.params` |
| `2026-06-27 20:03:52` | `cowrie.command.input` |
| `2026-06-27 20:03:52` | `cowrie.log.closed` |
| `2026-06-27 20:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdaffcfeb77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:04 |
| **Last Seen** | 2026-06-27 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:04:34` | `cowrie.session.connect` |
| `2026-06-27 20:04:34` | `cowrie.client.version` |
| `2026-06-27 20:04:34` | `cowrie.client.kex` |
| `2026-06-27 20:04:35` | `cowrie.login.success` |
| `2026-06-27 20:04:35` | `cowrie.session.params` |
| `2026-06-27 20:04:35` | `cowrie.command.input` |
| `2026-06-27 20:04:36` | `cowrie.log.closed` |
| `2026-06-27 20:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af4c1ee0b35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:05 |
| **Last Seen** | 2026-06-27 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:05:18` | `cowrie.session.connect` |
| `2026-06-27 20:05:18` | `cowrie.client.version` |
| `2026-06-27 20:05:18` | `cowrie.client.kex` |
| `2026-06-27 20:05:19` | `cowrie.login.success` |
| `2026-06-27 20:05:20` | `cowrie.session.params` |
| `2026-06-27 20:05:20` | `cowrie.command.input` |
| `2026-06-27 20:05:20` | `cowrie.log.closed` |
| `2026-06-27 20:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b85e848fa5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 20:05 |
| **Last Seen** | 2026-06-27 20:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:05:20` | `cowrie.session.connect` |
| `2026-06-27 20:05:21` | `cowrie.client.version` |
| `2026-06-27 20:05:21` | `cowrie.client.kex` |
| `2026-06-27 20:05:27` | `cowrie.login.success` |
| `2026-06-27 20:05:31` | `cowrie.session.params` |
| `2026-06-27 20:05:31` | `cowrie.command.input` |
| `2026-06-27 20:05:32` | `cowrie.log.closed` |
| `2026-06-27 20:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb7f87e0418

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:06 |
| **Last Seen** | 2026-06-27 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:06:04` | `cowrie.session.connect` |
| `2026-06-27 20:06:04` | `cowrie.client.version` |
| `2026-06-27 20:06:04` | `cowrie.client.kex` |
| `2026-06-27 20:06:04` | `cowrie.login.success` |
| `2026-06-27 20:06:05` | `cowrie.session.params` |
| `2026-06-27 20:06:05` | `cowrie.command.input` |
| `2026-06-27 20:06:05` | `cowrie.log.closed` |
| `2026-06-27 20:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eff48f8e091

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:06 |
| **Last Seen** | 2026-06-27 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:06:49` | `cowrie.session.connect` |
| `2026-06-27 20:06:49` | `cowrie.client.version` |
| `2026-06-27 20:06:49` | `cowrie.client.kex` |
| `2026-06-27 20:06:49` | `cowrie.login.success` |
| `2026-06-27 20:06:50` | `cowrie.session.params` |
| `2026-06-27 20:06:50` | `cowrie.command.input` |
| `2026-06-27 20:06:50` | `cowrie.log.closed` |
| `2026-06-27 20:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c7287c3d21

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 20:07 |
| **Last Seen** | 2026-06-27 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:07:11` | `cowrie.session.connect` |
| `2026-06-27 20:07:11` | `cowrie.client.version` |
| `2026-06-27 20:07:11` | `cowrie.client.kex` |
| `2026-06-27 20:07:11` | `cowrie.login.success` |
| `2026-06-27 20:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e9bb87a585

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 20:07 |
| **Last Seen** | 2026-06-27 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:07:11` | `cowrie.session.connect` |
| `2026-06-27 20:07:11` | `cowrie.client.version` |
| `2026-06-27 20:07:11` | `cowrie.client.kex` |
| `2026-06-27 20:07:11` | `cowrie.login.success` |
| `2026-06-27 20:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7bad119bffe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:07 |
| **Last Seen** | 2026-06-27 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:07:34` | `cowrie.session.connect` |
| `2026-06-27 20:07:34` | `cowrie.client.version` |
| `2026-06-27 20:07:34` | `cowrie.client.kex` |
| `2026-06-27 20:07:34` | `cowrie.login.success` |
| `2026-06-27 20:07:35` | `cowrie.session.params` |
| `2026-06-27 20:07:35` | `cowrie.command.input` |
| `2026-06-27 20:07:35` | `cowrie.log.closed` |
| `2026-06-27 20:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a1dc0e6374

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:08 |
| **Last Seen** | 2026-06-27 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:08:18` | `cowrie.session.connect` |
| `2026-06-27 20:08:18` | `cowrie.client.version` |
| `2026-06-27 20:08:18` | `cowrie.client.kex` |
| `2026-06-27 20:08:19` | `cowrie.login.success` |
| `2026-06-27 20:08:19` | `cowrie.session.params` |
| `2026-06-27 20:08:19` | `cowrie.command.input` |
| `2026-06-27 20:08:20` | `cowrie.log.closed` |
| `2026-06-27 20:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b442476f83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:09 |
| **Last Seen** | 2026-06-27 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:09:02` | `cowrie.session.connect` |
| `2026-06-27 20:09:02` | `cowrie.client.version` |
| `2026-06-27 20:09:02` | `cowrie.client.kex` |
| `2026-06-27 20:09:02` | `cowrie.login.success` |
| `2026-06-27 20:09:03` | `cowrie.session.params` |
| `2026-06-27 20:09:03` | `cowrie.command.input` |
| `2026-06-27 20:09:03` | `cowrie.log.closed` |
| `2026-06-27 20:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdfcfc42355

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:09 |
| **Last Seen** | 2026-06-27 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:09:45` | `cowrie.session.connect` |
| `2026-06-27 20:09:45` | `cowrie.client.version` |
| `2026-06-27 20:09:45` | `cowrie.client.kex` |
| `2026-06-27 20:09:46` | `cowrie.login.success` |
| `2026-06-27 20:09:47` | `cowrie.session.params` |
| `2026-06-27 20:09:47` | `cowrie.command.input` |
| `2026-06-27 20:09:47` | `cowrie.log.closed` |
| `2026-06-27 20:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76639713ebb6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-27 20:10 |
| **Last Seen** | 2026-06-27 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; dmidecode -s p, uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:10:06` | `cowrie.session.connect` |
| `2026-06-27 20:10:06` | `cowrie.client.version` |
| `2026-06-27 20:10:06` | `cowrie.client.kex` |
| `2026-06-27 20:10:06` | `cowrie.login.success` |
| `2026-06-27 20:10:07` | `cowrie.session.params` |
| `2026-06-27 20:10:07` | `cowrie.command.input` |
| `2026-06-27 20:10:07` | `cowrie.command.input` |
| `2026-06-27 20:10:07` | `cowrie.command.input` |
| `2026-06-27 20:10:07` | `cowrie.command.input` |
| `2026-06-27 20:10:07` | `cowrie.log.closed` |
| `2026-06-27 20:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31681fd0aea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:10 |
| **Last Seen** | 2026-06-27 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:10:30` | `cowrie.session.connect` |
| `2026-06-27 20:10:30` | `cowrie.client.version` |
| `2026-06-27 20:10:30` | `cowrie.client.kex` |
| `2026-06-27 20:10:31` | `cowrie.login.success` |
| `2026-06-27 20:10:31` | `cowrie.session.params` |
| `2026-06-27 20:10:31` | `cowrie.command.input` |
| `2026-06-27 20:10:31` | `cowrie.log.closed` |
| `2026-06-27 20:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4d73dfd42d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:11 |
| **Last Seen** | 2026-06-27 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:11:16` | `cowrie.session.connect` |
| `2026-06-27 20:11:16` | `cowrie.client.version` |
| `2026-06-27 20:11:16` | `cowrie.client.kex` |
| `2026-06-27 20:11:16` | `cowrie.login.success` |
| `2026-06-27 20:11:17` | `cowrie.session.params` |
| `2026-06-27 20:11:17` | `cowrie.command.input` |
| `2026-06-27 20:11:17` | `cowrie.log.closed` |
| `2026-06-27 20:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d714d1a895

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:12 |
| **Last Seen** | 2026-06-27 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:12:02` | `cowrie.session.connect` |
| `2026-06-27 20:12:02` | `cowrie.client.version` |
| `2026-06-27 20:12:02` | `cowrie.client.kex` |
| `2026-06-27 20:12:03` | `cowrie.login.success` |
| `2026-06-27 20:12:03` | `cowrie.session.params` |
| `2026-06-27 20:12:03` | `cowrie.command.input` |
| `2026-06-27 20:12:03` | `cowrie.log.closed` |
| `2026-06-27 20:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60dc5d4fb6d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:12 |
| **Last Seen** | 2026-06-27 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:12:50` | `cowrie.session.connect` |
| `2026-06-27 20:12:50` | `cowrie.client.version` |
| `2026-06-27 20:12:50` | `cowrie.client.kex` |
| `2026-06-27 20:12:50` | `cowrie.login.success` |
| `2026-06-27 20:12:51` | `cowrie.session.params` |
| `2026-06-27 20:12:51` | `cowrie.command.input` |
| `2026-06-27 20:12:51` | `cowrie.log.closed` |
| `2026-06-27 20:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20aca226ddd2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:13 |
| **Last Seen** | 2026-06-27 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:13:37` | `cowrie.session.connect` |
| `2026-06-27 20:13:37` | `cowrie.client.version` |
| `2026-06-27 20:13:37` | `cowrie.client.kex` |
| `2026-06-27 20:13:38` | `cowrie.login.success` |
| `2026-06-27 20:13:38` | `cowrie.session.params` |
| `2026-06-27 20:13:38` | `cowrie.command.input` |
| `2026-06-27 20:13:38` | `cowrie.log.closed` |
| `2026-06-27 20:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae2e1f375f1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 20:14 |
| **Last Seen** | 2026-06-27 20:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:14:05` | `cowrie.session.connect` |
| `2026-06-27 20:14:05` | `cowrie.client.version` |
| `2026-06-27 20:14:05` | `cowrie.client.kex` |
| `2026-06-27 20:14:07` | `cowrie.login.success` |
| `2026-06-27 20:14:08` | `cowrie.session.params` |
| `2026-06-27 20:14:08` | `cowrie.command.input` |
| `2026-06-27 20:14:09` | `cowrie.log.closed` |
| `2026-06-27 20:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0cdbf6c72b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:14 |
| **Last Seen** | 2026-06-27 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:14:25` | `cowrie.session.connect` |
| `2026-06-27 20:14:25` | `cowrie.client.version` |
| `2026-06-27 20:14:25` | `cowrie.client.kex` |
| `2026-06-27 20:14:26` | `cowrie.login.success` |
| `2026-06-27 20:14:27` | `cowrie.session.params` |
| `2026-06-27 20:14:27` | `cowrie.command.input` |
| `2026-06-27 20:14:27` | `cowrie.log.closed` |
| `2026-06-27 20:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae48b880d40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:15 |
| **Last Seen** | 2026-06-27 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:15:13` | `cowrie.session.connect` |
| `2026-06-27 20:15:13` | `cowrie.client.version` |
| `2026-06-27 20:15:13` | `cowrie.client.kex` |
| `2026-06-27 20:15:13` | `cowrie.login.success` |
| `2026-06-27 20:15:14` | `cowrie.session.params` |
| `2026-06-27 20:15:14` | `cowrie.command.input` |
| `2026-06-27 20:15:14` | `cowrie.log.closed` |
| `2026-06-27 20:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2549c5211b26

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:15 |
| **Last Seen** | 2026-06-27 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:15:59` | `cowrie.session.connect` |
| `2026-06-27 20:15:59` | `cowrie.client.version` |
| `2026-06-27 20:16:00` | `cowrie.client.kex` |
| `2026-06-27 20:16:00` | `cowrie.login.success` |
| `2026-06-27 20:16:01` | `cowrie.session.params` |
| `2026-06-27 20:16:01` | `cowrie.command.input` |
| `2026-06-27 20:16:01` | `cowrie.log.closed` |
| `2026-06-27 20:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5475dd40ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:16 |
| **Last Seen** | 2026-06-27 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:16:46` | `cowrie.session.connect` |
| `2026-06-27 20:16:46` | `cowrie.client.version` |
| `2026-06-27 20:16:46` | `cowrie.client.kex` |
| `2026-06-27 20:16:46` | `cowrie.login.success` |
| `2026-06-27 20:16:47` | `cowrie.session.params` |
| `2026-06-27 20:16:47` | `cowrie.command.input` |
| `2026-06-27 20:16:47` | `cowrie.log.closed` |
| `2026-06-27 20:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95211fb8ffe3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 20:17 |
| **Last Seen** | 2026-06-27 20:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:17:14` | `cowrie.session.connect` |
| `2026-06-27 20:17:16` | `cowrie.client.version` |
| `2026-06-27 20:17:16` | `cowrie.client.kex` |
| `2026-06-27 20:17:22` | `cowrie.login.success` |
| `2026-06-27 20:17:26` | `cowrie.session.params` |
| `2026-06-27 20:17:26` | `cowrie.command.input` |
| `2026-06-27 20:17:27` | `cowrie.log.closed` |
| `2026-06-27 20:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfdeec318477

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:17 |
| **Last Seen** | 2026-06-27 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:17:33` | `cowrie.session.connect` |
| `2026-06-27 20:17:33` | `cowrie.client.version` |
| `2026-06-27 20:17:34` | `cowrie.client.kex` |
| `2026-06-27 20:17:34` | `cowrie.login.success` |
| `2026-06-27 20:17:35` | `cowrie.session.params` |
| `2026-06-27 20:17:35` | `cowrie.command.input` |
| `2026-06-27 20:17:35` | `cowrie.log.closed` |
| `2026-06-27 20:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cbdef64473

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:18 |
| **Last Seen** | 2026-06-27 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:18:22` | `cowrie.session.connect` |
| `2026-06-27 20:18:22` | `cowrie.client.version` |
| `2026-06-27 20:18:22` | `cowrie.client.kex` |
| `2026-06-27 20:18:22` | `cowrie.login.success` |
| `2026-06-27 20:18:23` | `cowrie.session.params` |
| `2026-06-27 20:18:23` | `cowrie.command.input` |
| `2026-06-27 20:18:23` | `cowrie.log.closed` |
| `2026-06-27 20:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1c1a180ed8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:19 |
| **Last Seen** | 2026-06-27 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:19:11` | `cowrie.session.connect` |
| `2026-06-27 20:19:11` | `cowrie.client.version` |
| `2026-06-27 20:19:11` | `cowrie.client.kex` |
| `2026-06-27 20:19:11` | `cowrie.login.success` |
| `2026-06-27 20:19:12` | `cowrie.session.params` |
| `2026-06-27 20:19:12` | `cowrie.command.input` |
| `2026-06-27 20:19:12` | `cowrie.log.closed` |
| `2026-06-27 20:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5acaa7ade9d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:19 |
| **Last Seen** | 2026-06-27 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:19:59` | `cowrie.session.connect` |
| `2026-06-27 20:19:59` | `cowrie.client.version` |
| `2026-06-27 20:19:59` | `cowrie.client.kex` |
| `2026-06-27 20:19:59` | `cowrie.login.success` |
| `2026-06-27 20:20:00` | `cowrie.session.params` |
| `2026-06-27 20:20:00` | `cowrie.command.input` |
| `2026-06-27 20:20:00` | `cowrie.log.closed` |
| `2026-06-27 20:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff9915c46eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:20 |
| **Last Seen** | 2026-06-27 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:20:46` | `cowrie.session.connect` |
| `2026-06-27 20:20:46` | `cowrie.client.version` |
| `2026-06-27 20:20:46` | `cowrie.client.kex` |
| `2026-06-27 20:20:47` | `cowrie.login.success` |
| `2026-06-27 20:20:48` | `cowrie.session.params` |
| `2026-06-27 20:20:48` | `cowrie.command.input` |
| `2026-06-27 20:20:48` | `cowrie.log.closed` |
| `2026-06-27 20:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3132bed0a4ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:21 |
| **Last Seen** | 2026-06-27 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:21:33` | `cowrie.session.connect` |
| `2026-06-27 20:21:33` | `cowrie.client.version` |
| `2026-06-27 20:21:33` | `cowrie.client.kex` |
| `2026-06-27 20:21:34` | `cowrie.login.success` |
| `2026-06-27 20:21:34` | `cowrie.session.params` |
| `2026-06-27 20:21:34` | `cowrie.command.input` |
| `2026-06-27 20:21:34` | `cowrie.log.closed` |
| `2026-06-27 20:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcee4bdd20d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:22 |
| **Last Seen** | 2026-06-27 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:22:19` | `cowrie.session.connect` |
| `2026-06-27 20:22:19` | `cowrie.client.version` |
| `2026-06-27 20:22:20` | `cowrie.client.kex` |
| `2026-06-27 20:22:20` | `cowrie.login.success` |
| `2026-06-27 20:22:21` | `cowrie.session.params` |
| `2026-06-27 20:22:21` | `cowrie.command.input` |
| `2026-06-27 20:22:21` | `cowrie.log.closed` |
| `2026-06-27 20:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7421854b2ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:23 |
| **Last Seen** | 2026-06-27 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:23:06` | `cowrie.session.connect` |
| `2026-06-27 20:23:06` | `cowrie.client.version` |
| `2026-06-27 20:23:06` | `cowrie.client.kex` |
| `2026-06-27 20:23:06` | `cowrie.login.success` |
| `2026-06-27 20:23:07` | `cowrie.session.params` |
| `2026-06-27 20:23:07` | `cowrie.command.input` |
| `2026-06-27 20:23:07` | `cowrie.log.closed` |
| `2026-06-27 20:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785de08b8804

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:23 |
| **Last Seen** | 2026-06-27 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:23:54` | `cowrie.session.connect` |
| `2026-06-27 20:23:54` | `cowrie.client.version` |
| `2026-06-27 20:23:54` | `cowrie.client.kex` |
| `2026-06-27 20:23:55` | `cowrie.login.success` |
| `2026-06-27 20:23:55` | `cowrie.session.params` |
| `2026-06-27 20:23:55` | `cowrie.command.input` |
| `2026-06-27 20:23:56` | `cowrie.log.closed` |
| `2026-06-27 20:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b849e3c120d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:24 |
| **Last Seen** | 2026-06-27 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:24:44` | `cowrie.session.connect` |
| `2026-06-27 20:24:44` | `cowrie.client.version` |
| `2026-06-27 20:24:44` | `cowrie.client.kex` |
| `2026-06-27 20:24:44` | `cowrie.login.success` |
| `2026-06-27 20:24:45` | `cowrie.session.params` |
| `2026-06-27 20:24:45` | `cowrie.command.input` |
| `2026-06-27 20:24:45` | `cowrie.log.closed` |
| `2026-06-27 20:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fc0bed372e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:25 |
| **Last Seen** | 2026-06-27 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:25:33` | `cowrie.session.connect` |
| `2026-06-27 20:25:33` | `cowrie.client.version` |
| `2026-06-27 20:25:33` | `cowrie.client.kex` |
| `2026-06-27 20:25:34` | `cowrie.login.success` |
| `2026-06-27 20:25:34` | `cowrie.session.params` |
| `2026-06-27 20:25:34` | `cowrie.command.input` |
| `2026-06-27 20:25:35` | `cowrie.log.closed` |
| `2026-06-27 20:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9da059e31fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:26 |
| **Last Seen** | 2026-06-27 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:26:23` | `cowrie.session.connect` |
| `2026-06-27 20:26:23` | `cowrie.client.version` |
| `2026-06-27 20:26:23` | `cowrie.client.kex` |
| `2026-06-27 20:26:23` | `cowrie.login.success` |
| `2026-06-27 20:26:24` | `cowrie.session.params` |
| `2026-06-27 20:26:24` | `cowrie.command.input` |
| `2026-06-27 20:26:24` | `cowrie.log.closed` |
| `2026-06-27 20:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4af0b88d313

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:27 |
| **Last Seen** | 2026-06-27 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:27:12` | `cowrie.session.connect` |
| `2026-06-27 20:27:12` | `cowrie.client.version` |
| `2026-06-27 20:27:12` | `cowrie.client.kex` |
| `2026-06-27 20:27:12` | `cowrie.login.success` |
| `2026-06-27 20:27:13` | `cowrie.session.params` |
| `2026-06-27 20:27:13` | `cowrie.command.input` |
| `2026-06-27 20:27:13` | `cowrie.log.closed` |
| `2026-06-27 20:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5deec4e9f72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:28 |
| **Last Seen** | 2026-06-27 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:28:00` | `cowrie.session.connect` |
| `2026-06-27 20:28:00` | `cowrie.client.version` |
| `2026-06-27 20:28:00` | `cowrie.client.kex` |
| `2026-06-27 20:28:00` | `cowrie.login.success` |
| `2026-06-27 20:28:01` | `cowrie.session.params` |
| `2026-06-27 20:28:01` | `cowrie.command.input` |
| `2026-06-27 20:28:01` | `cowrie.log.closed` |
| `2026-06-27 20:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b2f74026a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:28 |
| **Last Seen** | 2026-06-27 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:28:47` | `cowrie.session.connect` |
| `2026-06-27 20:28:47` | `cowrie.client.version` |
| `2026-06-27 20:28:48` | `cowrie.client.kex` |
| `2026-06-27 20:28:48` | `cowrie.login.success` |
| `2026-06-27 20:28:49` | `cowrie.session.params` |
| `2026-06-27 20:28:49` | `cowrie.command.input` |
| `2026-06-27 20:28:49` | `cowrie.log.closed` |
| `2026-06-27 20:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bce9da6175

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 20:28 |
| **Last Seen** | 2026-06-27 20:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:28:48` | `cowrie.session.connect` |
| `2026-06-27 20:28:48` | `cowrie.client.version` |
| `2026-06-27 20:28:48` | `cowrie.client.kex` |
| `2026-06-27 20:28:50` | `cowrie.login.success` |
| `2026-06-27 20:28:52` | `cowrie.session.params` |
| `2026-06-27 20:28:52` | `cowrie.command.input` |
| `2026-06-27 20:28:52` | `cowrie.log.closed` |
| `2026-06-27 20:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d2c2f2f4ddd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 20:29 |
| **Last Seen** | 2026-06-27 20:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:29:16` | `cowrie.session.connect` |
| `2026-06-27 20:29:17` | `cowrie.client.version` |
| `2026-06-27 20:29:17` | `cowrie.client.kex` |
| `2026-06-27 20:29:24` | `cowrie.login.success` |
| `2026-06-27 20:29:28` | `cowrie.session.params` |
| `2026-06-27 20:29:28` | `cowrie.command.input` |
| `2026-06-27 20:29:29` | `cowrie.log.closed` |
| `2026-06-27 20:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957d7c4058b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:29 |
| **Last Seen** | 2026-06-27 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:29:37` | `cowrie.session.connect` |
| `2026-06-27 20:29:37` | `cowrie.client.version` |
| `2026-06-27 20:29:37` | `cowrie.client.kex` |
| `2026-06-27 20:29:38` | `cowrie.login.success` |
| `2026-06-27 20:29:39` | `cowrie.session.params` |
| `2026-06-27 20:29:39` | `cowrie.command.input` |
| `2026-06-27 20:29:39` | `cowrie.log.closed` |
| `2026-06-27 20:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c2208781e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:30 |
| **Last Seen** | 2026-06-27 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:30:28` | `cowrie.session.connect` |
| `2026-06-27 20:30:28` | `cowrie.client.version` |
| `2026-06-27 20:30:28` | `cowrie.client.kex` |
| `2026-06-27 20:30:28` | `cowrie.login.success` |
| `2026-06-27 20:30:29` | `cowrie.session.params` |
| `2026-06-27 20:30:29` | `cowrie.command.input` |
| `2026-06-27 20:30:29` | `cowrie.log.closed` |
| `2026-06-27 20:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c77f63524a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:31 |
| **Last Seen** | 2026-06-27 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:31:19` | `cowrie.session.connect` |
| `2026-06-27 20:31:19` | `cowrie.client.version` |
| `2026-06-27 20:31:19` | `cowrie.client.kex` |
| `2026-06-27 20:31:19` | `cowrie.login.success` |
| `2026-06-27 20:31:20` | `cowrie.session.params` |
| `2026-06-27 20:31:20` | `cowrie.command.input` |
| `2026-06-27 20:31:20` | `cowrie.log.closed` |
| `2026-06-27 20:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6047d4e48274

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:32 |
| **Last Seen** | 2026-06-27 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:32:10` | `cowrie.session.connect` |
| `2026-06-27 20:32:10` | `cowrie.client.version` |
| `2026-06-27 20:32:10` | `cowrie.client.kex` |
| `2026-06-27 20:32:10` | `cowrie.login.success` |
| `2026-06-27 20:32:11` | `cowrie.session.params` |
| `2026-06-27 20:32:11` | `cowrie.command.input` |
| `2026-06-27 20:32:11` | `cowrie.log.closed` |
| `2026-06-27 20:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02fa1e5879a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:33 |
| **Last Seen** | 2026-06-27 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:33:01` | `cowrie.session.connect` |
| `2026-06-27 20:33:01` | `cowrie.client.version` |
| `2026-06-27 20:33:01` | `cowrie.client.kex` |
| `2026-06-27 20:33:02` | `cowrie.login.success` |
| `2026-06-27 20:33:02` | `cowrie.session.params` |
| `2026-06-27 20:33:02` | `cowrie.command.input` |
| `2026-06-27 20:33:02` | `cowrie.log.closed` |
| `2026-06-27 20:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e966cea44e11

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:33 |
| **Last Seen** | 2026-06-27 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:33:51` | `cowrie.session.connect` |
| `2026-06-27 20:33:51` | `cowrie.client.version` |
| `2026-06-27 20:33:51` | `cowrie.client.kex` |
| `2026-06-27 20:33:51` | `cowrie.login.success` |
| `2026-06-27 20:33:52` | `cowrie.session.params` |
| `2026-06-27 20:33:52` | `cowrie.command.input` |
| `2026-06-27 20:33:52` | `cowrie.log.closed` |
| `2026-06-27 20:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad2247800fc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:34 |
| **Last Seen** | 2026-06-27 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:34:39` | `cowrie.session.connect` |
| `2026-06-27 20:34:39` | `cowrie.client.version` |
| `2026-06-27 20:34:39` | `cowrie.client.kex` |
| `2026-06-27 20:34:40` | `cowrie.login.success` |
| `2026-06-27 20:34:40` | `cowrie.session.params` |
| `2026-06-27 20:34:40` | `cowrie.command.input` |
| `2026-06-27 20:34:40` | `cowrie.log.closed` |
| `2026-06-27 20:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba09a4b475d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:35 |
| **Last Seen** | 2026-06-27 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:35:28` | `cowrie.session.connect` |
| `2026-06-27 20:35:28` | `cowrie.client.version` |
| `2026-06-27 20:35:28` | `cowrie.client.kex` |
| `2026-06-27 20:35:28` | `cowrie.login.success` |
| `2026-06-27 20:35:29` | `cowrie.session.params` |
| `2026-06-27 20:35:29` | `cowrie.command.input` |
| `2026-06-27 20:35:29` | `cowrie.log.closed` |
| `2026-06-27 20:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687925a0ac5e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:36 |
| **Last Seen** | 2026-06-27 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:36:18` | `cowrie.session.connect` |
| `2026-06-27 20:36:18` | `cowrie.client.version` |
| `2026-06-27 20:36:18` | `cowrie.client.kex` |
| `2026-06-27 20:36:19` | `cowrie.login.success` |
| `2026-06-27 20:36:20` | `cowrie.session.params` |
| `2026-06-27 20:36:20` | `cowrie.command.input` |
| `2026-06-27 20:36:20` | `cowrie.log.closed` |
| `2026-06-27 20:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860f467ba798

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:37 |
| **Last Seen** | 2026-06-27 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:37:10` | `cowrie.session.connect` |
| `2026-06-27 20:37:10` | `cowrie.client.version` |
| `2026-06-27 20:37:10` | `cowrie.client.kex` |
| `2026-06-27 20:37:11` | `cowrie.login.success` |
| `2026-06-27 20:37:12` | `cowrie.session.params` |
| `2026-06-27 20:37:12` | `cowrie.command.input` |
| `2026-06-27 20:37:12` | `cowrie.log.closed` |
| `2026-06-27 20:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090e31742d6a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:38 |
| **Last Seen** | 2026-06-27 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:38:03` | `cowrie.session.connect` |
| `2026-06-27 20:38:03` | `cowrie.client.version` |
| `2026-06-27 20:38:03` | `cowrie.client.kex` |
| `2026-06-27 20:38:04` | `cowrie.login.success` |
| `2026-06-27 20:38:04` | `cowrie.session.params` |
| `2026-06-27 20:38:04` | `cowrie.command.input` |
| `2026-06-27 20:38:04` | `cowrie.log.closed` |
| `2026-06-27 20:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bca489aa2fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:38 |
| **Last Seen** | 2026-06-27 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:38:56` | `cowrie.session.connect` |
| `2026-06-27 20:38:56` | `cowrie.client.version` |
| `2026-06-27 20:38:56` | `cowrie.client.kex` |
| `2026-06-27 20:38:56` | `cowrie.login.success` |
| `2026-06-27 20:38:57` | `cowrie.session.params` |
| `2026-06-27 20:38:57` | `cowrie.command.input` |
| `2026-06-27 20:38:57` | `cowrie.log.closed` |
| `2026-06-27 20:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ebae1b4ede

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:39 |
| **Last Seen** | 2026-06-27 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:39:47` | `cowrie.session.connect` |
| `2026-06-27 20:39:47` | `cowrie.client.version` |
| `2026-06-27 20:39:48` | `cowrie.client.kex` |
| `2026-06-27 20:39:48` | `cowrie.login.success` |
| `2026-06-27 20:39:49` | `cowrie.session.params` |
| `2026-06-27 20:39:49` | `cowrie.command.input` |
| `2026-06-27 20:39:49` | `cowrie.log.closed` |
| `2026-06-27 20:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e7f2f94b92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:40 |
| **Last Seen** | 2026-06-27 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:40:38` | `cowrie.session.connect` |
| `2026-06-27 20:40:38` | `cowrie.client.version` |
| `2026-06-27 20:40:39` | `cowrie.client.kex` |
| `2026-06-27 20:40:39` | `cowrie.login.success` |
| `2026-06-27 20:40:40` | `cowrie.session.params` |
| `2026-06-27 20:40:40` | `cowrie.command.input` |
| `2026-06-27 20:40:40` | `cowrie.log.closed` |
| `2026-06-27 20:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899daf0f5586

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 20:41 |
| **Last Seen** | 2026-06-27 20:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:41:18` | `cowrie.session.connect` |
| `2026-06-27 20:41:20` | `cowrie.client.version` |
| `2026-06-27 20:41:20` | `cowrie.client.kex` |
| `2026-06-27 20:41:25` | `cowrie.login.success` |
| `2026-06-27 20:41:29` | `cowrie.session.params` |
| `2026-06-27 20:41:29` | `cowrie.command.input` |
| `2026-06-27 20:41:31` | `cowrie.log.closed` |
| `2026-06-27 20:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc87139c6c81

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]63` |
| **First Seen** | 2026-06-27 20:41 |
| **Last Seen** | 2026-06-27 20:41 |
| **Session Duration** | 23s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:41:20` | `cowrie.session.connect` |
| `2026-06-27 20:41:20` | `cowrie.client.version` |
| `2026-06-27 20:41:20` | `cowrie.client.kex` |
| `2026-06-27 20:41:21` | `cowrie.client.fingerprint` |
| `2026-06-27 20:41:21` | `cowrie.login.failed` |
| `2026-06-27 20:41:22` | `cowrie.login.success` |
| `2026-06-27 20:41:43` | `cowrie.direct-tcpip.request` |
| `2026-06-27 20:41:43` | `cowrie.direct-tcpip.ja4` |
| `2026-06-27 20:41:43` | `cowrie.direct-tcpip.data` |
| `2026-06-27 20:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]63` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990bbf036839

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:41 |
| **Last Seen** | 2026-06-27 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:41:30` | `cowrie.session.connect` |
| `2026-06-27 20:41:30` | `cowrie.client.version` |
| `2026-06-27 20:41:30` | `cowrie.client.kex` |
| `2026-06-27 20:41:30` | `cowrie.login.success` |
| `2026-06-27 20:41:31` | `cowrie.session.params` |
| `2026-06-27 20:41:31` | `cowrie.command.input` |
| `2026-06-27 20:41:31` | `cowrie.log.closed` |
| `2026-06-27 20:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ed00c739d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:42 |
| **Last Seen** | 2026-06-27 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:42:20` | `cowrie.session.connect` |
| `2026-06-27 20:42:20` | `cowrie.client.version` |
| `2026-06-27 20:42:20` | `cowrie.client.kex` |
| `2026-06-27 20:42:20` | `cowrie.login.success` |
| `2026-06-27 20:42:21` | `cowrie.session.params` |
| `2026-06-27 20:42:21` | `cowrie.command.input` |
| `2026-06-27 20:42:21` | `cowrie.log.closed` |
| `2026-06-27 20:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5584eef6c58f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:43 |
| **Last Seen** | 2026-06-27 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:43:12` | `cowrie.session.connect` |
| `2026-06-27 20:43:12` | `cowrie.client.version` |
| `2026-06-27 20:43:12` | `cowrie.client.kex` |
| `2026-06-27 20:43:13` | `cowrie.login.success` |
| `2026-06-27 20:43:13` | `cowrie.session.params` |
| `2026-06-27 20:43:13` | `cowrie.command.input` |
| `2026-06-27 20:43:14` | `cowrie.log.closed` |
| `2026-06-27 20:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be212fccdecc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 20:43 |
| **Last Seen** | 2026-06-27 20:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:43:30` | `cowrie.session.connect` |
| `2026-06-27 20:43:30` | `cowrie.client.version` |
| `2026-06-27 20:43:30` | `cowrie.client.kex` |
| `2026-06-27 20:43:31` | `cowrie.login.success` |
| `2026-06-27 20:43:33` | `cowrie.session.params` |
| `2026-06-27 20:43:33` | `cowrie.command.input` |
| `2026-06-27 20:43:33` | `cowrie.log.closed` |
| `2026-06-27 20:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1108aa43dcac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:44 |
| **Last Seen** | 2026-06-27 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:44:06` | `cowrie.session.connect` |
| `2026-06-27 20:44:06` | `cowrie.client.version` |
| `2026-06-27 20:44:06` | `cowrie.client.kex` |
| `2026-06-27 20:44:06` | `cowrie.login.success` |
| `2026-06-27 20:44:07` | `cowrie.session.params` |
| `2026-06-27 20:44:07` | `cowrie.command.input` |
| `2026-06-27 20:44:07` | `cowrie.log.closed` |
| `2026-06-27 20:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-865dff08b19c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:45 |
| **Last Seen** | 2026-06-27 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:45:01` | `cowrie.session.connect` |
| `2026-06-27 20:45:01` | `cowrie.client.version` |
| `2026-06-27 20:45:01` | `cowrie.client.kex` |
| `2026-06-27 20:45:01` | `cowrie.login.success` |
| `2026-06-27 20:45:02` | `cowrie.session.params` |
| `2026-06-27 20:45:02` | `cowrie.command.input` |
| `2026-06-27 20:45:02` | `cowrie.log.closed` |
| `2026-06-27 20:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087121af4ebc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:45 |
| **Last Seen** | 2026-06-27 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:45:55` | `cowrie.session.connect` |
| `2026-06-27 20:45:55` | `cowrie.client.version` |
| `2026-06-27 20:45:55` | `cowrie.client.kex` |
| `2026-06-27 20:45:56` | `cowrie.login.success` |
| `2026-06-27 20:45:57` | `cowrie.session.params` |
| `2026-06-27 20:45:57` | `cowrie.command.input` |
| `2026-06-27 20:45:57` | `cowrie.log.closed` |
| `2026-06-27 20:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72992749b03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:46 |
| **Last Seen** | 2026-06-27 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:46:49` | `cowrie.session.connect` |
| `2026-06-27 20:46:49` | `cowrie.client.version` |
| `2026-06-27 20:46:49` | `cowrie.client.kex` |
| `2026-06-27 20:46:50` | `cowrie.login.success` |
| `2026-06-27 20:46:50` | `cowrie.session.params` |
| `2026-06-27 20:46:51` | `cowrie.command.input` |
| `2026-06-27 20:46:51` | `cowrie.log.closed` |
| `2026-06-27 20:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec9f5490b98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:47 |
| **Last Seen** | 2026-06-27 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:47:42` | `cowrie.session.connect` |
| `2026-06-27 20:47:42` | `cowrie.client.version` |
| `2026-06-27 20:47:42` | `cowrie.client.kex` |
| `2026-06-27 20:47:42` | `cowrie.login.success` |
| `2026-06-27 20:47:43` | `cowrie.session.params` |
| `2026-06-27 20:47:43` | `cowrie.command.input` |
| `2026-06-27 20:47:43` | `cowrie.log.closed` |
| `2026-06-27 20:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47ae130d146b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:48 |
| **Last Seen** | 2026-06-27 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:48:36` | `cowrie.session.connect` |
| `2026-06-27 20:48:36` | `cowrie.client.version` |
| `2026-06-27 20:48:36` | `cowrie.client.kex` |
| `2026-06-27 20:48:36` | `cowrie.login.success` |
| `2026-06-27 20:48:37` | `cowrie.session.params` |
| `2026-06-27 20:48:37` | `cowrie.command.input` |
| `2026-06-27 20:48:37` | `cowrie.log.closed` |
| `2026-06-27 20:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229bd78cd777

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:49 |
| **Last Seen** | 2026-06-27 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:49:30` | `cowrie.session.connect` |
| `2026-06-27 20:49:30` | `cowrie.client.version` |
| `2026-06-27 20:49:30` | `cowrie.client.kex` |
| `2026-06-27 20:49:30` | `cowrie.login.success` |
| `2026-06-27 20:49:31` | `cowrie.session.params` |
| `2026-06-27 20:49:31` | `cowrie.command.input` |
| `2026-06-27 20:49:31` | `cowrie.log.closed` |
| `2026-06-27 20:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eca41feb4e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:50 |
| **Last Seen** | 2026-06-27 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:50:26` | `cowrie.session.connect` |
| `2026-06-27 20:50:26` | `cowrie.client.version` |
| `2026-06-27 20:50:26` | `cowrie.client.kex` |
| `2026-06-27 20:50:26` | `cowrie.login.success` |
| `2026-06-27 20:50:27` | `cowrie.session.params` |
| `2026-06-27 20:50:27` | `cowrie.command.input` |
| `2026-06-27 20:50:27` | `cowrie.log.closed` |
| `2026-06-27 20:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a45404f441e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:51 |
| **Last Seen** | 2026-06-27 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:51:23` | `cowrie.session.connect` |
| `2026-06-27 20:51:23` | `cowrie.client.version` |
| `2026-06-27 20:51:23` | `cowrie.client.kex` |
| `2026-06-27 20:51:23` | `cowrie.login.success` |
| `2026-06-27 20:51:24` | `cowrie.session.params` |
| `2026-06-27 20:51:24` | `cowrie.command.input` |
| `2026-06-27 20:51:24` | `cowrie.log.closed` |
| `2026-06-27 20:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279eb521765d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:52 |
| **Last Seen** | 2026-06-27 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:52:18` | `cowrie.session.connect` |
| `2026-06-27 20:52:18` | `cowrie.client.version` |
| `2026-06-27 20:52:18` | `cowrie.client.kex` |
| `2026-06-27 20:52:19` | `cowrie.login.success` |
| `2026-06-27 20:52:19` | `cowrie.session.params` |
| `2026-06-27 20:52:19` | `cowrie.command.input` |
| `2026-06-27 20:52:19` | `cowrie.log.closed` |
| `2026-06-27 20:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b0e6192366

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 20:52 |
| **Last Seen** | 2026-06-27 20:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:52:57` | `cowrie.session.connect` |
| `2026-06-27 20:52:59` | `cowrie.client.version` |
| `2026-06-27 20:52:59` | `cowrie.client.kex` |
| `2026-06-27 20:53:04` | `cowrie.login.success` |
| `2026-06-27 20:53:08` | `cowrie.session.params` |
| `2026-06-27 20:53:08` | `cowrie.command.input` |
| `2026-06-27 20:53:09` | `cowrie.log.closed` |
| `2026-06-27 20:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c95a4aecf7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:53 |
| **Last Seen** | 2026-06-27 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:53:12` | `cowrie.session.connect` |
| `2026-06-27 20:53:12` | `cowrie.client.version` |
| `2026-06-27 20:53:12` | `cowrie.client.kex` |
| `2026-06-27 20:53:12` | `cowrie.login.success` |
| `2026-06-27 20:53:13` | `cowrie.session.params` |
| `2026-06-27 20:53:13` | `cowrie.command.input` |
| `2026-06-27 20:53:13` | `cowrie.log.closed` |
| `2026-06-27 20:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86489a146cc1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 20:54 |
| **Last Seen** | 2026-06-27 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 20:54:08` | `cowrie.session.connect` |
| `2026-06-27 20:54:08` | `cowrie.client.version` |
| `2026-06-27 20:54:08` | `cowrie.client.kex` |
| `2026-06-27 20:54:09` | `cowrie.login.success` |
| `2026-06-27 20:54:09` | `cowrie.session.params` |
| `2026-06-27 20:54:09` | `cowrie.command.input` |
| `2026-06-27 20:54:10` | `cowrie.log.closed` |
| `2026-06-27 20:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `209.99.185[.]59` | **132** | 2026-06-27 18:55 | 2026-06-27 20:55 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `157.230.42[.]17` | **116** | 2026-06-27 18:55 | 2026-06-27 20:54 | 79m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.29[.]10` | **14** | 2026-06-27 19:04 | 2026-06-27 20:45 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `118.26.104[.]78` | **4** | 2026-06-27 19:51 | 2026-06-27 19:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.146[.]145` | **2** | 2026-06-27 20:16 | 2026-06-27 20:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `180.76.250[.]159` | **2** | 2026-06-27 19:57 | 2026-06-27 19:59 | 2m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-06-27 20:10 | 2026-06-27 20:40 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-06-27 20:34 | 2026-06-27 20:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-06-27 19:58 | 2026-06-27 19:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | 1 | 2026-06-27 19:12 | 2026-06-27 19:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-06-27 19:32 | 2026-06-27 19:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.91.244[.]87` | 1 | 2026-06-27 20:47 | 2026-06-27 20:47 | 31s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]80` | 1 | 2026-06-27 19:50 | 2026-06-27 19:50 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.142.209[.]147` | 1 | 2026-06-27 19:46 | 2026-06-27 19:47 | 49s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **5/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 50/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `91.142.209[.]147` | ES | AXARNET COMUNICACIONES, S.L. | **100** ⚠️ | 4 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 50 |
| `192.42.116[.]63` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 15 |
| `157.230.42[.]17` | SG | DigitalOcean, LLC | **100** ⚠️ | 11 |
| `132.148.29[.]10` | US | GoDaddy.com, LLC | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 177 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 165 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 7 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 452 cases |
| Tool 34  | Credential Extractor        | ✅ 170 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 163 priority case(s) shown individually · 14 recon entry/entries in table (7 group(s) consolidating 272 session(s)).

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
_Report time: 2026-06-27T21:09:17Z_

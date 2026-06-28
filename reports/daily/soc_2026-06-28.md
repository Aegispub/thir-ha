# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-28 |
| **Generated At** | 2026-06-28T21:06:42Z |
| **Shift Time** | 21:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **308** |
| Confirmed Threats | **299** |
| False Positives Filtered | **9** (2.9%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **7** |
| High Severity Cases | **160** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **148** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **161** |
| Unique Credential Pairs | **160** |
| Unique Usernames | **85** |
| Unique Passwords | **142** |
| Successful Auth Pairs | **161** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 59 |
| `ubuntu` | 15 |
| `mysql` | 2 |
| `testuser` | 2 |
| `pi` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 9 |
| `1234` | 4 |
| `andrea` | 2 |
| `changeme123` | 2 |
| `111111` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 2 |
| `ruili` | `ruili` | 1 |
| `root` | `jordan23` | 1 |
| `fabio` | `fabio` | 1 |
| `root` | `4321` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ruili` | `ruili` | `45.205.1.42` | 2026-06-28T18:55:17 |
| `root` | `jordan23` | `209.99.185.59` | 2026-06-28T18:55:50 |
| `fabio` | `fabio` | `209.99.185.59` | 2026-06-28T18:56:45 |
| `root` | `4321` | `195.178.110.217` | 2026-06-28T18:57:21 |
| `ubuntu` | `username` | `209.99.185.59` | 2026-06-28T18:57:39 |
| `ubuntu` | `1qazxsw2` | `209.99.185.59` | 2026-06-28T18:58:34 |
| `andrea` | `andrea` | `209.99.185.59` | 2026-06-28T18:59:30 |
| `root` | `rkdepula` | `209.99.185.59` | 2026-06-28T19:00:31 |
| `root` | `QWE123456` | `209.99.185.59` | 2026-06-28T19:01:28 |
| `pul` | `123456` | `209.99.185.59` | 2026-06-28T19:02:24 |
| `root` | `54321` | `195.178.110.217` | 2026-06-28T19:02:42 |
| `xiaoyuyoupin` | `xiaoyuyoupin` | `209.99.185.59` | 2026-06-28T19:03:22 |
| `teste` | `teste` | `209.99.185.59` | 2026-06-28T19:04:17 |
| `gcv5` | `gcv5` | `209.99.185.59` | 2026-06-28T19:05:12 |
| `test3` | `1234` | `209.99.185.59` | 2026-06-28T19:06:09 |
| `root` | `123qwert` | `45.198.224.120` | 2026-06-28T19:06:15 |
| `isaac` | `isaac` | `209.99.185.59` | 2026-06-28T19:07:04 |
| `root` | `5tgb%TGB` | `209.99.185.59` | 2026-06-28T19:08:01 |
| `root` | `654321` | `195.178.110.217` | 2026-06-28T19:08:43 |
| `ubuntu` | `upload1234567` | `209.99.185.59` | 2026-06-28T19:08:56 |
| `datacenter` | `changeme123` | `209.99.185.59` | 2026-06-28T19:09:51 |
| `root` | `Pass123!@#` | `45.205.1.42` | 2026-06-28T19:10:00 |
| `root` | `P@ssword!@#123` | `209.99.185.59` | 2026-06-28T19:10:46 |
| `jian1412` | `1234` | `209.99.185.59` | 2026-06-28T19:11:43 |
| `yangliusha11` | `yangliusha11` | `209.99.185.59` | 2026-06-28T19:12:40 |
| `root` | `drcom123` | `209.99.185.59` | 2026-06-28T19:13:39 |
| `real` | `real` | `209.99.185.59` | 2026-06-28T19:14:38 |
| `root` | `P4ssw0rd` | `195.178.110.217` | 2026-06-28T19:15:16 |
| `rohit` | `rohit` | `209.99.185.59` | 2026-06-28T19:15:37 |
| `gonglitong` | `LItong@0405` | `209.99.185.59` | 2026-06-28T19:16:34 |
| `zhangk` | `zhangk123` | `209.99.185.59` | 2026-06-28T19:17:33 |
| `root` | `qwerty123` | `45.198.224.120` | 2026-06-28T19:17:36 |
| `whn` | `wanghuanan` | `209.99.185.59` | 2026-06-28T19:18:37 |
| `dima` | `111111` | `209.99.185.59` | 2026-06-28T19:19:38 |
| `root` | `123qwe,.` | `209.99.185.59` | 2026-06-28T19:20:37 |
| `astract` | `astract9` | `209.99.185.59` | 2026-06-28T19:21:37 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-28T19:22:16 |
| `zxf` | `123456` | `209.99.185.59` | 2026-06-28T19:22:35 |
| `ubuntu` | `a123456` | `209.99.185.59` | 2026-06-28T19:23:33 |
| `ceshi1` | `333333` | `209.99.185.59` | 2026-06-28T19:24:32 |
| `root` | `555555` | `45.205.1.42` | 2026-06-28T19:24:49 |
| `nicole` | `nicole` | `209.99.185.59` | 2026-06-28T19:25:31 |
| `root` | `manager123` | `209.99.185.59` | 2026-06-28T19:26:31 |
| `cxy` | `123456` | `209.99.185.59` | 2026-06-28T19:27:32 |
| `yohan` | `yohan` | `209.99.185.59` | 2026-06-28T19:28:33 |
| `root` | `andrea` | `45.198.224.120` | 2026-06-28T19:28:33 |
| `wy` | `wy123` | `209.99.185.59` | 2026-06-28T19:29:33 |
| `lijiajun` | `lijiajun` | `209.99.185.59` | 2026-06-28T19:30:33 |
| `root` | `korea2021` | `209.99.185.59` | 2026-06-28T19:31:34 |
| `chiye2` | `chiye2` | `209.99.185.59` | 2026-06-28T19:32:37 |
| `root` | `qwe12#$` | `209.99.185.59` | 2026-06-28T19:33:41 |
| `aisino` | `aisino` | `209.99.185.59` | 2026-06-28T19:34:41 |
| `root` | `123456789#` | `209.99.185.59` | 2026-06-28T19:35:41 |
| `suliyilei4` | `suliyilei4` | `209.99.185.59` | 2026-06-28T19:36:41 |
| `root` | `chenpeng` | `209.99.185.59` | 2026-06-28T19:37:42 |
| `root` | `123qaz` | `209.99.185.59` | 2026-06-28T19:38:44 |
| `root` | `Abc@123` | `45.205.1.42` | 2026-06-28T19:39:28 |
| `root` | `1qazZAQ!` | `209.99.185.59` | 2026-06-28T19:39:47 |
| `ubuntu` | `dev12` | `45.198.224.120` | 2026-06-28T19:40:11 |
| `root` | `1a2b3c4d5e6f7g` | `209.99.185.59` | 2026-06-28T19:40:50 |
| `htx` | `htx` | `209.99.185.59` | 2026-06-28T19:41:53 |
| `root` | `q123456789q` | `209.99.185.59` | 2026-06-28T19:42:55 |
| `cistest` | `cistest` | `209.99.185.59` | 2026-06-28T19:43:58 |
| `ma` | `123456` | `209.99.185.59` | 2026-06-28T19:45:02 |
| `cecilia` | `cecilia` | `209.99.185.59` | 2026-06-28T19:46:06 |
| `mysql` | `mysql!@#` | `209.99.185.59` | 2026-06-28T19:47:12 |
| `solr` | `solr` | `209.99.185.59` | 2026-06-28T19:48:15 |
| `angel` | `333333` | `209.99.185.59` | 2026-06-28T19:49:20 |
| `hxf` | `hxf` | `209.99.185.59` | 2026-06-28T19:50:30 |
| `ubuntu` | `dev12345` | `45.198.224.120` | 2026-06-28T19:51:23 |
| `bob` | `123456` | `209.99.185.59` | 2026-06-28T19:51:36 |
| `root` | `!qaz2wsx` | `209.99.185.59` | 2026-06-28T19:52:42 |
| `ubuntu` | `Admin@2021` | `209.99.185.59` | 2026-06-28T19:53:48 |
| `tomcat` | `abcd1234` | `45.205.1.42` | 2026-06-28T19:54:07 |
| `root` | `upload12` | `209.99.185.59` | 2026-06-28T19:54:53 |
| `jeus` | `jeus` | `209.99.185.59` | 2026-06-28T19:55:57 |
| `xcc` | `123456` | `209.99.185.59` | 2026-06-28T19:57:01 |
| `root` | `1a2s3d4` | `209.99.185.59` | 2026-06-28T19:58:08 |
| `root` | `Admin@6666` | `209.99.185.59` | 2026-06-28T19:59:15 |
| `webadmin` | `webadmin` | `209.99.185.59` | 2026-06-28T20:00:19 |
| `caoll22` | `N8ldt8uxAS` | `209.99.185.59` | 2026-06-28T20:01:04 |
| `root` | `admin@7777` | `209.99.185.59` | 2026-06-28T20:01:47 |
| `kexiao` | `kexiao` | `45.198.224.120` | 2026-06-28T20:02:24 |
| `iot` | `iot123456` | `209.99.185.59` | 2026-06-28T20:02:30 |
| `nongmin2` | `nongmin2` | `209.99.185.59` | 2026-06-28T20:03:14 |
| `root` | `q1` | `209.99.185.59` | 2026-06-28T20:04:06 |
| `root` | `**********` | `209.99.185.59` | 2026-06-28T20:05:09 |
| `smcho` | `smcho` | `209.99.185.59` | 2026-06-28T20:05:53 |
| `zhangwei2` | `zhangwei2` | `209.99.185.59` | 2026-06-28T20:06:38 |
| `root` | `jellyfin` | `91.92.40.90` | 2026-06-28T20:06:59 |
| `jellyfin` | `jellyfin` | `91.92.40.90` | 2026-06-28T20:07:00 |
| `root` | `g` | `209.99.185.59` | 2026-06-28T20:07:27 |
| `root` | `Qwe12345` | `209.99.185.59` | 2026-06-28T20:08:28 |
| `root` | `Oracle123!@#` | `45.205.1.42` | 2026-06-28T20:09:05 |
| `iexcel001` | `iexcel001321` | `209.99.185.59` | 2026-06-28T20:09:22 |
| `gitlab` | `111111` | `209.99.185.59` | 2026-06-28T20:10:22 |
| `caja17` | `caja17` | `209.99.185.59` | 2026-06-28T20:11:09 |
| `testuser` | `qwerty123456` | `209.99.185.59` | 2026-06-28T20:11:55 |
| `caja32` | `caja32` | `209.99.185.59` | 2026-06-28T20:12:42 |
| `ubuntu` | `user12345` | `45.198.224.120` | 2026-06-28T20:13:17 |
| `oracle` | `1` | `209.99.185.59` | 2026-06-28T20:13:31 |
| `root` | `root123456789` | `209.99.185.59` | 2026-06-28T20:14:17 |
| `root` | `777777777` | `209.99.185.59` | 2026-06-28T20:15:03 |
| `peer` | `peer` | `209.99.185.59` | 2026-06-28T20:15:51 |
| `cf` | `cf11235813` | `209.99.185.59` | 2026-06-28T20:16:39 |
| `honghee` | `1234` | `209.99.185.59` | 2026-06-28T20:17:28 |
| `tom` | `123456` | `45.148.10.239` | 2026-06-28T20:17:39 |
| `mysql` | `p@ssw0rd` | `209.99.185.59` | 2026-06-28T20:18:17 |
| `pi` | `1` | `209.99.185.59` | 2026-06-28T20:19:06 |
| `dell` | `dell@666` | `209.99.185.59` | 2026-06-28T20:19:56 |
| `root` | `caonima123` | `209.99.185.59` | 2026-06-28T20:20:45 |
| `wang` | `123qwe!@#` | `209.99.185.59` | 2026-06-28T20:21:34 |
| `guest` | `test123` | `209.99.185.59` | 2026-06-28T20:22:24 |
| `ubuntu` | `qwert1` | `209.99.185.59` | 2026-06-28T20:23:15 |
| `root` | `asdfghjkl;'\` | `45.205.1.42` | 2026-06-28T20:23:50 |
| `ubuntu` | `a1b2c3d4e5` | `209.99.185.59` | 2026-06-28T20:24:05 |
| `pi` | `hello` | `45.198.224.120` | 2026-06-28T20:24:11 |
| `root` | `123qwe` | `209.99.185.59` | 2026-06-28T20:24:57 |
| `ubuntu` | `pass123456789` | `209.99.185.59` | 2026-06-28T20:25:47 |
| `legal` | `legal` | `209.99.185.59` | 2026-06-28T20:26:34 |
| `root` | `Dell@123` | `209.99.185.59` | 2026-06-28T20:27:22 |
| `philip` | `psh01087` | `209.99.185.59` | 2026-06-28T20:28:09 |
| `xzhuai` | `xzh` | `209.99.185.59` | 2026-06-28T20:28:57 |
| `root` | `Password99` | `209.99.185.59` | 2026-06-28T20:29:45 |
| `ansible` | `123qwe` | `209.99.185.59` | 2026-06-28T20:30:33 |
| `root` | `noaccess` | `209.99.185.59` | 2026-06-28T20:31:21 |
| `czk` | `czk` | `209.99.185.59` | 2026-06-28T20:32:09 |
| `newuser` | `newuser` | `209.99.185.59` | 2026-06-28T20:32:55 |
| `root` | `qwerty09` | `209.99.185.59` | 2026-06-28T20:33:43 |
| `root` | `temp` | `209.99.185.59` | 2026-06-28T20:34:33 |
| `root` | `sorin123!@#` | `209.99.185.59` | 2026-06-28T20:35:21 |
| `ubuntu` | `a1s2d3` | `45.198.224.120` | 2026-06-28T20:35:23 |
| `label` | `label` | `209.99.185.59` | 2026-06-28T20:36:08 |
| `ubuntu` | `qazWSX123!@#` | `209.99.185.59` | 2026-06-28T20:36:57 |
| `ubuntu` | `P@ssw0rd` | `209.99.185.59` | 2026-06-28T20:37:45 |
| `etri` | `etri` | `209.99.185.59` | 2026-06-28T20:38:32 |
| `root` | `Preforsa2023*` | `45.205.1.42` | 2026-06-28T20:38:38 |
| `fanglingfei` | `ictmcg2021` | `209.99.185.59` | 2026-06-28T20:39:18 |
| `xkcao` | `12345678` | `209.99.185.59` | 2026-06-28T20:40:05 |
| `root` | `ADMIN` | `209.99.185.59` | 2026-06-28T20:40:51 |
| `yanfeifan` | `yanfeifan@IAOS` | `209.99.185.59` | 2026-06-28T20:41:39 |
| `steam` | `steam123` | `209.99.185.59` | 2026-06-28T20:42:27 |
| `roy` | `123456` | `209.99.185.59` | 2026-06-28T20:43:15 |
| `root` | `procesor` | `209.99.185.59` | 2026-06-28T20:44:04 |
| `testuser` | `12345` | `209.99.185.59` | 2026-06-28T20:44:53 |
| `root` | `plm54321plm` | `209.99.185.59` | 2026-06-28T20:45:41 |
| `root` | `qwert@123` | `45.198.224.120` | 2026-06-28T20:46:28 |
| `root` | `root@2015` | `209.99.185.59` | 2026-06-28T20:46:29 |
| `zero` | `zero` | `209.99.185.59` | 2026-06-28T20:47:18 |
| `hostmaster` | `hostmaster123` | `209.99.185.59` | 2026-06-28T20:48:09 |
| `root` | `rootpasswd` | `209.99.185.59` | 2026-06-28T20:49:00 |
| `zjy` | `123456` | `209.99.185.59` | 2026-06-28T20:49:52 |
| `deployer` | `changeme123` | `209.99.185.59` | 2026-06-28T20:50:44 |
| `root` | `Qwe1!2` | `209.99.185.59` | 2026-06-28T20:51:34 |
| `root` | `lkjhgf` | `209.99.185.59` | 2026-06-28T20:52:23 |
| `test2` | `1234` | `209.99.185.59` | 2026-06-28T20:53:13 |
| `root` | `P@ssw0rd456` | `45.205.1.42` | 2026-06-28T20:53:32 |
| `ubuntu` | `Changeme_123` | `209.99.185.59` | 2026-06-28T20:54:02 |
| `admin` | `admin` | `8.221.121.6` | 2026-06-28T20:54:21 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-28T20:54:22 |
| `jira` | `pass123` | `209.99.185.59` | 2026-06-28T20:54:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **308** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 161 |
| libssh | 6 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 154 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 4 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 154 | 5 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 4 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `195.178.110.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS10396` | DATACOM CARIBE, INC. | 1 | MEDIUM |
| `AS197170` | TechTies Inc. | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (160)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-97ccc2525430

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 18:55 |
| **Last Seen** | 2026-06-28 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:55:14` | `cowrie.session.connect` |
| `2026-06-28 18:55:15` | `cowrie.client.version` |
| `2026-06-28 18:55:15` | `cowrie.client.kex` |
| `2026-06-28 18:55:17` | `cowrie.login.success` |
| `2026-06-28 18:55:19` | `cowrie.session.params` |
| `2026-06-28 18:55:19` | `cowrie.command.input` |
| `2026-06-28 18:55:19` | `cowrie.log.closed` |
| `2026-06-28 18:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d2d0822499

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:55 |
| **Last Seen** | 2026-06-28 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:55:50` | `cowrie.session.connect` |
| `2026-06-28 18:55:50` | `cowrie.client.version` |
| `2026-06-28 18:55:50` | `cowrie.client.kex` |
| `2026-06-28 18:55:50` | `cowrie.login.success` |
| `2026-06-28 18:55:51` | `cowrie.session.params` |
| `2026-06-28 18:55:51` | `cowrie.command.input` |
| `2026-06-28 18:55:51` | `cowrie.log.closed` |
| `2026-06-28 18:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c0a82619f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:56 |
| **Last Seen** | 2026-06-28 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:56:45` | `cowrie.session.connect` |
| `2026-06-28 18:56:45` | `cowrie.client.version` |
| `2026-06-28 18:56:45` | `cowrie.client.kex` |
| `2026-06-28 18:56:45` | `cowrie.login.success` |
| `2026-06-28 18:56:46` | `cowrie.session.params` |
| `2026-06-28 18:56:46` | `cowrie.command.input` |
| `2026-06-28 18:56:46` | `cowrie.log.closed` |
| `2026-06-28 18:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e02898bc4d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:57 |
| **Last Seen** | 2026-06-28 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:57:21` | `cowrie.session.connect` |
| `2026-06-28 18:57:21` | `cowrie.client.version` |
| `2026-06-28 18:57:21` | `cowrie.client.kex` |
| `2026-06-28 18:57:21` | `cowrie.login.success` |
| `2026-06-28 18:57:22` | `cowrie.session.params` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.success` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.command.input` |
| `2026-06-28 18:57:22` | `cowrie.log.closed` |
| `2026-06-28 18:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89059c39e44d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:57 |
| **Last Seen** | 2026-06-28 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:57:39` | `cowrie.session.connect` |
| `2026-06-28 18:57:39` | `cowrie.client.version` |
| `2026-06-28 18:57:39` | `cowrie.client.kex` |
| `2026-06-28 18:57:39` | `cowrie.login.success` |
| `2026-06-28 18:57:40` | `cowrie.session.params` |
| `2026-06-28 18:57:40` | `cowrie.command.input` |
| `2026-06-28 18:57:40` | `cowrie.log.closed` |
| `2026-06-28 18:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c2153fe599

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:58 |
| **Last Seen** | 2026-06-28 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:58:34` | `cowrie.session.connect` |
| `2026-06-28 18:58:34` | `cowrie.client.version` |
| `2026-06-28 18:58:34` | `cowrie.client.kex` |
| `2026-06-28 18:58:34` | `cowrie.login.success` |
| `2026-06-28 18:58:35` | `cowrie.session.params` |
| `2026-06-28 18:58:35` | `cowrie.command.input` |
| `2026-06-28 18:58:35` | `cowrie.log.closed` |
| `2026-06-28 18:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24acf0e15192

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:59 |
| **Last Seen** | 2026-06-28 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:59:30` | `cowrie.session.connect` |
| `2026-06-28 18:59:30` | `cowrie.client.version` |
| `2026-06-28 18:59:30` | `cowrie.client.kex` |
| `2026-06-28 18:59:30` | `cowrie.login.success` |
| `2026-06-28 18:59:31` | `cowrie.session.params` |
| `2026-06-28 18:59:31` | `cowrie.command.input` |
| `2026-06-28 18:59:31` | `cowrie.log.closed` |
| `2026-06-28 18:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d49e2f9d0d9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:00 |
| **Last Seen** | 2026-06-28 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:00:30` | `cowrie.session.connect` |
| `2026-06-28 19:00:30` | `cowrie.client.version` |
| `2026-06-28 19:00:30` | `cowrie.client.kex` |
| `2026-06-28 19:00:31` | `cowrie.login.success` |
| `2026-06-28 19:00:32` | `cowrie.session.params` |
| `2026-06-28 19:00:32` | `cowrie.command.input` |
| `2026-06-28 19:00:32` | `cowrie.log.closed` |
| `2026-06-28 19:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f24b8da2dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:01 |
| **Last Seen** | 2026-06-28 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:01:28` | `cowrie.session.connect` |
| `2026-06-28 19:01:28` | `cowrie.client.version` |
| `2026-06-28 19:01:28` | `cowrie.client.kex` |
| `2026-06-28 19:01:28` | `cowrie.login.success` |
| `2026-06-28 19:01:29` | `cowrie.session.params` |
| `2026-06-28 19:01:29` | `cowrie.command.input` |
| `2026-06-28 19:01:29` | `cowrie.log.closed` |
| `2026-06-28 19:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6828765cefd2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:02 |
| **Last Seen** | 2026-06-28 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:02:24` | `cowrie.session.connect` |
| `2026-06-28 19:02:24` | `cowrie.client.version` |
| `2026-06-28 19:02:24` | `cowrie.client.kex` |
| `2026-06-28 19:02:24` | `cowrie.login.success` |
| `2026-06-28 19:02:25` | `cowrie.session.params` |
| `2026-06-28 19:02:25` | `cowrie.command.input` |
| `2026-06-28 19:02:25` | `cowrie.log.closed` |
| `2026-06-28 19:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3d3eec735c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 19:02 |
| **Last Seen** | 2026-06-28 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:02:41` | `cowrie.session.connect` |
| `2026-06-28 19:02:41` | `cowrie.client.version` |
| `2026-06-28 19:02:41` | `cowrie.client.kex` |
| `2026-06-28 19:02:42` | `cowrie.login.success` |
| `2026-06-28 19:02:42` | `cowrie.session.params` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.success` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:42` | `cowrie.command.input` |
| `2026-06-28 19:02:43` | `cowrie.log.closed` |
| `2026-06-28 19:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97f6c14301f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:03 |
| **Last Seen** | 2026-06-28 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:03:22` | `cowrie.session.connect` |
| `2026-06-28 19:03:22` | `cowrie.client.version` |
| `2026-06-28 19:03:22` | `cowrie.client.kex` |
| `2026-06-28 19:03:22` | `cowrie.login.success` |
| `2026-06-28 19:03:23` | `cowrie.session.params` |
| `2026-06-28 19:03:23` | `cowrie.command.input` |
| `2026-06-28 19:03:23` | `cowrie.log.closed` |
| `2026-06-28 19:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87098586d5ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:04 |
| **Last Seen** | 2026-06-28 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:04:17` | `cowrie.session.connect` |
| `2026-06-28 19:04:17` | `cowrie.client.version` |
| `2026-06-28 19:04:17` | `cowrie.client.kex` |
| `2026-06-28 19:04:17` | `cowrie.login.success` |
| `2026-06-28 19:04:18` | `cowrie.session.params` |
| `2026-06-28 19:04:18` | `cowrie.command.input` |
| `2026-06-28 19:04:18` | `cowrie.log.closed` |
| `2026-06-28 19:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff7dd033e21f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:05 |
| **Last Seen** | 2026-06-28 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:05:11` | `cowrie.session.connect` |
| `2026-06-28 19:05:11` | `cowrie.client.version` |
| `2026-06-28 19:05:11` | `cowrie.client.kex` |
| `2026-06-28 19:05:12` | `cowrie.login.success` |
| `2026-06-28 19:05:13` | `cowrie.session.params` |
| `2026-06-28 19:05:13` | `cowrie.command.input` |
| `2026-06-28 19:05:13` | `cowrie.log.closed` |
| `2026-06-28 19:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94239bf79fc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 19:06 |
| **Last Seen** | 2026-06-28 19:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:06:07` | `cowrie.session.connect` |
| `2026-06-28 19:06:08` | `cowrie.client.version` |
| `2026-06-28 19:06:08` | `cowrie.client.kex` |
| `2026-06-28 19:06:15` | `cowrie.login.success` |
| `2026-06-28 19:06:18` | `cowrie.session.params` |
| `2026-06-28 19:06:18` | `cowrie.command.input` |
| `2026-06-28 19:06:20` | `cowrie.log.closed` |
| `2026-06-28 19:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7f683ddb3c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:06 |
| **Last Seen** | 2026-06-28 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:06:08` | `cowrie.session.connect` |
| `2026-06-28 19:06:08` | `cowrie.client.version` |
| `2026-06-28 19:06:08` | `cowrie.client.kex` |
| `2026-06-28 19:06:09` | `cowrie.login.success` |
| `2026-06-28 19:06:09` | `cowrie.session.params` |
| `2026-06-28 19:06:09` | `cowrie.command.input` |
| `2026-06-28 19:06:10` | `cowrie.log.closed` |
| `2026-06-28 19:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0708ef7879

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:07 |
| **Last Seen** | 2026-06-28 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:07:04` | `cowrie.session.connect` |
| `2026-06-28 19:07:04` | `cowrie.client.version` |
| `2026-06-28 19:07:04` | `cowrie.client.kex` |
| `2026-06-28 19:07:04` | `cowrie.login.success` |
| `2026-06-28 19:07:05` | `cowrie.session.params` |
| `2026-06-28 19:07:05` | `cowrie.command.input` |
| `2026-06-28 19:07:05` | `cowrie.log.closed` |
| `2026-06-28 19:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926ac269200d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:08 |
| **Last Seen** | 2026-06-28 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:08:01` | `cowrie.session.connect` |
| `2026-06-28 19:08:01` | `cowrie.client.version` |
| `2026-06-28 19:08:01` | `cowrie.client.kex` |
| `2026-06-28 19:08:01` | `cowrie.login.success` |
| `2026-06-28 19:08:02` | `cowrie.session.params` |
| `2026-06-28 19:08:02` | `cowrie.command.input` |
| `2026-06-28 19:08:02` | `cowrie.log.closed` |
| `2026-06-28 19:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dcc5b2578b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 19:08 |
| **Last Seen** | 2026-06-28 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:08:42` | `cowrie.session.connect` |
| `2026-06-28 19:08:42` | `cowrie.client.version` |
| `2026-06-28 19:08:42` | `cowrie.client.kex` |
| `2026-06-28 19:08:43` | `cowrie.login.success` |
| `2026-06-28 19:08:43` | `cowrie.session.params` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.success` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:43` | `cowrie.command.input` |
| `2026-06-28 19:08:44` | `cowrie.log.closed` |
| `2026-06-28 19:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7257e0059f7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:08 |
| **Last Seen** | 2026-06-28 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:08:56` | `cowrie.session.connect` |
| `2026-06-28 19:08:56` | `cowrie.client.version` |
| `2026-06-28 19:08:56` | `cowrie.client.kex` |
| `2026-06-28 19:08:56` | `cowrie.login.success` |
| `2026-06-28 19:08:57` | `cowrie.session.params` |
| `2026-06-28 19:08:57` | `cowrie.command.input` |
| `2026-06-28 19:08:57` | `cowrie.log.closed` |
| `2026-06-28 19:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802222be9afc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:09 |
| **Last Seen** | 2026-06-28 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:09:51` | `cowrie.session.connect` |
| `2026-06-28 19:09:51` | `cowrie.client.version` |
| `2026-06-28 19:09:51` | `cowrie.client.kex` |
| `2026-06-28 19:09:51` | `cowrie.login.success` |
| `2026-06-28 19:09:52` | `cowrie.session.params` |
| `2026-06-28 19:09:52` | `cowrie.command.input` |
| `2026-06-28 19:09:52` | `cowrie.log.closed` |
| `2026-06-28 19:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c8983158ef9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 19:09 |
| **Last Seen** | 2026-06-28 19:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:09:58` | `cowrie.session.connect` |
| `2026-06-28 19:09:58` | `cowrie.client.version` |
| `2026-06-28 19:09:58` | `cowrie.client.kex` |
| `2026-06-28 19:10:00` | `cowrie.login.success` |
| `2026-06-28 19:10:02` | `cowrie.session.params` |
| `2026-06-28 19:10:02` | `cowrie.command.input` |
| `2026-06-28 19:10:02` | `cowrie.log.closed` |
| `2026-06-28 19:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b40b5b6ab8a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:10 |
| **Last Seen** | 2026-06-28 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:10:46` | `cowrie.session.connect` |
| `2026-06-28 19:10:46` | `cowrie.client.version` |
| `2026-06-28 19:10:46` | `cowrie.client.kex` |
| `2026-06-28 19:10:46` | `cowrie.login.success` |
| `2026-06-28 19:10:47` | `cowrie.session.params` |
| `2026-06-28 19:10:47` | `cowrie.command.input` |
| `2026-06-28 19:10:47` | `cowrie.log.closed` |
| `2026-06-28 19:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6c16b8f3de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:11 |
| **Last Seen** | 2026-06-28 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:11:42` | `cowrie.session.connect` |
| `2026-06-28 19:11:42` | `cowrie.client.version` |
| `2026-06-28 19:11:42` | `cowrie.client.kex` |
| `2026-06-28 19:11:43` | `cowrie.login.success` |
| `2026-06-28 19:11:43` | `cowrie.session.params` |
| `2026-06-28 19:11:43` | `cowrie.command.input` |
| `2026-06-28 19:11:43` | `cowrie.log.closed` |
| `2026-06-28 19:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b6519b61f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:12 |
| **Last Seen** | 2026-06-28 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:12:39` | `cowrie.session.connect` |
| `2026-06-28 19:12:39` | `cowrie.client.version` |
| `2026-06-28 19:12:39` | `cowrie.client.kex` |
| `2026-06-28 19:12:40` | `cowrie.login.success` |
| `2026-06-28 19:12:41` | `cowrie.session.params` |
| `2026-06-28 19:12:41` | `cowrie.command.input` |
| `2026-06-28 19:12:41` | `cowrie.log.closed` |
| `2026-06-28 19:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5880cae03831

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:13 |
| **Last Seen** | 2026-06-28 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:13:38` | `cowrie.session.connect` |
| `2026-06-28 19:13:38` | `cowrie.client.version` |
| `2026-06-28 19:13:38` | `cowrie.client.kex` |
| `2026-06-28 19:13:39` | `cowrie.login.success` |
| `2026-06-28 19:13:39` | `cowrie.session.params` |
| `2026-06-28 19:13:39` | `cowrie.command.input` |
| `2026-06-28 19:13:39` | `cowrie.log.closed` |
| `2026-06-28 19:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0663af856fa1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:14 |
| **Last Seen** | 2026-06-28 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:14:37` | `cowrie.session.connect` |
| `2026-06-28 19:14:37` | `cowrie.client.version` |
| `2026-06-28 19:14:37` | `cowrie.client.kex` |
| `2026-06-28 19:14:38` | `cowrie.login.success` |
| `2026-06-28 19:14:39` | `cowrie.session.params` |
| `2026-06-28 19:14:39` | `cowrie.command.input` |
| `2026-06-28 19:14:39` | `cowrie.log.closed` |
| `2026-06-28 19:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65cd8afa5316

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 19:15 |
| **Last Seen** | 2026-06-28 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:15:15` | `cowrie.session.connect` |
| `2026-06-28 19:15:15` | `cowrie.client.version` |
| `2026-06-28 19:15:15` | `cowrie.client.kex` |
| `2026-06-28 19:15:16` | `cowrie.login.success` |
| `2026-06-28 19:15:16` | `cowrie.session.params` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.success` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:16` | `cowrie.command.input` |
| `2026-06-28 19:15:17` | `cowrie.log.closed` |
| `2026-06-28 19:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf385e679800

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:15 |
| **Last Seen** | 2026-06-28 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:15:36` | `cowrie.session.connect` |
| `2026-06-28 19:15:36` | `cowrie.client.version` |
| `2026-06-28 19:15:37` | `cowrie.client.kex` |
| `2026-06-28 19:15:37` | `cowrie.login.success` |
| `2026-06-28 19:15:38` | `cowrie.session.params` |
| `2026-06-28 19:15:38` | `cowrie.command.input` |
| `2026-06-28 19:15:38` | `cowrie.log.closed` |
| `2026-06-28 19:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dad5ba4cf2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:16 |
| **Last Seen** | 2026-06-28 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:16:34` | `cowrie.session.connect` |
| `2026-06-28 19:16:34` | `cowrie.client.version` |
| `2026-06-28 19:16:34` | `cowrie.client.kex` |
| `2026-06-28 19:16:34` | `cowrie.login.success` |
| `2026-06-28 19:16:35` | `cowrie.session.params` |
| `2026-06-28 19:16:35` | `cowrie.command.input` |
| `2026-06-28 19:16:35` | `cowrie.log.closed` |
| `2026-06-28 19:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1045c1b2ed

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 19:17 |
| **Last Seen** | 2026-06-28 19:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:17:28` | `cowrie.session.connect` |
| `2026-06-28 19:17:29` | `cowrie.client.version` |
| `2026-06-28 19:17:29` | `cowrie.client.kex` |
| `2026-06-28 19:17:36` | `cowrie.login.success` |
| `2026-06-28 19:17:39` | `cowrie.session.params` |
| `2026-06-28 19:17:39` | `cowrie.command.input` |
| `2026-06-28 19:17:41` | `cowrie.log.closed` |
| `2026-06-28 19:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5986c48455c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:17 |
| **Last Seen** | 2026-06-28 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:17:33` | `cowrie.session.connect` |
| `2026-06-28 19:17:33` | `cowrie.client.version` |
| `2026-06-28 19:17:33` | `cowrie.client.kex` |
| `2026-06-28 19:17:33` | `cowrie.login.success` |
| `2026-06-28 19:17:34` | `cowrie.session.params` |
| `2026-06-28 19:17:34` | `cowrie.command.input` |
| `2026-06-28 19:17:34` | `cowrie.log.closed` |
| `2026-06-28 19:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e23c841b4274

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:18 |
| **Last Seen** | 2026-06-28 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:18:36` | `cowrie.session.connect` |
| `2026-06-28 19:18:36` | `cowrie.client.version` |
| `2026-06-28 19:18:37` | `cowrie.client.kex` |
| `2026-06-28 19:18:37` | `cowrie.login.success` |
| `2026-06-28 19:18:38` | `cowrie.session.params` |
| `2026-06-28 19:18:38` | `cowrie.command.input` |
| `2026-06-28 19:18:38` | `cowrie.log.closed` |
| `2026-06-28 19:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985a76af489c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:19 |
| **Last Seen** | 2026-06-28 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:19:38` | `cowrie.session.connect` |
| `2026-06-28 19:19:38` | `cowrie.client.version` |
| `2026-06-28 19:19:38` | `cowrie.client.kex` |
| `2026-06-28 19:19:38` | `cowrie.login.success` |
| `2026-06-28 19:19:39` | `cowrie.session.params` |
| `2026-06-28 19:19:39` | `cowrie.command.input` |
| `2026-06-28 19:19:39` | `cowrie.log.closed` |
| `2026-06-28 19:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baac99bef1b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:20 |
| **Last Seen** | 2026-06-28 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:20:37` | `cowrie.session.connect` |
| `2026-06-28 19:20:37` | `cowrie.client.version` |
| `2026-06-28 19:20:37` | `cowrie.client.kex` |
| `2026-06-28 19:20:37` | `cowrie.login.success` |
| `2026-06-28 19:20:38` | `cowrie.session.params` |
| `2026-06-28 19:20:38` | `cowrie.command.input` |
| `2026-06-28 19:20:38` | `cowrie.log.closed` |
| `2026-06-28 19:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb3d19e81a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:21 |
| **Last Seen** | 2026-06-28 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:21:36` | `cowrie.session.connect` |
| `2026-06-28 19:21:36` | `cowrie.client.version` |
| `2026-06-28 19:21:36` | `cowrie.client.kex` |
| `2026-06-28 19:21:37` | `cowrie.login.success` |
| `2026-06-28 19:21:38` | `cowrie.session.params` |
| `2026-06-28 19:21:38` | `cowrie.command.input` |
| `2026-06-28 19:21:38` | `cowrie.log.closed` |
| `2026-06-28 19:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b5ef0d2c23

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:22 |
| **Last Seen** | 2026-06-28 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:22:34` | `cowrie.session.connect` |
| `2026-06-28 19:22:34` | `cowrie.client.version` |
| `2026-06-28 19:22:34` | `cowrie.client.kex` |
| `2026-06-28 19:22:35` | `cowrie.login.success` |
| `2026-06-28 19:22:36` | `cowrie.session.params` |
| `2026-06-28 19:22:36` | `cowrie.command.input` |
| `2026-06-28 19:22:36` | `cowrie.log.closed` |
| `2026-06-28 19:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02878bd43af2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:23 |
| **Last Seen** | 2026-06-28 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:23:33` | `cowrie.session.connect` |
| `2026-06-28 19:23:33` | `cowrie.client.version` |
| `2026-06-28 19:23:33` | `cowrie.client.kex` |
| `2026-06-28 19:23:33` | `cowrie.login.success` |
| `2026-06-28 19:23:34` | `cowrie.session.params` |
| `2026-06-28 19:23:34` | `cowrie.command.input` |
| `2026-06-28 19:23:34` | `cowrie.log.closed` |
| `2026-06-28 19:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8873eb7f1d61

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:24 |
| **Last Seen** | 2026-06-28 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:24:31` | `cowrie.session.connect` |
| `2026-06-28 19:24:31` | `cowrie.client.version` |
| `2026-06-28 19:24:31` | `cowrie.client.kex` |
| `2026-06-28 19:24:32` | `cowrie.login.success` |
| `2026-06-28 19:24:32` | `cowrie.session.params` |
| `2026-06-28 19:24:32` | `cowrie.command.input` |
| `2026-06-28 19:24:32` | `cowrie.log.closed` |
| `2026-06-28 19:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f975d5b71c9c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 19:24 |
| **Last Seen** | 2026-06-28 19:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:24:46` | `cowrie.session.connect` |
| `2026-06-28 19:24:47` | `cowrie.client.version` |
| `2026-06-28 19:24:47` | `cowrie.client.kex` |
| `2026-06-28 19:24:49` | `cowrie.login.success` |
| `2026-06-28 19:24:50` | `cowrie.session.params` |
| `2026-06-28 19:24:50` | `cowrie.command.input` |
| `2026-06-28 19:24:50` | `cowrie.log.closed` |
| `2026-06-28 19:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-939831469cf4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:25 |
| **Last Seen** | 2026-06-28 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:25:30` | `cowrie.session.connect` |
| `2026-06-28 19:25:30` | `cowrie.client.version` |
| `2026-06-28 19:25:30` | `cowrie.client.kex` |
| `2026-06-28 19:25:31` | `cowrie.login.success` |
| `2026-06-28 19:25:32` | `cowrie.session.params` |
| `2026-06-28 19:25:32` | `cowrie.command.input` |
| `2026-06-28 19:25:32` | `cowrie.log.closed` |
| `2026-06-28 19:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9784693e58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:26 |
| **Last Seen** | 2026-06-28 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:26:31` | `cowrie.session.connect` |
| `2026-06-28 19:26:31` | `cowrie.client.version` |
| `2026-06-28 19:26:31` | `cowrie.client.kex` |
| `2026-06-28 19:26:31` | `cowrie.login.success` |
| `2026-06-28 19:26:32` | `cowrie.session.params` |
| `2026-06-28 19:26:32` | `cowrie.command.input` |
| `2026-06-28 19:26:32` | `cowrie.log.closed` |
| `2026-06-28 19:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c57a76574f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:27 |
| **Last Seen** | 2026-06-28 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:27:32` | `cowrie.session.connect` |
| `2026-06-28 19:27:32` | `cowrie.client.version` |
| `2026-06-28 19:27:32` | `cowrie.client.kex` |
| `2026-06-28 19:27:32` | `cowrie.login.success` |
| `2026-06-28 19:27:33` | `cowrie.session.params` |
| `2026-06-28 19:27:33` | `cowrie.command.input` |
| `2026-06-28 19:27:33` | `cowrie.log.closed` |
| `2026-06-28 19:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d1b36755da

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 19:28 |
| **Last Seen** | 2026-06-28 19:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:28:26` | `cowrie.session.connect` |
| `2026-06-28 19:28:28` | `cowrie.client.version` |
| `2026-06-28 19:28:28` | `cowrie.client.kex` |
| `2026-06-28 19:28:33` | `cowrie.login.success` |
| `2026-06-28 19:28:37` | `cowrie.session.params` |
| `2026-06-28 19:28:37` | `cowrie.command.input` |
| `2026-06-28 19:28:39` | `cowrie.log.closed` |
| `2026-06-28 19:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79140214438

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:28 |
| **Last Seen** | 2026-06-28 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:28:33` | `cowrie.session.connect` |
| `2026-06-28 19:28:33` | `cowrie.client.version` |
| `2026-06-28 19:28:33` | `cowrie.client.kex` |
| `2026-06-28 19:28:33` | `cowrie.login.success` |
| `2026-06-28 19:28:34` | `cowrie.session.params` |
| `2026-06-28 19:28:34` | `cowrie.command.input` |
| `2026-06-28 19:28:34` | `cowrie.log.closed` |
| `2026-06-28 19:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e628c0ce64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:29 |
| **Last Seen** | 2026-06-28 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:29:33` | `cowrie.session.connect` |
| `2026-06-28 19:29:33` | `cowrie.client.version` |
| `2026-06-28 19:29:33` | `cowrie.client.kex` |
| `2026-06-28 19:29:33` | `cowrie.login.success` |
| `2026-06-28 19:29:34` | `cowrie.session.params` |
| `2026-06-28 19:29:34` | `cowrie.command.input` |
| `2026-06-28 19:29:34` | `cowrie.log.closed` |
| `2026-06-28 19:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2abd919c2e99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:30 |
| **Last Seen** | 2026-06-28 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:30:32` | `cowrie.session.connect` |
| `2026-06-28 19:30:32` | `cowrie.client.version` |
| `2026-06-28 19:30:33` | `cowrie.client.kex` |
| `2026-06-28 19:30:33` | `cowrie.login.success` |
| `2026-06-28 19:30:34` | `cowrie.session.params` |
| `2026-06-28 19:30:34` | `cowrie.command.input` |
| `2026-06-28 19:30:34` | `cowrie.log.closed` |
| `2026-06-28 19:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e37440803b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:31 |
| **Last Seen** | 2026-06-28 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:31:34` | `cowrie.session.connect` |
| `2026-06-28 19:31:34` | `cowrie.client.version` |
| `2026-06-28 19:31:34` | `cowrie.client.kex` |
| `2026-06-28 19:31:34` | `cowrie.login.success` |
| `2026-06-28 19:31:35` | `cowrie.session.params` |
| `2026-06-28 19:31:35` | `cowrie.command.input` |
| `2026-06-28 19:31:35` | `cowrie.log.closed` |
| `2026-06-28 19:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ffb97e56a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:32 |
| **Last Seen** | 2026-06-28 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:32:36` | `cowrie.session.connect` |
| `2026-06-28 19:32:36` | `cowrie.client.version` |
| `2026-06-28 19:32:36` | `cowrie.client.kex` |
| `2026-06-28 19:32:37` | `cowrie.login.success` |
| `2026-06-28 19:32:38` | `cowrie.session.params` |
| `2026-06-28 19:32:38` | `cowrie.command.input` |
| `2026-06-28 19:32:38` | `cowrie.log.closed` |
| `2026-06-28 19:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1935eada9bec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:33 |
| **Last Seen** | 2026-06-28 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:33:40` | `cowrie.session.connect` |
| `2026-06-28 19:33:40` | `cowrie.client.version` |
| `2026-06-28 19:33:40` | `cowrie.client.kex` |
| `2026-06-28 19:33:41` | `cowrie.login.success` |
| `2026-06-28 19:33:41` | `cowrie.session.params` |
| `2026-06-28 19:33:41` | `cowrie.command.input` |
| `2026-06-28 19:33:41` | `cowrie.log.closed` |
| `2026-06-28 19:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cd1cd08114

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:34 |
| **Last Seen** | 2026-06-28 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:34:40` | `cowrie.session.connect` |
| `2026-06-28 19:34:40` | `cowrie.client.version` |
| `2026-06-28 19:34:40` | `cowrie.client.kex` |
| `2026-06-28 19:34:41` | `cowrie.login.success` |
| `2026-06-28 19:34:42` | `cowrie.session.params` |
| `2026-06-28 19:34:42` | `cowrie.command.input` |
| `2026-06-28 19:34:42` | `cowrie.log.closed` |
| `2026-06-28 19:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78682527b05b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:35 |
| **Last Seen** | 2026-06-28 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:35:41` | `cowrie.session.connect` |
| `2026-06-28 19:35:41` | `cowrie.client.version` |
| `2026-06-28 19:35:41` | `cowrie.client.kex` |
| `2026-06-28 19:35:41` | `cowrie.login.success` |
| `2026-06-28 19:35:42` | `cowrie.session.params` |
| `2026-06-28 19:35:42` | `cowrie.command.input` |
| `2026-06-28 19:35:42` | `cowrie.log.closed` |
| `2026-06-28 19:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ab9e9a41bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:36 |
| **Last Seen** | 2026-06-28 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:36:40` | `cowrie.session.connect` |
| `2026-06-28 19:36:40` | `cowrie.client.version` |
| `2026-06-28 19:36:40` | `cowrie.client.kex` |
| `2026-06-28 19:36:41` | `cowrie.login.success` |
| `2026-06-28 19:36:42` | `cowrie.session.params` |
| `2026-06-28 19:36:42` | `cowrie.command.input` |
| `2026-06-28 19:36:42` | `cowrie.log.closed` |
| `2026-06-28 19:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d691675d59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:37 |
| **Last Seen** | 2026-06-28 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:37:41` | `cowrie.session.connect` |
| `2026-06-28 19:37:41` | `cowrie.client.version` |
| `2026-06-28 19:37:41` | `cowrie.client.kex` |
| `2026-06-28 19:37:42` | `cowrie.login.success` |
| `2026-06-28 19:37:43` | `cowrie.session.params` |
| `2026-06-28 19:37:43` | `cowrie.command.input` |
| `2026-06-28 19:37:43` | `cowrie.log.closed` |
| `2026-06-28 19:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7421db9aeb16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:38 |
| **Last Seen** | 2026-06-28 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:38:43` | `cowrie.session.connect` |
| `2026-06-28 19:38:43` | `cowrie.client.version` |
| `2026-06-28 19:38:43` | `cowrie.client.kex` |
| `2026-06-28 19:38:44` | `cowrie.login.success` |
| `2026-06-28 19:38:44` | `cowrie.session.params` |
| `2026-06-28 19:38:44` | `cowrie.command.input` |
| `2026-06-28 19:38:44` | `cowrie.log.closed` |
| `2026-06-28 19:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4d9c839a63

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 19:39 |
| **Last Seen** | 2026-06-28 19:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:39:27` | `cowrie.session.connect` |
| `2026-06-28 19:39:27` | `cowrie.client.version` |
| `2026-06-28 19:39:27` | `cowrie.client.kex` |
| `2026-06-28 19:39:28` | `cowrie.login.success` |
| `2026-06-28 19:39:30` | `cowrie.session.params` |
| `2026-06-28 19:39:30` | `cowrie.command.input` |
| `2026-06-28 19:39:30` | `cowrie.log.closed` |
| `2026-06-28 19:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e72969dfeb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:39 |
| **Last Seen** | 2026-06-28 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:39:47` | `cowrie.session.connect` |
| `2026-06-28 19:39:47` | `cowrie.client.version` |
| `2026-06-28 19:39:47` | `cowrie.client.kex` |
| `2026-06-28 19:39:47` | `cowrie.login.success` |
| `2026-06-28 19:39:48` | `cowrie.session.params` |
| `2026-06-28 19:39:48` | `cowrie.command.input` |
| `2026-06-28 19:39:48` | `cowrie.log.closed` |
| `2026-06-28 19:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cad18225ef1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 19:40 |
| **Last Seen** | 2026-06-28 19:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:40:03` | `cowrie.session.connect` |
| `2026-06-28 19:40:06` | `cowrie.client.version` |
| `2026-06-28 19:40:06` | `cowrie.client.kex` |
| `2026-06-28 19:40:11` | `cowrie.login.success` |
| `2026-06-28 19:40:15` | `cowrie.session.params` |
| `2026-06-28 19:40:15` | `cowrie.command.input` |
| `2026-06-28 19:40:16` | `cowrie.log.closed` |
| `2026-06-28 19:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-258f050cf84e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:40 |
| **Last Seen** | 2026-06-28 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:40:50` | `cowrie.session.connect` |
| `2026-06-28 19:40:50` | `cowrie.client.version` |
| `2026-06-28 19:40:50` | `cowrie.client.kex` |
| `2026-06-28 19:40:50` | `cowrie.login.success` |
| `2026-06-28 19:40:51` | `cowrie.session.params` |
| `2026-06-28 19:40:51` | `cowrie.command.input` |
| `2026-06-28 19:40:51` | `cowrie.log.closed` |
| `2026-06-28 19:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b469987e40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:41 |
| **Last Seen** | 2026-06-28 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:41:52` | `cowrie.session.connect` |
| `2026-06-28 19:41:52` | `cowrie.client.version` |
| `2026-06-28 19:41:52` | `cowrie.client.kex` |
| `2026-06-28 19:41:53` | `cowrie.login.success` |
| `2026-06-28 19:41:53` | `cowrie.session.params` |
| `2026-06-28 19:41:53` | `cowrie.command.input` |
| `2026-06-28 19:41:54` | `cowrie.log.closed` |
| `2026-06-28 19:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9f7325d6cf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:42 |
| **Last Seen** | 2026-06-28 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:42:55` | `cowrie.session.connect` |
| `2026-06-28 19:42:55` | `cowrie.client.version` |
| `2026-06-28 19:42:55` | `cowrie.client.kex` |
| `2026-06-28 19:42:55` | `cowrie.login.success` |
| `2026-06-28 19:42:56` | `cowrie.session.params` |
| `2026-06-28 19:42:56` | `cowrie.command.input` |
| `2026-06-28 19:42:56` | `cowrie.log.closed` |
| `2026-06-28 19:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13cfde57c545

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:43 |
| **Last Seen** | 2026-06-28 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:43:58` | `cowrie.session.connect` |
| `2026-06-28 19:43:58` | `cowrie.client.version` |
| `2026-06-28 19:43:58` | `cowrie.client.kex` |
| `2026-06-28 19:43:58` | `cowrie.login.success` |
| `2026-06-28 19:43:59` | `cowrie.session.params` |
| `2026-06-28 19:43:59` | `cowrie.command.input` |
| `2026-06-28 19:43:59` | `cowrie.log.closed` |
| `2026-06-28 19:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7398ead9739

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:45 |
| **Last Seen** | 2026-06-28 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:45:02` | `cowrie.session.connect` |
| `2026-06-28 19:45:02` | `cowrie.client.version` |
| `2026-06-28 19:45:02` | `cowrie.client.kex` |
| `2026-06-28 19:45:02` | `cowrie.login.success` |
| `2026-06-28 19:45:03` | `cowrie.session.params` |
| `2026-06-28 19:45:03` | `cowrie.command.input` |
| `2026-06-28 19:45:03` | `cowrie.log.closed` |
| `2026-06-28 19:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d9747a540a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:46 |
| **Last Seen** | 2026-06-28 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:46:06` | `cowrie.session.connect` |
| `2026-06-28 19:46:06` | `cowrie.client.version` |
| `2026-06-28 19:46:06` | `cowrie.client.kex` |
| `2026-06-28 19:46:06` | `cowrie.login.success` |
| `2026-06-28 19:46:07` | `cowrie.session.params` |
| `2026-06-28 19:46:07` | `cowrie.command.input` |
| `2026-06-28 19:46:07` | `cowrie.log.closed` |
| `2026-06-28 19:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2c3e23edf7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:47 |
| **Last Seen** | 2026-06-28 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:47:11` | `cowrie.session.connect` |
| `2026-06-28 19:47:11` | `cowrie.client.version` |
| `2026-06-28 19:47:11` | `cowrie.client.kex` |
| `2026-06-28 19:47:12` | `cowrie.login.success` |
| `2026-06-28 19:47:12` | `cowrie.session.params` |
| `2026-06-28 19:47:12` | `cowrie.command.input` |
| `2026-06-28 19:47:12` | `cowrie.log.closed` |
| `2026-06-28 19:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cf0cb0bd9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:48 |
| **Last Seen** | 2026-06-28 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:48:15` | `cowrie.session.connect` |
| `2026-06-28 19:48:15` | `cowrie.client.version` |
| `2026-06-28 19:48:15` | `cowrie.client.kex` |
| `2026-06-28 19:48:15` | `cowrie.login.success` |
| `2026-06-28 19:48:16` | `cowrie.session.params` |
| `2026-06-28 19:48:16` | `cowrie.command.input` |
| `2026-06-28 19:48:16` | `cowrie.log.closed` |
| `2026-06-28 19:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc39bf142b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:49 |
| **Last Seen** | 2026-06-28 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:49:20` | `cowrie.session.connect` |
| `2026-06-28 19:49:20` | `cowrie.client.version` |
| `2026-06-28 19:49:20` | `cowrie.client.kex` |
| `2026-06-28 19:49:20` | `cowrie.login.success` |
| `2026-06-28 19:49:21` | `cowrie.session.params` |
| `2026-06-28 19:49:21` | `cowrie.command.input` |
| `2026-06-28 19:49:21` | `cowrie.log.closed` |
| `2026-06-28 19:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35dd76316ad1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:50 |
| **Last Seen** | 2026-06-28 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:50:29` | `cowrie.session.connect` |
| `2026-06-28 19:50:29` | `cowrie.client.version` |
| `2026-06-28 19:50:29` | `cowrie.client.kex` |
| `2026-06-28 19:50:30` | `cowrie.login.success` |
| `2026-06-28 19:50:30` | `cowrie.session.params` |
| `2026-06-28 19:50:30` | `cowrie.command.input` |
| `2026-06-28 19:50:31` | `cowrie.log.closed` |
| `2026-06-28 19:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c9d1f8629c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 19:51 |
| **Last Seen** | 2026-06-28 19:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:51:16` | `cowrie.session.connect` |
| `2026-06-28 19:51:17` | `cowrie.client.version` |
| `2026-06-28 19:51:17` | `cowrie.client.kex` |
| `2026-06-28 19:51:23` | `cowrie.login.success` |
| `2026-06-28 19:51:26` | `cowrie.session.params` |
| `2026-06-28 19:51:26` | `cowrie.command.input` |
| `2026-06-28 19:51:27` | `cowrie.log.closed` |
| `2026-06-28 19:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7fa21b186f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:51 |
| **Last Seen** | 2026-06-28 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:51:36` | `cowrie.session.connect` |
| `2026-06-28 19:51:36` | `cowrie.client.version` |
| `2026-06-28 19:51:36` | `cowrie.client.kex` |
| `2026-06-28 19:51:36` | `cowrie.login.success` |
| `2026-06-28 19:51:37` | `cowrie.session.params` |
| `2026-06-28 19:51:37` | `cowrie.command.input` |
| `2026-06-28 19:51:37` | `cowrie.log.closed` |
| `2026-06-28 19:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c75a2231734

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:52 |
| **Last Seen** | 2026-06-28 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:52:42` | `cowrie.session.connect` |
| `2026-06-28 19:52:42` | `cowrie.client.version` |
| `2026-06-28 19:52:42` | `cowrie.client.kex` |
| `2026-06-28 19:52:42` | `cowrie.login.success` |
| `2026-06-28 19:52:43` | `cowrie.session.params` |
| `2026-06-28 19:52:43` | `cowrie.command.input` |
| `2026-06-28 19:52:43` | `cowrie.log.closed` |
| `2026-06-28 19:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e955c0c48810

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:53 |
| **Last Seen** | 2026-06-28 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:53:47` | `cowrie.session.connect` |
| `2026-06-28 19:53:47` | `cowrie.client.version` |
| `2026-06-28 19:53:47` | `cowrie.client.kex` |
| `2026-06-28 19:53:48` | `cowrie.login.success` |
| `2026-06-28 19:53:49` | `cowrie.session.params` |
| `2026-06-28 19:53:49` | `cowrie.command.input` |
| `2026-06-28 19:53:49` | `cowrie.log.closed` |
| `2026-06-28 19:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48daad121017

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 19:54 |
| **Last Seen** | 2026-06-28 19:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:54:05` | `cowrie.session.connect` |
| `2026-06-28 19:54:05` | `cowrie.client.version` |
| `2026-06-28 19:54:05` | `cowrie.client.kex` |
| `2026-06-28 19:54:07` | `cowrie.login.success` |
| `2026-06-28 19:54:09` | `cowrie.session.params` |
| `2026-06-28 19:54:09` | `cowrie.command.input` |
| `2026-06-28 19:54:09` | `cowrie.log.closed` |
| `2026-06-28 19:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9ef4e2a70e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:54 |
| **Last Seen** | 2026-06-28 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:54:52` | `cowrie.session.connect` |
| `2026-06-28 19:54:52` | `cowrie.client.version` |
| `2026-06-28 19:54:52` | `cowrie.client.kex` |
| `2026-06-28 19:54:53` | `cowrie.login.success` |
| `2026-06-28 19:54:53` | `cowrie.session.params` |
| `2026-06-28 19:54:53` | `cowrie.command.input` |
| `2026-06-28 19:54:53` | `cowrie.log.closed` |
| `2026-06-28 19:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ff36c4fa0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:55 |
| **Last Seen** | 2026-06-28 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:55:56` | `cowrie.session.connect` |
| `2026-06-28 19:55:56` | `cowrie.client.version` |
| `2026-06-28 19:55:56` | `cowrie.client.kex` |
| `2026-06-28 19:55:57` | `cowrie.login.success` |
| `2026-06-28 19:55:58` | `cowrie.session.params` |
| `2026-06-28 19:55:58` | `cowrie.command.input` |
| `2026-06-28 19:55:58` | `cowrie.log.closed` |
| `2026-06-28 19:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede0a1f950e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:57 |
| **Last Seen** | 2026-06-28 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:57:01` | `cowrie.session.connect` |
| `2026-06-28 19:57:01` | `cowrie.client.version` |
| `2026-06-28 19:57:01` | `cowrie.client.kex` |
| `2026-06-28 19:57:01` | `cowrie.login.success` |
| `2026-06-28 19:57:02` | `cowrie.session.params` |
| `2026-06-28 19:57:02` | `cowrie.command.input` |
| `2026-06-28 19:57:02` | `cowrie.log.closed` |
| `2026-06-28 19:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99727a9458e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:58 |
| **Last Seen** | 2026-06-28 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:58:07` | `cowrie.session.connect` |
| `2026-06-28 19:58:07` | `cowrie.client.version` |
| `2026-06-28 19:58:08` | `cowrie.client.kex` |
| `2026-06-28 19:58:08` | `cowrie.login.success` |
| `2026-06-28 19:58:09` | `cowrie.session.params` |
| `2026-06-28 19:58:09` | `cowrie.command.input` |
| `2026-06-28 19:58:09` | `cowrie.log.closed` |
| `2026-06-28 19:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69b787f5cca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 19:59 |
| **Last Seen** | 2026-06-28 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 19:59:14` | `cowrie.session.connect` |
| `2026-06-28 19:59:14` | `cowrie.client.version` |
| `2026-06-28 19:59:14` | `cowrie.client.kex` |
| `2026-06-28 19:59:15` | `cowrie.login.success` |
| `2026-06-28 19:59:15` | `cowrie.session.params` |
| `2026-06-28 19:59:15` | `cowrie.command.input` |
| `2026-06-28 19:59:16` | `cowrie.log.closed` |
| `2026-06-28 19:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4876bdca276b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:00 |
| **Last Seen** | 2026-06-28 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:00:19` | `cowrie.session.connect` |
| `2026-06-28 20:00:19` | `cowrie.client.version` |
| `2026-06-28 20:00:19` | `cowrie.client.kex` |
| `2026-06-28 20:00:19` | `cowrie.login.success` |
| `2026-06-28 20:00:20` | `cowrie.session.params` |
| `2026-06-28 20:00:20` | `cowrie.command.input` |
| `2026-06-28 20:00:20` | `cowrie.log.closed` |
| `2026-06-28 20:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4368f87bcbc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:01 |
| **Last Seen** | 2026-06-28 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:01:03` | `cowrie.session.connect` |
| `2026-06-28 20:01:03` | `cowrie.client.version` |
| `2026-06-28 20:01:03` | `cowrie.client.kex` |
| `2026-06-28 20:01:04` | `cowrie.login.success` |
| `2026-06-28 20:01:05` | `cowrie.session.params` |
| `2026-06-28 20:01:05` | `cowrie.command.input` |
| `2026-06-28 20:01:05` | `cowrie.log.closed` |
| `2026-06-28 20:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0edff1b78c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:01 |
| **Last Seen** | 2026-06-28 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:01:46` | `cowrie.session.connect` |
| `2026-06-28 20:01:46` | `cowrie.client.version` |
| `2026-06-28 20:01:46` | `cowrie.client.kex` |
| `2026-06-28 20:01:47` | `cowrie.login.success` |
| `2026-06-28 20:01:47` | `cowrie.session.params` |
| `2026-06-28 20:01:47` | `cowrie.command.input` |
| `2026-06-28 20:01:47` | `cowrie.log.closed` |
| `2026-06-28 20:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fcab380686

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 20:02 |
| **Last Seen** | 2026-06-28 20:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:02:18` | `cowrie.session.connect` |
| `2026-06-28 20:02:19` | `cowrie.client.version` |
| `2026-06-28 20:02:19` | `cowrie.client.kex` |
| `2026-06-28 20:02:24` | `cowrie.login.success` |
| `2026-06-28 20:02:27` | `cowrie.session.params` |
| `2026-06-28 20:02:27` | `cowrie.command.input` |
| `2026-06-28 20:02:28` | `cowrie.log.closed` |
| `2026-06-28 20:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca87855fd69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:02 |
| **Last Seen** | 2026-06-28 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:02:30` | `cowrie.session.connect` |
| `2026-06-28 20:02:30` | `cowrie.client.version` |
| `2026-06-28 20:02:30` | `cowrie.client.kex` |
| `2026-06-28 20:02:30` | `cowrie.login.success` |
| `2026-06-28 20:02:31` | `cowrie.session.params` |
| `2026-06-28 20:02:31` | `cowrie.command.input` |
| `2026-06-28 20:02:31` | `cowrie.log.closed` |
| `2026-06-28 20:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff488df309c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:03 |
| **Last Seen** | 2026-06-28 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:03:14` | `cowrie.session.connect` |
| `2026-06-28 20:03:14` | `cowrie.client.version` |
| `2026-06-28 20:03:14` | `cowrie.client.kex` |
| `2026-06-28 20:03:14` | `cowrie.login.success` |
| `2026-06-28 20:03:15` | `cowrie.session.params` |
| `2026-06-28 20:03:15` | `cowrie.command.input` |
| `2026-06-28 20:03:15` | `cowrie.log.closed` |
| `2026-06-28 20:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3f71ff8ba9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:04 |
| **Last Seen** | 2026-06-28 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:04:05` | `cowrie.session.connect` |
| `2026-06-28 20:04:05` | `cowrie.client.version` |
| `2026-06-28 20:04:06` | `cowrie.client.kex` |
| `2026-06-28 20:04:06` | `cowrie.login.success` |
| `2026-06-28 20:04:07` | `cowrie.session.params` |
| `2026-06-28 20:04:07` | `cowrie.command.input` |
| `2026-06-28 20:04:07` | `cowrie.log.closed` |
| `2026-06-28 20:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a598547d347c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:05 |
| **Last Seen** | 2026-06-28 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:05:08` | `cowrie.session.connect` |
| `2026-06-28 20:05:08` | `cowrie.client.version` |
| `2026-06-28 20:05:08` | `cowrie.client.kex` |
| `2026-06-28 20:05:09` | `cowrie.login.success` |
| `2026-06-28 20:05:09` | `cowrie.session.params` |
| `2026-06-28 20:05:09` | `cowrie.command.input` |
| `2026-06-28 20:05:10` | `cowrie.log.closed` |
| `2026-06-28 20:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef68a98064c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:05 |
| **Last Seen** | 2026-06-28 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:05:53` | `cowrie.session.connect` |
| `2026-06-28 20:05:53` | `cowrie.client.version` |
| `2026-06-28 20:05:53` | `cowrie.client.kex` |
| `2026-06-28 20:05:53` | `cowrie.login.success` |
| `2026-06-28 20:05:54` | `cowrie.session.params` |
| `2026-06-28 20:05:54` | `cowrie.command.input` |
| `2026-06-28 20:05:54` | `cowrie.log.closed` |
| `2026-06-28 20:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c918442ee1c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:06 |
| **Last Seen** | 2026-06-28 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:06:37` | `cowrie.session.connect` |
| `2026-06-28 20:06:37` | `cowrie.client.version` |
| `2026-06-28 20:06:37` | `cowrie.client.kex` |
| `2026-06-28 20:06:38` | `cowrie.login.success` |
| `2026-06-28 20:06:38` | `cowrie.session.params` |
| `2026-06-28 20:06:38` | `cowrie.command.input` |
| `2026-06-28 20:06:38` | `cowrie.log.closed` |
| `2026-06-28 20:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc0545892c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]90` |
| **First Seen** | 2026-06-28 20:06 |
| **Last Seen** | 2026-06-28 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:06:58` | `cowrie.session.connect` |
| `2026-06-28 20:06:58` | `cowrie.client.version` |
| `2026-06-28 20:06:59` | `cowrie.client.kex` |
| `2026-06-28 20:06:59` | `cowrie.login.success` |
| `2026-06-28 20:07:00` | `cowrie.session.params` |
| `2026-06-28 20:07:00` | `cowrie.command.input` |
| `2026-06-28 20:07:00` | `cowrie.log.closed` |
| `2026-06-28 20:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]90` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ea4f7cf631

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]90` |
| **First Seen** | 2026-06-28 20:07 |
| **Last Seen** | 2026-06-28 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:07:00` | `cowrie.session.connect` |
| `2026-06-28 20:07:00` | `cowrie.client.version` |
| `2026-06-28 20:07:00` | `cowrie.client.kex` |
| `2026-06-28 20:07:00` | `cowrie.login.success` |
| `2026-06-28 20:07:01` | `cowrie.session.params` |
| `2026-06-28 20:07:01` | `cowrie.command.input` |
| `2026-06-28 20:07:01` | `cowrie.log.closed` |
| `2026-06-28 20:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]90` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6420dab11347

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:07 |
| **Last Seen** | 2026-06-28 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:07:27` | `cowrie.session.connect` |
| `2026-06-28 20:07:27` | `cowrie.client.version` |
| `2026-06-28 20:07:27` | `cowrie.client.kex` |
| `2026-06-28 20:07:27` | `cowrie.login.success` |
| `2026-06-28 20:07:28` | `cowrie.session.params` |
| `2026-06-28 20:07:28` | `cowrie.command.input` |
| `2026-06-28 20:07:28` | `cowrie.log.closed` |
| `2026-06-28 20:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9bc93727a32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:08 |
| **Last Seen** | 2026-06-28 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:08:27` | `cowrie.session.connect` |
| `2026-06-28 20:08:27` | `cowrie.client.version` |
| `2026-06-28 20:08:28` | `cowrie.client.kex` |
| `2026-06-28 20:08:28` | `cowrie.login.success` |
| `2026-06-28 20:08:29` | `cowrie.session.params` |
| `2026-06-28 20:08:29` | `cowrie.command.input` |
| `2026-06-28 20:08:29` | `cowrie.log.closed` |
| `2026-06-28 20:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b9131f53dab

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 20:09 |
| **Last Seen** | 2026-06-28 20:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:09:02` | `cowrie.session.connect` |
| `2026-06-28 20:09:03` | `cowrie.client.version` |
| `2026-06-28 20:09:03` | `cowrie.client.kex` |
| `2026-06-28 20:09:05` | `cowrie.login.success` |
| `2026-06-28 20:09:06` | `cowrie.session.params` |
| `2026-06-28 20:09:06` | `cowrie.command.input` |
| `2026-06-28 20:09:07` | `cowrie.log.closed` |
| `2026-06-28 20:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce0435d0d96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:09 |
| **Last Seen** | 2026-06-28 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:09:21` | `cowrie.session.connect` |
| `2026-06-28 20:09:21` | `cowrie.client.version` |
| `2026-06-28 20:09:21` | `cowrie.client.kex` |
| `2026-06-28 20:09:22` | `cowrie.login.success` |
| `2026-06-28 20:09:23` | `cowrie.session.params` |
| `2026-06-28 20:09:23` | `cowrie.command.input` |
| `2026-06-28 20:09:23` | `cowrie.log.closed` |
| `2026-06-28 20:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f841b8b4826

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:10 |
| **Last Seen** | 2026-06-28 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:10:22` | `cowrie.session.connect` |
| `2026-06-28 20:10:22` | `cowrie.client.version` |
| `2026-06-28 20:10:22` | `cowrie.client.kex` |
| `2026-06-28 20:10:22` | `cowrie.login.success` |
| `2026-06-28 20:10:23` | `cowrie.session.params` |
| `2026-06-28 20:10:23` | `cowrie.command.input` |
| `2026-06-28 20:10:23` | `cowrie.log.closed` |
| `2026-06-28 20:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5875711c235

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:11 |
| **Last Seen** | 2026-06-28 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:11:08` | `cowrie.session.connect` |
| `2026-06-28 20:11:08` | `cowrie.client.version` |
| `2026-06-28 20:11:09` | `cowrie.client.kex` |
| `2026-06-28 20:11:09` | `cowrie.login.success` |
| `2026-06-28 20:11:10` | `cowrie.session.params` |
| `2026-06-28 20:11:10` | `cowrie.command.input` |
| `2026-06-28 20:11:10` | `cowrie.log.closed` |
| `2026-06-28 20:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978ad054e3ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:11 |
| **Last Seen** | 2026-06-28 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:11:55` | `cowrie.session.connect` |
| `2026-06-28 20:11:55` | `cowrie.client.version` |
| `2026-06-28 20:11:55` | `cowrie.client.kex` |
| `2026-06-28 20:11:55` | `cowrie.login.success` |
| `2026-06-28 20:11:56` | `cowrie.session.params` |
| `2026-06-28 20:11:56` | `cowrie.command.input` |
| `2026-06-28 20:11:56` | `cowrie.log.closed` |
| `2026-06-28 20:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4d876d55b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:12 |
| **Last Seen** | 2026-06-28 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:12:42` | `cowrie.session.connect` |
| `2026-06-28 20:12:42` | `cowrie.client.version` |
| `2026-06-28 20:12:42` | `cowrie.client.kex` |
| `2026-06-28 20:12:42` | `cowrie.login.success` |
| `2026-06-28 20:12:43` | `cowrie.session.params` |
| `2026-06-28 20:12:43` | `cowrie.command.input` |
| `2026-06-28 20:12:43` | `cowrie.log.closed` |
| `2026-06-28 20:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abc179fcdf3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 20:13 |
| **Last Seen** | 2026-06-28 20:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:13:11` | `cowrie.session.connect` |
| `2026-06-28 20:13:12` | `cowrie.client.version` |
| `2026-06-28 20:13:12` | `cowrie.client.kex` |
| `2026-06-28 20:13:17` | `cowrie.login.success` |
| `2026-06-28 20:13:20` | `cowrie.session.params` |
| `2026-06-28 20:13:20` | `cowrie.command.input` |
| `2026-06-28 20:13:21` | `cowrie.log.closed` |
| `2026-06-28 20:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785f0a1789b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:13 |
| **Last Seen** | 2026-06-28 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:13:31` | `cowrie.session.connect` |
| `2026-06-28 20:13:31` | `cowrie.client.version` |
| `2026-06-28 20:13:31` | `cowrie.client.kex` |
| `2026-06-28 20:13:31` | `cowrie.login.success` |
| `2026-06-28 20:13:32` | `cowrie.session.params` |
| `2026-06-28 20:13:32` | `cowrie.command.input` |
| `2026-06-28 20:13:32` | `cowrie.log.closed` |
| `2026-06-28 20:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55848783578c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:14 |
| **Last Seen** | 2026-06-28 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:14:17` | `cowrie.session.connect` |
| `2026-06-28 20:14:17` | `cowrie.client.version` |
| `2026-06-28 20:14:17` | `cowrie.client.kex` |
| `2026-06-28 20:14:17` | `cowrie.login.success` |
| `2026-06-28 20:14:18` | `cowrie.session.params` |
| `2026-06-28 20:14:18` | `cowrie.command.input` |
| `2026-06-28 20:14:18` | `cowrie.log.closed` |
| `2026-06-28 20:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e2febca42c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:15 |
| **Last Seen** | 2026-06-28 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:15:03` | `cowrie.session.connect` |
| `2026-06-28 20:15:03` | `cowrie.client.version` |
| `2026-06-28 20:15:03` | `cowrie.client.kex` |
| `2026-06-28 20:15:03` | `cowrie.login.success` |
| `2026-06-28 20:15:04` | `cowrie.session.params` |
| `2026-06-28 20:15:04` | `cowrie.command.input` |
| `2026-06-28 20:15:04` | `cowrie.log.closed` |
| `2026-06-28 20:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978810ea4dfc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:15 |
| **Last Seen** | 2026-06-28 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:15:50` | `cowrie.session.connect` |
| `2026-06-28 20:15:50` | `cowrie.client.version` |
| `2026-06-28 20:15:51` | `cowrie.client.kex` |
| `2026-06-28 20:15:51` | `cowrie.login.success` |
| `2026-06-28 20:15:52` | `cowrie.session.params` |
| `2026-06-28 20:15:52` | `cowrie.command.input` |
| `2026-06-28 20:15:52` | `cowrie.log.closed` |
| `2026-06-28 20:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2047066e64b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:16 |
| **Last Seen** | 2026-06-28 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:16:39` | `cowrie.session.connect` |
| `2026-06-28 20:16:39` | `cowrie.client.version` |
| `2026-06-28 20:16:39` | `cowrie.client.kex` |
| `2026-06-28 20:16:39` | `cowrie.login.success` |
| `2026-06-28 20:16:40` | `cowrie.session.params` |
| `2026-06-28 20:16:40` | `cowrie.command.input` |
| `2026-06-28 20:16:40` | `cowrie.log.closed` |
| `2026-06-28 20:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9191ee5d1a2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:17 |
| **Last Seen** | 2026-06-28 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:17:28` | `cowrie.session.connect` |
| `2026-06-28 20:17:28` | `cowrie.client.version` |
| `2026-06-28 20:17:28` | `cowrie.client.kex` |
| `2026-06-28 20:17:28` | `cowrie.login.success` |
| `2026-06-28 20:17:29` | `cowrie.session.params` |
| `2026-06-28 20:17:29` | `cowrie.command.input` |
| `2026-06-28 20:17:29` | `cowrie.log.closed` |
| `2026-06-28 20:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ee7e73e7245

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-28 20:17 |
| **Last Seen** | 2026-06-28 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:17:39` | `cowrie.session.connect` |
| `2026-06-28 20:17:39` | `cowrie.client.version` |
| `2026-06-28 20:17:39` | `cowrie.client.kex` |
| `2026-06-28 20:17:39` | `cowrie.login.success` |
| `2026-06-28 20:17:40` | `cowrie.session.params` |
| `2026-06-28 20:17:40` | `cowrie.command.input` |
| `2026-06-28 20:17:40` | `cowrie.log.closed` |
| `2026-06-28 20:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca1f77ff45a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:18 |
| **Last Seen** | 2026-06-28 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:18:17` | `cowrie.session.connect` |
| `2026-06-28 20:18:17` | `cowrie.client.version` |
| `2026-06-28 20:18:17` | `cowrie.client.kex` |
| `2026-06-28 20:18:17` | `cowrie.login.success` |
| `2026-06-28 20:18:18` | `cowrie.session.params` |
| `2026-06-28 20:18:18` | `cowrie.command.input` |
| `2026-06-28 20:18:18` | `cowrie.log.closed` |
| `2026-06-28 20:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ae49f154b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:19 |
| **Last Seen** | 2026-06-28 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:19:06` | `cowrie.session.connect` |
| `2026-06-28 20:19:06` | `cowrie.client.version` |
| `2026-06-28 20:19:06` | `cowrie.client.kex` |
| `2026-06-28 20:19:06` | `cowrie.login.success` |
| `2026-06-28 20:19:07` | `cowrie.session.params` |
| `2026-06-28 20:19:07` | `cowrie.command.input` |
| `2026-06-28 20:19:07` | `cowrie.log.closed` |
| `2026-06-28 20:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbea69d51f6b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:19 |
| **Last Seen** | 2026-06-28 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:19:55` | `cowrie.session.connect` |
| `2026-06-28 20:19:55` | `cowrie.client.version` |
| `2026-06-28 20:19:55` | `cowrie.client.kex` |
| `2026-06-28 20:19:56` | `cowrie.login.success` |
| `2026-06-28 20:19:56` | `cowrie.session.params` |
| `2026-06-28 20:19:56` | `cowrie.command.input` |
| `2026-06-28 20:19:56` | `cowrie.log.closed` |
| `2026-06-28 20:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a06aefbbd9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:20 |
| **Last Seen** | 2026-06-28 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:20:45` | `cowrie.session.connect` |
| `2026-06-28 20:20:45` | `cowrie.client.version` |
| `2026-06-28 20:20:45` | `cowrie.client.kex` |
| `2026-06-28 20:20:45` | `cowrie.login.success` |
| `2026-06-28 20:20:46` | `cowrie.session.params` |
| `2026-06-28 20:20:46` | `cowrie.command.input` |
| `2026-06-28 20:20:46` | `cowrie.log.closed` |
| `2026-06-28 20:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a72eecc72f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:21 |
| **Last Seen** | 2026-06-28 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:21:34` | `cowrie.session.connect` |
| `2026-06-28 20:21:34` | `cowrie.client.version` |
| `2026-06-28 20:21:34` | `cowrie.client.kex` |
| `2026-06-28 20:21:34` | `cowrie.login.success` |
| `2026-06-28 20:21:35` | `cowrie.session.params` |
| `2026-06-28 20:21:35` | `cowrie.command.input` |
| `2026-06-28 20:21:35` | `cowrie.log.closed` |
| `2026-06-28 20:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62240a6c2b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:22 |
| **Last Seen** | 2026-06-28 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:22:24` | `cowrie.session.connect` |
| `2026-06-28 20:22:24` | `cowrie.client.version` |
| `2026-06-28 20:22:24` | `cowrie.client.kex` |
| `2026-06-28 20:22:24` | `cowrie.login.success` |
| `2026-06-28 20:22:25` | `cowrie.session.params` |
| `2026-06-28 20:22:25` | `cowrie.command.input` |
| `2026-06-28 20:22:25` | `cowrie.log.closed` |
| `2026-06-28 20:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf894c97b7ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:23 |
| **Last Seen** | 2026-06-28 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:23:14` | `cowrie.session.connect` |
| `2026-06-28 20:23:14` | `cowrie.client.version` |
| `2026-06-28 20:23:14` | `cowrie.client.kex` |
| `2026-06-28 20:23:15` | `cowrie.login.success` |
| `2026-06-28 20:23:15` | `cowrie.session.params` |
| `2026-06-28 20:23:15` | `cowrie.command.input` |
| `2026-06-28 20:23:16` | `cowrie.log.closed` |
| `2026-06-28 20:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed4553ba576

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 20:23 |
| **Last Seen** | 2026-06-28 20:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:23:48` | `cowrie.session.connect` |
| `2026-06-28 20:23:48` | `cowrie.client.version` |
| `2026-06-28 20:23:48` | `cowrie.client.kex` |
| `2026-06-28 20:23:50` | `cowrie.login.success` |
| `2026-06-28 20:23:51` | `cowrie.session.params` |
| `2026-06-28 20:23:51` | `cowrie.command.input` |
| `2026-06-28 20:23:52` | `cowrie.log.closed` |
| `2026-06-28 20:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3334f86c4ac

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 20:24 |
| **Last Seen** | 2026-06-28 20:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:24:04` | `cowrie.session.connect` |
| `2026-06-28 20:24:06` | `cowrie.client.version` |
| `2026-06-28 20:24:06` | `cowrie.client.kex` |
| `2026-06-28 20:24:11` | `cowrie.login.success` |
| `2026-06-28 20:24:14` | `cowrie.session.params` |
| `2026-06-28 20:24:14` | `cowrie.command.input` |
| `2026-06-28 20:24:15` | `cowrie.log.closed` |
| `2026-06-28 20:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bba297b5496

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:24 |
| **Last Seen** | 2026-06-28 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:24:04` | `cowrie.session.connect` |
| `2026-06-28 20:24:04` | `cowrie.client.version` |
| `2026-06-28 20:24:05` | `cowrie.client.kex` |
| `2026-06-28 20:24:05` | `cowrie.login.success` |
| `2026-06-28 20:24:06` | `cowrie.session.params` |
| `2026-06-28 20:24:06` | `cowrie.command.input` |
| `2026-06-28 20:24:06` | `cowrie.log.closed` |
| `2026-06-28 20:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2e115dbb2e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:24 |
| **Last Seen** | 2026-06-28 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:24:57` | `cowrie.session.connect` |
| `2026-06-28 20:24:57` | `cowrie.client.version` |
| `2026-06-28 20:24:57` | `cowrie.client.kex` |
| `2026-06-28 20:24:57` | `cowrie.login.success` |
| `2026-06-28 20:24:58` | `cowrie.session.params` |
| `2026-06-28 20:24:58` | `cowrie.command.input` |
| `2026-06-28 20:24:58` | `cowrie.log.closed` |
| `2026-06-28 20:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd21100b7870

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:25 |
| **Last Seen** | 2026-06-28 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:25:46` | `cowrie.session.connect` |
| `2026-06-28 20:25:46` | `cowrie.client.version` |
| `2026-06-28 20:25:46` | `cowrie.client.kex` |
| `2026-06-28 20:25:47` | `cowrie.login.success` |
| `2026-06-28 20:25:47` | `cowrie.session.params` |
| `2026-06-28 20:25:47` | `cowrie.command.input` |
| `2026-06-28 20:25:48` | `cowrie.log.closed` |
| `2026-06-28 20:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0715ce48b40c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:26 |
| **Last Seen** | 2026-06-28 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:26:34` | `cowrie.session.connect` |
| `2026-06-28 20:26:34` | `cowrie.client.version` |
| `2026-06-28 20:26:34` | `cowrie.client.kex` |
| `2026-06-28 20:26:34` | `cowrie.login.success` |
| `2026-06-28 20:26:35` | `cowrie.session.params` |
| `2026-06-28 20:26:35` | `cowrie.command.input` |
| `2026-06-28 20:26:35` | `cowrie.log.closed` |
| `2026-06-28 20:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83317cb6391a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:27 |
| **Last Seen** | 2026-06-28 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:27:21` | `cowrie.session.connect` |
| `2026-06-28 20:27:21` | `cowrie.client.version` |
| `2026-06-28 20:27:21` | `cowrie.client.kex` |
| `2026-06-28 20:27:22` | `cowrie.login.success` |
| `2026-06-28 20:27:22` | `cowrie.session.params` |
| `2026-06-28 20:27:22` | `cowrie.command.input` |
| `2026-06-28 20:27:23` | `cowrie.log.closed` |
| `2026-06-28 20:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0acb323db94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:28 |
| **Last Seen** | 2026-06-28 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:28:09` | `cowrie.session.connect` |
| `2026-06-28 20:28:09` | `cowrie.client.version` |
| `2026-06-28 20:28:09` | `cowrie.client.kex` |
| `2026-06-28 20:28:09` | `cowrie.login.success` |
| `2026-06-28 20:28:10` | `cowrie.session.params` |
| `2026-06-28 20:28:10` | `cowrie.command.input` |
| `2026-06-28 20:28:10` | `cowrie.log.closed` |
| `2026-06-28 20:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc46688b681

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:28 |
| **Last Seen** | 2026-06-28 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:28:57` | `cowrie.session.connect` |
| `2026-06-28 20:28:57` | `cowrie.client.version` |
| `2026-06-28 20:28:57` | `cowrie.client.kex` |
| `2026-06-28 20:28:57` | `cowrie.login.success` |
| `2026-06-28 20:28:58` | `cowrie.session.params` |
| `2026-06-28 20:28:58` | `cowrie.command.input` |
| `2026-06-28 20:28:58` | `cowrie.log.closed` |
| `2026-06-28 20:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2582faaed201

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:29 |
| **Last Seen** | 2026-06-28 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:29:44` | `cowrie.session.connect` |
| `2026-06-28 20:29:44` | `cowrie.client.version` |
| `2026-06-28 20:29:44` | `cowrie.client.kex` |
| `2026-06-28 20:29:45` | `cowrie.login.success` |
| `2026-06-28 20:29:45` | `cowrie.session.params` |
| `2026-06-28 20:29:45` | `cowrie.command.input` |
| `2026-06-28 20:29:45` | `cowrie.log.closed` |
| `2026-06-28 20:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d43cd4ceadd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:30 |
| **Last Seen** | 2026-06-28 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:30:32` | `cowrie.session.connect` |
| `2026-06-28 20:30:32` | `cowrie.client.version` |
| `2026-06-28 20:30:32` | `cowrie.client.kex` |
| `2026-06-28 20:30:33` | `cowrie.login.success` |
| `2026-06-28 20:30:33` | `cowrie.session.params` |
| `2026-06-28 20:30:33` | `cowrie.command.input` |
| `2026-06-28 20:30:34` | `cowrie.log.closed` |
| `2026-06-28 20:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2aca76c0b97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:31 |
| **Last Seen** | 2026-06-28 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:31:21` | `cowrie.session.connect` |
| `2026-06-28 20:31:21` | `cowrie.client.version` |
| `2026-06-28 20:31:21` | `cowrie.client.kex` |
| `2026-06-28 20:31:21` | `cowrie.login.success` |
| `2026-06-28 20:31:22` | `cowrie.session.params` |
| `2026-06-28 20:31:22` | `cowrie.command.input` |
| `2026-06-28 20:31:22` | `cowrie.log.closed` |
| `2026-06-28 20:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206a4274903a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:32 |
| **Last Seen** | 2026-06-28 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:32:08` | `cowrie.session.connect` |
| `2026-06-28 20:32:08` | `cowrie.client.version` |
| `2026-06-28 20:32:08` | `cowrie.client.kex` |
| `2026-06-28 20:32:09` | `cowrie.login.success` |
| `2026-06-28 20:32:10` | `cowrie.session.params` |
| `2026-06-28 20:32:10` | `cowrie.command.input` |
| `2026-06-28 20:32:10` | `cowrie.log.closed` |
| `2026-06-28 20:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea8dde6120d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:32 |
| **Last Seen** | 2026-06-28 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:32:55` | `cowrie.session.connect` |
| `2026-06-28 20:32:55` | `cowrie.client.version` |
| `2026-06-28 20:32:55` | `cowrie.client.kex` |
| `2026-06-28 20:32:55` | `cowrie.login.success` |
| `2026-06-28 20:32:56` | `cowrie.session.params` |
| `2026-06-28 20:32:56` | `cowrie.command.input` |
| `2026-06-28 20:32:56` | `cowrie.log.closed` |
| `2026-06-28 20:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a6136901d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:33 |
| **Last Seen** | 2026-06-28 20:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:33:42` | `cowrie.session.connect` |
| `2026-06-28 20:33:42` | `cowrie.client.version` |
| `2026-06-28 20:33:42` | `cowrie.client.kex` |
| `2026-06-28 20:33:43` | `cowrie.login.success` |
| `2026-06-28 20:33:45` | `cowrie.session.params` |
| `2026-06-28 20:33:45` | `cowrie.command.input` |
| `2026-06-28 20:33:46` | `cowrie.log.closed` |
| `2026-06-28 20:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9cf052a458

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:34 |
| **Last Seen** | 2026-06-28 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:34:32` | `cowrie.session.connect` |
| `2026-06-28 20:34:32` | `cowrie.client.version` |
| `2026-06-28 20:34:33` | `cowrie.client.kex` |
| `2026-06-28 20:34:33` | `cowrie.login.success` |
| `2026-06-28 20:34:34` | `cowrie.session.params` |
| `2026-06-28 20:34:34` | `cowrie.command.input` |
| `2026-06-28 20:34:34` | `cowrie.log.closed` |
| `2026-06-28 20:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b505fa22b0f9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 20:35 |
| **Last Seen** | 2026-06-28 20:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:35:15` | `cowrie.session.connect` |
| `2026-06-28 20:35:17` | `cowrie.client.version` |
| `2026-06-28 20:35:17` | `cowrie.client.kex` |
| `2026-06-28 20:35:23` | `cowrie.login.success` |
| `2026-06-28 20:35:26` | `cowrie.session.params` |
| `2026-06-28 20:35:26` | `cowrie.command.input` |
| `2026-06-28 20:35:27` | `cowrie.log.closed` |
| `2026-06-28 20:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dfa05975d41

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:35 |
| **Last Seen** | 2026-06-28 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:35:20` | `cowrie.session.connect` |
| `2026-06-28 20:35:20` | `cowrie.client.version` |
| `2026-06-28 20:35:20` | `cowrie.client.kex` |
| `2026-06-28 20:35:21` | `cowrie.login.success` |
| `2026-06-28 20:35:21` | `cowrie.session.params` |
| `2026-06-28 20:35:21` | `cowrie.command.input` |
| `2026-06-28 20:35:21` | `cowrie.log.closed` |
| `2026-06-28 20:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844b49cb33ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:36 |
| **Last Seen** | 2026-06-28 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:36:08` | `cowrie.session.connect` |
| `2026-06-28 20:36:08` | `cowrie.client.version` |
| `2026-06-28 20:36:08` | `cowrie.client.kex` |
| `2026-06-28 20:36:08` | `cowrie.login.success` |
| `2026-06-28 20:36:09` | `cowrie.session.params` |
| `2026-06-28 20:36:09` | `cowrie.command.input` |
| `2026-06-28 20:36:09` | `cowrie.log.closed` |
| `2026-06-28 20:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dcfeb334e5e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:36 |
| **Last Seen** | 2026-06-28 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:36:56` | `cowrie.session.connect` |
| `2026-06-28 20:36:56` | `cowrie.client.version` |
| `2026-06-28 20:36:56` | `cowrie.client.kex` |
| `2026-06-28 20:36:57` | `cowrie.login.success` |
| `2026-06-28 20:36:57` | `cowrie.session.params` |
| `2026-06-28 20:36:57` | `cowrie.command.input` |
| `2026-06-28 20:36:58` | `cowrie.log.closed` |
| `2026-06-28 20:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63422126943c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:37 |
| **Last Seen** | 2026-06-28 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:37:44` | `cowrie.session.connect` |
| `2026-06-28 20:37:44` | `cowrie.client.version` |
| `2026-06-28 20:37:44` | `cowrie.client.kex` |
| `2026-06-28 20:37:45` | `cowrie.login.success` |
| `2026-06-28 20:37:46` | `cowrie.session.params` |
| `2026-06-28 20:37:46` | `cowrie.command.input` |
| `2026-06-28 20:37:46` | `cowrie.log.closed` |
| `2026-06-28 20:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587f73c4f0f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:38 |
| **Last Seen** | 2026-06-28 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:38:31` | `cowrie.session.connect` |
| `2026-06-28 20:38:31` | `cowrie.client.version` |
| `2026-06-28 20:38:32` | `cowrie.client.kex` |
| `2026-06-28 20:38:32` | `cowrie.login.success` |
| `2026-06-28 20:38:33` | `cowrie.session.params` |
| `2026-06-28 20:38:33` | `cowrie.command.input` |
| `2026-06-28 20:38:33` | `cowrie.log.closed` |
| `2026-06-28 20:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3565a5bf0f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 20:38 |
| **Last Seen** | 2026-06-28 20:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:38:35` | `cowrie.session.connect` |
| `2026-06-28 20:38:35` | `cowrie.client.version` |
| `2026-06-28 20:38:35` | `cowrie.client.kex` |
| `2026-06-28 20:38:38` | `cowrie.login.success` |
| `2026-06-28 20:38:39` | `cowrie.session.params` |
| `2026-06-28 20:38:39` | `cowrie.command.input` |
| `2026-06-28 20:38:40` | `cowrie.log.closed` |
| `2026-06-28 20:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb950865efc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:39 |
| **Last Seen** | 2026-06-28 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:39:18` | `cowrie.session.connect` |
| `2026-06-28 20:39:18` | `cowrie.client.version` |
| `2026-06-28 20:39:18` | `cowrie.client.kex` |
| `2026-06-28 20:39:18` | `cowrie.login.success` |
| `2026-06-28 20:39:19` | `cowrie.session.params` |
| `2026-06-28 20:39:19` | `cowrie.command.input` |
| `2026-06-28 20:39:19` | `cowrie.log.closed` |
| `2026-06-28 20:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0066e69ba2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:40 |
| **Last Seen** | 2026-06-28 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:40:04` | `cowrie.session.connect` |
| `2026-06-28 20:40:04` | `cowrie.client.version` |
| `2026-06-28 20:40:04` | `cowrie.client.kex` |
| `2026-06-28 20:40:05` | `cowrie.login.success` |
| `2026-06-28 20:40:05` | `cowrie.session.params` |
| `2026-06-28 20:40:05` | `cowrie.command.input` |
| `2026-06-28 20:40:06` | `cowrie.log.closed` |
| `2026-06-28 20:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c16f10cd736

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:40 |
| **Last Seen** | 2026-06-28 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:40:51` | `cowrie.session.connect` |
| `2026-06-28 20:40:51` | `cowrie.client.version` |
| `2026-06-28 20:40:51` | `cowrie.client.kex` |
| `2026-06-28 20:40:51` | `cowrie.login.success` |
| `2026-06-28 20:40:52` | `cowrie.session.params` |
| `2026-06-28 20:40:52` | `cowrie.command.input` |
| `2026-06-28 20:40:52` | `cowrie.log.closed` |
| `2026-06-28 20:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978cc8d1ea6d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:41 |
| **Last Seen** | 2026-06-28 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:41:38` | `cowrie.session.connect` |
| `2026-06-28 20:41:38` | `cowrie.client.version` |
| `2026-06-28 20:41:38` | `cowrie.client.kex` |
| `2026-06-28 20:41:39` | `cowrie.login.success` |
| `2026-06-28 20:41:40` | `cowrie.session.params` |
| `2026-06-28 20:41:40` | `cowrie.command.input` |
| `2026-06-28 20:41:40` | `cowrie.log.closed` |
| `2026-06-28 20:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41969ef58dea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:42 |
| **Last Seen** | 2026-06-28 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:42:26` | `cowrie.session.connect` |
| `2026-06-28 20:42:26` | `cowrie.client.version` |
| `2026-06-28 20:42:26` | `cowrie.client.kex` |
| `2026-06-28 20:42:27` | `cowrie.login.success` |
| `2026-06-28 20:42:27` | `cowrie.session.params` |
| `2026-06-28 20:42:27` | `cowrie.command.input` |
| `2026-06-28 20:42:28` | `cowrie.log.closed` |
| `2026-06-28 20:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f40596a4083f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:43 |
| **Last Seen** | 2026-06-28 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:43:15` | `cowrie.session.connect` |
| `2026-06-28 20:43:15` | `cowrie.client.version` |
| `2026-06-28 20:43:15` | `cowrie.client.kex` |
| `2026-06-28 20:43:15` | `cowrie.login.success` |
| `2026-06-28 20:43:16` | `cowrie.session.params` |
| `2026-06-28 20:43:16` | `cowrie.command.input` |
| `2026-06-28 20:43:16` | `cowrie.log.closed` |
| `2026-06-28 20:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39382a94983e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:44 |
| **Last Seen** | 2026-06-28 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:44:04` | `cowrie.session.connect` |
| `2026-06-28 20:44:04` | `cowrie.client.version` |
| `2026-06-28 20:44:04` | `cowrie.client.kex` |
| `2026-06-28 20:44:04` | `cowrie.login.success` |
| `2026-06-28 20:44:05` | `cowrie.session.params` |
| `2026-06-28 20:44:05` | `cowrie.command.input` |
| `2026-06-28 20:44:05` | `cowrie.log.closed` |
| `2026-06-28 20:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915674251447

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:44 |
| **Last Seen** | 2026-06-28 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:44:52` | `cowrie.session.connect` |
| `2026-06-28 20:44:52` | `cowrie.client.version` |
| `2026-06-28 20:44:52` | `cowrie.client.kex` |
| `2026-06-28 20:44:53` | `cowrie.login.success` |
| `2026-06-28 20:44:53` | `cowrie.session.params` |
| `2026-06-28 20:44:53` | `cowrie.command.input` |
| `2026-06-28 20:44:53` | `cowrie.log.closed` |
| `2026-06-28 20:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f64b0625b7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:45 |
| **Last Seen** | 2026-06-28 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:45:40` | `cowrie.session.connect` |
| `2026-06-28 20:45:40` | `cowrie.client.version` |
| `2026-06-28 20:45:41` | `cowrie.client.kex` |
| `2026-06-28 20:45:41` | `cowrie.login.success` |
| `2026-06-28 20:45:42` | `cowrie.session.params` |
| `2026-06-28 20:45:42` | `cowrie.command.input` |
| `2026-06-28 20:45:42` | `cowrie.log.closed` |
| `2026-06-28 20:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07745cb488ab

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 20:46 |
| **Last Seen** | 2026-06-28 20:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:46:21` | `cowrie.session.connect` |
| `2026-06-28 20:46:22` | `cowrie.client.version` |
| `2026-06-28 20:46:22` | `cowrie.client.kex` |
| `2026-06-28 20:46:28` | `cowrie.login.success` |
| `2026-06-28 20:46:31` | `cowrie.session.params` |
| `2026-06-28 20:46:31` | `cowrie.command.input` |
| `2026-06-28 20:46:34` | `cowrie.log.closed` |
| `2026-06-28 20:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43557561fd00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:46 |
| **Last Seen** | 2026-06-28 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:46:28` | `cowrie.session.connect` |
| `2026-06-28 20:46:28` | `cowrie.client.version` |
| `2026-06-28 20:46:28` | `cowrie.client.kex` |
| `2026-06-28 20:46:29` | `cowrie.login.success` |
| `2026-06-28 20:46:29` | `cowrie.session.params` |
| `2026-06-28 20:46:29` | `cowrie.command.input` |
| `2026-06-28 20:46:29` | `cowrie.log.closed` |
| `2026-06-28 20:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf1879e371b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:47 |
| **Last Seen** | 2026-06-28 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:47:17` | `cowrie.session.connect` |
| `2026-06-28 20:47:17` | `cowrie.client.version` |
| `2026-06-28 20:47:17` | `cowrie.client.kex` |
| `2026-06-28 20:47:18` | `cowrie.login.success` |
| `2026-06-28 20:47:19` | `cowrie.session.params` |
| `2026-06-28 20:47:19` | `cowrie.command.input` |
| `2026-06-28 20:47:19` | `cowrie.log.closed` |
| `2026-06-28 20:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c710efad5d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:48 |
| **Last Seen** | 2026-06-28 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:48:08` | `cowrie.session.connect` |
| `2026-06-28 20:48:08` | `cowrie.client.version` |
| `2026-06-28 20:48:08` | `cowrie.client.kex` |
| `2026-06-28 20:48:09` | `cowrie.login.success` |
| `2026-06-28 20:48:09` | `cowrie.session.params` |
| `2026-06-28 20:48:09` | `cowrie.command.input` |
| `2026-06-28 20:48:09` | `cowrie.log.closed` |
| `2026-06-28 20:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e20b12fbdf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:49 |
| **Last Seen** | 2026-06-28 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:49:00` | `cowrie.session.connect` |
| `2026-06-28 20:49:00` | `cowrie.client.version` |
| `2026-06-28 20:49:00` | `cowrie.client.kex` |
| `2026-06-28 20:49:00` | `cowrie.login.success` |
| `2026-06-28 20:49:01` | `cowrie.session.params` |
| `2026-06-28 20:49:01` | `cowrie.command.input` |
| `2026-06-28 20:49:01` | `cowrie.log.closed` |
| `2026-06-28 20:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85310c97609d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:49 |
| **Last Seen** | 2026-06-28 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:49:52` | `cowrie.session.connect` |
| `2026-06-28 20:49:52` | `cowrie.client.version` |
| `2026-06-28 20:49:52` | `cowrie.client.kex` |
| `2026-06-28 20:49:52` | `cowrie.login.success` |
| `2026-06-28 20:49:53` | `cowrie.session.params` |
| `2026-06-28 20:49:53` | `cowrie.command.input` |
| `2026-06-28 20:49:53` | `cowrie.log.closed` |
| `2026-06-28 20:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a492647d0ef0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:50 |
| **Last Seen** | 2026-06-28 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:50:43` | `cowrie.session.connect` |
| `2026-06-28 20:50:43` | `cowrie.client.version` |
| `2026-06-28 20:50:43` | `cowrie.client.kex` |
| `2026-06-28 20:50:44` | `cowrie.login.success` |
| `2026-06-28 20:50:44` | `cowrie.session.params` |
| `2026-06-28 20:50:44` | `cowrie.command.input` |
| `2026-06-28 20:50:44` | `cowrie.log.closed` |
| `2026-06-28 20:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54aa467263f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:51 |
| **Last Seen** | 2026-06-28 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:51:33` | `cowrie.session.connect` |
| `2026-06-28 20:51:33` | `cowrie.client.version` |
| `2026-06-28 20:51:33` | `cowrie.client.kex` |
| `2026-06-28 20:51:34` | `cowrie.login.success` |
| `2026-06-28 20:51:35` | `cowrie.session.params` |
| `2026-06-28 20:51:35` | `cowrie.command.input` |
| `2026-06-28 20:51:35` | `cowrie.log.closed` |
| `2026-06-28 20:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3513a226844b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:52 |
| **Last Seen** | 2026-06-28 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:52:23` | `cowrie.session.connect` |
| `2026-06-28 20:52:23` | `cowrie.client.version` |
| `2026-06-28 20:52:23` | `cowrie.client.kex` |
| `2026-06-28 20:52:23` | `cowrie.login.success` |
| `2026-06-28 20:52:24` | `cowrie.session.params` |
| `2026-06-28 20:52:24` | `cowrie.command.input` |
| `2026-06-28 20:52:24` | `cowrie.log.closed` |
| `2026-06-28 20:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5702af7282e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:53 |
| **Last Seen** | 2026-06-28 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:53:12` | `cowrie.session.connect` |
| `2026-06-28 20:53:12` | `cowrie.client.version` |
| `2026-06-28 20:53:12` | `cowrie.client.kex` |
| `2026-06-28 20:53:13` | `cowrie.login.success` |
| `2026-06-28 20:53:13` | `cowrie.session.params` |
| `2026-06-28 20:53:13` | `cowrie.command.input` |
| `2026-06-28 20:53:13` | `cowrie.log.closed` |
| `2026-06-28 20:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d05184b479

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 20:53 |
| **Last Seen** | 2026-06-28 20:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:53:30` | `cowrie.session.connect` |
| `2026-06-28 20:53:30` | `cowrie.client.version` |
| `2026-06-28 20:53:30` | `cowrie.client.kex` |
| `2026-06-28 20:53:32` | `cowrie.login.success` |
| `2026-06-28 20:53:34` | `cowrie.session.params` |
| `2026-06-28 20:53:34` | `cowrie.command.input` |
| `2026-06-28 20:53:34` | `cowrie.log.closed` |
| `2026-06-28 20:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46fd840eacd4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:54 |
| **Last Seen** | 2026-06-28 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:54:02` | `cowrie.session.connect` |
| `2026-06-28 20:54:02` | `cowrie.client.version` |
| `2026-06-28 20:54:02` | `cowrie.client.kex` |
| `2026-06-28 20:54:02` | `cowrie.login.success` |
| `2026-06-28 20:54:03` | `cowrie.session.params` |
| `2026-06-28 20:54:03` | `cowrie.command.input` |
| `2026-06-28 20:54:03` | `cowrie.log.closed` |
| `2026-06-28 20:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30720415333

| Field | Detail |
|---|---|
| **Source IP** | `8.221.121[.]6` |
| **First Seen** | 2026-06-28 20:54 |
| **Last Seen** | 2026-06-28 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:54:21` | `cowrie.session.connect` |
| `2026-06-28 20:54:21` | `cowrie.client.version` |
| `2026-06-28 20:54:21` | `cowrie.client.kex` |
| `2026-06-28 20:54:21` | `cowrie.login.success` |
| `2026-06-28 20:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.221.121[.]6` to AbuseIPDB if not already reported
- [ ] Block `8.221.121[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3942d8d88c6

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-28 20:54 |
| **Last Seen** | 2026-06-28 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:54:22` | `cowrie.session.connect` |
| `2026-06-28 20:54:22` | `cowrie.client.version` |
| `2026-06-28 20:54:22` | `cowrie.client.kex` |
| `2026-06-28 20:54:22` | `cowrie.login.success` |
| `2026-06-28 20:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7b6da30397

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 20:54 |
| **Last Seen** | 2026-06-28 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 20:54:52` | `cowrie.session.connect` |
| `2026-06-28 20:54:52` | `cowrie.client.version` |
| `2026-06-28 20:54:52` | `cowrie.client.kex` |
| `2026-06-28 20:54:52` | `cowrie.login.success` |
| `2026-06-28 20:54:53` | `cowrie.session.params` |
| `2026-06-28 20:54:53` | `cowrie.command.input` |
| `2026-06-28 20:54:53` | `cowrie.log.closed` |
| `2026-06-28 20:54:53` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **132** | 2026-06-28 18:55 | 2026-06-28 20:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **2** | 2026-06-28 19:10 | 2026-06-28 19:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `39.152.240[.]15` | 1 | 2026-06-28 18:56 | 2026-06-28 18:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-28 19:05 | 2026-06-28 19:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-06-28 19:34 | 2026-06-28 19:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]198` | 1 | 2026-06-28 20:38 | 2026-06-28 20:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | 1 | 2026-06-28 20:06 | 2026-06-28 20:06 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `66.132.186[.]198` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `195.178.110[.]217` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 18 |
| `91.92.40[.]90` | NL | TechTies Inc. | **100** ⚠️ | 12 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 50 |
| `39.152.240[.]15` | CN | China Mobile Communications Corporation | **100** ⚠️ | 22 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `45.148.10[.]239` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 38 |
| `45.148.10[.]151` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 169 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 160 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 308 cases |
| Tool 34  | Credential Extractor        | ✅ 161 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (2.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 160 priority case(s) shown individually · 7 recon entry/entries in table (2 group(s) consolidating 134 session(s)).

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
_Report time: 2026-06-28T21:06:42Z_

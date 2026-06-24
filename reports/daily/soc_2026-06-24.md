# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-24 |
| **Generated At** | 2026-06-24T10:55:38Z |
| **Shift Time** | 10:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **348** |
| Confirmed Threats | **341** |
| False Positives Filtered | **7** (2.0%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **8** |
| High Severity Cases | **158** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **190** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **159** |
| Unique Credential Pairs | **153** |
| Unique Usernames | **94** |
| Unique Passwords | **133** |
| Successful Auth Pairs | **156** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `ubuntu` | 11 |
| `admin` | 7 |
| `pi` | 4 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 12 |
| `admin` | 4 |
| `1234` | 3 |
| `1` | 3 |
| `passpass` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 4 |
| `pi` | `raspberryraspberry993311` | 2 |
| `pi` | `raspberry` | 2 |
| `root` | `---fuck_you----` | 2 |
| `ubuntu` | `q1w2e` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `q1w2e` | `45.205.1.42` | 2026-06-24T06:55:07 |
| `root` | `muie123` | `209.99.185.59` | 2026-06-24T06:55:36 |
| `xtrus` | `xtrus` | `209.99.185.59` | 2026-06-24T06:56:30 |
| `xdyang` | `xdyang` | `209.99.185.59` | 2026-06-24T06:57:24 |
| `xuchi` | `xuchi` | `209.99.185.59` | 2026-06-24T06:58:15 |
| `root` | `Password!@#456` | `209.99.185.59` | 2026-06-24T06:59:05 |
| `root` | `hahaha` | `209.99.185.59` | 2026-06-24T06:59:57 |
| `hadoop` | `654321` | `209.99.185.59` | 2026-06-24T07:00:49 |
| `yangxh` | `yangxinhao` | `209.99.185.59` | 2026-06-24T07:01:45 |
| `server` | `passpass` | `209.99.185.59` | 2026-06-24T07:02:37 |
| `pix` | `cisco` | `209.99.185.59` | 2026-06-24T07:03:30 |
| `ubuntu` | `qwerty77` | `209.99.185.59` | 2026-06-24T07:04:22 |
| `root` | `linod3.com` | `209.99.185.59` | 2026-06-24T07:05:15 |
| `user` | `q1w2e3` | `209.99.185.59` | 2026-06-24T07:06:05 |
| `huangxy` | `huangxy` | `209.99.185.59` | 2026-06-24T07:06:56 |
| `sjkim` | `sjkim` | `209.99.185.59` | 2026-06-24T07:07:47 |
| `zhangxh` | `zhangxh` | `209.99.185.59` | 2026-06-24T07:08:40 |
| `testuser` | `testuser123` | `45.205.1.42` | 2026-06-24T07:09:32 |
| `fangchao` | `123456` | `209.99.185.59` | 2026-06-24T07:09:34 |
| `xyy` | `xyy` | `209.99.185.59` | 2026-06-24T07:10:28 |
| `pi` | `raspberryraspberry993311` | `111.77.115.116` | 2026-06-24T07:10:43 |
| `pi` | `raspberry` | `111.77.115.116` | 2026-06-24T07:10:43 |
| `root` | `qwaszx!@#` | `209.99.185.59` | 2026-06-24T07:11:21 |
| `visitor` | `visitor` | `209.99.185.59` | 2026-06-24T07:12:14 |
| `dusq` | `123456` | `209.99.185.59` | 2026-06-24T07:13:07 |
| `deploy` | `123456` | `209.99.185.59` | 2026-06-24T07:14:05 |
| `ubuntu` | `developer` | `209.99.185.59` | 2026-06-24T07:15:00 |
| `market` | `123456` | `209.99.185.59` | 2026-06-24T07:15:55 |
| `ubuntu` | `Pa22w0rd` | `209.99.185.59` | 2026-06-24T07:16:49 |
| `service` | `123plm123` | `209.99.185.59` | 2026-06-24T07:17:42 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-24T07:17:59 |
| `qhp` | `a236339.0` | `209.99.185.59` | 2026-06-24T07:18:35 |
| `root` | `0p9o8i7u6y5t4r3e2w` | `209.99.185.59` | 2026-06-24T07:19:28 |
| `wht` | `wht123` | `209.99.185.59` | 2026-06-24T07:20:22 |
| `es` | `es` | `209.99.185.59` | 2026-06-24T07:21:16 |
| `root` | `sysadmin` | `209.99.185.59` | 2026-06-24T07:22:13 |
| `ubuntu` | `abcd@1234` | `209.99.185.59` | 2026-06-24T07:23:08 |
| `dustin` | `dustin` | `45.205.1.42` | 2026-06-24T07:23:57 |
| `datacenter` | `password` | `209.99.185.59` | 2026-06-24T07:24:02 |
| `ubuntu` | `Parasol1` | `209.99.185.59` | 2026-06-24T07:24:55 |
| `root` | `131313` | `209.99.185.59` | 2026-06-24T07:25:49 |
| `ubuntu` | `QWEQWE!@#!@#` | `209.99.185.59` | 2026-06-24T07:26:44 |
| `jcpark` | `jcpark` | `209.99.185.59` | 2026-06-24T07:27:43 |
| `root` | `Ypfamily@123` | `209.99.185.59` | 2026-06-24T07:28:40 |
| `dell` | `123456789` | `209.99.185.59` | 2026-06-24T07:29:37 |
| `root` | `abc123!@` | `209.99.185.59` | 2026-06-24T07:30:32 |
| `admin` | `blackinclub!@#123` | `209.99.185.59` | 2026-06-24T07:31:26 |
| `sjw` | `sjw` | `209.99.185.59` | 2026-06-24T07:32:25 |
| `debian` | `123qwe` | `209.99.185.59` | 2026-06-24T07:33:21 |
| `ubuntu` | `asd1234` | `209.99.185.59` | 2026-06-24T07:34:17 |
| `john` | `john123` | `209.99.185.59` | 2026-06-24T07:35:15 |
| `wangzh` | `RenXinNanCe9816` | `209.99.185.59` | 2026-06-24T07:36:12 |
| `admin1` | `333333` | `209.99.185.59` | 2026-06-24T07:37:07 |
| `root` | `QAZ@1231qwe` | `209.99.185.59` | 2026-06-24T07:38:02 |
| `admin` | `Admin123` | `45.205.1.42` | 2026-06-24T07:38:07 |
| `root` | `admin@4444` | `209.99.185.59` | 2026-06-24T07:38:57 |
| `edgar` | `edgar` | `209.99.185.59` | 2026-06-24T07:39:54 |
| `liyue` | `asdf1234` | `209.99.185.59` | 2026-06-24T07:40:52 |
| `test` | `222222` | `209.99.185.59` | 2026-06-24T07:41:50 |
| `datacenter` | `1234567` | `209.99.185.59` | 2026-06-24T07:42:47 |
| `sg` | `korea2011` | `209.99.185.59` | 2026-06-24T07:43:43 |
| `hsi` | `hsi` | `209.99.185.59` | 2026-06-24T07:44:38 |
| `postgres` | `postgres123!@#` | `209.99.185.59` | 2026-06-24T07:45:35 |
| `root` | `Welcome123!` | `209.99.185.59` | 2026-06-24T07:46:31 |
| `root` | `hy123456` | `209.99.185.59` | 2026-06-24T07:47:27 |
| `admin` | `admin` | `185.65.202.199` | 2026-06-24T07:48:00 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-24T07:48:01 |
| `weiyuxuan` | `o443W586A2` | `209.99.185.59` | 2026-06-24T07:48:26 |
| `root` | `supervisor` | `209.99.185.59` | 2026-06-24T07:49:22 |
| `ubuntu1` | `123456` | `209.99.185.59` | 2026-06-24T07:50:18 |
| `root` | `ubuntu12` | `209.99.185.59` | 2026-06-24T07:51:14 |
| `root` | `robert` | `209.99.185.59` | 2026-06-24T07:52:11 |
| `root` | `Os3leni*` | `45.205.1.42` | 2026-06-24T07:52:30 |
| `omp` | `omp` | `209.99.185.59` | 2026-06-24T07:53:09 |
| `tempo` | `tempo` | `209.99.185.59` | 2026-06-24T07:54:10 |
| `ds` | `ds` | `209.99.185.59` | 2026-06-24T07:55:12 |
| `xiaxq` | `xtHcfelwNV` | `209.99.185.59` | 2026-06-24T07:56:12 |
| `git` | `1q2w3e4r` | `209.99.185.59` | 2026-06-24T07:57:09 |
| `admin` | `qwe123` | `209.99.185.59` | 2026-06-24T07:58:05 |
| `root` | `server$321!+` | `209.99.185.59` | 2026-06-24T07:59:05 |
| `openbravo` | `123456` | `209.99.185.59` | 2026-06-24T08:00:05 |
| `admin` | `admin` | `43.110.37.217` | 2026-06-24T08:00:36 |
| `student5` | `123456` | `209.99.185.59` | 2026-06-24T08:00:55 |
| `thy` | `thy` | `209.99.185.59` | 2026-06-24T08:01:45 |
| `zjz` | `zjz123` | `209.99.185.59` | 2026-06-24T08:02:30 |
| `zxx` | `zxx` | `209.99.185.59` | 2026-06-24T08:03:15 |
| `navidad` | `navidad` | `209.99.185.59` | 2026-06-24T08:04:00 |
| `login01` | `login01` | `209.99.185.59` | 2026-06-24T08:04:47 |
| `downloader` | `123456` | `209.99.185.59` | 2026-06-24T08:05:33 |
| `root` | `qWeRtYuIoP` | `209.99.185.59` | 2026-06-24T08:06:21 |
| `root` | `1234` | `45.205.1.42` | 2026-06-24T08:06:53 |
| `vyatta` | `vyatta` | `209.99.185.59` | 2026-06-24T08:07:07 |
| `root` | `test123` | `209.99.185.59` | 2026-06-24T08:07:55 |
| `root` | `admin999` | `209.99.185.59` | 2026-06-24T08:08:44 |
| `root` | `QAZ1231qaz!` | `209.99.185.59` | 2026-06-24T08:09:29 |
| `root` | `test0` | `209.99.185.59` | 2026-06-24T08:10:13 |
| `wpyan` | `test321` | `209.99.185.59` | 2026-06-24T08:10:59 |
| `dongzi` | `159357` | `209.99.185.59` | 2026-06-24T08:11:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.199.1.98` | 2026-06-24T08:11:44 |
| `*1` | `$4` | `104.199.1.98` | 2026-06-24T08:11:53 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 936` | `104.199.1.98` | 2026-06-24T08:11:55 |
| `root` | `163.com` | `209.99.185.59` | 2026-06-24T08:12:31 |
| `grid` | `grid` | `209.99.185.59` | 2026-06-24T08:13:24 |
| `wpyan` | `qwerty123` | `209.99.185.59` | 2026-06-24T08:14:14 |
| `root` | `163.2019` | `209.99.185.59` | 2026-06-24T08:15:01 |
| `student7` | `123456` | `209.99.185.59` | 2026-06-24T08:15:48 |
| `rzzhang` | `221333` | `209.99.185.59` | 2026-06-24T08:16:34 |
| `cow` | `cow123!` | `209.99.185.59` | 2026-06-24T08:17:22 |
| `longpengpeng` | `123456` | `209.99.185.59` | 2026-06-24T08:18:10 |
| `chenyuce` | `chenyuce` | `209.99.185.59` | 2026-06-24T08:18:59 |
| `ubuntu` | `selfrep192` | `209.99.185.59` | 2026-06-24T08:19:49 |
| `junwen` | `junwen` | `209.99.185.59` | 2026-06-24T08:20:42 |
| `root` | `adminHW` | `45.205.1.42` | 2026-06-24T08:21:06 |
| `root` | `trustno1` | `209.99.185.59` | 2026-06-24T08:21:29 |
| `mirza2` | `ouyang123` | `209.99.185.59` | 2026-06-24T08:22:16 |
| `root` | `BB@123456` | `209.99.185.59` | 2026-06-24T08:23:03 |
| `manager` | `1` | `209.99.185.59` | 2026-06-24T08:23:53 |
| `root` | `P4$$WORD` | `209.99.185.59` | 2026-06-24T08:24:44 |
| `root` | `UNKNOWN` | `209.99.185.59` | 2026-06-24T08:25:35 |
| `root` | `---fuck_you----` | `223.197.103.19` | 2026-06-24T08:25:39 |
| `xkcao` | `123` | `209.99.185.59` | 2026-06-24T08:26:28 |
| `ubuntu` | `abcdefg` | `209.99.185.59` | 2026-06-24T08:27:20 |
| `omnisky` | `432rt654123` | `209.99.185.59` | 2026-06-24T08:28:08 |
| `adm` | `adm123` | `209.99.185.59` | 2026-06-24T08:28:55 |
| `dell` | `dell@7000` | `209.99.185.59` | 2026-06-24T08:29:44 |
| `xiangliuyu` | `123123123456` | `209.99.185.59` | 2026-06-24T08:30:37 |
| `root` | `root123` | `209.99.185.59` | 2026-06-24T08:31:29 |
| `root` | `qazw1234` | `209.99.185.59` | 2026-06-24T08:32:19 |
| `root` | `password@123` | `209.99.185.59` | 2026-06-24T08:33:08 |
| `ubuntu` | `1q2w3e4r` | `209.99.185.59` | 2026-06-24T08:33:56 |
| `rainbow` | `1234` | `209.99.185.59` | 2026-06-24T08:34:47 |
| `root` | `**********` | `45.205.1.42` | 2026-06-24T08:35:07 |
| `ceshi3` | `ceshi31234` | `209.99.185.59` | 2026-06-24T08:35:38 |
| `mail` | `qwerty` | `209.99.185.59` | 2026-06-24T08:36:26 |
| `root` | `Rainbow20.` | `209.99.185.59` | 2026-06-24T08:37:15 |
| `dev` | `123qwe` | `209.99.185.59` | 2026-06-24T08:38:04 |
| `wangyan` | `wangyan123` | `209.99.185.59` | 2026-06-24T08:38:53 |
| `zhengyabiao` | `zhengyabiao` | `209.99.185.59` | 2026-06-24T08:39:42 |
| `homepage` | `1` | `209.99.185.59` | 2026-06-24T08:40:33 |
| `test` | `test111111` | `209.99.185.59` | 2026-06-24T08:41:28 |
| `ytx` | `123456` | `209.99.185.59` | 2026-06-24T08:42:19 |
| `root` | ``1q` | `209.99.185.59` | 2026-06-24T08:43:12 |
| `ldx` | `ldx123` | `209.99.185.59` | 2026-06-24T08:44:00 |
| `dingy` | `qwe123` | `209.99.185.59` | 2026-06-24T08:44:50 |
| `ykt` | `ykt` | `209.99.185.59` | 2026-06-24T08:45:39 |
| `jung` | `1234` | `209.99.185.59` | 2026-06-24T08:46:28 |
| `mass` | `Mass@1#2$3` | `209.99.185.59` | 2026-06-24T08:47:18 |
| `jhseo` | `jhseo` | `209.99.185.59` | 2026-06-24T08:48:11 |
| `user` | `passpass` | `209.99.185.59` | 2026-06-24T08:49:05 |
| `testuser` | `123` | `45.205.1.42` | 2026-06-24T08:49:20 |
| `g` | `123456` | `209.99.185.59` | 2026-06-24T08:49:55 |
| `hx` | `linux123` | `209.99.185.59` | 2026-06-24T08:50:48 |
| `root` | `qwe123rty` | `209.99.185.59` | 2026-06-24T08:51:40 |
| `inven4` | `inven4` | `209.99.185.59` | 2026-06-24T08:52:30 |
| `csh` | `1` | `209.99.185.59` | 2026-06-24T08:53:19 |
| `gding` | `huwh` | `209.99.185.59` | 2026-06-24T08:54:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **348** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 150 |
| libssh | 9 |
| OpenSSH | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 145 | 2 |
| `46c5bd974888...` | Modern SSH client | 4 | 1 |
| `19532158b559...` | Mirai/variant | 2 | 2 |
| `5f904648ee89...` | Generic scanner | 2 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 145 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `46c5bd974888...` | OpenSSH | 4 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS215540` | GLOBAL CONNECTIVITY SOLUTIONS LLP | 1 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |
| `AS133776` | Quanzhou | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS4515` | PCCW IMS Ltd (PCCW Business Internet Access) | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (158)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8043891873cb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 06:55 |
| **Last Seen** | 2026-06-24 06:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:55:07` | `cowrie.login.success` |
| `2026-06-24 06:55:11` | `cowrie.session.params` |
| `2026-06-24 06:55:11` | `cowrie.command.input` |
| `2026-06-24 06:55:13` | `cowrie.log.closed` |
| `2026-06-24 06:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6116b20e150a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:55 |
| **Last Seen** | 2026-06-24 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:55:36` | `cowrie.session.connect` |
| `2026-06-24 06:55:36` | `cowrie.client.version` |
| `2026-06-24 06:55:36` | `cowrie.client.kex` |
| `2026-06-24 06:55:36` | `cowrie.login.success` |
| `2026-06-24 06:55:37` | `cowrie.session.params` |
| `2026-06-24 06:55:37` | `cowrie.command.input` |
| `2026-06-24 06:55:37` | `cowrie.log.closed` |
| `2026-06-24 06:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cebb71171b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:56 |
| **Last Seen** | 2026-06-24 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:56:29` | `cowrie.session.connect` |
| `2026-06-24 06:56:29` | `cowrie.client.version` |
| `2026-06-24 06:56:29` | `cowrie.client.kex` |
| `2026-06-24 06:56:30` | `cowrie.login.success` |
| `2026-06-24 06:56:31` | `cowrie.session.params` |
| `2026-06-24 06:56:31` | `cowrie.command.input` |
| `2026-06-24 06:56:31` | `cowrie.log.closed` |
| `2026-06-24 06:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c9706d8ad1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:57 |
| **Last Seen** | 2026-06-24 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:57:23` | `cowrie.session.connect` |
| `2026-06-24 06:57:23` | `cowrie.client.version` |
| `2026-06-24 06:57:23` | `cowrie.client.kex` |
| `2026-06-24 06:57:24` | `cowrie.login.success` |
| `2026-06-24 06:57:25` | `cowrie.session.params` |
| `2026-06-24 06:57:25` | `cowrie.command.input` |
| `2026-06-24 06:57:25` | `cowrie.log.closed` |
| `2026-06-24 06:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a77e15560bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:58 |
| **Last Seen** | 2026-06-24 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:58:14` | `cowrie.session.connect` |
| `2026-06-24 06:58:14` | `cowrie.client.version` |
| `2026-06-24 06:58:14` | `cowrie.client.kex` |
| `2026-06-24 06:58:15` | `cowrie.login.success` |
| `2026-06-24 06:58:15` | `cowrie.session.params` |
| `2026-06-24 06:58:15` | `cowrie.command.input` |
| `2026-06-24 06:58:16` | `cowrie.log.closed` |
| `2026-06-24 06:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa2f3e1d9e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:59 |
| **Last Seen** | 2026-06-24 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:59:04` | `cowrie.session.connect` |
| `2026-06-24 06:59:04` | `cowrie.client.version` |
| `2026-06-24 06:59:05` | `cowrie.client.kex` |
| `2026-06-24 06:59:05` | `cowrie.login.success` |
| `2026-06-24 06:59:06` | `cowrie.session.params` |
| `2026-06-24 06:59:06` | `cowrie.command.input` |
| `2026-06-24 06:59:06` | `cowrie.log.closed` |
| `2026-06-24 06:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc9f035b26d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 06:59 |
| **Last Seen** | 2026-06-24 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:59:56` | `cowrie.session.connect` |
| `2026-06-24 06:59:56` | `cowrie.client.version` |
| `2026-06-24 06:59:56` | `cowrie.client.kex` |
| `2026-06-24 06:59:57` | `cowrie.login.success` |
| `2026-06-24 06:59:57` | `cowrie.session.params` |
| `2026-06-24 06:59:57` | `cowrie.command.input` |
| `2026-06-24 06:59:57` | `cowrie.log.closed` |
| `2026-06-24 06:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e14adb281dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:00 |
| **Last Seen** | 2026-06-24 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:00:48` | `cowrie.session.connect` |
| `2026-06-24 07:00:48` | `cowrie.client.version` |
| `2026-06-24 07:00:49` | `cowrie.client.kex` |
| `2026-06-24 07:00:49` | `cowrie.login.success` |
| `2026-06-24 07:00:50` | `cowrie.session.params` |
| `2026-06-24 07:00:50` | `cowrie.command.input` |
| `2026-06-24 07:00:50` | `cowrie.log.closed` |
| `2026-06-24 07:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d19f10b2e74

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:01 |
| **Last Seen** | 2026-06-24 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:01:44` | `cowrie.session.connect` |
| `2026-06-24 07:01:44` | `cowrie.client.version` |
| `2026-06-24 07:01:44` | `cowrie.client.kex` |
| `2026-06-24 07:01:45` | `cowrie.login.success` |
| `2026-06-24 07:01:46` | `cowrie.session.params` |
| `2026-06-24 07:01:46` | `cowrie.command.input` |
| `2026-06-24 07:01:46` | `cowrie.log.closed` |
| `2026-06-24 07:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8a9c102e1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:02 |
| **Last Seen** | 2026-06-24 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:02:37` | `cowrie.session.connect` |
| `2026-06-24 07:02:37` | `cowrie.client.version` |
| `2026-06-24 07:02:37` | `cowrie.client.kex` |
| `2026-06-24 07:02:37` | `cowrie.login.success` |
| `2026-06-24 07:02:38` | `cowrie.session.params` |
| `2026-06-24 07:02:38` | `cowrie.command.input` |
| `2026-06-24 07:02:38` | `cowrie.log.closed` |
| `2026-06-24 07:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7761f7e48145

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:03 |
| **Last Seen** | 2026-06-24 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:03:30` | `cowrie.session.connect` |
| `2026-06-24 07:03:30` | `cowrie.client.version` |
| `2026-06-24 07:03:30` | `cowrie.client.kex` |
| `2026-06-24 07:03:30` | `cowrie.login.success` |
| `2026-06-24 07:03:31` | `cowrie.session.params` |
| `2026-06-24 07:03:31` | `cowrie.command.input` |
| `2026-06-24 07:03:31` | `cowrie.log.closed` |
| `2026-06-24 07:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4831453af1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:04 |
| **Last Seen** | 2026-06-24 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:04:22` | `cowrie.session.connect` |
| `2026-06-24 07:04:22` | `cowrie.client.version` |
| `2026-06-24 07:04:22` | `cowrie.client.kex` |
| `2026-06-24 07:04:22` | `cowrie.login.success` |
| `2026-06-24 07:04:23` | `cowrie.session.params` |
| `2026-06-24 07:04:23` | `cowrie.command.input` |
| `2026-06-24 07:04:23` | `cowrie.log.closed` |
| `2026-06-24 07:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fad6e87bbe9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:05 |
| **Last Seen** | 2026-06-24 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:05:14` | `cowrie.session.connect` |
| `2026-06-24 07:05:14` | `cowrie.client.version` |
| `2026-06-24 07:05:14` | `cowrie.client.kex` |
| `2026-06-24 07:05:15` | `cowrie.login.success` |
| `2026-06-24 07:05:15` | `cowrie.session.params` |
| `2026-06-24 07:05:15` | `cowrie.command.input` |
| `2026-06-24 07:05:16` | `cowrie.log.closed` |
| `2026-06-24 07:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d19b7512e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:06 |
| **Last Seen** | 2026-06-24 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:06:05` | `cowrie.session.connect` |
| `2026-06-24 07:06:05` | `cowrie.client.version` |
| `2026-06-24 07:06:05` | `cowrie.client.kex` |
| `2026-06-24 07:06:05` | `cowrie.login.success` |
| `2026-06-24 07:06:06` | `cowrie.session.params` |
| `2026-06-24 07:06:06` | `cowrie.command.input` |
| `2026-06-24 07:06:06` | `cowrie.log.closed` |
| `2026-06-24 07:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0de3d8c51e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:06 |
| **Last Seen** | 2026-06-24 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:06:56` | `cowrie.session.connect` |
| `2026-06-24 07:06:56` | `cowrie.client.version` |
| `2026-06-24 07:06:56` | `cowrie.client.kex` |
| `2026-06-24 07:06:56` | `cowrie.login.success` |
| `2026-06-24 07:06:57` | `cowrie.session.params` |
| `2026-06-24 07:06:57` | `cowrie.command.input` |
| `2026-06-24 07:06:57` | `cowrie.log.closed` |
| `2026-06-24 07:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccdb55f9ad3f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:07 |
| **Last Seen** | 2026-06-24 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:07:47` | `cowrie.session.connect` |
| `2026-06-24 07:07:47` | `cowrie.client.version` |
| `2026-06-24 07:07:47` | `cowrie.client.kex` |
| `2026-06-24 07:07:47` | `cowrie.login.success` |
| `2026-06-24 07:07:48` | `cowrie.session.params` |
| `2026-06-24 07:07:48` | `cowrie.command.input` |
| `2026-06-24 07:07:48` | `cowrie.log.closed` |
| `2026-06-24 07:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d53ff1f0c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:08 |
| **Last Seen** | 2026-06-24 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:08:40` | `cowrie.session.connect` |
| `2026-06-24 07:08:40` | `cowrie.client.version` |
| `2026-06-24 07:08:40` | `cowrie.client.kex` |
| `2026-06-24 07:08:40` | `cowrie.login.success` |
| `2026-06-24 07:08:41` | `cowrie.session.params` |
| `2026-06-24 07:08:41` | `cowrie.command.input` |
| `2026-06-24 07:08:41` | `cowrie.log.closed` |
| `2026-06-24 07:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3be2dc4579d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 07:09 |
| **Last Seen** | 2026-06-24 07:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:09:24` | `cowrie.session.connect` |
| `2026-06-24 07:09:25` | `cowrie.client.version` |
| `2026-06-24 07:09:25` | `cowrie.client.kex` |
| `2026-06-24 07:09:32` | `cowrie.login.success` |
| `2026-06-24 07:09:36` | `cowrie.session.params` |
| `2026-06-24 07:09:36` | `cowrie.command.input` |
| `2026-06-24 07:09:38` | `cowrie.log.closed` |
| `2026-06-24 07:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60abc68dbd7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:09 |
| **Last Seen** | 2026-06-24 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:09:33` | `cowrie.session.connect` |
| `2026-06-24 07:09:33` | `cowrie.client.version` |
| `2026-06-24 07:09:33` | `cowrie.client.kex` |
| `2026-06-24 07:09:34` | `cowrie.login.success` |
| `2026-06-24 07:09:34` | `cowrie.session.params` |
| `2026-06-24 07:09:34` | `cowrie.command.input` |
| `2026-06-24 07:09:34` | `cowrie.log.closed` |
| `2026-06-24 07:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985952f0c082

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:10 |
| **Last Seen** | 2026-06-24 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:10:27` | `cowrie.session.connect` |
| `2026-06-24 07:10:27` | `cowrie.client.version` |
| `2026-06-24 07:10:27` | `cowrie.client.kex` |
| `2026-06-24 07:10:28` | `cowrie.login.success` |
| `2026-06-24 07:10:28` | `cowrie.session.params` |
| `2026-06-24 07:10:28` | `cowrie.command.input` |
| `2026-06-24 07:10:29` | `cowrie.log.closed` |
| `2026-06-24 07:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff78aaedd46

| Field | Detail |
|---|---|
| **Source IP** | `111.77.115[.]116` |
| **First Seen** | 2026-06-24 07:10 |
| **Last Seen** | 2026-06-24 07:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/oIgUmIEI` |
| **Download Attempts** | 9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc |
| **Malware Analysis** | 9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc (MEDIUM) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:10:41` | `cowrie.session.connect` |
| `2026-06-24 07:10:41` | `cowrie.client.version` |
| `2026-06-24 07:10:41` | `cowrie.client.kex` |
| `2026-06-24 07:10:43` | `cowrie.login.success` |
| `2026-06-24 07:10:44` | `cowrie.client.var` |
| `2026-06-24 07:10:44` | `cowrie.session.params` |
| `2026-06-24 07:10:44` | `cowrie.command.input` |
| `2026-06-24 07:10:45` | `cowrie.session.file_download` |
| `2026-06-24 07:10:45` | `cowrie.log.closed` |
| `2026-06-24 07:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.77.115[.]116` to AbuseIPDB if not already reported
- [ ] Block `111.77.115[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c8e662c6f9

| Field | Detail |
|---|---|
| **Source IP** | `111.77.115[.]116` |
| **First Seen** | 2026-06-24 07:10 |
| **Last Seen** | 2026-06-24 07:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/oIgUmIEI` |
| **Download Attempts** | 9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc |
| **Malware Analysis** | 9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc (MEDIUM) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:10:41` | `cowrie.session.connect` |
| `2026-06-24 07:10:41` | `cowrie.client.version` |
| `2026-06-24 07:10:41` | `cowrie.client.kex` |
| `2026-06-24 07:10:43` | `cowrie.login.success` |
| `2026-06-24 07:10:44` | `cowrie.client.var` |
| `2026-06-24 07:10:45` | `cowrie.session.params` |
| `2026-06-24 07:10:45` | `cowrie.command.input` |
| `2026-06-24 07:10:45` | `cowrie.session.file_download` |
| `2026-06-24 07:10:45` | `cowrie.log.closed` |
| `2026-06-24 07:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.77.115[.]116` to AbuseIPDB if not already reported
- [ ] Block `111.77.115[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f867b1a261

| Field | Detail |
|---|---|
| **Source IP** | `111.77.115[.]116` |
| **First Seen** | 2026-06-24 07:10 |
| **Last Seen** | 2026-06-24 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x oIgUmIEI && bash -c ./oIgUmIEI, ./oIgUmIEI` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:10:46` | `cowrie.session.connect` |
| `2026-06-24 07:10:46` | `cowrie.client.version` |
| `2026-06-24 07:10:46` | `cowrie.client.kex` |
| `2026-06-24 07:10:47` | `cowrie.login.success` |
| `2026-06-24 07:10:48` | `cowrie.client.var` |
| `2026-06-24 07:10:48` | `cowrie.session.params` |
| `2026-06-24 07:10:48` | `cowrie.command.input` |
| `2026-06-24 07:10:48` | `cowrie.command.input` |
| `2026-06-24 07:10:48` | `cowrie.command.failed` |
| `2026-06-24 07:10:48` | `cowrie.log.closed` |
| `2026-06-24 07:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.77.115[.]116` to AbuseIPDB if not already reported
- [ ] Block `111.77.115[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ffc5b35ace

| Field | Detail |
|---|---|
| **Source IP** | `111.77.115[.]116` |
| **First Seen** | 2026-06-24 07:10 |
| **Last Seen** | 2026-06-24 07:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x oIgUmIEI && bash -c ./oIgUmIEI, ./oIgUmIEI` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:10:47` | `cowrie.session.connect` |
| `2026-06-24 07:10:47` | `cowrie.client.version` |
| `2026-06-24 07:10:47` | `cowrie.client.kex` |
| `2026-06-24 07:10:49` | `cowrie.login.success` |
| `2026-06-24 07:10:50` | `cowrie.client.var` |
| `2026-06-24 07:10:50` | `cowrie.session.params` |
| `2026-06-24 07:10:50` | `cowrie.command.input` |
| `2026-06-24 07:10:50` | `cowrie.command.input` |
| `2026-06-24 07:10:50` | `cowrie.command.failed` |
| `2026-06-24 07:10:50` | `cowrie.log.closed` |
| `2026-06-24 07:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.77.115[.]116` to AbuseIPDB if not already reported
- [ ] Block `111.77.115[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a816c0749040

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:11 |
| **Last Seen** | 2026-06-24 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:11:20` | `cowrie.session.connect` |
| `2026-06-24 07:11:20` | `cowrie.client.version` |
| `2026-06-24 07:11:21` | `cowrie.client.kex` |
| `2026-06-24 07:11:21` | `cowrie.login.success` |
| `2026-06-24 07:11:22` | `cowrie.session.params` |
| `2026-06-24 07:11:22` | `cowrie.command.input` |
| `2026-06-24 07:11:22` | `cowrie.log.closed` |
| `2026-06-24 07:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f7fc93171c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:12 |
| **Last Seen** | 2026-06-24 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:12:14` | `cowrie.session.connect` |
| `2026-06-24 07:12:14` | `cowrie.client.version` |
| `2026-06-24 07:12:14` | `cowrie.client.kex` |
| `2026-06-24 07:12:14` | `cowrie.login.success` |
| `2026-06-24 07:12:15` | `cowrie.session.params` |
| `2026-06-24 07:12:15` | `cowrie.command.input` |
| `2026-06-24 07:12:15` | `cowrie.log.closed` |
| `2026-06-24 07:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6292a02c616

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:13 |
| **Last Seen** | 2026-06-24 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:13:06` | `cowrie.session.connect` |
| `2026-06-24 07:13:06` | `cowrie.client.version` |
| `2026-06-24 07:13:06` | `cowrie.client.kex` |
| `2026-06-24 07:13:07` | `cowrie.login.success` |
| `2026-06-24 07:13:08` | `cowrie.session.params` |
| `2026-06-24 07:13:08` | `cowrie.command.input` |
| `2026-06-24 07:13:08` | `cowrie.log.closed` |
| `2026-06-24 07:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81c9b1f8487

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:14 |
| **Last Seen** | 2026-06-24 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:14:05` | `cowrie.session.connect` |
| `2026-06-24 07:14:05` | `cowrie.client.version` |
| `2026-06-24 07:14:05` | `cowrie.client.kex` |
| `2026-06-24 07:14:05` | `cowrie.login.success` |
| `2026-06-24 07:14:06` | `cowrie.session.params` |
| `2026-06-24 07:14:06` | `cowrie.command.input` |
| `2026-06-24 07:14:06` | `cowrie.log.closed` |
| `2026-06-24 07:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b6be7cfe72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:15 |
| **Last Seen** | 2026-06-24 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:15:00` | `cowrie.session.connect` |
| `2026-06-24 07:15:00` | `cowrie.client.version` |
| `2026-06-24 07:15:00` | `cowrie.client.kex` |
| `2026-06-24 07:15:00` | `cowrie.login.success` |
| `2026-06-24 07:15:01` | `cowrie.session.params` |
| `2026-06-24 07:15:01` | `cowrie.command.input` |
| `2026-06-24 07:15:01` | `cowrie.log.closed` |
| `2026-06-24 07:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c35bb8ada0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:15 |
| **Last Seen** | 2026-06-24 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:15:55` | `cowrie.session.connect` |
| `2026-06-24 07:15:55` | `cowrie.client.version` |
| `2026-06-24 07:15:55` | `cowrie.client.kex` |
| `2026-06-24 07:15:55` | `cowrie.login.success` |
| `2026-06-24 07:15:56` | `cowrie.session.params` |
| `2026-06-24 07:15:56` | `cowrie.command.input` |
| `2026-06-24 07:15:56` | `cowrie.log.closed` |
| `2026-06-24 07:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6810a59c2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:16 |
| **Last Seen** | 2026-06-24 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:16:48` | `cowrie.session.connect` |
| `2026-06-24 07:16:48` | `cowrie.client.version` |
| `2026-06-24 07:16:48` | `cowrie.client.kex` |
| `2026-06-24 07:16:49` | `cowrie.login.success` |
| `2026-06-24 07:16:49` | `cowrie.session.params` |
| `2026-06-24 07:16:49` | `cowrie.command.input` |
| `2026-06-24 07:16:50` | `cowrie.log.closed` |
| `2026-06-24 07:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ad5cb05c10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:17 |
| **Last Seen** | 2026-06-24 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:17:42` | `cowrie.session.connect` |
| `2026-06-24 07:17:42` | `cowrie.client.version` |
| `2026-06-24 07:17:42` | `cowrie.client.kex` |
| `2026-06-24 07:17:42` | `cowrie.login.success` |
| `2026-06-24 07:17:43` | `cowrie.session.params` |
| `2026-06-24 07:17:43` | `cowrie.command.input` |
| `2026-06-24 07:17:43` | `cowrie.log.closed` |
| `2026-06-24 07:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207da67b28a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:18 |
| **Last Seen** | 2026-06-24 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:18:34` | `cowrie.session.connect` |
| `2026-06-24 07:18:34` | `cowrie.client.version` |
| `2026-06-24 07:18:35` | `cowrie.client.kex` |
| `2026-06-24 07:18:35` | `cowrie.login.success` |
| `2026-06-24 07:18:36` | `cowrie.session.params` |
| `2026-06-24 07:18:36` | `cowrie.command.input` |
| `2026-06-24 07:18:36` | `cowrie.log.closed` |
| `2026-06-24 07:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704bf4e34a25

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:19 |
| **Last Seen** | 2026-06-24 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:19:28` | `cowrie.session.connect` |
| `2026-06-24 07:19:28` | `cowrie.client.version` |
| `2026-06-24 07:19:28` | `cowrie.client.kex` |
| `2026-06-24 07:19:28` | `cowrie.login.success` |
| `2026-06-24 07:19:29` | `cowrie.session.params` |
| `2026-06-24 07:19:29` | `cowrie.command.input` |
| `2026-06-24 07:19:29` | `cowrie.log.closed` |
| `2026-06-24 07:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f4e5ae380b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:20 |
| **Last Seen** | 2026-06-24 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:20:21` | `cowrie.session.connect` |
| `2026-06-24 07:20:21` | `cowrie.client.version` |
| `2026-06-24 07:20:21` | `cowrie.client.kex` |
| `2026-06-24 07:20:22` | `cowrie.login.success` |
| `2026-06-24 07:20:22` | `cowrie.session.params` |
| `2026-06-24 07:20:22` | `cowrie.command.input` |
| `2026-06-24 07:20:23` | `cowrie.log.closed` |
| `2026-06-24 07:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066d71028434

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:21 |
| **Last Seen** | 2026-06-24 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:21:16` | `cowrie.session.connect` |
| `2026-06-24 07:21:16` | `cowrie.client.version` |
| `2026-06-24 07:21:16` | `cowrie.client.kex` |
| `2026-06-24 07:21:16` | `cowrie.login.success` |
| `2026-06-24 07:21:17` | `cowrie.session.params` |
| `2026-06-24 07:21:17` | `cowrie.command.input` |
| `2026-06-24 07:21:17` | `cowrie.log.closed` |
| `2026-06-24 07:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f8af292043

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:22 |
| **Last Seen** | 2026-06-24 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:22:13` | `cowrie.session.connect` |
| `2026-06-24 07:22:13` | `cowrie.client.version` |
| `2026-06-24 07:22:13` | `cowrie.client.kex` |
| `2026-06-24 07:22:13` | `cowrie.login.success` |
| `2026-06-24 07:22:14` | `cowrie.session.params` |
| `2026-06-24 07:22:14` | `cowrie.command.input` |
| `2026-06-24 07:22:14` | `cowrie.log.closed` |
| `2026-06-24 07:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73fc218baca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:23 |
| **Last Seen** | 2026-06-24 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:23:08` | `cowrie.session.connect` |
| `2026-06-24 07:23:08` | `cowrie.client.version` |
| `2026-06-24 07:23:08` | `cowrie.client.kex` |
| `2026-06-24 07:23:08` | `cowrie.login.success` |
| `2026-06-24 07:23:09` | `cowrie.session.params` |
| `2026-06-24 07:23:09` | `cowrie.command.input` |
| `2026-06-24 07:23:09` | `cowrie.log.closed` |
| `2026-06-24 07:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b39c6b6199

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 07:23 |
| **Last Seen** | 2026-06-24 07:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:23:49` | `cowrie.session.connect` |
| `2026-06-24 07:23:50` | `cowrie.client.version` |
| `2026-06-24 07:23:50` | `cowrie.client.kex` |
| `2026-06-24 07:23:57` | `cowrie.login.success` |
| `2026-06-24 07:24:01` | `cowrie.session.params` |
| `2026-06-24 07:24:01` | `cowrie.command.input` |
| `2026-06-24 07:24:03` | `cowrie.log.closed` |
| `2026-06-24 07:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b07ba11b5a31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:24 |
| **Last Seen** | 2026-06-24 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:24:01` | `cowrie.session.connect` |
| `2026-06-24 07:24:01` | `cowrie.client.version` |
| `2026-06-24 07:24:02` | `cowrie.client.kex` |
| `2026-06-24 07:24:02` | `cowrie.login.success` |
| `2026-06-24 07:24:03` | `cowrie.session.params` |
| `2026-06-24 07:24:03` | `cowrie.command.input` |
| `2026-06-24 07:24:03` | `cowrie.log.closed` |
| `2026-06-24 07:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a178d84442a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:24 |
| **Last Seen** | 2026-06-24 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:24:55` | `cowrie.session.connect` |
| `2026-06-24 07:24:55` | `cowrie.client.version` |
| `2026-06-24 07:24:55` | `cowrie.client.kex` |
| `2026-06-24 07:24:55` | `cowrie.login.success` |
| `2026-06-24 07:24:56` | `cowrie.session.params` |
| `2026-06-24 07:24:56` | `cowrie.command.input` |
| `2026-06-24 07:24:56` | `cowrie.log.closed` |
| `2026-06-24 07:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126399adb84e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:25 |
| **Last Seen** | 2026-06-24 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:25:48` | `cowrie.session.connect` |
| `2026-06-24 07:25:48` | `cowrie.client.version` |
| `2026-06-24 07:25:48` | `cowrie.client.kex` |
| `2026-06-24 07:25:49` | `cowrie.login.success` |
| `2026-06-24 07:25:50` | `cowrie.session.params` |
| `2026-06-24 07:25:50` | `cowrie.command.input` |
| `2026-06-24 07:25:50` | `cowrie.log.closed` |
| `2026-06-24 07:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28facb339304

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:26 |
| **Last Seen** | 2026-06-24 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:26:44` | `cowrie.session.connect` |
| `2026-06-24 07:26:44` | `cowrie.client.version` |
| `2026-06-24 07:26:44` | `cowrie.client.kex` |
| `2026-06-24 07:26:44` | `cowrie.login.success` |
| `2026-06-24 07:26:45` | `cowrie.session.params` |
| `2026-06-24 07:26:45` | `cowrie.command.input` |
| `2026-06-24 07:26:45` | `cowrie.log.closed` |
| `2026-06-24 07:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d375c11509

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:27 |
| **Last Seen** | 2026-06-24 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:27:43` | `cowrie.session.connect` |
| `2026-06-24 07:27:43` | `cowrie.client.version` |
| `2026-06-24 07:27:43` | `cowrie.client.kex` |
| `2026-06-24 07:27:43` | `cowrie.login.success` |
| `2026-06-24 07:27:44` | `cowrie.session.params` |
| `2026-06-24 07:27:44` | `cowrie.command.input` |
| `2026-06-24 07:27:44` | `cowrie.log.closed` |
| `2026-06-24 07:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1fae317f82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:28 |
| **Last Seen** | 2026-06-24 07:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:28:39` | `cowrie.session.connect` |
| `2026-06-24 07:28:39` | `cowrie.client.version` |
| `2026-06-24 07:28:40` | `cowrie.client.kex` |
| `2026-06-24 07:28:40` | `cowrie.login.success` |
| `2026-06-24 07:28:41` | `cowrie.session.params` |
| `2026-06-24 07:28:41` | `cowrie.command.input` |
| `2026-06-24 07:28:41` | `cowrie.log.closed` |
| `2026-06-24 07:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860b32abfae8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:29 |
| **Last Seen** | 2026-06-24 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:29:36` | `cowrie.session.connect` |
| `2026-06-24 07:29:36` | `cowrie.client.version` |
| `2026-06-24 07:29:36` | `cowrie.client.kex` |
| `2026-06-24 07:29:37` | `cowrie.login.success` |
| `2026-06-24 07:29:38` | `cowrie.session.params` |
| `2026-06-24 07:29:38` | `cowrie.command.input` |
| `2026-06-24 07:29:38` | `cowrie.log.closed` |
| `2026-06-24 07:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77337c71627e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:30 |
| **Last Seen** | 2026-06-24 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:30:32` | `cowrie.session.connect` |
| `2026-06-24 07:30:32` | `cowrie.client.version` |
| `2026-06-24 07:30:32` | `cowrie.client.kex` |
| `2026-06-24 07:30:32` | `cowrie.login.success` |
| `2026-06-24 07:30:33` | `cowrie.session.params` |
| `2026-06-24 07:30:33` | `cowrie.command.input` |
| `2026-06-24 07:30:33` | `cowrie.log.closed` |
| `2026-06-24 07:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c7cbbe19ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:31 |
| **Last Seen** | 2026-06-24 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:31:26` | `cowrie.session.connect` |
| `2026-06-24 07:31:26` | `cowrie.client.version` |
| `2026-06-24 07:31:26` | `cowrie.client.kex` |
| `2026-06-24 07:31:26` | `cowrie.login.success` |
| `2026-06-24 07:31:27` | `cowrie.session.params` |
| `2026-06-24 07:31:27` | `cowrie.command.input` |
| `2026-06-24 07:31:27` | `cowrie.log.closed` |
| `2026-06-24 07:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147cd702dc43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:32 |
| **Last Seen** | 2026-06-24 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:32:25` | `cowrie.session.connect` |
| `2026-06-24 07:32:25` | `cowrie.client.version` |
| `2026-06-24 07:32:25` | `cowrie.client.kex` |
| `2026-06-24 07:32:25` | `cowrie.login.success` |
| `2026-06-24 07:32:26` | `cowrie.session.params` |
| `2026-06-24 07:32:26` | `cowrie.command.input` |
| `2026-06-24 07:32:26` | `cowrie.log.closed` |
| `2026-06-24 07:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13709f5c93b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:33 |
| **Last Seen** | 2026-06-24 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:33:21` | `cowrie.session.connect` |
| `2026-06-24 07:33:21` | `cowrie.client.version` |
| `2026-06-24 07:33:21` | `cowrie.client.kex` |
| `2026-06-24 07:33:21` | `cowrie.login.success` |
| `2026-06-24 07:33:22` | `cowrie.session.params` |
| `2026-06-24 07:33:22` | `cowrie.command.input` |
| `2026-06-24 07:33:22` | `cowrie.log.closed` |
| `2026-06-24 07:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efad5f5ebd64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:34 |
| **Last Seen** | 2026-06-24 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:34:17` | `cowrie.session.connect` |
| `2026-06-24 07:34:17` | `cowrie.client.version` |
| `2026-06-24 07:34:17` | `cowrie.client.kex` |
| `2026-06-24 07:34:17` | `cowrie.login.success` |
| `2026-06-24 07:34:18` | `cowrie.session.params` |
| `2026-06-24 07:34:18` | `cowrie.command.input` |
| `2026-06-24 07:34:18` | `cowrie.log.closed` |
| `2026-06-24 07:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7b8d17c4b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:35 |
| **Last Seen** | 2026-06-24 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:35:14` | `cowrie.session.connect` |
| `2026-06-24 07:35:14` | `cowrie.client.version` |
| `2026-06-24 07:35:14` | `cowrie.client.kex` |
| `2026-06-24 07:35:15` | `cowrie.login.success` |
| `2026-06-24 07:35:15` | `cowrie.session.params` |
| `2026-06-24 07:35:15` | `cowrie.command.input` |
| `2026-06-24 07:35:15` | `cowrie.log.closed` |
| `2026-06-24 07:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd79929db027

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:36 |
| **Last Seen** | 2026-06-24 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:36:12` | `cowrie.session.connect` |
| `2026-06-24 07:36:12` | `cowrie.client.version` |
| `2026-06-24 07:36:12` | `cowrie.client.kex` |
| `2026-06-24 07:36:12` | `cowrie.login.success` |
| `2026-06-24 07:36:13` | `cowrie.session.params` |
| `2026-06-24 07:36:13` | `cowrie.command.input` |
| `2026-06-24 07:36:13` | `cowrie.log.closed` |
| `2026-06-24 07:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645cd64955e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:37 |
| **Last Seen** | 2026-06-24 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:37:07` | `cowrie.session.connect` |
| `2026-06-24 07:37:07` | `cowrie.client.version` |
| `2026-06-24 07:37:07` | `cowrie.client.kex` |
| `2026-06-24 07:37:07` | `cowrie.login.success` |
| `2026-06-24 07:37:08` | `cowrie.session.params` |
| `2026-06-24 07:37:08` | `cowrie.command.input` |
| `2026-06-24 07:37:08` | `cowrie.log.closed` |
| `2026-06-24 07:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9860816cb39

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 07:37 |
| **Last Seen** | 2026-06-24 07:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:37:59` | `cowrie.session.connect` |
| `2026-06-24 07:38:01` | `cowrie.client.version` |
| `2026-06-24 07:38:01` | `cowrie.client.kex` |
| `2026-06-24 07:38:07` | `cowrie.login.success` |
| `2026-06-24 07:38:11` | `cowrie.session.params` |
| `2026-06-24 07:38:11` | `cowrie.command.input` |
| `2026-06-24 07:38:13` | `cowrie.log.closed` |
| `2026-06-24 07:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ba6aac3c30

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:38 |
| **Last Seen** | 2026-06-24 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:38:01` | `cowrie.session.connect` |
| `2026-06-24 07:38:01` | `cowrie.client.version` |
| `2026-06-24 07:38:01` | `cowrie.client.kex` |
| `2026-06-24 07:38:02` | `cowrie.login.success` |
| `2026-06-24 07:38:03` | `cowrie.session.params` |
| `2026-06-24 07:38:03` | `cowrie.command.input` |
| `2026-06-24 07:38:03` | `cowrie.log.closed` |
| `2026-06-24 07:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778fc0e81586

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:38 |
| **Last Seen** | 2026-06-24 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:38:57` | `cowrie.session.connect` |
| `2026-06-24 07:38:57` | `cowrie.client.version` |
| `2026-06-24 07:38:57` | `cowrie.client.kex` |
| `2026-06-24 07:38:57` | `cowrie.login.success` |
| `2026-06-24 07:38:58` | `cowrie.session.params` |
| `2026-06-24 07:38:58` | `cowrie.command.input` |
| `2026-06-24 07:38:58` | `cowrie.log.closed` |
| `2026-06-24 07:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55cc140ee67d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:39 |
| **Last Seen** | 2026-06-24 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:39:54` | `cowrie.session.connect` |
| `2026-06-24 07:39:54` | `cowrie.client.version` |
| `2026-06-24 07:39:54` | `cowrie.client.kex` |
| `2026-06-24 07:39:54` | `cowrie.login.success` |
| `2026-06-24 07:39:55` | `cowrie.session.params` |
| `2026-06-24 07:39:55` | `cowrie.command.input` |
| `2026-06-24 07:39:55` | `cowrie.log.closed` |
| `2026-06-24 07:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a525b067db3a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:40 |
| **Last Seen** | 2026-06-24 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:40:51` | `cowrie.session.connect` |
| `2026-06-24 07:40:51` | `cowrie.client.version` |
| `2026-06-24 07:40:52` | `cowrie.client.kex` |
| `2026-06-24 07:40:52` | `cowrie.login.success` |
| `2026-06-24 07:40:53` | `cowrie.session.params` |
| `2026-06-24 07:40:53` | `cowrie.command.input` |
| `2026-06-24 07:40:53` | `cowrie.log.closed` |
| `2026-06-24 07:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9218ad98d1f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:41 |
| **Last Seen** | 2026-06-24 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:41:50` | `cowrie.session.connect` |
| `2026-06-24 07:41:50` | `cowrie.client.version` |
| `2026-06-24 07:41:50` | `cowrie.client.kex` |
| `2026-06-24 07:41:50` | `cowrie.login.success` |
| `2026-06-24 07:41:51` | `cowrie.session.params` |
| `2026-06-24 07:41:51` | `cowrie.command.input` |
| `2026-06-24 07:41:51` | `cowrie.log.closed` |
| `2026-06-24 07:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07fd01b11ca8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:42 |
| **Last Seen** | 2026-06-24 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:42:47` | `cowrie.session.connect` |
| `2026-06-24 07:42:47` | `cowrie.client.version` |
| `2026-06-24 07:42:47` | `cowrie.client.kex` |
| `2026-06-24 07:42:47` | `cowrie.login.success` |
| `2026-06-24 07:42:48` | `cowrie.session.params` |
| `2026-06-24 07:42:48` | `cowrie.command.input` |
| `2026-06-24 07:42:48` | `cowrie.log.closed` |
| `2026-06-24 07:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3dcdaefbb4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:43 |
| **Last Seen** | 2026-06-24 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:43:42` | `cowrie.session.connect` |
| `2026-06-24 07:43:42` | `cowrie.client.version` |
| `2026-06-24 07:43:42` | `cowrie.client.kex` |
| `2026-06-24 07:43:43` | `cowrie.login.success` |
| `2026-06-24 07:43:43` | `cowrie.session.params` |
| `2026-06-24 07:43:43` | `cowrie.command.input` |
| `2026-06-24 07:43:44` | `cowrie.log.closed` |
| `2026-06-24 07:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae3d611132c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:44 |
| **Last Seen** | 2026-06-24 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:44:37` | `cowrie.session.connect` |
| `2026-06-24 07:44:37` | `cowrie.client.version` |
| `2026-06-24 07:44:37` | `cowrie.client.kex` |
| `2026-06-24 07:44:38` | `cowrie.login.success` |
| `2026-06-24 07:44:38` | `cowrie.session.params` |
| `2026-06-24 07:44:38` | `cowrie.command.input` |
| `2026-06-24 07:44:38` | `cowrie.log.closed` |
| `2026-06-24 07:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24cdfeaa613e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:45 |
| **Last Seen** | 2026-06-24 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:45:34` | `cowrie.session.connect` |
| `2026-06-24 07:45:34` | `cowrie.client.version` |
| `2026-06-24 07:45:34` | `cowrie.client.kex` |
| `2026-06-24 07:45:35` | `cowrie.login.success` |
| `2026-06-24 07:45:35` | `cowrie.session.params` |
| `2026-06-24 07:45:35` | `cowrie.command.input` |
| `2026-06-24 07:45:36` | `cowrie.log.closed` |
| `2026-06-24 07:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84860d26e32d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:46 |
| **Last Seen** | 2026-06-24 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:46:30` | `cowrie.session.connect` |
| `2026-06-24 07:46:30` | `cowrie.client.version` |
| `2026-06-24 07:46:30` | `cowrie.client.kex` |
| `2026-06-24 07:46:31` | `cowrie.login.success` |
| `2026-06-24 07:46:32` | `cowrie.session.params` |
| `2026-06-24 07:46:32` | `cowrie.command.input` |
| `2026-06-24 07:46:32` | `cowrie.log.closed` |
| `2026-06-24 07:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94d77c566b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:47 |
| **Last Seen** | 2026-06-24 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:47:27` | `cowrie.session.connect` |
| `2026-06-24 07:47:27` | `cowrie.client.version` |
| `2026-06-24 07:47:27` | `cowrie.client.kex` |
| `2026-06-24 07:47:27` | `cowrie.login.success` |
| `2026-06-24 07:47:28` | `cowrie.session.params` |
| `2026-06-24 07:47:28` | `cowrie.command.input` |
| `2026-06-24 07:47:28` | `cowrie.log.closed` |
| `2026-06-24 07:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae824db91a1

| Field | Detail |
|---|---|
| **Source IP** | `185.65.202[.]199` |
| **First Seen** | 2026-06-24 07:48 |
| **Last Seen** | 2026-06-24 07:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:48:00` | `cowrie.session.connect` |
| `2026-06-24 07:48:00` | `cowrie.client.version` |
| `2026-06-24 07:48:00` | `cowrie.client.kex` |
| `2026-06-24 07:48:00` | `cowrie.login.success` |
| `2026-06-24 07:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.65.202[.]199` to AbuseIPDB if not already reported
- [ ] Block `185.65.202[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352a7c23cc81

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-24 07:48 |
| **Last Seen** | 2026-06-24 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:48:00` | `cowrie.session.connect` |
| `2026-06-24 07:48:00` | `cowrie.client.version` |
| `2026-06-24 07:48:00` | `cowrie.client.kex` |
| `2026-06-24 07:48:01` | `cowrie.login.success` |
| `2026-06-24 07:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e0aafd7ea58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:48 |
| **Last Seen** | 2026-06-24 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:48:25` | `cowrie.session.connect` |
| `2026-06-24 07:48:25` | `cowrie.client.version` |
| `2026-06-24 07:48:25` | `cowrie.client.kex` |
| `2026-06-24 07:48:26` | `cowrie.login.success` |
| `2026-06-24 07:48:26` | `cowrie.session.params` |
| `2026-06-24 07:48:26` | `cowrie.command.input` |
| `2026-06-24 07:48:27` | `cowrie.log.closed` |
| `2026-06-24 07:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e40ecce0ec5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:49 |
| **Last Seen** | 2026-06-24 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:49:22` | `cowrie.session.connect` |
| `2026-06-24 07:49:22` | `cowrie.client.version` |
| `2026-06-24 07:49:22` | `cowrie.client.kex` |
| `2026-06-24 07:49:22` | `cowrie.login.success` |
| `2026-06-24 07:49:23` | `cowrie.session.params` |
| `2026-06-24 07:49:23` | `cowrie.command.input` |
| `2026-06-24 07:49:23` | `cowrie.log.closed` |
| `2026-06-24 07:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc2f04acb64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:50 |
| **Last Seen** | 2026-06-24 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:50:17` | `cowrie.session.connect` |
| `2026-06-24 07:50:17` | `cowrie.client.version` |
| `2026-06-24 07:50:17` | `cowrie.client.kex` |
| `2026-06-24 07:50:18` | `cowrie.login.success` |
| `2026-06-24 07:50:18` | `cowrie.session.params` |
| `2026-06-24 07:50:18` | `cowrie.command.input` |
| `2026-06-24 07:50:19` | `cowrie.log.closed` |
| `2026-06-24 07:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5521735e2b88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:51 |
| **Last Seen** | 2026-06-24 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:51:13` | `cowrie.session.connect` |
| `2026-06-24 07:51:13` | `cowrie.client.version` |
| `2026-06-24 07:51:13` | `cowrie.client.kex` |
| `2026-06-24 07:51:14` | `cowrie.login.success` |
| `2026-06-24 07:51:14` | `cowrie.session.params` |
| `2026-06-24 07:51:14` | `cowrie.command.input` |
| `2026-06-24 07:51:14` | `cowrie.log.closed` |
| `2026-06-24 07:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a17b468f459

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:52 |
| **Last Seen** | 2026-06-24 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:52:11` | `cowrie.session.connect` |
| `2026-06-24 07:52:11` | `cowrie.client.version` |
| `2026-06-24 07:52:11` | `cowrie.client.kex` |
| `2026-06-24 07:52:11` | `cowrie.login.success` |
| `2026-06-24 07:52:12` | `cowrie.session.params` |
| `2026-06-24 07:52:12` | `cowrie.command.input` |
| `2026-06-24 07:52:12` | `cowrie.log.closed` |
| `2026-06-24 07:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570fbf81eb98

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 07:52 |
| **Last Seen** | 2026-06-24 07:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:52:22` | `cowrie.session.connect` |
| `2026-06-24 07:52:24` | `cowrie.client.version` |
| `2026-06-24 07:52:24` | `cowrie.client.kex` |
| `2026-06-24 07:52:30` | `cowrie.login.success` |
| `2026-06-24 07:52:33` | `cowrie.session.params` |
| `2026-06-24 07:52:33` | `cowrie.command.input` |
| `2026-06-24 07:52:34` | `cowrie.log.closed` |
| `2026-06-24 07:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41cf254bc1f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:53 |
| **Last Seen** | 2026-06-24 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:53:08` | `cowrie.session.connect` |
| `2026-06-24 07:53:08` | `cowrie.client.version` |
| `2026-06-24 07:53:08` | `cowrie.client.kex` |
| `2026-06-24 07:53:09` | `cowrie.login.success` |
| `2026-06-24 07:53:09` | `cowrie.session.params` |
| `2026-06-24 07:53:09` | `cowrie.command.input` |
| `2026-06-24 07:53:10` | `cowrie.log.closed` |
| `2026-06-24 07:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b47423497db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:54 |
| **Last Seen** | 2026-06-24 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:54:10` | `cowrie.session.connect` |
| `2026-06-24 07:54:10` | `cowrie.client.version` |
| `2026-06-24 07:54:10` | `cowrie.client.kex` |
| `2026-06-24 07:54:10` | `cowrie.login.success` |
| `2026-06-24 07:54:11` | `cowrie.session.params` |
| `2026-06-24 07:54:11` | `cowrie.command.input` |
| `2026-06-24 07:54:11` | `cowrie.log.closed` |
| `2026-06-24 07:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03be342c6c5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:55 |
| **Last Seen** | 2026-06-24 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:55:11` | `cowrie.session.connect` |
| `2026-06-24 07:55:11` | `cowrie.client.version` |
| `2026-06-24 07:55:12` | `cowrie.client.kex` |
| `2026-06-24 07:55:12` | `cowrie.login.success` |
| `2026-06-24 07:55:13` | `cowrie.session.params` |
| `2026-06-24 07:55:13` | `cowrie.command.input` |
| `2026-06-24 07:55:13` | `cowrie.log.closed` |
| `2026-06-24 07:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5b8cf99cd0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:56 |
| **Last Seen** | 2026-06-24 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:56:12` | `cowrie.session.connect` |
| `2026-06-24 07:56:12` | `cowrie.client.version` |
| `2026-06-24 07:56:12` | `cowrie.client.kex` |
| `2026-06-24 07:56:12` | `cowrie.login.success` |
| `2026-06-24 07:56:13` | `cowrie.session.params` |
| `2026-06-24 07:56:13` | `cowrie.command.input` |
| `2026-06-24 07:56:13` | `cowrie.log.closed` |
| `2026-06-24 07:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2f8e8755552

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:57 |
| **Last Seen** | 2026-06-24 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:57:08` | `cowrie.session.connect` |
| `2026-06-24 07:57:08` | `cowrie.client.version` |
| `2026-06-24 07:57:08` | `cowrie.client.kex` |
| `2026-06-24 07:57:09` | `cowrie.login.success` |
| `2026-06-24 07:57:09` | `cowrie.session.params` |
| `2026-06-24 07:57:09` | `cowrie.command.input` |
| `2026-06-24 07:57:10` | `cowrie.log.closed` |
| `2026-06-24 07:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a8218dfb3c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:58 |
| **Last Seen** | 2026-06-24 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:58:05` | `cowrie.session.connect` |
| `2026-06-24 07:58:05` | `cowrie.client.version` |
| `2026-06-24 07:58:05` | `cowrie.client.kex` |
| `2026-06-24 07:58:05` | `cowrie.login.success` |
| `2026-06-24 07:58:06` | `cowrie.session.params` |
| `2026-06-24 07:58:06` | `cowrie.command.input` |
| `2026-06-24 07:58:06` | `cowrie.log.closed` |
| `2026-06-24 07:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef25aa116b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 07:59 |
| **Last Seen** | 2026-06-24 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 07:59:04` | `cowrie.session.connect` |
| `2026-06-24 07:59:04` | `cowrie.client.version` |
| `2026-06-24 07:59:04` | `cowrie.client.kex` |
| `2026-06-24 07:59:05` | `cowrie.login.success` |
| `2026-06-24 07:59:05` | `cowrie.session.params` |
| `2026-06-24 07:59:05` | `cowrie.command.input` |
| `2026-06-24 07:59:06` | `cowrie.log.closed` |
| `2026-06-24 07:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73807b0d7164

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:00 |
| **Last Seen** | 2026-06-24 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:00:04` | `cowrie.session.connect` |
| `2026-06-24 08:00:04` | `cowrie.client.version` |
| `2026-06-24 08:00:04` | `cowrie.client.kex` |
| `2026-06-24 08:00:05` | `cowrie.login.success` |
| `2026-06-24 08:00:06` | `cowrie.session.params` |
| `2026-06-24 08:00:06` | `cowrie.command.input` |
| `2026-06-24 08:00:06` | `cowrie.log.closed` |
| `2026-06-24 08:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6976d31db3

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-06-24 08:00 |
| **Last Seen** | 2026-06-24 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:00:36` | `cowrie.session.connect` |
| `2026-06-24 08:00:36` | `cowrie.client.version` |
| `2026-06-24 08:00:36` | `cowrie.client.kex` |
| `2026-06-24 08:00:36` | `cowrie.login.success` |
| `2026-06-24 08:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ff8856f552

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-24 08:00 |
| **Last Seen** | 2026-06-24 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:00:37` | `cowrie.session.connect` |
| `2026-06-24 08:00:37` | `cowrie.client.version` |
| `2026-06-24 08:00:37` | `cowrie.client.kex` |
| `2026-06-24 08:00:37` | `cowrie.login.success` |
| `2026-06-24 08:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d916389b97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:00 |
| **Last Seen** | 2026-06-24 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:00:54` | `cowrie.session.connect` |
| `2026-06-24 08:00:54` | `cowrie.client.version` |
| `2026-06-24 08:00:55` | `cowrie.client.kex` |
| `2026-06-24 08:00:55` | `cowrie.login.success` |
| `2026-06-24 08:00:56` | `cowrie.session.params` |
| `2026-06-24 08:00:56` | `cowrie.command.input` |
| `2026-06-24 08:00:56` | `cowrie.log.closed` |
| `2026-06-24 08:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b07300043a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:01 |
| **Last Seen** | 2026-06-24 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:01:44` | `cowrie.session.connect` |
| `2026-06-24 08:01:44` | `cowrie.client.version` |
| `2026-06-24 08:01:44` | `cowrie.client.kex` |
| `2026-06-24 08:01:45` | `cowrie.login.success` |
| `2026-06-24 08:01:45` | `cowrie.session.params` |
| `2026-06-24 08:01:45` | `cowrie.command.input` |
| `2026-06-24 08:01:46` | `cowrie.log.closed` |
| `2026-06-24 08:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0732c7d416b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:02 |
| **Last Seen** | 2026-06-24 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:02:30` | `cowrie.session.connect` |
| `2026-06-24 08:02:30` | `cowrie.client.version` |
| `2026-06-24 08:02:30` | `cowrie.client.kex` |
| `2026-06-24 08:02:30` | `cowrie.login.success` |
| `2026-06-24 08:02:31` | `cowrie.session.params` |
| `2026-06-24 08:02:31` | `cowrie.command.input` |
| `2026-06-24 08:02:31` | `cowrie.log.closed` |
| `2026-06-24 08:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c253ee2913b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:03 |
| **Last Seen** | 2026-06-24 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:03:14` | `cowrie.session.connect` |
| `2026-06-24 08:03:14` | `cowrie.client.version` |
| `2026-06-24 08:03:14` | `cowrie.client.kex` |
| `2026-06-24 08:03:15` | `cowrie.login.success` |
| `2026-06-24 08:03:16` | `cowrie.session.params` |
| `2026-06-24 08:03:16` | `cowrie.command.input` |
| `2026-06-24 08:03:16` | `cowrie.log.closed` |
| `2026-06-24 08:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581a44bf4abe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:04 |
| **Last Seen** | 2026-06-24 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:04:00` | `cowrie.session.connect` |
| `2026-06-24 08:04:00` | `cowrie.client.version` |
| `2026-06-24 08:04:00` | `cowrie.client.kex` |
| `2026-06-24 08:04:00` | `cowrie.login.success` |
| `2026-06-24 08:04:01` | `cowrie.session.params` |
| `2026-06-24 08:04:01` | `cowrie.command.input` |
| `2026-06-24 08:04:01` | `cowrie.log.closed` |
| `2026-06-24 08:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92e51c0ac00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:04 |
| **Last Seen** | 2026-06-24 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:04:46` | `cowrie.session.connect` |
| `2026-06-24 08:04:46` | `cowrie.client.version` |
| `2026-06-24 08:04:46` | `cowrie.client.kex` |
| `2026-06-24 08:04:47` | `cowrie.login.success` |
| `2026-06-24 08:04:47` | `cowrie.session.params` |
| `2026-06-24 08:04:47` | `cowrie.command.input` |
| `2026-06-24 08:04:48` | `cowrie.log.closed` |
| `2026-06-24 08:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75730aa2428

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:05 |
| **Last Seen** | 2026-06-24 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:05:33` | `cowrie.session.connect` |
| `2026-06-24 08:05:33` | `cowrie.client.version` |
| `2026-06-24 08:05:33` | `cowrie.client.kex` |
| `2026-06-24 08:05:33` | `cowrie.login.success` |
| `2026-06-24 08:05:34` | `cowrie.session.params` |
| `2026-06-24 08:05:34` | `cowrie.command.input` |
| `2026-06-24 08:05:34` | `cowrie.log.closed` |
| `2026-06-24 08:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1517c9373897

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:06 |
| **Last Seen** | 2026-06-24 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:06:21` | `cowrie.session.connect` |
| `2026-06-24 08:06:21` | `cowrie.client.version` |
| `2026-06-24 08:06:21` | `cowrie.client.kex` |
| `2026-06-24 08:06:21` | `cowrie.login.success` |
| `2026-06-24 08:06:22` | `cowrie.session.params` |
| `2026-06-24 08:06:22` | `cowrie.command.input` |
| `2026-06-24 08:06:22` | `cowrie.log.closed` |
| `2026-06-24 08:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbfb590dfa7f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 08:06 |
| **Last Seen** | 2026-06-24 08:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:06:45` | `cowrie.session.connect` |
| `2026-06-24 08:06:47` | `cowrie.client.version` |
| `2026-06-24 08:06:47` | `cowrie.client.kex` |
| `2026-06-24 08:06:53` | `cowrie.login.success` |
| `2026-06-24 08:06:57` | `cowrie.session.params` |
| `2026-06-24 08:06:57` | `cowrie.command.input` |
| `2026-06-24 08:06:58` | `cowrie.log.closed` |
| `2026-06-24 08:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d55a8b5a7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:07 |
| **Last Seen** | 2026-06-24 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:07:07` | `cowrie.session.connect` |
| `2026-06-24 08:07:07` | `cowrie.client.version` |
| `2026-06-24 08:07:07` | `cowrie.client.kex` |
| `2026-06-24 08:07:07` | `cowrie.login.success` |
| `2026-06-24 08:07:08` | `cowrie.session.params` |
| `2026-06-24 08:07:08` | `cowrie.command.input` |
| `2026-06-24 08:07:08` | `cowrie.log.closed` |
| `2026-06-24 08:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a7b5c8f2af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:07 |
| **Last Seen** | 2026-06-24 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:07:54` | `cowrie.session.connect` |
| `2026-06-24 08:07:54` | `cowrie.client.version` |
| `2026-06-24 08:07:55` | `cowrie.client.kex` |
| `2026-06-24 08:07:55` | `cowrie.login.success` |
| `2026-06-24 08:07:56` | `cowrie.session.params` |
| `2026-06-24 08:07:56` | `cowrie.command.input` |
| `2026-06-24 08:07:56` | `cowrie.log.closed` |
| `2026-06-24 08:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552a39a02e3a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:08 |
| **Last Seen** | 2026-06-24 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:08:43` | `cowrie.session.connect` |
| `2026-06-24 08:08:43` | `cowrie.client.version` |
| `2026-06-24 08:08:43` | `cowrie.client.kex` |
| `2026-06-24 08:08:44` | `cowrie.login.success` |
| `2026-06-24 08:08:45` | `cowrie.session.params` |
| `2026-06-24 08:08:45` | `cowrie.command.input` |
| `2026-06-24 08:08:45` | `cowrie.log.closed` |
| `2026-06-24 08:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1da3285bb8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:09 |
| **Last Seen** | 2026-06-24 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:09:28` | `cowrie.session.connect` |
| `2026-06-24 08:09:28` | `cowrie.client.version` |
| `2026-06-24 08:09:28` | `cowrie.client.kex` |
| `2026-06-24 08:09:29` | `cowrie.login.success` |
| `2026-06-24 08:09:29` | `cowrie.session.params` |
| `2026-06-24 08:09:29` | `cowrie.command.input` |
| `2026-06-24 08:09:30` | `cowrie.log.closed` |
| `2026-06-24 08:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64cf60ad7e8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:10 |
| **Last Seen** | 2026-06-24 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:10:13` | `cowrie.session.connect` |
| `2026-06-24 08:10:13` | `cowrie.client.version` |
| `2026-06-24 08:10:13` | `cowrie.client.kex` |
| `2026-06-24 08:10:13` | `cowrie.login.success` |
| `2026-06-24 08:10:14` | `cowrie.session.params` |
| `2026-06-24 08:10:14` | `cowrie.command.input` |
| `2026-06-24 08:10:14` | `cowrie.log.closed` |
| `2026-06-24 08:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de6d1c18ab1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:10 |
| **Last Seen** | 2026-06-24 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:10:58` | `cowrie.session.connect` |
| `2026-06-24 08:10:58` | `cowrie.client.version` |
| `2026-06-24 08:10:58` | `cowrie.client.kex` |
| `2026-06-24 08:10:59` | `cowrie.login.success` |
| `2026-06-24 08:10:59` | `cowrie.session.params` |
| `2026-06-24 08:10:59` | `cowrie.command.input` |
| `2026-06-24 08:11:00` | `cowrie.log.closed` |
| `2026-06-24 08:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3260f342068a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:11 |
| **Last Seen** | 2026-06-24 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:11:44` | `cowrie.session.connect` |
| `2026-06-24 08:11:44` | `cowrie.client.version` |
| `2026-06-24 08:11:44` | `cowrie.client.kex` |
| `2026-06-24 08:11:44` | `cowrie.login.success` |
| `2026-06-24 08:11:45` | `cowrie.session.params` |
| `2026-06-24 08:11:45` | `cowrie.command.input` |
| `2026-06-24 08:11:45` | `cowrie.log.closed` |
| `2026-06-24 08:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1abb90b3339d

| Field | Detail |
|---|---|
| **Source IP** | `104.199.1[.]98` |
| **First Seen** | 2026-06-24 08:11 |
| **Last Seen** | 2026-06-24 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:11:44` | `cowrie.session.connect` |
| `2026-06-24 08:11:44` | `cowrie.login.success` |
| `2026-06-24 08:11:45` | `cowrie.session.params` |
| `2026-06-24 08:11:45` | `cowrie.command.input` |
| `2026-06-24 08:11:45` | `cowrie.command.input` |
| `2026-06-24 08:11:45` | `cowrie.command.failed` |
| `2026-06-24 08:11:45` | `cowrie.command.input` |
| `2026-06-24 08:11:45` | `cowrie.log.closed` |
| `2026-06-24 08:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.1[.]98` to AbuseIPDB if not already reported
- [ ] Block `104.199.1[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f875e8b8d5a

| Field | Detail |
|---|---|
| **Source IP** | `104.199.1[.]98` |
| **First Seen** | 2026-06-24 08:11 |
| **Last Seen** | 2026-06-24 08:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:11:53` | `cowrie.session.connect` |
| `2026-06-24 08:11:53` | `cowrie.login.success` |
| `2026-06-24 08:11:54` | `cowrie.session.params` |
| `2026-06-24 08:11:54` | `cowrie.command.input` |
| `2026-06-24 08:11:54` | `cowrie.command.failed` |
| `2026-06-24 08:12:08` | `cowrie.log.closed` |
| `2026-06-24 08:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.1[.]98` to AbuseIPDB if not already reported
- [ ] Block `104.199.1[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2f67ffa1ae

| Field | Detail |
|---|---|
| **Source IP** | `104.199.1[.]98` |
| **First Seen** | 2026-06-24 08:11 |
| **Last Seen** | 2026-06-24 08:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:11:55` | `cowrie.session.connect` |
| `2026-06-24 08:11:55` | `cowrie.login.success` |
| `2026-06-24 08:11:56` | `cowrie.session.params` |
| `2026-06-24 08:11:56` | `cowrie.command.input` |
| `2026-06-24 08:12:08` | `cowrie.log.closed` |
| `2026-06-24 08:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.1[.]98` to AbuseIPDB if not already reported
- [ ] Block `104.199.1[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33fb882bc34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:12 |
| **Last Seen** | 2026-06-24 08:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:12:31` | `cowrie.session.connect` |
| `2026-06-24 08:12:31` | `cowrie.client.version` |
| `2026-06-24 08:12:31` | `cowrie.client.kex` |
| `2026-06-24 08:12:31` | `cowrie.login.success` |
| `2026-06-24 08:12:32` | `cowrie.session.params` |
| `2026-06-24 08:12:32` | `cowrie.command.input` |
| `2026-06-24 08:12:32` | `cowrie.log.closed` |
| `2026-06-24 08:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0626fe8f81c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:13 |
| **Last Seen** | 2026-06-24 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:13:24` | `cowrie.session.connect` |
| `2026-06-24 08:13:24` | `cowrie.client.version` |
| `2026-06-24 08:13:24` | `cowrie.client.kex` |
| `2026-06-24 08:13:24` | `cowrie.login.success` |
| `2026-06-24 08:13:25` | `cowrie.session.params` |
| `2026-06-24 08:13:25` | `cowrie.command.input` |
| `2026-06-24 08:13:25` | `cowrie.log.closed` |
| `2026-06-24 08:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26af73cc4ee8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:14 |
| **Last Seen** | 2026-06-24 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:14:13` | `cowrie.session.connect` |
| `2026-06-24 08:14:13` | `cowrie.client.version` |
| `2026-06-24 08:14:13` | `cowrie.client.kex` |
| `2026-06-24 08:14:14` | `cowrie.login.success` |
| `2026-06-24 08:14:14` | `cowrie.session.params` |
| `2026-06-24 08:14:14` | `cowrie.command.input` |
| `2026-06-24 08:14:14` | `cowrie.log.closed` |
| `2026-06-24 08:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36a3ad5695f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:15 |
| **Last Seen** | 2026-06-24 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:15:01` | `cowrie.session.connect` |
| `2026-06-24 08:15:01` | `cowrie.client.version` |
| `2026-06-24 08:15:01` | `cowrie.client.kex` |
| `2026-06-24 08:15:01` | `cowrie.login.success` |
| `2026-06-24 08:15:02` | `cowrie.session.params` |
| `2026-06-24 08:15:02` | `cowrie.command.input` |
| `2026-06-24 08:15:02` | `cowrie.log.closed` |
| `2026-06-24 08:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fb47d9d11e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:15 |
| **Last Seen** | 2026-06-24 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:15:47` | `cowrie.session.connect` |
| `2026-06-24 08:15:47` | `cowrie.client.version` |
| `2026-06-24 08:15:47` | `cowrie.client.kex` |
| `2026-06-24 08:15:48` | `cowrie.login.success` |
| `2026-06-24 08:15:48` | `cowrie.session.params` |
| `2026-06-24 08:15:48` | `cowrie.command.input` |
| `2026-06-24 08:15:48` | `cowrie.log.closed` |
| `2026-06-24 08:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4961e045036c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:16 |
| **Last Seen** | 2026-06-24 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:16:34` | `cowrie.session.connect` |
| `2026-06-24 08:16:34` | `cowrie.client.version` |
| `2026-06-24 08:16:34` | `cowrie.client.kex` |
| `2026-06-24 08:16:34` | `cowrie.login.success` |
| `2026-06-24 08:16:35` | `cowrie.session.params` |
| `2026-06-24 08:16:35` | `cowrie.command.input` |
| `2026-06-24 08:16:35` | `cowrie.log.closed` |
| `2026-06-24 08:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821716f96d5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:17 |
| **Last Seen** | 2026-06-24 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:17:21` | `cowrie.session.connect` |
| `2026-06-24 08:17:21` | `cowrie.client.version` |
| `2026-06-24 08:17:22` | `cowrie.client.kex` |
| `2026-06-24 08:17:22` | `cowrie.login.success` |
| `2026-06-24 08:17:23` | `cowrie.session.params` |
| `2026-06-24 08:17:23` | `cowrie.command.input` |
| `2026-06-24 08:17:23` | `cowrie.log.closed` |
| `2026-06-24 08:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bc0947c5712

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:18 |
| **Last Seen** | 2026-06-24 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:18:09` | `cowrie.session.connect` |
| `2026-06-24 08:18:09` | `cowrie.client.version` |
| `2026-06-24 08:18:09` | `cowrie.client.kex` |
| `2026-06-24 08:18:10` | `cowrie.login.success` |
| `2026-06-24 08:18:10` | `cowrie.session.params` |
| `2026-06-24 08:18:10` | `cowrie.command.input` |
| `2026-06-24 08:18:10` | `cowrie.log.closed` |
| `2026-06-24 08:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77975f0efe13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:18 |
| **Last Seen** | 2026-06-24 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:18:59` | `cowrie.session.connect` |
| `2026-06-24 08:18:59` | `cowrie.client.version` |
| `2026-06-24 08:18:59` | `cowrie.client.kex` |
| `2026-06-24 08:18:59` | `cowrie.login.success` |
| `2026-06-24 08:19:00` | `cowrie.session.params` |
| `2026-06-24 08:19:00` | `cowrie.command.input` |
| `2026-06-24 08:19:00` | `cowrie.log.closed` |
| `2026-06-24 08:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965a2c2fa454

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:19 |
| **Last Seen** | 2026-06-24 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:19:49` | `cowrie.session.connect` |
| `2026-06-24 08:19:49` | `cowrie.client.version` |
| `2026-06-24 08:19:49` | `cowrie.client.kex` |
| `2026-06-24 08:19:49` | `cowrie.login.success` |
| `2026-06-24 08:19:50` | `cowrie.session.params` |
| `2026-06-24 08:19:50` | `cowrie.command.input` |
| `2026-06-24 08:19:50` | `cowrie.log.closed` |
| `2026-06-24 08:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a4c44a9f62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:20 |
| **Last Seen** | 2026-06-24 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:20:42` | `cowrie.session.connect` |
| `2026-06-24 08:20:42` | `cowrie.client.version` |
| `2026-06-24 08:20:42` | `cowrie.client.kex` |
| `2026-06-24 08:20:42` | `cowrie.login.success` |
| `2026-06-24 08:20:43` | `cowrie.session.params` |
| `2026-06-24 08:20:43` | `cowrie.command.input` |
| `2026-06-24 08:20:43` | `cowrie.log.closed` |
| `2026-06-24 08:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53639fc31f32

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 08:20 |
| **Last Seen** | 2026-06-24 08:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:20:58` | `cowrie.session.connect` |
| `2026-06-24 08:21:00` | `cowrie.client.version` |
| `2026-06-24 08:21:00` | `cowrie.client.kex` |
| `2026-06-24 08:21:06` | `cowrie.login.success` |
| `2026-06-24 08:21:09` | `cowrie.session.params` |
| `2026-06-24 08:21:09` | `cowrie.command.input` |
| `2026-06-24 08:21:11` | `cowrie.log.closed` |
| `2026-06-24 08:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198831758bcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:21 |
| **Last Seen** | 2026-06-24 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:21:28` | `cowrie.session.connect` |
| `2026-06-24 08:21:28` | `cowrie.client.version` |
| `2026-06-24 08:21:28` | `cowrie.client.kex` |
| `2026-06-24 08:21:29` | `cowrie.login.success` |
| `2026-06-24 08:21:29` | `cowrie.session.params` |
| `2026-06-24 08:21:29` | `cowrie.command.input` |
| `2026-06-24 08:21:30` | `cowrie.log.closed` |
| `2026-06-24 08:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75d5803b118

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:22 |
| **Last Seen** | 2026-06-24 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:22:16` | `cowrie.session.connect` |
| `2026-06-24 08:22:16` | `cowrie.client.version` |
| `2026-06-24 08:22:16` | `cowrie.client.kex` |
| `2026-06-24 08:22:16` | `cowrie.login.success` |
| `2026-06-24 08:22:17` | `cowrie.session.params` |
| `2026-06-24 08:22:17` | `cowrie.command.input` |
| `2026-06-24 08:22:17` | `cowrie.log.closed` |
| `2026-06-24 08:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72205f82292

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:23 |
| **Last Seen** | 2026-06-24 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:23:03` | `cowrie.session.connect` |
| `2026-06-24 08:23:03` | `cowrie.client.version` |
| `2026-06-24 08:23:03` | `cowrie.client.kex` |
| `2026-06-24 08:23:03` | `cowrie.login.success` |
| `2026-06-24 08:23:04` | `cowrie.session.params` |
| `2026-06-24 08:23:04` | `cowrie.command.input` |
| `2026-06-24 08:23:04` | `cowrie.log.closed` |
| `2026-06-24 08:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5331df5e004

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:23 |
| **Last Seen** | 2026-06-24 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:23:53` | `cowrie.session.connect` |
| `2026-06-24 08:23:53` | `cowrie.client.version` |
| `2026-06-24 08:23:53` | `cowrie.client.kex` |
| `2026-06-24 08:23:53` | `cowrie.login.success` |
| `2026-06-24 08:23:54` | `cowrie.session.params` |
| `2026-06-24 08:23:54` | `cowrie.command.input` |
| `2026-06-24 08:23:54` | `cowrie.log.closed` |
| `2026-06-24 08:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c99c3af6d4ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:24 |
| **Last Seen** | 2026-06-24 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:24:43` | `cowrie.session.connect` |
| `2026-06-24 08:24:43` | `cowrie.client.version` |
| `2026-06-24 08:24:43` | `cowrie.client.kex` |
| `2026-06-24 08:24:44` | `cowrie.login.success` |
| `2026-06-24 08:24:45` | `cowrie.session.params` |
| `2026-06-24 08:24:45` | `cowrie.command.input` |
| `2026-06-24 08:24:45` | `cowrie.log.closed` |
| `2026-06-24 08:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c32b61c562

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:25 |
| **Last Seen** | 2026-06-24 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:25:34` | `cowrie.session.connect` |
| `2026-06-24 08:25:34` | `cowrie.client.version` |
| `2026-06-24 08:25:34` | `cowrie.client.kex` |
| `2026-06-24 08:25:35` | `cowrie.login.success` |
| `2026-06-24 08:25:35` | `cowrie.session.params` |
| `2026-06-24 08:25:35` | `cowrie.command.input` |
| `2026-06-24 08:25:36` | `cowrie.log.closed` |
| `2026-06-24 08:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877757a22e1b

| Field | Detail |
|---|---|
| **Source IP** | `223.197.103[.]19` |
| **First Seen** | 2026-06-24 08:25 |
| **Last Seen** | 2026-06-24 08:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:25:38` | `cowrie.session.connect` |
| `2026-06-24 08:25:38` | `cowrie.client.version` |
| `2026-06-24 08:25:38` | `cowrie.client.kex` |
| `2026-06-24 08:25:39` | `cowrie.login.success` |
| `2026-06-24 08:25:40` | `cowrie.session.params` |
| `2026-06-24 08:25:40` | `cowrie.command.input` |
| `2026-06-24 08:25:40` | `cowrie.log.closed` |
| `2026-06-24 08:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.103[.]19` to AbuseIPDB if not already reported
- [ ] Block `223.197.103[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0064e30688b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:26 |
| **Last Seen** | 2026-06-24 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:26:28` | `cowrie.session.connect` |
| `2026-06-24 08:26:28` | `cowrie.client.version` |
| `2026-06-24 08:26:28` | `cowrie.client.kex` |
| `2026-06-24 08:26:28` | `cowrie.login.success` |
| `2026-06-24 08:26:29` | `cowrie.session.params` |
| `2026-06-24 08:26:29` | `cowrie.command.input` |
| `2026-06-24 08:26:29` | `cowrie.log.closed` |
| `2026-06-24 08:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d74ada04c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:27 |
| **Last Seen** | 2026-06-24 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:27:19` | `cowrie.session.connect` |
| `2026-06-24 08:27:19` | `cowrie.client.version` |
| `2026-06-24 08:27:19` | `cowrie.client.kex` |
| `2026-06-24 08:27:20` | `cowrie.login.success` |
| `2026-06-24 08:27:21` | `cowrie.session.params` |
| `2026-06-24 08:27:21` | `cowrie.command.input` |
| `2026-06-24 08:27:21` | `cowrie.log.closed` |
| `2026-06-24 08:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fcd8d4667c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:28 |
| **Last Seen** | 2026-06-24 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:28:07` | `cowrie.session.connect` |
| `2026-06-24 08:28:07` | `cowrie.client.version` |
| `2026-06-24 08:28:08` | `cowrie.client.kex` |
| `2026-06-24 08:28:08` | `cowrie.login.success` |
| `2026-06-24 08:28:08` | `cowrie.session.params` |
| `2026-06-24 08:28:08` | `cowrie.command.input` |
| `2026-06-24 08:28:09` | `cowrie.log.closed` |
| `2026-06-24 08:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b5d9b7b9bc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:28 |
| **Last Seen** | 2026-06-24 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:28:55` | `cowrie.session.connect` |
| `2026-06-24 08:28:55` | `cowrie.client.version` |
| `2026-06-24 08:28:55` | `cowrie.client.kex` |
| `2026-06-24 08:28:55` | `cowrie.login.success` |
| `2026-06-24 08:28:56` | `cowrie.session.params` |
| `2026-06-24 08:28:56` | `cowrie.command.input` |
| `2026-06-24 08:28:56` | `cowrie.log.closed` |
| `2026-06-24 08:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab4f6aabac44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:29 |
| **Last Seen** | 2026-06-24 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:29:43` | `cowrie.session.connect` |
| `2026-06-24 08:29:43` | `cowrie.client.version` |
| `2026-06-24 08:29:44` | `cowrie.client.kex` |
| `2026-06-24 08:29:44` | `cowrie.login.success` |
| `2026-06-24 08:29:45` | `cowrie.session.params` |
| `2026-06-24 08:29:45` | `cowrie.command.input` |
| `2026-06-24 08:29:45` | `cowrie.log.closed` |
| `2026-06-24 08:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10cdd1cc2f05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:30 |
| **Last Seen** | 2026-06-24 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:30:37` | `cowrie.session.connect` |
| `2026-06-24 08:30:37` | `cowrie.client.version` |
| `2026-06-24 08:30:37` | `cowrie.client.kex` |
| `2026-06-24 08:30:37` | `cowrie.login.success` |
| `2026-06-24 08:30:38` | `cowrie.session.params` |
| `2026-06-24 08:30:38` | `cowrie.command.input` |
| `2026-06-24 08:30:38` | `cowrie.log.closed` |
| `2026-06-24 08:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530538ea69a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:31 |
| **Last Seen** | 2026-06-24 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:31:29` | `cowrie.session.connect` |
| `2026-06-24 08:31:29` | `cowrie.client.version` |
| `2026-06-24 08:31:29` | `cowrie.client.kex` |
| `2026-06-24 08:31:29` | `cowrie.login.success` |
| `2026-06-24 08:31:30` | `cowrie.session.params` |
| `2026-06-24 08:31:30` | `cowrie.command.input` |
| `2026-06-24 08:31:30` | `cowrie.log.closed` |
| `2026-06-24 08:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e55995476b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:32 |
| **Last Seen** | 2026-06-24 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:32:18` | `cowrie.session.connect` |
| `2026-06-24 08:32:18` | `cowrie.client.version` |
| `2026-06-24 08:32:18` | `cowrie.client.kex` |
| `2026-06-24 08:32:19` | `cowrie.login.success` |
| `2026-06-24 08:32:19` | `cowrie.session.params` |
| `2026-06-24 08:32:19` | `cowrie.command.input` |
| `2026-06-24 08:32:19` | `cowrie.log.closed` |
| `2026-06-24 08:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f0299f5f13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:33 |
| **Last Seen** | 2026-06-24 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:33:07` | `cowrie.session.connect` |
| `2026-06-24 08:33:07` | `cowrie.client.version` |
| `2026-06-24 08:33:08` | `cowrie.client.kex` |
| `2026-06-24 08:33:08` | `cowrie.login.success` |
| `2026-06-24 08:33:09` | `cowrie.session.params` |
| `2026-06-24 08:33:09` | `cowrie.command.input` |
| `2026-06-24 08:33:09` | `cowrie.log.closed` |
| `2026-06-24 08:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60ca474acee2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:33 |
| **Last Seen** | 2026-06-24 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:33:55` | `cowrie.session.connect` |
| `2026-06-24 08:33:55` | `cowrie.client.version` |
| `2026-06-24 08:33:56` | `cowrie.client.kex` |
| `2026-06-24 08:33:56` | `cowrie.login.success` |
| `2026-06-24 08:33:57` | `cowrie.session.params` |
| `2026-06-24 08:33:57` | `cowrie.command.input` |
| `2026-06-24 08:33:57` | `cowrie.log.closed` |
| `2026-06-24 08:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791309a41207

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:34 |
| **Last Seen** | 2026-06-24 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:34:46` | `cowrie.session.connect` |
| `2026-06-24 08:34:46` | `cowrie.client.version` |
| `2026-06-24 08:34:47` | `cowrie.client.kex` |
| `2026-06-24 08:34:47` | `cowrie.login.success` |
| `2026-06-24 08:34:48` | `cowrie.session.params` |
| `2026-06-24 08:34:48` | `cowrie.command.input` |
| `2026-06-24 08:34:48` | `cowrie.log.closed` |
| `2026-06-24 08:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d23d5718c13

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 08:34 |
| **Last Seen** | 2026-06-24 08:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:34:59` | `cowrie.session.connect` |
| `2026-06-24 08:35:00` | `cowrie.client.version` |
| `2026-06-24 08:35:00` | `cowrie.client.kex` |
| `2026-06-24 08:35:07` | `cowrie.login.success` |
| `2026-06-24 08:35:10` | `cowrie.session.params` |
| `2026-06-24 08:35:10` | `cowrie.command.input` |
| `2026-06-24 08:35:12` | `cowrie.log.closed` |
| `2026-06-24 08:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723c74aa6592

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:35 |
| **Last Seen** | 2026-06-24 08:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:35:38` | `cowrie.session.connect` |
| `2026-06-24 08:35:38` | `cowrie.client.version` |
| `2026-06-24 08:35:38` | `cowrie.client.kex` |
| `2026-06-24 08:35:38` | `cowrie.login.success` |
| `2026-06-24 08:35:39` | `cowrie.session.params` |
| `2026-06-24 08:35:39` | `cowrie.command.input` |
| `2026-06-24 08:35:39` | `cowrie.log.closed` |
| `2026-06-24 08:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1e4e263939

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:36 |
| **Last Seen** | 2026-06-24 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:36:26` | `cowrie.session.connect` |
| `2026-06-24 08:36:26` | `cowrie.client.version` |
| `2026-06-24 08:36:26` | `cowrie.client.kex` |
| `2026-06-24 08:36:26` | `cowrie.login.success` |
| `2026-06-24 08:36:27` | `cowrie.session.params` |
| `2026-06-24 08:36:27` | `cowrie.command.input` |
| `2026-06-24 08:36:27` | `cowrie.log.closed` |
| `2026-06-24 08:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc078499bef9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:37 |
| **Last Seen** | 2026-06-24 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:37:14` | `cowrie.session.connect` |
| `2026-06-24 08:37:14` | `cowrie.client.version` |
| `2026-06-24 08:37:14` | `cowrie.client.kex` |
| `2026-06-24 08:37:15` | `cowrie.login.success` |
| `2026-06-24 08:37:16` | `cowrie.session.params` |
| `2026-06-24 08:37:16` | `cowrie.command.input` |
| `2026-06-24 08:37:16` | `cowrie.log.closed` |
| `2026-06-24 08:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46050b4933bc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:38 |
| **Last Seen** | 2026-06-24 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:38:03` | `cowrie.session.connect` |
| `2026-06-24 08:38:03` | `cowrie.client.version` |
| `2026-06-24 08:38:04` | `cowrie.client.kex` |
| `2026-06-24 08:38:04` | `cowrie.login.success` |
| `2026-06-24 08:38:05` | `cowrie.session.params` |
| `2026-06-24 08:38:05` | `cowrie.command.input` |
| `2026-06-24 08:38:05` | `cowrie.log.closed` |
| `2026-06-24 08:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3e1bf9f4db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:38 |
| **Last Seen** | 2026-06-24 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:38:53` | `cowrie.session.connect` |
| `2026-06-24 08:38:53` | `cowrie.client.version` |
| `2026-06-24 08:38:53` | `cowrie.client.kex` |
| `2026-06-24 08:38:53` | `cowrie.login.success` |
| `2026-06-24 08:38:54` | `cowrie.session.params` |
| `2026-06-24 08:38:54` | `cowrie.command.input` |
| `2026-06-24 08:38:54` | `cowrie.log.closed` |
| `2026-06-24 08:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22754f6988d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:39 |
| **Last Seen** | 2026-06-24 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:39:41` | `cowrie.session.connect` |
| `2026-06-24 08:39:41` | `cowrie.client.version` |
| `2026-06-24 08:39:41` | `cowrie.client.kex` |
| `2026-06-24 08:39:42` | `cowrie.login.success` |
| `2026-06-24 08:39:42` | `cowrie.session.params` |
| `2026-06-24 08:39:42` | `cowrie.command.input` |
| `2026-06-24 08:39:43` | `cowrie.log.closed` |
| `2026-06-24 08:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27661a3d53e2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:40 |
| **Last Seen** | 2026-06-24 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:40:33` | `cowrie.session.connect` |
| `2026-06-24 08:40:33` | `cowrie.client.version` |
| `2026-06-24 08:40:33` | `cowrie.client.kex` |
| `2026-06-24 08:40:33` | `cowrie.login.success` |
| `2026-06-24 08:40:34` | `cowrie.session.params` |
| `2026-06-24 08:40:34` | `cowrie.command.input` |
| `2026-06-24 08:40:34` | `cowrie.log.closed` |
| `2026-06-24 08:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9c64c919a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:41 |
| **Last Seen** | 2026-06-24 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:41:28` | `cowrie.session.connect` |
| `2026-06-24 08:41:28` | `cowrie.client.version` |
| `2026-06-24 08:41:28` | `cowrie.client.kex` |
| `2026-06-24 08:41:28` | `cowrie.login.success` |
| `2026-06-24 08:41:29` | `cowrie.session.params` |
| `2026-06-24 08:41:29` | `cowrie.command.input` |
| `2026-06-24 08:41:29` | `cowrie.log.closed` |
| `2026-06-24 08:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8205650dec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:42 |
| **Last Seen** | 2026-06-24 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:42:18` | `cowrie.session.connect` |
| `2026-06-24 08:42:18` | `cowrie.client.version` |
| `2026-06-24 08:42:18` | `cowrie.client.kex` |
| `2026-06-24 08:42:19` | `cowrie.login.success` |
| `2026-06-24 08:42:19` | `cowrie.session.params` |
| `2026-06-24 08:42:19` | `cowrie.command.input` |
| `2026-06-24 08:42:20` | `cowrie.log.closed` |
| `2026-06-24 08:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb64b96e0155

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:43 |
| **Last Seen** | 2026-06-24 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:43:12` | `cowrie.session.connect` |
| `2026-06-24 08:43:12` | `cowrie.client.version` |
| `2026-06-24 08:43:12` | `cowrie.client.kex` |
| `2026-06-24 08:43:12` | `cowrie.login.success` |
| `2026-06-24 08:43:13` | `cowrie.session.params` |
| `2026-06-24 08:43:13` | `cowrie.command.input` |
| `2026-06-24 08:43:13` | `cowrie.log.closed` |
| `2026-06-24 08:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c23cf5c5f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:44 |
| **Last Seen** | 2026-06-24 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:44:00` | `cowrie.session.connect` |
| `2026-06-24 08:44:00` | `cowrie.client.version` |
| `2026-06-24 08:44:00` | `cowrie.client.kex` |
| `2026-06-24 08:44:00` | `cowrie.login.success` |
| `2026-06-24 08:44:01` | `cowrie.session.params` |
| `2026-06-24 08:44:01` | `cowrie.command.input` |
| `2026-06-24 08:44:01` | `cowrie.log.closed` |
| `2026-06-24 08:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aef0d5ab13a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:44 |
| **Last Seen** | 2026-06-24 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:44:49` | `cowrie.session.connect` |
| `2026-06-24 08:44:49` | `cowrie.client.version` |
| `2026-06-24 08:44:49` | `cowrie.client.kex` |
| `2026-06-24 08:44:50` | `cowrie.login.success` |
| `2026-06-24 08:44:50` | `cowrie.session.params` |
| `2026-06-24 08:44:50` | `cowrie.command.input` |
| `2026-06-24 08:44:50` | `cowrie.log.closed` |
| `2026-06-24 08:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3e76f5a76d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:45 |
| **Last Seen** | 2026-06-24 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:45:39` | `cowrie.session.connect` |
| `2026-06-24 08:45:39` | `cowrie.client.version` |
| `2026-06-24 08:45:39` | `cowrie.client.kex` |
| `2026-06-24 08:45:39` | `cowrie.login.success` |
| `2026-06-24 08:45:40` | `cowrie.session.params` |
| `2026-06-24 08:45:40` | `cowrie.command.input` |
| `2026-06-24 08:45:40` | `cowrie.log.closed` |
| `2026-06-24 08:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c5de9cbc2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:46 |
| **Last Seen** | 2026-06-24 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:46:27` | `cowrie.session.connect` |
| `2026-06-24 08:46:27` | `cowrie.client.version` |
| `2026-06-24 08:46:27` | `cowrie.client.kex` |
| `2026-06-24 08:46:28` | `cowrie.login.success` |
| `2026-06-24 08:46:28` | `cowrie.session.params` |
| `2026-06-24 08:46:28` | `cowrie.command.input` |
| `2026-06-24 08:46:28` | `cowrie.log.closed` |
| `2026-06-24 08:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b5529d53f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:47 |
| **Last Seen** | 2026-06-24 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:47:17` | `cowrie.session.connect` |
| `2026-06-24 08:47:17` | `cowrie.client.version` |
| `2026-06-24 08:47:17` | `cowrie.client.kex` |
| `2026-06-24 08:47:18` | `cowrie.login.success` |
| `2026-06-24 08:47:18` | `cowrie.session.params` |
| `2026-06-24 08:47:18` | `cowrie.command.input` |
| `2026-06-24 08:47:18` | `cowrie.log.closed` |
| `2026-06-24 08:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973ebed1ab4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:48 |
| **Last Seen** | 2026-06-24 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:48:10` | `cowrie.session.connect` |
| `2026-06-24 08:48:10` | `cowrie.client.version` |
| `2026-06-24 08:48:10` | `cowrie.client.kex` |
| `2026-06-24 08:48:11` | `cowrie.login.success` |
| `2026-06-24 08:48:11` | `cowrie.session.params` |
| `2026-06-24 08:48:11` | `cowrie.command.input` |
| `2026-06-24 08:48:12` | `cowrie.log.closed` |
| `2026-06-24 08:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8694c883432e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:49 |
| **Last Seen** | 2026-06-24 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:49:05` | `cowrie.session.connect` |
| `2026-06-24 08:49:05` | `cowrie.client.version` |
| `2026-06-24 08:49:05` | `cowrie.client.kex` |
| `2026-06-24 08:49:05` | `cowrie.login.success` |
| `2026-06-24 08:49:06` | `cowrie.session.params` |
| `2026-06-24 08:49:06` | `cowrie.command.input` |
| `2026-06-24 08:49:06` | `cowrie.log.closed` |
| `2026-06-24 08:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189ed91f44a1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 08:49 |
| **Last Seen** | 2026-06-24 08:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:49:11` | `cowrie.session.connect` |
| `2026-06-24 08:49:13` | `cowrie.client.version` |
| `2026-06-24 08:49:13` | `cowrie.client.kex` |
| `2026-06-24 08:49:20` | `cowrie.login.success` |
| `2026-06-24 08:49:23` | `cowrie.session.params` |
| `2026-06-24 08:49:23` | `cowrie.command.input` |
| `2026-06-24 08:49:25` | `cowrie.log.closed` |
| `2026-06-24 08:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1915ccbfc530

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:49 |
| **Last Seen** | 2026-06-24 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:49:55` | `cowrie.session.connect` |
| `2026-06-24 08:49:55` | `cowrie.client.version` |
| `2026-06-24 08:49:55` | `cowrie.client.kex` |
| `2026-06-24 08:49:55` | `cowrie.login.success` |
| `2026-06-24 08:49:56` | `cowrie.session.params` |
| `2026-06-24 08:49:56` | `cowrie.command.input` |
| `2026-06-24 08:49:56` | `cowrie.log.closed` |
| `2026-06-24 08:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bb0dc460c00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:50 |
| **Last Seen** | 2026-06-24 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:50:48` | `cowrie.session.connect` |
| `2026-06-24 08:50:48` | `cowrie.client.version` |
| `2026-06-24 08:50:48` | `cowrie.client.kex` |
| `2026-06-24 08:50:48` | `cowrie.login.success` |
| `2026-06-24 08:50:49` | `cowrie.session.params` |
| `2026-06-24 08:50:49` | `cowrie.command.input` |
| `2026-06-24 08:50:49` | `cowrie.log.closed` |
| `2026-06-24 08:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c2e22214d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:51 |
| **Last Seen** | 2026-06-24 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:51:40` | `cowrie.session.connect` |
| `2026-06-24 08:51:40` | `cowrie.client.version` |
| `2026-06-24 08:51:40` | `cowrie.client.kex` |
| `2026-06-24 08:51:40` | `cowrie.login.success` |
| `2026-06-24 08:51:41` | `cowrie.session.params` |
| `2026-06-24 08:51:41` | `cowrie.command.input` |
| `2026-06-24 08:51:41` | `cowrie.log.closed` |
| `2026-06-24 08:51:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0ea2336b48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:52 |
| **Last Seen** | 2026-06-24 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:52:30` | `cowrie.session.connect` |
| `2026-06-24 08:52:30` | `cowrie.client.version` |
| `2026-06-24 08:52:30` | `cowrie.client.kex` |
| `2026-06-24 08:52:30` | `cowrie.login.success` |
| `2026-06-24 08:52:31` | `cowrie.session.params` |
| `2026-06-24 08:52:31` | `cowrie.command.input` |
| `2026-06-24 08:52:31` | `cowrie.log.closed` |
| `2026-06-24 08:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a833283015ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:53 |
| **Last Seen** | 2026-06-24 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:53:19` | `cowrie.session.connect` |
| `2026-06-24 08:53:19` | `cowrie.client.version` |
| `2026-06-24 08:53:19` | `cowrie.client.kex` |
| `2026-06-24 08:53:19` | `cowrie.login.success` |
| `2026-06-24 08:53:20` | `cowrie.session.params` |
| `2026-06-24 08:53:20` | `cowrie.command.input` |
| `2026-06-24 08:53:20` | `cowrie.log.closed` |
| `2026-06-24 08:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537d3ce5fe79

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 08:54 |
| **Last Seen** | 2026-06-24 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 08:54:10` | `cowrie.session.connect` |
| `2026-06-24 08:54:10` | `cowrie.client.version` |
| `2026-06-24 08:54:10` | `cowrie.client.kex` |
| `2026-06-24 08:54:11` | `cowrie.login.success` |
| `2026-06-24 08:54:12` | `cowrie.session.params` |
| `2026-06-24 08:54:12` | `cowrie.command.input` |
| `2026-06-24 08:54:12` | `cowrie.log.closed` |
| `2026-06-24 08:54:12` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **137** | 2026-06-24 06:55 | 2026-06-24 08:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `104.199.1[.]98` | **30** | 2026-06-24 08:11 | 2026-06-24 08:11 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **3** | 2026-06-24 07:01 | 2026-06-24 08:52 | 4m | 0 | `T1592` | 🟢 LOW |
| `220.160.32[.]79` | **3** | 2026-06-24 08:36 | 2026-06-24 08:45 | 6m | 0 | `T1592` | 🟢 LOW |
| `182.43.22[.]64` | **2** | 2026-06-24 08:24 | 2026-06-24 08:26 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.143.162[.]210` | **2** | 2026-06-24 08:15 | 2026-06-24 08:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `220.197.14[.]60` | 1 | 2026-06-24 08:49 | 2026-06-24 08:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-06-24 07:44 | 2026-06-24 07:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-24 07:03 | 2026-06-24 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-24 06:58 | 2026-06-24 06:58 | 35s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-06-24 07:35 | 2026-06-24 07:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.208.139[.]201` | 1 | 2026-06-24 08:48 | 2026-06-24 08:48 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (31 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **21/73** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `220.160.32[.]79` | CN | CHINANET Fujian province network | **100** ⚠️ | 4 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `111.77.115[.]116` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 2 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `220.197.14[.]60` | CN | China Unicom | **100** ⚠️ | 11 |
| `185.65.202[.]199` | DE | LLC IT-service | **100** ⚠️ | 8 |
| `43.110.37[.]217` | US | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 31 |
| `85.208.139[.]201` | DE | HOST TELECOM LTD | **100** ⚠️ | 0 |
| `3.143.162[.]210` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 164 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 158 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 2 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 348 cases |
| Tool 34  | Credential Extractor        | ✅ 159 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 31 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 158 priority case(s) shown individually · 12 recon entry/entries in table (6 group(s) consolidating 177 session(s)).

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
_Report time: 2026-06-24T10:55:38Z_

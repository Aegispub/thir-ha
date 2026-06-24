# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-24 |
| **Generated At** | 2026-06-24T20:00:42Z |
| **Shift Time** | 20:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **314** |
| Confirmed Threats | **304** |
| False Positives Filtered | **10** (3.2%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **7** |
| High Severity Cases | **161** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **153** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **166** |
| Unique Credential Pairs | **156** |
| Unique Usernames | **84** |
| Unique Passwords | **135** |
| Successful Auth Pairs | **158** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 60 |
| `ubuntu` | 10 |
| `admin` | 7 |
| `user` | 4 |
| `dell` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 13 |
| `LeitboGi0ro` | 5 |
| `` | 4 |
| `123@@@` | 3 |
| `111111` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `admin` | `` | 4 |
| `root` | `123@@@` | 3 |
| `root` | `smo@@kkklss` | 2 |
| `xushibin` | `xu66` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `xushibin` | `xu66` | `209.99.185.59` | 2026-06-24T16:55:45 |
| `hsc20` | `hsc4223429Hsc2021@thu` | `209.99.185.59` | 2026-06-24T16:56:38 |
| `oracle` | `123qazwsx` | `209.99.185.59` | 2026-06-24T16:57:30 |
| `cajas8` | `cajas8` | `209.99.185.59` | 2026-06-24T16:58:22 |
| `dinyu` | `micah941777` | `209.99.185.59` | 2026-06-24T16:59:15 |
| `root` | `Qwerty` | `209.99.185.59` | 2026-06-24T17:00:10 |
| `xguest` | `123456` | `209.99.185.59` | 2026-06-24T17:01:05 |
| `admin` | `pgj-heu05HQM=bMvz` | `209.99.185.59` | 2026-06-24T17:02:00 |
| `testtest` | `testtest` | `209.99.185.59` | 2026-06-24T17:02:54 |
| `emart` | `emart` | `209.99.185.59` | 2026-06-24T17:03:47 |
| `root` | `pass7` | `45.205.1.42` | 2026-06-24T17:04:29 |
| `ubuntu` | `ubuntu12` | `209.99.185.59` | 2026-06-24T17:04:39 |
| `root` | `c.20fmq0ofk1` | `209.99.185.59` | 2026-06-24T17:05:33 |
| `yangyan` | `yangyan` | `209.99.185.59` | 2026-06-24T17:06:26 |
| `postgres` | `senha` | `209.99.185.59` | 2026-06-24T17:07:21 |
| `root` | `QAZWSX123` | `209.99.185.59` | 2026-06-24T17:08:16 |
| `gpadmin` | `gpadmin123` | `209.99.185.59` | 2026-06-24T17:09:12 |
| `testch` | `testch` | `209.99.185.59` | 2026-06-24T17:10:08 |
| `test` | `asdf1234` | `209.99.185.59` | 2026-06-24T17:11:03 |
| `xcy` | `xcy123456` | `209.99.185.59` | 2026-06-24T17:11:59 |
| `root` | `TheBestIsp2019` | `209.99.185.59` | 2026-06-24T17:12:56 |
| `xspeng` | `xspeng` | `209.99.185.59` | 2026-06-24T17:13:54 |
| `user` | `Abc123` | `209.99.185.59` | 2026-06-24T17:14:51 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-24T17:15:17 |
| `root` | `mobilegsm` | `209.99.185.59` | 2026-06-24T17:15:47 |
| `youngrae` | `young3` | `209.99.185.59` | 2026-06-24T17:16:42 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-24T17:16:58 |
| `root` | `upload12345` | `209.99.185.59` | 2026-06-24T17:17:36 |
| `root` | `Welcome` | `45.205.1.42` | 2026-06-24T17:18:23 |
| `root` | `marmarram` | `209.99.185.59` | 2026-06-24T17:18:32 |
| `xzz` | `xzz20` | `209.99.185.59` | 2026-06-24T17:19:28 |
| `hr` | `111111` | `209.99.185.59` | 2026-06-24T17:20:23 |
| `root` | `qwerty21` | `209.99.185.59` | 2026-06-24T17:21:19 |
| `root` | `!root` | `193.32.162.84` | 2026-06-24T17:22:22 |
| `sj` | `GSJ2128.` | `209.99.185.59` | 2026-06-24T17:22:36 |
| `xzk` | `xzk` | `209.99.185.59` | 2026-06-24T17:23:31 |
| `root` | `111111` | `193.32.162.84` | 2026-06-24T17:24:22 |
| `zhangwei5` | `zhangwei5` | `209.99.185.59` | 2026-06-24T17:24:26 |
| `cgd` | `cgd123456` | `209.99.185.59` | 2026-06-24T17:25:23 |
| `root` | `123123` | `193.32.162.84` | 2026-06-24T17:26:22 |
| `root` | `kali` | `209.99.185.59` | 2026-06-24T17:26:22 |
| `fanxiazeng` | `fanxiazeng` | `209.99.185.59` | 2026-06-24T17:27:19 |
| `yangliusha20` | `yangliusha20` | `209.99.185.59` | 2026-06-24T17:28:16 |
| `root` | `123321` | `193.32.162.84` | 2026-06-24T17:28:21 |
| `user` | `resu` | `209.99.185.59` | 2026-06-24T17:29:12 |
| `msfdev` | `msfdev` | `209.99.185.59` | 2026-06-24T17:30:08 |
| `root` | `1234` | `193.32.162.84` | 2026-06-24T17:30:20 |
| `root` | `!@#$12` | `209.99.185.59` | 2026-06-24T17:31:05 |
| `eesfq` | `eesfq8403` | `209.99.185.59` | 2026-06-24T17:32:03 |
| `root` | `12345` | `193.32.162.84` | 2026-06-24T17:32:18 |
| `ubuntu` | `abc1234567` | `45.205.1.42` | 2026-06-24T17:32:32 |
| `xiey` | `xiey` | `209.99.185.59` | 2026-06-24T17:33:04 |
| `root` | `999999999` | `209.99.185.59` | 2026-06-24T17:34:03 |
| `version` | `123456` | `209.99.185.59` | 2026-06-24T17:35:02 |
| `danny` | `danny` | `209.99.185.59` | 2026-06-24T17:36:01 |
| `root` | `1234567` | `193.32.162.84` | 2026-06-24T17:36:04 |
| `user` | `user321` | `209.99.185.59` | 2026-06-24T17:37:00 |
| `root` | `12345678` | `193.32.162.84` | 2026-06-24T17:37:53 |
| `zhx` | `123456` | `209.99.185.59` | 2026-06-24T17:38:01 |
| `root` | `local` | `209.99.185.59` | 2026-06-24T17:39:03 |
| `hadoop` | `hadoop123` | `209.99.185.59` | 2026-06-24T17:40:04 |
| `root` | `123qwe!@#QWE` | `209.99.185.59` | 2026-06-24T17:41:04 |
| `root` | `qwertasdfg` | `209.99.185.59` | 2026-06-24T17:42:05 |
| `songyx` | `songyuxiang` | `209.99.185.59` | 2026-06-24T17:43:05 |
| `xuweilin` | `123` | `209.99.185.59` | 2026-06-24T17:44:10 |
| `benfeng` | `xubenfeng@159` | `209.99.185.59` | 2026-06-24T17:45:16 |
| `root` | `silusroot` | `209.99.185.59` | 2026-06-24T17:46:20 |
| `root` | `root1234` | `45.205.1.42` | 2026-06-24T17:46:38 |
| `backup` | `1234567` | `209.99.185.59` | 2026-06-24T17:47:23 |
| `postfix` | `postfix` | `209.99.185.59` | 2026-06-24T17:48:24 |
| `admin` | `123123` | `209.99.185.59` | 2026-06-24T17:49:26 |
| `dell` | `Dell@2020` | `209.99.185.59` | 2026-06-24T17:50:40 |
| `ld` | `6226` | `209.99.185.59` | 2026-06-24T17:51:46 |
| `web1` | `web1` | `209.99.185.59` | 2026-06-24T17:52:51 |
| `tomcat` | `123456` | `209.99.185.59` | 2026-06-24T17:53:55 |
| `uzivatel` | `uzivatel` | `209.99.185.59` | 2026-06-24T17:54:58 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-24T17:55:19 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-24T17:55:19 |
| `root` | `Admin1qaz!QAZ` | `209.99.185.59` | 2026-06-24T17:56:03 |
| `wjw` | `123456` | `209.99.185.59` | 2026-06-24T17:57:07 |
| `root` | `xiaochen` | `209.99.185.59` | 2026-06-24T17:58:12 |
| `shcho` | `1234` | `209.99.185.59` | 2026-06-24T17:59:15 |
| `root` | `admin_123` | `209.99.185.59` | 2026-06-24T18:00:17 |
| `police` | `police` | `45.205.1.42` | 2026-06-24T18:00:45 |
| `myuser` | `123456` | `209.99.185.59` | 2026-06-24T18:00:57 |
| `root` | `root@2017` | `209.99.185.59` | 2026-06-24T18:01:38 |
| `dell` | `dell@9000` | `209.99.185.59` | 2026-06-24T18:02:19 |
| `lc` | `lc123` | `209.99.185.59` | 2026-06-24T18:03:01 |
| `sg` | `korea2019` | `209.99.185.59` | 2026-06-24T18:03:43 |
| `admin` | `admin` | `180.172.43.152` | 2026-06-24T18:03:46 |
| `yxz` | `123456` | `209.99.185.59` | 2026-06-24T18:04:27 |
| `wtliu` | `server74` | `209.99.185.59` | 2026-06-24T18:05:10 |
| `root` | `Ab123456` | `209.99.185.59` | 2026-06-24T18:05:53 |
| `root` | `qaz12qwe` | `209.99.185.59` | 2026-06-24T18:06:36 |
| `root` | `publish` | `209.99.185.59` | 2026-06-24T18:07:19 |
| `root` | `1234asdf` | `209.99.185.59` | 2026-06-24T18:08:01 |
| `root` | `Root123!@#` | `209.99.185.59` | 2026-06-24T18:08:43 |
| `Admin` | `admin` | `209.99.185.59` | 2026-06-24T18:09:26 |
| `liangyuan` | `liangyuan` | `209.99.185.59` | 2026-06-24T18:10:10 |
| `lhy` | `lhy890` | `209.99.185.59` | 2026-06-24T18:10:55 |
| `pi` | `123` | `209.99.185.59` | 2026-06-24T18:11:40 |
| `zhangsan` | `zhangsan321` | `209.99.185.59` | 2026-06-24T18:12:25 |
| `ubuntu` | `asdf1234` | `209.99.185.59` | 2026-06-24T18:13:10 |
| `gjy` | `gjy` | `209.99.185.59` | 2026-06-24T18:13:53 |
| `cpr` | `cpr` | `209.99.185.59` | 2026-06-24T18:14:38 |
| `ubuntu` | `asd123456` | `45.205.1.42` | 2026-06-24T18:14:53 |
| `wocloud` | `wocloud` | `209.99.185.59` | 2026-06-24T18:15:24 |
| `gestcom` | `gestcom` | `209.99.185.59` | 2026-06-24T18:16:12 |
| `root` | `kkkkkk` | `209.99.185.59` | 2026-06-24T18:17:00 |
| `chen` | `Nick941226` | `209.99.185.59` | 2026-06-24T18:17:49 |
| `root` | `22` | `209.99.185.59` | 2026-06-24T18:18:36 |
| `ltsp169` | `123456` | `209.99.185.59` | 2026-06-24T18:19:25 |
| `ubuntu` | `666666` | `209.99.185.59` | 2026-06-24T18:20:12 |
| `root` | `1qaz2wsX` | `209.99.185.59` | 2026-06-24T18:21:00 |
| `root` | `12345x` | `209.99.185.59` | 2026-06-24T18:21:48 |
| `root` | `Root@2016` | `209.99.185.59` | 2026-06-24T18:22:36 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-24T18:22:39 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-24T18:22:40 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-24T18:22:48 |
| `mic` | `mic604` | `209.99.185.59` | 2026-06-24T18:23:26 |
| `root` | `upload1234567890` | `209.99.185.59` | 2026-06-24T18:24:16 |
| `cs21-nik` | `Nk1234` | `209.99.185.59` | 2026-06-24T18:25:12 |
| `ubuntu` | `qwerty1234` | `209.99.185.59` | 2026-06-24T18:26:05 |
| `shsong` | `123456` | `209.99.185.59` | 2026-06-24T18:26:54 |
| `root` | `P@ssword1234567890` | `209.99.185.59` | 2026-06-24T18:27:43 |
| `wly` | `wly` | `209.99.185.59` | 2026-06-24T18:28:33 |
| `shell` | `shell` | `45.205.1.42` | 2026-06-24T18:28:59 |
| `zijin` | `zzj956959688` | `209.99.185.59` | 2026-06-24T18:29:23 |
| `postgres` | `333333` | `209.99.185.59` | 2026-06-24T18:30:14 |
| `chenhao` | `/]$6kbnz` | `209.99.185.59` | 2026-06-24T18:31:05 |
| `test` | `qwer` | `209.99.185.59` | 2026-06-24T18:31:56 |
| `root` | `root@8000` | `209.99.185.59` | 2026-06-24T18:32:46 |
| `amax` | `amax123` | `209.99.185.59` | 2026-06-24T18:33:35 |
| `qzj` | `123456` | `209.99.185.59` | 2026-06-24T18:34:25 |
| `robin` | `robin` | `209.99.185.59` | 2026-06-24T18:35:16 |
| `ubuntu` | `12345` | `209.99.185.59` | 2026-06-24T18:36:08 |
| `root` | `Tencent@2021` | `209.99.185.59` | 2026-06-24T18:37:02 |
| `smbuser` | `test@123` | `209.99.185.59` | 2026-06-24T18:37:54 |
| `root` | `zaq12wsxcd` | `209.99.185.59` | 2026-06-24T18:38:46 |
| `kari` | `kari` | `209.99.185.59` | 2026-06-24T18:39:37 |
| `song` | `123456` | `209.99.185.59` | 2026-06-24T18:40:28 |
| `qianmaolin` | `qianmaolin` | `209.99.185.59` | 2026-06-24T18:41:22 |
| `bsks1` | `bsks` | `209.99.185.59` | 2026-06-24T18:42:17 |
| `root` | `abc12345` | `45.205.1.42` | 2026-06-24T18:43:07 |
| `root` | `freedom` | `209.99.185.59` | 2026-06-24T18:43:16 |
| `user` | `1q2w@3e4r` | `209.99.185.59` | 2026-06-24T18:44:14 |
| `ubuntu` | `hadoop123456` | `209.99.185.59` | 2026-06-24T18:45:07 |
| `root` | `l3tm3in` | `209.99.185.59` | 2026-06-24T18:45:58 |
| `esroot` | `esroot` | `209.99.185.59` | 2026-06-24T18:46:50 |
| `secre4` | `secre4` | `209.99.185.59` | 2026-06-24T18:47:44 |
| `ubuntu` | `developer123456` | `209.99.185.59` | 2026-06-24T18:48:37 |
| `zhangsan` | `111111` | `209.99.185.59` | 2026-06-24T18:49:32 |
| `ubuntu` | `Muiemuie123!` | `209.99.185.59` | 2026-06-24T18:50:25 |
| `operador` | `123456` | `209.99.185.59` | 2026-06-24T18:51:18 |
| `webmaster` | `1qaz@WSX3edc` | `209.99.185.59` | 2026-06-24T18:52:11 |
| `dell` | `dell@8000` | `209.99.185.59` | 2026-06-24T18:53:02 |
| `root` | `WordPass&2021` | `209.99.185.59` | 2026-06-24T18:53:56 |
| `steam` | `password` | `209.99.185.59` | 2026-06-24T18:54:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **314** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 154 |
| Paramiko (Python) | 10 |
| libssh | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 142 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 142 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |

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
```
echo '!root' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `193.32.162.84`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **12** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS402253` | SKN Subnet & Telecom Ltd | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (161)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5906ff1df5eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:55 |
| **Last Seen** | 2026-06-24 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:55:45` | `cowrie.session.connect` |
| `2026-06-24 16:55:45` | `cowrie.client.version` |
| `2026-06-24 16:55:45` | `cowrie.client.kex` |
| `2026-06-24 16:55:45` | `cowrie.login.success` |
| `2026-06-24 16:55:46` | `cowrie.session.params` |
| `2026-06-24 16:55:46` | `cowrie.command.input` |
| `2026-06-24 16:55:46` | `cowrie.log.closed` |
| `2026-06-24 16:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f3c0180a75

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:56 |
| **Last Seen** | 2026-06-24 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:56:37` | `cowrie.session.connect` |
| `2026-06-24 16:56:37` | `cowrie.client.version` |
| `2026-06-24 16:56:37` | `cowrie.client.kex` |
| `2026-06-24 16:56:38` | `cowrie.login.success` |
| `2026-06-24 16:56:39` | `cowrie.session.params` |
| `2026-06-24 16:56:39` | `cowrie.command.input` |
| `2026-06-24 16:56:39` | `cowrie.log.closed` |
| `2026-06-24 16:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37339d8682f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:57 |
| **Last Seen** | 2026-06-24 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:57:29` | `cowrie.session.connect` |
| `2026-06-24 16:57:29` | `cowrie.client.version` |
| `2026-06-24 16:57:30` | `cowrie.client.kex` |
| `2026-06-24 16:57:30` | `cowrie.login.success` |
| `2026-06-24 16:57:31` | `cowrie.session.params` |
| `2026-06-24 16:57:31` | `cowrie.command.input` |
| `2026-06-24 16:57:31` | `cowrie.log.closed` |
| `2026-06-24 16:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88abe7b38710

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:58 |
| **Last Seen** | 2026-06-24 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:58:21` | `cowrie.session.connect` |
| `2026-06-24 16:58:21` | `cowrie.client.version` |
| `2026-06-24 16:58:21` | `cowrie.client.kex` |
| `2026-06-24 16:58:22` | `cowrie.login.success` |
| `2026-06-24 16:58:22` | `cowrie.session.params` |
| `2026-06-24 16:58:22` | `cowrie.command.input` |
| `2026-06-24 16:58:22` | `cowrie.log.closed` |
| `2026-06-24 16:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86fc57a897b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 16:59 |
| **Last Seen** | 2026-06-24 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 16:59:14` | `cowrie.session.connect` |
| `2026-06-24 16:59:14` | `cowrie.client.version` |
| `2026-06-24 16:59:14` | `cowrie.client.kex` |
| `2026-06-24 16:59:15` | `cowrie.login.success` |
| `2026-06-24 16:59:16` | `cowrie.session.params` |
| `2026-06-24 16:59:16` | `cowrie.command.input` |
| `2026-06-24 16:59:16` | `cowrie.log.closed` |
| `2026-06-24 16:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2172790a358f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:00 |
| **Last Seen** | 2026-06-24 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:00:10` | `cowrie.session.connect` |
| `2026-06-24 17:00:10` | `cowrie.client.version` |
| `2026-06-24 17:00:10` | `cowrie.client.kex` |
| `2026-06-24 17:00:10` | `cowrie.login.success` |
| `2026-06-24 17:00:11` | `cowrie.session.params` |
| `2026-06-24 17:00:11` | `cowrie.command.input` |
| `2026-06-24 17:00:11` | `cowrie.log.closed` |
| `2026-06-24 17:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1999ba3535

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:01 |
| **Last Seen** | 2026-06-24 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:01:05` | `cowrie.session.connect` |
| `2026-06-24 17:01:05` | `cowrie.client.version` |
| `2026-06-24 17:01:05` | `cowrie.client.kex` |
| `2026-06-24 17:01:05` | `cowrie.login.success` |
| `2026-06-24 17:01:06` | `cowrie.session.params` |
| `2026-06-24 17:01:06` | `cowrie.command.input` |
| `2026-06-24 17:01:06` | `cowrie.log.closed` |
| `2026-06-24 17:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c80b15f9c34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:02 |
| **Last Seen** | 2026-06-24 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:02:00` | `cowrie.session.connect` |
| `2026-06-24 17:02:00` | `cowrie.client.version` |
| `2026-06-24 17:02:00` | `cowrie.client.kex` |
| `2026-06-24 17:02:00` | `cowrie.login.success` |
| `2026-06-24 17:02:01` | `cowrie.session.params` |
| `2026-06-24 17:02:01` | `cowrie.command.input` |
| `2026-06-24 17:02:01` | `cowrie.log.closed` |
| `2026-06-24 17:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39b8abd2fd6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:02 |
| **Last Seen** | 2026-06-24 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:02:53` | `cowrie.session.connect` |
| `2026-06-24 17:02:53` | `cowrie.client.version` |
| `2026-06-24 17:02:53` | `cowrie.client.kex` |
| `2026-06-24 17:02:54` | `cowrie.login.success` |
| `2026-06-24 17:02:54` | `cowrie.session.params` |
| `2026-06-24 17:02:54` | `cowrie.command.input` |
| `2026-06-24 17:02:55` | `cowrie.log.closed` |
| `2026-06-24 17:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd80ca188f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:03 |
| **Last Seen** | 2026-06-24 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:03:46` | `cowrie.session.connect` |
| `2026-06-24 17:03:46` | `cowrie.client.version` |
| `2026-06-24 17:03:47` | `cowrie.client.kex` |
| `2026-06-24 17:03:47` | `cowrie.login.success` |
| `2026-06-24 17:03:48` | `cowrie.session.params` |
| `2026-06-24 17:03:48` | `cowrie.command.input` |
| `2026-06-24 17:03:48` | `cowrie.log.closed` |
| `2026-06-24 17:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41f4edec50b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 17:04 |
| **Last Seen** | 2026-06-24 17:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:04:21` | `cowrie.session.connect` |
| `2026-06-24 17:04:23` | `cowrie.client.version` |
| `2026-06-24 17:04:23` | `cowrie.client.kex` |
| `2026-06-24 17:04:29` | `cowrie.login.success` |
| `2026-06-24 17:04:33` | `cowrie.session.params` |
| `2026-06-24 17:04:33` | `cowrie.command.input` |
| `2026-06-24 17:04:35` | `cowrie.log.closed` |
| `2026-06-24 17:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1255d04cd09d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:04 |
| **Last Seen** | 2026-06-24 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:04:39` | `cowrie.session.connect` |
| `2026-06-24 17:04:39` | `cowrie.client.version` |
| `2026-06-24 17:04:39` | `cowrie.client.kex` |
| `2026-06-24 17:04:39` | `cowrie.login.success` |
| `2026-06-24 17:04:40` | `cowrie.session.params` |
| `2026-06-24 17:04:40` | `cowrie.command.input` |
| `2026-06-24 17:04:40` | `cowrie.log.closed` |
| `2026-06-24 17:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2c11ef4af4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:05 |
| **Last Seen** | 2026-06-24 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:05:32` | `cowrie.session.connect` |
| `2026-06-24 17:05:32` | `cowrie.client.version` |
| `2026-06-24 17:05:32` | `cowrie.client.kex` |
| `2026-06-24 17:05:33` | `cowrie.login.success` |
| `2026-06-24 17:05:34` | `cowrie.session.params` |
| `2026-06-24 17:05:34` | `cowrie.command.input` |
| `2026-06-24 17:05:34` | `cowrie.log.closed` |
| `2026-06-24 17:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e7aa626a1f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:06 |
| **Last Seen** | 2026-06-24 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:06:26` | `cowrie.session.connect` |
| `2026-06-24 17:06:26` | `cowrie.client.version` |
| `2026-06-24 17:06:26` | `cowrie.client.kex` |
| `2026-06-24 17:06:26` | `cowrie.login.success` |
| `2026-06-24 17:06:27` | `cowrie.session.params` |
| `2026-06-24 17:06:27` | `cowrie.command.input` |
| `2026-06-24 17:06:27` | `cowrie.log.closed` |
| `2026-06-24 17:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1431a75b2c99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:07 |
| **Last Seen** | 2026-06-24 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:07:20` | `cowrie.session.connect` |
| `2026-06-24 17:07:20` | `cowrie.client.version` |
| `2026-06-24 17:07:20` | `cowrie.client.kex` |
| `2026-06-24 17:07:21` | `cowrie.login.success` |
| `2026-06-24 17:07:22` | `cowrie.session.params` |
| `2026-06-24 17:07:22` | `cowrie.command.input` |
| `2026-06-24 17:07:22` | `cowrie.log.closed` |
| `2026-06-24 17:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8d981f5914

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:08 |
| **Last Seen** | 2026-06-24 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:08:16` | `cowrie.session.connect` |
| `2026-06-24 17:08:16` | `cowrie.client.version` |
| `2026-06-24 17:08:16` | `cowrie.client.kex` |
| `2026-06-24 17:08:16` | `cowrie.login.success` |
| `2026-06-24 17:08:17` | `cowrie.session.params` |
| `2026-06-24 17:08:17` | `cowrie.command.input` |
| `2026-06-24 17:08:17` | `cowrie.log.closed` |
| `2026-06-24 17:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e280fa486ae4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:09 |
| **Last Seen** | 2026-06-24 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:09:11` | `cowrie.session.connect` |
| `2026-06-24 17:09:11` | `cowrie.client.version` |
| `2026-06-24 17:09:11` | `cowrie.client.kex` |
| `2026-06-24 17:09:12` | `cowrie.login.success` |
| `2026-06-24 17:09:12` | `cowrie.session.params` |
| `2026-06-24 17:09:12` | `cowrie.command.input` |
| `2026-06-24 17:09:13` | `cowrie.log.closed` |
| `2026-06-24 17:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe76f3bb927

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:10 |
| **Last Seen** | 2026-06-24 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:10:07` | `cowrie.session.connect` |
| `2026-06-24 17:10:07` | `cowrie.client.version` |
| `2026-06-24 17:10:07` | `cowrie.client.kex` |
| `2026-06-24 17:10:08` | `cowrie.login.success` |
| `2026-06-24 17:10:08` | `cowrie.session.params` |
| `2026-06-24 17:10:08` | `cowrie.command.input` |
| `2026-06-24 17:10:09` | `cowrie.log.closed` |
| `2026-06-24 17:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed6bbfff5d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:11 |
| **Last Seen** | 2026-06-24 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:11:03` | `cowrie.session.connect` |
| `2026-06-24 17:11:03` | `cowrie.client.version` |
| `2026-06-24 17:11:03` | `cowrie.client.kex` |
| `2026-06-24 17:11:03` | `cowrie.login.success` |
| `2026-06-24 17:11:04` | `cowrie.session.params` |
| `2026-06-24 17:11:04` | `cowrie.command.input` |
| `2026-06-24 17:11:04` | `cowrie.log.closed` |
| `2026-06-24 17:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acfe6f042424

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:11 |
| **Last Seen** | 2026-06-24 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:11:58` | `cowrie.session.connect` |
| `2026-06-24 17:11:58` | `cowrie.client.version` |
| `2026-06-24 17:11:59` | `cowrie.client.kex` |
| `2026-06-24 17:11:59` | `cowrie.login.success` |
| `2026-06-24 17:11:59` | `cowrie.session.params` |
| `2026-06-24 17:11:59` | `cowrie.command.input` |
| `2026-06-24 17:12:00` | `cowrie.log.closed` |
| `2026-06-24 17:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a3a82c18ca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:12 |
| **Last Seen** | 2026-06-24 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:12:56` | `cowrie.session.connect` |
| `2026-06-24 17:12:56` | `cowrie.client.version` |
| `2026-06-24 17:12:56` | `cowrie.client.kex` |
| `2026-06-24 17:12:56` | `cowrie.login.success` |
| `2026-06-24 17:12:57` | `cowrie.session.params` |
| `2026-06-24 17:12:57` | `cowrie.command.input` |
| `2026-06-24 17:12:57` | `cowrie.log.closed` |
| `2026-06-24 17:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1576de4cafac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:13 |
| **Last Seen** | 2026-06-24 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:13:53` | `cowrie.session.connect` |
| `2026-06-24 17:13:53` | `cowrie.client.version` |
| `2026-06-24 17:13:53` | `cowrie.client.kex` |
| `2026-06-24 17:13:54` | `cowrie.login.success` |
| `2026-06-24 17:13:54` | `cowrie.session.params` |
| `2026-06-24 17:13:54` | `cowrie.command.input` |
| `2026-06-24 17:13:55` | `cowrie.log.closed` |
| `2026-06-24 17:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdb623e1531

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:14 |
| **Last Seen** | 2026-06-24 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:14:51` | `cowrie.session.connect` |
| `2026-06-24 17:14:51` | `cowrie.client.version` |
| `2026-06-24 17:14:51` | `cowrie.client.kex` |
| `2026-06-24 17:14:51` | `cowrie.login.success` |
| `2026-06-24 17:14:52` | `cowrie.session.params` |
| `2026-06-24 17:14:52` | `cowrie.command.input` |
| `2026-06-24 17:14:52` | `cowrie.log.closed` |
| `2026-06-24 17:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1bc9e56133

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-24 17:15 |
| **Last Seen** | 2026-06-24 17:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:15:16` | `cowrie.session.connect` |
| `2026-06-24 17:15:16` | `cowrie.client.version` |
| `2026-06-24 17:15:16` | `cowrie.client.kex` |
| `2026-06-24 17:15:17` | `cowrie.login.success` |
| `2026-06-24 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efafd12c9053

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:15 |
| **Last Seen** | 2026-06-24 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:15:47` | `cowrie.session.connect` |
| `2026-06-24 17:15:47` | `cowrie.client.version` |
| `2026-06-24 17:15:47` | `cowrie.client.kex` |
| `2026-06-24 17:15:47` | `cowrie.login.success` |
| `2026-06-24 17:15:48` | `cowrie.session.params` |
| `2026-06-24 17:15:48` | `cowrie.command.input` |
| `2026-06-24 17:15:48` | `cowrie.log.closed` |
| `2026-06-24 17:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073fe82b7ca3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:16 |
| **Last Seen** | 2026-06-24 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:16:42` | `cowrie.session.connect` |
| `2026-06-24 17:16:42` | `cowrie.client.version` |
| `2026-06-24 17:16:42` | `cowrie.client.kex` |
| `2026-06-24 17:16:42` | `cowrie.login.success` |
| `2026-06-24 17:16:43` | `cowrie.session.params` |
| `2026-06-24 17:16:43` | `cowrie.command.input` |
| `2026-06-24 17:16:43` | `cowrie.log.closed` |
| `2026-06-24 17:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47720a02bde1

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-24 17:16 |
| **Last Seen** | 2026-06-24 17:19 |
| **Session Duration** | 140s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:16:57` | `cowrie.session.connect` |
| `2026-06-24 17:16:57` | `cowrie.client.version` |
| `2026-06-24 17:16:57` | `cowrie.client.kex` |
| `2026-06-24 17:16:58` | `cowrie.login.success` |
| `2026-06-24 17:16:59` | `cowrie.session.file_upload` |
| `2026-06-24 17:17:00` | `cowrie.session.params` |
| `2026-06-24 17:17:00` | `cowrie.command.input` |
| `2026-06-24 17:17:00` | `cowrie.command.input` |
| `2026-06-24 17:17:00` | `cowrie.command.input` |
| `2026-06-24 17:17:00` | `cowrie.command.failed` |
| `2026-06-24 17:17:00` | `cowrie.log.closed` |
| `2026-06-24 17:17:01` | `cowrie.session.params` |
| `2026-06-24 17:17:01` | `cowrie.command.input` |
| `2026-06-24 17:17:01` | `cowrie.log.closed` |
| `2026-06-24 17:17:02` | `cowrie.session.params` |
| `2026-06-24 17:17:02` | `cowrie.command.input` |
| `2026-06-24 17:17:02` | `cowrie.log.closed` |
| `2026-06-24 17:17:03` | `cowrie.session.params` |
| `2026-06-24 17:17:03` | `cowrie.command.input` |
| `2026-06-24 17:17:03` | `cowrie.command.failed` |
| `2026-06-24 17:17:03` | `cowrie.command.failed` |
| `2026-06-24 17:18:04` | `cowrie.session.params` |
| `2026-06-24 17:18:04` | `cowrie.command.input` |
| `2026-06-24 17:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253cb9c3e6c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:17 |
| **Last Seen** | 2026-06-24 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:17:36` | `cowrie.session.connect` |
| `2026-06-24 17:17:36` | `cowrie.client.version` |
| `2026-06-24 17:17:36` | `cowrie.client.kex` |
| `2026-06-24 17:17:36` | `cowrie.login.success` |
| `2026-06-24 17:17:37` | `cowrie.session.params` |
| `2026-06-24 17:17:37` | `cowrie.command.input` |
| `2026-06-24 17:17:37` | `cowrie.log.closed` |
| `2026-06-24 17:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de18643afc7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 17:18 |
| **Last Seen** | 2026-06-24 17:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:18:16` | `cowrie.session.connect` |
| `2026-06-24 17:18:17` | `cowrie.client.version` |
| `2026-06-24 17:18:17` | `cowrie.client.kex` |
| `2026-06-24 17:18:23` | `cowrie.login.success` |
| `2026-06-24 17:18:28` | `cowrie.session.params` |
| `2026-06-24 17:18:28` | `cowrie.command.input` |
| `2026-06-24 17:18:29` | `cowrie.log.closed` |
| `2026-06-24 17:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fce7c920e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:18 |
| **Last Seen** | 2026-06-24 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:18:32` | `cowrie.session.connect` |
| `2026-06-24 17:18:32` | `cowrie.client.version` |
| `2026-06-24 17:18:32` | `cowrie.client.kex` |
| `2026-06-24 17:18:32` | `cowrie.login.success` |
| `2026-06-24 17:18:33` | `cowrie.session.params` |
| `2026-06-24 17:18:33` | `cowrie.command.input` |
| `2026-06-24 17:18:33` | `cowrie.log.closed` |
| `2026-06-24 17:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f8e628e265

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-24 17:18 |
| **Last Seen** | 2026-06-24 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:18:38` | `cowrie.session.connect` |
| `2026-06-24 17:18:38` | `cowrie.client.version` |
| `2026-06-24 17:18:38` | `cowrie.client.kex` |
| `2026-06-24 17:18:38` | `cowrie.login.success` |
| `2026-06-24 17:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1196ddf5057a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:19 |
| **Last Seen** | 2026-06-24 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:19:27` | `cowrie.session.connect` |
| `2026-06-24 17:19:27` | `cowrie.client.version` |
| `2026-06-24 17:19:27` | `cowrie.client.kex` |
| `2026-06-24 17:19:28` | `cowrie.login.success` |
| `2026-06-24 17:19:29` | `cowrie.session.params` |
| `2026-06-24 17:19:29` | `cowrie.command.input` |
| `2026-06-24 17:19:29` | `cowrie.log.closed` |
| `2026-06-24 17:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-117a9a3f6832

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-24 17:19 |
| **Last Seen** | 2026-06-24 17:22 |
| **Session Duration** | 139s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:19:43` | `cowrie.session.connect` |
| `2026-06-24 17:19:43` | `cowrie.client.version` |
| `2026-06-24 17:19:43` | `cowrie.client.kex` |
| `2026-06-24 17:19:43` | `cowrie.login.success` |
| `2026-06-24 17:19:45` | `cowrie.session.file_upload` |
| `2026-06-24 17:19:46` | `cowrie.session.params` |
| `2026-06-24 17:19:46` | `cowrie.command.input` |
| `2026-06-24 17:19:46` | `cowrie.command.input` |
| `2026-06-24 17:19:46` | `cowrie.command.input` |
| `2026-06-24 17:19:46` | `cowrie.command.failed` |
| `2026-06-24 17:19:46` | `cowrie.log.closed` |
| `2026-06-24 17:19:47` | `cowrie.session.params` |
| `2026-06-24 17:19:47` | `cowrie.command.input` |
| `2026-06-24 17:19:47` | `cowrie.log.closed` |
| `2026-06-24 17:19:47` | `cowrie.session.params` |
| `2026-06-24 17:19:47` | `cowrie.command.input` |
| `2026-06-24 17:19:48` | `cowrie.log.closed` |
| `2026-06-24 17:19:48` | `cowrie.session.params` |
| `2026-06-24 17:19:48` | `cowrie.command.input` |
| `2026-06-24 17:19:48` | `cowrie.command.failed` |
| `2026-06-24 17:19:48` | `cowrie.command.failed` |
| `2026-06-24 17:20:50` | `cowrie.session.params` |
| `2026-06-24 17:20:50` | `cowrie.command.input` |
| `2026-06-24 17:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e589720a3224

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:20 |
| **Last Seen** | 2026-06-24 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:20:23` | `cowrie.session.connect` |
| `2026-06-24 17:20:23` | `cowrie.client.version` |
| `2026-06-24 17:20:23` | `cowrie.client.kex` |
| `2026-06-24 17:20:23` | `cowrie.login.success` |
| `2026-06-24 17:20:24` | `cowrie.session.params` |
| `2026-06-24 17:20:24` | `cowrie.command.input` |
| `2026-06-24 17:20:24` | `cowrie.log.closed` |
| `2026-06-24 17:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffca60b7d98a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:21 |
| **Last Seen** | 2026-06-24 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:21:18` | `cowrie.session.connect` |
| `2026-06-24 17:21:18` | `cowrie.client.version` |
| `2026-06-24 17:21:18` | `cowrie.client.kex` |
| `2026-06-24 17:21:19` | `cowrie.login.success` |
| `2026-06-24 17:21:19` | `cowrie.session.params` |
| `2026-06-24 17:21:19` | `cowrie.command.input` |
| `2026-06-24 17:21:20` | `cowrie.log.closed` |
| `2026-06-24 17:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89bc9e07455e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:22 |
| **Last Seen** | 2026-06-24 17:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '!root' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:22:19` | `cowrie.session.connect` |
| `2026-06-24 17:22:19` | `cowrie.client.version` |
| `2026-06-24 17:22:19` | `cowrie.client.kex` |
| `2026-06-24 17:22:22` | `cowrie.login.success` |
| `2026-06-24 17:22:26` | `cowrie.session.params` |
| `2026-06-24 17:22:26` | `cowrie.command.input` |
| `2026-06-24 17:22:26` | `cowrie.command.input` |
| `2026-06-24 17:22:26` | `cowrie.command.input` |
| `2026-06-24 17:22:26` | `cowrie.command.input` |
| `2026-06-24 17:22:27` | `cowrie.log.closed` |
| `2026-06-24 17:22:29` | `cowrie.session.params` |
| `2026-06-24 17:22:29` | `cowrie.command.input` |
| `2026-06-24 17:22:29` | `cowrie.command.input` |
| `2026-06-24 17:22:29` | `cowrie.command.failed` |
| `2026-06-24 17:22:29` | `cowrie.command.failed` |
| `2026-06-24 17:22:29` | `cowrie.command.failed` |
| `2026-06-24 17:22:29` | `cowrie.command.failed` |
| `2026-06-24 17:22:32` | `cowrie.log.closed` |
| `2026-06-24 17:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9be79cb57b3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:22 |
| **Last Seen** | 2026-06-24 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:22:36` | `cowrie.session.connect` |
| `2026-06-24 17:22:36` | `cowrie.client.version` |
| `2026-06-24 17:22:36` | `cowrie.client.kex` |
| `2026-06-24 17:22:36` | `cowrie.login.success` |
| `2026-06-24 17:22:37` | `cowrie.session.params` |
| `2026-06-24 17:22:37` | `cowrie.command.input` |
| `2026-06-24 17:22:37` | `cowrie.log.closed` |
| `2026-06-24 17:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38323f3ea65

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:23 |
| **Last Seen** | 2026-06-24 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:23:30` | `cowrie.session.connect` |
| `2026-06-24 17:23:30` | `cowrie.client.version` |
| `2026-06-24 17:23:31` | `cowrie.client.kex` |
| `2026-06-24 17:23:31` | `cowrie.login.success` |
| `2026-06-24 17:23:32` | `cowrie.session.params` |
| `2026-06-24 17:23:32` | `cowrie.command.input` |
| `2026-06-24 17:23:32` | `cowrie.log.closed` |
| `2026-06-24 17:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0511115571a5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:24 |
| **Last Seen** | 2026-06-24 17:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '111111' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:24:19` | `cowrie.session.connect` |
| `2026-06-24 17:24:19` | `cowrie.client.version` |
| `2026-06-24 17:24:19` | `cowrie.client.kex` |
| `2026-06-24 17:24:22` | `cowrie.login.success` |
| `2026-06-24 17:24:24` | `cowrie.session.params` |
| `2026-06-24 17:24:24` | `cowrie.command.input` |
| `2026-06-24 17:24:24` | `cowrie.command.input` |
| `2026-06-24 17:24:24` | `cowrie.command.input` |
| `2026-06-24 17:24:24` | `cowrie.command.input` |
| `2026-06-24 17:24:25` | `cowrie.log.closed` |
| `2026-06-24 17:24:27` | `cowrie.session.params` |
| `2026-06-24 17:24:27` | `cowrie.command.input` |
| `2026-06-24 17:24:27` | `cowrie.command.input` |
| `2026-06-24 17:24:27` | `cowrie.command.failed` |
| `2026-06-24 17:24:27` | `cowrie.command.failed` |
| `2026-06-24 17:24:27` | `cowrie.command.failed` |
| `2026-06-24 17:24:27` | `cowrie.command.failed` |
| `2026-06-24 17:24:28` | `cowrie.log.closed` |
| `2026-06-24 17:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41b51ac638d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:24 |
| **Last Seen** | 2026-06-24 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:24:25` | `cowrie.session.connect` |
| `2026-06-24 17:24:25` | `cowrie.client.version` |
| `2026-06-24 17:24:26` | `cowrie.client.kex` |
| `2026-06-24 17:24:26` | `cowrie.login.success` |
| `2026-06-24 17:24:27` | `cowrie.session.params` |
| `2026-06-24 17:24:27` | `cowrie.command.input` |
| `2026-06-24 17:24:27` | `cowrie.log.closed` |
| `2026-06-24 17:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95323dad59e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:25 |
| **Last Seen** | 2026-06-24 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:25:23` | `cowrie.session.connect` |
| `2026-06-24 17:25:23` | `cowrie.client.version` |
| `2026-06-24 17:25:23` | `cowrie.client.kex` |
| `2026-06-24 17:25:23` | `cowrie.login.success` |
| `2026-06-24 17:25:24` | `cowrie.session.params` |
| `2026-06-24 17:25:24` | `cowrie.command.input` |
| `2026-06-24 17:25:24` | `cowrie.log.closed` |
| `2026-06-24 17:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68d66b7be5a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:26 |
| **Last Seen** | 2026-06-24 17:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:26:18` | `cowrie.session.connect` |
| `2026-06-24 17:26:19` | `cowrie.client.version` |
| `2026-06-24 17:26:19` | `cowrie.client.kex` |
| `2026-06-24 17:26:22` | `cowrie.login.success` |
| `2026-06-24 17:26:24` | `cowrie.session.params` |
| `2026-06-24 17:26:24` | `cowrie.command.input` |
| `2026-06-24 17:26:24` | `cowrie.command.input` |
| `2026-06-24 17:26:24` | `cowrie.command.input` |
| `2026-06-24 17:26:24` | `cowrie.command.input` |
| `2026-06-24 17:26:25` | `cowrie.log.closed` |
| `2026-06-24 17:26:28` | `cowrie.session.params` |
| `2026-06-24 17:26:28` | `cowrie.command.input` |
| `2026-06-24 17:26:28` | `cowrie.command.input` |
| `2026-06-24 17:26:28` | `cowrie.command.failed` |
| `2026-06-24 17:26:28` | `cowrie.command.failed` |
| `2026-06-24 17:26:28` | `cowrie.command.failed` |
| `2026-06-24 17:26:28` | `cowrie.command.failed` |
| `2026-06-24 17:26:28` | `cowrie.log.closed` |
| `2026-06-24 17:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ec200ea73d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:26 |
| **Last Seen** | 2026-06-24 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:26:22` | `cowrie.session.connect` |
| `2026-06-24 17:26:22` | `cowrie.client.version` |
| `2026-06-24 17:26:22` | `cowrie.client.kex` |
| `2026-06-24 17:26:22` | `cowrie.login.success` |
| `2026-06-24 17:26:23` | `cowrie.session.params` |
| `2026-06-24 17:26:23` | `cowrie.command.input` |
| `2026-06-24 17:26:23` | `cowrie.log.closed` |
| `2026-06-24 17:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301b86e297a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:27 |
| **Last Seen** | 2026-06-24 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:27:19` | `cowrie.session.connect` |
| `2026-06-24 17:27:19` | `cowrie.client.version` |
| `2026-06-24 17:27:19` | `cowrie.client.kex` |
| `2026-06-24 17:27:19` | `cowrie.login.success` |
| `2026-06-24 17:27:20` | `cowrie.session.params` |
| `2026-06-24 17:27:20` | `cowrie.command.input` |
| `2026-06-24 17:27:20` | `cowrie.log.closed` |
| `2026-06-24 17:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28611f6c7055

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:28 |
| **Last Seen** | 2026-06-24 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:28:16` | `cowrie.session.connect` |
| `2026-06-24 17:28:16` | `cowrie.client.version` |
| `2026-06-24 17:28:16` | `cowrie.client.kex` |
| `2026-06-24 17:28:16` | `cowrie.login.success` |
| `2026-06-24 17:28:17` | `cowrie.session.params` |
| `2026-06-24 17:28:17` | `cowrie.command.input` |
| `2026-06-24 17:28:17` | `cowrie.log.closed` |
| `2026-06-24 17:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c0d037e263

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:28 |
| **Last Seen** | 2026-06-24 17:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123321' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:28:18` | `cowrie.session.connect` |
| `2026-06-24 17:28:18` | `cowrie.client.version` |
| `2026-06-24 17:28:18` | `cowrie.client.kex` |
| `2026-06-24 17:28:21` | `cowrie.login.success` |
| `2026-06-24 17:28:24` | `cowrie.session.params` |
| `2026-06-24 17:28:24` | `cowrie.command.input` |
| `2026-06-24 17:28:24` | `cowrie.command.input` |
| `2026-06-24 17:28:24` | `cowrie.command.input` |
| `2026-06-24 17:28:24` | `cowrie.command.input` |
| `2026-06-24 17:28:24` | `cowrie.log.closed` |
| `2026-06-24 17:28:26` | `cowrie.session.params` |
| `2026-06-24 17:28:26` | `cowrie.command.input` |
| `2026-06-24 17:28:26` | `cowrie.command.input` |
| `2026-06-24 17:28:26` | `cowrie.command.failed` |
| `2026-06-24 17:28:26` | `cowrie.command.failed` |
| `2026-06-24 17:28:26` | `cowrie.command.failed` |
| `2026-06-24 17:28:26` | `cowrie.command.failed` |
| `2026-06-24 17:28:28` | `cowrie.log.closed` |
| `2026-06-24 17:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3375aa33acc3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:29 |
| **Last Seen** | 2026-06-24 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:29:12` | `cowrie.session.connect` |
| `2026-06-24 17:29:12` | `cowrie.client.version` |
| `2026-06-24 17:29:12` | `cowrie.client.kex` |
| `2026-06-24 17:29:12` | `cowrie.login.success` |
| `2026-06-24 17:29:13` | `cowrie.session.params` |
| `2026-06-24 17:29:13` | `cowrie.command.input` |
| `2026-06-24 17:29:13` | `cowrie.log.closed` |
| `2026-06-24 17:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8da0324557f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:30 |
| **Last Seen** | 2026-06-24 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:30:08` | `cowrie.session.connect` |
| `2026-06-24 17:30:08` | `cowrie.client.version` |
| `2026-06-24 17:30:08` | `cowrie.client.kex` |
| `2026-06-24 17:30:08` | `cowrie.login.success` |
| `2026-06-24 17:30:09` | `cowrie.session.params` |
| `2026-06-24 17:30:09` | `cowrie.command.input` |
| `2026-06-24 17:30:09` | `cowrie.log.closed` |
| `2026-06-24 17:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0261fc5f6a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:30 |
| **Last Seen** | 2026-06-24 17:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:30:17` | `cowrie.session.connect` |
| `2026-06-24 17:30:18` | `cowrie.client.version` |
| `2026-06-24 17:30:18` | `cowrie.client.kex` |
| `2026-06-24 17:30:20` | `cowrie.login.success` |
| `2026-06-24 17:30:22` | `cowrie.session.params` |
| `2026-06-24 17:30:22` | `cowrie.command.input` |
| `2026-06-24 17:30:22` | `cowrie.command.input` |
| `2026-06-24 17:30:22` | `cowrie.command.input` |
| `2026-06-24 17:30:22` | `cowrie.command.input` |
| `2026-06-24 17:30:23` | `cowrie.log.closed` |
| `2026-06-24 17:30:25` | `cowrie.session.params` |
| `2026-06-24 17:30:25` | `cowrie.command.input` |
| `2026-06-24 17:30:25` | `cowrie.command.input` |
| `2026-06-24 17:30:25` | `cowrie.command.failed` |
| `2026-06-24 17:30:25` | `cowrie.command.failed` |
| `2026-06-24 17:30:25` | `cowrie.command.failed` |
| `2026-06-24 17:30:25` | `cowrie.command.failed` |
| `2026-06-24 17:30:26` | `cowrie.log.closed` |
| `2026-06-24 17:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da17c10749d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:31 |
| **Last Seen** | 2026-06-24 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:31:04` | `cowrie.session.connect` |
| `2026-06-24 17:31:04` | `cowrie.client.version` |
| `2026-06-24 17:31:04` | `cowrie.client.kex` |
| `2026-06-24 17:31:05` | `cowrie.login.success` |
| `2026-06-24 17:31:05` | `cowrie.session.params` |
| `2026-06-24 17:31:05` | `cowrie.command.input` |
| `2026-06-24 17:31:05` | `cowrie.log.closed` |
| `2026-06-24 17:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cac023a5c7c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:32 |
| **Last Seen** | 2026-06-24 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:32:02` | `cowrie.session.connect` |
| `2026-06-24 17:32:02` | `cowrie.client.version` |
| `2026-06-24 17:32:02` | `cowrie.client.kex` |
| `2026-06-24 17:32:03` | `cowrie.login.success` |
| `2026-06-24 17:32:04` | `cowrie.session.params` |
| `2026-06-24 17:32:04` | `cowrie.command.input` |
| `2026-06-24 17:32:04` | `cowrie.log.closed` |
| `2026-06-24 17:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e7960245b3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:32 |
| **Last Seen** | 2026-06-24 17:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:32:15` | `cowrie.session.connect` |
| `2026-06-24 17:32:15` | `cowrie.client.version` |
| `2026-06-24 17:32:15` | `cowrie.client.kex` |
| `2026-06-24 17:32:18` | `cowrie.login.success` |
| `2026-06-24 17:32:20` | `cowrie.session.params` |
| `2026-06-24 17:32:20` | `cowrie.command.input` |
| `2026-06-24 17:32:20` | `cowrie.command.input` |
| `2026-06-24 17:32:20` | `cowrie.command.input` |
| `2026-06-24 17:32:20` | `cowrie.command.input` |
| `2026-06-24 17:32:21` | `cowrie.log.closed` |
| `2026-06-24 17:32:23` | `cowrie.session.params` |
| `2026-06-24 17:32:23` | `cowrie.command.input` |
| `2026-06-24 17:32:23` | `cowrie.command.input` |
| `2026-06-24 17:32:23` | `cowrie.command.failed` |
| `2026-06-24 17:32:23` | `cowrie.command.failed` |
| `2026-06-24 17:32:23` | `cowrie.command.failed` |
| `2026-06-24 17:32:23` | `cowrie.command.failed` |
| `2026-06-24 17:32:24` | `cowrie.log.closed` |
| `2026-06-24 17:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ebfee5c501

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 17:32 |
| **Last Seen** | 2026-06-24 17:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:32:24` | `cowrie.session.connect` |
| `2026-06-24 17:32:26` | `cowrie.client.version` |
| `2026-06-24 17:32:26` | `cowrie.client.kex` |
| `2026-06-24 17:32:32` | `cowrie.login.success` |
| `2026-06-24 17:32:36` | `cowrie.session.params` |
| `2026-06-24 17:32:36` | `cowrie.command.input` |
| `2026-06-24 17:32:37` | `cowrie.log.closed` |
| `2026-06-24 17:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12227fcd618

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:33 |
| **Last Seen** | 2026-06-24 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:33:03` | `cowrie.session.connect` |
| `2026-06-24 17:33:03` | `cowrie.client.version` |
| `2026-06-24 17:33:03` | `cowrie.client.kex` |
| `2026-06-24 17:33:04` | `cowrie.login.success` |
| `2026-06-24 17:33:04` | `cowrie.session.params` |
| `2026-06-24 17:33:04` | `cowrie.command.input` |
| `2026-06-24 17:33:04` | `cowrie.log.closed` |
| `2026-06-24 17:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a873684f745c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:34 |
| **Last Seen** | 2026-06-24 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:34:03` | `cowrie.session.connect` |
| `2026-06-24 17:34:03` | `cowrie.client.version` |
| `2026-06-24 17:34:03` | `cowrie.client.kex` |
| `2026-06-24 17:34:03` | `cowrie.login.success` |
| `2026-06-24 17:34:04` | `cowrie.session.params` |
| `2026-06-24 17:34:04` | `cowrie.command.input` |
| `2026-06-24 17:34:04` | `cowrie.log.closed` |
| `2026-06-24 17:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d977dedf8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:35 |
| **Last Seen** | 2026-06-24 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:35:01` | `cowrie.session.connect` |
| `2026-06-24 17:35:01` | `cowrie.client.version` |
| `2026-06-24 17:35:02` | `cowrie.client.kex` |
| `2026-06-24 17:35:02` | `cowrie.login.success` |
| `2026-06-24 17:35:03` | `cowrie.session.params` |
| `2026-06-24 17:35:03` | `cowrie.command.input` |
| `2026-06-24 17:35:03` | `cowrie.log.closed` |
| `2026-06-24 17:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27e2bb58855

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:35 |
| **Last Seen** | 2026-06-24 17:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:35:59` | `cowrie.session.connect` |
| `2026-06-24 17:36:00` | `cowrie.client.version` |
| `2026-06-24 17:36:00` | `cowrie.client.kex` |
| `2026-06-24 17:36:04` | `cowrie.login.success` |
| `2026-06-24 17:36:06` | `cowrie.session.params` |
| `2026-06-24 17:36:06` | `cowrie.command.input` |
| `2026-06-24 17:36:06` | `cowrie.command.input` |
| `2026-06-24 17:36:06` | `cowrie.command.input` |
| `2026-06-24 17:36:06` | `cowrie.command.input` |
| `2026-06-24 17:36:07` | `cowrie.log.closed` |
| `2026-06-24 17:36:09` | `cowrie.session.params` |
| `2026-06-24 17:36:09` | `cowrie.command.input` |
| `2026-06-24 17:36:09` | `cowrie.command.input` |
| `2026-06-24 17:36:09` | `cowrie.command.failed` |
| `2026-06-24 17:36:09` | `cowrie.command.failed` |
| `2026-06-24 17:36:09` | `cowrie.command.failed` |
| `2026-06-24 17:36:09` | `cowrie.command.failed` |
| `2026-06-24 17:36:10` | `cowrie.log.closed` |
| `2026-06-24 17:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2195b8769c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:36 |
| **Last Seen** | 2026-06-24 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:36:01` | `cowrie.session.connect` |
| `2026-06-24 17:36:01` | `cowrie.client.version` |
| `2026-06-24 17:36:01` | `cowrie.client.kex` |
| `2026-06-24 17:36:01` | `cowrie.login.success` |
| `2026-06-24 17:36:02` | `cowrie.session.params` |
| `2026-06-24 17:36:02` | `cowrie.command.input` |
| `2026-06-24 17:36:02` | `cowrie.log.closed` |
| `2026-06-24 17:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a58d4874c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:37 |
| **Last Seen** | 2026-06-24 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:37:00` | `cowrie.session.connect` |
| `2026-06-24 17:37:00` | `cowrie.client.version` |
| `2026-06-24 17:37:00` | `cowrie.client.kex` |
| `2026-06-24 17:37:00` | `cowrie.login.success` |
| `2026-06-24 17:37:01` | `cowrie.session.params` |
| `2026-06-24 17:37:01` | `cowrie.command.input` |
| `2026-06-24 17:37:01` | `cowrie.log.closed` |
| `2026-06-24 17:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ff96f3dfbf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-06-24 17:37 |
| **Last Seen** | 2026-06-24 17:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:37:50` | `cowrie.session.connect` |
| `2026-06-24 17:37:50` | `cowrie.client.version` |
| `2026-06-24 17:37:50` | `cowrie.client.kex` |
| `2026-06-24 17:37:53` | `cowrie.login.success` |
| `2026-06-24 17:37:56` | `cowrie.session.params` |
| `2026-06-24 17:37:56` | `cowrie.command.input` |
| `2026-06-24 17:37:56` | `cowrie.command.input` |
| `2026-06-24 17:37:56` | `cowrie.command.input` |
| `2026-06-24 17:37:56` | `cowrie.command.input` |
| `2026-06-24 17:37:57` | `cowrie.log.closed` |
| `2026-06-24 17:37:59` | `cowrie.session.params` |
| `2026-06-24 17:37:59` | `cowrie.command.input` |
| `2026-06-24 17:37:59` | `cowrie.command.input` |
| `2026-06-24 17:37:59` | `cowrie.command.failed` |
| `2026-06-24 17:37:59` | `cowrie.command.failed` |
| `2026-06-24 17:37:59` | `cowrie.command.failed` |
| `2026-06-24 17:37:59` | `cowrie.command.failed` |
| `2026-06-24 17:37:59` | `cowrie.log.closed` |
| `2026-06-24 17:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222f15fd019d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:38 |
| **Last Seen** | 2026-06-24 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:38:01` | `cowrie.session.connect` |
| `2026-06-24 17:38:01` | `cowrie.client.version` |
| `2026-06-24 17:38:01` | `cowrie.client.kex` |
| `2026-06-24 17:38:01` | `cowrie.login.success` |
| `2026-06-24 17:38:02` | `cowrie.session.params` |
| `2026-06-24 17:38:02` | `cowrie.command.input` |
| `2026-06-24 17:38:02` | `cowrie.log.closed` |
| `2026-06-24 17:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a7d71ba2de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:39 |
| **Last Seen** | 2026-06-24 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:39:02` | `cowrie.session.connect` |
| `2026-06-24 17:39:02` | `cowrie.client.version` |
| `2026-06-24 17:39:02` | `cowrie.client.kex` |
| `2026-06-24 17:39:03` | `cowrie.login.success` |
| `2026-06-24 17:39:04` | `cowrie.session.params` |
| `2026-06-24 17:39:04` | `cowrie.command.input` |
| `2026-06-24 17:39:04` | `cowrie.log.closed` |
| `2026-06-24 17:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d174715e9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:40 |
| **Last Seen** | 2026-06-24 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:40:03` | `cowrie.session.connect` |
| `2026-06-24 17:40:03` | `cowrie.client.version` |
| `2026-06-24 17:40:03` | `cowrie.client.kex` |
| `2026-06-24 17:40:04` | `cowrie.login.success` |
| `2026-06-24 17:40:04` | `cowrie.session.params` |
| `2026-06-24 17:40:04` | `cowrie.command.input` |
| `2026-06-24 17:40:04` | `cowrie.log.closed` |
| `2026-06-24 17:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c744312f1ec5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:41 |
| **Last Seen** | 2026-06-24 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:41:04` | `cowrie.session.connect` |
| `2026-06-24 17:41:04` | `cowrie.client.version` |
| `2026-06-24 17:41:04` | `cowrie.client.kex` |
| `2026-06-24 17:41:04` | `cowrie.login.success` |
| `2026-06-24 17:41:05` | `cowrie.session.params` |
| `2026-06-24 17:41:05` | `cowrie.command.input` |
| `2026-06-24 17:41:05` | `cowrie.log.closed` |
| `2026-06-24 17:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620838bbea6a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:42 |
| **Last Seen** | 2026-06-24 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:42:04` | `cowrie.session.connect` |
| `2026-06-24 17:42:04` | `cowrie.client.version` |
| `2026-06-24 17:42:04` | `cowrie.client.kex` |
| `2026-06-24 17:42:05` | `cowrie.login.success` |
| `2026-06-24 17:42:05` | `cowrie.session.params` |
| `2026-06-24 17:42:05` | `cowrie.command.input` |
| `2026-06-24 17:42:06` | `cowrie.log.closed` |
| `2026-06-24 17:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526a5bc38f92

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:43 |
| **Last Seen** | 2026-06-24 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:43:05` | `cowrie.session.connect` |
| `2026-06-24 17:43:05` | `cowrie.client.version` |
| `2026-06-24 17:43:05` | `cowrie.client.kex` |
| `2026-06-24 17:43:05` | `cowrie.login.success` |
| `2026-06-24 17:43:06` | `cowrie.session.params` |
| `2026-06-24 17:43:06` | `cowrie.command.input` |
| `2026-06-24 17:43:06` | `cowrie.log.closed` |
| `2026-06-24 17:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69fc10ff9fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:44 |
| **Last Seen** | 2026-06-24 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:44:09` | `cowrie.session.connect` |
| `2026-06-24 17:44:09` | `cowrie.client.version` |
| `2026-06-24 17:44:09` | `cowrie.client.kex` |
| `2026-06-24 17:44:10` | `cowrie.login.success` |
| `2026-06-24 17:44:10` | `cowrie.session.params` |
| `2026-06-24 17:44:10` | `cowrie.command.input` |
| `2026-06-24 17:44:11` | `cowrie.log.closed` |
| `2026-06-24 17:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a412788e5b8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:45 |
| **Last Seen** | 2026-06-24 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:45:16` | `cowrie.session.connect` |
| `2026-06-24 17:45:16` | `cowrie.client.version` |
| `2026-06-24 17:45:16` | `cowrie.client.kex` |
| `2026-06-24 17:45:16` | `cowrie.login.success` |
| `2026-06-24 17:45:17` | `cowrie.session.params` |
| `2026-06-24 17:45:17` | `cowrie.command.input` |
| `2026-06-24 17:45:17` | `cowrie.log.closed` |
| `2026-06-24 17:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c89068be7fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:46 |
| **Last Seen** | 2026-06-24 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:46:20` | `cowrie.session.connect` |
| `2026-06-24 17:46:20` | `cowrie.client.version` |
| `2026-06-24 17:46:20` | `cowrie.client.kex` |
| `2026-06-24 17:46:20` | `cowrie.login.success` |
| `2026-06-24 17:46:21` | `cowrie.session.params` |
| `2026-06-24 17:46:21` | `cowrie.command.input` |
| `2026-06-24 17:46:21` | `cowrie.log.closed` |
| `2026-06-24 17:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b13020987ee

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 17:46 |
| **Last Seen** | 2026-06-24 17:46 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:46:30` | `cowrie.session.connect` |
| `2026-06-24 17:46:32` | `cowrie.client.version` |
| `2026-06-24 17:46:32` | `cowrie.client.kex` |
| `2026-06-24 17:46:38` | `cowrie.login.success` |
| `2026-06-24 17:46:42` | `cowrie.session.params` |
| `2026-06-24 17:46:42` | `cowrie.command.input` |
| `2026-06-24 17:46:44` | `cowrie.log.closed` |
| `2026-06-24 17:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82894b1ee8ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:47 |
| **Last Seen** | 2026-06-24 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:47:22` | `cowrie.session.connect` |
| `2026-06-24 17:47:22` | `cowrie.client.version` |
| `2026-06-24 17:47:22` | `cowrie.client.kex` |
| `2026-06-24 17:47:23` | `cowrie.login.success` |
| `2026-06-24 17:47:23` | `cowrie.session.params` |
| `2026-06-24 17:47:23` | `cowrie.command.input` |
| `2026-06-24 17:47:23` | `cowrie.log.closed` |
| `2026-06-24 17:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7cd89500394

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:48 |
| **Last Seen** | 2026-06-24 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:48:24` | `cowrie.session.connect` |
| `2026-06-24 17:48:24` | `cowrie.client.version` |
| `2026-06-24 17:48:24` | `cowrie.client.kex` |
| `2026-06-24 17:48:24` | `cowrie.login.success` |
| `2026-06-24 17:48:25` | `cowrie.session.params` |
| `2026-06-24 17:48:25` | `cowrie.command.input` |
| `2026-06-24 17:48:25` | `cowrie.log.closed` |
| `2026-06-24 17:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2476e8e23351

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:49 |
| **Last Seen** | 2026-06-24 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:49:25` | `cowrie.session.connect` |
| `2026-06-24 17:49:25` | `cowrie.client.version` |
| `2026-06-24 17:49:25` | `cowrie.client.kex` |
| `2026-06-24 17:49:26` | `cowrie.login.success` |
| `2026-06-24 17:49:26` | `cowrie.session.params` |
| `2026-06-24 17:49:26` | `cowrie.command.input` |
| `2026-06-24 17:49:27` | `cowrie.log.closed` |
| `2026-06-24 17:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8972308cf2cf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:50 |
| **Last Seen** | 2026-06-24 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:50:39` | `cowrie.session.connect` |
| `2026-06-24 17:50:39` | `cowrie.client.version` |
| `2026-06-24 17:50:40` | `cowrie.client.kex` |
| `2026-06-24 17:50:40` | `cowrie.login.success` |
| `2026-06-24 17:50:41` | `cowrie.session.params` |
| `2026-06-24 17:50:41` | `cowrie.command.input` |
| `2026-06-24 17:50:41` | `cowrie.log.closed` |
| `2026-06-24 17:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19e04f6f851

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:51 |
| **Last Seen** | 2026-06-24 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:51:46` | `cowrie.session.connect` |
| `2026-06-24 17:51:46` | `cowrie.client.version` |
| `2026-06-24 17:51:46` | `cowrie.client.kex` |
| `2026-06-24 17:51:46` | `cowrie.login.success` |
| `2026-06-24 17:51:47` | `cowrie.session.params` |
| `2026-06-24 17:51:47` | `cowrie.command.input` |
| `2026-06-24 17:51:47` | `cowrie.log.closed` |
| `2026-06-24 17:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3f81652b7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:52 |
| **Last Seen** | 2026-06-24 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:52:50` | `cowrie.session.connect` |
| `2026-06-24 17:52:50` | `cowrie.client.version` |
| `2026-06-24 17:52:51` | `cowrie.client.kex` |
| `2026-06-24 17:52:51` | `cowrie.login.success` |
| `2026-06-24 17:52:52` | `cowrie.session.params` |
| `2026-06-24 17:52:52` | `cowrie.command.input` |
| `2026-06-24 17:52:52` | `cowrie.log.closed` |
| `2026-06-24 17:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e1f3f76944

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:53 |
| **Last Seen** | 2026-06-24 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:53:55` | `cowrie.session.connect` |
| `2026-06-24 17:53:55` | `cowrie.client.version` |
| `2026-06-24 17:53:55` | `cowrie.client.kex` |
| `2026-06-24 17:53:55` | `cowrie.login.success` |
| `2026-06-24 17:53:56` | `cowrie.session.params` |
| `2026-06-24 17:53:56` | `cowrie.command.input` |
| `2026-06-24 17:53:56` | `cowrie.log.closed` |
| `2026-06-24 17:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6dac0c8c817

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:54 |
| **Last Seen** | 2026-06-24 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:54:58` | `cowrie.session.connect` |
| `2026-06-24 17:54:58` | `cowrie.client.version` |
| `2026-06-24 17:54:58` | `cowrie.client.kex` |
| `2026-06-24 17:54:58` | `cowrie.login.success` |
| `2026-06-24 17:54:59` | `cowrie.session.params` |
| `2026-06-24 17:54:59` | `cowrie.command.input` |
| `2026-06-24 17:54:59` | `cowrie.log.closed` |
| `2026-06-24 17:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe218f0986d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 17:55 |
| **Last Seen** | 2026-06-24 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:55:18` | `cowrie.session.connect` |
| `2026-06-24 17:55:18` | `cowrie.client.version` |
| `2026-06-24 17:55:18` | `cowrie.client.kex` |
| `2026-06-24 17:55:19` | `cowrie.login.success` |
| `2026-06-24 17:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c7b6fbfa7a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 17:55 |
| **Last Seen** | 2026-06-24 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:55:19` | `cowrie.session.connect` |
| `2026-06-24 17:55:19` | `cowrie.client.version` |
| `2026-06-24 17:55:19` | `cowrie.client.kex` |
| `2026-06-24 17:55:19` | `cowrie.login.success` |
| `2026-06-24 17:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e6295b5b36

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:56 |
| **Last Seen** | 2026-06-24 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:56:03` | `cowrie.session.connect` |
| `2026-06-24 17:56:03` | `cowrie.client.version` |
| `2026-06-24 17:56:03` | `cowrie.client.kex` |
| `2026-06-24 17:56:03` | `cowrie.login.success` |
| `2026-06-24 17:56:04` | `cowrie.session.params` |
| `2026-06-24 17:56:04` | `cowrie.command.input` |
| `2026-06-24 17:56:04` | `cowrie.log.closed` |
| `2026-06-24 17:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b62ee5fcb4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:57 |
| **Last Seen** | 2026-06-24 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:57:07` | `cowrie.session.connect` |
| `2026-06-24 17:57:07` | `cowrie.client.version` |
| `2026-06-24 17:57:07` | `cowrie.client.kex` |
| `2026-06-24 17:57:07` | `cowrie.login.success` |
| `2026-06-24 17:57:08` | `cowrie.session.params` |
| `2026-06-24 17:57:08` | `cowrie.command.input` |
| `2026-06-24 17:57:08` | `cowrie.log.closed` |
| `2026-06-24 17:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c42a2066886

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:58 |
| **Last Seen** | 2026-06-24 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:58:12` | `cowrie.session.connect` |
| `2026-06-24 17:58:12` | `cowrie.client.version` |
| `2026-06-24 17:58:12` | `cowrie.client.kex` |
| `2026-06-24 17:58:12` | `cowrie.login.success` |
| `2026-06-24 17:58:13` | `cowrie.session.params` |
| `2026-06-24 17:58:13` | `cowrie.command.input` |
| `2026-06-24 17:58:13` | `cowrie.log.closed` |
| `2026-06-24 17:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d420cb5a5fde

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 17:59 |
| **Last Seen** | 2026-06-24 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 17:59:15` | `cowrie.session.connect` |
| `2026-06-24 17:59:15` | `cowrie.client.version` |
| `2026-06-24 17:59:15` | `cowrie.client.kex` |
| `2026-06-24 17:59:15` | `cowrie.login.success` |
| `2026-06-24 17:59:16` | `cowrie.session.params` |
| `2026-06-24 17:59:16` | `cowrie.command.input` |
| `2026-06-24 17:59:16` | `cowrie.log.closed` |
| `2026-06-24 17:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9241aed3a986

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:00 |
| **Last Seen** | 2026-06-24 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:00:16` | `cowrie.session.connect` |
| `2026-06-24 18:00:16` | `cowrie.client.version` |
| `2026-06-24 18:00:17` | `cowrie.client.kex` |
| `2026-06-24 18:00:17` | `cowrie.login.success` |
| `2026-06-24 18:00:18` | `cowrie.session.params` |
| `2026-06-24 18:00:18` | `cowrie.command.input` |
| `2026-06-24 18:00:18` | `cowrie.log.closed` |
| `2026-06-24 18:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eb3d0676cb4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 18:00 |
| **Last Seen** | 2026-06-24 18:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:00:37` | `cowrie.session.connect` |
| `2026-06-24 18:00:39` | `cowrie.client.version` |
| `2026-06-24 18:00:39` | `cowrie.client.kex` |
| `2026-06-24 18:00:45` | `cowrie.login.success` |
| `2026-06-24 18:00:49` | `cowrie.session.params` |
| `2026-06-24 18:00:49` | `cowrie.command.input` |
| `2026-06-24 18:00:50` | `cowrie.log.closed` |
| `2026-06-24 18:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f21724b513

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:00 |
| **Last Seen** | 2026-06-24 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:00:57` | `cowrie.session.connect` |
| `2026-06-24 18:00:57` | `cowrie.client.version` |
| `2026-06-24 18:00:57` | `cowrie.client.kex` |
| `2026-06-24 18:00:57` | `cowrie.login.success` |
| `2026-06-24 18:00:58` | `cowrie.session.params` |
| `2026-06-24 18:00:58` | `cowrie.command.input` |
| `2026-06-24 18:00:58` | `cowrie.log.closed` |
| `2026-06-24 18:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1981a2462ce4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:01 |
| **Last Seen** | 2026-06-24 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:01:37` | `cowrie.session.connect` |
| `2026-06-24 18:01:37` | `cowrie.client.version` |
| `2026-06-24 18:01:37` | `cowrie.client.kex` |
| `2026-06-24 18:01:38` | `cowrie.login.success` |
| `2026-06-24 18:01:39` | `cowrie.session.params` |
| `2026-06-24 18:01:39` | `cowrie.command.input` |
| `2026-06-24 18:01:39` | `cowrie.log.closed` |
| `2026-06-24 18:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb53aba9cdde

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:02 |
| **Last Seen** | 2026-06-24 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:02:19` | `cowrie.session.connect` |
| `2026-06-24 18:02:19` | `cowrie.client.version` |
| `2026-06-24 18:02:19` | `cowrie.client.kex` |
| `2026-06-24 18:02:19` | `cowrie.login.success` |
| `2026-06-24 18:02:20` | `cowrie.session.params` |
| `2026-06-24 18:02:20` | `cowrie.command.input` |
| `2026-06-24 18:02:20` | `cowrie.log.closed` |
| `2026-06-24 18:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a43174590e

| Field | Detail |
|---|---|
| **Source IP** | `180.172.43[.]152` |
| **First Seen** | 2026-06-24 18:02 |
| **Last Seen** | 2026-06-24 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:02:44` | `cowrie.session.connect` |
| `2026-06-24 18:02:45` | `cowrie.telnet.option` |
| `2026-06-24 18:02:46` | `cowrie.telnet.option` |
| `2026-06-24 18:03:46` | `cowrie.login.success` |
| `2026-06-24 18:03:47` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `180.172.43[.]152` to AbuseIPDB if not already reported
- [ ] Block `180.172.43[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f40226e0df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:03 |
| **Last Seen** | 2026-06-24 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:03:00` | `cowrie.session.connect` |
| `2026-06-24 18:03:00` | `cowrie.client.version` |
| `2026-06-24 18:03:01` | `cowrie.client.kex` |
| `2026-06-24 18:03:01` | `cowrie.login.success` |
| `2026-06-24 18:03:02` | `cowrie.session.params` |
| `2026-06-24 18:03:02` | `cowrie.command.input` |
| `2026-06-24 18:03:02` | `cowrie.log.closed` |
| `2026-06-24 18:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83aa6c6d5ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:03 |
| **Last Seen** | 2026-06-24 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:03:43` | `cowrie.session.connect` |
| `2026-06-24 18:03:43` | `cowrie.client.version` |
| `2026-06-24 18:03:43` | `cowrie.client.kex` |
| `2026-06-24 18:03:43` | `cowrie.login.success` |
| `2026-06-24 18:03:44` | `cowrie.session.params` |
| `2026-06-24 18:03:44` | `cowrie.command.input` |
| `2026-06-24 18:03:44` | `cowrie.log.closed` |
| `2026-06-24 18:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7c42e9d6d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:04 |
| **Last Seen** | 2026-06-24 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:04:26` | `cowrie.session.connect` |
| `2026-06-24 18:04:26` | `cowrie.client.version` |
| `2026-06-24 18:04:26` | `cowrie.client.kex` |
| `2026-06-24 18:04:27` | `cowrie.login.success` |
| `2026-06-24 18:04:28` | `cowrie.session.params` |
| `2026-06-24 18:04:28` | `cowrie.command.input` |
| `2026-06-24 18:04:28` | `cowrie.log.closed` |
| `2026-06-24 18:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce077eaaab35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:05 |
| **Last Seen** | 2026-06-24 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:05:09` | `cowrie.session.connect` |
| `2026-06-24 18:05:09` | `cowrie.client.version` |
| `2026-06-24 18:05:10` | `cowrie.client.kex` |
| `2026-06-24 18:05:10` | `cowrie.login.success` |
| `2026-06-24 18:05:11` | `cowrie.session.params` |
| `2026-06-24 18:05:11` | `cowrie.command.input` |
| `2026-06-24 18:05:11` | `cowrie.log.closed` |
| `2026-06-24 18:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b9b77a6075

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:05 |
| **Last Seen** | 2026-06-24 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:05:53` | `cowrie.session.connect` |
| `2026-06-24 18:05:53` | `cowrie.client.version` |
| `2026-06-24 18:05:53` | `cowrie.client.kex` |
| `2026-06-24 18:05:53` | `cowrie.login.success` |
| `2026-06-24 18:05:54` | `cowrie.session.params` |
| `2026-06-24 18:05:54` | `cowrie.command.input` |
| `2026-06-24 18:05:54` | `cowrie.log.closed` |
| `2026-06-24 18:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5735ce5918c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:06 |
| **Last Seen** | 2026-06-24 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:06:35` | `cowrie.session.connect` |
| `2026-06-24 18:06:35` | `cowrie.client.version` |
| `2026-06-24 18:06:35` | `cowrie.client.kex` |
| `2026-06-24 18:06:36` | `cowrie.login.success` |
| `2026-06-24 18:06:37` | `cowrie.session.params` |
| `2026-06-24 18:06:37` | `cowrie.command.input` |
| `2026-06-24 18:06:37` | `cowrie.log.closed` |
| `2026-06-24 18:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4eebb584b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:07 |
| **Last Seen** | 2026-06-24 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:07:18` | `cowrie.session.connect` |
| `2026-06-24 18:07:18` | `cowrie.client.version` |
| `2026-06-24 18:07:18` | `cowrie.client.kex` |
| `2026-06-24 18:07:19` | `cowrie.login.success` |
| `2026-06-24 18:07:20` | `cowrie.session.params` |
| `2026-06-24 18:07:20` | `cowrie.command.input` |
| `2026-06-24 18:07:20` | `cowrie.log.closed` |
| `2026-06-24 18:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f53810cd78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:08 |
| **Last Seen** | 2026-06-24 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:08:00` | `cowrie.session.connect` |
| `2026-06-24 18:08:00` | `cowrie.client.version` |
| `2026-06-24 18:08:00` | `cowrie.client.kex` |
| `2026-06-24 18:08:01` | `cowrie.login.success` |
| `2026-06-24 18:08:01` | `cowrie.session.params` |
| `2026-06-24 18:08:01` | `cowrie.command.input` |
| `2026-06-24 18:08:02` | `cowrie.log.closed` |
| `2026-06-24 18:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee0dc97161fc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:08 |
| **Last Seen** | 2026-06-24 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:08:43` | `cowrie.session.connect` |
| `2026-06-24 18:08:43` | `cowrie.client.version` |
| `2026-06-24 18:08:43` | `cowrie.client.kex` |
| `2026-06-24 18:08:43` | `cowrie.login.success` |
| `2026-06-24 18:08:44` | `cowrie.session.params` |
| `2026-06-24 18:08:44` | `cowrie.command.input` |
| `2026-06-24 18:08:44` | `cowrie.log.closed` |
| `2026-06-24 18:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a2649a5d78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:09 |
| **Last Seen** | 2026-06-24 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:09:26` | `cowrie.session.connect` |
| `2026-06-24 18:09:26` | `cowrie.client.version` |
| `2026-06-24 18:09:26` | `cowrie.client.kex` |
| `2026-06-24 18:09:26` | `cowrie.login.success` |
| `2026-06-24 18:09:27` | `cowrie.session.params` |
| `2026-06-24 18:09:27` | `cowrie.command.input` |
| `2026-06-24 18:09:27` | `cowrie.log.closed` |
| `2026-06-24 18:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69a687b55e9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:10 |
| **Last Seen** | 2026-06-24 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:10:10` | `cowrie.session.connect` |
| `2026-06-24 18:10:10` | `cowrie.client.version` |
| `2026-06-24 18:10:10` | `cowrie.client.kex` |
| `2026-06-24 18:10:10` | `cowrie.login.success` |
| `2026-06-24 18:10:11` | `cowrie.session.params` |
| `2026-06-24 18:10:11` | `cowrie.command.input` |
| `2026-06-24 18:10:11` | `cowrie.log.closed` |
| `2026-06-24 18:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1b7ad2fb58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:10 |
| **Last Seen** | 2026-06-24 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:10:55` | `cowrie.session.connect` |
| `2026-06-24 18:10:55` | `cowrie.client.version` |
| `2026-06-24 18:10:55` | `cowrie.client.kex` |
| `2026-06-24 18:10:55` | `cowrie.login.success` |
| `2026-06-24 18:10:56` | `cowrie.session.params` |
| `2026-06-24 18:10:56` | `cowrie.command.input` |
| `2026-06-24 18:10:56` | `cowrie.log.closed` |
| `2026-06-24 18:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5eb891dbdc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:11 |
| **Last Seen** | 2026-06-24 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:11:40` | `cowrie.session.connect` |
| `2026-06-24 18:11:40` | `cowrie.client.version` |
| `2026-06-24 18:11:40` | `cowrie.client.kex` |
| `2026-06-24 18:11:40` | `cowrie.login.success` |
| `2026-06-24 18:11:41` | `cowrie.session.params` |
| `2026-06-24 18:11:41` | `cowrie.command.input` |
| `2026-06-24 18:11:41` | `cowrie.log.closed` |
| `2026-06-24 18:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30613813b1ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:12 |
| **Last Seen** | 2026-06-24 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:12:24` | `cowrie.session.connect` |
| `2026-06-24 18:12:24` | `cowrie.client.version` |
| `2026-06-24 18:12:24` | `cowrie.client.kex` |
| `2026-06-24 18:12:25` | `cowrie.login.success` |
| `2026-06-24 18:12:26` | `cowrie.session.params` |
| `2026-06-24 18:12:26` | `cowrie.command.input` |
| `2026-06-24 18:12:26` | `cowrie.log.closed` |
| `2026-06-24 18:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a83e5537fd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:13 |
| **Last Seen** | 2026-06-24 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:13:09` | `cowrie.session.connect` |
| `2026-06-24 18:13:09` | `cowrie.client.version` |
| `2026-06-24 18:13:09` | `cowrie.client.kex` |
| `2026-06-24 18:13:10` | `cowrie.login.success` |
| `2026-06-24 18:13:10` | `cowrie.session.params` |
| `2026-06-24 18:13:10` | `cowrie.command.input` |
| `2026-06-24 18:13:11` | `cowrie.log.closed` |
| `2026-06-24 18:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6c38b4f353

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:13 |
| **Last Seen** | 2026-06-24 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:13:52` | `cowrie.session.connect` |
| `2026-06-24 18:13:52` | `cowrie.client.version` |
| `2026-06-24 18:13:52` | `cowrie.client.kex` |
| `2026-06-24 18:13:53` | `cowrie.login.success` |
| `2026-06-24 18:13:54` | `cowrie.session.params` |
| `2026-06-24 18:13:54` | `cowrie.command.input` |
| `2026-06-24 18:13:54` | `cowrie.log.closed` |
| `2026-06-24 18:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd7ab4fb906

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:14 |
| **Last Seen** | 2026-06-24 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:14:37` | `cowrie.session.connect` |
| `2026-06-24 18:14:37` | `cowrie.client.version` |
| `2026-06-24 18:14:37` | `cowrie.client.kex` |
| `2026-06-24 18:14:38` | `cowrie.login.success` |
| `2026-06-24 18:14:39` | `cowrie.session.params` |
| `2026-06-24 18:14:39` | `cowrie.command.input` |
| `2026-06-24 18:14:39` | `cowrie.log.closed` |
| `2026-06-24 18:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4548fc307ec9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 18:14 |
| **Last Seen** | 2026-06-24 18:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:14:46` | `cowrie.session.connect` |
| `2026-06-24 18:14:48` | `cowrie.client.version` |
| `2026-06-24 18:14:48` | `cowrie.client.kex` |
| `2026-06-24 18:14:53` | `cowrie.login.success` |
| `2026-06-24 18:14:57` | `cowrie.session.params` |
| `2026-06-24 18:14:57` | `cowrie.command.input` |
| `2026-06-24 18:14:59` | `cowrie.log.closed` |
| `2026-06-24 18:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fccb82920609

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:15 |
| **Last Seen** | 2026-06-24 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:15:24` | `cowrie.session.connect` |
| `2026-06-24 18:15:24` | `cowrie.client.version` |
| `2026-06-24 18:15:24` | `cowrie.client.kex` |
| `2026-06-24 18:15:24` | `cowrie.login.success` |
| `2026-06-24 18:15:25` | `cowrie.session.params` |
| `2026-06-24 18:15:25` | `cowrie.command.input` |
| `2026-06-24 18:15:25` | `cowrie.log.closed` |
| `2026-06-24 18:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60249c97488d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:16 |
| **Last Seen** | 2026-06-24 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:16:11` | `cowrie.session.connect` |
| `2026-06-24 18:16:11` | `cowrie.client.version` |
| `2026-06-24 18:16:12` | `cowrie.client.kex` |
| `2026-06-24 18:16:12` | `cowrie.login.success` |
| `2026-06-24 18:16:13` | `cowrie.session.params` |
| `2026-06-24 18:16:13` | `cowrie.command.input` |
| `2026-06-24 18:16:13` | `cowrie.log.closed` |
| `2026-06-24 18:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a050971aae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:17 |
| **Last Seen** | 2026-06-24 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:17:00` | `cowrie.session.connect` |
| `2026-06-24 18:17:00` | `cowrie.client.version` |
| `2026-06-24 18:17:00` | `cowrie.client.kex` |
| `2026-06-24 18:17:00` | `cowrie.login.success` |
| `2026-06-24 18:17:01` | `cowrie.session.params` |
| `2026-06-24 18:17:01` | `cowrie.command.input` |
| `2026-06-24 18:17:01` | `cowrie.log.closed` |
| `2026-06-24 18:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a9162b23e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:17 |
| **Last Seen** | 2026-06-24 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:17:48` | `cowrie.session.connect` |
| `2026-06-24 18:17:48` | `cowrie.client.version` |
| `2026-06-24 18:17:48` | `cowrie.client.kex` |
| `2026-06-24 18:17:49` | `cowrie.login.success` |
| `2026-06-24 18:17:50` | `cowrie.session.params` |
| `2026-06-24 18:17:50` | `cowrie.command.input` |
| `2026-06-24 18:17:50` | `cowrie.log.closed` |
| `2026-06-24 18:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d31a1427644

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:18 |
| **Last Seen** | 2026-06-24 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:18:36` | `cowrie.session.connect` |
| `2026-06-24 18:18:36` | `cowrie.client.version` |
| `2026-06-24 18:18:36` | `cowrie.client.kex` |
| `2026-06-24 18:18:36` | `cowrie.login.success` |
| `2026-06-24 18:18:37` | `cowrie.session.params` |
| `2026-06-24 18:18:37` | `cowrie.command.input` |
| `2026-06-24 18:18:37` | `cowrie.log.closed` |
| `2026-06-24 18:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86351920ff4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:19 |
| **Last Seen** | 2026-06-24 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:19:24` | `cowrie.session.connect` |
| `2026-06-24 18:19:24` | `cowrie.client.version` |
| `2026-06-24 18:19:24` | `cowrie.client.kex` |
| `2026-06-24 18:19:25` | `cowrie.login.success` |
| `2026-06-24 18:19:25` | `cowrie.session.params` |
| `2026-06-24 18:19:25` | `cowrie.command.input` |
| `2026-06-24 18:19:25` | `cowrie.log.closed` |
| `2026-06-24 18:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08f268f87c50

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:20 |
| **Last Seen** | 2026-06-24 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:20:12` | `cowrie.session.connect` |
| `2026-06-24 18:20:12` | `cowrie.client.version` |
| `2026-06-24 18:20:12` | `cowrie.client.kex` |
| `2026-06-24 18:20:12` | `cowrie.login.success` |
| `2026-06-24 18:20:13` | `cowrie.session.params` |
| `2026-06-24 18:20:13` | `cowrie.command.input` |
| `2026-06-24 18:20:13` | `cowrie.log.closed` |
| `2026-06-24 18:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2833e77048

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:20 |
| **Last Seen** | 2026-06-24 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:20:59` | `cowrie.session.connect` |
| `2026-06-24 18:20:59` | `cowrie.client.version` |
| `2026-06-24 18:20:59` | `cowrie.client.kex` |
| `2026-06-24 18:21:00` | `cowrie.login.success` |
| `2026-06-24 18:21:00` | `cowrie.session.params` |
| `2026-06-24 18:21:00` | `cowrie.command.input` |
| `2026-06-24 18:21:01` | `cowrie.log.closed` |
| `2026-06-24 18:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d8a1b25f68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:21 |
| **Last Seen** | 2026-06-24 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:21:48` | `cowrie.session.connect` |
| `2026-06-24 18:21:48` | `cowrie.client.version` |
| `2026-06-24 18:21:48` | `cowrie.client.kex` |
| `2026-06-24 18:21:48` | `cowrie.login.success` |
| `2026-06-24 18:21:49` | `cowrie.session.params` |
| `2026-06-24 18:21:49` | `cowrie.command.input` |
| `2026-06-24 18:21:49` | `cowrie.log.closed` |
| `2026-06-24 18:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380e8adf9dbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:22 |
| **Last Seen** | 2026-06-24 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:22:36` | `cowrie.session.connect` |
| `2026-06-24 18:22:36` | `cowrie.client.version` |
| `2026-06-24 18:22:36` | `cowrie.client.kex` |
| `2026-06-24 18:22:36` | `cowrie.login.success` |
| `2026-06-24 18:22:37` | `cowrie.session.params` |
| `2026-06-24 18:22:37` | `cowrie.command.input` |
| `2026-06-24 18:22:37` | `cowrie.log.closed` |
| `2026-06-24 18:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c513b7dae8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 18:22 |
| **Last Seen** | 2026-06-24 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:22:39` | `cowrie.session.connect` |
| `2026-06-24 18:22:39` | `cowrie.client.version` |
| `2026-06-24 18:22:39` | `cowrie.client.kex` |
| `2026-06-24 18:22:39` | `cowrie.login.success` |
| `2026-06-24 18:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6730a1999cd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 18:22 |
| **Last Seen** | 2026-06-24 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:22:40` | `cowrie.session.connect` |
| `2026-06-24 18:22:40` | `cowrie.client.version` |
| `2026-06-24 18:22:40` | `cowrie.client.kex` |
| `2026-06-24 18:22:40` | `cowrie.login.success` |
| `2026-06-24 18:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883cdec217a8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 18:22 |
| **Last Seen** | 2026-06-24 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:22:48` | `cowrie.session.connect` |
| `2026-06-24 18:22:48` | `cowrie.client.version` |
| `2026-06-24 18:22:48` | `cowrie.client.kex` |
| `2026-06-24 18:22:48` | `cowrie.login.success` |
| `2026-06-24 18:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4204a3afcb15

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 18:22 |
| **Last Seen** | 2026-06-24 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:22:48` | `cowrie.session.connect` |
| `2026-06-24 18:22:48` | `cowrie.client.version` |
| `2026-06-24 18:22:48` | `cowrie.client.kex` |
| `2026-06-24 18:22:48` | `cowrie.login.success` |
| `2026-06-24 18:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7673d3644a9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:23 |
| **Last Seen** | 2026-06-24 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:23:25` | `cowrie.session.connect` |
| `2026-06-24 18:23:25` | `cowrie.client.version` |
| `2026-06-24 18:23:25` | `cowrie.client.kex` |
| `2026-06-24 18:23:26` | `cowrie.login.success` |
| `2026-06-24 18:23:26` | `cowrie.session.params` |
| `2026-06-24 18:23:26` | `cowrie.command.input` |
| `2026-06-24 18:23:26` | `cowrie.log.closed` |
| `2026-06-24 18:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4354afca4c48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:24 |
| **Last Seen** | 2026-06-24 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:24:16` | `cowrie.session.connect` |
| `2026-06-24 18:24:16` | `cowrie.client.version` |
| `2026-06-24 18:24:16` | `cowrie.client.kex` |
| `2026-06-24 18:24:16` | `cowrie.login.success` |
| `2026-06-24 18:24:17` | `cowrie.session.params` |
| `2026-06-24 18:24:17` | `cowrie.command.input` |
| `2026-06-24 18:24:17` | `cowrie.log.closed` |
| `2026-06-24 18:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce55fda09bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:25 |
| **Last Seen** | 2026-06-24 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:25:11` | `cowrie.session.connect` |
| `2026-06-24 18:25:11` | `cowrie.client.version` |
| `2026-06-24 18:25:11` | `cowrie.client.kex` |
| `2026-06-24 18:25:12` | `cowrie.login.success` |
| `2026-06-24 18:25:12` | `cowrie.session.params` |
| `2026-06-24 18:25:12` | `cowrie.command.input` |
| `2026-06-24 18:25:13` | `cowrie.log.closed` |
| `2026-06-24 18:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0ea75c853d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:26 |
| **Last Seen** | 2026-06-24 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:26:05` | `cowrie.session.connect` |
| `2026-06-24 18:26:05` | `cowrie.client.version` |
| `2026-06-24 18:26:05` | `cowrie.client.kex` |
| `2026-06-24 18:26:05` | `cowrie.login.success` |
| `2026-06-24 18:26:06` | `cowrie.session.params` |
| `2026-06-24 18:26:06` | `cowrie.command.input` |
| `2026-06-24 18:26:06` | `cowrie.log.closed` |
| `2026-06-24 18:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61fa558b99eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:26 |
| **Last Seen** | 2026-06-24 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:26:54` | `cowrie.session.connect` |
| `2026-06-24 18:26:54` | `cowrie.client.version` |
| `2026-06-24 18:26:54` | `cowrie.client.kex` |
| `2026-06-24 18:26:54` | `cowrie.login.success` |
| `2026-06-24 18:26:55` | `cowrie.session.params` |
| `2026-06-24 18:26:55` | `cowrie.command.input` |
| `2026-06-24 18:26:55` | `cowrie.log.closed` |
| `2026-06-24 18:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443a81eccb29

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:27 |
| **Last Seen** | 2026-06-24 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:27:43` | `cowrie.session.connect` |
| `2026-06-24 18:27:43` | `cowrie.client.version` |
| `2026-06-24 18:27:43` | `cowrie.client.kex` |
| `2026-06-24 18:27:43` | `cowrie.login.success` |
| `2026-06-24 18:27:44` | `cowrie.session.params` |
| `2026-06-24 18:27:44` | `cowrie.command.input` |
| `2026-06-24 18:27:44` | `cowrie.log.closed` |
| `2026-06-24 18:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b5f859d3e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:28 |
| **Last Seen** | 2026-06-24 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:28:32` | `cowrie.session.connect` |
| `2026-06-24 18:28:32` | `cowrie.client.version` |
| `2026-06-24 18:28:32` | `cowrie.client.kex` |
| `2026-06-24 18:28:33` | `cowrie.login.success` |
| `2026-06-24 18:28:33` | `cowrie.session.params` |
| `2026-06-24 18:28:33` | `cowrie.command.input` |
| `2026-06-24 18:28:34` | `cowrie.log.closed` |
| `2026-06-24 18:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177ecfbccfd3

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 18:28 |
| **Last Seen** | 2026-06-24 18:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:28:51` | `cowrie.session.connect` |
| `2026-06-24 18:28:52` | `cowrie.client.version` |
| `2026-06-24 18:28:52` | `cowrie.client.kex` |
| `2026-06-24 18:28:59` | `cowrie.login.success` |
| `2026-06-24 18:29:03` | `cowrie.session.params` |
| `2026-06-24 18:29:03` | `cowrie.command.input` |
| `2026-06-24 18:29:04` | `cowrie.log.closed` |
| `2026-06-24 18:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e146b4b6bc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:29 |
| **Last Seen** | 2026-06-24 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:29:22` | `cowrie.session.connect` |
| `2026-06-24 18:29:22` | `cowrie.client.version` |
| `2026-06-24 18:29:23` | `cowrie.client.kex` |
| `2026-06-24 18:29:23` | `cowrie.login.success` |
| `2026-06-24 18:29:24` | `cowrie.session.params` |
| `2026-06-24 18:29:24` | `cowrie.command.input` |
| `2026-06-24 18:29:24` | `cowrie.log.closed` |
| `2026-06-24 18:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e10be57ca066

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:30 |
| **Last Seen** | 2026-06-24 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:30:14` | `cowrie.session.connect` |
| `2026-06-24 18:30:14` | `cowrie.client.version` |
| `2026-06-24 18:30:14` | `cowrie.client.kex` |
| `2026-06-24 18:30:14` | `cowrie.login.success` |
| `2026-06-24 18:30:15` | `cowrie.session.params` |
| `2026-06-24 18:30:15` | `cowrie.command.input` |
| `2026-06-24 18:30:15` | `cowrie.log.closed` |
| `2026-06-24 18:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0378f3bcca94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:31 |
| **Last Seen** | 2026-06-24 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:31:05` | `cowrie.session.connect` |
| `2026-06-24 18:31:05` | `cowrie.client.version` |
| `2026-06-24 18:31:05` | `cowrie.client.kex` |
| `2026-06-24 18:31:05` | `cowrie.login.success` |
| `2026-06-24 18:31:06` | `cowrie.session.params` |
| `2026-06-24 18:31:06` | `cowrie.command.input` |
| `2026-06-24 18:31:06` | `cowrie.log.closed` |
| `2026-06-24 18:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c3d47f709b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:31 |
| **Last Seen** | 2026-06-24 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:31:56` | `cowrie.session.connect` |
| `2026-06-24 18:31:56` | `cowrie.client.version` |
| `2026-06-24 18:31:56` | `cowrie.client.kex` |
| `2026-06-24 18:31:56` | `cowrie.login.success` |
| `2026-06-24 18:31:57` | `cowrie.session.params` |
| `2026-06-24 18:31:57` | `cowrie.command.input` |
| `2026-06-24 18:31:57` | `cowrie.log.closed` |
| `2026-06-24 18:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151352a057a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:32 |
| **Last Seen** | 2026-06-24 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:32:46` | `cowrie.session.connect` |
| `2026-06-24 18:32:46` | `cowrie.client.version` |
| `2026-06-24 18:32:46` | `cowrie.client.kex` |
| `2026-06-24 18:32:46` | `cowrie.login.success` |
| `2026-06-24 18:32:47` | `cowrie.session.params` |
| `2026-06-24 18:32:47` | `cowrie.command.input` |
| `2026-06-24 18:32:47` | `cowrie.log.closed` |
| `2026-06-24 18:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770dc345c07d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:33 |
| **Last Seen** | 2026-06-24 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:33:35` | `cowrie.session.connect` |
| `2026-06-24 18:33:35` | `cowrie.client.version` |
| `2026-06-24 18:33:35` | `cowrie.client.kex` |
| `2026-06-24 18:33:35` | `cowrie.login.success` |
| `2026-06-24 18:33:36` | `cowrie.session.params` |
| `2026-06-24 18:33:36` | `cowrie.command.input` |
| `2026-06-24 18:33:36` | `cowrie.log.closed` |
| `2026-06-24 18:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeb7009602da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:34 |
| **Last Seen** | 2026-06-24 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:34:25` | `cowrie.session.connect` |
| `2026-06-24 18:34:25` | `cowrie.client.version` |
| `2026-06-24 18:34:25` | `cowrie.client.kex` |
| `2026-06-24 18:34:25` | `cowrie.login.success` |
| `2026-06-24 18:34:26` | `cowrie.session.params` |
| `2026-06-24 18:34:26` | `cowrie.command.input` |
| `2026-06-24 18:34:26` | `cowrie.log.closed` |
| `2026-06-24 18:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edba1bdeee34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:35 |
| **Last Seen** | 2026-06-24 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:35:16` | `cowrie.session.connect` |
| `2026-06-24 18:35:16` | `cowrie.client.version` |
| `2026-06-24 18:35:16` | `cowrie.client.kex` |
| `2026-06-24 18:35:16` | `cowrie.login.success` |
| `2026-06-24 18:35:17` | `cowrie.session.params` |
| `2026-06-24 18:35:17` | `cowrie.command.input` |
| `2026-06-24 18:35:17` | `cowrie.log.closed` |
| `2026-06-24 18:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb79f36bf134

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:36 |
| **Last Seen** | 2026-06-24 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:36:08` | `cowrie.session.connect` |
| `2026-06-24 18:36:08` | `cowrie.client.version` |
| `2026-06-24 18:36:08` | `cowrie.client.kex` |
| `2026-06-24 18:36:08` | `cowrie.login.success` |
| `2026-06-24 18:36:09` | `cowrie.session.params` |
| `2026-06-24 18:36:09` | `cowrie.command.input` |
| `2026-06-24 18:36:09` | `cowrie.log.closed` |
| `2026-06-24 18:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ff03a91002

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:37 |
| **Last Seen** | 2026-06-24 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:37:01` | `cowrie.session.connect` |
| `2026-06-24 18:37:01` | `cowrie.client.version` |
| `2026-06-24 18:37:01` | `cowrie.client.kex` |
| `2026-06-24 18:37:02` | `cowrie.login.success` |
| `2026-06-24 18:37:03` | `cowrie.session.params` |
| `2026-06-24 18:37:03` | `cowrie.command.input` |
| `2026-06-24 18:37:03` | `cowrie.log.closed` |
| `2026-06-24 18:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a7acbc40d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:37 |
| **Last Seen** | 2026-06-24 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:37:54` | `cowrie.session.connect` |
| `2026-06-24 18:37:54` | `cowrie.client.version` |
| `2026-06-24 18:37:54` | `cowrie.client.kex` |
| `2026-06-24 18:37:54` | `cowrie.login.success` |
| `2026-06-24 18:37:55` | `cowrie.session.params` |
| `2026-06-24 18:37:55` | `cowrie.command.input` |
| `2026-06-24 18:37:55` | `cowrie.log.closed` |
| `2026-06-24 18:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7ee73ad213

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:38 |
| **Last Seen** | 2026-06-24 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:38:45` | `cowrie.session.connect` |
| `2026-06-24 18:38:45` | `cowrie.client.version` |
| `2026-06-24 18:38:45` | `cowrie.client.kex` |
| `2026-06-24 18:38:46` | `cowrie.login.success` |
| `2026-06-24 18:38:46` | `cowrie.session.params` |
| `2026-06-24 18:38:46` | `cowrie.command.input` |
| `2026-06-24 18:38:46` | `cowrie.log.closed` |
| `2026-06-24 18:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff7514318e0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:39 |
| **Last Seen** | 2026-06-24 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:39:36` | `cowrie.session.connect` |
| `2026-06-24 18:39:36` | `cowrie.client.version` |
| `2026-06-24 18:39:37` | `cowrie.client.kex` |
| `2026-06-24 18:39:37` | `cowrie.login.success` |
| `2026-06-24 18:39:38` | `cowrie.session.params` |
| `2026-06-24 18:39:38` | `cowrie.command.input` |
| `2026-06-24 18:39:38` | `cowrie.log.closed` |
| `2026-06-24 18:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3385b3313d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:40 |
| **Last Seen** | 2026-06-24 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:40:28` | `cowrie.session.connect` |
| `2026-06-24 18:40:28` | `cowrie.client.version` |
| `2026-06-24 18:40:28` | `cowrie.client.kex` |
| `2026-06-24 18:40:28` | `cowrie.login.success` |
| `2026-06-24 18:40:29` | `cowrie.session.params` |
| `2026-06-24 18:40:29` | `cowrie.command.input` |
| `2026-06-24 18:40:29` | `cowrie.log.closed` |
| `2026-06-24 18:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756c6ef2f59c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:41 |
| **Last Seen** | 2026-06-24 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:41:22` | `cowrie.session.connect` |
| `2026-06-24 18:41:22` | `cowrie.client.version` |
| `2026-06-24 18:41:22` | `cowrie.client.kex` |
| `2026-06-24 18:41:22` | `cowrie.login.success` |
| `2026-06-24 18:41:23` | `cowrie.session.params` |
| `2026-06-24 18:41:23` | `cowrie.command.input` |
| `2026-06-24 18:41:23` | `cowrie.log.closed` |
| `2026-06-24 18:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6886caf711a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:42 |
| **Last Seen** | 2026-06-24 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:42:16` | `cowrie.session.connect` |
| `2026-06-24 18:42:16` | `cowrie.client.version` |
| `2026-06-24 18:42:16` | `cowrie.client.kex` |
| `2026-06-24 18:42:17` | `cowrie.login.success` |
| `2026-06-24 18:42:18` | `cowrie.session.params` |
| `2026-06-24 18:42:18` | `cowrie.command.input` |
| `2026-06-24 18:42:18` | `cowrie.log.closed` |
| `2026-06-24 18:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e849650183f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 18:43 |
| **Last Seen** | 2026-06-24 18:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:43:00` | `cowrie.session.connect` |
| `2026-06-24 18:43:02` | `cowrie.client.version` |
| `2026-06-24 18:43:02` | `cowrie.client.kex` |
| `2026-06-24 18:43:07` | `cowrie.login.success` |
| `2026-06-24 18:43:11` | `cowrie.session.params` |
| `2026-06-24 18:43:11` | `cowrie.command.input` |
| `2026-06-24 18:43:13` | `cowrie.log.closed` |
| `2026-06-24 18:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8a55f9600b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:43 |
| **Last Seen** | 2026-06-24 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:43:16` | `cowrie.session.connect` |
| `2026-06-24 18:43:16` | `cowrie.client.version` |
| `2026-06-24 18:43:16` | `cowrie.client.kex` |
| `2026-06-24 18:43:16` | `cowrie.login.success` |
| `2026-06-24 18:43:17` | `cowrie.session.params` |
| `2026-06-24 18:43:17` | `cowrie.command.input` |
| `2026-06-24 18:43:17` | `cowrie.log.closed` |
| `2026-06-24 18:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab9f2f9b529

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:44 |
| **Last Seen** | 2026-06-24 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:44:13` | `cowrie.session.connect` |
| `2026-06-24 18:44:13` | `cowrie.client.version` |
| `2026-06-24 18:44:13` | `cowrie.client.kex` |
| `2026-06-24 18:44:14` | `cowrie.login.success` |
| `2026-06-24 18:44:14` | `cowrie.session.params` |
| `2026-06-24 18:44:14` | `cowrie.command.input` |
| `2026-06-24 18:44:15` | `cowrie.log.closed` |
| `2026-06-24 18:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7bf9e40cf5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:45 |
| **Last Seen** | 2026-06-24 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:45:06` | `cowrie.session.connect` |
| `2026-06-24 18:45:06` | `cowrie.client.version` |
| `2026-06-24 18:45:06` | `cowrie.client.kex` |
| `2026-06-24 18:45:07` | `cowrie.login.success` |
| `2026-06-24 18:45:07` | `cowrie.session.params` |
| `2026-06-24 18:45:07` | `cowrie.command.input` |
| `2026-06-24 18:45:07` | `cowrie.log.closed` |
| `2026-06-24 18:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cebbc44c214

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:45 |
| **Last Seen** | 2026-06-24 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:45:58` | `cowrie.session.connect` |
| `2026-06-24 18:45:58` | `cowrie.client.version` |
| `2026-06-24 18:45:58` | `cowrie.client.kex` |
| `2026-06-24 18:45:58` | `cowrie.login.success` |
| `2026-06-24 18:45:59` | `cowrie.session.params` |
| `2026-06-24 18:45:59` | `cowrie.command.input` |
| `2026-06-24 18:45:59` | `cowrie.log.closed` |
| `2026-06-24 18:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a29c117f423

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:46 |
| **Last Seen** | 2026-06-24 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:46:50` | `cowrie.session.connect` |
| `2026-06-24 18:46:50` | `cowrie.client.version` |
| `2026-06-24 18:46:50` | `cowrie.client.kex` |
| `2026-06-24 18:46:50` | `cowrie.login.success` |
| `2026-06-24 18:46:51` | `cowrie.session.params` |
| `2026-06-24 18:46:51` | `cowrie.command.input` |
| `2026-06-24 18:46:51` | `cowrie.log.closed` |
| `2026-06-24 18:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56782c255934

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:47 |
| **Last Seen** | 2026-06-24 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:47:43` | `cowrie.session.connect` |
| `2026-06-24 18:47:43` | `cowrie.client.version` |
| `2026-06-24 18:47:43` | `cowrie.client.kex` |
| `2026-06-24 18:47:44` | `cowrie.login.success` |
| `2026-06-24 18:47:44` | `cowrie.session.params` |
| `2026-06-24 18:47:44` | `cowrie.command.input` |
| `2026-06-24 18:47:44` | `cowrie.log.closed` |
| `2026-06-24 18:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10713219497a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:48 |
| **Last Seen** | 2026-06-24 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:48:37` | `cowrie.session.connect` |
| `2026-06-24 18:48:37` | `cowrie.client.version` |
| `2026-06-24 18:48:37` | `cowrie.client.kex` |
| `2026-06-24 18:48:37` | `cowrie.login.success` |
| `2026-06-24 18:48:38` | `cowrie.session.params` |
| `2026-06-24 18:48:38` | `cowrie.command.input` |
| `2026-06-24 18:48:38` | `cowrie.log.closed` |
| `2026-06-24 18:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43644de68c91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:49 |
| **Last Seen** | 2026-06-24 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:49:31` | `cowrie.session.connect` |
| `2026-06-24 18:49:31` | `cowrie.client.version` |
| `2026-06-24 18:49:31` | `cowrie.client.kex` |
| `2026-06-24 18:49:32` | `cowrie.login.success` |
| `2026-06-24 18:49:32` | `cowrie.session.params` |
| `2026-06-24 18:49:32` | `cowrie.command.input` |
| `2026-06-24 18:49:32` | `cowrie.log.closed` |
| `2026-06-24 18:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b1fb9e86fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:50 |
| **Last Seen** | 2026-06-24 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:50:24` | `cowrie.session.connect` |
| `2026-06-24 18:50:24` | `cowrie.client.version` |
| `2026-06-24 18:50:25` | `cowrie.client.kex` |
| `2026-06-24 18:50:25` | `cowrie.login.success` |
| `2026-06-24 18:50:26` | `cowrie.session.params` |
| `2026-06-24 18:50:26` | `cowrie.command.input` |
| `2026-06-24 18:50:26` | `cowrie.log.closed` |
| `2026-06-24 18:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c27d8cda4b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:51 |
| **Last Seen** | 2026-06-24 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:51:18` | `cowrie.session.connect` |
| `2026-06-24 18:51:18` | `cowrie.client.version` |
| `2026-06-24 18:51:18` | `cowrie.client.kex` |
| `2026-06-24 18:51:18` | `cowrie.login.success` |
| `2026-06-24 18:51:19` | `cowrie.session.params` |
| `2026-06-24 18:51:19` | `cowrie.command.input` |
| `2026-06-24 18:51:19` | `cowrie.log.closed` |
| `2026-06-24 18:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3372f7acf346

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:52 |
| **Last Seen** | 2026-06-24 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:52:10` | `cowrie.session.connect` |
| `2026-06-24 18:52:10` | `cowrie.client.version` |
| `2026-06-24 18:52:10` | `cowrie.client.kex` |
| `2026-06-24 18:52:11` | `cowrie.login.success` |
| `2026-06-24 18:52:11` | `cowrie.session.params` |
| `2026-06-24 18:52:11` | `cowrie.command.input` |
| `2026-06-24 18:52:12` | `cowrie.log.closed` |
| `2026-06-24 18:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d189065f73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:53 |
| **Last Seen** | 2026-06-24 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:53:02` | `cowrie.session.connect` |
| `2026-06-24 18:53:02` | `cowrie.client.version` |
| `2026-06-24 18:53:02` | `cowrie.client.kex` |
| `2026-06-24 18:53:02` | `cowrie.login.success` |
| `2026-06-24 18:53:03` | `cowrie.session.params` |
| `2026-06-24 18:53:03` | `cowrie.command.input` |
| `2026-06-24 18:53:03` | `cowrie.log.closed` |
| `2026-06-24 18:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba7019aa91f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:53 |
| **Last Seen** | 2026-06-24 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:53:56` | `cowrie.session.connect` |
| `2026-06-24 18:53:56` | `cowrie.client.version` |
| `2026-06-24 18:53:56` | `cowrie.client.kex` |
| `2026-06-24 18:53:56` | `cowrie.login.success` |
| `2026-06-24 18:53:57` | `cowrie.session.params` |
| `2026-06-24 18:53:57` | `cowrie.command.input` |
| `2026-06-24 18:53:57` | `cowrie.log.closed` |
| `2026-06-24 18:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80736c2705e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:54 |
| **Last Seen** | 2026-06-24 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:54:51` | `cowrie.session.connect` |
| `2026-06-24 18:54:51` | `cowrie.client.version` |
| `2026-06-24 18:54:51` | `cowrie.client.kex` |
| `2026-06-24 18:54:51` | `cowrie.login.success` |
| `2026-06-24 18:54:52` | `cowrie.session.params` |
| `2026-06-24 18:54:52` | `cowrie.command.input` |
| `2026-06-24 18:54:52` | `cowrie.log.closed` |
| `2026-06-24 18:54:52` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **134** | 2026-06-24 16:55 | 2026-06-24 18:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **2** | 2026-06-24 17:12 | 2026-06-24 18:12 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-24 17:05 | 2026-06-24 18:32 | 2m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-06-24 17:15 | 2026-06-24 17:34 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-06-24 18:29 | 2026-06-24 18:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `27.153.157[.]138` | 1 | 2026-06-24 17:53 | 2026-06-24 17:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `42.203.111[.]50` | 1 | 2026-06-24 18:28 | 2026-06-24 18:28 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `27.153.157[.]138` | CN | Putian city a broadband | **100** ⚠️ | 12 |
| `137.131.9[.]65` | US | Oracle Corporation | **100** ⚠️ | 4 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `103.203.57[.]2` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `42.203.111[.]50` | CN | CHINANET Liaoning province network | **100** ⚠️ | 50 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `193.32.162[.]84` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 171 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 161 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 8 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 314 cases |
| Tool 34  | Credential Extractor        | ✅ 166 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (3.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 31 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 161 priority case(s) shown individually · 7 recon entry/entries in table (4 group(s) consolidating 140 session(s)).

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
_Report time: 2026-06-24T20:00:42Z_

